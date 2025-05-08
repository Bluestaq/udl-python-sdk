# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    sar_observation_get_params,
    sar_observation_list_params,
    sar_observation_count_params,
    sar_observation_tuple_params,
    sar_observation_create_params,
    sar_observation_create_bulk_params,
    sar_observation_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.sar_observation_get_response import SarObservationGetResponse
from ...types.sar_observation_list_response import SarObservationListResponse
from ...types.sar_observation_tuple_response import SarObservationTupleResponse

__all__ = ["SarObservationResource", "AsyncSarObservationResource"]


class SarObservationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SarObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SarObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SarObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SarObservationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        collection_end: Union[str, datetime],
        collection_start: Union[str, datetime],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        sar_mode: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        azimuth_angle: float | NotGiven = NOT_GIVEN,
        center_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        continuous_spot_angle: float | NotGiven = NOT_GIVEN,
        coord_sys: str | NotGiven = NOT_GIVEN,
        detection_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        detection_id: str | NotGiven = NOT_GIVEN,
        detection_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        dwell_time: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        far_range: float | NotGiven = NOT_GIVEN,
        graze_angle: float | NotGiven = NOT_GIVEN,
        ground_resolution_projection: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        incidence_angle: float | NotGiven = NOT_GIVEN,
        looks_azimuth: int | NotGiven = NOT_GIVEN,
        looks_range: int | NotGiven = NOT_GIVEN,
        multilook_number: float | NotGiven = NOT_GIVEN,
        near_range: float | NotGiven = NOT_GIVEN,
        ob_direction: str | NotGiven = NOT_GIVEN,
        operating_band: str | NotGiven = NOT_GIVEN,
        operating_freq: float | NotGiven = NOT_GIVEN,
        orbit_state: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pulse_bandwidth: float | NotGiven = NOT_GIVEN,
        pulse_duration: float | NotGiven = NOT_GIVEN,
        resolution_azimuth: float | NotGiven = NOT_GIVEN,
        resolution_range: float | NotGiven = NOT_GIVEN,
        rx_polarization: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat_end: float | NotGiven = NOT_GIVEN,
        senlat_start: float | NotGiven = NOT_GIVEN,
        senlon_end: float | NotGiven = NOT_GIVEN,
        senlon_start: float | NotGiven = NOT_GIVEN,
        senvelx: float | NotGiven = NOT_GIVEN,
        senvely: float | NotGiven = NOT_GIVEN,
        senvelz: float | NotGiven = NOT_GIVEN,
        slant_range: float | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        spacing_azimuth: float | NotGiven = NOT_GIVEN,
        spacing_range: float | NotGiven = NOT_GIVEN,
        squint_angle: float | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        swath_length: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        targetposx: float | NotGiven = NOT_GIVEN,
        targetposy: float | NotGiven = NOT_GIVEN,
        targetposz: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        tx_polarization: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SAR observation as a POST body and ingest
        into the database. This operation is not intended to be used for automated feeds
        into UDL. Data providers should contact the UDL team for specific role
        assignments and for instructions on setting up a permanent feed through an
        alternate mechanism.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          collection_end: Collection end time in ISO 8601 UTC format with microsecond precision.

          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.

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

          sar_mode: Collection mode setting for this collection (e.g. AREA, SPOTLIGHT, STRIP, etc.).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the image event as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground (POLYGON, POINT, LINE).

          azimuth_angle: The azimuth angle, in degrees, of the SAR satellite nadir subpoint measured
              clockwise from true north at the subpoint.

          center_time: The datetime at the center point of the collection in ISO 8601 UTC format with
              microsecond precision.

          collection_id: Optional identifier to indicate the specific collection tasking which produced
              this observation.

          continuous_spot_angle: Required sweep angle for the continuous spot scene in degrees.

          coord_sys: The coordinate system used for the sensor velocity and target position vectors
              for the collection.

          detection_end: The detection end time in ISO 8601 UTC format, with microsecond precision.

          detection_id: Identifier of the specific detection within a collection which produced this
              observation.

          detection_start: The detection start time in ISO 8601 UTC format, with microsecond precision.

          dwell_time: The duration, in seconds, of this detection.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          far_range: Specifies the farthest range, in kilometers, from the flight path to target
              during the collection.

          graze_angle: The graze angle (also referred to as look angle) for the collection in degrees.

          ground_resolution_projection: Distance between independent measurements, representing the physical dimension
              that represents a pixel of the image.

          id_sensor: Unique identifier of the reporting sensor.

          incidence_angle: The center incidence angle in degrees.

          looks_azimuth: The number of looks in the azimuth direction.

          looks_range: The number of looks in the range direction.

          multilook_number: Averages the input synthetic aperture radar (SAR) data by looks in range and
              azimuth to approximate square pixels, mitigates speckle, and reduces SAR tool
              processing time.

          near_range: Specifies the closest range, in kilometers, from the flight path to target
              during the collection.

          ob_direction: The antenna pointing direction (LEFT, RIGHT).

          operating_band: Name of the band containing operating frequency for the collection (e.g. C, E,
              EHF, HF, K, Ka, Ku, L, Q, S, SHF, UNK, UHF, V, VHF, VLF, W, X). See RFBandType
              for more details and descriptions of each band name.

          operating_freq: The operating frequency, in Mhz, for the collection.

          orbit_state: The orbital direction (ASCENDING, DESCENDING) of the platform during the
              collection.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source to indicate the onorbit object
              hosting the sensor associated with this collection. This may be an internal
              identifier and not necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by the source to indicate the sensor for this
              collection. This may be an internal identifier and not necessarily a valid
              sensor ID.

          pulse_bandwidth: The bandwidth frequency of the pulse in Mhz.

          pulse_duration: The duration of a pulse in seconds.

          resolution_azimuth: The resolution in the azimuth direction measured in meters.

          resolution_range: The resolution in the range direction measured in meters.

          rx_polarization: Receive polarization e.g. H - (Horizontally Polarized) Perpendicular to Earth's
              surface, V - (Vertically Polarized) Parallel to Earth's surface, L - (Left Hand
              Circularly Polarized) Rotating left relative to the earth's surface, R - (Right
              Hand Circularly Polarized) Rotating right relative to the earth's surface.

          sat_no: Satellite/Catalog number of the spacecraft hosting the sensor associated with
              this collection.

          senalt: Sensor altitude during collection in kilometers.

          senlat_end: WGS-84 sensor latitude sub-point at collect end time (collectionEnd),
              represented as -90 to 90 degrees (negative values south of equator).

          senlat_start: WGS-84 sensor latitude sub-point at collect start time (collectionStart),
              represented as -90 to 90 degrees (negative values south of equator).

          senlon_end: WGS-84 sensor longitude sub-point at collect end time (collectionEnd),
              represented as -180 to 180 degrees (negative values west of Prime Meridian).

          senlon_start: WGS-84 sensor longitude sub-point at collect start time (collectionStart),
              represented as -180 to 180 degrees (negative values west of Prime Meridian).

          senvelx: Sensor platform X-velocity during collection in kilometers/second.

          senvely: Sensor platform Y-velocity during collection in kilometers/second.

          senvelz: Sensor platform Z-velocity during collection in kilometers/second.

          slant_range: Slant distance from sensor to center point of imaging event in kilometers.

          snr: Signal to noise ratio, in dB.

          spacing_azimuth: The pixel spacing in the azimuth direction measured in meters.

          spacing_range: The pixel spacing in the range direction measured in meters.

          squint_angle: The squint angle for the collection in degrees.

          src_ids: Array of UUIDs of the UDL data records that are related to the SAR Observation.
              See the associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object (e.g.
              /udl/sarobservation/{uuid}).

          src_typs: Array of UDL record types (e.g. ANALYTICMAGERY, ESID, GROUNDIMAGE, NOTIFICATION,
              POI, SV, TRACK) that are related to the SAR Observation. See the associated
              'srcIds' array for the record UUIDs, positionally corresponding to the record
              types in this array. The 'srcTyps' and 'srcIds' arrays must match in size.

          swath_length: The length of the collection as projected on the ground in kilometers.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          targetposx: The collection target X position in kilometers.

          targetposy: The collection target Y position in kilometers.

          targetposz: The collection target Z position in kilometers.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          tx_polarization: Transmit polarization e.g. H - (Horizontally Polarized) Perpendicular to Earth's
              surface, V - (Vertically Polarized) Parallel to Earth's surface, L - (Left Hand
              Circularly Polarized) Rotating left relative to the earth's surface, R - (Right
              Hand Circularly Polarized) Rotating right relative to the earth's surface.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/sarobservation",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "collection_end": collection_end,
                    "collection_start": collection_start,
                    "data_mode": data_mode,
                    "sar_mode": sar_mode,
                    "source": source,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "azimuth_angle": azimuth_angle,
                    "center_time": center_time,
                    "collection_id": collection_id,
                    "continuous_spot_angle": continuous_spot_angle,
                    "coord_sys": coord_sys,
                    "detection_end": detection_end,
                    "detection_id": detection_id,
                    "detection_start": detection_start,
                    "dwell_time": dwell_time,
                    "external_id": external_id,
                    "far_range": far_range,
                    "graze_angle": graze_angle,
                    "ground_resolution_projection": ground_resolution_projection,
                    "id_sensor": id_sensor,
                    "incidence_angle": incidence_angle,
                    "looks_azimuth": looks_azimuth,
                    "looks_range": looks_range,
                    "multilook_number": multilook_number,
                    "near_range": near_range,
                    "ob_direction": ob_direction,
                    "operating_band": operating_band,
                    "operating_freq": operating_freq,
                    "orbit_state": orbit_state,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pulse_bandwidth": pulse_bandwidth,
                    "pulse_duration": pulse_duration,
                    "resolution_azimuth": resolution_azimuth,
                    "resolution_range": resolution_range,
                    "rx_polarization": rx_polarization,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat_end": senlat_end,
                    "senlat_start": senlat_start,
                    "senlon_end": senlon_end,
                    "senlon_start": senlon_start,
                    "senvelx": senvelx,
                    "senvely": senvely,
                    "senvelz": senvelz,
                    "slant_range": slant_range,
                    "snr": snr,
                    "spacing_azimuth": spacing_azimuth,
                    "spacing_range": spacing_range,
                    "squint_angle": squint_angle,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "swath_length": swath_length,
                    "tags": tags,
                    "targetposx": targetposx,
                    "targetposy": targetposy,
                    "targetposz": targetposz,
                    "transaction_id": transaction_id,
                    "tx_polarization": tx_polarization,
                },
                sar_observation_create_params.SarObservationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        collection_start: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SarObservationListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sarobservation",
            page=SyncOffsetPage[SarObservationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_start": collection_start,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sar_observation_list_params.SarObservationListParams,
                ),
            ),
            model=SarObservationListResponse,
        )

    def count(
        self,
        *,
        collection_start: Union[str, datetime],
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
          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/sarobservation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_start": collection_start,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sar_observation_count_params.SarObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[sar_observation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of SAR
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
            "/udl/sarobservation/createBulk",
            body=maybe_transform(body, Iterable[sar_observation_create_bulk_params.Body]),
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
    ) -> SarObservationGetResponse:
        """
        Service operation to get a single SAR observations by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/sarobservation/{id}",
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
                    sar_observation_get_params.SarObservationGetParams,
                ),
            ),
            cast_to=SarObservationGetResponse,
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
            "/udl/sarobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        collection_start: Union[str, datetime],
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SarObservationTupleResponse:
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
          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/sarobservation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_start": collection_start,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sar_observation_tuple_params.SarObservationTupleParams,
                ),
            ),
            cast_to=SarObservationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[sar_observation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take SAR observations as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-sar",
            body=maybe_transform(body, Iterable[sar_observation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSarObservationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSarObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSarObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSarObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSarObservationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        collection_end: Union[str, datetime],
        collection_start: Union[str, datetime],
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        sar_mode: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        azimuth_angle: float | NotGiven = NOT_GIVEN,
        center_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        continuous_spot_angle: float | NotGiven = NOT_GIVEN,
        coord_sys: str | NotGiven = NOT_GIVEN,
        detection_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        detection_id: str | NotGiven = NOT_GIVEN,
        detection_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        dwell_time: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        far_range: float | NotGiven = NOT_GIVEN,
        graze_angle: float | NotGiven = NOT_GIVEN,
        ground_resolution_projection: float | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        incidence_angle: float | NotGiven = NOT_GIVEN,
        looks_azimuth: int | NotGiven = NOT_GIVEN,
        looks_range: int | NotGiven = NOT_GIVEN,
        multilook_number: float | NotGiven = NOT_GIVEN,
        near_range: float | NotGiven = NOT_GIVEN,
        ob_direction: str | NotGiven = NOT_GIVEN,
        operating_band: str | NotGiven = NOT_GIVEN,
        operating_freq: float | NotGiven = NOT_GIVEN,
        orbit_state: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        pulse_bandwidth: float | NotGiven = NOT_GIVEN,
        pulse_duration: float | NotGiven = NOT_GIVEN,
        resolution_azimuth: float | NotGiven = NOT_GIVEN,
        resolution_range: float | NotGiven = NOT_GIVEN,
        rx_polarization: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        senalt: float | NotGiven = NOT_GIVEN,
        senlat_end: float | NotGiven = NOT_GIVEN,
        senlat_start: float | NotGiven = NOT_GIVEN,
        senlon_end: float | NotGiven = NOT_GIVEN,
        senlon_start: float | NotGiven = NOT_GIVEN,
        senvelx: float | NotGiven = NOT_GIVEN,
        senvely: float | NotGiven = NOT_GIVEN,
        senvelz: float | NotGiven = NOT_GIVEN,
        slant_range: float | NotGiven = NOT_GIVEN,
        snr: float | NotGiven = NOT_GIVEN,
        spacing_azimuth: float | NotGiven = NOT_GIVEN,
        spacing_range: float | NotGiven = NOT_GIVEN,
        squint_angle: float | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        swath_length: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        targetposx: float | NotGiven = NOT_GIVEN,
        targetposy: float | NotGiven = NOT_GIVEN,
        targetposz: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        tx_polarization: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SAR observation as a POST body and ingest
        into the database. This operation is not intended to be used for automated feeds
        into UDL. Data providers should contact the UDL team for specific role
        assignments and for instructions on setting up a permanent feed through an
        alternate mechanism.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          collection_end: Collection end time in ISO 8601 UTC format with microsecond precision.

          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.

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

          sar_mode: Collection mode setting for this collection (e.g. AREA, SPOTLIGHT, STRIP, etc.).

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the image event as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground (POLYGON, POINT, LINE).

          azimuth_angle: The azimuth angle, in degrees, of the SAR satellite nadir subpoint measured
              clockwise from true north at the subpoint.

          center_time: The datetime at the center point of the collection in ISO 8601 UTC format with
              microsecond precision.

          collection_id: Optional identifier to indicate the specific collection tasking which produced
              this observation.

          continuous_spot_angle: Required sweep angle for the continuous spot scene in degrees.

          coord_sys: The coordinate system used for the sensor velocity and target position vectors
              for the collection.

          detection_end: The detection end time in ISO 8601 UTC format, with microsecond precision.

          detection_id: Identifier of the specific detection within a collection which produced this
              observation.

          detection_start: The detection start time in ISO 8601 UTC format, with microsecond precision.

          dwell_time: The duration, in seconds, of this detection.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          far_range: Specifies the farthest range, in kilometers, from the flight path to target
              during the collection.

          graze_angle: The graze angle (also referred to as look angle) for the collection in degrees.

          ground_resolution_projection: Distance between independent measurements, representing the physical dimension
              that represents a pixel of the image.

          id_sensor: Unique identifier of the reporting sensor.

          incidence_angle: The center incidence angle in degrees.

          looks_azimuth: The number of looks in the azimuth direction.

          looks_range: The number of looks in the range direction.

          multilook_number: Averages the input synthetic aperture radar (SAR) data by looks in range and
              azimuth to approximate square pixels, mitigates speckle, and reduces SAR tool
              processing time.

          near_range: Specifies the closest range, in kilometers, from the flight path to target
              during the collection.

          ob_direction: The antenna pointing direction (LEFT, RIGHT).

          operating_band: Name of the band containing operating frequency for the collection (e.g. C, E,
              EHF, HF, K, Ka, Ku, L, Q, S, SHF, UNK, UHF, V, VHF, VLF, W, X). See RFBandType
              for more details and descriptions of each band name.

          operating_freq: The operating frequency, in Mhz, for the collection.

          orbit_state: The orbital direction (ASCENDING, DESCENDING) of the platform during the
              collection.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source to indicate the onorbit object
              hosting the sensor associated with this collection. This may be an internal
              identifier and not necessarily a valid satellite number.

          orig_sensor_id: Optional identifier provided by the source to indicate the sensor for this
              collection. This may be an internal identifier and not necessarily a valid
              sensor ID.

          pulse_bandwidth: The bandwidth frequency of the pulse in Mhz.

          pulse_duration: The duration of a pulse in seconds.

          resolution_azimuth: The resolution in the azimuth direction measured in meters.

          resolution_range: The resolution in the range direction measured in meters.

          rx_polarization: Receive polarization e.g. H - (Horizontally Polarized) Perpendicular to Earth's
              surface, V - (Vertically Polarized) Parallel to Earth's surface, L - (Left Hand
              Circularly Polarized) Rotating left relative to the earth's surface, R - (Right
              Hand Circularly Polarized) Rotating right relative to the earth's surface.

          sat_no: Satellite/Catalog number of the spacecraft hosting the sensor associated with
              this collection.

          senalt: Sensor altitude during collection in kilometers.

          senlat_end: WGS-84 sensor latitude sub-point at collect end time (collectionEnd),
              represented as -90 to 90 degrees (negative values south of equator).

          senlat_start: WGS-84 sensor latitude sub-point at collect start time (collectionStart),
              represented as -90 to 90 degrees (negative values south of equator).

          senlon_end: WGS-84 sensor longitude sub-point at collect end time (collectionEnd),
              represented as -180 to 180 degrees (negative values west of Prime Meridian).

          senlon_start: WGS-84 sensor longitude sub-point at collect start time (collectionStart),
              represented as -180 to 180 degrees (negative values west of Prime Meridian).

          senvelx: Sensor platform X-velocity during collection in kilometers/second.

          senvely: Sensor platform Y-velocity during collection in kilometers/second.

          senvelz: Sensor platform Z-velocity during collection in kilometers/second.

          slant_range: Slant distance from sensor to center point of imaging event in kilometers.

          snr: Signal to noise ratio, in dB.

          spacing_azimuth: The pixel spacing in the azimuth direction measured in meters.

          spacing_range: The pixel spacing in the range direction measured in meters.

          squint_angle: The squint angle for the collection in degrees.

          src_ids: Array of UUIDs of the UDL data records that are related to the SAR Observation.
              See the associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object (e.g.
              /udl/sarobservation/{uuid}).

          src_typs: Array of UDL record types (e.g. ANALYTICMAGERY, ESID, GROUNDIMAGE, NOTIFICATION,
              POI, SV, TRACK) that are related to the SAR Observation. See the associated
              'srcIds' array for the record UUIDs, positionally corresponding to the record
              types in this array. The 'srcTyps' and 'srcIds' arrays must match in size.

          swath_length: The length of the collection as projected on the ground in kilometers.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          targetposx: The collection target X position in kilometers.

          targetposy: The collection target Y position in kilometers.

          targetposz: The collection target Z position in kilometers.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          tx_polarization: Transmit polarization e.g. H - (Horizontally Polarized) Perpendicular to Earth's
              surface, V - (Vertically Polarized) Parallel to Earth's surface, L - (Left Hand
              Circularly Polarized) Rotating left relative to the earth's surface, R - (Right
              Hand Circularly Polarized) Rotating right relative to the earth's surface.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/sarobservation",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "collection_end": collection_end,
                    "collection_start": collection_start,
                    "data_mode": data_mode,
                    "sar_mode": sar_mode,
                    "source": source,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "azimuth_angle": azimuth_angle,
                    "center_time": center_time,
                    "collection_id": collection_id,
                    "continuous_spot_angle": continuous_spot_angle,
                    "coord_sys": coord_sys,
                    "detection_end": detection_end,
                    "detection_id": detection_id,
                    "detection_start": detection_start,
                    "dwell_time": dwell_time,
                    "external_id": external_id,
                    "far_range": far_range,
                    "graze_angle": graze_angle,
                    "ground_resolution_projection": ground_resolution_projection,
                    "id_sensor": id_sensor,
                    "incidence_angle": incidence_angle,
                    "looks_azimuth": looks_azimuth,
                    "looks_range": looks_range,
                    "multilook_number": multilook_number,
                    "near_range": near_range,
                    "ob_direction": ob_direction,
                    "operating_band": operating_band,
                    "operating_freq": operating_freq,
                    "orbit_state": orbit_state,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "pulse_bandwidth": pulse_bandwidth,
                    "pulse_duration": pulse_duration,
                    "resolution_azimuth": resolution_azimuth,
                    "resolution_range": resolution_range,
                    "rx_polarization": rx_polarization,
                    "sat_no": sat_no,
                    "senalt": senalt,
                    "senlat_end": senlat_end,
                    "senlat_start": senlat_start,
                    "senlon_end": senlon_end,
                    "senlon_start": senlon_start,
                    "senvelx": senvelx,
                    "senvely": senvely,
                    "senvelz": senvelz,
                    "slant_range": slant_range,
                    "snr": snr,
                    "spacing_azimuth": spacing_azimuth,
                    "spacing_range": spacing_range,
                    "squint_angle": squint_angle,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "swath_length": swath_length,
                    "tags": tags,
                    "targetposx": targetposx,
                    "targetposy": targetposy,
                    "targetposz": targetposz,
                    "transaction_id": transaction_id,
                    "tx_polarization": tx_polarization,
                },
                sar_observation_create_params.SarObservationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        collection_start: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SarObservationListResponse, AsyncOffsetPage[SarObservationListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sarobservation",
            page=AsyncOffsetPage[SarObservationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_start": collection_start,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sar_observation_list_params.SarObservationListParams,
                ),
            ),
            model=SarObservationListResponse,
        )

    async def count(
        self,
        *,
        collection_start: Union[str, datetime],
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
          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/sarobservation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collection_start": collection_start,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sar_observation_count_params.SarObservationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[sar_observation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of SAR
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
            "/udl/sarobservation/createBulk",
            body=await async_maybe_transform(body, Iterable[sar_observation_create_bulk_params.Body]),
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
    ) -> SarObservationGetResponse:
        """
        Service operation to get a single SAR observations by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/sarobservation/{id}",
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
                    sar_observation_get_params.SarObservationGetParams,
                ),
            ),
            cast_to=SarObservationGetResponse,
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
            "/udl/sarobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        collection_start: Union[str, datetime],
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SarObservationTupleResponse:
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
          collection_start: Collection start time in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/sarobservation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collection_start": collection_start,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sar_observation_tuple_params.SarObservationTupleParams,
                ),
            ),
            cast_to=SarObservationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[sar_observation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take SAR observations as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-sar",
            body=await async_maybe_transform(body, Iterable[sar_observation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SarObservationResourceWithRawResponse:
    def __init__(self, sar_observation: SarObservationResource) -> None:
        self._sar_observation = sar_observation

        self.create = to_raw_response_wrapper(
            sar_observation.create,
        )
        self.list = to_raw_response_wrapper(
            sar_observation.list,
        )
        self.count = to_raw_response_wrapper(
            sar_observation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            sar_observation.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            sar_observation.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            sar_observation.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            sar_observation.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            sar_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._sar_observation.history)


class AsyncSarObservationResourceWithRawResponse:
    def __init__(self, sar_observation: AsyncSarObservationResource) -> None:
        self._sar_observation = sar_observation

        self.create = async_to_raw_response_wrapper(
            sar_observation.create,
        )
        self.list = async_to_raw_response_wrapper(
            sar_observation.list,
        )
        self.count = async_to_raw_response_wrapper(
            sar_observation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            sar_observation.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            sar_observation.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            sar_observation.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            sar_observation.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            sar_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._sar_observation.history)


class SarObservationResourceWithStreamingResponse:
    def __init__(self, sar_observation: SarObservationResource) -> None:
        self._sar_observation = sar_observation

        self.create = to_streamed_response_wrapper(
            sar_observation.create,
        )
        self.list = to_streamed_response_wrapper(
            sar_observation.list,
        )
        self.count = to_streamed_response_wrapper(
            sar_observation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            sar_observation.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            sar_observation.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            sar_observation.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            sar_observation.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            sar_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._sar_observation.history)


class AsyncSarObservationResourceWithStreamingResponse:
    def __init__(self, sar_observation: AsyncSarObservationResource) -> None:
        self._sar_observation = sar_observation

        self.create = async_to_streamed_response_wrapper(
            sar_observation.create,
        )
        self.list = async_to_streamed_response_wrapper(
            sar_observation.list,
        )
        self.count = async_to_streamed_response_wrapper(
            sar_observation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            sar_observation.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            sar_observation.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            sar_observation.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            sar_observation.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            sar_observation.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._sar_observation.history)
