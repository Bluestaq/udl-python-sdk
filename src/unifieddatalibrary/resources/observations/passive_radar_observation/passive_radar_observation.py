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
    passive_radar_observation_get_params,
    passive_radar_observation_list_params,
    passive_radar_observation_count_params,
    passive_radar_observation_tuple_params,
    passive_radar_observation_create_params,
    passive_radar_observation_create_bulk_params,
    passive_radar_observation_file_create_params,
)
from ....types.observations.passive_radar_observation_get_response import PassiveRadarObservationGetResponse
from ....types.observations.passive_radar_observation_list_response import PassiveRadarObservationListResponse
from ....types.observations.passive_radar_observation_tuple_response import PassiveRadarObservationTupleResponse

__all__ = ["PassiveRadarObservationResource", "AsyncPassiveRadarObservationResource"]


class PassiveRadarObservationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> PassiveRadarObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PassiveRadarObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PassiveRadarObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return PassiveRadarObservationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        accel: float | NotGiven = NOT_GIVEN,
        accel_unc: float | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_bias: float | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        bistatic_range: float | NotGiven = NOT_GIVEN,
        bistatic_range_accel: float | NotGiven = NOT_GIVEN,
        bistatic_range_accel_unc: float | NotGiven = NOT_GIVEN,
        bistatic_range_bias: float | NotGiven = NOT_GIVEN,
        bistatic_range_rate: float | NotGiven = NOT_GIVEN,
        bistatic_range_rate_unc: float | NotGiven = NOT_GIVEN,
        bistatic_range_unc: float | NotGiven = NOT_GIVEN,
        coning: float | NotGiven = NOT_GIVEN,
        coning_unc: float | NotGiven = NOT_GIVEN,
        declination: float | NotGiven = NOT_GIVEN,
        delay: float | NotGiven = NOT_GIVEN,
        delay_bias: float | NotGiven = NOT_GIVEN,
        delay_unc: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        doppler: float | NotGiven = NOT_GIVEN,
        doppler_unc: float | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_bias: float | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        ext_observation_id: str | NotGiven = NOT_GIVEN,
        id_rf_emitter: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_sensor_ref_receiver: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        ob_position: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        orthogonal_rcs: float | NotGiven = NOT_GIVEN,
        orthogonal_rcs_unc: float | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_unc: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        timing_bias: float | NotGiven = NOT_GIVEN,
        tof: float | NotGiven = NOT_GIVEN,
        tof_bias: float | NotGiven = NOT_GIVEN,
        tof_unc: float | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single PassiveRadarObservation as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          accel: The target Acceleration measurement in kilometers/sec^2 for this observation.

          accel_unc: The target Acceleration uncertainty measurement in kilometers/sec^2 for this
              observation.

          alt: The target altitude relative to WGS-84 ellipsoid, in kilometers for this
              observation.

          azimuth: Line of sight azimuth angle in degrees and topocentric frame.

          azimuth_bias: Sensor azimuth angle bias in degrees.

          azimuth_rate: Rate of change of the line of sight azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the line of sight azimuth angle measurement, in
              degrees.

          bistatic_range: Target bistatic path distance in kilometers. This is the
              transmitter-to-target-to-surveillance site distance.

          bistatic_range_accel: Bistatic range acceleration in kilometers/sec^2.

          bistatic_range_accel_unc: One sigma uncertainty in the bistatic range acceleration measurement, in
              kilometers/sec^2.

          bistatic_range_bias: Sensor bistatic range bias in kilometers.

          bistatic_range_rate: Rate of change of the bistatic path in kilometers/sec.

          bistatic_range_rate_unc: One sigma uncertainty in rate of change of the bistatic path in kilometers/sec.

          bistatic_range_unc: One sigma uncertainty in bistatic range in kilometers.

          coning: Coning angle in degrees.

          coning_unc: One sigma uncertainty in the coning angle measurement, in degrees.

          declination: Line of sight declination angle in degrees and J2000 coordinate frame.

          delay: The time difference, in seconds, between the signal collected at the
              surveillance site (after being reflected from the target) and the reference site
              (direct path line-of-sight signal).

          delay_bias: Delay bias in seconds.

          delay_unc: One sigma uncertainty in the delay measurement, in seconds.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          doppler: Doppler measurement in hertz.

          doppler_unc: One sigma uncertainty in the Doppler measurement in hertz.

          elevation: Line of sight elevation in degrees and topocentric frame.

          elevation_bias: Sensor elevation bias in degrees.

          elevation_rate: Rate of change of the line of sight elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the line of sight elevation angle measurement, in
              degrees.

          ext_observation_id: Optional external observation identifier provided by the source.

          id_rf_emitter: Unique identifier of the transmitter. This ID can be used to obtain additional
              information on an RFEmitter using the 'get by ID' operation (e.g.
              /udl/rfemitter/{id}). For example, the RFEmitter with idRFEmitter = abc would be
              queried as /udl/rfemitter/abc.

          id_sensor: Unique identifier of the reporting surveillance sensor. This ID can be used to
              obtain additional information on a sensor using the 'get by ID' operation (e.g.
              /udl/sensor/{id}). For example, the sensor with idSensor = abc would be queried
              as /udl/sensor/abc.

          id_sensor_ref_receiver: Unique identifier of the reference receiver sensor. This ID can be used to
              obtain additional information on a sensor using the 'get by ID' operation (e.g.
              /udl/sensor/{id}). For example, the sensor with idSensor = abc would be queried
              as /udl/sensor/abc.

          lat: WGS-84 target latitude sub-point at observation time (obTime), represented as
              -90 to 90 degrees (negative values south of equator).

          lon: WGS-84 target longitude sub-point at observation time (obTime), represented as
              -180 to 180 degrees (negative values west of Prime Meridian).

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

          orthogonal_rcs_unc: One sigma uncertainty in orthogonal polarization Radar Cross Section, in
              meters^2.

          ra: Line of sight right ascension in degrees and J2000 coordinate frame.

          rcs: Radar cross section in meters squared for polarization principal.

          rcs_unc: One sigma uncertainty in principal polarization Radar Cross Section, in
              meters^2.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          snr: Signal to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          timing_bias: Sensor timing bias in seconds.

          tof: Time of flight (TOF) in seconds. This is the calculated propagation time from
              transmitter-to-target-to-surveillance site.

          tof_bias: The Time of Flight (TOF) bias in seconds.

          tof_unc: One sigma uncertainty in time of flight in seconds.

          track_id: Unique identifier of a track that represents a tracklet for this observation.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          xvel: X velocity of target in kilometers/sec in J2000 coordinate frame.

          yvel: Y velocity of target in kilometers/sec in J2000 coordinate frame.

          zvel: Z velocity of target in kilometers/sec in J2000 coordinate frame.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/passiveradarobservation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "accel": accel,
                    "accel_unc": accel_unc,
                    "alt": alt,
                    "azimuth": azimuth,
                    "azimuth_bias": azimuth_bias,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "bistatic_range": bistatic_range,
                    "bistatic_range_accel": bistatic_range_accel,
                    "bistatic_range_accel_unc": bistatic_range_accel_unc,
                    "bistatic_range_bias": bistatic_range_bias,
                    "bistatic_range_rate": bistatic_range_rate,
                    "bistatic_range_rate_unc": bistatic_range_rate_unc,
                    "bistatic_range_unc": bistatic_range_unc,
                    "coning": coning,
                    "coning_unc": coning_unc,
                    "declination": declination,
                    "delay": delay,
                    "delay_bias": delay_bias,
                    "delay_unc": delay_unc,
                    "descriptor": descriptor,
                    "doppler": doppler,
                    "doppler_unc": doppler_unc,
                    "elevation": elevation,
                    "elevation_bias": elevation_bias,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "ext_observation_id": ext_observation_id,
                    "id_rf_emitter": id_rf_emitter,
                    "id_sensor": id_sensor,
                    "id_sensor_ref_receiver": id_sensor_ref_receiver,
                    "lat": lat,
                    "lon": lon,
                    "ob_position": ob_position,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "orthogonal_rcs": orthogonal_rcs,
                    "orthogonal_rcs_unc": orthogonal_rcs_unc,
                    "ra": ra,
                    "rcs": rcs,
                    "rcs_unc": rcs_unc,
                    "sat_no": sat_no,
                    "snr": snr,
                    "tags": tags,
                    "task_id": task_id,
                    "timing_bias": timing_bias,
                    "tof": tof,
                    "tof_bias": tof_bias,
                    "tof_unc": tof_unc,
                    "track_id": track_id,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "xvel": xvel,
                    "yvel": yvel,
                    "zvel": zvel,
                },
                passive_radar_observation_create_params.PassiveRadarObservationCreateParams,
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
    ) -> SyncOffsetPage[PassiveRadarObservationListResponse]:
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
            "/udl/passiveradarobservation",
            page=SyncOffsetPage[PassiveRadarObservationListResponse],
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
                    passive_radar_observation_list_params.PassiveRadarObservationListParams,
                ),
            ),
            model=PassiveRadarObservationListResponse,
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
            "/udl/passiveradarobservation/count",
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
                    passive_radar_observation_count_params.PassiveRadarObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[passive_radar_observation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        PassiveRadarObservation records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/passiveradarobservation/createBulk",
            body=maybe_transform(body, Iterable[passive_radar_observation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def file_create(
        self,
        *,
        body: Iterable[passive_radar_observation_file_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple PassiveRadarObservation records as a POST
        body and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-passiveradar",
            body=maybe_transform(body, Iterable[passive_radar_observation_file_create_params.Body]),
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
    ) -> PassiveRadarObservationGetResponse:
        """
        Service operation to get a single PassiveRadarObservation record by its unique
        ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/passiveradarobservation/{id}",
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
                    passive_radar_observation_get_params.PassiveRadarObservationGetParams,
                ),
            ),
            cast_to=PassiveRadarObservationGetResponse,
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/passiveradarobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> PassiveRadarObservationTupleResponse:
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
            "/udl/passiveradarobservation/tuple",
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
                    passive_radar_observation_tuple_params.PassiveRadarObservationTupleParams,
                ),
            ),
            cast_to=PassiveRadarObservationTupleResponse,
        )


class AsyncPassiveRadarObservationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPassiveRadarObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPassiveRadarObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPassiveRadarObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncPassiveRadarObservationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        ob_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        accel: float | NotGiven = NOT_GIVEN,
        accel_unc: float | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        azimuth: float | NotGiven = NOT_GIVEN,
        azimuth_bias: float | NotGiven = NOT_GIVEN,
        azimuth_rate: float | NotGiven = NOT_GIVEN,
        azimuth_unc: float | NotGiven = NOT_GIVEN,
        bistatic_range: float | NotGiven = NOT_GIVEN,
        bistatic_range_accel: float | NotGiven = NOT_GIVEN,
        bistatic_range_accel_unc: float | NotGiven = NOT_GIVEN,
        bistatic_range_bias: float | NotGiven = NOT_GIVEN,
        bistatic_range_rate: float | NotGiven = NOT_GIVEN,
        bistatic_range_rate_unc: float | NotGiven = NOT_GIVEN,
        bistatic_range_unc: float | NotGiven = NOT_GIVEN,
        coning: float | NotGiven = NOT_GIVEN,
        coning_unc: float | NotGiven = NOT_GIVEN,
        declination: float | NotGiven = NOT_GIVEN,
        delay: float | NotGiven = NOT_GIVEN,
        delay_bias: float | NotGiven = NOT_GIVEN,
        delay_unc: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        doppler: float | NotGiven = NOT_GIVEN,
        doppler_unc: float | NotGiven = NOT_GIVEN,
        elevation: float | NotGiven = NOT_GIVEN,
        elevation_bias: float | NotGiven = NOT_GIVEN,
        elevation_rate: float | NotGiven = NOT_GIVEN,
        elevation_unc: float | NotGiven = NOT_GIVEN,
        ext_observation_id: str | NotGiven = NOT_GIVEN,
        id_rf_emitter: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_sensor_ref_receiver: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        ob_position: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        orthogonal_rcs: float | NotGiven = NOT_GIVEN,
        orthogonal_rcs_unc: float | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_unc: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        timing_bias: float | NotGiven = NOT_GIVEN,
        tof: float | NotGiven = NOT_GIVEN,
        tof_bias: float | NotGiven = NOT_GIVEN,
        tof_unc: float | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single PassiveRadarObservation as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          accel: The target Acceleration measurement in kilometers/sec^2 for this observation.

          accel_unc: The target Acceleration uncertainty measurement in kilometers/sec^2 for this
              observation.

          alt: The target altitude relative to WGS-84 ellipsoid, in kilometers for this
              observation.

          azimuth: Line of sight azimuth angle in degrees and topocentric frame.

          azimuth_bias: Sensor azimuth angle bias in degrees.

          azimuth_rate: Rate of change of the line of sight azimuth in degrees per second.

          azimuth_unc: One sigma uncertainty in the line of sight azimuth angle measurement, in
              degrees.

          bistatic_range: Target bistatic path distance in kilometers. This is the
              transmitter-to-target-to-surveillance site distance.

          bistatic_range_accel: Bistatic range acceleration in kilometers/sec^2.

          bistatic_range_accel_unc: One sigma uncertainty in the bistatic range acceleration measurement, in
              kilometers/sec^2.

          bistatic_range_bias: Sensor bistatic range bias in kilometers.

          bistatic_range_rate: Rate of change of the bistatic path in kilometers/sec.

          bistatic_range_rate_unc: One sigma uncertainty in rate of change of the bistatic path in kilometers/sec.

          bistatic_range_unc: One sigma uncertainty in bistatic range in kilometers.

          coning: Coning angle in degrees.

          coning_unc: One sigma uncertainty in the coning angle measurement, in degrees.

          declination: Line of sight declination angle in degrees and J2000 coordinate frame.

          delay: The time difference, in seconds, between the signal collected at the
              surveillance site (after being reflected from the target) and the reference site
              (direct path line-of-sight signal).

          delay_bias: Delay bias in seconds.

          delay_unc: One sigma uncertainty in the delay measurement, in seconds.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          doppler: Doppler measurement in hertz.

          doppler_unc: One sigma uncertainty in the Doppler measurement in hertz.

          elevation: Line of sight elevation in degrees and topocentric frame.

          elevation_bias: Sensor elevation bias in degrees.

          elevation_rate: Rate of change of the line of sight elevation in degrees per second.

          elevation_unc: One sigma uncertainty in the line of sight elevation angle measurement, in
              degrees.

          ext_observation_id: Optional external observation identifier provided by the source.

          id_rf_emitter: Unique identifier of the transmitter. This ID can be used to obtain additional
              information on an RFEmitter using the 'get by ID' operation (e.g.
              /udl/rfemitter/{id}). For example, the RFEmitter with idRFEmitter = abc would be
              queried as /udl/rfemitter/abc.

          id_sensor: Unique identifier of the reporting surveillance sensor. This ID can be used to
              obtain additional information on a sensor using the 'get by ID' operation (e.g.
              /udl/sensor/{id}). For example, the sensor with idSensor = abc would be queried
              as /udl/sensor/abc.

          id_sensor_ref_receiver: Unique identifier of the reference receiver sensor. This ID can be used to
              obtain additional information on a sensor using the 'get by ID' operation (e.g.
              /udl/sensor/{id}). For example, the sensor with idSensor = abc would be queried
              as /udl/sensor/abc.

          lat: WGS-84 target latitude sub-point at observation time (obTime), represented as
              -90 to 90 degrees (negative values south of equator).

          lon: WGS-84 target longitude sub-point at observation time (obTime), represented as
              -180 to 180 degrees (negative values west of Prime Meridian).

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

          orthogonal_rcs_unc: One sigma uncertainty in orthogonal polarization Radar Cross Section, in
              meters^2.

          ra: Line of sight right ascension in degrees and J2000 coordinate frame.

          rcs: Radar cross section in meters squared for polarization principal.

          rcs_unc: One sigma uncertainty in principal polarization Radar Cross Section, in
              meters^2.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          snr: Signal to noise ratio, in dB.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional identifier to indicate the specific tasking which produced this
              observation.

          timing_bias: Sensor timing bias in seconds.

          tof: Time of flight (TOF) in seconds. This is the calculated propagation time from
              transmitter-to-target-to-surveillance site.

          tof_bias: The Time of Flight (TOF) bias in seconds.

          tof_unc: One sigma uncertainty in time of flight in seconds.

          track_id: Unique identifier of a track that represents a tracklet for this observation.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this observation is part of an uncorrelated track or was
              unable to be correlated to a known object. This flag should only be set to true
              by data providers after an attempt to correlate to an on-orbit object was made
              and failed. If unable to correlate, the 'origObjectId' field may be populated
              with an internal data provider specific identifier.

          xvel: X velocity of target in kilometers/sec in J2000 coordinate frame.

          yvel: Y velocity of target in kilometers/sec in J2000 coordinate frame.

          zvel: Z velocity of target in kilometers/sec in J2000 coordinate frame.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/passiveradarobservation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "ob_time": ob_time,
                    "source": source,
                    "id": id,
                    "accel": accel,
                    "accel_unc": accel_unc,
                    "alt": alt,
                    "azimuth": azimuth,
                    "azimuth_bias": azimuth_bias,
                    "azimuth_rate": azimuth_rate,
                    "azimuth_unc": azimuth_unc,
                    "bistatic_range": bistatic_range,
                    "bistatic_range_accel": bistatic_range_accel,
                    "bistatic_range_accel_unc": bistatic_range_accel_unc,
                    "bistatic_range_bias": bistatic_range_bias,
                    "bistatic_range_rate": bistatic_range_rate,
                    "bistatic_range_rate_unc": bistatic_range_rate_unc,
                    "bistatic_range_unc": bistatic_range_unc,
                    "coning": coning,
                    "coning_unc": coning_unc,
                    "declination": declination,
                    "delay": delay,
                    "delay_bias": delay_bias,
                    "delay_unc": delay_unc,
                    "descriptor": descriptor,
                    "doppler": doppler,
                    "doppler_unc": doppler_unc,
                    "elevation": elevation,
                    "elevation_bias": elevation_bias,
                    "elevation_rate": elevation_rate,
                    "elevation_unc": elevation_unc,
                    "ext_observation_id": ext_observation_id,
                    "id_rf_emitter": id_rf_emitter,
                    "id_sensor": id_sensor,
                    "id_sensor_ref_receiver": id_sensor_ref_receiver,
                    "lat": lat,
                    "lon": lon,
                    "ob_position": ob_position,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "orthogonal_rcs": orthogonal_rcs,
                    "orthogonal_rcs_unc": orthogonal_rcs_unc,
                    "ra": ra,
                    "rcs": rcs,
                    "rcs_unc": rcs_unc,
                    "sat_no": sat_no,
                    "snr": snr,
                    "tags": tags,
                    "task_id": task_id,
                    "timing_bias": timing_bias,
                    "tof": tof,
                    "tof_bias": tof_bias,
                    "tof_unc": tof_unc,
                    "track_id": track_id,
                    "transaction_id": transaction_id,
                    "uct": uct,
                    "xvel": xvel,
                    "yvel": yvel,
                    "zvel": zvel,
                },
                passive_radar_observation_create_params.PassiveRadarObservationCreateParams,
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
    ) -> AsyncPaginator[PassiveRadarObservationListResponse, AsyncOffsetPage[PassiveRadarObservationListResponse]]:
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
            "/udl/passiveradarobservation",
            page=AsyncOffsetPage[PassiveRadarObservationListResponse],
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
                    passive_radar_observation_list_params.PassiveRadarObservationListParams,
                ),
            ),
            model=PassiveRadarObservationListResponse,
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
            "/udl/passiveradarobservation/count",
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
                    passive_radar_observation_count_params.PassiveRadarObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[passive_radar_observation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        PassiveRadarObservation records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/passiveradarobservation/createBulk",
            body=await async_maybe_transform(body, Iterable[passive_radar_observation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def file_create(
        self,
        *,
        body: Iterable[passive_radar_observation_file_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple PassiveRadarObservation records as a POST
        body and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-passiveradar",
            body=await async_maybe_transform(body, Iterable[passive_radar_observation_file_create_params.Body]),
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
    ) -> PassiveRadarObservationGetResponse:
        """
        Service operation to get a single PassiveRadarObservation record by its unique
        ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/passiveradarobservation/{id}",
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
                    passive_radar_observation_get_params.PassiveRadarObservationGetParams,
                ),
            ),
            cast_to=PassiveRadarObservationGetResponse,
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/passiveradarobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> PassiveRadarObservationTupleResponse:
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
            "/udl/passiveradarobservation/tuple",
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
                    passive_radar_observation_tuple_params.PassiveRadarObservationTupleParams,
                ),
            ),
            cast_to=PassiveRadarObservationTupleResponse,
        )


