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
from ...types.ais import history_aodr_params, history_list_params
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.ais_full import AIsFull

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
        ts: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[AIsFull]:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: The timestamp that the vessel position was recorded, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ais/history",
            page=SyncOffsetPage[AIsFull],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=AIsFull,
        )

    def aodr(
        self,
        *,
        ts: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        notification: str | NotGiven = NOT_GIVEN,
        output_delimiter: str | NotGiven = NOT_GIVEN,
        output_format: str | NotGiven = NOT_GIVEN,
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
          ts: The timestamp that the vessel position was recorded, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/ais/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    history_aodr_params.HistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
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
        ts: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AIsFull, AsyncOffsetPage[AIsFull]]:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: The timestamp that the vessel position was recorded, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ais/history",
            page=AsyncOffsetPage[AIsFull],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=AIsFull,
        )

    async def aodr(
        self,
        *,
        ts: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        notification: str | NotGiven = NOT_GIVEN,
        output_delimiter: str | NotGiven = NOT_GIVEN,
        output_format: str | NotGiven = NOT_GIVEN,
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
          ts: The timestamp that the vessel position was recorded, in ISO 8601 UTC format.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/ais/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ts": ts,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    history_aodr_params.HistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
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


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_raw_response_wrapper(
            history.list,
        )
        self.aodr = async_to_raw_response_wrapper(
            history.aodr,
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


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.list = async_to_streamed_response_wrapper(
            history.list,
        )
        self.aodr = async_to_streamed_response_wrapper(
            history.aodr,
        )
