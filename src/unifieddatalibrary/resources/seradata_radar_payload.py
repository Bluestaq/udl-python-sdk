# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    seradata_radar_payload_get_params,
    seradata_radar_payload_list_params,
    seradata_radar_payload_count_params,
    seradata_radar_payload_tuple_params,
    seradata_radar_payload_create_params,
    seradata_radar_payload_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.seradata_radar_payload_get_response import SeradataRadarPayloadGetResponse
from ..types.seradata_radar_payload_list_response import SeradataRadarPayloadListResponse
from ..types.seradata_radar_payload_tuple_response import SeradataRadarPayloadTupleResponse
from ..types.seradata_radar_payload_queryhelp_response import SeradataRadarPayloadQueryhelpResponse

__all__ = ["SeradataRadarPayloadResource", "AsyncSeradataRadarPayloadResource"]


class SeradataRadarPayloadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeradataRadarPayloadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SeradataRadarPayloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeradataRadarPayloadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SeradataRadarPayloadResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        spacecraft_id: str,
        id: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        best_resolution: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        constellation_interferometric_capability: str | NotGiven = NOT_GIVEN,
        duty_cycle: str | NotGiven = NOT_GIVEN,
        field_of_regard: float | NotGiven = NOT_GIVEN,
        field_of_view: float | NotGiven = NOT_GIVEN,
        frequency: float | NotGiven = NOT_GIVEN,
        frequency_band: str | NotGiven = NOT_GIVEN,
        ground_station_locations: str | NotGiven = NOT_GIVEN,
        ground_stations: str | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        partner_spacecraft: str | NotGiven = NOT_GIVEN,
        pointing_method: str | NotGiven = NOT_GIVEN,
        receive_polarization: str | NotGiven = NOT_GIVEN,
        recorder_size: str | NotGiven = NOT_GIVEN,
        swath_width: float | NotGiven = NOT_GIVEN,
        transmit_polarization: str | NotGiven = NOT_GIVEN,
        wave_length: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SeradataRadarPayload as a POST body and
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

          source: Source of the data.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          id: Unique identifier of the record, auto-generated by the system.

          bandwidth: Radar bandwidth in mega hertz.

          best_resolution: Best resolution in meters.

          category: Radar category, e.g. SAR, Surface Search, etc.

          constellation_interferometric_capability: Constellation interferometric capability.

          duty_cycle: Duty cycle.

          field_of_regard: Field of regard of this radar in degrees.

          field_of_view: Field of view of this radar in kilometers.

          frequency: Frequency in giga hertz.

          frequency_band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          ground_station_locations: Ground Station Locations for this payload.

          ground_stations: Ground Station info for this payload.

          hosted_for_company_org_id: Hosted for company/Organization Id.

          id_sensor: UUID of the Sensor record.

          manufacturer_org_id: Manufacturer Organization Id.

          name: Sensor name from Seradata, e.g. ALT (Radar Altimeter), COSI (Corea SAR
              Instrument), etc.

          notes: Payload notes.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          partner_spacecraft: Partner seradata-spacecraft.

          pointing_method: Point method for this radar, e.g. Spacecraft.

          receive_polarization: Receive polarization, e.g. Lin Dual, Lin vert, etc.

          recorder_size: Recorder size, e.g. 256.

          swath_width: Swath width in kilometers.

          transmit_polarization: Transmit polarization, e.g. Lin Dual, Lin vert, etc.

          wave_length: Wave length in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/seradataradarpayload",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "spacecraft_id": spacecraft_id,
                    "id": id,
                    "bandwidth": bandwidth,
                    "best_resolution": best_resolution,
                    "category": category,
                    "constellation_interferometric_capability": constellation_interferometric_capability,
                    "duty_cycle": duty_cycle,
                    "field_of_regard": field_of_regard,
                    "field_of_view": field_of_view,
                    "frequency": frequency,
                    "frequency_band": frequency_band,
                    "ground_station_locations": ground_station_locations,
                    "ground_stations": ground_stations,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "id_sensor": id_sensor,
                    "manufacturer_org_id": manufacturer_org_id,
                    "name": name,
                    "notes": notes,
                    "origin": origin,
                    "partner_spacecraft": partner_spacecraft,
                    "pointing_method": pointing_method,
                    "receive_polarization": receive_polarization,
                    "recorder_size": recorder_size,
                    "swath_width": swath_width,
                    "transmit_polarization": transmit_polarization,
                    "wave_length": wave_length,
                },
                seradata_radar_payload_create_params.SeradataRadarPayloadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        spacecraft_id: str,
        body_id: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        best_resolution: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        constellation_interferometric_capability: str | NotGiven = NOT_GIVEN,
        duty_cycle: str | NotGiven = NOT_GIVEN,
        field_of_regard: float | NotGiven = NOT_GIVEN,
        field_of_view: float | NotGiven = NOT_GIVEN,
        frequency: float | NotGiven = NOT_GIVEN,
        frequency_band: str | NotGiven = NOT_GIVEN,
        ground_station_locations: str | NotGiven = NOT_GIVEN,
        ground_stations: str | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        partner_spacecraft: str | NotGiven = NOT_GIVEN,
        pointing_method: str | NotGiven = NOT_GIVEN,
        receive_polarization: str | NotGiven = NOT_GIVEN,
        recorder_size: str | NotGiven = NOT_GIVEN,
        swath_width: float | NotGiven = NOT_GIVEN,
        transmit_polarization: str | NotGiven = NOT_GIVEN,
        wave_length: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an SeradataRadarPayload.

        A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          source: Source of the data.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          body_id: Unique identifier of the record, auto-generated by the system.

          bandwidth: Radar bandwidth in mega hertz.

          best_resolution: Best resolution in meters.

          category: Radar category, e.g. SAR, Surface Search, etc.

          constellation_interferometric_capability: Constellation interferometric capability.

          duty_cycle: Duty cycle.

          field_of_regard: Field of regard of this radar in degrees.

          field_of_view: Field of view of this radar in kilometers.

          frequency: Frequency in giga hertz.

          frequency_band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          ground_station_locations: Ground Station Locations for this payload.

          ground_stations: Ground Station info for this payload.

          hosted_for_company_org_id: Hosted for company/Organization Id.

          id_sensor: UUID of the Sensor record.

          manufacturer_org_id: Manufacturer Organization Id.

          name: Sensor name from Seradata, e.g. ALT (Radar Altimeter), COSI (Corea SAR
              Instrument), etc.

          notes: Payload notes.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          partner_spacecraft: Partner seradata-spacecraft.

          pointing_method: Point method for this radar, e.g. Spacecraft.

          receive_polarization: Receive polarization, e.g. Lin Dual, Lin vert, etc.

          recorder_size: Recorder size, e.g. 256.

          swath_width: Swath width in kilometers.

          transmit_polarization: Transmit polarization, e.g. Lin Dual, Lin vert, etc.

          wave_length: Wave length in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/seradataradarpayload/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "spacecraft_id": spacecraft_id,
                    "body_id": body_id,
                    "bandwidth": bandwidth,
                    "best_resolution": best_resolution,
                    "category": category,
                    "constellation_interferometric_capability": constellation_interferometric_capability,
                    "duty_cycle": duty_cycle,
                    "field_of_regard": field_of_regard,
                    "field_of_view": field_of_view,
                    "frequency": frequency,
                    "frequency_band": frequency_band,
                    "ground_station_locations": ground_station_locations,
                    "ground_stations": ground_stations,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "id_sensor": id_sensor,
                    "manufacturer_org_id": manufacturer_org_id,
                    "name": name,
                    "notes": notes,
                    "origin": origin,
                    "partner_spacecraft": partner_spacecraft,
                    "pointing_method": pointing_method,
                    "receive_polarization": receive_polarization,
                    "recorder_size": recorder_size,
                    "swath_width": swath_width,
                    "transmit_polarization": transmit_polarization,
                    "wave_length": wave_length,
                },
                seradata_radar_payload_update_params.SeradataRadarPayloadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SeradataRadarPayloadListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/seradataradarpayload",
            page=SyncOffsetPage[SeradataRadarPayloadListResponse],
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
                    seradata_radar_payload_list_params.SeradataRadarPayloadListParams,
                ),
            ),
            model=SeradataRadarPayloadListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete an SeradataRadarPayload specified by the passed ID
        path parameter. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/udl/seradataradarpayload/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/seradataradarpayload/count",
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
                    seradata_radar_payload_count_params.SeradataRadarPayloadCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> SeradataRadarPayloadGetResponse:
        """
        Service operation to get a single SeradataRadarPayload by its unique ID passed
        as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/seradataradarpayload/{id}",
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
                    seradata_radar_payload_get_params.SeradataRadarPayloadGetParams,
                ),
            ),
            cast_to=SeradataRadarPayloadGetResponse,
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
    ) -> SeradataRadarPayloadQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/seradataradarpayload/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeradataRadarPayloadQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SeradataRadarPayloadTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/seradataradarpayload/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    seradata_radar_payload_tuple_params.SeradataRadarPayloadTupleParams,
                ),
            ),
            cast_to=SeradataRadarPayloadTupleResponse,
        )


class AsyncSeradataRadarPayloadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeradataRadarPayloadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSeradataRadarPayloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeradataRadarPayloadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSeradataRadarPayloadResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        spacecraft_id: str,
        id: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        best_resolution: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        constellation_interferometric_capability: str | NotGiven = NOT_GIVEN,
        duty_cycle: str | NotGiven = NOT_GIVEN,
        field_of_regard: float | NotGiven = NOT_GIVEN,
        field_of_view: float | NotGiven = NOT_GIVEN,
        frequency: float | NotGiven = NOT_GIVEN,
        frequency_band: str | NotGiven = NOT_GIVEN,
        ground_station_locations: str | NotGiven = NOT_GIVEN,
        ground_stations: str | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        partner_spacecraft: str | NotGiven = NOT_GIVEN,
        pointing_method: str | NotGiven = NOT_GIVEN,
        receive_polarization: str | NotGiven = NOT_GIVEN,
        recorder_size: str | NotGiven = NOT_GIVEN,
        swath_width: float | NotGiven = NOT_GIVEN,
        transmit_polarization: str | NotGiven = NOT_GIVEN,
        wave_length: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SeradataRadarPayload as a POST body and
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

          source: Source of the data.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          id: Unique identifier of the record, auto-generated by the system.

          bandwidth: Radar bandwidth in mega hertz.

          best_resolution: Best resolution in meters.

          category: Radar category, e.g. SAR, Surface Search, etc.

          constellation_interferometric_capability: Constellation interferometric capability.

          duty_cycle: Duty cycle.

          field_of_regard: Field of regard of this radar in degrees.

          field_of_view: Field of view of this radar in kilometers.

          frequency: Frequency in giga hertz.

          frequency_band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          ground_station_locations: Ground Station Locations for this payload.

          ground_stations: Ground Station info for this payload.

          hosted_for_company_org_id: Hosted for company/Organization Id.

          id_sensor: UUID of the Sensor record.

          manufacturer_org_id: Manufacturer Organization Id.

          name: Sensor name from Seradata, e.g. ALT (Radar Altimeter), COSI (Corea SAR
              Instrument), etc.

          notes: Payload notes.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          partner_spacecraft: Partner seradata-spacecraft.

          pointing_method: Point method for this radar, e.g. Spacecraft.

          receive_polarization: Receive polarization, e.g. Lin Dual, Lin vert, etc.

          recorder_size: Recorder size, e.g. 256.

          swath_width: Swath width in kilometers.

          transmit_polarization: Transmit polarization, e.g. Lin Dual, Lin vert, etc.

          wave_length: Wave length in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/seradataradarpayload",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "spacecraft_id": spacecraft_id,
                    "id": id,
                    "bandwidth": bandwidth,
                    "best_resolution": best_resolution,
                    "category": category,
                    "constellation_interferometric_capability": constellation_interferometric_capability,
                    "duty_cycle": duty_cycle,
                    "field_of_regard": field_of_regard,
                    "field_of_view": field_of_view,
                    "frequency": frequency,
                    "frequency_band": frequency_band,
                    "ground_station_locations": ground_station_locations,
                    "ground_stations": ground_stations,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "id_sensor": id_sensor,
                    "manufacturer_org_id": manufacturer_org_id,
                    "name": name,
                    "notes": notes,
                    "origin": origin,
                    "partner_spacecraft": partner_spacecraft,
                    "pointing_method": pointing_method,
                    "receive_polarization": receive_polarization,
                    "recorder_size": recorder_size,
                    "swath_width": swath_width,
                    "transmit_polarization": transmit_polarization,
                    "wave_length": wave_length,
                },
                seradata_radar_payload_create_params.SeradataRadarPayloadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        spacecraft_id: str,
        body_id: str | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        best_resolution: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        constellation_interferometric_capability: str | NotGiven = NOT_GIVEN,
        duty_cycle: str | NotGiven = NOT_GIVEN,
        field_of_regard: float | NotGiven = NOT_GIVEN,
        field_of_view: float | NotGiven = NOT_GIVEN,
        frequency: float | NotGiven = NOT_GIVEN,
        frequency_band: str | NotGiven = NOT_GIVEN,
        ground_station_locations: str | NotGiven = NOT_GIVEN,
        ground_stations: str | NotGiven = NOT_GIVEN,
        hosted_for_company_org_id: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        partner_spacecraft: str | NotGiven = NOT_GIVEN,
        pointing_method: str | NotGiven = NOT_GIVEN,
        receive_polarization: str | NotGiven = NOT_GIVEN,
        recorder_size: str | NotGiven = NOT_GIVEN,
        swath_width: float | NotGiven = NOT_GIVEN,
        transmit_polarization: str | NotGiven = NOT_GIVEN,
        wave_length: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an SeradataRadarPayload.

        A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          source: Source of the data.

          spacecraft_id: Seradata ID of the spacecraft (SeradataSpacecraftDetails ID).

          body_id: Unique identifier of the record, auto-generated by the system.

          bandwidth: Radar bandwidth in mega hertz.

          best_resolution: Best resolution in meters.

          category: Radar category, e.g. SAR, Surface Search, etc.

          constellation_interferometric_capability: Constellation interferometric capability.

          duty_cycle: Duty cycle.

          field_of_regard: Field of regard of this radar in degrees.

          field_of_view: Field of view of this radar in kilometers.

          frequency: Frequency in giga hertz.

          frequency_band: Name of the band of this RF range (e.g.
              X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
              details and descriptions of each band name.

          ground_station_locations: Ground Station Locations for this payload.

          ground_stations: Ground Station info for this payload.

          hosted_for_company_org_id: Hosted for company/Organization Id.

          id_sensor: UUID of the Sensor record.

          manufacturer_org_id: Manufacturer Organization Id.

          name: Sensor name from Seradata, e.g. ALT (Radar Altimeter), COSI (Corea SAR
              Instrument), etc.

          notes: Payload notes.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          partner_spacecraft: Partner seradata-spacecraft.

          pointing_method: Point method for this radar, e.g. Spacecraft.

          receive_polarization: Receive polarization, e.g. Lin Dual, Lin vert, etc.

          recorder_size: Recorder size, e.g. 256.

          swath_width: Swath width in kilometers.

          transmit_polarization: Transmit polarization, e.g. Lin Dual, Lin vert, etc.

          wave_length: Wave length in meters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/seradataradarpayload/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "spacecraft_id": spacecraft_id,
                    "body_id": body_id,
                    "bandwidth": bandwidth,
                    "best_resolution": best_resolution,
                    "category": category,
                    "constellation_interferometric_capability": constellation_interferometric_capability,
                    "duty_cycle": duty_cycle,
                    "field_of_regard": field_of_regard,
                    "field_of_view": field_of_view,
                    "frequency": frequency,
                    "frequency_band": frequency_band,
                    "ground_station_locations": ground_station_locations,
                    "ground_stations": ground_stations,
                    "hosted_for_company_org_id": hosted_for_company_org_id,
                    "id_sensor": id_sensor,
                    "manufacturer_org_id": manufacturer_org_id,
                    "name": name,
                    "notes": notes,
                    "origin": origin,
                    "partner_spacecraft": partner_spacecraft,
                    "pointing_method": pointing_method,
                    "receive_polarization": receive_polarization,
                    "recorder_size": recorder_size,
                    "swath_width": swath_width,
                    "transmit_polarization": transmit_polarization,
                    "wave_length": wave_length,
                },
                seradata_radar_payload_update_params.SeradataRadarPayloadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SeradataRadarPayloadListResponse, AsyncOffsetPage[SeradataRadarPayloadListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/seradataradarpayload",
            page=AsyncOffsetPage[SeradataRadarPayloadListResponse],
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
                    seradata_radar_payload_list_params.SeradataRadarPayloadListParams,
                ),
            ),
            model=SeradataRadarPayloadListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete an SeradataRadarPayload specified by the passed ID
        path parameter. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/udl/seradataradarpayload/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/seradataradarpayload/count",
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
                    seradata_radar_payload_count_params.SeradataRadarPayloadCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> SeradataRadarPayloadGetResponse:
        """
        Service operation to get a single SeradataRadarPayload by its unique ID passed
        as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/seradataradarpayload/{id}",
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
                    seradata_radar_payload_get_params.SeradataRadarPayloadGetParams,
                ),
            ),
            cast_to=SeradataRadarPayloadGetResponse,
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
    ) -> SeradataRadarPayloadQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/seradataradarpayload/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeradataRadarPayloadQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SeradataRadarPayloadTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/seradataradarpayload/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    seradata_radar_payload_tuple_params.SeradataRadarPayloadTupleParams,
                ),
            ),
            cast_to=SeradataRadarPayloadTupleResponse,
        )