class PassiveRadarObservationResourceWithRawResponse:
    def __init__(self, passive_radar_observation: PassiveRadarObservationResource) -> None:
        self._passive_radar_observation = passive_radar_observation

        self.create = to_raw_response_wrapper(
            passive_radar_observation.create,
        )
        self.list = to_raw_response_wrapper(
            passive_radar_observation.list,
        )
        self.count = to_raw_response_wrapper(
            passive_radar_observation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            passive_radar_observation.create_bulk,
        )
        self.file_create = to_raw_response_wrapper(
            passive_radar_observation.file_create,
        )
        self.get = to_raw_response_wrapper(
            passive_radar_observation.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            passive_radar_observation.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            passive_radar_observation.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._passive_radar_observation.history)


class AsyncPassiveRadarObservationResourceWithRawResponse:
    def __init__(self, passive_radar_observation: AsyncPassiveRadarObservationResource) -> None:
        self._passive_radar_observation = passive_radar_observation

        self.create = async_to_raw_response_wrapper(
            passive_radar_observation.create,
        )
        self.list = async_to_raw_response_wrapper(
            passive_radar_observation.list,
        )
        self.count = async_to_raw_response_wrapper(
            passive_radar_observation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            passive_radar_observation.create_bulk,
        )
        self.file_create = async_to_raw_response_wrapper(
            passive_radar_observation.file_create,
        )
        self.get = async_to_raw_response_wrapper(
            passive_radar_observation.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            passive_radar_observation.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            passive_radar_observation.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._passive_radar_observation.history)


