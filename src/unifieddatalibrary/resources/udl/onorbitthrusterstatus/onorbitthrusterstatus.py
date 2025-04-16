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

__all__ = ["OnorbitthrusterstatusResource", "AsyncOnorbitthrusterstatusResource"]


class OnorbitthrusterstatusResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> OnorbitthrusterstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnorbitthrusterstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnorbitthrusterstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return OnorbitthrusterstatusResourceWithStreamingResponse(self)


class AsyncOnorbitthrusterstatusResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOnorbitthrusterstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnorbitthrusterstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnorbitthrusterstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOnorbitthrusterstatusResourceWithStreamingResponse(self)


class OnorbitthrusterstatusResourceWithRawResponse:
    def __init__(self, onorbitthrusterstatus: OnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._onorbitthrusterstatus.history)


class AsyncOnorbitthrusterstatusResourceWithRawResponse:
    def __init__(self, onorbitthrusterstatus: AsyncOnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._onorbitthrusterstatus.history)


class OnorbitthrusterstatusResourceWithStreamingResponse:
    def __init__(self, onorbitthrusterstatus: OnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._onorbitthrusterstatus.history)


class AsyncOnorbitthrusterstatusResourceWithStreamingResponse:
    def __init__(self, onorbitthrusterstatus: AsyncOnorbitthrusterstatusResource) -> None:
        self._onorbitthrusterstatus = onorbitthrusterstatus

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._onorbitthrusterstatus.history)
