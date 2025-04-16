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

__all__ = ["GnssobservationsetResource", "AsyncGnssobservationsetResource"]


class GnssobservationsetResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> GnssobservationsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GnssobservationsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GnssobservationsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return GnssobservationsetResourceWithStreamingResponse(self)


class AsyncGnssobservationsetResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGnssobservationsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGnssobservationsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGnssobservationsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncGnssobservationsetResourceWithStreamingResponse(self)


class GnssobservationsetResourceWithRawResponse:
    def __init__(self, gnssobservationset: GnssobservationsetResource) -> None:
        self._gnssobservationset = gnssobservationset

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._gnssobservationset.history)


class AsyncGnssobservationsetResourceWithRawResponse:
    def __init__(self, gnssobservationset: AsyncGnssobservationsetResource) -> None:
        self._gnssobservationset = gnssobservationset

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._gnssobservationset.history)


class GnssobservationsetResourceWithStreamingResponse:
    def __init__(self, gnssobservationset: GnssobservationsetResource) -> None:
        self._gnssobservationset = gnssobservationset

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._gnssobservationset.history)


class AsyncGnssobservationsetResourceWithStreamingResponse:
    def __init__(self, gnssobservationset: AsyncGnssobservationsetResource) -> None:
        self._gnssobservationset = gnssobservationset

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._gnssobservationset.history)
