# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .swir import (
    SwirResource,
    AsyncSwirResource,
    SwirResourceWithRawResponse,
    AsyncSwirResourceWithRawResponse,
    SwirResourceWithStreamingResponse,
    AsyncSwirResourceWithStreamingResponse,
)
from .ecpsdr import (
    EcpsdrResource,
    AsyncEcpsdrResource,
    EcpsdrResourceWithRawResponse,
    AsyncEcpsdrResourceWithRawResponse,
    EcpsdrResourceWithStreamingResponse,
    AsyncEcpsdrResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .monoradar.monoradar import (
    MonoradarResource,
    AsyncMonoradarResource,
    MonoradarResourceWithRawResponse,
    AsyncMonoradarResourceWithRawResponse,
    MonoradarResourceWithStreamingResponse,
    AsyncMonoradarResourceWithStreamingResponse,
)
from .rf_observation.rf_observation import (
    RfObservationResource,
    AsyncRfObservationResource,
    RfObservationResourceWithRawResponse,
    AsyncRfObservationResourceWithRawResponse,
    RfObservationResourceWithStreamingResponse,
    AsyncRfObservationResourceWithStreamingResponse,
)
from .eo_observations.eo_observations import (
    EoObservationsResource,
    AsyncEoObservationsResource,
    EoObservationsResourceWithRawResponse,
    AsyncEoObservationsResourceWithRawResponse,
    EoObservationsResourceWithStreamingResponse,
    AsyncEoObservationsResourceWithStreamingResponse,
)
from .radarobservation.radarobservation import (
    RadarobservationResource,
    AsyncRadarobservationResource,
    RadarobservationResourceWithRawResponse,
    AsyncRadarobservationResourceWithRawResponse,
    RadarobservationResourceWithStreamingResponse,
    AsyncRadarobservationResourceWithStreamingResponse,
)
from .passive_radar_observation.passive_radar_observation import (
    PassiveRadarObservationResource,
    AsyncPassiveRadarObservationResource,
    PassiveRadarObservationResourceWithRawResponse,
    AsyncPassiveRadarObservationResourceWithRawResponse,
    PassiveRadarObservationResourceWithStreamingResponse,
    AsyncPassiveRadarObservationResourceWithStreamingResponse,
)

__all__ = ["ObservationsResource", "AsyncObservationsResource"]


class ObservationsResource(SyncAPIResource):
    @cached_property
    def ecpsdr(self) -> EcpsdrResource:
        return EcpsdrResource(self._client)

    @cached_property
    def monoradar(self) -> MonoradarResource:
        return MonoradarResource(self._client)

    @cached_property
    def swir(self) -> SwirResource:
        return SwirResource(self._client)

    @cached_property
    def radarobservation(self) -> RadarobservationResource:
        return RadarobservationResource(self._client)

    @cached_property
    def rf_observation(self) -> RfObservationResource:
        return RfObservationResource(self._client)

    @cached_property
    def passive_radar_observation(self) -> PassiveRadarObservationResource:
        return PassiveRadarObservationResource(self._client)

    @cached_property
    def eo_observations(self) -> EoObservationsResource:
        return EoObservationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ObservationsResourceWithStreamingResponse(self)


class AsyncObservationsResource(AsyncAPIResource):
    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResource:
        return AsyncEcpsdrResource(self._client)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResource:
        return AsyncMonoradarResource(self._client)

    @cached_property
    def swir(self) -> AsyncSwirResource:
        return AsyncSwirResource(self._client)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResource:
        return AsyncRadarobservationResource(self._client)

    @cached_property
    def rf_observation(self) -> AsyncRfObservationResource:
        return AsyncRfObservationResource(self._client)

    @cached_property
    def passive_radar_observation(self) -> AsyncPassiveRadarObservationResource:
        return AsyncPassiveRadarObservationResource(self._client)

    @cached_property
    def eo_observations(self) -> AsyncEoObservationsResource:
        return AsyncEoObservationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncObservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncObservationsResourceWithStreamingResponse(self)


class ObservationsResourceWithRawResponse:
    def __init__(self, observations: ObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> EcpsdrResourceWithRawResponse:
        return EcpsdrResourceWithRawResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> MonoradarResourceWithRawResponse:
        return MonoradarResourceWithRawResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> SwirResourceWithRawResponse:
        return SwirResourceWithRawResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> RadarobservationResourceWithRawResponse:
        return RadarobservationResourceWithRawResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> RfObservationResourceWithRawResponse:
        return RfObservationResourceWithRawResponse(self._observations.rf_observation)

    @cached_property
    def passive_radar_observation(self) -> PassiveRadarObservationResourceWithRawResponse:
        return PassiveRadarObservationResourceWithRawResponse(self._observations.passive_radar_observation)

    @cached_property
    def eo_observations(self) -> EoObservationsResourceWithRawResponse:
        return EoObservationsResourceWithRawResponse(self._observations.eo_observations)


class AsyncObservationsResourceWithRawResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResourceWithRawResponse:
        return AsyncEcpsdrResourceWithRawResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResourceWithRawResponse:
        return AsyncMonoradarResourceWithRawResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> AsyncSwirResourceWithRawResponse:
        return AsyncSwirResourceWithRawResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResourceWithRawResponse:
        return AsyncRadarobservationResourceWithRawResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> AsyncRfObservationResourceWithRawResponse:
        return AsyncRfObservationResourceWithRawResponse(self._observations.rf_observation)

    @cached_property
    def passive_radar_observation(self) -> AsyncPassiveRadarObservationResourceWithRawResponse:
        return AsyncPassiveRadarObservationResourceWithRawResponse(self._observations.passive_radar_observation)

    @cached_property
    def eo_observations(self) -> AsyncEoObservationsResourceWithRawResponse:
        return AsyncEoObservationsResourceWithRawResponse(self._observations.eo_observations)


class ObservationsResourceWithStreamingResponse:
    def __init__(self, observations: ObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> EcpsdrResourceWithStreamingResponse:
        return EcpsdrResourceWithStreamingResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> MonoradarResourceWithStreamingResponse:
        return MonoradarResourceWithStreamingResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> SwirResourceWithStreamingResponse:
        return SwirResourceWithStreamingResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> RadarobservationResourceWithStreamingResponse:
        return RadarobservationResourceWithStreamingResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> RfObservationResourceWithStreamingResponse:
        return RfObservationResourceWithStreamingResponse(self._observations.rf_observation)

    @cached_property
    def passive_radar_observation(self) -> PassiveRadarObservationResourceWithStreamingResponse:
        return PassiveRadarObservationResourceWithStreamingResponse(self._observations.passive_radar_observation)

    @cached_property
    def eo_observations(self) -> EoObservationsResourceWithStreamingResponse:
        return EoObservationsResourceWithStreamingResponse(self._observations.eo_observations)


class AsyncObservationsResourceWithStreamingResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResourceWithStreamingResponse:
        return AsyncEcpsdrResourceWithStreamingResponse(self._observations.ecpsdr)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResourceWithStreamingResponse:
        return AsyncMonoradarResourceWithStreamingResponse(self._observations.monoradar)

    @cached_property
    def swir(self) -> AsyncSwirResourceWithStreamingResponse:
        return AsyncSwirResourceWithStreamingResponse(self._observations.swir)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResourceWithStreamingResponse:
        return AsyncRadarobservationResourceWithStreamingResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> AsyncRfObservationResourceWithStreamingResponse:
        return AsyncRfObservationResourceWithStreamingResponse(self._observations.rf_observation)

    @cached_property
    def passive_radar_observation(self) -> AsyncPassiveRadarObservationResourceWithStreamingResponse:
        return AsyncPassiveRadarObservationResourceWithStreamingResponse(self._observations.passive_radar_observation)

    @cached_property
    def eo_observations(self) -> AsyncEoObservationsResourceWithStreamingResponse:
        return AsyncEoObservationsResourceWithStreamingResponse(self._observations.eo_observations)
