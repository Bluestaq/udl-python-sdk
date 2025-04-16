# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GeostatusResource", "AsyncGeostatusResource"]


class GeostatusResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> GeostatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GeostatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeostatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return GeostatusResourceWithStreamingResponse(self)


class AsyncGeostatusResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGeostatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGeostatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeostatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncGeostatusResourceWithStreamingResponse(self)


class GeostatusResourceWithRawResponse:
    def __init__(self, geostatus: GeostatusResource) -> None:
        self._geostatus = geostatus

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._geostatus.history)


class AsyncGeostatusResourceWithRawResponse:
    def __init__(self, geostatus: AsyncGeostatusResource) -> None:
        self._geostatus = geostatus

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._geostatus.history)


class GeostatusResourceWithStreamingResponse:
    def __init__(self, geostatus: GeostatusResource) -> None:
        self._geostatus = geostatus

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._geostatus.history)


class AsyncGeostatusResourceWithStreamingResponse:
    def __init__(self, geostatus: AsyncGeostatusResource) -> None:
        self._geostatus = geostatus

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._geostatus.history)
