# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.observations import (
    radarobservation_get_params,
    radarobservation_list_params,
    radarobservation_count_params,
    radarobservation_tuple_params,
    radarobservation_create_params,
    radarobservation_create_bulk_params,
    radarobservation_unvalidated_publish_params,
)
from ....types.observations.radarobservation_get_response import RadarobservationGetResponse
from ....types.observations.radarobservation_list_response import RadarobservationListResponse
from ....types.observations.radarobservation_tuple_response import RadarobservationTupleResponse
from ....types.observations.radarobservation_queryhelp_response import RadarobservationQueryhelpResponse

__all__ = ["RadarobservationResource", "AsyncRadarobservationResource"]


class RadarobservationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> RadarobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RadarobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RadarobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return RadarobservationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_bias: float | NotGiven = NOT_GIVEN,
        azimuth_measured: bool | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        beam: float | NotGiven = NOT_GIVEN,
        declination: float | NotGiven = NOT_GIVEN,
        declination_measured: bool | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        doppler: float | NotGiven = NOT_GIVEN,
        doppler_unc: float | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_bias: float | NotGiven = NOT_GIVEN,
        elevation_measured: bool | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        ob_position: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        orthogonal_rcs: float | NotGiven = NOT_GIVEN,
        orthogonal_rcs_unc: float | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        ra_measured: bool | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        range_accel: float | NotGiven = NOT_GIVEN,
        range_accel_unc: float | NotGiven = NOT_GIVEN,
        range_bias: float | NotGiven = NOT_GIVEN,
        range_measured: bool | NotGiven = NOT_GIVEN,
        range_rate: float | NotGiven = NOT_GIVEN,
        range_rate_measured: bool | NotGiven = NOT_GIVEN,
        range_rate_unc: float | NotGiven = NOT_GIVEN,
        range_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_unc: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sen_reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        timing_bias: float | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        tracking_state: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        x: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        y: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        z: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single radar observation as a POST body and ingest
        into the database. This operation is not intended to be used for automated feeds
        into UDL. Data providers should contact the UDL team for specific role
        assignments and for instructions on setting up a permanent feed through an
        alternate mechanism.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          azimuth: azimuth angle in degrees and topocentric frame.

          azimuth_bias: Sensor azimuth angle bias in degrees.

          azimuth_measured: Optional flag indicating whether the azimuth value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          azimuth_rate: Rate of change of the line of sight azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the line of sight azimuth angle measurement, in
              degrees.

          beam: ID of the beam that produced this observation.

          declination: Line of sight declination angle in degrees and J2000 coordinate frame.

          declination_measured: Optional flag indicating whether the declination value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          doppler: Corrected doppler measurement in meters per second.

          doppler_unc: One sigma uncertainty in the corrected doppler measurement, in meters/second.

          elevation: Line of sight elevation in degrees and topocentric frame.

          elevation_bias: Sensor elevation bias in degrees.

          elevation_measured: Optional flag indicating whether the elevation value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          elevation_rate: Rate of change of the line of sight elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the line of sight elevation angle measurement, in
              degrees.

          id_sensor: Unique identifier of the reporting sensor.

          ob_position: The position of this observation within a track (FENCE, FIRST, IN, LAST,
              SINGLE). This identifier is optional and, if null, no assumption should be made
              regarding whether other observations may or may not exist to compose a track.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          orthogonal_rcs: Radar cross section in meters squared for orthogonal polarization.

          orthogonal_rcs_unc: one sigma uncertainty in orthogonal polarization Radar Cross Section, in
              meters^2.

          ra: Line of sight right ascension in degrees and J2000 coordinate frame.

          ra_measured: Optional flag indicating whether the ra value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range: Target range in km.

          range_accel: Range accelaration in km/s2.

          range_accel_unc: One sigma uncertainty in the range acceleration measurement, in
              kilometers/(second^2).

          range_bias: Sensor range bias in km.

          range_measured: Optional flag indicating whether the range value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range_rate: Rate of change of the line of sight range in km/sec.

          range_rate_measured: Optional flag indicating whether the rangeRate value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          range_rate_unc: One sigma uncertainty in the range rate measurement, in kilometers/second.

          range_unc: One sigma uncertainty in the range measurement, in kilometers.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rcs: Radar cross section in meters squared for polarization principal.

          rcs_unc: one sigma uncertainty in principal polarization Radar Cross Section, in
              meters^2.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          sen_reference_frame: The reference frame of the observing sensor state. If the senReferenceFrame is
              null it is assumed to be J2000.

          senx: Sensor x position in km at obTime (if mobile/onorbit) in the specified
              senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.

          seny: Sensor y position in km at obTime (if mobile/onorbit) in the specified
              senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.

          senz: Sensor z position in km at obTime (if mobile/onorbit) in the specified
              senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.

          snr: Signal to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          timing_bias: Sensor timing bias in seconds.

          track_id: Optional identifier of the track to which this observation belongs.

          tracking_state: The beam type (or tracking state) in use at the time of collection of this
              observation. Values include:

              INIT ACQ WITH INIT VALUES: Initial acquisition based on predefined initial
              values such as position, velocity, or other specific parameters.

              INIT ACQ: Initial acquisition when no prior information or initial values such
              as position or velocity are available.

              TRACKING SINGLE BEAM: Continuously tracks and monitors a single target using one
              specific radar beam.

              TRACKING SEQUENTIAL ROVING: Sequentially tracks different targets or areas by
              "roving" from one sector to the next in a systematic order.

              SELF ACQ WITH INIT VALUES: Autonomously acquires targets using predefined
              starting parameters or initial values.

              SELF ACQ: Automatically detects and locks onto targets without the need for
              predefined initial settings.

              NON-TRACKING: Non-tracking.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          x: X position of target in km in J2000 coordinate frame.

          xvel: X velocity of target in km/sec in J2000 coordinate frame.

          y: Y position of target in km in J2000 coordinate frame.

          yvel: Y velocity of target in km/sec in J2000 coordinate frame.

          z: Z position of target in km in J2000 coordinate frame.

          zvel: Z velocity of target in km/sec in J2000 coordinate frame.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/radarobservation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "azimuth": azimuth,
                    "azimuth_bias": azimuth_bias,
                    "azimuth_measured": azimuth_measured,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "beam": beam,
                    "declination": declination,
                    "declination_measured": declination_measured,
                    "descriptor": descriptor,
                    "doppler": doppler,
                    "doppler_unc": doppler_unc,
                    "elevation": elevation,
                    "elevation_bias": elevation_bias,
                    "elevation_measured": elevation_measured,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "id_sensor": id_sensor,
                    "ob_position": ob_position,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "orthogonal_rcs": orthogonal_rcs,
                    "orthogonal_rcs_unc": orthogonal_rcs_unc,
                    "ra": ra,
                    "ra_measured": ra_measured,
                    "range": range,
                    "range_accel": range_accel,
                    "range_accel_unc": range_accel_unc,
                    "range_bias": range_bias,
                    "range_measured": range_measured,
                    "range_rate": range_rate,
                    "range_rate_measured": range_rate_measured,
                    "range_rate_unc": range_rate_unc,
                    "range_unc": range_unc,
                    "raw_file_uri": raw_file_uri,
                    "rcs": rcs,
                    "rcs_unc": rcs_unc,
                    "sat_no": sat_no,
                    "sen_reference_frame": sen_reference_frame,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "snr": snr,
                    "tags": tags,
                    "task_id": task_id,
                    "timing_bias": timing_bias,
                    "track_id": track_id,
                    "tracking_state": tracking_state,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "x": x,
                    "xvel": xvel,
                    "y": y,
                    "yvel": yvel,
                    "z": z,
                    "zvel": zvel,
                },
                radarobservation_create_params.RadarobservationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[RadarobservationListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/radarobservation",
            page=SyncOffsetPage[RadarobservationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_list_params.RadarobservationListParams,
                ),
            ),
            model=RadarobservationListResponse,
        )

    def count(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/radarobservation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_count_params.RadarobservationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[radarobservation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of radar
        observations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/radarobservation/createBulk",
            body=maybe_transform(body, Iterable[radarobservation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RadarobservationGetResponse:
        """
        Service operation to get a single radar observations by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/radarobservation/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_get_params.RadarobservationGetParams,
                ),
            ),
            cast_to=RadarobservationGetResponse,
        )

    def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RadarobservationQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/radarobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RadarobservationQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RadarobservationTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/radarobservation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_tuple_params.RadarobservationTupleParams,
                ),
            ),
            cast_to=RadarobservationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[radarobservation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple radar observations as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-radar",
            body=maybe_transform(body, Iterable[radarobservation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRadarobservationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRadarobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRadarobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRadarobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncRadarobservationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_bias: float | NotGiven = NOT_GIVEN,
        azimuth_measured: bool | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        beam: float | NotGiven = NOT_GIVEN,
        declination: float | NotGiven = NOT_GIVEN,
        declination_measured: bool | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        doppler: float | NotGiven = NOT_GIVEN,
        doppler_unc: float | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_bias: float | NotGiven = NOT_GIVEN,
        elevation_measured: bool | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        ob_position: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        orthogonal_rcs: float | NotGiven = NOT_GIVEN,
        orthogonal_rcs_unc: float | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        ra_measured: bool | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        range_accel: float | NotGiven = NOT_GIVEN,
        range_accel_unc: float | NotGiven = NOT_GIVEN,
        range_bias: float | NotGiven = NOT_GIVEN,
        range_measured: bool | NotGiven = NOT_GIVEN,
        range_rate: float | NotGiven = NOT_GIVEN,
        range_rate_measured: bool | NotGiven = NOT_GIVEN,
        range_rate_unc: float | NotGiven = NOT_GIVEN,
        range_unc: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_unc: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sen_reference_frame: Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"] | NotGiven = NOT_GIVEN,
        senx: float | NotGiven = NOT_GIVEN,
        seny: float | NotGiven = NOT_GIVEN,
        senz: float | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        timing_bias: float | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        tracking_state: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        x: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        y: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        z: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single radar observation as a POST body and ingest
        into the database. This operation is not intended to be used for automated feeds
        into UDL. Data providers should contact the UDL team for specific role
        assignments and for instructions on setting up a permanent feed through an
        alternate mechanism.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          azimuth: azimuth angle in degrees and topocentric frame.

          azimuth_bias: Sensor azimuth angle bias in degrees.

          azimuth_measured: Optional flag indicating whether the azimuth value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          azimuth_rate: Rate of change of the line of sight azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the line of sight azimuth angle measurement, in
              degrees.

          beam: ID of the beam that produced this observation.

          declination: Line of sight declination angle in degrees and J2000 coordinate frame.

          declination_measured: Optional flag indicating whether the declination value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          doppler: Corrected doppler measurement in meters per second.

          doppler_unc: One sigma uncertainty in the corrected doppler measurement, in meters/second.

          elevation: Line of sight elevation in degrees and topocentric frame.

          elevation_bias: Sensor elevation bias in degrees.

          elevation_measured: Optional flag indicating whether the elevation value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          elevation_rate: Rate of change of the line of sight elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the line of sight elevation angle measurement, in
              degrees.

          id_sensor: Unique identifier of the reporting sensor.

          ob_position: The position of this observation within a track (FENCE, FIRST, IN, LAST,
              SINGLE). This identifier is optional and, if null, no assumption should be made
              regarding whether other observations may or may not exist to compose a track.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by observation source to indicate the target
              onorbit object of this observation. This may be an internal identifier and not
              necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by observation source to indicate the sensor
              identifier which produced this observation. This may be an internal identifier
              and not necessarily a valid sensor ID.

          orthogonal_rcs: Radar cross section in meters squared for orthogonal polarization.

          orthogonal_rcs_unc: one sigma uncertainty in orthogonal polarization Radar Cross Section, in
              meters^2.

          ra: Line of sight right ascension in degrees and J2000 coordinate frame.

          ra_measured: Optional flag indicating whether the ra value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range: Target range in km.

          range_accel: Range accelaration in km/s2.

          range_accel_unc: One sigma uncertainty in the range acceleration measurement, in
              kilometers/(second^2).

          range_bias: Sensor range bias in km.

          range_measured: Optional flag indicating whether the range value is measured (true) or computed
              (false). If null, consumers may consult the data provider for information
              regarding whether the corresponding value is computed or measured.

          range_rate: Rate of change of the line of sight range in km/sec.

          range_rate_measured: Optional flag indicating whether the rangeRate value is measured (true) or
              computed (false). If null, consumers may consult the data provider for
              information regarding whether the corresponding value is computed or measured.

          range_rate_unc: One sigma uncertainty in the range rate measurement, in kilometers/second.

          range_unc: One sigma uncertainty in the range measurement, in kilometers.

          raw_file_uri: Optional URI location in the document repository of the raw file parsed by the
              system to produce this record. To download the raw file, prepend
              https://udl-hostname/scs/download?id= to this value.

          rcs: Radar cross section in meters squared for polarization principal.

          rcs_unc: one sigma uncertainty in principal polarization Radar Cross Section, in
              meters^2.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          sen_reference_frame: The reference frame of the observing sensor state. If the senReferenceFrame is
              null it is assumed to be J2000.

          senx: Sensor x position in km at obTime (if mobile/onorbit) in the specified
              senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.

          seny: Sensor y position in km at obTime (if mobile/onorbit) in the specified
              senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.

          senz: Sensor z position in km at obTime (if mobile/onorbit) in the specified
              senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.

          snr: Signal to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          timing_bias: Sensor timing bias in seconds.

          track_id: Optional identifier of the track to which this observation belongs.

          tracking_state: The beam type (or tracking state) in use at the time of collection of this
              observation. Values include:

              INIT ACQ WITH INIT VALUES: Initial acquisition based on predefined initial
              values such as position, velocity, or other specific parameters.

              INIT ACQ: Initial acquisition when no prior information or initial values such
              as position or velocity are available.

              TRACKING SINGLE BEAM: Continuously tracks and monitors a single target using one
              specific radar beam.

              TRACKING SEQUENTIAL ROVING: Sequentially tracks different targets or areas by
              "roving" from one sector to the next in a systematic order.

              SELF ACQ WITH INIT VALUES: Autonomously acquires targets using predefined
              starting parameters or initial values.

              SELF ACQ: Automatically detects and locks onto targets without the need for
              predefined initial settings.

              NON-TRACKING: Non-tracking.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          x: X position of target in km in J2000 coordinate frame.

          xvel: X velocity of target in km/sec in J2000 coordinate frame.

          y: Y position of target in km in J2000 coordinate frame.

          yvel: Y velocity of target in km/sec in J2000 coordinate frame.

          z: Z position of target in km in J2000 coordinate frame.

          zvel: Z velocity of target in km/sec in J2000 coordinate frame.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/radarobservation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "azimuth": azimuth,
                    "azimuth_bias": azimuth_bias,
                    "azimuth_measured": azimuth_measured,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "beam": beam,
                    "declination": declination,
                    "declination_measured": declination_measured,
                    "descriptor": descriptor,
                    "doppler": doppler,
                    "doppler_unc": doppler_unc,
                    "elevation": elevation,
                    "elevation_bias": elevation_bias,
                    "elevation_measured": elevation_measured,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "id_sensor": id_sensor,
                    "ob_position": ob_position,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "orthogonal_rcs": orthogonal_rcs,
                    "orthogonal_rcs_unc": orthogonal_rcs_unc,
                    "ra": ra,
                    "ra_measured": ra_measured,
                    "range": range,
                    "range_accel": range_accel,
                    "range_accel_unc": range_accel_unc,
                    "range_bias": range_bias,
                    "range_measured": range_measured,
                    "range_rate": range_rate,
                    "range_rate_measured": range_rate_measured,
                    "range_rate_unc": range_rate_unc,
                    "range_unc": range_unc,
                    "raw_file_uri": raw_file_uri,
                    "rcs": rcs,
                    "rcs_unc": rcs_unc,
                    "sat_no": sat_no,
                    "sen_reference_frame": sen_reference_frame,
                    "senx": senx,
                    "seny": seny,
                    "senz": senz,
                    "snr": snr,
                    "tags": tags,
                    "task_id": task_id,
                    "timing_bias": timing_bias,
                    "track_id": track_id,
                    "tracking_state": tracking_state,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "x": x,
                    "xvel": xvel,
                    "y": y,
                    "yvel": yvel,
                    "z": z,
                    "zvel": zvel,
                },
                radarobservation_create_params.RadarobservationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RadarobservationListResponse, AsyncOffsetPage[RadarobservationListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/radarobservation",
            page=AsyncOffsetPage[RadarobservationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_list_params.RadarobservationListParams,
                ),
            ),
            model=RadarobservationListResponse,
        )

    async def count(
        self,
        *,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/radarobservation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_count_params.RadarobservationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[radarobservation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of radar
        observations as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/radarobservation/createBulk",
            body=await async_maybe_transform(body, Iterable[radarobservation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RadarobservationGetResponse:
        """
        Service operation to get a single radar observations by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/radarobservation/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_get_params.RadarobservationGetParams,
                ),
            ),
            cast_to=RadarobservationGetResponse,
        )

    async def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RadarobservationQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/radarobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RadarobservationQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        ob_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RadarobservationTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          ob_time: Ob detection time in ISO 8601 UTC with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/radarobservation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "ob_time": ob_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    radarobservation_tuple_params.RadarobservationTupleParams,
                ),
            ),
            cast_to=RadarobservationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[radarobservation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple radar observations as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-radar",
            body=await async_maybe_transform(body, Iterable[radarobservation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RadarobservationResourceWithRawResponse:
    def __init__(self, radarobservation: RadarobservationResource) -> None:
        self._radarobservation = radarobservation

        self.create = to_raw_response_wrapper(
            radarobservation.create,
        )
        self.list = to_raw_response_wrapper(
            radarobservation.list,
        )
        self.count = to_raw_response_wrapper(
            radarobservation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            radarobservation.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            radarobservation.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            radarobservation.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            radarobservation.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            radarobservation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._radarobservation.history)


class AsyncRadarobservationResourceWithRawResponse:
    def __init__(self, radarobservation: AsyncRadarobservationResource) -> None:
        self._radarobservation = radarobservation

        self.create = async_to_raw_response_wrapper(
            radarobservation.create,
        )
        self.list = async_to_raw_response_wrapper(
            radarobservation.list,
        )
        self.count = async_to_raw_response_wrapper(
            radarobservation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            radarobservation.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            radarobservation.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            radarobservation.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            radarobservation.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            radarobservation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._radarobservation.history)


class RadarobservationResourceWithStreamingResponse:
    def __init__(self, radarobservation: RadarobservationResource) -> None:
        self._radarobservation = radarobservation

        self.create = to_streamed_response_wrapper(
            radarobservation.create,
        )
        self.list = to_streamed_response_wrapper(
            radarobservation.list,
        )
        self.count = to_streamed_response_wrapper(
            radarobservation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            radarobservation.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            radarobservation.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            radarobservation.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            radarobservation.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            radarobservation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._radarobservation.history)


class AsyncRadarobservationResourceWithStreamingResponse:
    def __init__(self, radarobservation: AsyncRadarobservationResource) -> None:
        self._radarobservation = radarobservation

        self.create = async_to_streamed_response_wrapper(
            radarobservation.create,
        )
        self.list = async_to_streamed_response_wrapper(
            radarobservation.list,
        )
        self.count = async_to_streamed_response_wrapper(
            radarobservation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            radarobservation.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            radarobservation.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            radarobservation.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            radarobservation.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            radarobservation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._radarobservation.history)
