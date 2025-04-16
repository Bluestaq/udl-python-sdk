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
from ...types.supporting_data.provider_metadata_retrieve_response import ProviderMetadataRetrieveResponse

__all__ = ["ProviderMetadataResource", "AsyncProviderMetadataResource"]


class ProviderMetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProviderMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProviderMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return ProviderMetadataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderMetadataRetrieveResponse:
        return self._get(
            "/udl/dataowner/providerMetadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderMetadataRetrieveResponse,
        )


class AsyncProviderMetadataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProviderMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncProviderMetadataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderMetadataRetrieveResponse:
        return await self._get(
            "/udl/dataowner/providerMetadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderMetadataRetrieveResponse,
        )


class ProviderMetadataResourceWithRawResponse:
    def __init__(self, provider_metadata: ProviderMetadataResource) -> None:
        self._provider_metadata = provider_metadata

        self.retrieve = to_raw_response_wrapper(
            provider_metadata.retrieve,
        )


class AsyncProviderMetadataResourceWithRawResponse:
    def __init__(self, provider_metadata: AsyncProviderMetadataResource) -> None:
        self._provider_metadata = provider_metadata

        self.retrieve = async_to_raw_response_wrapper(
            provider_metadata.retrieve,
        )


class ProviderMetadataResourceWithStreamingResponse:
    def __init__(self, provider_metadata: ProviderMetadataResource) -> None:
        self._provider_metadata = provider_metadata

        self.retrieve = to_streamed_response_wrapper(
            provider_metadata.retrieve,
        )


class AsyncProviderMetadataResourceWithStreamingResponse:
    def __init__(self, provider_metadata: AsyncProviderMetadataResource) -> None:
        self._provider_metadata = provider_metadata

        self.retrieve = async_to_streamed_response_wrapper(
            provider_metadata.retrieve,
        )
