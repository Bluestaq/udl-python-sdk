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

__all__ = ["LaunchEventResource", "AsyncLaunchEventResource"]


class LaunchEventResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> LaunchEventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return LaunchEventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LaunchEventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return LaunchEventResourceWithStreamingResponse(self)


class AsyncLaunchEventResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLaunchEventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLaunchEventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLaunchEventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncLaunchEventResourceWithStreamingResponse(self)


class LaunchEventResourceWithRawResponse:
    def __init__(self, launch_event: LaunchEventResource) -> None:
        self._launch_event = launch_event

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._launch_event.history)


class AsyncLaunchEventResourceWithRawResponse:
    def __init__(self, launch_event: AsyncLaunchEventResource) -> None:
        self._launch_event = launch_event

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._launch_event.history)


class LaunchEventResourceWithStreamingResponse:
    def __init__(self, launch_event: LaunchEventResource) -> None:
        self._launch_event = launch_event

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._launch_event.history)


class AsyncLaunchEventResourceWithStreamingResponse:
    def __init__(self, launch_event: AsyncLaunchEventResource) -> None:
        self._launch_event = launch_event

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._launch_event.history)
