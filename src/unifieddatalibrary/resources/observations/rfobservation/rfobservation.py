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

__all__ = ["RfobservationResource", "AsyncRfobservationResource"]


class RfobservationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> RfobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RfobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RfobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return RfobservationResourceWithStreamingResponse(self)


class AsyncRfobservationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRfobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRfobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRfobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncRfobservationResourceWithStreamingResponse(self)


class RfobservationResourceWithRawResponse:
    def __init__(self, rfobservation: RfobservationResource) -> None:
        self._rfobservation = rfobservation

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._rfobservation.history)


class AsyncRfobservationResourceWithRawResponse:
    def __init__(self, rfobservation: AsyncRfobservationResource) -> None:
        self._rfobservation = rfobservation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._rfobservation.history)


class RfobservationResourceWithStreamingResponse:
    def __init__(self, rfobservation: RfobservationResource) -> None:
        self._rfobservation = rfobservation

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._rfobservation.history)


class AsyncRfobservationResourceWithStreamingResponse:
    def __init__(self, rfobservation: AsyncRfobservationResource) -> None:
        self._rfobservation = rfobservation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._rfobservation.history)
