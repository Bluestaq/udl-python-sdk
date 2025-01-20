# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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

__all__ = ["LinkStatusResource", "AsyncLinkStatusResource"]


class LinkStatusResource(SyncAPIResource):
    @cached_property
    def datalink(self) -> DatalinkResource:
        return DatalinkResource(self._client)

    @cached_property
    def with_raw_response(self) -> LinkStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return LinkStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return LinkStatusResourceWithStreamingResponse(self)


class AsyncLinkStatusResource(AsyncAPIResource):
    @cached_property
    def datalink(self) -> AsyncDatalinkResource:
        return AsyncDatalinkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLinkStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncLinkStatusResourceWithStreamingResponse(self)


class LinkStatusResourceWithRawResponse:
    def __init__(self, link_status: LinkStatusResource) -> None:
        self._link_status = link_status

    @cached_property
    def datalink(self) -> DatalinkResourceWithRawResponse:
        return DatalinkResourceWithRawResponse(self._link_status.datalink)


class AsyncLinkStatusResourceWithRawResponse:
    def __init__(self, link_status: AsyncLinkStatusResource) -> None:
        self._link_status = link_status

    @cached_property
    def datalink(self) -> AsyncDatalinkResourceWithRawResponse:
        return AsyncDatalinkResourceWithRawResponse(self._link_status.datalink)


class LinkStatusResourceWithStreamingResponse:
    def __init__(self, link_status: LinkStatusResource) -> None:
        self._link_status = link_status

    @cached_property
    def datalink(self) -> DatalinkResourceWithStreamingResponse:
        return DatalinkResourceWithStreamingResponse(self._link_status.datalink)


class AsyncLinkStatusResourceWithStreamingResponse:
    def __init__(self, link_status: AsyncLinkStatusResource) -> None:
        self._link_status = link_status

    @cached_property
    def datalink(self) -> AsyncDatalinkResourceWithStreamingResponse:
        return AsyncDatalinkResourceWithStreamingResponse(self._link_status.datalink)
