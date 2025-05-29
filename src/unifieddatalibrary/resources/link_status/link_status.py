# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ...types import (
    link_status_get_params,
    link_status_list_params,
    link_status_count_params,
    link_status_tuple_params,
    link_status_create_params,
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
from .datalink import (
    DatalinkResource,
    AsyncDatalinkResource,
    DatalinkResourceWithRawResponse,
    AsyncDatalinkResourceWithRawResponse,
    DatalinkResourceWithStreamingResponse,
    AsyncDatalinkResourceWithStreamingResponse,
)
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
from ...types.link_status_get_response import LinkStatusGetResponse
from ...types.link_status_list_response import LinkStatusListResponse
from ...types.link_status_tuple_response import LinkStatusTupleResponse
from ...types.link_status_queryhelp_response import LinkStatusQueryhelpResponse

__all__ = ["LinkStatusResource", "AsyncLinkStatusResource"]


class LinkStatusResource(SyncAPIResource):
    @cached_property
    def datalink(self) -> DatalinkResource:
        return DatalinkResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> LinkStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LinkStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return LinkStatusResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_point1_lat: float,
        end_point1_lon: float,
        end_point1_name: str,
        end_point2_lat: float,
        end_point2_lon: float,
        end_point2_name: str,
        link_name: str,
        link_start_time: Union[str, datetime],
        link_stop_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        band: str | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        data_rate1_to2: float | NotGiven = NOT_GIVEN,
        data_rate2_to1: float | NotGiven = NOT_GIVEN,
        id_beam1: str | NotGiven = NOT_GIVEN,
        id_beam2: str | NotGiven = NOT_GIVEN,
        link_state: str | NotGiven = NOT_GIVEN,
        link_type: str | NotGiven = NOT_GIVEN,
        ops_cap: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        sat_no1: int | NotGiven = NOT_GIVEN,
        sat_no2: int | NotGiven = NOT_GIVEN,
        sys_cap: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single LinkStatus as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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

          end_point1_lat: Latitude of link endpoint-1, WGS-84 in degrees. -90 to 90 degrees (negative
              values south of equator).

          end_point1_lon: Longitude of link endpoint-1, WGS-84 longitude in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          end_point1_name: The name or description of link endpoint-1, corresponding to beam-1.

          end_point2_lat: Latitude of link endpoint-2, WGS-84 in degrees. -90 to 90 degrees (negative
              values south of equator).

          end_point2_lon: Longitude of link endpoint-2, WGS-84 longitude in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          end_point2_name: The name or description of link endpoint-2, corresponding to beam-2.

          link_name: The name or description of the link.

          link_start_time: The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format.

          link_stop_time: The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          band: The RF band employed by the link (e.g. MIL-KA, COM-KA, X-BAND, C-BAND, etc.).

          constellation: The constellation name if the link is established over a LEO/MEO constellation.
              In this case, idOnOrbit1 and idOnOrbit2 will be null.

          data_rate1_to2: The endpoint-1 to endpoint-2 data rate, in kbps.

          data_rate2_to1: The endpoint-2 to endpoint-1 data rate, in kbps.

          id_beam1: The ID of beam-1 forming the link. In the case of two sat link, beam-1
              corresponds to Sat-1.

          id_beam2: The ID of beam-2 forming the link. In the case of two sat link, beam-2
              corresponds to Sat-2.

          link_state: The state of the link (e.g. OK, DEGRADED-WEATHER, DEGRADED-EMI, etc.).

          link_type: The type of the link.

          ops_cap: The OPSCAP mission status of the system(s) forming the link.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          sat_no1: Satellite/catalog number of the target on-orbit primary object.

          sat_no2: Satellite/catalog number of the target on-orbit secondary object.

          sys_cap: The SYSCAP mission status of the system(s) forming the link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/linkstatus",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_point1_lat": end_point1_lat,
                    "end_point1_lon": end_point1_lon,
                    "end_point1_name": end_point1_name,
                    "end_point2_lat": end_point2_lat,
                    "end_point2_lon": end_point2_lon,
                    "end_point2_name": end_point2_name,
                    "link_name": link_name,
                    "link_start_time": link_start_time,
                    "link_stop_time": link_stop_time,
                    "source": source,
                    "id": id,
                    "band": band,
                    "constellation": constellation,
                    "data_rate1_to2": data_rate1_to2,
                    "data_rate2_to1": data_rate2_to1,
                    "id_beam1": id_beam1,
                    "id_beam2": id_beam2,
                    "link_state": link_state,
                    "link_type": link_type,
                    "ops_cap": ops_cap,
                    "origin": origin,
                    "sat_no1": sat_no1,
                    "sat_no2": sat_no2,
                    "sys_cap": sys_cap,
                },
                link_status_create_params.LinkStatusCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        created_at: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        link_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        link_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[LinkStatusListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          created_at: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          link_start_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          link_stop_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/linkstatus",
            page=SyncOffsetPage[LinkStatusListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "link_start_time": link_start_time,
                        "link_stop_time": link_stop_time,
                        "max_results": max_results,
                    },
                    link_status_list_params.LinkStatusListParams,
                ),
            ),
            model=LinkStatusListResponse,
        )

    def count(
        self,
        *,
        created_at: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        link_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        link_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          created_at: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          link_start_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          link_stop_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/linkstatus/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "link_start_time": link_start_time,
                        "link_stop_time": link_stop_time,
                        "max_results": max_results,
                    },
                    link_status_count_params.LinkStatusCountParams,
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
    ) -> LinkStatusGetResponse:
        """
        Service operation to get a single LinkStatus record by its unique ID passed as a
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
            f"/udl/linkstatus/{id}",
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
                    link_status_get_params.LinkStatusGetParams,
                ),
            ),
            cast_to=LinkStatusGetResponse,
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
    ) -> LinkStatusQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/linkstatus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkStatusQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        created_at: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        link_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        link_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkStatusTupleResponse:
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

          created_at: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          link_start_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          link_stop_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/linkstatus/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "created_at": created_at,
                        "first_result": first_result,
                        "link_start_time": link_start_time,
                        "link_stop_time": link_stop_time,
                        "max_results": max_results,
                    },
                    link_status_tuple_params.LinkStatusTupleParams,
                ),
            ),
            cast_to=LinkStatusTupleResponse,
        )


class AsyncLinkStatusResource(AsyncAPIResource):
    @cached_property
    def datalink(self) -> AsyncDatalinkResource:
        return AsyncDatalinkResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLinkStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncLinkStatusResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_point1_lat: float,
        end_point1_lon: float,
        end_point1_name: str,
        end_point2_lat: float,
        end_point2_lon: float,
        end_point2_name: str,
        link_name: str,
        link_start_time: Union[str, datetime],
        link_stop_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        band: str | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        data_rate1_to2: float | NotGiven = NOT_GIVEN,
        data_rate2_to1: float | NotGiven = NOT_GIVEN,
        id_beam1: str | NotGiven = NOT_GIVEN,
        id_beam2: str | NotGiven = NOT_GIVEN,
        link_state: str | NotGiven = NOT_GIVEN,
        link_type: str | NotGiven = NOT_GIVEN,
        ops_cap: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        sat_no1: int | NotGiven = NOT_GIVEN,
        sat_no2: int | NotGiven = NOT_GIVEN,
        sys_cap: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single LinkStatus as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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

          end_point1_lat: Latitude of link endpoint-1, WGS-84 in degrees. -90 to 90 degrees (negative
              values south of equator).

          end_point1_lon: Longitude of link endpoint-1, WGS-84 longitude in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          end_point1_name: The name or description of link endpoint-1, corresponding to beam-1.

          end_point2_lat: Latitude of link endpoint-2, WGS-84 in degrees. -90 to 90 degrees (negative
              values south of equator).

          end_point2_lon: Longitude of link endpoint-2, WGS-84 longitude in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          end_point2_name: The name or description of link endpoint-2, corresponding to beam-2.

          link_name: The name or description of the link.

          link_start_time: The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format.

          link_stop_time: The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          band: The RF band employed by the link (e.g. MIL-KA, COM-KA, X-BAND, C-BAND, etc.).

          constellation: The constellation name if the link is established over a LEO/MEO constellation.
              In this case, idOnOrbit1 and idOnOrbit2 will be null.

          data_rate1_to2: The endpoint-1 to endpoint-2 data rate, in kbps.

          data_rate2_to1: The endpoint-2 to endpoint-1 data rate, in kbps.

          id_beam1: The ID of beam-1 forming the link. In the case of two sat link, beam-1
              corresponds to Sat-1.

          id_beam2: The ID of beam-2 forming the link. In the case of two sat link, beam-2
              corresponds to Sat-2.

          link_state: The state of the link (e.g. OK, DEGRADED-WEATHER, DEGRADED-EMI, etc.).

          link_type: The type of the link.

          ops_cap: The OPSCAP mission status of the system(s) forming the link.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          sat_no1: Satellite/catalog number of the target on-orbit primary object.

          sat_no2: Satellite/catalog number of the target on-orbit secondary object.

          sys_cap: The SYSCAP mission status of the system(s) forming the link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/linkstatus",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_point1_lat": end_point1_lat,
                    "end_point1_lon": end_point1_lon,
                    "end_point1_name": end_point1_name,
                    "end_point2_lat": end_point2_lat,
                    "end_point2_lon": end_point2_lon,
                    "end_point2_name": end_point2_name,
                    "link_name": link_name,
                    "link_start_time": link_start_time,
                    "link_stop_time": link_stop_time,
                    "source": source,
                    "id": id,
                    "band": band,
                    "constellation": constellation,
                    "data_rate1_to2": data_rate1_to2,
                    "data_rate2_to1": data_rate2_to1,
                    "id_beam1": id_beam1,
                    "id_beam2": id_beam2,
                    "link_state": link_state,
                    "link_type": link_type,
                    "ops_cap": ops_cap,
                    "origin": origin,
                    "sat_no1": sat_no1,
                    "sat_no2": sat_no2,
                    "sys_cap": sys_cap,
                },
                link_status_create_params.LinkStatusCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        created_at: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        link_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        link_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LinkStatusListResponse, AsyncOffsetPage[LinkStatusListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          created_at: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          link_start_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          link_stop_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/linkstatus",
            page=AsyncOffsetPage[LinkStatusListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "link_start_time": link_start_time,
                        "link_stop_time": link_stop_time,
                        "max_results": max_results,
                    },
                    link_status_list_params.LinkStatusListParams,
                ),
            ),
            model=LinkStatusListResponse,
        )

    async def count(
        self,
        *,
        created_at: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        link_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        link_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          created_at: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          link_start_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          link_stop_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/linkstatus/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "link_start_time": link_start_time,
                        "link_stop_time": link_stop_time,
                        "max_results": max_results,
                    },
                    link_status_count_params.LinkStatusCountParams,
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
    ) -> LinkStatusGetResponse:
        """
        Service operation to get a single LinkStatus record by its unique ID passed as a
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
            f"/udl/linkstatus/{id}",
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
                    link_status_get_params.LinkStatusGetParams,
                ),
            ),
            cast_to=LinkStatusGetResponse,
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
    ) -> LinkStatusQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/linkstatus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkStatusQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        created_at: Union[str, date] | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        link_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        link_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LinkStatusTupleResponse:
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

          created_at: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          link_start_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link establishment time, or the time that the link becomes available for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          link_stop_time: (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
              The link termination time, or the time that the link becomes unavailable for
              use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/linkstatus/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "created_at": created_at,
                        "first_result": first_result,
                        "link_start_time": link_start_time,
                        "link_stop_time": link_stop_time,
                        "max_results": max_results,
                    },
                    link_status_tuple_params.LinkStatusTupleParams,
                ),
            ),
            cast_to=LinkStatusTupleResponse,
        )


