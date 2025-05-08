# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

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
from ...types.orbitdetermination import history_aodr_params, history_list_params, history_count_params
from ...types.orbitdetermination.history_list_response import HistoryListResponse

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return HistoryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[HistoryListResponse]:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/orbitdetermination/history",
            page=SyncOffsetPage[HistoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=HistoryListResponse,
        )

    def aodr(
        self,
        *,
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        notification: str | NotGiven = NOT_GIVEN,
        output_delimiter: str | NotGiven = NOT_GIVEN,
        output_format: str | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation, then write that data to the
        Secure Content Store. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/orbitdetermination/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                        "start_time": start_time,
                    },
                    history_aodr_params.HistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/orbitdetermination/history/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    history_count_params.HistoryCountParams,
                ),
            ),
            cast_to=str,
        )


class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncHistoryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[HistoryListResponse, AsyncOffsetPage[HistoryListResponse]]:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/orbitdetermination/history",
            page=AsyncOffsetPage[HistoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=HistoryListResponse,
        )

    async def aodr(
        self,
        *,
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        notification: str | NotGiven = NOT_GIVEN,
        output_delimiter: str | NotGiven = NOT_GIVEN,
        output_format: str | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation, then write that data to the
        Secure Content Store. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/orbitdetermination/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                        "start_time": start_time,
                    },
                    history_aodr_params.HistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
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
          id_on_orbit: (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
              of the target satellite on-orbit object. This ID can be used to obtain
              additional information on an OnOrbit object using the 'get by ID' operation
              (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
              be queried as /udl/onorbit/25544.

          start_time: (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
              solution in ISO 8601 UTC datetime format, with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/orbitdetermination/history/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "id_on_orbit": id_on_orbit,
                        "max_results": max_results,
                        "start_time": start_time,
                    },
                    history_count_params.HistoryCountParams,
                ),
            ),
            cast_to=str,
        )


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.list = to_raw_response_wrapper(
            history.list,
        )
        self.aodr = to_raw_response_wrapper(
            history.aodr,
        )
        self.count = to_raw_response_wrapper(
            history.count,
        )


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_raw_response_wrapper(
            history.list,
        )
        self.aodr = async_to_raw_response_wrapper(
            history.aodr,
        )
        self.count = async_to_raw_response_wrapper(
            history.count,
        )


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.list = to_streamed_response_wrapper(
            history.list,
        )
        self.aodr = to_streamed_response_wrapper(
            history.aodr,
        )
        self.count = to_streamed_response_wrapper(
            history.count,
        )


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_streamed_response_wrapper(
            history.list,
        )
        self.aodr = async_to_streamed_response_wrapper(
            history.aodr,
        )
        self.count = async_to_streamed_response_wrapper(
            history.count,
        )
