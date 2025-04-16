# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .mti.mti import (
    MtiResource,
    AsyncMtiResource,
    MtiResourceWithRawResponse,
    AsyncMtiResourceWithRawResponse,
    MtiResourceWithStreamingResponse,
    AsyncMtiResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .geostatus.geostatus import (
    GeostatusResource,
    AsyncGeostatusResource,
    GeostatusResourceWithRawResponse,
    AsyncGeostatusResourceWithRawResponse,
    GeostatusResourceWithStreamingResponse,
    AsyncGeostatusResourceWithStreamingResponse,
)
from .notification.notification import (
    NotificationResource,
    AsyncNotificationResource,
    NotificationResourceWithRawResponse,
    AsyncNotificationResourceWithRawResponse,
    NotificationResourceWithStreamingResponse,
    AsyncNotificationResourceWithStreamingResponse,
)
from .onboardnavigation.onboardnavigation import (
    OnboardnavigationResource,
    AsyncOnboardnavigationResource,
    OnboardnavigationResourceWithRawResponse,
    AsyncOnboardnavigationResourceWithRawResponse,
    OnboardnavigationResourceWithStreamingResponse,
    AsyncOnboardnavigationResourceWithStreamingResponse,
)
from .gnssobservationset.gnssobservationset import (
    GnssobservationsetResource,
    AsyncGnssobservationsetResource,
    GnssobservationsetResourceWithRawResponse,
    AsyncGnssobservationsetResourceWithRawResponse,
    GnssobservationsetResourceWithStreamingResponse,
    AsyncGnssobservationsetResourceWithStreamingResponse,
)
from .onorbitthrusterstatus.onorbitthrusterstatus import (
    OnorbitthrusterstatusResource,
    AsyncOnorbitthrusterstatusResource,
    OnorbitthrusterstatusResourceWithRawResponse,
    AsyncOnorbitthrusterstatusResourceWithRawResponse,
    OnorbitthrusterstatusResourceWithStreamingResponse,
    AsyncOnorbitthrusterstatusResourceWithStreamingResponse,
)

__all__ = ["UdlResource", "AsyncUdlResource"]


class UdlResource(SyncAPIResource):
    @cached_property
    def geostatus(self) -> GeostatusResource:
        return GeostatusResource(self._client)

    @cached_property
    def gnssobservationset(self) -> GnssobservationsetResource:
        return GnssobservationsetResource(self._client)

    @cached_property
    def mti(self) -> MtiResource:
        return MtiResource(self._client)

    @cached_property
    def notification(self) -> NotificationResource:
        return NotificationResource(self._client)

    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResource:
        return OnboardnavigationResource(self._client)

    @cached_property
    def onorbitthrusterstatus(self) -> OnorbitthrusterstatusResource:
        return OnorbitthrusterstatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> UdlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UdlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UdlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return UdlResourceWithStreamingResponse(self)


class AsyncUdlResource(AsyncAPIResource):
    @cached_property
    def geostatus(self) -> AsyncGeostatusResource:
        return AsyncGeostatusResource(self._client)

    @cached_property
    def gnssobservationset(self) -> AsyncGnssobservationsetResource:
        return AsyncGnssobservationsetResource(self._client)

    @cached_property
    def mti(self) -> AsyncMtiResource:
        return AsyncMtiResource(self._client)

    @cached_property
    def notification(self) -> AsyncNotificationResource:
        return AsyncNotificationResource(self._client)

    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResource:
        return AsyncOnboardnavigationResource(self._client)

    @cached_property
    def onorbitthrusterstatus(self) -> AsyncOnorbitthrusterstatusResource:
        return AsyncOnorbitthrusterstatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUdlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUdlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUdlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncUdlResourceWithStreamingResponse(self)


