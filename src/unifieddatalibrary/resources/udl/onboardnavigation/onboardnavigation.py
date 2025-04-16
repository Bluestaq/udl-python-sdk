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

__all__ = ["OnboardnavigationResource", "AsyncOnboardnavigationResource"]


class OnboardnavigationResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> OnboardnavigationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnboardnavigationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnboardnavigationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return OnboardnavigationResourceWithStreamingResponse(self)


class AsyncOnboardnavigationResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOnboardnavigationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnboardnavigationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnboardnavigationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOnboardnavigationResourceWithStreamingResponse(self)


class OnboardnavigationResourceWithRawResponse:
    def __init__(self, onboardnavigation: OnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._onboardnavigation.history)


class AsyncOnboardnavigationResourceWithRawResponse:
    def __init__(self, onboardnavigation: AsyncOnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._onboardnavigation.history)


class OnboardnavigationResourceWithStreamingResponse:
    def __init__(self, onboardnavigation: OnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._onboardnavigation.history)


class AsyncOnboardnavigationResourceWithStreamingResponse:
    def __init__(self, onboardnavigation: AsyncOnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._onboardnavigation.history)
