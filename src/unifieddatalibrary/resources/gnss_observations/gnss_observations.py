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

__all__ = ["GnssObservationsResource", "AsyncGnssObservationsResource"]


class GnssObservationsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> GnssObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GnssObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GnssObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return GnssObservationsResourceWithStreamingResponse(self)


class AsyncGnssObservationsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGnssObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGnssObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGnssObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncGnssObservationsResourceWithStreamingResponse(self)


class GnssObservationsResourceWithRawResponse:
    def __init__(self, gnss_observations: GnssObservationsResource) -> None:
        self._gnss_observations = gnss_observations

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._gnss_observations.history)


class AsyncGnssObservationsResourceWithRawResponse:
    def __init__(self, gnss_observations: AsyncGnssObservationsResource) -> None:
        self._gnss_observations = gnss_observations

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._gnss_observations.history)


class GnssObservationsResourceWithStreamingResponse:
    def __init__(self, gnss_observations: GnssObservationsResource) -> None:
        self._gnss_observations = gnss_observations

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._gnss_observations.history)


class AsyncGnssObservationsResourceWithStreamingResponse:
    def __init__(self, gnss_observations: AsyncGnssObservationsResource) -> None:
        self._gnss_observations = gnss_observations

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._gnss_observations.history)
