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

__all__ = ["FlightplanResource", "AsyncFlightplanResource"]


class FlightplanResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> FlightplanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return FlightplanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlightplanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return FlightplanResourceWithStreamingResponse(self)


class AsyncFlightplanResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFlightplanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlightplanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlightplanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncFlightplanResourceWithStreamingResponse(self)


class FlightplanResourceWithRawResponse:
    def __init__(self, flightplan: FlightplanResource) -> None:
        self._flightplan = flightplan

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._flightplan.history)


class AsyncFlightplanResourceWithRawResponse:
    def __init__(self, flightplan: AsyncFlightplanResource) -> None:
        self._flightplan = flightplan

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._flightplan.history)


class FlightplanResourceWithStreamingResponse:
    def __init__(self, flightplan: FlightplanResource) -> None:
        self._flightplan = flightplan

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._flightplan.history)


class AsyncFlightplanResourceWithStreamingResponse:
    def __init__(self, flightplan: AsyncFlightplanResource) -> None:
        self._flightplan = flightplan

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._flightplan.history)