class UdlResourceWithRawResponse:
    def __init__(self, udl: UdlResource) -> None:
        self._udl = udl

    @cached_property
    def geostatus(self) -> GeostatusResourceWithRawResponse:
        return GeostatusResourceWithRawResponse(self._udl.geostatus)

    @cached_property
    def gnssobservationset(self) -> GnssobservationsetResourceWithRawResponse:
        return GnssobservationsetResourceWithRawResponse(self._udl.gnssobservationset)

    @cached_property
    def mti(self) -> MtiResourceWithRawResponse:
        return MtiResourceWithRawResponse(self._udl.mti)

    @cached_property
    def notification(self) -> NotificationResourceWithRawResponse:
        return NotificationResourceWithRawResponse(self._udl.notification)

    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResourceWithRawResponse:
        return OnboardnavigationResourceWithRawResponse(self._udl.onboardnavigation)

    @cached_property
    def onorbitthrusterstatus(self) -> OnorbitthrusterstatusResourceWithRawResponse:
        return OnorbitthrusterstatusResourceWithRawResponse(self._udl.onorbitthrusterstatus)


class AsyncUdlResourceWithRawResponse:
    def __init__(self, udl: AsyncUdlResource) -> None:
        self._udl = udl

    @cached_property
    def geostatus(self) -> AsyncGeostatusResourceWithRawResponse:
        return AsyncGeostatusResourceWithRawResponse(self._udl.geostatus)

    @cached_property
    def gnssobservationset(self) -> AsyncGnssobservationsetResourceWithRawResponse:
        return AsyncGnssobservationsetResourceWithRawResponse(self._udl.gnssobservationset)

    @cached_property
    def mti(self) -> AsyncMtiResourceWithRawResponse:
        return AsyncMtiResourceWithRawResponse(self._udl.mti)

    @cached_property
    def notification(self) -> AsyncNotificationResourceWithRawResponse:
        return AsyncNotificationResourceWithRawResponse(self._udl.notification)

    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResourceWithRawResponse:
        return AsyncOnboardnavigationResourceWithRawResponse(self._udl.onboardnavigation)

    @cached_property
    def onorbitthrusterstatus(self) -> AsyncOnorbitthrusterstatusResourceWithRawResponse:
        return AsyncOnorbitthrusterstatusResourceWithRawResponse(self._udl.onorbitthrusterstatus)


class UdlResourceWithStreamingResponse:
    def __init__(self, udl: UdlResource) -> None:
        self._udl = udl

    @cached_property
    def geostatus(self) -> GeostatusResourceWithStreamingResponse:
        return GeostatusResourceWithStreamingResponse(self._udl.geostatus)

    @cached_property
    def gnssobservationset(self) -> GnssobservationsetResourceWithStreamingResponse:
        return GnssobservationsetResourceWithStreamingResponse(self._udl.gnssobservationset)

    @cached_property
    def mti(self) -> MtiResourceWithStreamingResponse:
        return MtiResourceWithStreamingResponse(self._udl.mti)

    @cached_property
    def notification(self) -> NotificationResourceWithStreamingResponse:
        return NotificationResourceWithStreamingResponse(self._udl.notification)

    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResourceWithStreamingResponse:
        return OnboardnavigationResourceWithStreamingResponse(self._udl.onboardnavigation)

    @cached_property
    def onorbitthrusterstatus(self) -> OnorbitthrusterstatusResourceWithStreamingResponse:
        return OnorbitthrusterstatusResourceWithStreamingResponse(self._udl.onorbitthrusterstatus)


class AsyncUdlResourceWithStreamingResponse:
    def __init__(self, udl: AsyncUdlResource) -> None:
        self._udl = udl

    @cached_property
    def geostatus(self) -> AsyncGeostatusResourceWithStreamingResponse:
        return AsyncGeostatusResourceWithStreamingResponse(self._udl.geostatus)

    @cached_property
    def gnssobservationset(self) -> AsyncGnssobservationsetResourceWithStreamingResponse:
        return AsyncGnssobservationsetResourceWithStreamingResponse(self._udl.gnssobservationset)

    @cached_property
    def mti(self) -> AsyncMtiResourceWithStreamingResponse:
        return AsyncMtiResourceWithStreamingResponse(self._udl.mti)

    @cached_property
    def notification(self) -> AsyncNotificationResourceWithStreamingResponse:
        return AsyncNotificationResourceWithStreamingResponse(self._udl.notification)

    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResourceWithStreamingResponse:
        return AsyncOnboardnavigationResourceWithStreamingResponse(self._udl.onboardnavigation)

    @cached_property
    def onorbitthrusterstatus(self) -> AsyncOnorbitthrusterstatusResourceWithStreamingResponse:
        return AsyncOnorbitthrusterstatusResourceWithStreamingResponse(self._udl.onorbitthrusterstatus)
