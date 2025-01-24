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

__all__ = ["LogisticsSupportResource", "AsyncLogisticsSupportResource"]


class LogisticsSupportResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogisticsSupportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return LogisticsSupportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogisticsSupportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return LogisticsSupportResourceWithStreamingResponse(self)


class AsyncLogisticsSupportResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogisticsSupportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogisticsSupportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogisticsSupportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncLogisticsSupportResourceWithStreamingResponse(self)


class LogisticsSupportResourceWithRawResponse:
    def __init__(self, logistics_support: LogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._logistics_support.history)


class AsyncLogisticsSupportResourceWithRawResponse:
    def __init__(self, logistics_support: AsyncLogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._logistics_support.history)


class LogisticsSupportResourceWithStreamingResponse:
    def __init__(self, logistics_support: LogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._logistics_support.history)


class AsyncLogisticsSupportResourceWithStreamingResponse:
    def __init__(self, logistics_support: AsyncLogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._logistics_support.history)