class LinkStatusResourceWithRawResponse:
    def __init__(self, link_status: LinkStatusResource) -> None:
        self._link_status = link_status

        self.create = to_raw_response_wrapper(
            link_status.create,
        )
        self.list = to_raw_response_wrapper(
            link_status.list,
        )
        self.count = to_raw_response_wrapper(
            link_status.count,
        )
        self.get = to_raw_response_wrapper(
            link_status.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            link_status.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            link_status.tuple,
        )

    @cached_property
    def datalink(self) -> DatalinkResourceWithRawResponse:
        return DatalinkResourceWithRawResponse(self._link_status.datalink)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._link_status.history)


class AsyncLinkStatusResourceWithRawResponse:
    def __init__(self, link_status: AsyncLinkStatusResource) -> None:
        self._link_status = link_status

        self.create = async_to_raw_response_wrapper(
            link_status.create,
        )
        self.list = async_to_raw_response_wrapper(
            link_status.list,
        )
        self.count = async_to_raw_response_wrapper(
            link_status.count,
        )
        self.get = async_to_raw_response_wrapper(
            link_status.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            link_status.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            link_status.tuple,
        )

    @cached_property
    def datalink(self) -> AsyncDatalinkResourceWithRawResponse:
        return AsyncDatalinkResourceWithRawResponse(self._link_status.datalink)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._link_status.history)


