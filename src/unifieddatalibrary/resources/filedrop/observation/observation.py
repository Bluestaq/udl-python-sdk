# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rf import (
    RfResource,
    AsyncRfResource,
    RfResourceWithRawResponse,
    AsyncRfResourceWithRawResponse,
    RfResourceWithStreamingResponse,
    AsyncRfResourceWithStreamingResponse,
)
from .radar import (
    RadarResource,
    AsyncRadarResource,
    RadarResourceWithRawResponse,
    AsyncRadarResourceWithRawResponse,
    RadarResourceWithStreamingResponse,
    AsyncRadarResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .passive_radar import (
    PassiveRadarResource,
    AsyncPassiveRadarResource,
    PassiveRadarResourceWithRawResponse,
    AsyncPassiveRadarResourceWithRawResponse,
    PassiveRadarResourceWithStreamingResponse,
    AsyncPassiveRadarResourceWithStreamingResponse,
)
from .onboardnavigation import (
    OnboardnavigationResource,
    AsyncOnboardnavigationResource,
    OnboardnavigationResourceWithRawResponse,
    AsyncOnboardnavigationResourceWithRawResponse,
    OnboardnavigationResourceWithStreamingResponse,
    AsyncOnboardnavigationResourceWithStreamingResponse,
)

__all__ = ["ObservationResource", "AsyncObservationResource"]


class ObservationResource(SyncAPIResource):
    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResource:
        return OnboardnavigationResource(self._client)

    @cached_property
    def passive_radar(self) -> PassiveRadarResource:
        return PassiveRadarResource(self._client)

    @cached_property
    def radar(self) -> RadarResource:
        return RadarResource(self._client)

    @cached_property
    def rf(self) -> RfResource:
        return RfResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return ObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return ObservationResourceWithStreamingResponse(self)


class AsyncObservationResource(AsyncAPIResource):
    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResource:
        return AsyncOnboardnavigationResource(self._client)

    @cached_property
    def passive_radar(self) -> AsyncPassiveRadarResource:
        return AsyncPassiveRadarResource(self._client)

    @cached_property
    def radar(self) -> AsyncRadarResource:
        return AsyncRadarResource(self._client)

    @cached_property
    def rf(self) -> AsyncRfResource:
        return AsyncRfResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncObservationResourceWithStreamingResponse(self)


class ObservationResourceWithRawResponse:
    def __init__(self, observation: ObservationResource) -> None:
        self._observation = observation

    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResourceWithRawResponse:
        return OnboardnavigationResourceWithRawResponse(self._observation.onboardnavigation)

    @cached_property
    def passive_radar(self) -> PassiveRadarResourceWithRawResponse:
        return PassiveRadarResourceWithRawResponse(self._observation.passive_radar)

    @cached_property
    def radar(self) -> RadarResourceWithRawResponse:
        return RadarResourceWithRawResponse(self._observation.radar)

    @cached_property
    def rf(self) -> RfResourceWithRawResponse:
        return RfResourceWithRawResponse(self._observation.rf)


class AsyncObservationResourceWithRawResponse:
    def __init__(self, observation: AsyncObservationResource) -> None:
        self._observation = observation

    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResourceWithRawResponse:
        return AsyncOnboardnavigationResourceWithRawResponse(self._observation.onboardnavigation)

    @cached_property
    def passive_radar(self) -> AsyncPassiveRadarResourceWithRawResponse:
        return AsyncPassiveRadarResourceWithRawResponse(self._observation.passive_radar)

    @cached_property
    def radar(self) -> AsyncRadarResourceWithRawResponse:
        return AsyncRadarResourceWithRawResponse(self._observation.radar)

    @cached_property
    def rf(self) -> AsyncRfResourceWithRawResponse:
        return AsyncRfResourceWithRawResponse(self._observation.rf)


class ObservationResourceWithStreamingResponse:
    def __init__(self, observation: ObservationResource) -> None:
        self._observation = observation

    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResourceWithStreamingResponse:
        return OnboardnavigationResourceWithStreamingResponse(self._observation.onboardnavigation)

    @cached_property
    def passive_radar(self) -> PassiveRadarResourceWithStreamingResponse:
        return PassiveRadarResourceWithStreamingResponse(self._observation.passive_radar)

    @cached_property
    def radar(self) -> RadarResourceWithStreamingResponse:
        return RadarResourceWithStreamingResponse(self._observation.radar)

    @cached_property
    def rf(self) -> RfResourceWithStreamingResponse:
        return RfResourceWithStreamingResponse(self._observation.rf)


class AsyncObservationResourceWithStreamingResponse:
    def __init__(self, observation: AsyncObservationResource) -> None:
        self._observation = observation

    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResourceWithStreamingResponse:
        return AsyncOnboardnavigationResourceWithStreamingResponse(self._observation.onboardnavigation)

    @cached_property
    def passive_radar(self) -> AsyncPassiveRadarResourceWithStreamingResponse:
        return AsyncPassiveRadarResourceWithStreamingResponse(self._observation.passive_radar)

    @cached_property
    def radar(self) -> AsyncRadarResourceWithStreamingResponse:
        return AsyncRadarResourceWithStreamingResponse(self._observation.radar)

    @cached_property
    def rf(self) -> AsyncRfResourceWithStreamingResponse:
        return AsyncRfResourceWithStreamingResponse(self._observation.rf)
