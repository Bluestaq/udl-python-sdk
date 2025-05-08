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
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GnssRawIfResource", "AsyncGnssRawIfResource"]


class GnssRawIfResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> GnssRawIfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GnssRawIfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GnssRawIfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return GnssRawIfResourceWithStreamingResponse(self)


class AsyncGnssRawIfResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGnssRawIfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGnssRawIfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGnssRawIfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncGnssRawIfResourceWithStreamingResponse(self)


class GnssRawIfResourceWithRawResponse:
    def __init__(self, gnss_raw_if: GnssRawIfResource) -> None:
        self._gnss_raw_if = gnss_raw_if

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._gnss_raw_if.history)


class AsyncGnssRawIfResourceWithRawResponse:
    def __init__(self, gnss_raw_if: AsyncGnssRawIfResource) -> None:
        self._gnss_raw_if = gnss_raw_if

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._gnss_raw_if.history)


class GnssRawIfResourceWithStreamingResponse:
    def __init__(self, gnss_raw_if: GnssRawIfResource) -> None:
        self._gnss_raw_if = gnss_raw_if

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._gnss_raw_if.history)


class AsyncGnssRawIfResourceWithStreamingResponse:
    def __init__(self, gnss_raw_if: AsyncGnssRawIfResource) -> None:
        self._gnss_raw_if = gnss_raw_if

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._gnss_raw_if.history)
