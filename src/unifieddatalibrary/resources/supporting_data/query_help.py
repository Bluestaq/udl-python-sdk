# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["QueryHelpResource", "AsyncQueryHelpResource"]


class QueryHelpResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryHelpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return QueryHelpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryHelpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return QueryHelpResourceWithStreamingResponse(self)

    def retrieve(
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
            "/udl/dataowner/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncQueryHelpResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryHelpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryHelpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryHelpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncQueryHelpResourceWithStreamingResponse(self)

    async def retrieve(
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
            "/udl/dataowner/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class QueryHelpResourceWithRawResponse:
    def __init__(self, query_help: QueryHelpResource) -> None:
        self._query_help = query_help

        self.retrieve = to_raw_response_wrapper(
            query_help.retrieve,
        )


class AsyncQueryHelpResourceWithRawResponse:
    def __init__(self, query_help: AsyncQueryHelpResource) -> None:
        self._query_help = query_help

        self.retrieve = async_to_raw_response_wrapper(
            query_help.retrieve,
        )


class QueryHelpResourceWithStreamingResponse:
    def __init__(self, query_help: QueryHelpResource) -> None:
        self._query_help = query_help

        self.retrieve = to_streamed_response_wrapper(
            query_help.retrieve,
        )


class AsyncQueryHelpResourceWithStreamingResponse:
    def __init__(self, query_help: AsyncQueryHelpResource) -> None:
        self._query_help = query_help

        self.retrieve = async_to_streamed_response_wrapper(
            query_help.retrieve,
        )
