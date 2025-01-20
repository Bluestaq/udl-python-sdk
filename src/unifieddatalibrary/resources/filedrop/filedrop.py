# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .eo import (
    EoResource,
    AsyncEoResource,
    EoResourceWithRawResponse,
    AsyncEoResourceWithRawResponse,
    EoResourceWithStreamingResponse,
    AsyncEoResourceWithStreamingResponse,
)
from .mti import (
    MtiResource,
    AsyncMtiResource,
    MtiResourceWithRawResponse,
    AsyncMtiResourceWithRawResponse,
    MtiResourceWithStreamingResponse,
    AsyncMtiResourceWithStreamingResponse,
)
from .evac import (
    EvacResource,
    AsyncEvacResource,
    EvacResourceWithRawResponse,
    AsyncEvacResourceWithRawResponse,
    EvacResourceWithStreamingResponse,
    AsyncEvacResourceWithStreamingResponse,
)
from .elsets import (
    ElsetsResource,
    AsyncElsetsResource,
    ElsetsResourceWithRawResponse,
    AsyncElsetsResourceWithRawResponse,
    ElsetsResourceWithStreamingResponse,
    AsyncElsetsResourceWithStreamingResponse,
)
from .tracks import (
    TracksResource,
    AsyncTracksResource,
    TracksResourceWithRawResponse,
    AsyncTracksResourceWithRawResponse,
    TracksResourceWithStreamingResponse,
    AsyncTracksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .ephemeris import (
    EphemerisResource,
    AsyncEphemerisResource,
    EphemerisResourceWithRawResponse,
    AsyncEphemerisResourceWithRawResponse,
    EphemerisResourceWithStreamingResponse,
    AsyncEphemerisResourceWithStreamingResponse,
)
from .gnssrawif import (
    GnssrawifResource,
    AsyncGnssrawifResource,
    GnssrawifResourceWithRawResponse,
    AsyncGnssrawifResourceWithRawResponse,
    GnssrawifResourceWithStreamingResponse,
    AsyncGnssrawifResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .flightplans import (
    FlightplansResource,
    AsyncFlightplansResource,
    FlightplansResourceWithRawResponse,
    AsyncFlightplansResourceWithRawResponse,
    FlightplansResourceWithStreamingResponse,
    AsyncFlightplansResourceWithStreamingResponse,
)
from .orbit_track import (
    OrbitTrackResource,
    AsyncOrbitTrackResource,
    OrbitTrackResourceWithRawResponse,
    AsyncOrbitTrackResourceWithRawResponse,
    OrbitTrackResourceWithStreamingResponse,
    AsyncOrbitTrackResourceWithStreamingResponse,
)
from .trackroutes import (
    TrackroutesResource,
    AsyncTrackroutesResource,
    TrackroutesResourceWithRawResponse,
    AsyncTrackroutesResourceWithRawResponse,
    TrackroutesResourceWithStreamingResponse,
    AsyncTrackroutesResourceWithStreamingResponse,
)
from .weather_data import (
    WeatherDataResource,
    AsyncWeatherDataResource,
    WeatherDataResourceWithRawResponse,
    AsyncWeatherDataResourceWithRawResponse,
    WeatherDataResourceWithStreamingResponse,
    AsyncWeatherDataResourceWithStreamingResponse,
)
from .state_vectors import (
    StateVectorsResource,
    AsyncStateVectorsResource,
    StateVectorsResourceWithRawResponse,
    AsyncStateVectorsResourceWithRawResponse,
    StateVectorsResourceWithStreamingResponse,
    AsyncStateVectorsResourceWithStreamingResponse,
)
from .effectrequests import (
    EffectrequestsResource,
    AsyncEffectrequestsResource,
    EffectrequestsResourceWithRawResponse,
    AsyncEffectrequestsResourceWithRawResponse,
    EffectrequestsResourceWithStreamingResponse,
    AsyncEffectrequestsResourceWithStreamingResponse,
)
from .effectresponses import (
    EffectresponsesResource,
    AsyncEffectresponsesResource,
    EffectresponsesResourceWithRawResponse,
    AsyncEffectresponsesResourceWithRawResponse,
    EffectresponsesResourceWithStreamingResponse,
    AsyncEffectresponsesResourceWithStreamingResponse,
)
from .eventevolutions import (
    EventevolutionsResource,
    AsyncEventevolutionsResource,
    EventevolutionsResourceWithRawResponse,
    AsyncEventevolutionsResourceWithRawResponse,
    EventevolutionsResourceWithStreamingResponse,
    AsyncEventevolutionsResourceWithStreamingResponse,
)
from .weather_reports import (
    WeatherReportsResource,
    AsyncWeatherReportsResource,
    WeatherReportsResourceWithRawResponse,
    AsyncWeatherReportsResourceWithRawResponse,
    WeatherReportsResourceWithStreamingResponse,
    AsyncWeatherReportsResourceWithStreamingResponse,
)
from .gnssobservations import (
    GnssobservationsResource,
    AsyncGnssobservationsResource,
    GnssobservationsResourceWithRawResponse,
    AsyncGnssobservationsResourceWithRawResponse,
    GnssobservationsResourceWithStreamingResponse,
    AsyncGnssobservationsResourceWithStreamingResponse,
)
from .orbit_determination import (
    OrbitDeterminationResource,
    AsyncOrbitDeterminationResource,
    OrbitDeterminationResourceWithRawResponse,
    AsyncOrbitDeterminationResourceWithRawResponse,
    OrbitDeterminationResourceWithStreamingResponse,
    AsyncOrbitDeterminationResourceWithStreamingResponse,
)
from .surfaceobstructions import (
    SurfaceobstructionsResource,
    AsyncSurfaceobstructionsResource,
    SurfaceobstructionsResourceWithRawResponse,
    AsyncSurfaceobstructionsResourceWithRawResponse,
    SurfaceobstructionsResourceWithStreamingResponse,
    AsyncSurfaceobstructionsResourceWithStreamingResponse,
)
from .mission_ops.mission_ops import (
    MissionOpsResource,
    AsyncMissionOpsResource,
    MissionOpsResourceWithRawResponse,
    AsyncMissionOpsResourceWithRawResponse,
    MissionOpsResourceWithStreamingResponse,
    AsyncMissionOpsResourceWithStreamingResponse,
)
from .observation.observation import (
    ObservationResource,
    AsyncObservationResource,
    ObservationResourceWithRawResponse,
    AsyncObservationResourceWithRawResponse,
    ObservationResourceWithStreamingResponse,
    AsyncObservationResourceWithStreamingResponse,
)
from .report_and_activity.report_and_activity import (
    ReportAndActivityResource,
    AsyncReportAndActivityResource,
    ReportAndActivityResourceWithRawResponse,
    AsyncReportAndActivityResourceWithRawResponse,
    ReportAndActivityResourceWithStreamingResponse,
    AsyncReportAndActivityResourceWithStreamingResponse,
)

__all__ = ["FiledropResource", "AsyncFiledropResource"]


class FiledropResource(SyncAPIResource):
    @cached_property
    def effectrequests(self) -> EffectrequestsResource:
        return EffectrequestsResource(self._client)

    @cached_property
    def effectresponses(self) -> EffectresponsesResource:
        return EffectresponsesResource(self._client)

    @cached_property
    def elsets(self) -> ElsetsResource:
        return ElsetsResource(self._client)

    @cached_property
    def eo(self) -> EoResource:
        return EoResource(self._client)

    @cached_property
    def ephemeris(self) -> EphemerisResource:
        return EphemerisResource(self._client)

    @cached_property
    def evac(self) -> EvacResource:
        return EvacResource(self._client)

    @cached_property
    def eventevolutions(self) -> EventevolutionsResource:
        return EventevolutionsResource(self._client)

    @cached_property
    def flightplans(self) -> FlightplansResource:
        return FlightplansResource(self._client)

    @cached_property
    def gnssobservations(self) -> GnssobservationsResource:
        return GnssobservationsResource(self._client)

    @cached_property
    def gnssrawif(self) -> GnssrawifResource:
        return GnssrawifResource(self._client)

    @cached_property
    def mti(self) -> MtiResource:
        return MtiResource(self._client)

    @cached_property
    def observation(self) -> ObservationResource:
        return ObservationResource(self._client)

    @cached_property
    def orbit_determination(self) -> OrbitDeterminationResource:
        return OrbitDeterminationResource(self._client)

    @cached_property
    def orbit_track(self) -> OrbitTrackResource:
        return OrbitTrackResource(self._client)

    @cached_property
    def mission_ops(self) -> MissionOpsResource:
        return MissionOpsResource(self._client)

    @cached_property
    def report_and_activity(self) -> ReportAndActivityResource:
        return ReportAndActivityResource(self._client)

    @cached_property
    def surfaceobstructions(self) -> SurfaceobstructionsResource:
        return SurfaceobstructionsResource(self._client)

    @cached_property
    def state_vectors(self) -> StateVectorsResource:
        return StateVectorsResource(self._client)

    @cached_property
    def trackroutes(self) -> TrackroutesResource:
        return TrackroutesResource(self._client)

    @cached_property
    def tracks(self) -> TracksResource:
        return TracksResource(self._client)

    @cached_property
    def weather_data(self) -> WeatherDataResource:
        return WeatherDataResource(self._client)

    @cached_property
    def weather_reports(self) -> WeatherReportsResource:
        return WeatherReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FiledropResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return FiledropResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiledropResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return FiledropResourceWithStreamingResponse(self)


class AsyncFiledropResource(AsyncAPIResource):
    @cached_property
    def effectrequests(self) -> AsyncEffectrequestsResource:
        return AsyncEffectrequestsResource(self._client)

    @cached_property
    def effectresponses(self) -> AsyncEffectresponsesResource:
        return AsyncEffectresponsesResource(self._client)

    @cached_property
    def elsets(self) -> AsyncElsetsResource:
        return AsyncElsetsResource(self._client)

    @cached_property
    def eo(self) -> AsyncEoResource:
        return AsyncEoResource(self._client)

    @cached_property
    def ephemeris(self) -> AsyncEphemerisResource:
        return AsyncEphemerisResource(self._client)

    @cached_property
    def evac(self) -> AsyncEvacResource:
        return AsyncEvacResource(self._client)

    @cached_property
    def eventevolutions(self) -> AsyncEventevolutionsResource:
        return AsyncEventevolutionsResource(self._client)

    @cached_property
    def flightplans(self) -> AsyncFlightplansResource:
        return AsyncFlightplansResource(self._client)

    @cached_property
    def gnssobservations(self) -> AsyncGnssobservationsResource:
        return AsyncGnssobservationsResource(self._client)

    @cached_property
    def gnssrawif(self) -> AsyncGnssrawifResource:
        return AsyncGnssrawifResource(self._client)

    @cached_property
    def mti(self) -> AsyncMtiResource:
        return AsyncMtiResource(self._client)

    @cached_property
    def observation(self) -> AsyncObservationResource:
        return AsyncObservationResource(self._client)

    @cached_property
    def orbit_determination(self) -> AsyncOrbitDeterminationResource:
        return AsyncOrbitDeterminationResource(self._client)

    @cached_property
    def orbit_track(self) -> AsyncOrbitTrackResource:
        return AsyncOrbitTrackResource(self._client)

    @cached_property
    def mission_ops(self) -> AsyncMissionOpsResource:
        return AsyncMissionOpsResource(self._client)

    @cached_property
    def report_and_activity(self) -> AsyncReportAndActivityResource:
        return AsyncReportAndActivityResource(self._client)

    @cached_property
    def surfaceobstructions(self) -> AsyncSurfaceobstructionsResource:
        return AsyncSurfaceobstructionsResource(self._client)

    @cached_property
    def state_vectors(self) -> AsyncStateVectorsResource:
        return AsyncStateVectorsResource(self._client)

    @cached_property
    def trackroutes(self) -> AsyncTrackroutesResource:
        return AsyncTrackroutesResource(self._client)

    @cached_property
    def tracks(self) -> AsyncTracksResource:
        return AsyncTracksResource(self._client)

    @cached_property
    def weather_data(self) -> AsyncWeatherDataResource:
        return AsyncWeatherDataResource(self._client)

    @cached_property
    def weather_reports(self) -> AsyncWeatherReportsResource:
        return AsyncWeatherReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFiledropResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiledropResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiledropResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncFiledropResourceWithStreamingResponse(self)


class FiledropResourceWithRawResponse:
    def __init__(self, filedrop: FiledropResource) -> None:
        self._filedrop = filedrop

    @cached_property
    def effectrequests(self) -> EffectrequestsResourceWithRawResponse:
        return EffectrequestsResourceWithRawResponse(self._filedrop.effectrequests)

    @cached_property
    def effectresponses(self) -> EffectresponsesResourceWithRawResponse:
        return EffectresponsesResourceWithRawResponse(self._filedrop.effectresponses)

    @cached_property
    def elsets(self) -> ElsetsResourceWithRawResponse:
        return ElsetsResourceWithRawResponse(self._filedrop.elsets)

    @cached_property
    def eo(self) -> EoResourceWithRawResponse:
        return EoResourceWithRawResponse(self._filedrop.eo)

    @cached_property
    def ephemeris(self) -> EphemerisResourceWithRawResponse:
        return EphemerisResourceWithRawResponse(self._filedrop.ephemeris)

    @cached_property
    def evac(self) -> EvacResourceWithRawResponse:
        return EvacResourceWithRawResponse(self._filedrop.evac)

    @cached_property
    def eventevolutions(self) -> EventevolutionsResourceWithRawResponse:
        return EventevolutionsResourceWithRawResponse(self._filedrop.eventevolutions)

    @cached_property
    def flightplans(self) -> FlightplansResourceWithRawResponse:
        return FlightplansResourceWithRawResponse(self._filedrop.flightplans)

    @cached_property
    def gnssobservations(self) -> GnssobservationsResourceWithRawResponse:
        return GnssobservationsResourceWithRawResponse(self._filedrop.gnssobservations)

    @cached_property
    def gnssrawif(self) -> GnssrawifResourceWithRawResponse:
        return GnssrawifResourceWithRawResponse(self._filedrop.gnssrawif)

    @cached_property
    def mti(self) -> MtiResourceWithRawResponse:
        return MtiResourceWithRawResponse(self._filedrop.mti)

    @cached_property
    def observation(self) -> ObservationResourceWithRawResponse:
        return ObservationResourceWithRawResponse(self._filedrop.observation)

    @cached_property
    def orbit_determination(self) -> OrbitDeterminationResourceWithRawResponse:
        return OrbitDeterminationResourceWithRawResponse(self._filedrop.orbit_determination)

    @cached_property
    def orbit_track(self) -> OrbitTrackResourceWithRawResponse:
        return OrbitTrackResourceWithRawResponse(self._filedrop.orbit_track)

    @cached_property
    def mission_ops(self) -> MissionOpsResourceWithRawResponse:
        return MissionOpsResourceWithRawResponse(self._filedrop.mission_ops)

    @cached_property
    def report_and_activity(self) -> ReportAndActivityResourceWithRawResponse:
        return ReportAndActivityResourceWithRawResponse(self._filedrop.report_and_activity)

    @cached_property
    def surfaceobstructions(self) -> SurfaceobstructionsResourceWithRawResponse:
        return SurfaceobstructionsResourceWithRawResponse(self._filedrop.surfaceobstructions)

    @cached_property
    def state_vectors(self) -> StateVectorsResourceWithRawResponse:
        return StateVectorsResourceWithRawResponse(self._filedrop.state_vectors)

    @cached_property
    def trackroutes(self) -> TrackroutesResourceWithRawResponse:
        return TrackroutesResourceWithRawResponse(self._filedrop.trackroutes)

    @cached_property
    def tracks(self) -> TracksResourceWithRawResponse:
        return TracksResourceWithRawResponse(self._filedrop.tracks)

    @cached_property
    def weather_data(self) -> WeatherDataResourceWithRawResponse:
        return WeatherDataResourceWithRawResponse(self._filedrop.weather_data)

    @cached_property
    def weather_reports(self) -> WeatherReportsResourceWithRawResponse:
        return WeatherReportsResourceWithRawResponse(self._filedrop.weather_reports)


class AsyncFiledropResourceWithRawResponse:
    def __init__(self, filedrop: AsyncFiledropResource) -> None:
        self._filedrop = filedrop

    @cached_property
    def effectrequests(self) -> AsyncEffectrequestsResourceWithRawResponse:
        return AsyncEffectrequestsResourceWithRawResponse(self._filedrop.effectrequests)

    @cached_property
    def effectresponses(self) -> AsyncEffectresponsesResourceWithRawResponse:
        return AsyncEffectresponsesResourceWithRawResponse(self._filedrop.effectresponses)

    @cached_property
    def elsets(self) -> AsyncElsetsResourceWithRawResponse:
        return AsyncElsetsResourceWithRawResponse(self._filedrop.elsets)

    @cached_property
    def eo(self) -> AsyncEoResourceWithRawResponse:
        return AsyncEoResourceWithRawResponse(self._filedrop.eo)

    @cached_property
    def ephemeris(self) -> AsyncEphemerisResourceWithRawResponse:
        return AsyncEphemerisResourceWithRawResponse(self._filedrop.ephemeris)

    @cached_property
    def evac(self) -> AsyncEvacResourceWithRawResponse:
        return AsyncEvacResourceWithRawResponse(self._filedrop.evac)

    @cached_property
    def eventevolutions(self) -> AsyncEventevolutionsResourceWithRawResponse:
        return AsyncEventevolutionsResourceWithRawResponse(self._filedrop.eventevolutions)

    @cached_property
    def flightplans(self) -> AsyncFlightplansResourceWithRawResponse:
        return AsyncFlightplansResourceWithRawResponse(self._filedrop.flightplans)

    @cached_property
    def gnssobservations(self) -> AsyncGnssobservationsResourceWithRawResponse:
        return AsyncGnssobservationsResourceWithRawResponse(self._filedrop.gnssobservations)

    @cached_property
    def gnssrawif(self) -> AsyncGnssrawifResourceWithRawResponse:
        return AsyncGnssrawifResourceWithRawResponse(self._filedrop.gnssrawif)

    @cached_property
    def mti(self) -> AsyncMtiResourceWithRawResponse:
        return AsyncMtiResourceWithRawResponse(self._filedrop.mti)

    @cached_property
    def observation(self) -> AsyncObservationResourceWithRawResponse:
        return AsyncObservationResourceWithRawResponse(self._filedrop.observation)

    @cached_property
    def orbit_determination(self) -> AsyncOrbitDeterminationResourceWithRawResponse:
        return AsyncOrbitDeterminationResourceWithRawResponse(self._filedrop.orbit_determination)

    @cached_property
    def orbit_track(self) -> AsyncOrbitTrackResourceWithRawResponse:
        return AsyncOrbitTrackResourceWithRawResponse(self._filedrop.orbit_track)

    @cached_property
    def mission_ops(self) -> AsyncMissionOpsResourceWithRawResponse:
        return AsyncMissionOpsResourceWithRawResponse(self._filedrop.mission_ops)

    @cached_property
    def report_and_activity(self) -> AsyncReportAndActivityResourceWithRawResponse:
        return AsyncReportAndActivityResourceWithRawResponse(self._filedrop.report_and_activity)

    @cached_property
    def surfaceobstructions(self) -> AsyncSurfaceobstructionsResourceWithRawResponse:
        return AsyncSurfaceobstructionsResourceWithRawResponse(self._filedrop.surfaceobstructions)

    @cached_property
    def state_vectors(self) -> AsyncStateVectorsResourceWithRawResponse:
        return AsyncStateVectorsResourceWithRawResponse(self._filedrop.state_vectors)

    @cached_property
    def trackroutes(self) -> AsyncTrackroutesResourceWithRawResponse:
        return AsyncTrackroutesResourceWithRawResponse(self._filedrop.trackroutes)

    @cached_property
    def tracks(self) -> AsyncTracksResourceWithRawResponse:
        return AsyncTracksResourceWithRawResponse(self._filedrop.tracks)

    @cached_property
    def weather_data(self) -> AsyncWeatherDataResourceWithRawResponse:
        return AsyncWeatherDataResourceWithRawResponse(self._filedrop.weather_data)

    @cached_property
    def weather_reports(self) -> AsyncWeatherReportsResourceWithRawResponse:
        return AsyncWeatherReportsResourceWithRawResponse(self._filedrop.weather_reports)


class FiledropResourceWithStreamingResponse:
    def __init__(self, filedrop: FiledropResource) -> None:
        self._filedrop = filedrop

    @cached_property
    def effectrequests(self) -> EffectrequestsResourceWithStreamingResponse:
        return EffectrequestsResourceWithStreamingResponse(self._filedrop.effectrequests)

    @cached_property
    def effectresponses(self) -> EffectresponsesResourceWithStreamingResponse:
        return EffectresponsesResourceWithStreamingResponse(self._filedrop.effectresponses)

    @cached_property
    def elsets(self) -> ElsetsResourceWithStreamingResponse:
        return ElsetsResourceWithStreamingResponse(self._filedrop.elsets)

    @cached_property
    def eo(self) -> EoResourceWithStreamingResponse:
        return EoResourceWithStreamingResponse(self._filedrop.eo)

    @cached_property
    def ephemeris(self) -> EphemerisResourceWithStreamingResponse:
        return EphemerisResourceWithStreamingResponse(self._filedrop.ephemeris)

    @cached_property
    def evac(self) -> EvacResourceWithStreamingResponse:
        return EvacResourceWithStreamingResponse(self._filedrop.evac)

    @cached_property
    def eventevolutions(self) -> EventevolutionsResourceWithStreamingResponse:
        return EventevolutionsResourceWithStreamingResponse(self._filedrop.eventevolutions)

    @cached_property
    def flightplans(self) -> FlightplansResourceWithStreamingResponse:
        return FlightplansResourceWithStreamingResponse(self._filedrop.flightplans)

    @cached_property
    def gnssobservations(self) -> GnssobservationsResourceWithStreamingResponse:
        return GnssobservationsResourceWithStreamingResponse(self._filedrop.gnssobservations)

    @cached_property
    def gnssrawif(self) -> GnssrawifResourceWithStreamingResponse:
        return GnssrawifResourceWithStreamingResponse(self._filedrop.gnssrawif)

    @cached_property
    def mti(self) -> MtiResourceWithStreamingResponse:
        return MtiResourceWithStreamingResponse(self._filedrop.mti)

    @cached_property
    def observation(self) -> ObservationResourceWithStreamingResponse:
        return ObservationResourceWithStreamingResponse(self._filedrop.observation)

    @cached_property
    def orbit_determination(self) -> OrbitDeterminationResourceWithStreamingResponse:
        return OrbitDeterminationResourceWithStreamingResponse(self._filedrop.orbit_determination)

    @cached_property
    def orbit_track(self) -> OrbitTrackResourceWithStreamingResponse:
        return OrbitTrackResourceWithStreamingResponse(self._filedrop.orbit_track)

    @cached_property
    def mission_ops(self) -> MissionOpsResourceWithStreamingResponse:
        return MissionOpsResourceWithStreamingResponse(self._filedrop.mission_ops)

    @cached_property
    def report_and_activity(self) -> ReportAndActivityResourceWithStreamingResponse:
        return ReportAndActivityResourceWithStreamingResponse(self._filedrop.report_and_activity)

    @cached_property
    def surfaceobstructions(self) -> SurfaceobstructionsResourceWithStreamingResponse:
        return SurfaceobstructionsResourceWithStreamingResponse(self._filedrop.surfaceobstructions)

    @cached_property
    def state_vectors(self) -> StateVectorsResourceWithStreamingResponse:
        return StateVectorsResourceWithStreamingResponse(self._filedrop.state_vectors)

    @cached_property
    def trackroutes(self) -> TrackroutesResourceWithStreamingResponse:
        return TrackroutesResourceWithStreamingResponse(self._filedrop.trackroutes)

    @cached_property
    def tracks(self) -> TracksResourceWithStreamingResponse:
        return TracksResourceWithStreamingResponse(self._filedrop.tracks)

    @cached_property
    def weather_data(self) -> WeatherDataResourceWithStreamingResponse:
        return WeatherDataResourceWithStreamingResponse(self._filedrop.weather_data)

    @cached_property
    def weather_reports(self) -> WeatherReportsResourceWithStreamingResponse:
        return WeatherReportsResourceWithStreamingResponse(self._filedrop.weather_reports)


class AsyncFiledropResourceWithStreamingResponse:
    def __init__(self, filedrop: AsyncFiledropResource) -> None:
        self._filedrop = filedrop

    @cached_property
    def effectrequests(self) -> AsyncEffectrequestsResourceWithStreamingResponse:
        return AsyncEffectrequestsResourceWithStreamingResponse(self._filedrop.effectrequests)

    @cached_property
    def effectresponses(self) -> AsyncEffectresponsesResourceWithStreamingResponse:
        return AsyncEffectresponsesResourceWithStreamingResponse(self._filedrop.effectresponses)

    @cached_property
    def elsets(self) -> AsyncElsetsResourceWithStreamingResponse:
        return AsyncElsetsResourceWithStreamingResponse(self._filedrop.elsets)

    @cached_property
    def eo(self) -> AsyncEoResourceWithStreamingResponse:
        return AsyncEoResourceWithStreamingResponse(self._filedrop.eo)

    @cached_property
    def ephemeris(self) -> AsyncEphemerisResourceWithStreamingResponse:
        return AsyncEphemerisResourceWithStreamingResponse(self._filedrop.ephemeris)

    @cached_property
    def evac(self) -> AsyncEvacResourceWithStreamingResponse:
        return AsyncEvacResourceWithStreamingResponse(self._filedrop.evac)

    @cached_property
    def eventevolutions(self) -> AsyncEventevolutionsResourceWithStreamingResponse:
        return AsyncEventevolutionsResourceWithStreamingResponse(self._filedrop.eventevolutions)

    @cached_property
    def flightplans(self) -> AsyncFlightplansResourceWithStreamingResponse:
        return AsyncFlightplansResourceWithStreamingResponse(self._filedrop.flightplans)

    @cached_property
    def gnssobservations(self) -> AsyncGnssobservationsResourceWithStreamingResponse:
        return AsyncGnssobservationsResourceWithStreamingResponse(self._filedrop.gnssobservations)

    @cached_property
    def gnssrawif(self) -> AsyncGnssrawifResourceWithStreamingResponse:
        return AsyncGnssrawifResourceWithStreamingResponse(self._filedrop.gnssrawif)

    @cached_property
    def mti(self) -> AsyncMtiResourceWithStreamingResponse:
        return AsyncMtiResourceWithStreamingResponse(self._filedrop.mti)

    @cached_property
    def observation(self) -> AsyncObservationResourceWithStreamingResponse:
        return AsyncObservationResourceWithStreamingResponse(self._filedrop.observation)

    @cached_property
    def orbit_determination(self) -> AsyncOrbitDeterminationResourceWithStreamingResponse:
        return AsyncOrbitDeterminationResourceWithStreamingResponse(self._filedrop.orbit_determination)

    @cached_property
    def orbit_track(self) -> AsyncOrbitTrackResourceWithStreamingResponse:
        return AsyncOrbitTrackResourceWithStreamingResponse(self._filedrop.orbit_track)

    @cached_property
    def mission_ops(self) -> AsyncMissionOpsResourceWithStreamingResponse:
        return AsyncMissionOpsResourceWithStreamingResponse(self._filedrop.mission_ops)

    @cached_property
    def report_and_activity(self) -> AsyncReportAndActivityResourceWithStreamingResponse:
        return AsyncReportAndActivityResourceWithStreamingResponse(self._filedrop.report_and_activity)

    @cached_property
    def surfaceobstructions(self) -> AsyncSurfaceobstructionsResourceWithStreamingResponse:
        return AsyncSurfaceobstructionsResourceWithStreamingResponse(self._filedrop.surfaceobstructions)

    @cached_property
    def state_vectors(self) -> AsyncStateVectorsResourceWithStreamingResponse:
        return AsyncStateVectorsResourceWithStreamingResponse(self._filedrop.state_vectors)

    @cached_property
    def trackroutes(self) -> AsyncTrackroutesResourceWithStreamingResponse:
        return AsyncTrackroutesResourceWithStreamingResponse(self._filedrop.trackroutes)

    @cached_property
    def tracks(self) -> AsyncTracksResourceWithStreamingResponse:
        return AsyncTracksResourceWithStreamingResponse(self._filedrop.tracks)

    @cached_property
    def weather_data(self) -> AsyncWeatherDataResourceWithStreamingResponse:
        return AsyncWeatherDataResourceWithStreamingResponse(self._filedrop.weather_data)

    @cached_property
    def weather_reports(self) -> AsyncWeatherReportsResourceWithStreamingResponse:
        return AsyncWeatherReportsResourceWithStreamingResponse(self._filedrop.weather_reports)
