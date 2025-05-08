# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import scs_view_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ScsViewsResource", "AsyncScsViewsResource"]


class ScsViewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScsViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScsViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScsViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ScsViewsResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> BinaryAPIResponse:
        """
        Return a single file to view in browser.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/scs/view/{id}",
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
                    scs_view_retrieve_params.ScsViewRetrieveParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncScsViewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScsViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScsViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScsViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncScsViewsResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Return a single file to view in browser.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/scs/view/{id}",
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
                    scs_view_retrieve_params.ScsViewRetrieveParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ScsViewsResourceWithRawResponse:
    def __init__(self, scs_views: ScsViewsResource) -> None:
        self._scs_views = scs_views

        self.retrieve = to_custom_raw_response_wrapper(
            scs_views.retrieve,
            BinaryAPIResponse,
        )


class AsyncScsViewsResourceWithRawResponse:
    def __init__(self, scs_views: AsyncScsViewsResource) -> None:
        self._scs_views = scs_views

        self.retrieve = async_to_custom_raw_response_wrapper(
            scs_views.retrieve,
            AsyncBinaryAPIResponse,
        )


class ScsViewsResourceWithStreamingResponse:
    def __init__(self, scs_views: ScsViewsResource) -> None:
        self._scs_views = scs_views

        self.retrieve = to_custom_streamed_response_wrapper(
            scs_views.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncScsViewsResourceWithStreamingResponse:
    def __init__(self, scs_views: AsyncScsViewsResource) -> None:
        self._scs_views = scs_views

        self.retrieve = async_to_custom_streamed_response_wrapper(
            scs_views.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
