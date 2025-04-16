# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.airtaskingorder_list_response import AirtaskingorderListResponse

__all__ = ["AirtaskingordersResource", "AsyncAirtaskingordersResource"]


class AirtaskingordersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AirtaskingordersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirtaskingordersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirtaskingordersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirtaskingordersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirtaskingorderListResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.
        """
        return self._get(
            "/udl/airtaskingorder",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirtaskingorderListResponse,
        )


class AsyncAirtaskingordersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAirtaskingordersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirtaskingordersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirtaskingordersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirtaskingordersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirtaskingorderListResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.
        """
        return await self._get(
            "/udl/airtaskingorder",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirtaskingorderListResponse,
        )


class AirtaskingordersResourceWithRawResponse:
    def __init__(self, airtaskingorders: AirtaskingordersResource) -> None:
        self._airtaskingorders = airtaskingorders

        self.list = to_raw_response_wrapper(
            airtaskingorders.list,
        )


class AsyncAirtaskingordersResourceWithRawResponse:
    def __init__(self, airtaskingorders: AsyncAirtaskingordersResource) -> None:
        self._airtaskingorders = airtaskingorders

        self.list = async_to_raw_response_wrapper(
            airtaskingorders.list,
        )


class AirtaskingordersResourceWithStreamingResponse:
    def __init__(self, airtaskingorders: AirtaskingordersResource) -> None:
        self._airtaskingorders = airtaskingorders

        self.list = to_streamed_response_wrapper(
            airtaskingorders.list,
        )


class AsyncAirtaskingordersResourceWithStreamingResponse:
    def __init__(self, airtaskingorders: AsyncAirtaskingordersResource) -> None:
        self._airtaskingorders = airtaskingorders

        self.list = async_to_streamed_response_wrapper(
            airtaskingorders.list,
        )
