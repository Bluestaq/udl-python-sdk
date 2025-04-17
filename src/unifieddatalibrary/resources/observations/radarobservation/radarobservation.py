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

__all__ = ["RadarobservationResource", "AsyncRadarobservationResource"]


class RadarobservationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> RadarobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RadarobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RadarobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return RadarobservationResourceWithStreamingResponse(self)


class AsyncRadarobservationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRadarobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRadarobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRadarobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncRadarobservationResourceWithStreamingResponse(self)


class RadarobservationResourceWithRawResponse:
    def __init__(self, radarobservation: RadarobservationResource) -> None:
        self._radarobservation = radarobservation

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._radarobservation.history)


class AsyncRadarobservationResourceWithRawResponse:
    def __init__(self, radarobservation: AsyncRadarobservationResource) -> None:
        self._radarobservation = radarobservation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._radarobservation.history)


class RadarobservationResourceWithStreamingResponse:
    def __init__(self, radarobservation: RadarobservationResource) -> None:
        self._radarobservation = radarobservation

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._radarobservation.history)


class AsyncRadarobservationResourceWithStreamingResponse:
    def __init__(self, radarobservation: AsyncRadarobservationResource) -> None:
        self._radarobservation = radarobservation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._radarobservation.history)
