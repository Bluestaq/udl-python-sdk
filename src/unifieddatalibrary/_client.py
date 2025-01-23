# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    beam,
    comm,
    cots,
    crew,
    buses,
    h3geo,
    items,
    ecpsdr,
    engines,
    udl_sar,
    udl_sgi,
    aircraft,
    antennas,
    channels,
    entities,
    airfields,
    batteries,
    countries,
    equipment,
    maneuvers,
    air_events,
    udl_sigact,
    ais_objects,
    ephemerides,
    airloadplans,
    attitudesets,
    airfieldslots,
    attitude_data,
    beam_contours,
    drift_history,
    enginedetails,
    launch_events,
    udl_sortieppr,
    air_load_plans,
    airfield_slots,
    batterydetails,
    engine_details,
    eoobservations,
    ground_imagery,
    item_trackings,
    missile_tracks,
    udl_sensorplan,
    udl_skyimagery,
    airfield_status,
    event_evolution,
    isr_collections,
    udl_sigact_text,
    udl_spaceenvobs,
    udl_starcatalog,
    aircraft_sorties,
    airtaskingorders,
    analytic_imagery,
    equipmentremarks,
    iono_observations,
    air_tasking_orders,
    logistics_supports,
    udl_soiobservationset,
    aircraft_status_remarks,
    airspace_control_orders,
    airfieldslotconsumptions,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, UnifieddatalibraryError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.ais import ais
from .resources.eop import eop
from .resources.evac import evac
from .resources.elsets import elsets
from .resources.onorbit import onorbit
from .resources.filedrop import filedrop
from .resources.ephemeris import ephemeris
from .resources.tdoa_fdoa import tdoa_fdoa
from .resources.flightplans import flightplans
from .resources.link_status import link_status
from .resources.mission_ops import mission_ops
from .resources.conjunctions import conjunctions
from .resources.observations import observations
from .resources.attitude_sets import attitude_sets
from .resources.diffofarrival import diffofarrival
from .resources.air_operations import air_operations
from .resources.airfieldstatus import airfieldstatus
from .resources.ephemeris_sets import ephemeris_sets
from .resources.effect_requests import effect_requests
from .resources.eo_observations import eo_observations
from .resources.eventevolutions import eventevolutions
from .resources.supporting_data import supporting_data
from .resources.collect_requests import collect_requests
from .resources.effect_responses import effect_responses
from .resources.aircraft_statuses import aircraft_statuses
from .resources.collect_responses import collect_responses
from .resources.diplomatic_clearance import diplomatic_clearance
from .resources.air_transport_missions import air_transport_missions

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Unifieddatalibrary",
    "AsyncUnifieddatalibrary",
    "Client",
    "AsyncClient",
]