class LinkStatusResourceWithStreamingResponse:
    def __init__(self, link_status: LinkStatusResource) -> None:
        self._link_status = link_status

        self.create = to_streamed_response_wrapper(
            link_status.create,
        )
        self.list = to_streamed_response_wrapper(
            link_status.list,
        )
        self.count = to_streamed_response_wrapper(
            link_status.count,
        )
        self.get = to_streamed_response_wrapper(
            link_status.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            link_status.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            link_status.tuple,
        )

    @cached_property
    def datalink(self) -> DatalinkResourceWithStreamingResponse:
        return DatalinkResourceWithStreamingResponse(self._link_status.datalink)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._link_status.history)


class AsyncLinkStatusResourceWithStreamingResponse:
    def __init__(self, link_status: AsyncLinkStatusResource) -> None:
        self._link_status = link_status

        self.create = async_to_streamed_response_wrapper(
            link_status.create,
        )
        self.list = async_to_streamed_response_wrapper(
            link_status.list,
        )
        self.count = async_to_streamed_response_wrapper(
            link_status.count,
        )
        self.get = async_to_streamed_response_wrapper(
            link_status.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            link_status.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            link_status.tuple,
        )

    @cached_property
    def datalink(self) -> AsyncDatalinkResourceWithStreamingResponse:
        return AsyncDatalinkResourceWithStreamingResponse(self._link_status.datalink)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._link_status.history)