class PassiveRadarObservationResourceWithStreamingResponse:
    def __init__(self, passive_radar_observation: PassiveRadarObservationResource) -> None:
        self._passive_radar_observation = passive_radar_observation

        self.create = to_streamed_response_wrapper(
            passive_radar_observation.create,
        )
        self.list = to_streamed_response_wrapper(
            passive_radar_observation.list,
        )
        self.count = to_streamed_response_wrapper(
            passive_radar_observation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            passive_radar_observation.create_bulk,
        )
        self.file_create = to_streamed_response_wrapper(
            passive_radar_observation.file_create,
        )
        self.get = to_streamed_response_wrapper(
            passive_radar_observation.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            passive_radar_observation.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            passive_radar_observation.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._passive_radar_observation.history)


class AsyncPassiveRadarObservationResourceWithStreamingResponse:
    def __init__(self, passive_radar_observation: AsyncPassiveRadarObservationResource) -> None:
        self._passive_radar_observation = passive_radar_observation

        self.create = async_to_streamed_response_wrapper(
            passive_radar_observation.create,
        )
        self.list = async_to_streamed_response_wrapper(
            passive_radar_observation.list,
        )
        self.count = async_to_streamed_response_wrapper(
            passive_radar_observation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            passive_radar_observation.create_bulk,
        )
        self.file_create = async_to_streamed_response_wrapper(
            passive_radar_observation.file_create,
        )
        self.get = async_to_streamed_response_wrapper(
            passive_radar_observation.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            passive_radar_observation.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            passive_radar_observation.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._passive_radar_observation.history)
