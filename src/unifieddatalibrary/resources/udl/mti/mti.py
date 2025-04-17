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

__all__ = ["MtiResource", "AsyncMtiResource"]


class MtiResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> MtiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return MtiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MtiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return MtiResourceWithStreamingResponse(self)


class AsyncMtiResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMtiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMtiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMtiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncMtiResourceWithStreamingResponse(self)


class MtiResourceWithRawResponse:
    def __init__(self, mti: MtiResource) -> None:
        self._mti = mti

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._mti.history)


class AsyncMtiResourceWithRawResponse:
    def __init__(self, mti: AsyncMtiResource) -> None:
        self._mti = mti

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._mti.history)


class MtiResourceWithStreamingResponse:
    def __init__(self, mti: MtiResource) -> None:
        self._mti = mti

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._mti.history)


class AsyncMtiResourceWithStreamingResponse:
    def __init__(self, mti: AsyncMtiResource) -> None:
        self._mti = mti

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._mti.history)