class SeradataRadarPayloadResourceWithRawResponse:
    def __init__(self, seradata_radar_payload: SeradataRadarPayloadResource) -> None:
        self._seradata_radar_payload = seradata_radar_payload

        self.create = to_raw_response_wrapper(
            seradata_radar_payload.create,
        )
        self.update = to_raw_response_wrapper(
            seradata_radar_payload.update,
        )
        self.list = to_raw_response_wrapper(
            seradata_radar_payload.list,
        )
        self.delete = to_raw_response_wrapper(
            seradata_radar_payload.delete,
        )
        self.count = to_raw_response_wrapper(
            seradata_radar_payload.count,
        )
        self.get = to_raw_response_wrapper(
            seradata_radar_payload.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            seradata_radar_payload.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            seradata_radar_payload.tuple,
        )


class AsyncSeradataRadarPayloadResourceWithRawResponse:
    def __init__(self, seradata_radar_payload: AsyncSeradataRadarPayloadResource) -> None:
        self._seradata_radar_payload = seradata_radar_payload

        self.create = async_to_raw_response_wrapper(
            seradata_radar_payload.create,
        )
        self.update = async_to_raw_response_wrapper(
            seradata_radar_payload.update,
        )
        self.list = async_to_raw_response_wrapper(
            seradata_radar_payload.list,
        )
        self.delete = async_to_raw_response_wrapper(
            seradata_radar_payload.delete,
        )
        self.count = async_to_raw_response_wrapper(
            seradata_radar_payload.count,
        )
        self.get = async_to_raw_response_wrapper(
            seradata_radar_payload.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            seradata_radar_payload.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            seradata_radar_payload.tuple,
        )