class Unifieddatalibrary(SyncAPIClient):
    conjunctions: conjunctions.ConjunctionsResource
    air_operations: air_operations.AirOperationsResource
    ephemerides: ephemerides.EphemeridesResource
    observations: observations.ObservationsResource
    ais_objects: ais_objects.AIsObjectsResource
    analytic_imagery: analytic_imagery.AnalyticImageryResource
    collect_requests: collect_requests.CollectRequestsResource
    collect_responses: collect_responses.CollectResponsesResource
    crew: crew.CrewResource
    diffofarrival: diffofarrival.DiffofarrivalResource
    ecpsdr: ecpsdr.EcpsdrResource
    filedrop: filedrop.FiledropResource
    ground_imagery: ground_imagery.GroundImageryResource
    h3geo: h3geo.H3geoResource
    iono_observations: iono_observations.IonoObservationsResource
    isr_collections: isr_collections.IsrCollectionsResource
    items: items.ItemsResource
    item_trackings: item_trackings.ItemTrackingsResource
    launch_events: launch_events.LaunchEventsResource
    logistics_supports: logistics_supports.LogisticsSupportsResource
    maneuvers: maneuvers.ManeuversResource
    missile_tracks: missile_tracks.MissileTracksResource
    udl_sar: udl_sar.UdlSarResource
    udl_sensorplan: udl_sensorplan.UdlSensorplanResource
    udl_sgi: udl_sgi.UdlSgiResource
    udl_sigact: udl_sigact.UdlSigactResource
    udl_sigact_text: udl_sigact_text.UdlSigactTextResource
    udl_skyimagery: udl_skyimagery.UdlSkyimageryResource
    udl_soiobservationset: udl_soiobservationset.UdlSoiobservationsetResource
    udl_sortieppr: udl_sortieppr.UdlSortiepprResource
    udl_spaceenvobs: udl_spaceenvobs.UdlSpaceenvobsResource
    udl_starcatalog: udl_starcatalog.UdlStarcatalogResource
    aircraft: aircraft.AircraftResource
    aircraft_sorties: aircraft_sorties.AircraftSortiesResource
    aircraft_statuses: aircraft_statuses.AircraftStatusesResource
    aircraft_status_remarks: aircraft_status_remarks.AircraftStatusRemarksResource
    air_events: air_events.AirEventsResource
    airfields: airfields.AirfieldsResource
    airfield_slots: airfield_slots.AirfieldSlotsResource
    airfieldslots: airfieldslots.AirfieldslotsResource
    airfieldslotconsumptions: airfieldslotconsumptions.AirfieldslotconsumptionsResource
    airfieldstatus: airfieldstatus.AirfieldstatusResource
    airfield_status: airfield_status.AirfieldStatusResource
    air_load_plans: air_load_plans.AirLoadPlansResource
    airloadplans: airloadplans.AirloadplansResource
    airspace_control_orders: airspace_control_orders.AirspaceControlOrdersResource
    airtaskingorders: airtaskingorders.AirtaskingordersResource
    air_tasking_orders: air_tasking_orders.AirTaskingOrdersResource
    air_transport_missions: air_transport_missions.AirTransportMissionsResource
    ais: ais.AIsResource
    antennas: antennas.AntennasResource
    onorbit: onorbit.OnorbitResource
    ephemeris: ephemeris.EphemerisResource
    attitude_data: attitude_data.AttitudeDataResource
    attitude_sets: attitude_sets.AttitudeSetsResource
    attitudesets: attitudesets.AttitudesetsResource
    batteries: batteries.BatteriesResource
    batterydetails: batterydetails.BatterydetailsResource
    beam: beam.BeamResource
    beam_contours: beam_contours.BeamContoursResource
    buses: buses.BusesResource
    channels: channels.ChannelsResource
    comm: comm.CommResource
    cots: cots.CotsResource
    countries: countries.CountriesResource
    link_status: link_status.LinkStatusResource
    supporting_data: supporting_data.SupportingDataResource
    tdoa_fdoa: tdoa_fdoa.TdoaFdoaResource
    diplomatic_clearance: diplomatic_clearance.DiplomaticClearanceResource
    drift_history: drift_history.DriftHistoryResource
    mission_ops: mission_ops.MissionOpsResource
    effect_requests: effect_requests.EffectRequestsResource
    effect_responses: effect_responses.EffectResponsesResource
    elsets: elsets.ElsetsResource
    engines: engines.EnginesResource
    enginedetails: enginedetails.EnginedetailsResource
    engine_details: engine_details.EngineDetailsResource
    entities: entities.EntitiesResource
    eo_observations: eo_observations.EoObservationsResource
    eoobservations: eoobservations.EoobservationsResource
    eop: eop.EopResource
    ephemeris_sets: ephemeris_sets.EphemerisSetsResource
    equipment: equipment.EquipmentResource
    equipmentremarks: equipmentremarks.EquipmentremarksResource
    evac: evac.EvacResource
    event_evolution: event_evolution.EventEvolutionResource
    eventevolutions: eventevolutions.EventevolutionsResource
    flightplans: flightplans.FlightplansResource
    with_raw_response: UnifieddatalibraryWithRawResponse
    with_streaming_response: UnifieddatalibraryWithStreamedResponse

    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous unifieddatalibrary client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `HTTP_BASIC_AUTH_USERNAME`
        - `password` from `HTTP_BASIC_AUTH_PASSWORD`
        """
        if username is None:
            username = os.environ.get("HTTP_BASIC_AUTH_USERNAME")
        if username is None:
            raise UnifieddatalibraryError(
                "The username client option must be set either by passing username to the client or by setting the HTTP_BASIC_AUTH_USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("HTTP_BASIC_AUTH_PASSWORD")
        if password is None:
            raise UnifieddatalibraryError(
                "The password client option must be set either by passing password to the client or by setting the HTTP_BASIC_AUTH_PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("UNIFIEDDATALIBRARY_BASE_URL")
        if base_url is None:
            base_url = f"https://unifieddatalibrary.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.conjunctions = conjunctions.ConjunctionsResource(self)
        self.air_operations = air_operations.AirOperationsResource(self)
        self.ephemerides = ephemerides.EphemeridesResource(self)
        self.observations = observations.ObservationsResource(self)
        self.ais_objects = ais_objects.AIsObjectsResource(self)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResource(self)
        self.collect_requests = collect_requests.CollectRequestsResource(self)
        self.collect_responses = collect_responses.CollectResponsesResource(self)
        self.crew = crew.CrewResource(self)
        self.diffofarrival = diffofarrival.DiffofarrivalResource(self)
        self.ecpsdr = ecpsdr.EcpsdrResource(self)
        self.filedrop = filedrop.FiledropResource(self)
        self.ground_imagery = ground_imagery.GroundImageryResource(self)
        self.h3geo = h3geo.H3geoResource(self)
        self.iono_observations = iono_observations.IonoObservationsResource(self)
        self.isr_collections = isr_collections.IsrCollectionsResource(self)
        self.items = items.ItemsResource(self)
        self.item_trackings = item_trackings.ItemTrackingsResource(self)
        self.launch_events = launch_events.LaunchEventsResource(self)
        self.logistics_supports = logistics_supports.LogisticsSupportsResource(self)
        self.maneuvers = maneuvers.ManeuversResource(self)
        self.missile_tracks = missile_tracks.MissileTracksResource(self)
        self.udl_sar = udl_sar.UdlSarResource(self)
        self.udl_sensorplan = udl_sensorplan.UdlSensorplanResource(self)
        self.udl_sgi = udl_sgi.UdlSgiResource(self)
        self.udl_sigact = udl_sigact.UdlSigactResource(self)
        self.udl_sigact_text = udl_sigact_text.UdlSigactTextResource(self)
        self.udl_skyimagery = udl_skyimagery.UdlSkyimageryResource(self)
        self.udl_soiobservationset = udl_soiobservationset.UdlSoiobservationsetResource(self)
        self.udl_sortieppr = udl_sortieppr.UdlSortiepprResource(self)
        self.udl_spaceenvobs = udl_spaceenvobs.UdlSpaceenvobsResource(self)
        self.udl_starcatalog = udl_starcatalog.UdlStarcatalogResource(self)
        self.aircraft = aircraft.AircraftResource(self)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResource(self)
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResource(self)
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResource(self)
        self.air_events = air_events.AirEventsResource(self)
        self.airfields = airfields.AirfieldsResource(self)
        self.airfield_slots = airfield_slots.AirfieldSlotsResource(self)
        self.airfieldslots = airfieldslots.AirfieldslotsResource(self)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AirfieldslotconsumptionsResource(self)
        self.airfieldstatus = airfieldstatus.AirfieldstatusResource(self)
        self.airfield_status = airfield_status.AirfieldStatusResource(self)
        self.air_load_plans = air_load_plans.AirLoadPlansResource(self)
        self.airloadplans = airloadplans.AirloadplansResource(self)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResource(self)
        self.airtaskingorders = airtaskingorders.AirtaskingordersResource(self)
        self.air_tasking_orders = air_tasking_orders.AirTaskingOrdersResource(self)
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResource(self)
        self.ais = ais.AIsResource(self)
        self.antennas = antennas.AntennasResource(self)
        self.onorbit = onorbit.OnorbitResource(self)
        self.ephemeris = ephemeris.EphemerisResource(self)
        self.attitude_data = attitude_data.AttitudeDataResource(self)
        self.attitude_sets = attitude_sets.AttitudeSetsResource(self)
        self.attitudesets = attitudesets.AttitudesetsResource(self)
        self.batteries = batteries.BatteriesResource(self)
        self.batterydetails = batterydetails.BatterydetailsResource(self)
        self.beam = beam.BeamResource(self)
        self.beam_contours = beam_contours.BeamContoursResource(self)
        self.buses = buses.BusesResource(self)
        self.channels = channels.ChannelsResource(self)
        self.comm = comm.CommResource(self)
        self.cots = cots.CotsResource(self)
        self.countries = countries.CountriesResource(self)
        self.link_status = link_status.LinkStatusResource(self)
        self.supporting_data = supporting_data.SupportingDataResource(self)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResource(self)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResource(self)
        self.drift_history = drift_history.DriftHistoryResource(self)
        self.mission_ops = mission_ops.MissionOpsResource(self)
        self.effect_requests = effect_requests.EffectRequestsResource(self)
        self.effect_responses = effect_responses.EffectResponsesResource(self)
        self.elsets = elsets.ElsetsResource(self)
        self.engines = engines.EnginesResource(self)
        self.enginedetails = enginedetails.EnginedetailsResource(self)
        self.engine_details = engine_details.EngineDetailsResource(self)
        self.entities = entities.EntitiesResource(self)
        self.eo_observations = eo_observations.EoObservationsResource(self)
        self.eoobservations = eoobservations.EoobservationsResource(self)
        self.eop = eop.EopResource(self)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResource(self)
        self.equipment = equipment.EquipmentResource(self)
        self.equipmentremarks = equipmentremarks.EquipmentremarksResource(self)
        self.evac = evac.EvacResource(self)
        self.event_evolution = event_evolution.EventEvolutionResource(self)
        self.eventevolutions = eventevolutions.EventevolutionsResource(self)
        self.flightplans = flightplans.FlightplansResource(self)
        self.with_raw_response = UnifieddatalibraryWithRawResponse(self)
        self.with_streaming_response = UnifieddatalibraryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncUnifieddatalibrary(AsyncAPIClient):
    conjunctions: conjunctions.AsyncConjunctionsResource
    air_operations: air_operations.AsyncAirOperationsResource
    ephemerides: ephemerides.AsyncEphemeridesResource
    observations: observations.AsyncObservationsResource
    ais_objects: ais_objects.AsyncAIsObjectsResource
    analytic_imagery: analytic_imagery.AsyncAnalyticImageryResource
    collect_requests: collect_requests.AsyncCollectRequestsResource
    collect_responses: collect_responses.AsyncCollectResponsesResource
    crew: crew.AsyncCrewResource
    diffofarrival: diffofarrival.AsyncDiffofarrivalResource
    ecpsdr: ecpsdr.AsyncEcpsdrResource
    filedrop: filedrop.AsyncFiledropResource
    ground_imagery: ground_imagery.AsyncGroundImageryResource
    h3geo: h3geo.AsyncH3geoResource
    iono_observations: iono_observations.AsyncIonoObservationsResource
    isr_collections: isr_collections.AsyncIsrCollectionsResource
    items: items.AsyncItemsResource
    item_trackings: item_trackings.AsyncItemTrackingsResource
    launch_events: launch_events.AsyncLaunchEventsResource
    logistics_supports: logistics_supports.AsyncLogisticsSupportsResource
    maneuvers: maneuvers.AsyncManeuversResource
    missile_tracks: missile_tracks.AsyncMissileTracksResource
    udl_sar: udl_sar.AsyncUdlSarResource
    udl_sensorplan: udl_sensorplan.AsyncUdlSensorplanResource
    udl_sgi: udl_sgi.AsyncUdlSgiResource
    udl_sigact: udl_sigact.AsyncUdlSigactResource
    udl_sigact_text: udl_sigact_text.AsyncUdlSigactTextResource
    udl_skyimagery: udl_skyimagery.AsyncUdlSkyimageryResource
    udl_soiobservationset: udl_soiobservationset.AsyncUdlSoiobservationsetResource
    udl_sortieppr: udl_sortieppr.AsyncUdlSortiepprResource
    udl_spaceenvobs: udl_spaceenvobs.AsyncUdlSpaceenvobsResource
    udl_starcatalog: udl_starcatalog.AsyncUdlStarcatalogResource
    aircraft: aircraft.AsyncAircraftResource
    aircraft_sorties: aircraft_sorties.AsyncAircraftSortiesResource
    aircraft_statuses: aircraft_statuses.AsyncAircraftStatusesResource
    aircraft_status_remarks: aircraft_status_remarks.AsyncAircraftStatusRemarksResource
    air_events: air_events.AsyncAirEventsResource
    airfields: airfields.AsyncAirfieldsResource
    airfield_slots: airfield_slots.AsyncAirfieldSlotsResource
    airfieldslots: airfieldslots.AsyncAirfieldslotsResource
    airfieldslotconsumptions: airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResource
    airfieldstatus: airfieldstatus.AsyncAirfieldstatusResource
    airfield_status: airfield_status.AsyncAirfieldStatusResource
    air_load_plans: air_load_plans.AsyncAirLoadPlansResource
    airloadplans: airloadplans.AsyncAirloadplansResource
    airspace_control_orders: airspace_control_orders.AsyncAirspaceControlOrdersResource
    airtaskingorders: airtaskingorders.AsyncAirtaskingordersResource
    air_tasking_orders: air_tasking_orders.AsyncAirTaskingOrdersResource
    air_transport_missions: air_transport_missions.AsyncAirTransportMissionsResource
    ais: ais.AsyncAIsResource
    antennas: antennas.AsyncAntennasResource
    onorbit: onorbit.AsyncOnorbitResource
    ephemeris: ephemeris.AsyncEphemerisResource
    attitude_data: attitude_data.AsyncAttitudeDataResource
    attitude_sets: attitude_sets.AsyncAttitudeSetsResource
    attitudesets: attitudesets.AsyncAttitudesetsResource
    batteries: batteries.AsyncBatteriesResource
    batterydetails: batterydetails.AsyncBatterydetailsResource
    beam: beam.AsyncBeamResource
    beam_contours: beam_contours.AsyncBeamContoursResource
    buses: buses.AsyncBusesResource
    channels: channels.AsyncChannelsResource
    comm: comm.AsyncCommResource
    cots: cots.AsyncCotsResource
    countries: countries.AsyncCountriesResource
    link_status: link_status.AsyncLinkStatusResource
    supporting_data: supporting_data.AsyncSupportingDataResource
    tdoa_fdoa: tdoa_fdoa.AsyncTdoaFdoaResource
    diplomatic_clearance: diplomatic_clearance.AsyncDiplomaticClearanceResource
    drift_history: drift_history.AsyncDriftHistoryResource
    mission_ops: mission_ops.AsyncMissionOpsResource
    effect_requests: effect_requests.AsyncEffectRequestsResource
    effect_responses: effect_responses.AsyncEffectResponsesResource
    elsets: elsets.AsyncElsetsResource
    engines: engines.AsyncEnginesResource
    enginedetails: enginedetails.AsyncEnginedetailsResource
    engine_details: engine_details.AsyncEngineDetailsResource
    entities: entities.AsyncEntitiesResource
    eo_observations: eo_observations.AsyncEoObservationsResource
    eoobservations: eoobservations.AsyncEoobservationsResource
    eop: eop.AsyncEopResource
    ephemeris_sets: ephemeris_sets.AsyncEphemerisSetsResource
    equipment: equipment.AsyncEquipmentResource
    equipmentremarks: equipmentremarks.AsyncEquipmentremarksResource
    evac: evac.AsyncEvacResource
    event_evolution: event_evolution.AsyncEventEvolutionResource
    eventevolutions: eventevolutions.AsyncEventevolutionsResource
    flightplans: flightplans.AsyncFlightplansResource
    with_raw_response: AsyncUnifieddatalibraryWithRawResponse
    with_streaming_response: AsyncUnifieddatalibraryWithStreamedResponse

    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async unifieddatalibrary client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `HTTP_BASIC_AUTH_USERNAME`
        - `password` from `HTTP_BASIC_AUTH_PASSWORD`
        """
        if username is None:
            username = os.environ.get("HTTP_BASIC_AUTH_USERNAME")
        if username is None:
            raise UnifieddatalibraryError(
                "The username client option must be set either by passing username to the client or by setting the HTTP_BASIC_AUTH_USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("HTTP_BASIC_AUTH_PASSWORD")
        if password is None:
            raise UnifieddatalibraryError(
                "The password client option must be set either by passing password to the client or by setting the HTTP_BASIC_AUTH_PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("UNIFIEDDATALIBRARY_BASE_URL")
        if base_url is None:
            base_url = f"https://unifieddatalibrary.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.conjunctions = conjunctions.AsyncConjunctionsResource(self)
        self.air_operations = air_operations.AsyncAirOperationsResource(self)
        self.ephemerides = ephemerides.AsyncEphemeridesResource(self)
        self.observations = observations.AsyncObservationsResource(self)
        self.ais_objects = ais_objects.AsyncAIsObjectsResource(self)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResource(self)
        self.collect_requests = collect_requests.AsyncCollectRequestsResource(self)
        self.collect_responses = collect_responses.AsyncCollectResponsesResource(self)
        self.crew = crew.AsyncCrewResource(self)
        self.diffofarrival = diffofarrival.AsyncDiffofarrivalResource(self)
        self.ecpsdr = ecpsdr.AsyncEcpsdrResource(self)
        self.filedrop = filedrop.AsyncFiledropResource(self)
        self.ground_imagery = ground_imagery.AsyncGroundImageryResource(self)
        self.h3geo = h3geo.AsyncH3geoResource(self)
        self.iono_observations = iono_observations.AsyncIonoObservationsResource(self)
        self.isr_collections = isr_collections.AsyncIsrCollectionsResource(self)
        self.items = items.AsyncItemsResource(self)
        self.item_trackings = item_trackings.AsyncItemTrackingsResource(self)
        self.launch_events = launch_events.AsyncLaunchEventsResource(self)
        self.logistics_supports = logistics_supports.AsyncLogisticsSupportsResource(self)
        self.maneuvers = maneuvers.AsyncManeuversResource(self)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResource(self)
        self.udl_sar = udl_sar.AsyncUdlSarResource(self)
        self.udl_sensorplan = udl_sensorplan.AsyncUdlSensorplanResource(self)
        self.udl_sgi = udl_sgi.AsyncUdlSgiResource(self)
        self.udl_sigact = udl_sigact.AsyncUdlSigactResource(self)
        self.udl_sigact_text = udl_sigact_text.AsyncUdlSigactTextResource(self)
        self.udl_skyimagery = udl_skyimagery.AsyncUdlSkyimageryResource(self)
        self.udl_soiobservationset = udl_soiobservationset.AsyncUdlSoiobservationsetResource(self)
        self.udl_sortieppr = udl_sortieppr.AsyncUdlSortiepprResource(self)
        self.udl_spaceenvobs = udl_spaceenvobs.AsyncUdlSpaceenvobsResource(self)
        self.udl_starcatalog = udl_starcatalog.AsyncUdlStarcatalogResource(self)
        self.aircraft = aircraft.AsyncAircraftResource(self)
        self.aircraft_sorties = aircraft_sorties.AsyncAircraftSortiesResource(self)
        self.aircraft_statuses = aircraft_statuses.AsyncAircraftStatusesResource(self)
        self.aircraft_status_remarks = aircraft_status_remarks.AsyncAircraftStatusRemarksResource(self)
        self.air_events = air_events.AsyncAirEventsResource(self)
        self.airfields = airfields.AsyncAirfieldsResource(self)
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResource(self)
        self.airfieldslots = airfieldslots.AsyncAirfieldslotsResource(self)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResource(self)
        self.airfieldstatus = airfieldstatus.AsyncAirfieldstatusResource(self)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResource(self)
        self.air_load_plans = air_load_plans.AsyncAirLoadPlansResource(self)
        self.airloadplans = airloadplans.AsyncAirloadplansResource(self)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResource(self)
        self.airtaskingorders = airtaskingorders.AsyncAirtaskingordersResource(self)
        self.air_tasking_orders = air_tasking_orders.AsyncAirTaskingOrdersResource(self)
        self.air_transport_missions = air_transport_missions.AsyncAirTransportMissionsResource(self)
        self.ais = ais.AsyncAIsResource(self)
        self.antennas = antennas.AsyncAntennasResource(self)
        self.onorbit = onorbit.AsyncOnorbitResource(self)
        self.ephemeris = ephemeris.AsyncEphemerisResource(self)
        self.attitude_data = attitude_data.AsyncAttitudeDataResource(self)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResource(self)
        self.attitudesets = attitudesets.AsyncAttitudesetsResource(self)
        self.batteries = batteries.AsyncBatteriesResource(self)
        self.batterydetails = batterydetails.AsyncBatterydetailsResource(self)
        self.beam = beam.AsyncBeamResource(self)
        self.beam_contours = beam_contours.AsyncBeamContoursResource(self)
        self.buses = buses.AsyncBusesResource(self)
        self.channels = channels.AsyncChannelsResource(self)
        self.comm = comm.AsyncCommResource(self)
        self.cots = cots.AsyncCotsResource(self)
        self.countries = countries.AsyncCountriesResource(self)
        self.link_status = link_status.AsyncLinkStatusResource(self)
        self.supporting_data = supporting_data.AsyncSupportingDataResource(self)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResource(self)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResource(self)
        self.drift_history = drift_history.AsyncDriftHistoryResource(self)
        self.mission_ops = mission_ops.AsyncMissionOpsResource(self)
        self.effect_requests = effect_requests.AsyncEffectRequestsResource(self)
        self.effect_responses = effect_responses.AsyncEffectResponsesResource(self)
        self.elsets = elsets.AsyncElsetsResource(self)
        self.engines = engines.AsyncEnginesResource(self)
        self.enginedetails = enginedetails.AsyncEnginedetailsResource(self)
        self.engine_details = engine_details.AsyncEngineDetailsResource(self)
        self.entities = entities.AsyncEntitiesResource(self)
        self.eo_observations = eo_observations.AsyncEoObservationsResource(self)
        self.eoobservations = eoobservations.AsyncEoobservationsResource(self)
        self.eop = eop.AsyncEopResource(self)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResource(self)
        self.equipment = equipment.AsyncEquipmentResource(self)
        self.equipmentremarks = equipmentremarks.AsyncEquipmentremarksResource(self)
        self.evac = evac.AsyncEvacResource(self)
        self.event_evolution = event_evolution.AsyncEventEvolutionResource(self)
        self.eventevolutions = eventevolutions.AsyncEventevolutionsResource(self)
        self.flightplans = flightplans.AsyncFlightplansResource(self)
        self.with_raw_response = AsyncUnifieddatalibraryWithRawResponse(self)
        self.with_streaming_response = AsyncUnifieddatalibraryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class UnifieddatalibraryWithRawResponse:
    def __init__(self, client: Unifieddatalibrary) -> None:
        self.conjunctions = conjunctions.ConjunctionsResourceWithRawResponse(client.conjunctions)
        self.air_operations = air_operations.AirOperationsResourceWithRawResponse(client.air_operations)
        self.ephemerides = ephemerides.EphemeridesResourceWithRawResponse(client.ephemerides)
        self.observations = observations.ObservationsResourceWithRawResponse(client.observations)
        self.ais_objects = ais_objects.AIsObjectsResourceWithRawResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResourceWithRawResponse(client.analytic_imagery)
        self.collect_requests = collect_requests.CollectRequestsResourceWithRawResponse(client.collect_requests)
        self.collect_responses = collect_responses.CollectResponsesResourceWithRawResponse(client.collect_responses)
        self.crew = crew.CrewResourceWithRawResponse(client.crew)
        self.diffofarrival = diffofarrival.DiffofarrivalResourceWithRawResponse(client.diffofarrival)
        self.ecpsdr = ecpsdr.EcpsdrResourceWithRawResponse(client.ecpsdr)
        self.filedrop = filedrop.FiledropResourceWithRawResponse(client.filedrop)
        self.ground_imagery = ground_imagery.GroundImageryResourceWithRawResponse(client.ground_imagery)
        self.h3geo = h3geo.H3geoResourceWithRawResponse(client.h3geo)
        self.iono_observations = iono_observations.IonoObservationsResourceWithRawResponse(client.iono_observations)
        self.isr_collections = isr_collections.IsrCollectionsResourceWithRawResponse(client.isr_collections)
        self.items = items.ItemsResourceWithRawResponse(client.items)
        self.item_trackings = item_trackings.ItemTrackingsResourceWithRawResponse(client.item_trackings)
        self.launch_events = launch_events.LaunchEventsResourceWithRawResponse(client.launch_events)
        self.logistics_supports = logistics_supports.LogisticsSupportsResourceWithRawResponse(client.logistics_supports)
        self.maneuvers = maneuvers.ManeuversResourceWithRawResponse(client.maneuvers)
        self.missile_tracks = missile_tracks.MissileTracksResourceWithRawResponse(client.missile_tracks)
        self.udl_sar = udl_sar.UdlSarResourceWithRawResponse(client.udl_sar)
        self.udl_sensorplan = udl_sensorplan.UdlSensorplanResourceWithRawResponse(client.udl_sensorplan)
        self.udl_sgi = udl_sgi.UdlSgiResourceWithRawResponse(client.udl_sgi)
        self.udl_sigact = udl_sigact.UdlSigactResourceWithRawResponse(client.udl_sigact)
        self.udl_sigact_text = udl_sigact_text.UdlSigactTextResourceWithRawResponse(client.udl_sigact_text)
        self.udl_skyimagery = udl_skyimagery.UdlSkyimageryResourceWithRawResponse(client.udl_skyimagery)
        self.udl_soiobservationset = udl_soiobservationset.UdlSoiobservationsetResourceWithRawResponse(
            client.udl_soiobservationset
        )
        self.udl_sortieppr = udl_sortieppr.UdlSortiepprResourceWithRawResponse(client.udl_sortieppr)
        self.udl_spaceenvobs = udl_spaceenvobs.UdlSpaceenvobsResourceWithRawResponse(client.udl_spaceenvobs)
        self.udl_starcatalog = udl_starcatalog.UdlStarcatalogResourceWithRawResponse(client.udl_starcatalog)
        self.aircraft = aircraft.AircraftResourceWithRawResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResourceWithRawResponse(client.aircraft_sorties)
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResourceWithRawResponse(client.aircraft_statuses)
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResourceWithRawResponse(
            client.aircraft_status_remarks
        )
        self.air_events = air_events.AirEventsResourceWithRawResponse(client.air_events)
        self.airfields = airfields.AirfieldsResourceWithRawResponse(client.airfields)
        self.airfield_slots = airfield_slots.AirfieldSlotsResourceWithRawResponse(client.airfield_slots)
        self.airfieldslots = airfieldslots.AirfieldslotsResourceWithRawResponse(client.airfieldslots)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AirfieldslotconsumptionsResourceWithRawResponse(
            client.airfieldslotconsumptions
        )
        self.airfieldstatus = airfieldstatus.AirfieldstatusResourceWithRawResponse(client.airfieldstatus)
        self.airfield_status = airfield_status.AirfieldStatusResourceWithRawResponse(client.airfield_status)
        self.air_load_plans = air_load_plans.AirLoadPlansResourceWithRawResponse(client.air_load_plans)
        self.airloadplans = airloadplans.AirloadplansResourceWithRawResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResourceWithRawResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AirtaskingordersResourceWithRawResponse(client.airtaskingorders)
        self.air_tasking_orders = air_tasking_orders.AirTaskingOrdersResourceWithRawResponse(client.air_tasking_orders)
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResourceWithRawResponse(
            client.air_transport_missions
        )
        self.ais = ais.AIsResourceWithRawResponse(client.ais)
        self.antennas = antennas.AntennasResourceWithRawResponse(client.antennas)
        self.onorbit = onorbit.OnorbitResourceWithRawResponse(client.onorbit)
        self.ephemeris = ephemeris.EphemerisResourceWithRawResponse(client.ephemeris)
        self.attitude_data = attitude_data.AttitudeDataResourceWithRawResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AttitudeSetsResourceWithRawResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AttitudesetsResourceWithRawResponse(client.attitudesets)
        self.batteries = batteries.BatteriesResourceWithRawResponse(client.batteries)
        self.batterydetails = batterydetails.BatterydetailsResourceWithRawResponse(client.batterydetails)
        self.beam = beam.BeamResourceWithRawResponse(client.beam)
        self.beam_contours = beam_contours.BeamContoursResourceWithRawResponse(client.beam_contours)
        self.buses = buses.BusesResourceWithRawResponse(client.buses)
        self.channels = channels.ChannelsResourceWithRawResponse(client.channels)
        self.comm = comm.CommResourceWithRawResponse(client.comm)
        self.cots = cots.CotsResourceWithRawResponse(client.cots)
        self.countries = countries.CountriesResourceWithRawResponse(client.countries)
        self.link_status = link_status.LinkStatusResourceWithRawResponse(client.link_status)
        self.supporting_data = supporting_data.SupportingDataResourceWithRawResponse(client.supporting_data)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResourceWithRawResponse(client.tdoa_fdoa)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResourceWithRawResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.DriftHistoryResourceWithRawResponse(client.drift_history)
        self.mission_ops = mission_ops.MissionOpsResourceWithRawResponse(client.mission_ops)
        self.effect_requests = effect_requests.EffectRequestsResourceWithRawResponse(client.effect_requests)
        self.effect_responses = effect_responses.EffectResponsesResourceWithRawResponse(client.effect_responses)
        self.elsets = elsets.ElsetsResourceWithRawResponse(client.elsets)
        self.engines = engines.EnginesResourceWithRawResponse(client.engines)
        self.enginedetails = enginedetails.EnginedetailsResourceWithRawResponse(client.enginedetails)
        self.engine_details = engine_details.EngineDetailsResourceWithRawResponse(client.engine_details)
        self.entities = entities.EntitiesResourceWithRawResponse(client.entities)
        self.eo_observations = eo_observations.EoObservationsResourceWithRawResponse(client.eo_observations)
        self.eoobservations = eoobservations.EoobservationsResourceWithRawResponse(client.eoobservations)
        self.eop = eop.EopResourceWithRawResponse(client.eop)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResourceWithRawResponse(client.ephemeris_sets)
        self.equipment = equipment.EquipmentResourceWithRawResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.EquipmentremarksResourceWithRawResponse(client.equipmentremarks)
        self.evac = evac.EvacResourceWithRawResponse(client.evac)
        self.event_evolution = event_evolution.EventEvolutionResourceWithRawResponse(client.event_evolution)
        self.eventevolutions = eventevolutions.EventevolutionsResourceWithRawResponse(client.eventevolutions)
        self.flightplans = flightplans.FlightplansResourceWithRawResponse(client.flightplans)


class AsyncUnifieddatalibraryWithRawResponse:
    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self.conjunctions = conjunctions.AsyncConjunctionsResourceWithRawResponse(client.conjunctions)
        self.air_operations = air_operations.AsyncAirOperationsResourceWithRawResponse(client.air_operations)
        self.ephemerides = ephemerides.AsyncEphemeridesResourceWithRawResponse(client.ephemerides)
        self.observations = observations.AsyncObservationsResourceWithRawResponse(client.observations)
        self.ais_objects = ais_objects.AsyncAIsObjectsResourceWithRawResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResourceWithRawResponse(client.analytic_imagery)
        self.collect_requests = collect_requests.AsyncCollectRequestsResourceWithRawResponse(client.collect_requests)
        self.collect_responses = collect_responses.AsyncCollectResponsesResourceWithRawResponse(
            client.collect_responses
        )
        self.crew = crew.AsyncCrewResourceWithRawResponse(client.crew)
        self.diffofarrival = diffofarrival.AsyncDiffofarrivalResourceWithRawResponse(client.diffofarrival)
        self.ecpsdr = ecpsdr.AsyncEcpsdrResourceWithRawResponse(client.ecpsdr)
        self.filedrop = filedrop.AsyncFiledropResourceWithRawResponse(client.filedrop)
        self.ground_imagery = ground_imagery.AsyncGroundImageryResourceWithRawResponse(client.ground_imagery)
        self.h3geo = h3geo.AsyncH3geoResourceWithRawResponse(client.h3geo)
        self.iono_observations = iono_observations.AsyncIonoObservationsResourceWithRawResponse(
            client.iono_observations
        )
        self.isr_collections = isr_collections.AsyncIsrCollectionsResourceWithRawResponse(client.isr_collections)
        self.items = items.AsyncItemsResourceWithRawResponse(client.items)
        self.item_trackings = item_trackings.AsyncItemTrackingsResourceWithRawResponse(client.item_trackings)
        self.launch_events = launch_events.AsyncLaunchEventsResourceWithRawResponse(client.launch_events)
        self.logistics_supports = logistics_supports.AsyncLogisticsSupportsResourceWithRawResponse(
            client.logistics_supports
        )
        self.maneuvers = maneuvers.AsyncManeuversResourceWithRawResponse(client.maneuvers)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResourceWithRawResponse(client.missile_tracks)
        self.udl_sar = udl_sar.AsyncUdlSarResourceWithRawResponse(client.udl_sar)
        self.udl_sensorplan = udl_sensorplan.AsyncUdlSensorplanResourceWithRawResponse(client.udl_sensorplan)
        self.udl_sgi = udl_sgi.AsyncUdlSgiResourceWithRawResponse(client.udl_sgi)
        self.udl_sigact = udl_sigact.AsyncUdlSigactResourceWithRawResponse(client.udl_sigact)
        self.udl_sigact_text = udl_sigact_text.AsyncUdlSigactTextResourceWithRawResponse(client.udl_sigact_text)
        self.udl_skyimagery = udl_skyimagery.AsyncUdlSkyimageryResourceWithRawResponse(client.udl_skyimagery)
        self.udl_soiobservationset = udl_soiobservationset.AsyncUdlSoiobservationsetResourceWithRawResponse(
            client.udl_soiobservationset
        )
        self.udl_sortieppr = udl_sortieppr.AsyncUdlSortiepprResourceWithRawResponse(client.udl_sortieppr)
        self.udl_spaceenvobs = udl_spaceenvobs.AsyncUdlSpaceenvobsResourceWithRawResponse(client.udl_spaceenvobs)
        self.udl_starcatalog = udl_starcatalog.AsyncUdlStarcatalogResourceWithRawResponse(client.udl_starcatalog)
        self.aircraft = aircraft.AsyncAircraftResourceWithRawResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AsyncAircraftSortiesResourceWithRawResponse(client.aircraft_sorties)
        self.aircraft_statuses = aircraft_statuses.AsyncAircraftStatusesResourceWithRawResponse(
            client.aircraft_statuses
        )
        self.aircraft_status_remarks = aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithRawResponse(
            client.aircraft_status_remarks
        )
        self.air_events = air_events.AsyncAirEventsResourceWithRawResponse(client.air_events)
        self.airfields = airfields.AsyncAirfieldsResourceWithRawResponse(client.airfields)
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResourceWithRawResponse(client.airfield_slots)
        self.airfieldslots = airfieldslots.AsyncAirfieldslotsResourceWithRawResponse(client.airfieldslots)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResourceWithRawResponse(
            client.airfieldslotconsumptions
        )
        self.airfieldstatus = airfieldstatus.AsyncAirfieldstatusResourceWithRawResponse(client.airfieldstatus)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResourceWithRawResponse(client.airfield_status)
        self.air_load_plans = air_load_plans.AsyncAirLoadPlansResourceWithRawResponse(client.air_load_plans)
        self.airloadplans = airloadplans.AsyncAirloadplansResourceWithRawResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResourceWithRawResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AsyncAirtaskingordersResourceWithRawResponse(client.airtaskingorders)
        self.air_tasking_orders = air_tasking_orders.AsyncAirTaskingOrdersResourceWithRawResponse(
            client.air_tasking_orders
        )
        self.air_transport_missions = air_transport_missions.AsyncAirTransportMissionsResourceWithRawResponse(
            client.air_transport_missions
        )
        self.ais = ais.AsyncAIsResourceWithRawResponse(client.ais)
        self.antennas = antennas.AsyncAntennasResourceWithRawResponse(client.antennas)
        self.onorbit = onorbit.AsyncOnorbitResourceWithRawResponse(client.onorbit)
        self.ephemeris = ephemeris.AsyncEphemerisResourceWithRawResponse(client.ephemeris)
        self.attitude_data = attitude_data.AsyncAttitudeDataResourceWithRawResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResourceWithRawResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AsyncAttitudesetsResourceWithRawResponse(client.attitudesets)
        self.batteries = batteries.AsyncBatteriesResourceWithRawResponse(client.batteries)
        self.batterydetails = batterydetails.AsyncBatterydetailsResourceWithRawResponse(client.batterydetails)
        self.beam = beam.AsyncBeamResourceWithRawResponse(client.beam)
        self.beam_contours = beam_contours.AsyncBeamContoursResourceWithRawResponse(client.beam_contours)
        self.buses = buses.AsyncBusesResourceWithRawResponse(client.buses)
        self.channels = channels.AsyncChannelsResourceWithRawResponse(client.channels)
        self.comm = comm.AsyncCommResourceWithRawResponse(client.comm)
        self.cots = cots.AsyncCotsResourceWithRawResponse(client.cots)
        self.countries = countries.AsyncCountriesResourceWithRawResponse(client.countries)
        self.link_status = link_status.AsyncLinkStatusResourceWithRawResponse(client.link_status)
        self.supporting_data = supporting_data.AsyncSupportingDataResourceWithRawResponse(client.supporting_data)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResourceWithRawResponse(client.tdoa_fdoa)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResourceWithRawResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.AsyncDriftHistoryResourceWithRawResponse(client.drift_history)
        self.mission_ops = mission_ops.AsyncMissionOpsResourceWithRawResponse(client.mission_ops)
        self.effect_requests = effect_requests.AsyncEffectRequestsResourceWithRawResponse(client.effect_requests)
        self.effect_responses = effect_responses.AsyncEffectResponsesResourceWithRawResponse(client.effect_responses)
        self.elsets = elsets.AsyncElsetsResourceWithRawResponse(client.elsets)
        self.engines = engines.AsyncEnginesResourceWithRawResponse(client.engines)
        self.enginedetails = enginedetails.AsyncEnginedetailsResourceWithRawResponse(client.enginedetails)
        self.engine_details = engine_details.AsyncEngineDetailsResourceWithRawResponse(client.engine_details)
        self.entities = entities.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.eo_observations = eo_observations.AsyncEoObservationsResourceWithRawResponse(client.eo_observations)
        self.eoobservations = eoobservations.AsyncEoobservationsResourceWithRawResponse(client.eoobservations)
        self.eop = eop.AsyncEopResourceWithRawResponse(client.eop)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResourceWithRawResponse(client.ephemeris_sets)
        self.equipment = equipment.AsyncEquipmentResourceWithRawResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.AsyncEquipmentremarksResourceWithRawResponse(client.equipmentremarks)
        self.evac = evac.AsyncEvacResourceWithRawResponse(client.evac)
        self.event_evolution = event_evolution.AsyncEventEvolutionResourceWithRawResponse(client.event_evolution)
        self.eventevolutions = eventevolutions.AsyncEventevolutionsResourceWithRawResponse(client.eventevolutions)
        self.flightplans = flightplans.AsyncFlightplansResourceWithRawResponse(client.flightplans)


class UnifieddatalibraryWithStreamedResponse:
    def __init__(self, client: Unifieddatalibrary) -> None:
        self.conjunctions = conjunctions.ConjunctionsResourceWithStreamingResponse(client.conjunctions)
        self.air_operations = air_operations.AirOperationsResourceWithStreamingResponse(client.air_operations)
        self.ephemerides = ephemerides.EphemeridesResourceWithStreamingResponse(client.ephemerides)
        self.observations = observations.ObservationsResourceWithStreamingResponse(client.observations)
        self.ais_objects = ais_objects.AIsObjectsResourceWithStreamingResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResourceWithStreamingResponse(client.analytic_imagery)
        self.collect_requests = collect_requests.CollectRequestsResourceWithStreamingResponse(client.collect_requests)
        self.collect_responses = collect_responses.CollectResponsesResourceWithStreamingResponse(
            client.collect_responses
        )
        self.crew = crew.CrewResourceWithStreamingResponse(client.crew)
        self.diffofarrival = diffofarrival.DiffofarrivalResourceWithStreamingResponse(client.diffofarrival)
        self.ecpsdr = ecpsdr.EcpsdrResourceWithStreamingResponse(client.ecpsdr)
        self.filedrop = filedrop.FiledropResourceWithStreamingResponse(client.filedrop)
        self.ground_imagery = ground_imagery.GroundImageryResourceWithStreamingResponse(client.ground_imagery)
        self.h3geo = h3geo.H3geoResourceWithStreamingResponse(client.h3geo)
        self.iono_observations = iono_observations.IonoObservationsResourceWithStreamingResponse(
            client.iono_observations
        )
        self.isr_collections = isr_collections.IsrCollectionsResourceWithStreamingResponse(client.isr_collections)
        self.items = items.ItemsResourceWithStreamingResponse(client.items)
        self.item_trackings = item_trackings.ItemTrackingsResourceWithStreamingResponse(client.item_trackings)
        self.launch_events = launch_events.LaunchEventsResourceWithStreamingResponse(client.launch_events)
        self.logistics_supports = logistics_supports.LogisticsSupportsResourceWithStreamingResponse(
            client.logistics_supports
        )
        self.maneuvers = maneuvers.ManeuversResourceWithStreamingResponse(client.maneuvers)
        self.missile_tracks = missile_tracks.MissileTracksResourceWithStreamingResponse(client.missile_tracks)
        self.udl_sar = udl_sar.UdlSarResourceWithStreamingResponse(client.udl_sar)
        self.udl_sensorplan = udl_sensorplan.UdlSensorplanResourceWithStreamingResponse(client.udl_sensorplan)
        self.udl_sgi = udl_sgi.UdlSgiResourceWithStreamingResponse(client.udl_sgi)
        self.udl_sigact = udl_sigact.UdlSigactResourceWithStreamingResponse(client.udl_sigact)
        self.udl_sigact_text = udl_sigact_text.UdlSigactTextResourceWithStreamingResponse(client.udl_sigact_text)
        self.udl_skyimagery = udl_skyimagery.UdlSkyimageryResourceWithStreamingResponse(client.udl_skyimagery)
        self.udl_soiobservationset = udl_soiobservationset.UdlSoiobservationsetResourceWithStreamingResponse(
            client.udl_soiobservationset
        )
        self.udl_sortieppr = udl_sortieppr.UdlSortiepprResourceWithStreamingResponse(client.udl_sortieppr)
        self.udl_spaceenvobs = udl_spaceenvobs.UdlSpaceenvobsResourceWithStreamingResponse(client.udl_spaceenvobs)
        self.udl_starcatalog = udl_starcatalog.UdlStarcatalogResourceWithStreamingResponse(client.udl_starcatalog)
        self.aircraft = aircraft.AircraftResourceWithStreamingResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResourceWithStreamingResponse(client.aircraft_sorties)
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResourceWithStreamingResponse(
            client.aircraft_statuses
        )
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResourceWithStreamingResponse(
            client.aircraft_status_remarks
        )
        self.air_events = air_events.AirEventsResourceWithStreamingResponse(client.air_events)
        self.airfields = airfields.AirfieldsResourceWithStreamingResponse(client.airfields)
        self.airfield_slots = airfield_slots.AirfieldSlotsResourceWithStreamingResponse(client.airfield_slots)
        self.airfieldslots = airfieldslots.AirfieldslotsResourceWithStreamingResponse(client.airfieldslots)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AirfieldslotconsumptionsResourceWithStreamingResponse(
            client.airfieldslotconsumptions
        )
        self.airfieldstatus = airfieldstatus.AirfieldstatusResourceWithStreamingResponse(client.airfieldstatus)
        self.airfield_status = airfield_status.AirfieldStatusResourceWithStreamingResponse(client.airfield_status)
        self.air_load_plans = air_load_plans.AirLoadPlansResourceWithStreamingResponse(client.air_load_plans)
        self.airloadplans = airloadplans.AirloadplansResourceWithStreamingResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResourceWithStreamingResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AirtaskingordersResourceWithStreamingResponse(client.airtaskingorders)
        self.air_tasking_orders = air_tasking_orders.AirTaskingOrdersResourceWithStreamingResponse(
            client.air_tasking_orders
        )
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResourceWithStreamingResponse(
            client.air_transport_missions
        )
        self.ais = ais.AIsResourceWithStreamingResponse(client.ais)
        self.antennas = antennas.AntennasResourceWithStreamingResponse(client.antennas)
        self.onorbit = onorbit.OnorbitResourceWithStreamingResponse(client.onorbit)
        self.ephemeris = ephemeris.EphemerisResourceWithStreamingResponse(client.ephemeris)
        self.attitude_data = attitude_data.AttitudeDataResourceWithStreamingResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AttitudeSetsResourceWithStreamingResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AttitudesetsResourceWithStreamingResponse(client.attitudesets)
        self.batteries = batteries.BatteriesResourceWithStreamingResponse(client.batteries)
        self.batterydetails = batterydetails.BatterydetailsResourceWithStreamingResponse(client.batterydetails)
        self.beam = beam.BeamResourceWithStreamingResponse(client.beam)
        self.beam_contours = beam_contours.BeamContoursResourceWithStreamingResponse(client.beam_contours)
        self.buses = buses.BusesResourceWithStreamingResponse(client.buses)
        self.channels = channels.ChannelsResourceWithStreamingResponse(client.channels)
        self.comm = comm.CommResourceWithStreamingResponse(client.comm)
        self.cots = cots.CotsResourceWithStreamingResponse(client.cots)
        self.countries = countries.CountriesResourceWithStreamingResponse(client.countries)
        self.link_status = link_status.LinkStatusResourceWithStreamingResponse(client.link_status)
        self.supporting_data = supporting_data.SupportingDataResourceWithStreamingResponse(client.supporting_data)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResourceWithStreamingResponse(client.tdoa_fdoa)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResourceWithStreamingResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.DriftHistoryResourceWithStreamingResponse(client.drift_history)
        self.mission_ops = mission_ops.MissionOpsResourceWithStreamingResponse(client.mission_ops)
        self.effect_requests = effect_requests.EffectRequestsResourceWithStreamingResponse(client.effect_requests)
        self.effect_responses = effect_responses.EffectResponsesResourceWithStreamingResponse(client.effect_responses)
        self.elsets = elsets.ElsetsResourceWithStreamingResponse(client.elsets)
        self.engines = engines.EnginesResourceWithStreamingResponse(client.engines)
        self.enginedetails = enginedetails.EnginedetailsResourceWithStreamingResponse(client.enginedetails)
        self.engine_details = engine_details.EngineDetailsResourceWithStreamingResponse(client.engine_details)
        self.entities = entities.EntitiesResourceWithStreamingResponse(client.entities)
        self.eo_observations = eo_observations.EoObservationsResourceWithStreamingResponse(client.eo_observations)
        self.eoobservations = eoobservations.EoobservationsResourceWithStreamingResponse(client.eoobservations)
        self.eop = eop.EopResourceWithStreamingResponse(client.eop)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResourceWithStreamingResponse(client.ephemeris_sets)
        self.equipment = equipment.EquipmentResourceWithStreamingResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.EquipmentremarksResourceWithStreamingResponse(client.equipmentremarks)
        self.evac = evac.EvacResourceWithStreamingResponse(client.evac)
        self.event_evolution = event_evolution.EventEvolutionResourceWithStreamingResponse(client.event_evolution)
        self.eventevolutions = eventevolutions.EventevolutionsResourceWithStreamingResponse(client.eventevolutions)
        self.flightplans = flightplans.FlightplansResourceWithStreamingResponse(client.flightplans)


class AsyncUnifieddatalibraryWithStreamedResponse:
    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self.conjunctions = conjunctions.AsyncConjunctionsResourceWithStreamingResponse(client.conjunctions)
        self.air_operations = air_operations.AsyncAirOperationsResourceWithStreamingResponse(client.air_operations)
        self.ephemerides = ephemerides.AsyncEphemeridesResourceWithStreamingResponse(client.ephemerides)
        self.observations = observations.AsyncObservationsResourceWithStreamingResponse(client.observations)
        self.ais_objects = ais_objects.AsyncAIsObjectsResourceWithStreamingResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResourceWithStreamingResponse(
            client.analytic_imagery
        )
        self.collect_requests = collect_requests.AsyncCollectRequestsResourceWithStreamingResponse(
            client.collect_requests
        )
        self.collect_responses = collect_responses.AsyncCollectResponsesResourceWithStreamingResponse(
            client.collect_responses
        )
        self.crew = crew.AsyncCrewResourceWithStreamingResponse(client.crew)
        self.diffofarrival = diffofarrival.AsyncDiffofarrivalResourceWithStreamingResponse(client.diffofarrival)
        self.ecpsdr = ecpsdr.AsyncEcpsdrResourceWithStreamingResponse(client.ecpsdr)
        self.filedrop = filedrop.AsyncFiledropResourceWithStreamingResponse(client.filedrop)
        self.ground_imagery = ground_imagery.AsyncGroundImageryResourceWithStreamingResponse(client.ground_imagery)
        self.h3geo = h3geo.AsyncH3geoResourceWithStreamingResponse(client.h3geo)
        self.iono_observations = iono_observations.AsyncIonoObservationsResourceWithStreamingResponse(
            client.iono_observations
        )
        self.isr_collections = isr_collections.AsyncIsrCollectionsResourceWithStreamingResponse(client.isr_collections)
        self.items = items.AsyncItemsResourceWithStreamingResponse(client.items)
        self.item_trackings = item_trackings.AsyncItemTrackingsResourceWithStreamingResponse(client.item_trackings)
        self.launch_events = launch_events.AsyncLaunchEventsResourceWithStreamingResponse(client.launch_events)
        self.logistics_supports = logistics_supports.AsyncLogisticsSupportsResourceWithStreamingResponse(
            client.logistics_supports
        )
        self.maneuvers = maneuvers.AsyncManeuversResourceWithStreamingResponse(client.maneuvers)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResourceWithStreamingResponse(client.missile_tracks)
        self.udl_sar = udl_sar.AsyncUdlSarResourceWithStreamingResponse(client.udl_sar)
        self.udl_sensorplan = udl_sensorplan.AsyncUdlSensorplanResourceWithStreamingResponse(client.udl_sensorplan)
        self.udl_sgi = udl_sgi.AsyncUdlSgiResourceWithStreamingResponse(client.udl_sgi)
        self.udl_sigact = udl_sigact.AsyncUdlSigactResourceWithStreamingResponse(client.udl_sigact)
        self.udl_sigact_text = udl_sigact_text.AsyncUdlSigactTextResourceWithStreamingResponse(client.udl_sigact_text)
        self.udl_skyimagery = udl_skyimagery.AsyncUdlSkyimageryResourceWithStreamingResponse(client.udl_skyimagery)
        self.udl_soiobservationset = udl_soiobservationset.AsyncUdlSoiobservationsetResourceWithStreamingResponse(
            client.udl_soiobservationset
        )
        self.udl_sortieppr = udl_sortieppr.AsyncUdlSortiepprResourceWithStreamingResponse(client.udl_sortieppr)
        self.udl_spaceenvobs = udl_spaceenvobs.AsyncUdlSpaceenvobsResourceWithStreamingResponse(client.udl_spaceenvobs)
        self.udl_starcatalog = udl_starcatalog.AsyncUdlStarcatalogResourceWithStreamingResponse(client.udl_starcatalog)
        self.aircraft = aircraft.AsyncAircraftResourceWithStreamingResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AsyncAircraftSortiesResourceWithStreamingResponse(
            client.aircraft_sorties
        )
        self.aircraft_statuses = aircraft_statuses.AsyncAircraftStatusesResourceWithStreamingResponse(
            client.aircraft_statuses
        )
        self.aircraft_status_remarks = aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithStreamingResponse(
            client.aircraft_status_remarks
        )
        self.air_events = air_events.AsyncAirEventsResourceWithStreamingResponse(client.air_events)
        self.airfields = airfields.AsyncAirfieldsResourceWithStreamingResponse(client.airfields)
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResourceWithStreamingResponse(client.airfield_slots)
        self.airfieldslots = airfieldslots.AsyncAirfieldslotsResourceWithStreamingResponse(client.airfieldslots)
        self.airfieldslotconsumptions = (
            airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResourceWithStreamingResponse(
                client.airfieldslotconsumptions
            )
        )
        self.airfieldstatus = airfieldstatus.AsyncAirfieldstatusResourceWithStreamingResponse(client.airfieldstatus)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResourceWithStreamingResponse(client.airfield_status)
        self.air_load_plans = air_load_plans.AsyncAirLoadPlansResourceWithStreamingResponse(client.air_load_plans)
        self.airloadplans = airloadplans.AsyncAirloadplansResourceWithStreamingResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResourceWithStreamingResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AsyncAirtaskingordersResourceWithStreamingResponse(
            client.airtaskingorders
        )
        self.air_tasking_orders = air_tasking_orders.AsyncAirTaskingOrdersResourceWithStreamingResponse(
            client.air_tasking_orders
        )
        self.air_transport_missions = air_transport_missions.AsyncAirTransportMissionsResourceWithStreamingResponse(
            client.air_transport_missions
        )
        self.ais = ais.AsyncAIsResourceWithStreamingResponse(client.ais)
        self.antennas = antennas.AsyncAntennasResourceWithStreamingResponse(client.antennas)
        self.onorbit = onorbit.AsyncOnorbitResourceWithStreamingResponse(client.onorbit)
        self.ephemeris = ephemeris.AsyncEphemerisResourceWithStreamingResponse(client.ephemeris)
        self.attitude_data = attitude_data.AsyncAttitudeDataResourceWithStreamingResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResourceWithStreamingResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AsyncAttitudesetsResourceWithStreamingResponse(client.attitudesets)
        self.batteries = batteries.AsyncBatteriesResourceWithStreamingResponse(client.batteries)
        self.batterydetails = batterydetails.AsyncBatterydetailsResourceWithStreamingResponse(client.batterydetails)
        self.beam = beam.AsyncBeamResourceWithStreamingResponse(client.beam)
        self.beam_contours = beam_contours.AsyncBeamContoursResourceWithStreamingResponse(client.beam_contours)
        self.buses = buses.AsyncBusesResourceWithStreamingResponse(client.buses)
        self.channels = channels.AsyncChannelsResourceWithStreamingResponse(client.channels)
        self.comm = comm.AsyncCommResourceWithStreamingResponse(client.comm)
        self.cots = cots.AsyncCotsResourceWithStreamingResponse(client.cots)
        self.countries = countries.AsyncCountriesResourceWithStreamingResponse(client.countries)
        self.link_status = link_status.AsyncLinkStatusResourceWithStreamingResponse(client.link_status)
        self.supporting_data = supporting_data.AsyncSupportingDataResourceWithStreamingResponse(client.supporting_data)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResourceWithStreamingResponse(client.tdoa_fdoa)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResourceWithStreamingResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.AsyncDriftHistoryResourceWithStreamingResponse(client.drift_history)
        self.mission_ops = mission_ops.AsyncMissionOpsResourceWithStreamingResponse(client.mission_ops)
        self.effect_requests = effect_requests.AsyncEffectRequestsResourceWithStreamingResponse(client.effect_requests)
        self.effect_responses = effect_responses.AsyncEffectResponsesResourceWithStreamingResponse(
            client.effect_responses
        )
        self.elsets = elsets.AsyncElsetsResourceWithStreamingResponse(client.elsets)
        self.engines = engines.AsyncEnginesResourceWithStreamingResponse(client.engines)
        self.enginedetails = enginedetails.AsyncEnginedetailsResourceWithStreamingResponse(client.enginedetails)
        self.engine_details = engine_details.AsyncEngineDetailsResourceWithStreamingResponse(client.engine_details)
        self.entities = entities.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.eo_observations = eo_observations.AsyncEoObservationsResourceWithStreamingResponse(client.eo_observations)
        self.eoobservations = eoobservations.AsyncEoobservationsResourceWithStreamingResponse(client.eoobservations)
        self.eop = eop.AsyncEopResourceWithStreamingResponse(client.eop)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResourceWithStreamingResponse(client.ephemeris_sets)
        self.equipment = equipment.AsyncEquipmentResourceWithStreamingResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.AsyncEquipmentremarksResourceWithStreamingResponse(
            client.equipmentremarks
        )
        self.evac = evac.AsyncEvacResourceWithStreamingResponse(client.evac)
        self.event_evolution = event_evolution.AsyncEventEvolutionResourceWithStreamingResponse(client.event_evolution)
        self.eventevolutions = eventevolutions.AsyncEventevolutionsResourceWithStreamingResponse(client.eventevolutions)
        self.flightplans = flightplans.AsyncFlightplansResourceWithStreamingResponse(client.flightplans)


Client = Unifieddatalibrary

AsyncClient = AsyncUnifieddatalibrary
