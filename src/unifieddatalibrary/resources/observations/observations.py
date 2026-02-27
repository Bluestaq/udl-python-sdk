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
from .obscorrelation.obscorrelation import (
    ObscorrelationResource,
    AsyncObscorrelationResource,
    ObscorrelationResourceWithRawResponse,
    AsyncObscorrelationResourceWithRawResponse,
    ObscorrelationResourceWithStreamingResponse,
    AsyncObscorrelationResourceWithStreamingResponse,
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
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return EcpsdrResource(self._client)

    @cached_property
    def eo_observations(self) -> EoObservationsResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return EoObservationsResource(self._client)

    @cached_property
    def monoradar(self) -> MonoradarResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return MonoradarResource(self._client)

    @cached_property
    def obscorrelation(self) -> ObscorrelationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return ObscorrelationResource(self._client)

    @cached_property
    def passive_radar_observation(self) -> PassiveRadarObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return PassiveRadarObservationResource(self._client)

    @cached_property
    def radarobservation(self) -> RadarobservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return RadarobservationResource(self._client)

    @cached_property
    def rf_observation(self) -> RfObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return RfObservationResource(self._client)

    @cached_property
    def swir(self) -> SwirResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return SwirResource(self._client)

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
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncEcpsdrResource(self._client)

    @cached_property
    def eo_observations(self) -> AsyncEoObservationsResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncEoObservationsResource(self._client)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncMonoradarResource(self._client)

    @cached_property
    def obscorrelation(self) -> AsyncObscorrelationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncObscorrelationResource(self._client)

    @cached_property
    def passive_radar_observation(self) -> AsyncPassiveRadarObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncPassiveRadarObservationResource(self._client)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncRadarobservationResource(self._client)

    @cached_property
    def rf_observation(self) -> AsyncRfObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncRfObservationResource(self._client)

    @cached_property
    def swir(self) -> AsyncSwirResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncSwirResource(self._client)

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
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return EcpsdrResourceWithRawResponse(self._observations.ecpsdr)

    @cached_property
    def eo_observations(self) -> EoObservationsResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return EoObservationsResourceWithRawResponse(self._observations.eo_observations)

    @cached_property
    def monoradar(self) -> MonoradarResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return MonoradarResourceWithRawResponse(self._observations.monoradar)

    @cached_property
    def obscorrelation(self) -> ObscorrelationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return ObscorrelationResourceWithRawResponse(self._observations.obscorrelation)

    @cached_property
    def passive_radar_observation(self) -> PassiveRadarObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return PassiveRadarObservationResourceWithRawResponse(self._observations.passive_radar_observation)

    @cached_property
    def radarobservation(self) -> RadarobservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return RadarobservationResourceWithRawResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> RfObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return RfObservationResourceWithRawResponse(self._observations.rf_observation)

    @cached_property
    def swir(self) -> SwirResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return SwirResourceWithRawResponse(self._observations.swir)


class AsyncObservationsResourceWithRawResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncEcpsdrResourceWithRawResponse(self._observations.ecpsdr)

    @cached_property
    def eo_observations(self) -> AsyncEoObservationsResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncEoObservationsResourceWithRawResponse(self._observations.eo_observations)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncMonoradarResourceWithRawResponse(self._observations.monoradar)

    @cached_property
    def obscorrelation(self) -> AsyncObscorrelationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncObscorrelationResourceWithRawResponse(self._observations.obscorrelation)

    @cached_property
    def passive_radar_observation(self) -> AsyncPassiveRadarObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncPassiveRadarObservationResourceWithRawResponse(self._observations.passive_radar_observation)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncRadarobservationResourceWithRawResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> AsyncRfObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncRfObservationResourceWithRawResponse(self._observations.rf_observation)

    @cached_property
    def swir(self) -> AsyncSwirResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncSwirResourceWithRawResponse(self._observations.swir)


class ObservationsResourceWithStreamingResponse:
    def __init__(self, observations: ObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> EcpsdrResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return EcpsdrResourceWithStreamingResponse(self._observations.ecpsdr)

    @cached_property
    def eo_observations(self) -> EoObservationsResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return EoObservationsResourceWithStreamingResponse(self._observations.eo_observations)

    @cached_property
    def monoradar(self) -> MonoradarResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return MonoradarResourceWithStreamingResponse(self._observations.monoradar)

    @cached_property
    def obscorrelation(self) -> ObscorrelationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return ObscorrelationResourceWithStreamingResponse(self._observations.obscorrelation)

    @cached_property
    def passive_radar_observation(self) -> PassiveRadarObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return PassiveRadarObservationResourceWithStreamingResponse(self._observations.passive_radar_observation)

    @cached_property
    def radarobservation(self) -> RadarobservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return RadarobservationResourceWithStreamingResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> RfObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return RfObservationResourceWithStreamingResponse(self._observations.rf_observation)

    @cached_property
    def swir(self) -> SwirResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return SwirResourceWithStreamingResponse(self._observations.swir)


class AsyncObservationsResourceWithStreamingResponse:
    def __init__(self, observations: AsyncObservationsResource) -> None:
        self._observations = observations

    @cached_property
    def ecpsdr(self) -> AsyncEcpsdrResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncEcpsdrResourceWithStreamingResponse(self._observations.ecpsdr)

    @cached_property
    def eo_observations(self) -> AsyncEoObservationsResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncEoObservationsResourceWithStreamingResponse(self._observations.eo_observations)

    @cached_property
    def monoradar(self) -> AsyncMonoradarResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncMonoradarResourceWithStreamingResponse(self._observations.monoradar)

    @cached_property
    def obscorrelation(self) -> AsyncObscorrelationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncObscorrelationResourceWithStreamingResponse(self._observations.obscorrelation)

    @cached_property
    def passive_radar_observation(self) -> AsyncPassiveRadarObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncPassiveRadarObservationResourceWithStreamingResponse(self._observations.passive_radar_observation)

    @cached_property
    def radarobservation(self) -> AsyncRadarobservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncRadarobservationResourceWithStreamingResponse(self._observations.radarobservation)

    @cached_property
    def rf_observation(self) -> AsyncRfObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncRfObservationResourceWithStreamingResponse(self._observations.rf_observation)

    @cached_property
    def swir(self) -> AsyncSwirResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        return AsyncSwirResourceWithStreamingResponse(self._observations.swir)
