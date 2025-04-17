# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.supporting_data.dataowner_retrieve_response import DataownerRetrieveResponse

__all__ = ["DataownerResource", "AsyncDataownerResource"]


class DataownerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataownerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DataownerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataownerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return DataownerResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataownerRetrieveResponse:
        return self._get(
            "/udl/dataowner",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataownerRetrieveResponse,
        )

    def count(
        self,
        *,
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
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/dataowner/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncDataownerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataownerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDataownerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataownerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDataownerResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataownerRetrieveResponse:
        return await self._get(
            "/udl/dataowner",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataownerRetrieveResponse,
        )

    async def count(
        self,
        *,
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
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/dataowner/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class DataownerResourceWithRawResponse:
    def __init__(self, dataowner: DataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = to_raw_response_wrapper(
            dataowner.retrieve,
        )
        self.count = to_raw_response_wrapper(
            dataowner.count,
        )


class AsyncDataownerResourceWithRawResponse:
    def __init__(self, dataowner: AsyncDataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = async_to_raw_response_wrapper(
            dataowner.retrieve,
        )
        self.count = async_to_raw_response_wrapper(
            dataowner.count,
        )


class DataownerResourceWithStreamingResponse:
    def __init__(self, dataowner: DataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = to_streamed_response_wrapper(
            dataowner.retrieve,
        )
        self.count = to_streamed_response_wrapper(
            dataowner.count,
        )


class AsyncDataownerResourceWithStreamingResponse:
    def __init__(self, dataowner: AsyncDataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = async_to_streamed_response_wrapper(
            dataowner.retrieve,
        )
        self.count = async_to_streamed_response_wrapper(
            dataowner.count,
        )