class SeradataRadarPayloadResourceWithStreamingResponse:
    def __init__(self, seradata_radar_payload: SeradataRadarPayloadResource) -> None:
        self._seradata_radar_payload = seradata_radar_payload

        self.create = to_streamed_response_wrapper(
            seradata_radar_payload.create,
        )
        self.update = to_streamed_response_wrapper(
            seradata_radar_payload.update,
        )
        self.list = to_streamed_response_wrapper(
            seradata_radar_payload.list,
        )
        self.delete = to_streamed_response_wrapper(
            seradata_radar_payload.delete,
        )
        self.count = to_streamed_response_wrapper(
            seradata_radar_payload.count,
        )
        self.get = to_streamed_response_wrapper(
            seradata_radar_payload.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            seradata_radar_payload.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            seradata_radar_payload.tuple,
        )


class AsyncSeradataRadarPayloadResourceWithStreamingResponse:
    def __init__(self, seradata_radar_payload: AsyncSeradataRadarPayloadResource) -> None:
        self._seradata_radar_payload = seradata_radar_payload

        self.create = async_to_streamed_response_wrapper(
            seradata_radar_payload.create,
        )
        self.update = async_to_streamed_response_wrapper(
            seradata_radar_payload.update,
        )
        self.list = async_to_streamed_response_wrapper(
            seradata_radar_payload.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            seradata_radar_payload.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            seradata_radar_payload.count,
        )
        self.get = async_to_streamed_response_wrapper(
            seradata_radar_payload.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            seradata_radar_payload.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            seradata_radar_payload.tuple,
        )
