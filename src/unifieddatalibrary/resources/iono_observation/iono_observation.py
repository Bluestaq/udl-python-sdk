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

__all__ = ["IonoObservationResource", "AsyncIonoObservationResource"]


class IonoObservationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> IonoObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return IonoObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IonoObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return IonoObservationResourceWithStreamingResponse(self)


class AsyncIonoObservationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIonoObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIonoObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIonoObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncIonoObservationResourceWithStreamingResponse(self)


class IonoObservationResourceWithRawResponse:
    def __init__(self, iono_observation: IonoObservationResource) -> None:
        self._iono_observation = iono_observation

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._iono_observation.history)


class AsyncIonoObservationResourceWithRawResponse:
    def __init__(self, iono_observation: AsyncIonoObservationResource) -> None:
        self._iono_observation = iono_observation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._iono_observation.history)


class IonoObservationResourceWithStreamingResponse:
    def __init__(self, iono_observation: IonoObservationResource) -> None:
        self._iono_observation = iono_observation

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._iono_observation.history)


class AsyncIonoObservationResourceWithStreamingResponse:
    def __init__(self, iono_observation: AsyncIonoObservationResource) -> None:
        self._iono_observation = iono_observation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._iono_observation.history)
