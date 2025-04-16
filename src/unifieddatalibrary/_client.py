# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
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
    ir,
    mti,
    poi,
    beam,
    comm,
    cots,
    crew,
    item,
    port,
    buses,
    stage,
    ecpsdr,
    rfband,
    status,
    vessel,
    engines,
    surface,
    aircraft,
    antennas,
    channels,
    dropzone,
    entities,
    location,
    manifold,
    airfields,
    batteries,
    countries,
    equipment,
    geostatus,
    gnssrawif,
    monoradar,
    rfemitter,
    scs_views,
    substatus,
    air_events,
    flightplan,
    launchsite,
    navigation,
    rfbandtype,
    routestats,
    scientific,
    sensortype,
    siteremark,
    solararray,
    ais_objects,
    launchevent,
    onorbitlist,
    transponder,
    airloadplans,
    attitudesets,
    h3geohexcell,
    notification,
    onorbitevent,
    organization,
    airfieldslots,
    attitude_data,
    beam_contours,
    drift_history,
    enginedetails,
    groundimagery,
    launchvehicle,
    manifoldelset,
    operatingunit,
    air_load_plans,
    airfield_slots,
    batterydetails,
    engine_details,
    eoobservations,
    onorbitantenna,
    onorbitbattery,
    onorbitdetails,
    airfield_status,
    ionoobservation,
    launchdetection,
    onorbitthruster,
    aircraft_sorties,
    airtaskingorders,
    analytic_imagery,
    equipmentremarks,
    objectofinterest,
    radarobservation,
    rfemitterdetails,
    secure_messaging,
    launchsitedetails,
    onboardnavigation,
    onorbitsolararray,
    solararraydetails,
    air_tasking_orders,
    emittergeolocation,
    gnssobservationset,
    seradatanavigation,
    surfaceobstruction,
    operatingunitremark,
    organizationdetails,
    seradatacommdetails,
    aircraftstatusremark,
    launchvehicledetails,
    seradataearlywarning,
    seradataradarpayload,
    sensorobservationtype,
    seradatasigintpayload,
    aviationriskmanagement,
    seradataopticalpayload,
    aircraft_status_remarks,
    airspace_control_orders,
    navigationalobstruction,
    airfieldslotconsumptions,
    seradataspacecraftdetails,
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
from .resources.scs import scs
from .resources.sgi import sgi
from .resources.udl import udl
from .resources.evac import evac
from .resources.site import site
from .resources.swir import swir
from .resources.h3geo import h3geo
from .resources.track import track
from .resources.video import video
from .resources.elsets import elsets
from .resources.hazard import hazard
from .resources.sensor import sensor
from .resources.sigact import sigact
from .resources.taiutc import taiutc
from .resources.onorbit import onorbit
from .resources.ephemeris import ephemeris
from .resources.maneuvers import maneuvers
from .resources.sortieppr import sortieppr
from .resources.tdoa_fdoa import tdoa_fdoa
from .resources.orbittrack import orbittrack
from .resources.sensorplan import sensorplan
from .resources.sitestatus import sitestatus
from .resources.skyimagery import skyimagery
from .resources.trackroute import trackroute
from .resources.gnss_raw_if import gnss_raw_if
from .resources.link_status import link_status
from .resources.starcatalog import starcatalog
from .resources.statevector import statevector
from .resources.weatherdata import weatherdata
from .resources.conjunctions import conjunctions
from .resources.launch_event import launch_event
from .resources.observations import observations
from .resources.trackdetails import trackdetails
from .resources.attitude_sets import attitude_sets
from .resources.diffofarrival import diffofarrival
from .resources.rfobservation import rfobservation
from .resources.weatherreport import weatherreport
from .resources.air_operations import air_operations
from .resources.airfieldstatus import airfieldstatus
from .resources.ephemeris_sets import ephemeris_sets
from .resources.ground_imagery import ground_imagery
from .resources.item_trackings import item_trackings
from .resources.missile_tracks import missile_tracks
from .resources.sarobservation import sarobservation
from .resources.effect_requests import effect_requests
from .resources.eo_observations import eo_observations
from .resources.event_evolution import event_evolution
from .resources.isr_collections import isr_collections
from .resources.supporting_data import supporting_data
from .resources.collect_requests import collect_requests
from .resources.effect_responses import effect_responses
from .resources.iono_observation import iono_observation
from .resources.logisticssupport import logisticssupport
from .resources.aircraft_statuses import aircraft_statuses
from .resources.collect_responses import collect_responses
from .resources.featureassessment import featureassessment
from .resources.gnss_observations import gnss_observations
from .resources.missionassignment import missionassignment
from .resources.personnelrecovery import personnelrecovery
from .resources.sensormaintenance import sensormaintenance
from .resources.soiobservationset import soiobservationset
from .resources.orbitdetermination import orbitdetermination
from .resources.report_and_activity import report_and_activity
from .resources.spaceenvobservation import spaceenvobservation
from .resources.diplomatic_clearance import diplomatic_clearance
from .resources.onorbitthrusterstatus import onorbitthrusterstatus
from .resources.air_transport_missions import air_transport_missions
from .resources.globalatmosphericmodel import globalatmosphericmodel
from .resources.passiveradarobservation import passiveradarobservation

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
    air_events: air_events.AirEventsResource
    air_load_plans: air_load_plans.AirLoadPlansResource
    air_operations: air_operations.AirOperationsResource
    air_tasking_orders: air_tasking_orders.AirTaskingOrdersResource
    air_transport_missions: air_transport_missions.AirTransportMissionsResource
    aircraft: aircraft.AircraftResource
    aircraft_sorties: aircraft_sorties.AircraftSortiesResource
    aircraft_status_remarks: aircraft_status_remarks.AircraftStatusRemarksResource
    aircraft_statuses: aircraft_statuses.AircraftStatusesResource
    aircraftstatusremark: aircraftstatusremark.AircraftstatusremarkResource
    airfield_slots: airfield_slots.AirfieldSlotsResource
    airfield_status: airfield_status.AirfieldStatusResource
    airfields: airfields.AirfieldsResource
    airfieldslotconsumptions: airfieldslotconsumptions.AirfieldslotconsumptionsResource
    airfieldslots: airfieldslots.AirfieldslotsResource
    airfieldstatus: airfieldstatus.AirfieldstatusResource
    airloadplans: airloadplans.AirloadplansResource
    airspace_control_orders: airspace_control_orders.AirspaceControlOrdersResource
    airtaskingorders: airtaskingorders.AirtaskingordersResource
    ais: ais.AIsResource
    ais_objects: ais_objects.AIsObjectsResource
    analytic_imagery: analytic_imagery.AnalyticImageryResource
    antennas: antennas.AntennasResource
    attitude_data: attitude_data.AttitudeDataResource
    attitude_sets: attitude_sets.AttitudeSetsResource
    attitudesets: attitudesets.AttitudesetsResource
    batteries: batteries.BatteriesResource
    batterydetails: batterydetails.BatterydetailsResource
    beam: beam.BeamResource
    beam_contours: beam_contours.BeamContoursResource
    buses: buses.BusesResource
    channels: channels.ChannelsResource
    collect_requests: collect_requests.CollectRequestsResource
    collect_responses: collect_responses.CollectResponsesResource
    comm: comm.CommResource
    conjunctions: conjunctions.ConjunctionsResource
    cots: cots.CotsResource
    aviationriskmanagement: aviationriskmanagement.AviationriskmanagementResource
    dropzone: dropzone.DropzoneResource
    emittergeolocation: emittergeolocation.EmittergeolocationResource
    featureassessment: featureassessment.FeatureassessmentResource
    globalatmosphericmodel: globalatmosphericmodel.GlobalatmosphericmodelResource
    routestats: routestats.RoutestatsResource
    countries: countries.CountriesResource
    crew: crew.CrewResource
    diffofarrival: diffofarrival.DiffofarrivalResource
    diplomatic_clearance: diplomatic_clearance.DiplomaticClearanceResource
    drift_history: drift_history.DriftHistoryResource
    ecpsdr: ecpsdr.EcpsdrResource
    effect_requests: effect_requests.EffectRequestsResource
    effect_responses: effect_responses.EffectResponsesResource
    elsets: elsets.ElsetsResource
    engine_details: engine_details.EngineDetailsResource
    enginedetails: enginedetails.EnginedetailsResource
    engines: engines.EnginesResource
    entities: entities.EntitiesResource
    eo_observations: eo_observations.EoObservationsResource
    eoobservations: eoobservations.EoobservationsResource
    eop: eop.EopResource
    ephemeris: ephemeris.EphemerisResource
    ephemeris_sets: ephemeris_sets.EphemerisSetsResource
    equipment: equipment.EquipmentResource
    equipmentremarks: equipmentremarks.EquipmentremarksResource
    evac: evac.EvacResource
    event_evolution: event_evolution.EventEvolutionResource
    flightplan: flightplan.FlightplanResource
    geostatus: geostatus.GeostatusResource
    gnssobservationset: gnssobservationset.GnssobservationsetResource
    gnssrawif: gnssrawif.GnssrawifResource
    ground_imagery: ground_imagery.GroundImageryResource
    groundimagery: groundimagery.GroundimageryResource
    h3geo: h3geo.H3geoResource
    h3geohexcell: h3geohexcell.H3geohexcellResource
    hazard: hazard.HazardResource
    ionoobservation: ionoobservation.IonoobservationResource
    ir: ir.IrResource
    isr_collections: isr_collections.IsrCollectionsResource
    item: item.ItemResource
    item_trackings: item_trackings.ItemTrackingsResource
    launchdetection: launchdetection.LaunchdetectionResource
    launchevent: launchevent.LauncheventResource
    launchsite: launchsite.LaunchsiteResource
    launchsitedetails: launchsitedetails.LaunchsitedetailsResource
    launchvehicle: launchvehicle.LaunchvehicleResource
    launchvehicledetails: launchvehicledetails.LaunchvehicledetailsResource
    link_status: link_status.LinkStatusResource
    location: location.LocationResource
    logisticssupport: logisticssupport.LogisticssupportResource
    maneuvers: maneuvers.ManeuversResource
    manifold: manifold.ManifoldResource
    manifoldelset: manifoldelset.ManifoldelsetResource
    missile_tracks: missile_tracks.MissileTracksResource
    missionassignment: missionassignment.MissionassignmentResource
    monoradar: monoradar.MonoradarResource
    mti: mti.MtiResource
    navigation: navigation.NavigationResource
    navigationalobstruction: navigationalobstruction.NavigationalobstructionResource
    notification: notification.NotificationResource
    objectofinterest: objectofinterest.ObjectofinterestResource
    observations: observations.ObservationsResource
    onboardnavigation: onboardnavigation.OnboardnavigationResource
    onorbit: onorbit.OnorbitResource
    onorbitantenna: onorbitantenna.OnorbitantennaResource
    onorbitbattery: onorbitbattery.OnorbitbatteryResource
    onorbitdetails: onorbitdetails.OnorbitdetailsResource
    onorbitevent: onorbitevent.OnorbiteventResource
    onorbitlist: onorbitlist.OnorbitlistResource
    onorbitsolararray: onorbitsolararray.OnorbitsolararrayResource
    onorbitthruster: onorbitthruster.OnorbitthrusterResource
    onorbitthrusterstatus: onorbitthrusterstatus.OnorbitthrusterstatusResource
    operatingunit: operatingunit.OperatingunitResource
    operatingunitremark: operatingunitremark.OperatingunitremarkResource
    orbitdetermination: orbitdetermination.OrbitdeterminationResource
    orbittrack: orbittrack.OrbittrackResource
    organization: organization.OrganizationResource
    organizationdetails: organizationdetails.OrganizationdetailsResource
    passiveradarobservation: passiveradarobservation.PassiveradarobservationResource
    personnelrecovery: personnelrecovery.PersonnelrecoveryResource
    poi: poi.PoiResource
    port: port.PortResource
    radarobservation: radarobservation.RadarobservationResource
    rfband: rfband.RfbandResource
    rfbandtype: rfbandtype.RfbandtypeResource
    rfemitter: rfemitter.RfemitterResource
    rfemitterdetails: rfemitterdetails.RfemitterdetailsResource
    rfobservation: rfobservation.RfobservationResource
    sarobservation: sarobservation.SarobservationResource
    scientific: scientific.ScientificResource
    sensor: sensor.SensorResource
    sensormaintenance: sensormaintenance.SensormaintenanceResource
    sensorobservationtype: sensorobservationtype.SensorobservationtypeResource
    sensorplan: sensorplan.SensorplanResource
    sensortype: sensortype.SensortypeResource
    seradatacommdetails: seradatacommdetails.SeradatacommdetailsResource
    seradataearlywarning: seradataearlywarning.SeradataearlywarningResource
    seradatanavigation: seradatanavigation.SeradatanavigationResource
    seradataopticalpayload: seradataopticalpayload.SeradataopticalpayloadResource
    seradataradarpayload: seradataradarpayload.SeradataradarpayloadResource
    seradatasigintpayload: seradatasigintpayload.SeradatasigintpayloadResource
    seradataspacecraftdetails: seradataspacecraftdetails.SeradataspacecraftdetailsResource
    sgi: sgi.SgiResource
    sigact: sigact.SigactResource
    site: site.SiteResource
    siteremark: siteremark.SiteremarkResource
    sitestatus: sitestatus.SitestatusResource
    skyimagery: skyimagery.SkyimageryResource
    soiobservationset: soiobservationset.SoiobservationsetResource
    solararray: solararray.SolararrayResource
    solararraydetails: solararraydetails.SolararraydetailsResource
    sortieppr: sortieppr.SortiepprResource
    spaceenvobservation: spaceenvobservation.SpaceenvobservationResource
    stage: stage.StageResource
    starcatalog: starcatalog.StarcatalogResource
    statevector: statevector.StatevectorResource
    status: status.StatusResource
    substatus: substatus.SubstatusResource
    supporting_data: supporting_data.SupportingDataResource
    surface: surface.SurfaceResource
    surfaceobstruction: surfaceobstruction.SurfaceobstructionResource
    swir: swir.SwirResource
    taiutc: taiutc.TaiutcResource
    tdoa_fdoa: tdoa_fdoa.TdoaFdoaResource
    track: track.TrackResource
    trackdetails: trackdetails.TrackdetailsResource
    trackroute: trackroute.TrackrouteResource
    transponder: transponder.TransponderResource
    vessel: vessel.VesselResource
    video: video.VideoResource
    weatherdata: weatherdata.WeatherdataResource
    weatherreport: weatherreport.WeatherreportResource
    udl: udl.UdlResource
    gnss_observations: gnss_observations.GnssObservationsResource
    gnss_raw_if: gnss_raw_if.GnssRawIfResource
    iono_observation: iono_observation.IonoObservationResource
    launch_event: launch_event.LaunchEventResource
    report_and_activity: report_and_activity.ReportAndActivityResource
    secure_messaging: secure_messaging.SecureMessagingResource
    scs: scs.ScsResource
    scs_views: scs_views.ScsViewsResource
    with_raw_response: UnifieddatalibraryWithRawResponse
    with_streaming_response: UnifieddatalibraryWithStreamedResponse

    # client options
    password: str
    username: str

    def __init__(
        self,
        *,
        password: str | None = None,
        username: str | None = None,
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
        """Construct a new synchronous Unifieddatalibrary client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `password` from `UDL_AUTH_PASSWORD`
        - `username` from `UDL_AUTH_USERNAME`
        """
        if password is None:
            password = os.environ.get("UDL_AUTH_PASSWORD")
        if password is None:
            raise UnifieddatalibraryError(
                "The password client option must be set either by passing password to the client or by setting the UDL_AUTH_PASSWORD environment variable"
            )
        self.password = password

        if username is None:
            username = os.environ.get("UDL_AUTH_USERNAME")
        if username is None:
            raise UnifieddatalibraryError(
                "The username client option must be set either by passing username to the client or by setting the UDL_AUTH_USERNAME environment variable"
            )
        self.username = username

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

        self.air_events = air_events.AirEventsResource(self)
        self.air_load_plans = air_load_plans.AirLoadPlansResource(self)
        self.air_operations = air_operations.AirOperationsResource(self)
        self.air_tasking_orders = air_tasking_orders.AirTaskingOrdersResource(self)
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResource(self)
        self.aircraft = aircraft.AircraftResource(self)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResource(self)
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResource(self)
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResource(self)
        self.aircraftstatusremark = aircraftstatusremark.AircraftstatusremarkResource(self)
        self.airfield_slots = airfield_slots.AirfieldSlotsResource(self)
        self.airfield_status = airfield_status.AirfieldStatusResource(self)
        self.airfields = airfields.AirfieldsResource(self)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AirfieldslotconsumptionsResource(self)
        self.airfieldslots = airfieldslots.AirfieldslotsResource(self)
        self.airfieldstatus = airfieldstatus.AirfieldstatusResource(self)
        self.airloadplans = airloadplans.AirloadplansResource(self)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResource(self)
        self.airtaskingorders = airtaskingorders.AirtaskingordersResource(self)
        self.ais = ais.AIsResource(self)
        self.ais_objects = ais_objects.AIsObjectsResource(self)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResource(self)
        self.antennas = antennas.AntennasResource(self)
        self.attitude_data = attitude_data.AttitudeDataResource(self)
        self.attitude_sets = attitude_sets.AttitudeSetsResource(self)
        self.attitudesets = attitudesets.AttitudesetsResource(self)
        self.batteries = batteries.BatteriesResource(self)
        self.batterydetails = batterydetails.BatterydetailsResource(self)
        self.beam = beam.BeamResource(self)
        self.beam_contours = beam_contours.BeamContoursResource(self)
        self.buses = buses.BusesResource(self)
        self.channels = channels.ChannelsResource(self)
        self.collect_requests = collect_requests.CollectRequestsResource(self)
        self.collect_responses = collect_responses.CollectResponsesResource(self)
        self.comm = comm.CommResource(self)
        self.conjunctions = conjunctions.ConjunctionsResource(self)
        self.cots = cots.CotsResource(self)
        self.aviationriskmanagement = aviationriskmanagement.AviationriskmanagementResource(self)
        self.dropzone = dropzone.DropzoneResource(self)
        self.emittergeolocation = emittergeolocation.EmittergeolocationResource(self)
        self.featureassessment = featureassessment.FeatureassessmentResource(self)
        self.globalatmosphericmodel = globalatmosphericmodel.GlobalatmosphericmodelResource(self)
        self.routestats = routestats.RoutestatsResource(self)
        self.countries = countries.CountriesResource(self)
        self.crew = crew.CrewResource(self)
        self.diffofarrival = diffofarrival.DiffofarrivalResource(self)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResource(self)
        self.drift_history = drift_history.DriftHistoryResource(self)
        self.ecpsdr = ecpsdr.EcpsdrResource(self)
        self.effect_requests = effect_requests.EffectRequestsResource(self)
        self.effect_responses = effect_responses.EffectResponsesResource(self)
        self.elsets = elsets.ElsetsResource(self)
        self.engine_details = engine_details.EngineDetailsResource(self)
        self.enginedetails = enginedetails.EnginedetailsResource(self)
        self.engines = engines.EnginesResource(self)
        self.entities = entities.EntitiesResource(self)
        self.eo_observations = eo_observations.EoObservationsResource(self)
        self.eoobservations = eoobservations.EoobservationsResource(self)
        self.eop = eop.EopResource(self)
        self.ephemeris = ephemeris.EphemerisResource(self)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResource(self)
        self.equipment = equipment.EquipmentResource(self)
        self.equipmentremarks = equipmentremarks.EquipmentremarksResource(self)
        self.evac = evac.EvacResource(self)
        self.event_evolution = event_evolution.EventEvolutionResource(self)
        self.flightplan = flightplan.FlightplanResource(self)
        self.geostatus = geostatus.GeostatusResource(self)
        self.gnssobservationset = gnssobservationset.GnssobservationsetResource(self)
        self.gnssrawif = gnssrawif.GnssrawifResource(self)
        self.ground_imagery = ground_imagery.GroundImageryResource(self)
        self.groundimagery = groundimagery.GroundimageryResource(self)
        self.h3geo = h3geo.H3geoResource(self)
        self.h3geohexcell = h3geohexcell.H3geohexcellResource(self)
        self.hazard = hazard.HazardResource(self)
        self.ionoobservation = ionoobservation.IonoobservationResource(self)
        self.ir = ir.IrResource(self)
        self.isr_collections = isr_collections.IsrCollectionsResource(self)
        self.item = item.ItemResource(self)
        self.item_trackings = item_trackings.ItemTrackingsResource(self)
        self.launchdetection = launchdetection.LaunchdetectionResource(self)
        self.launchevent = launchevent.LauncheventResource(self)
        self.launchsite = launchsite.LaunchsiteResource(self)
        self.launchsitedetails = launchsitedetails.LaunchsitedetailsResource(self)
        self.launchvehicle = launchvehicle.LaunchvehicleResource(self)
        self.launchvehicledetails = launchvehicledetails.LaunchvehicledetailsResource(self)
        self.link_status = link_status.LinkStatusResource(self)
        self.location = location.LocationResource(self)
        self.logisticssupport = logisticssupport.LogisticssupportResource(self)
        self.maneuvers = maneuvers.ManeuversResource(self)
        self.manifold = manifold.ManifoldResource(self)
        self.manifoldelset = manifoldelset.ManifoldelsetResource(self)
        self.missile_tracks = missile_tracks.MissileTracksResource(self)
        self.missionassignment = missionassignment.MissionassignmentResource(self)
        self.monoradar = monoradar.MonoradarResource(self)
        self.mti = mti.MtiResource(self)
        self.navigation = navigation.NavigationResource(self)
        self.navigationalobstruction = navigationalobstruction.NavigationalobstructionResource(self)
        self.notification = notification.NotificationResource(self)
        self.objectofinterest = objectofinterest.ObjectofinterestResource(self)
        self.observations = observations.ObservationsResource(self)
        self.onboardnavigation = onboardnavigation.OnboardnavigationResource(self)
        self.onorbit = onorbit.OnorbitResource(self)
        self.onorbitantenna = onorbitantenna.OnorbitantennaResource(self)
        self.onorbitbattery = onorbitbattery.OnorbitbatteryResource(self)
        self.onorbitdetails = onorbitdetails.OnorbitdetailsResource(self)
        self.onorbitevent = onorbitevent.OnorbiteventResource(self)
        self.onorbitlist = onorbitlist.OnorbitlistResource(self)
        self.onorbitsolararray = onorbitsolararray.OnorbitsolararrayResource(self)
        self.onorbitthruster = onorbitthruster.OnorbitthrusterResource(self)
        self.onorbitthrusterstatus = onorbitthrusterstatus.OnorbitthrusterstatusResource(self)
        self.operatingunit = operatingunit.OperatingunitResource(self)
        self.operatingunitremark = operatingunitremark.OperatingunitremarkResource(self)
        self.orbitdetermination = orbitdetermination.OrbitdeterminationResource(self)
        self.orbittrack = orbittrack.OrbittrackResource(self)
        self.organization = organization.OrganizationResource(self)
        self.organizationdetails = organizationdetails.OrganizationdetailsResource(self)
        self.passiveradarobservation = passiveradarobservation.PassiveradarobservationResource(self)
        self.personnelrecovery = personnelrecovery.PersonnelrecoveryResource(self)
        self.poi = poi.PoiResource(self)
        self.port = port.PortResource(self)
        self.radarobservation = radarobservation.RadarobservationResource(self)
        self.rfband = rfband.RfbandResource(self)
        self.rfbandtype = rfbandtype.RfbandtypeResource(self)
        self.rfemitter = rfemitter.RfemitterResource(self)
        self.rfemitterdetails = rfemitterdetails.RfemitterdetailsResource(self)
        self.rfobservation = rfobservation.RfobservationResource(self)
        self.sarobservation = sarobservation.SarobservationResource(self)
        self.scientific = scientific.ScientificResource(self)
        self.sensor = sensor.SensorResource(self)
        self.sensormaintenance = sensormaintenance.SensormaintenanceResource(self)
        self.sensorobservationtype = sensorobservationtype.SensorobservationtypeResource(self)
        self.sensorplan = sensorplan.SensorplanResource(self)
        self.sensortype = sensortype.SensortypeResource(self)
        self.seradatacommdetails = seradatacommdetails.SeradatacommdetailsResource(self)
        self.seradataearlywarning = seradataearlywarning.SeradataearlywarningResource(self)
        self.seradatanavigation = seradatanavigation.SeradatanavigationResource(self)
        self.seradataopticalpayload = seradataopticalpayload.SeradataopticalpayloadResource(self)
        self.seradataradarpayload = seradataradarpayload.SeradataradarpayloadResource(self)
        self.seradatasigintpayload = seradatasigintpayload.SeradatasigintpayloadResource(self)
        self.seradataspacecraftdetails = seradataspacecraftdetails.SeradataspacecraftdetailsResource(self)
        self.sgi = sgi.SgiResource(self)
        self.sigact = sigact.SigactResource(self)
        self.site = site.SiteResource(self)
        self.siteremark = siteremark.SiteremarkResource(self)
        self.sitestatus = sitestatus.SitestatusResource(self)
        self.skyimagery = skyimagery.SkyimageryResource(self)
        self.soiobservationset = soiobservationset.SoiobservationsetResource(self)
        self.solararray = solararray.SolararrayResource(self)
        self.solararraydetails = solararraydetails.SolararraydetailsResource(self)
        self.sortieppr = sortieppr.SortiepprResource(self)
        self.spaceenvobservation = spaceenvobservation.SpaceenvobservationResource(self)
        self.stage = stage.StageResource(self)
        self.starcatalog = starcatalog.StarcatalogResource(self)
        self.statevector = statevector.StatevectorResource(self)
        self.status = status.StatusResource(self)
        self.substatus = substatus.SubstatusResource(self)
        self.supporting_data = supporting_data.SupportingDataResource(self)
        self.surface = surface.SurfaceResource(self)
        self.surfaceobstruction = surfaceobstruction.SurfaceobstructionResource(self)
        self.swir = swir.SwirResource(self)
        self.taiutc = taiutc.TaiutcResource(self)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResource(self)
        self.track = track.TrackResource(self)
        self.trackdetails = trackdetails.TrackdetailsResource(self)
        self.trackroute = trackroute.TrackrouteResource(self)
        self.transponder = transponder.TransponderResource(self)
        self.vessel = vessel.VesselResource(self)
        self.video = video.VideoResource(self)
        self.weatherdata = weatherdata.WeatherdataResource(self)
        self.weatherreport = weatherreport.WeatherreportResource(self)
        self.udl = udl.UdlResource(self)
        self.gnss_observations = gnss_observations.GnssObservationsResource(self)
        self.gnss_raw_if = gnss_raw_if.GnssRawIfResource(self)
        self.iono_observation = iono_observation.IonoObservationResource(self)
        self.launch_event = launch_event.LaunchEventResource(self)
        self.report_and_activity = report_and_activity.ReportAndActivityResource(self)
        self.secure_messaging = secure_messaging.SecureMessagingResource(self)
        self.scs = scs.ScsResource(self)
        self.scs_views = scs_views.ScsViewsResource(self)
        self.with_raw_response = UnifieddatalibraryWithRawResponse(self)
        self.with_streaming_response = UnifieddatalibraryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

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
        password: str | None = None,
        username: str | None = None,
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
            password=password or self.password,
            username=username or self.username,
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
    air_events: air_events.AsyncAirEventsResource
    air_load_plans: air_load_plans.AsyncAirLoadPlansResource
    air_operations: air_operations.AsyncAirOperationsResource
    air_tasking_orders: air_tasking_orders.AsyncAirTaskingOrdersResource
    air_transport_missions: air_transport_missions.AsyncAirTransportMissionsResource
    aircraft: aircraft.AsyncAircraftResource
    aircraft_sorties: aircraft_sorties.AsyncAircraftSortiesResource
    aircraft_status_remarks: aircraft_status_remarks.AsyncAircraftStatusRemarksResource
    aircraft_statuses: aircraft_statuses.AsyncAircraftStatusesResource
    aircraftstatusremark: aircraftstatusremark.AsyncAircraftstatusremarkResource
    airfield_slots: airfield_slots.AsyncAirfieldSlotsResource
    airfield_status: airfield_status.AsyncAirfieldStatusResource
    airfields: airfields.AsyncAirfieldsResource
    airfieldslotconsumptions: airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResource
    airfieldslots: airfieldslots.AsyncAirfieldslotsResource
    airfieldstatus: airfieldstatus.AsyncAirfieldstatusResource
    airloadplans: airloadplans.AsyncAirloadplansResource
    airspace_control_orders: airspace_control_orders.AsyncAirspaceControlOrdersResource
    airtaskingorders: airtaskingorders.AsyncAirtaskingordersResource
    ais: ais.AsyncAIsResource
    ais_objects: ais_objects.AsyncAIsObjectsResource
    analytic_imagery: analytic_imagery.AsyncAnalyticImageryResource
    antennas: antennas.AsyncAntennasResource
    attitude_data: attitude_data.AsyncAttitudeDataResource
    attitude_sets: attitude_sets.AsyncAttitudeSetsResource
    attitudesets: attitudesets.AsyncAttitudesetsResource
    batteries: batteries.AsyncBatteriesResource
    batterydetails: batterydetails.AsyncBatterydetailsResource
    beam: beam.AsyncBeamResource
    beam_contours: beam_contours.AsyncBeamContoursResource
    buses: buses.AsyncBusesResource
    channels: channels.AsyncChannelsResource
    collect_requests: collect_requests.AsyncCollectRequestsResource
    collect_responses: collect_responses.AsyncCollectResponsesResource
    comm: comm.AsyncCommResource
    conjunctions: conjunctions.AsyncConjunctionsResource
    cots: cots.AsyncCotsResource
    aviationriskmanagement: aviationriskmanagement.AsyncAviationriskmanagementResource
    dropzone: dropzone.AsyncDropzoneResource
    emittergeolocation: emittergeolocation.AsyncEmittergeolocationResource
    featureassessment: featureassessment.AsyncFeatureassessmentResource
    globalatmosphericmodel: globalatmosphericmodel.AsyncGlobalatmosphericmodelResource
    routestats: routestats.AsyncRoutestatsResource
    countries: countries.AsyncCountriesResource
    crew: crew.AsyncCrewResource
    diffofarrival: diffofarrival.AsyncDiffofarrivalResource
    diplomatic_clearance: diplomatic_clearance.AsyncDiplomaticClearanceResource
    drift_history: drift_history.AsyncDriftHistoryResource
    ecpsdr: ecpsdr.AsyncEcpsdrResource
    effect_requests: effect_requests.AsyncEffectRequestsResource
    effect_responses: effect_responses.AsyncEffectResponsesResource
    elsets: elsets.AsyncElsetsResource
    engine_details: engine_details.AsyncEngineDetailsResource
    enginedetails: enginedetails.AsyncEnginedetailsResource
    engines: engines.AsyncEnginesResource
    entities: entities.AsyncEntitiesResource
    eo_observations: eo_observations.AsyncEoObservationsResource
    eoobservations: eoobservations.AsyncEoobservationsResource
    eop: eop.AsyncEopResource
    ephemeris: ephemeris.AsyncEphemerisResource
    ephemeris_sets: ephemeris_sets.AsyncEphemerisSetsResource
    equipment: equipment.AsyncEquipmentResource
    equipmentremarks: equipmentremarks.AsyncEquipmentremarksResource
    evac: evac.AsyncEvacResource
    event_evolution: event_evolution.AsyncEventEvolutionResource
    flightplan: flightplan.AsyncFlightplanResource
    geostatus: geostatus.AsyncGeostatusResource
    gnssobservationset: gnssobservationset.AsyncGnssobservationsetResource
    gnssrawif: gnssrawif.AsyncGnssrawifResource
    ground_imagery: ground_imagery.AsyncGroundImageryResource
    groundimagery: groundimagery.AsyncGroundimageryResource
    h3geo: h3geo.AsyncH3geoResource
    h3geohexcell: h3geohexcell.AsyncH3geohexcellResource
    hazard: hazard.AsyncHazardResource
    ionoobservation: ionoobservation.AsyncIonoobservationResource
    ir: ir.AsyncIrResource
    isr_collections: isr_collections.AsyncIsrCollectionsResource
    item: item.AsyncItemResource
    item_trackings: item_trackings.AsyncItemTrackingsResource
    launchdetection: launchdetection.AsyncLaunchdetectionResource
    launchevent: launchevent.AsyncLauncheventResource
    launchsite: launchsite.AsyncLaunchsiteResource
    launchsitedetails: launchsitedetails.AsyncLaunchsitedetailsResource
    launchvehicle: launchvehicle.AsyncLaunchvehicleResource
    launchvehicledetails: launchvehicledetails.AsyncLaunchvehicledetailsResource
    link_status: link_status.AsyncLinkStatusResource
    location: location.AsyncLocationResource
    logisticssupport: logisticssupport.AsyncLogisticssupportResource
    maneuvers: maneuvers.AsyncManeuversResource
    manifold: manifold.AsyncManifoldResource
    manifoldelset: manifoldelset.AsyncManifoldelsetResource
    missile_tracks: missile_tracks.AsyncMissileTracksResource
    missionassignment: missionassignment.AsyncMissionassignmentResource
    monoradar: monoradar.AsyncMonoradarResource
    mti: mti.AsyncMtiResource
    navigation: navigation.AsyncNavigationResource
    navigationalobstruction: navigationalobstruction.AsyncNavigationalobstructionResource
    notification: notification.AsyncNotificationResource
    objectofinterest: objectofinterest.AsyncObjectofinterestResource
    observations: observations.AsyncObservationsResource
    onboardnavigation: onboardnavigation.AsyncOnboardnavigationResource
    onorbit: onorbit.AsyncOnorbitResource
    onorbitantenna: onorbitantenna.AsyncOnorbitantennaResource
    onorbitbattery: onorbitbattery.AsyncOnorbitbatteryResource
    onorbitdetails: onorbitdetails.AsyncOnorbitdetailsResource
    onorbitevent: onorbitevent.AsyncOnorbiteventResource
    onorbitlist: onorbitlist.AsyncOnorbitlistResource
    onorbitsolararray: onorbitsolararray.AsyncOnorbitsolararrayResource
    onorbitthruster: onorbitthruster.AsyncOnorbitthrusterResource
    onorbitthrusterstatus: onorbitthrusterstatus.AsyncOnorbitthrusterstatusResource
    operatingunit: operatingunit.AsyncOperatingunitResource
    operatingunitremark: operatingunitremark.AsyncOperatingunitremarkResource
    orbitdetermination: orbitdetermination.AsyncOrbitdeterminationResource
    orbittrack: orbittrack.AsyncOrbittrackResource
    organization: organization.AsyncOrganizationResource
    organizationdetails: organizationdetails.AsyncOrganizationdetailsResource
    passiveradarobservation: passiveradarobservation.AsyncPassiveradarobservationResource
    personnelrecovery: personnelrecovery.AsyncPersonnelrecoveryResource
    poi: poi.AsyncPoiResource
    port: port.AsyncPortResource
    radarobservation: radarobservation.AsyncRadarobservationResource
    rfband: rfband.AsyncRfbandResource
    rfbandtype: rfbandtype.AsyncRfbandtypeResource
    rfemitter: rfemitter.AsyncRfemitterResource
    rfemitterdetails: rfemitterdetails.AsyncRfemitterdetailsResource
    rfobservation: rfobservation.AsyncRfobservationResource
    sarobservation: sarobservation.AsyncSarobservationResource
    scientific: scientific.AsyncScientificResource
    sensor: sensor.AsyncSensorResource
    sensormaintenance: sensormaintenance.AsyncSensormaintenanceResource
    sensorobservationtype: sensorobservationtype.AsyncSensorobservationtypeResource
    sensorplan: sensorplan.AsyncSensorplanResource
    sensortype: sensortype.AsyncSensortypeResource
    seradatacommdetails: seradatacommdetails.AsyncSeradatacommdetailsResource
    seradataearlywarning: seradataearlywarning.AsyncSeradataearlywarningResource
    seradatanavigation: seradatanavigation.AsyncSeradatanavigationResource
    seradataopticalpayload: seradataopticalpayload.AsyncSeradataopticalpayloadResource
    seradataradarpayload: seradataradarpayload.AsyncSeradataradarpayloadResource
    seradatasigintpayload: seradatasigintpayload.AsyncSeradatasigintpayloadResource
    seradataspacecraftdetails: seradataspacecraftdetails.AsyncSeradataspacecraftdetailsResource
    sgi: sgi.AsyncSgiResource
    sigact: sigact.AsyncSigactResource
    site: site.AsyncSiteResource
    siteremark: siteremark.AsyncSiteremarkResource
    sitestatus: sitestatus.AsyncSitestatusResource
    skyimagery: skyimagery.AsyncSkyimageryResource
    soiobservationset: soiobservationset.AsyncSoiobservationsetResource
    solararray: solararray.AsyncSolararrayResource
    solararraydetails: solararraydetails.AsyncSolararraydetailsResource
    sortieppr: sortieppr.AsyncSortiepprResource
    spaceenvobservation: spaceenvobservation.AsyncSpaceenvobservationResource
    stage: stage.AsyncStageResource
    starcatalog: starcatalog.AsyncStarcatalogResource
    statevector: statevector.AsyncStatevectorResource
    status: status.AsyncStatusResource
    substatus: substatus.AsyncSubstatusResource
    supporting_data: supporting_data.AsyncSupportingDataResource
    surface: surface.AsyncSurfaceResource
    surfaceobstruction: surfaceobstruction.AsyncSurfaceobstructionResource
    swir: swir.AsyncSwirResource
    taiutc: taiutc.AsyncTaiutcResource
    tdoa_fdoa: tdoa_fdoa.AsyncTdoaFdoaResource
    track: track.AsyncTrackResource
    trackdetails: trackdetails.AsyncTrackdetailsResource
    trackroute: trackroute.AsyncTrackrouteResource
    transponder: transponder.AsyncTransponderResource
    vessel: vessel.AsyncVesselResource
    video: video.AsyncVideoResource
    weatherdata: weatherdata.AsyncWeatherdataResource
    weatherreport: weatherreport.AsyncWeatherreportResource
    udl: udl.AsyncUdlResource
    gnss_observations: gnss_observations.AsyncGnssObservationsResource
    gnss_raw_if: gnss_raw_if.AsyncGnssRawIfResource
    iono_observation: iono_observation.AsyncIonoObservationResource
    launch_event: launch_event.AsyncLaunchEventResource
    report_and_activity: report_and_activity.AsyncReportAndActivityResource
    secure_messaging: secure_messaging.AsyncSecureMessagingResource
    scs: scs.AsyncScsResource
    scs_views: scs_views.AsyncScsViewsResource
    with_raw_response: AsyncUnifieddatalibraryWithRawResponse
    with_streaming_response: AsyncUnifieddatalibraryWithStreamedResponse

    # client options
    password: str
    username: str

    def __init__(
        self,
        *,
        password: str | None = None,
        username: str | None = None,
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
        """Construct a new async AsyncUnifieddatalibrary client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `password` from `UDL_AUTH_PASSWORD`
        - `username` from `UDL_AUTH_USERNAME`
        """
        if password is None:
            password = os.environ.get("UDL_AUTH_PASSWORD")
        if password is None:
            raise UnifieddatalibraryError(
                "The password client option must be set either by passing password to the client or by setting the UDL_AUTH_PASSWORD environment variable"
            )
        self.password = password

        if username is None:
            username = os.environ.get("UDL_AUTH_USERNAME")
        if username is None:
            raise UnifieddatalibraryError(
                "The username client option must be set either by passing username to the client or by setting the UDL_AUTH_USERNAME environment variable"
            )
        self.username = username

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

        self.air_events = air_events.AsyncAirEventsResource(self)
        self.air_load_plans = air_load_plans.AsyncAirLoadPlansResource(self)
        self.air_operations = air_operations.AsyncAirOperationsResource(self)
        self.air_tasking_orders = air_tasking_orders.AsyncAirTaskingOrdersResource(self)
        self.air_transport_missions = air_transport_missions.AsyncAirTransportMissionsResource(self)
        self.aircraft = aircraft.AsyncAircraftResource(self)
        self.aircraft_sorties = aircraft_sorties.AsyncAircraftSortiesResource(self)
        self.aircraft_status_remarks = aircraft_status_remarks.AsyncAircraftStatusRemarksResource(self)
        self.aircraft_statuses = aircraft_statuses.AsyncAircraftStatusesResource(self)
        self.aircraftstatusremark = aircraftstatusremark.AsyncAircraftstatusremarkResource(self)
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResource(self)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResource(self)
        self.airfields = airfields.AsyncAirfieldsResource(self)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResource(self)
        self.airfieldslots = airfieldslots.AsyncAirfieldslotsResource(self)
        self.airfieldstatus = airfieldstatus.AsyncAirfieldstatusResource(self)
        self.airloadplans = airloadplans.AsyncAirloadplansResource(self)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResource(self)
        self.airtaskingorders = airtaskingorders.AsyncAirtaskingordersResource(self)
        self.ais = ais.AsyncAIsResource(self)
        self.ais_objects = ais_objects.AsyncAIsObjectsResource(self)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResource(self)
        self.antennas = antennas.AsyncAntennasResource(self)
        self.attitude_data = attitude_data.AsyncAttitudeDataResource(self)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResource(self)
        self.attitudesets = attitudesets.AsyncAttitudesetsResource(self)
        self.batteries = batteries.AsyncBatteriesResource(self)
        self.batterydetails = batterydetails.AsyncBatterydetailsResource(self)
        self.beam = beam.AsyncBeamResource(self)
        self.beam_contours = beam_contours.AsyncBeamContoursResource(self)
        self.buses = buses.AsyncBusesResource(self)
        self.channels = channels.AsyncChannelsResource(self)
        self.collect_requests = collect_requests.AsyncCollectRequestsResource(self)
        self.collect_responses = collect_responses.AsyncCollectResponsesResource(self)
        self.comm = comm.AsyncCommResource(self)
        self.conjunctions = conjunctions.AsyncConjunctionsResource(self)
        self.cots = cots.AsyncCotsResource(self)
        self.aviationriskmanagement = aviationriskmanagement.AsyncAviationriskmanagementResource(self)
        self.dropzone = dropzone.AsyncDropzoneResource(self)
        self.emittergeolocation = emittergeolocation.AsyncEmittergeolocationResource(self)
        self.featureassessment = featureassessment.AsyncFeatureassessmentResource(self)
        self.globalatmosphericmodel = globalatmosphericmodel.AsyncGlobalatmosphericmodelResource(self)
        self.routestats = routestats.AsyncRoutestatsResource(self)
        self.countries = countries.AsyncCountriesResource(self)
        self.crew = crew.AsyncCrewResource(self)
        self.diffofarrival = diffofarrival.AsyncDiffofarrivalResource(self)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResource(self)
        self.drift_history = drift_history.AsyncDriftHistoryResource(self)
        self.ecpsdr = ecpsdr.AsyncEcpsdrResource(self)
        self.effect_requests = effect_requests.AsyncEffectRequestsResource(self)
        self.effect_responses = effect_responses.AsyncEffectResponsesResource(self)
        self.elsets = elsets.AsyncElsetsResource(self)
        self.engine_details = engine_details.AsyncEngineDetailsResource(self)
        self.enginedetails = enginedetails.AsyncEnginedetailsResource(self)
        self.engines = engines.AsyncEnginesResource(self)
        self.entities = entities.AsyncEntitiesResource(self)
        self.eo_observations = eo_observations.AsyncEoObservationsResource(self)
        self.eoobservations = eoobservations.AsyncEoobservationsResource(self)
        self.eop = eop.AsyncEopResource(self)
        self.ephemeris = ephemeris.AsyncEphemerisResource(self)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResource(self)
        self.equipment = equipment.AsyncEquipmentResource(self)
        self.equipmentremarks = equipmentremarks.AsyncEquipmentremarksResource(self)
        self.evac = evac.AsyncEvacResource(self)
        self.event_evolution = event_evolution.AsyncEventEvolutionResource(self)
        self.flightplan = flightplan.AsyncFlightplanResource(self)
        self.geostatus = geostatus.AsyncGeostatusResource(self)
        self.gnssobservationset = gnssobservationset.AsyncGnssobservationsetResource(self)
        self.gnssrawif = gnssrawif.AsyncGnssrawifResource(self)
        self.ground_imagery = ground_imagery.AsyncGroundImageryResource(self)
        self.groundimagery = groundimagery.AsyncGroundimageryResource(self)
        self.h3geo = h3geo.AsyncH3geoResource(self)
        self.h3geohexcell = h3geohexcell.AsyncH3geohexcellResource(self)
        self.hazard = hazard.AsyncHazardResource(self)
        self.ionoobservation = ionoobservation.AsyncIonoobservationResource(self)
        self.ir = ir.AsyncIrResource(self)
        self.isr_collections = isr_collections.AsyncIsrCollectionsResource(self)
        self.item = item.AsyncItemResource(self)
        self.item_trackings = item_trackings.AsyncItemTrackingsResource(self)
        self.launchdetection = launchdetection.AsyncLaunchdetectionResource(self)
        self.launchevent = launchevent.AsyncLauncheventResource(self)
        self.launchsite = launchsite.AsyncLaunchsiteResource(self)
        self.launchsitedetails = launchsitedetails.AsyncLaunchsitedetailsResource(self)
        self.launchvehicle = launchvehicle.AsyncLaunchvehicleResource(self)
        self.launchvehicledetails = launchvehicledetails.AsyncLaunchvehicledetailsResource(self)
        self.link_status = link_status.AsyncLinkStatusResource(self)
        self.location = location.AsyncLocationResource(self)
        self.logisticssupport = logisticssupport.AsyncLogisticssupportResource(self)
        self.maneuvers = maneuvers.AsyncManeuversResource(self)
        self.manifold = manifold.AsyncManifoldResource(self)
        self.manifoldelset = manifoldelset.AsyncManifoldelsetResource(self)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResource(self)
        self.missionassignment = missionassignment.AsyncMissionassignmentResource(self)
        self.monoradar = monoradar.AsyncMonoradarResource(self)
        self.mti = mti.AsyncMtiResource(self)
        self.navigation = navigation.AsyncNavigationResource(self)
        self.navigationalobstruction = navigationalobstruction.AsyncNavigationalobstructionResource(self)
        self.notification = notification.AsyncNotificationResource(self)
        self.objectofinterest = objectofinterest.AsyncObjectofinterestResource(self)
        self.observations = observations.AsyncObservationsResource(self)
        self.onboardnavigation = onboardnavigation.AsyncOnboardnavigationResource(self)
        self.onorbit = onorbit.AsyncOnorbitResource(self)
        self.onorbitantenna = onorbitantenna.AsyncOnorbitantennaResource(self)
        self.onorbitbattery = onorbitbattery.AsyncOnorbitbatteryResource(self)
        self.onorbitdetails = onorbitdetails.AsyncOnorbitdetailsResource(self)
        self.onorbitevent = onorbitevent.AsyncOnorbiteventResource(self)
        self.onorbitlist = onorbitlist.AsyncOnorbitlistResource(self)
        self.onorbitsolararray = onorbitsolararray.AsyncOnorbitsolararrayResource(self)
        self.onorbitthruster = onorbitthruster.AsyncOnorbitthrusterResource(self)
        self.onorbitthrusterstatus = onorbitthrusterstatus.AsyncOnorbitthrusterstatusResource(self)
        self.operatingunit = operatingunit.AsyncOperatingunitResource(self)
        self.operatingunitremark = operatingunitremark.AsyncOperatingunitremarkResource(self)
        self.orbitdetermination = orbitdetermination.AsyncOrbitdeterminationResource(self)
        self.orbittrack = orbittrack.AsyncOrbittrackResource(self)
        self.organization = organization.AsyncOrganizationResource(self)
        self.organizationdetails = organizationdetails.AsyncOrganizationdetailsResource(self)
        self.passiveradarobservation = passiveradarobservation.AsyncPassiveradarobservationResource(self)
        self.personnelrecovery = personnelrecovery.AsyncPersonnelrecoveryResource(self)
        self.poi = poi.AsyncPoiResource(self)
        self.port = port.AsyncPortResource(self)
        self.radarobservation = radarobservation.AsyncRadarobservationResource(self)
        self.rfband = rfband.AsyncRfbandResource(self)
        self.rfbandtype = rfbandtype.AsyncRfbandtypeResource(self)
        self.rfemitter = rfemitter.AsyncRfemitterResource(self)
        self.rfemitterdetails = rfemitterdetails.AsyncRfemitterdetailsResource(self)
        self.rfobservation = rfobservation.AsyncRfobservationResource(self)
        self.sarobservation = sarobservation.AsyncSarobservationResource(self)
        self.scientific = scientific.AsyncScientificResource(self)
        self.sensor = sensor.AsyncSensorResource(self)
        self.sensormaintenance = sensormaintenance.AsyncSensormaintenanceResource(self)
        self.sensorobservationtype = sensorobservationtype.AsyncSensorobservationtypeResource(self)
        self.sensorplan = sensorplan.AsyncSensorplanResource(self)
        self.sensortype = sensortype.AsyncSensortypeResource(self)
        self.seradatacommdetails = seradatacommdetails.AsyncSeradatacommdetailsResource(self)
        self.seradataearlywarning = seradataearlywarning.AsyncSeradataearlywarningResource(self)
        self.seradatanavigation = seradatanavigation.AsyncSeradatanavigationResource(self)
        self.seradataopticalpayload = seradataopticalpayload.AsyncSeradataopticalpayloadResource(self)
        self.seradataradarpayload = seradataradarpayload.AsyncSeradataradarpayloadResource(self)
        self.seradatasigintpayload = seradatasigintpayload.AsyncSeradatasigintpayloadResource(self)
        self.seradataspacecraftdetails = seradataspacecraftdetails.AsyncSeradataspacecraftdetailsResource(self)
        self.sgi = sgi.AsyncSgiResource(self)
        self.sigact = sigact.AsyncSigactResource(self)
        self.site = site.AsyncSiteResource(self)
        self.siteremark = siteremark.AsyncSiteremarkResource(self)
        self.sitestatus = sitestatus.AsyncSitestatusResource(self)
        self.skyimagery = skyimagery.AsyncSkyimageryResource(self)
        self.soiobservationset = soiobservationset.AsyncSoiobservationsetResource(self)
        self.solararray = solararray.AsyncSolararrayResource(self)
        self.solararraydetails = solararraydetails.AsyncSolararraydetailsResource(self)
        self.sortieppr = sortieppr.AsyncSortiepprResource(self)
        self.spaceenvobservation = spaceenvobservation.AsyncSpaceenvobservationResource(self)
        self.stage = stage.AsyncStageResource(self)
        self.starcatalog = starcatalog.AsyncStarcatalogResource(self)
        self.statevector = statevector.AsyncStatevectorResource(self)
        self.status = status.AsyncStatusResource(self)
        self.substatus = substatus.AsyncSubstatusResource(self)
        self.supporting_data = supporting_data.AsyncSupportingDataResource(self)
        self.surface = surface.AsyncSurfaceResource(self)
        self.surfaceobstruction = surfaceobstruction.AsyncSurfaceobstructionResource(self)
        self.swir = swir.AsyncSwirResource(self)
        self.taiutc = taiutc.AsyncTaiutcResource(self)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResource(self)
        self.track = track.AsyncTrackResource(self)
        self.trackdetails = trackdetails.AsyncTrackdetailsResource(self)
        self.trackroute = trackroute.AsyncTrackrouteResource(self)
        self.transponder = transponder.AsyncTransponderResource(self)
        self.vessel = vessel.AsyncVesselResource(self)
        self.video = video.AsyncVideoResource(self)
        self.weatherdata = weatherdata.AsyncWeatherdataResource(self)
        self.weatherreport = weatherreport.AsyncWeatherreportResource(self)
        self.udl = udl.AsyncUdlResource(self)
        self.gnss_observations = gnss_observations.AsyncGnssObservationsResource(self)
        self.gnss_raw_if = gnss_raw_if.AsyncGnssRawIfResource(self)
        self.iono_observation = iono_observation.AsyncIonoObservationResource(self)
        self.launch_event = launch_event.AsyncLaunchEventResource(self)
        self.report_and_activity = report_and_activity.AsyncReportAndActivityResource(self)
        self.secure_messaging = secure_messaging.AsyncSecureMessagingResource(self)
        self.scs = scs.AsyncScsResource(self)
        self.scs_views = scs_views.AsyncScsViewsResource(self)
        self.with_raw_response = AsyncUnifieddatalibraryWithRawResponse(self)
        self.with_streaming_response = AsyncUnifieddatalibraryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

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
        password: str | None = None,
        username: str | None = None,
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
            password=password or self.password,
            username=username or self.username,
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
        self.air_events = air_events.AirEventsResourceWithRawResponse(client.air_events)
        self.air_load_plans = air_load_plans.AirLoadPlansResourceWithRawResponse(client.air_load_plans)
        self.air_operations = air_operations.AirOperationsResourceWithRawResponse(client.air_operations)
        self.air_tasking_orders = air_tasking_orders.AirTaskingOrdersResourceWithRawResponse(client.air_tasking_orders)
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResourceWithRawResponse(
            client.air_transport_missions
        )
        self.aircraft = aircraft.AircraftResourceWithRawResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResourceWithRawResponse(client.aircraft_sorties)
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResourceWithRawResponse(
            client.aircraft_status_remarks
        )
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResourceWithRawResponse(client.aircraft_statuses)
        self.aircraftstatusremark = aircraftstatusremark.AircraftstatusremarkResourceWithRawResponse(
            client.aircraftstatusremark
        )
        self.airfield_slots = airfield_slots.AirfieldSlotsResourceWithRawResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AirfieldStatusResourceWithRawResponse(client.airfield_status)
        self.airfields = airfields.AirfieldsResourceWithRawResponse(client.airfields)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AirfieldslotconsumptionsResourceWithRawResponse(
            client.airfieldslotconsumptions
        )
        self.airfieldslots = airfieldslots.AirfieldslotsResourceWithRawResponse(client.airfieldslots)
        self.airfieldstatus = airfieldstatus.AirfieldstatusResourceWithRawResponse(client.airfieldstatus)
        self.airloadplans = airloadplans.AirloadplansResourceWithRawResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResourceWithRawResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AirtaskingordersResourceWithRawResponse(client.airtaskingorders)
        self.ais = ais.AIsResourceWithRawResponse(client.ais)
        self.ais_objects = ais_objects.AIsObjectsResourceWithRawResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResourceWithRawResponse(client.analytic_imagery)
        self.antennas = antennas.AntennasResourceWithRawResponse(client.antennas)
        self.attitude_data = attitude_data.AttitudeDataResourceWithRawResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AttitudeSetsResourceWithRawResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AttitudesetsResourceWithRawResponse(client.attitudesets)
        self.batteries = batteries.BatteriesResourceWithRawResponse(client.batteries)
        self.batterydetails = batterydetails.BatterydetailsResourceWithRawResponse(client.batterydetails)
        self.beam = beam.BeamResourceWithRawResponse(client.beam)
        self.beam_contours = beam_contours.BeamContoursResourceWithRawResponse(client.beam_contours)
        self.buses = buses.BusesResourceWithRawResponse(client.buses)
        self.channels = channels.ChannelsResourceWithRawResponse(client.channels)
        self.collect_requests = collect_requests.CollectRequestsResourceWithRawResponse(client.collect_requests)
        self.collect_responses = collect_responses.CollectResponsesResourceWithRawResponse(client.collect_responses)
        self.comm = comm.CommResourceWithRawResponse(client.comm)
        self.conjunctions = conjunctions.ConjunctionsResourceWithRawResponse(client.conjunctions)
        self.cots = cots.CotsResourceWithRawResponse(client.cots)
        self.aviationriskmanagement = aviationriskmanagement.AviationriskmanagementResourceWithRawResponse(
            client.aviationriskmanagement
        )
        self.dropzone = dropzone.DropzoneResourceWithRawResponse(client.dropzone)
        self.emittergeolocation = emittergeolocation.EmittergeolocationResourceWithRawResponse(
            client.emittergeolocation
        )
        self.featureassessment = featureassessment.FeatureassessmentResourceWithRawResponse(client.featureassessment)
        self.globalatmosphericmodel = globalatmosphericmodel.GlobalatmosphericmodelResourceWithRawResponse(
            client.globalatmosphericmodel
        )
        self.routestats = routestats.RoutestatsResourceWithRawResponse(client.routestats)
        self.countries = countries.CountriesResourceWithRawResponse(client.countries)
        self.crew = crew.CrewResourceWithRawResponse(client.crew)
        self.diffofarrival = diffofarrival.DiffofarrivalResourceWithRawResponse(client.diffofarrival)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResourceWithRawResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.DriftHistoryResourceWithRawResponse(client.drift_history)
        self.ecpsdr = ecpsdr.EcpsdrResourceWithRawResponse(client.ecpsdr)
        self.effect_requests = effect_requests.EffectRequestsResourceWithRawResponse(client.effect_requests)
        self.effect_responses = effect_responses.EffectResponsesResourceWithRawResponse(client.effect_responses)
        self.elsets = elsets.ElsetsResourceWithRawResponse(client.elsets)
        self.engine_details = engine_details.EngineDetailsResourceWithRawResponse(client.engine_details)
        self.enginedetails = enginedetails.EnginedetailsResourceWithRawResponse(client.enginedetails)
        self.engines = engines.EnginesResourceWithRawResponse(client.engines)
        self.entities = entities.EntitiesResourceWithRawResponse(client.entities)
        self.eo_observations = eo_observations.EoObservationsResourceWithRawResponse(client.eo_observations)
        self.eoobservations = eoobservations.EoobservationsResourceWithRawResponse(client.eoobservations)
        self.eop = eop.EopResourceWithRawResponse(client.eop)
        self.ephemeris = ephemeris.EphemerisResourceWithRawResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResourceWithRawResponse(client.ephemeris_sets)
        self.equipment = equipment.EquipmentResourceWithRawResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.EquipmentremarksResourceWithRawResponse(client.equipmentremarks)
        self.evac = evac.EvacResourceWithRawResponse(client.evac)
        self.event_evolution = event_evolution.EventEvolutionResourceWithRawResponse(client.event_evolution)
        self.flightplan = flightplan.FlightplanResourceWithRawResponse(client.flightplan)
        self.geostatus = geostatus.GeostatusResourceWithRawResponse(client.geostatus)
        self.gnssobservationset = gnssobservationset.GnssobservationsetResourceWithRawResponse(
            client.gnssobservationset
        )
        self.gnssrawif = gnssrawif.GnssrawifResourceWithRawResponse(client.gnssrawif)
        self.ground_imagery = ground_imagery.GroundImageryResourceWithRawResponse(client.ground_imagery)
        self.groundimagery = groundimagery.GroundimageryResourceWithRawResponse(client.groundimagery)
        self.h3geo = h3geo.H3geoResourceWithRawResponse(client.h3geo)
        self.h3geohexcell = h3geohexcell.H3geohexcellResourceWithRawResponse(client.h3geohexcell)
        self.hazard = hazard.HazardResourceWithRawResponse(client.hazard)
        self.ionoobservation = ionoobservation.IonoobservationResourceWithRawResponse(client.ionoobservation)
        self.ir = ir.IrResourceWithRawResponse(client.ir)
        self.isr_collections = isr_collections.IsrCollectionsResourceWithRawResponse(client.isr_collections)
        self.item = item.ItemResourceWithRawResponse(client.item)
        self.item_trackings = item_trackings.ItemTrackingsResourceWithRawResponse(client.item_trackings)
        self.launchdetection = launchdetection.LaunchdetectionResourceWithRawResponse(client.launchdetection)
        self.launchevent = launchevent.LauncheventResourceWithRawResponse(client.launchevent)
        self.launchsite = launchsite.LaunchsiteResourceWithRawResponse(client.launchsite)
        self.launchsitedetails = launchsitedetails.LaunchsitedetailsResourceWithRawResponse(client.launchsitedetails)
        self.launchvehicle = launchvehicle.LaunchvehicleResourceWithRawResponse(client.launchvehicle)
        self.launchvehicledetails = launchvehicledetails.LaunchvehicledetailsResourceWithRawResponse(
            client.launchvehicledetails
        )
        self.link_status = link_status.LinkStatusResourceWithRawResponse(client.link_status)
        self.location = location.LocationResourceWithRawResponse(client.location)
        self.logisticssupport = logisticssupport.LogisticssupportResourceWithRawResponse(client.logisticssupport)
        self.maneuvers = maneuvers.ManeuversResourceWithRawResponse(client.maneuvers)
        self.manifold = manifold.ManifoldResourceWithRawResponse(client.manifold)
        self.manifoldelset = manifoldelset.ManifoldelsetResourceWithRawResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.MissileTracksResourceWithRawResponse(client.missile_tracks)
        self.missionassignment = missionassignment.MissionassignmentResourceWithRawResponse(client.missionassignment)
        self.monoradar = monoradar.MonoradarResourceWithRawResponse(client.monoradar)
        self.mti = mti.MtiResourceWithRawResponse(client.mti)
        self.navigation = navigation.NavigationResourceWithRawResponse(client.navigation)
        self.navigationalobstruction = navigationalobstruction.NavigationalobstructionResourceWithRawResponse(
            client.navigationalobstruction
        )
        self.notification = notification.NotificationResourceWithRawResponse(client.notification)
        self.objectofinterest = objectofinterest.ObjectofinterestResourceWithRawResponse(client.objectofinterest)
        self.observations = observations.ObservationsResourceWithRawResponse(client.observations)
        self.onboardnavigation = onboardnavigation.OnboardnavigationResourceWithRawResponse(client.onboardnavigation)
        self.onorbit = onorbit.OnorbitResourceWithRawResponse(client.onorbit)
        self.onorbitantenna = onorbitantenna.OnorbitantennaResourceWithRawResponse(client.onorbitantenna)
        self.onorbitbattery = onorbitbattery.OnorbitbatteryResourceWithRawResponse(client.onorbitbattery)
        self.onorbitdetails = onorbitdetails.OnorbitdetailsResourceWithRawResponse(client.onorbitdetails)
        self.onorbitevent = onorbitevent.OnorbiteventResourceWithRawResponse(client.onorbitevent)
        self.onorbitlist = onorbitlist.OnorbitlistResourceWithRawResponse(client.onorbitlist)
        self.onorbitsolararray = onorbitsolararray.OnorbitsolararrayResourceWithRawResponse(client.onorbitsolararray)
        self.onorbitthruster = onorbitthruster.OnorbitthrusterResourceWithRawResponse(client.onorbitthruster)
        self.onorbitthrusterstatus = onorbitthrusterstatus.OnorbitthrusterstatusResourceWithRawResponse(
            client.onorbitthrusterstatus
        )
        self.operatingunit = operatingunit.OperatingunitResourceWithRawResponse(client.operatingunit)
        self.operatingunitremark = operatingunitremark.OperatingunitremarkResourceWithRawResponse(
            client.operatingunitremark
        )
        self.orbitdetermination = orbitdetermination.OrbitdeterminationResourceWithRawResponse(
            client.orbitdetermination
        )
        self.orbittrack = orbittrack.OrbittrackResourceWithRawResponse(client.orbittrack)
        self.organization = organization.OrganizationResourceWithRawResponse(client.organization)
        self.organizationdetails = organizationdetails.OrganizationdetailsResourceWithRawResponse(
            client.organizationdetails
        )
        self.passiveradarobservation = passiveradarobservation.PassiveradarobservationResourceWithRawResponse(
            client.passiveradarobservation
        )
        self.personnelrecovery = personnelrecovery.PersonnelrecoveryResourceWithRawResponse(client.personnelrecovery)
        self.poi = poi.PoiResourceWithRawResponse(client.poi)
        self.port = port.PortResourceWithRawResponse(client.port)
        self.radarobservation = radarobservation.RadarobservationResourceWithRawResponse(client.radarobservation)
        self.rfband = rfband.RfbandResourceWithRawResponse(client.rfband)
        self.rfbandtype = rfbandtype.RfbandtypeResourceWithRawResponse(client.rfbandtype)
        self.rfemitter = rfemitter.RfemitterResourceWithRawResponse(client.rfemitter)
        self.rfemitterdetails = rfemitterdetails.RfemitterdetailsResourceWithRawResponse(client.rfemitterdetails)
        self.rfobservation = rfobservation.RfobservationResourceWithRawResponse(client.rfobservation)
        self.sarobservation = sarobservation.SarobservationResourceWithRawResponse(client.sarobservation)
        self.scientific = scientific.ScientificResourceWithRawResponse(client.scientific)
        self.sensor = sensor.SensorResourceWithRawResponse(client.sensor)
        self.sensormaintenance = sensormaintenance.SensormaintenanceResourceWithRawResponse(client.sensormaintenance)
        self.sensorobservationtype = sensorobservationtype.SensorobservationtypeResourceWithRawResponse(
            client.sensorobservationtype
        )
        self.sensorplan = sensorplan.SensorplanResourceWithRawResponse(client.sensorplan)
        self.sensortype = sensortype.SensortypeResourceWithRawResponse(client.sensortype)
        self.seradatacommdetails = seradatacommdetails.SeradatacommdetailsResourceWithRawResponse(
            client.seradatacommdetails
        )
        self.seradataearlywarning = seradataearlywarning.SeradataearlywarningResourceWithRawResponse(
            client.seradataearlywarning
        )
        self.seradatanavigation = seradatanavigation.SeradatanavigationResourceWithRawResponse(
            client.seradatanavigation
        )
        self.seradataopticalpayload = seradataopticalpayload.SeradataopticalpayloadResourceWithRawResponse(
            client.seradataopticalpayload
        )
        self.seradataradarpayload = seradataradarpayload.SeradataradarpayloadResourceWithRawResponse(
            client.seradataradarpayload
        )
        self.seradatasigintpayload = seradatasigintpayload.SeradatasigintpayloadResourceWithRawResponse(
            client.seradatasigintpayload
        )
        self.seradataspacecraftdetails = seradataspacecraftdetails.SeradataspacecraftdetailsResourceWithRawResponse(
            client.seradataspacecraftdetails
        )
        self.sgi = sgi.SgiResourceWithRawResponse(client.sgi)
        self.sigact = sigact.SigactResourceWithRawResponse(client.sigact)
        self.site = site.SiteResourceWithRawResponse(client.site)
        self.siteremark = siteremark.SiteremarkResourceWithRawResponse(client.siteremark)
        self.sitestatus = sitestatus.SitestatusResourceWithRawResponse(client.sitestatus)
        self.skyimagery = skyimagery.SkyimageryResourceWithRawResponse(client.skyimagery)
        self.soiobservationset = soiobservationset.SoiobservationsetResourceWithRawResponse(client.soiobservationset)
        self.solararray = solararray.SolararrayResourceWithRawResponse(client.solararray)
        self.solararraydetails = solararraydetails.SolararraydetailsResourceWithRawResponse(client.solararraydetails)
        self.sortieppr = sortieppr.SortiepprResourceWithRawResponse(client.sortieppr)
        self.spaceenvobservation = spaceenvobservation.SpaceenvobservationResourceWithRawResponse(
            client.spaceenvobservation
        )
        self.stage = stage.StageResourceWithRawResponse(client.stage)
        self.starcatalog = starcatalog.StarcatalogResourceWithRawResponse(client.starcatalog)
        self.statevector = statevector.StatevectorResourceWithRawResponse(client.statevector)
        self.status = status.StatusResourceWithRawResponse(client.status)
        self.substatus = substatus.SubstatusResourceWithRawResponse(client.substatus)
        self.supporting_data = supporting_data.SupportingDataResourceWithRawResponse(client.supporting_data)
        self.surface = surface.SurfaceResourceWithRawResponse(client.surface)
        self.surfaceobstruction = surfaceobstruction.SurfaceobstructionResourceWithRawResponse(
            client.surfaceobstruction
        )
        self.swir = swir.SwirResourceWithRawResponse(client.swir)
        self.taiutc = taiutc.TaiutcResourceWithRawResponse(client.taiutc)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResourceWithRawResponse(client.tdoa_fdoa)
        self.track = track.TrackResourceWithRawResponse(client.track)
        self.trackdetails = trackdetails.TrackdetailsResourceWithRawResponse(client.trackdetails)
        self.trackroute = trackroute.TrackrouteResourceWithRawResponse(client.trackroute)
        self.transponder = transponder.TransponderResourceWithRawResponse(client.transponder)
        self.vessel = vessel.VesselResourceWithRawResponse(client.vessel)
        self.video = video.VideoResourceWithRawResponse(client.video)
        self.weatherdata = weatherdata.WeatherdataResourceWithRawResponse(client.weatherdata)
        self.weatherreport = weatherreport.WeatherreportResourceWithRawResponse(client.weatherreport)
        self.udl = udl.UdlResourceWithRawResponse(client.udl)
        self.gnss_observations = gnss_observations.GnssObservationsResourceWithRawResponse(client.gnss_observations)
        self.gnss_raw_if = gnss_raw_if.GnssRawIfResourceWithRawResponse(client.gnss_raw_if)
        self.iono_observation = iono_observation.IonoObservationResourceWithRawResponse(client.iono_observation)
        self.launch_event = launch_event.LaunchEventResourceWithRawResponse(client.launch_event)
        self.report_and_activity = report_and_activity.ReportAndActivityResourceWithRawResponse(
            client.report_and_activity
        )
        self.secure_messaging = secure_messaging.SecureMessagingResourceWithRawResponse(client.secure_messaging)
        self.scs = scs.ScsResourceWithRawResponse(client.scs)
        self.scs_views = scs_views.ScsViewsResourceWithRawResponse(client.scs_views)


class AsyncUnifieddatalibraryWithRawResponse:
    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self.air_events = air_events.AsyncAirEventsResourceWithRawResponse(client.air_events)
        self.air_load_plans = air_load_plans.AsyncAirLoadPlansResourceWithRawResponse(client.air_load_plans)
        self.air_operations = air_operations.AsyncAirOperationsResourceWithRawResponse(client.air_operations)
        self.air_tasking_orders = air_tasking_orders.AsyncAirTaskingOrdersResourceWithRawResponse(
            client.air_tasking_orders
        )
        self.air_transport_missions = air_transport_missions.AsyncAirTransportMissionsResourceWithRawResponse(
            client.air_transport_missions
        )
        self.aircraft = aircraft.AsyncAircraftResourceWithRawResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AsyncAircraftSortiesResourceWithRawResponse(client.aircraft_sorties)
        self.aircraft_status_remarks = aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithRawResponse(
            client.aircraft_status_remarks
        )
        self.aircraft_statuses = aircraft_statuses.AsyncAircraftStatusesResourceWithRawResponse(
            client.aircraft_statuses
        )
        self.aircraftstatusremark = aircraftstatusremark.AsyncAircraftstatusremarkResourceWithRawResponse(
            client.aircraftstatusremark
        )
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResourceWithRawResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResourceWithRawResponse(client.airfield_status)
        self.airfields = airfields.AsyncAirfieldsResourceWithRawResponse(client.airfields)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResourceWithRawResponse(
            client.airfieldslotconsumptions
        )
        self.airfieldslots = airfieldslots.AsyncAirfieldslotsResourceWithRawResponse(client.airfieldslots)
        self.airfieldstatus = airfieldstatus.AsyncAirfieldstatusResourceWithRawResponse(client.airfieldstatus)
        self.airloadplans = airloadplans.AsyncAirloadplansResourceWithRawResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResourceWithRawResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AsyncAirtaskingordersResourceWithRawResponse(client.airtaskingorders)
        self.ais = ais.AsyncAIsResourceWithRawResponse(client.ais)
        self.ais_objects = ais_objects.AsyncAIsObjectsResourceWithRawResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResourceWithRawResponse(client.analytic_imagery)
        self.antennas = antennas.AsyncAntennasResourceWithRawResponse(client.antennas)
        self.attitude_data = attitude_data.AsyncAttitudeDataResourceWithRawResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResourceWithRawResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AsyncAttitudesetsResourceWithRawResponse(client.attitudesets)
        self.batteries = batteries.AsyncBatteriesResourceWithRawResponse(client.batteries)
        self.batterydetails = batterydetails.AsyncBatterydetailsResourceWithRawResponse(client.batterydetails)
        self.beam = beam.AsyncBeamResourceWithRawResponse(client.beam)
        self.beam_contours = beam_contours.AsyncBeamContoursResourceWithRawResponse(client.beam_contours)
        self.buses = buses.AsyncBusesResourceWithRawResponse(client.buses)
        self.channels = channels.AsyncChannelsResourceWithRawResponse(client.channels)
        self.collect_requests = collect_requests.AsyncCollectRequestsResourceWithRawResponse(client.collect_requests)
        self.collect_responses = collect_responses.AsyncCollectResponsesResourceWithRawResponse(
            client.collect_responses
        )
        self.comm = comm.AsyncCommResourceWithRawResponse(client.comm)
        self.conjunctions = conjunctions.AsyncConjunctionsResourceWithRawResponse(client.conjunctions)
        self.cots = cots.AsyncCotsResourceWithRawResponse(client.cots)
        self.aviationriskmanagement = aviationriskmanagement.AsyncAviationriskmanagementResourceWithRawResponse(
            client.aviationriskmanagement
        )
        self.dropzone = dropzone.AsyncDropzoneResourceWithRawResponse(client.dropzone)
        self.emittergeolocation = emittergeolocation.AsyncEmittergeolocationResourceWithRawResponse(
            client.emittergeolocation
        )
        self.featureassessment = featureassessment.AsyncFeatureassessmentResourceWithRawResponse(
            client.featureassessment
        )
        self.globalatmosphericmodel = globalatmosphericmodel.AsyncGlobalatmosphericmodelResourceWithRawResponse(
            client.globalatmosphericmodel
        )
        self.routestats = routestats.AsyncRoutestatsResourceWithRawResponse(client.routestats)
        self.countries = countries.AsyncCountriesResourceWithRawResponse(client.countries)
        self.crew = crew.AsyncCrewResourceWithRawResponse(client.crew)
        self.diffofarrival = diffofarrival.AsyncDiffofarrivalResourceWithRawResponse(client.diffofarrival)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResourceWithRawResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.AsyncDriftHistoryResourceWithRawResponse(client.drift_history)
        self.ecpsdr = ecpsdr.AsyncEcpsdrResourceWithRawResponse(client.ecpsdr)
        self.effect_requests = effect_requests.AsyncEffectRequestsResourceWithRawResponse(client.effect_requests)
        self.effect_responses = effect_responses.AsyncEffectResponsesResourceWithRawResponse(client.effect_responses)
        self.elsets = elsets.AsyncElsetsResourceWithRawResponse(client.elsets)
        self.engine_details = engine_details.AsyncEngineDetailsResourceWithRawResponse(client.engine_details)
        self.enginedetails = enginedetails.AsyncEnginedetailsResourceWithRawResponse(client.enginedetails)
        self.engines = engines.AsyncEnginesResourceWithRawResponse(client.engines)
        self.entities = entities.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.eo_observations = eo_observations.AsyncEoObservationsResourceWithRawResponse(client.eo_observations)
        self.eoobservations = eoobservations.AsyncEoobservationsResourceWithRawResponse(client.eoobservations)
        self.eop = eop.AsyncEopResourceWithRawResponse(client.eop)
        self.ephemeris = ephemeris.AsyncEphemerisResourceWithRawResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResourceWithRawResponse(client.ephemeris_sets)
        self.equipment = equipment.AsyncEquipmentResourceWithRawResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.AsyncEquipmentremarksResourceWithRawResponse(client.equipmentremarks)
        self.evac = evac.AsyncEvacResourceWithRawResponse(client.evac)
        self.event_evolution = event_evolution.AsyncEventEvolutionResourceWithRawResponse(client.event_evolution)
        self.flightplan = flightplan.AsyncFlightplanResourceWithRawResponse(client.flightplan)
        self.geostatus = geostatus.AsyncGeostatusResourceWithRawResponse(client.geostatus)
        self.gnssobservationset = gnssobservationset.AsyncGnssobservationsetResourceWithRawResponse(
            client.gnssobservationset
        )
        self.gnssrawif = gnssrawif.AsyncGnssrawifResourceWithRawResponse(client.gnssrawif)
        self.ground_imagery = ground_imagery.AsyncGroundImageryResourceWithRawResponse(client.ground_imagery)
        self.groundimagery = groundimagery.AsyncGroundimageryResourceWithRawResponse(client.groundimagery)
        self.h3geo = h3geo.AsyncH3geoResourceWithRawResponse(client.h3geo)
        self.h3geohexcell = h3geohexcell.AsyncH3geohexcellResourceWithRawResponse(client.h3geohexcell)
        self.hazard = hazard.AsyncHazardResourceWithRawResponse(client.hazard)
        self.ionoobservation = ionoobservation.AsyncIonoobservationResourceWithRawResponse(client.ionoobservation)
        self.ir = ir.AsyncIrResourceWithRawResponse(client.ir)
        self.isr_collections = isr_collections.AsyncIsrCollectionsResourceWithRawResponse(client.isr_collections)
        self.item = item.AsyncItemResourceWithRawResponse(client.item)
        self.item_trackings = item_trackings.AsyncItemTrackingsResourceWithRawResponse(client.item_trackings)
        self.launchdetection = launchdetection.AsyncLaunchdetectionResourceWithRawResponse(client.launchdetection)
        self.launchevent = launchevent.AsyncLauncheventResourceWithRawResponse(client.launchevent)
        self.launchsite = launchsite.AsyncLaunchsiteResourceWithRawResponse(client.launchsite)
        self.launchsitedetails = launchsitedetails.AsyncLaunchsitedetailsResourceWithRawResponse(
            client.launchsitedetails
        )
        self.launchvehicle = launchvehicle.AsyncLaunchvehicleResourceWithRawResponse(client.launchvehicle)
        self.launchvehicledetails = launchvehicledetails.AsyncLaunchvehicledetailsResourceWithRawResponse(
            client.launchvehicledetails
        )
        self.link_status = link_status.AsyncLinkStatusResourceWithRawResponse(client.link_status)
        self.location = location.AsyncLocationResourceWithRawResponse(client.location)
        self.logisticssupport = logisticssupport.AsyncLogisticssupportResourceWithRawResponse(client.logisticssupport)
        self.maneuvers = maneuvers.AsyncManeuversResourceWithRawResponse(client.maneuvers)
        self.manifold = manifold.AsyncManifoldResourceWithRawResponse(client.manifold)
        self.manifoldelset = manifoldelset.AsyncManifoldelsetResourceWithRawResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResourceWithRawResponse(client.missile_tracks)
        self.missionassignment = missionassignment.AsyncMissionassignmentResourceWithRawResponse(
            client.missionassignment
        )
        self.monoradar = monoradar.AsyncMonoradarResourceWithRawResponse(client.monoradar)
        self.mti = mti.AsyncMtiResourceWithRawResponse(client.mti)
        self.navigation = navigation.AsyncNavigationResourceWithRawResponse(client.navigation)
        self.navigationalobstruction = navigationalobstruction.AsyncNavigationalobstructionResourceWithRawResponse(
            client.navigationalobstruction
        )
        self.notification = notification.AsyncNotificationResourceWithRawResponse(client.notification)
        self.objectofinterest = objectofinterest.AsyncObjectofinterestResourceWithRawResponse(client.objectofinterest)
        self.observations = observations.AsyncObservationsResourceWithRawResponse(client.observations)
        self.onboardnavigation = onboardnavigation.AsyncOnboardnavigationResourceWithRawResponse(
            client.onboardnavigation
        )
        self.onorbit = onorbit.AsyncOnorbitResourceWithRawResponse(client.onorbit)
        self.onorbitantenna = onorbitantenna.AsyncOnorbitantennaResourceWithRawResponse(client.onorbitantenna)
        self.onorbitbattery = onorbitbattery.AsyncOnorbitbatteryResourceWithRawResponse(client.onorbitbattery)
        self.onorbitdetails = onorbitdetails.AsyncOnorbitdetailsResourceWithRawResponse(client.onorbitdetails)
        self.onorbitevent = onorbitevent.AsyncOnorbiteventResourceWithRawResponse(client.onorbitevent)
        self.onorbitlist = onorbitlist.AsyncOnorbitlistResourceWithRawResponse(client.onorbitlist)
        self.onorbitsolararray = onorbitsolararray.AsyncOnorbitsolararrayResourceWithRawResponse(
            client.onorbitsolararray
        )
        self.onorbitthruster = onorbitthruster.AsyncOnorbitthrusterResourceWithRawResponse(client.onorbitthruster)
        self.onorbitthrusterstatus = onorbitthrusterstatus.AsyncOnorbitthrusterstatusResourceWithRawResponse(
            client.onorbitthrusterstatus
        )
        self.operatingunit = operatingunit.AsyncOperatingunitResourceWithRawResponse(client.operatingunit)
        self.operatingunitremark = operatingunitremark.AsyncOperatingunitremarkResourceWithRawResponse(
            client.operatingunitremark
        )
        self.orbitdetermination = orbitdetermination.AsyncOrbitdeterminationResourceWithRawResponse(
            client.orbitdetermination
        )
        self.orbittrack = orbittrack.AsyncOrbittrackResourceWithRawResponse(client.orbittrack)
        self.organization = organization.AsyncOrganizationResourceWithRawResponse(client.organization)
        self.organizationdetails = organizationdetails.AsyncOrganizationdetailsResourceWithRawResponse(
            client.organizationdetails
        )
        self.passiveradarobservation = passiveradarobservation.AsyncPassiveradarobservationResourceWithRawResponse(
            client.passiveradarobservation
        )
        self.personnelrecovery = personnelrecovery.AsyncPersonnelrecoveryResourceWithRawResponse(
            client.personnelrecovery
        )
        self.poi = poi.AsyncPoiResourceWithRawResponse(client.poi)
        self.port = port.AsyncPortResourceWithRawResponse(client.port)
        self.radarobservation = radarobservation.AsyncRadarobservationResourceWithRawResponse(client.radarobservation)
        self.rfband = rfband.AsyncRfbandResourceWithRawResponse(client.rfband)
        self.rfbandtype = rfbandtype.AsyncRfbandtypeResourceWithRawResponse(client.rfbandtype)
        self.rfemitter = rfemitter.AsyncRfemitterResourceWithRawResponse(client.rfemitter)
        self.rfemitterdetails = rfemitterdetails.AsyncRfemitterdetailsResourceWithRawResponse(client.rfemitterdetails)
        self.rfobservation = rfobservation.AsyncRfobservationResourceWithRawResponse(client.rfobservation)
        self.sarobservation = sarobservation.AsyncSarobservationResourceWithRawResponse(client.sarobservation)
        self.scientific = scientific.AsyncScientificResourceWithRawResponse(client.scientific)
        self.sensor = sensor.AsyncSensorResourceWithRawResponse(client.sensor)
        self.sensormaintenance = sensormaintenance.AsyncSensormaintenanceResourceWithRawResponse(
            client.sensormaintenance
        )
        self.sensorobservationtype = sensorobservationtype.AsyncSensorobservationtypeResourceWithRawResponse(
            client.sensorobservationtype
        )
        self.sensorplan = sensorplan.AsyncSensorplanResourceWithRawResponse(client.sensorplan)
        self.sensortype = sensortype.AsyncSensortypeResourceWithRawResponse(client.sensortype)
        self.seradatacommdetails = seradatacommdetails.AsyncSeradatacommdetailsResourceWithRawResponse(
            client.seradatacommdetails
        )
        self.seradataearlywarning = seradataearlywarning.AsyncSeradataearlywarningResourceWithRawResponse(
            client.seradataearlywarning
        )
        self.seradatanavigation = seradatanavigation.AsyncSeradatanavigationResourceWithRawResponse(
            client.seradatanavigation
        )
        self.seradataopticalpayload = seradataopticalpayload.AsyncSeradataopticalpayloadResourceWithRawResponse(
            client.seradataopticalpayload
        )
        self.seradataradarpayload = seradataradarpayload.AsyncSeradataradarpayloadResourceWithRawResponse(
            client.seradataradarpayload
        )
        self.seradatasigintpayload = seradatasigintpayload.AsyncSeradatasigintpayloadResourceWithRawResponse(
            client.seradatasigintpayload
        )
        self.seradataspacecraftdetails = (
            seradataspacecraftdetails.AsyncSeradataspacecraftdetailsResourceWithRawResponse(
                client.seradataspacecraftdetails
            )
        )
        self.sgi = sgi.AsyncSgiResourceWithRawResponse(client.sgi)
        self.sigact = sigact.AsyncSigactResourceWithRawResponse(client.sigact)
        self.site = site.AsyncSiteResourceWithRawResponse(client.site)
        self.siteremark = siteremark.AsyncSiteremarkResourceWithRawResponse(client.siteremark)
        self.sitestatus = sitestatus.AsyncSitestatusResourceWithRawResponse(client.sitestatus)
        self.skyimagery = skyimagery.AsyncSkyimageryResourceWithRawResponse(client.skyimagery)
        self.soiobservationset = soiobservationset.AsyncSoiobservationsetResourceWithRawResponse(
            client.soiobservationset
        )
        self.solararray = solararray.AsyncSolararrayResourceWithRawResponse(client.solararray)
        self.solararraydetails = solararraydetails.AsyncSolararraydetailsResourceWithRawResponse(
            client.solararraydetails
        )
        self.sortieppr = sortieppr.AsyncSortiepprResourceWithRawResponse(client.sortieppr)
        self.spaceenvobservation = spaceenvobservation.AsyncSpaceenvobservationResourceWithRawResponse(
            client.spaceenvobservation
        )
        self.stage = stage.AsyncStageResourceWithRawResponse(client.stage)
        self.starcatalog = starcatalog.AsyncStarcatalogResourceWithRawResponse(client.starcatalog)
        self.statevector = statevector.AsyncStatevectorResourceWithRawResponse(client.statevector)
        self.status = status.AsyncStatusResourceWithRawResponse(client.status)
        self.substatus = substatus.AsyncSubstatusResourceWithRawResponse(client.substatus)
        self.supporting_data = supporting_data.AsyncSupportingDataResourceWithRawResponse(client.supporting_data)
        self.surface = surface.AsyncSurfaceResourceWithRawResponse(client.surface)
        self.surfaceobstruction = surfaceobstruction.AsyncSurfaceobstructionResourceWithRawResponse(
            client.surfaceobstruction
        )
        self.swir = swir.AsyncSwirResourceWithRawResponse(client.swir)
        self.taiutc = taiutc.AsyncTaiutcResourceWithRawResponse(client.taiutc)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResourceWithRawResponse(client.tdoa_fdoa)
        self.track = track.AsyncTrackResourceWithRawResponse(client.track)
        self.trackdetails = trackdetails.AsyncTrackdetailsResourceWithRawResponse(client.trackdetails)
        self.trackroute = trackroute.AsyncTrackrouteResourceWithRawResponse(client.trackroute)
        self.transponder = transponder.AsyncTransponderResourceWithRawResponse(client.transponder)
        self.vessel = vessel.AsyncVesselResourceWithRawResponse(client.vessel)
        self.video = video.AsyncVideoResourceWithRawResponse(client.video)
        self.weatherdata = weatherdata.AsyncWeatherdataResourceWithRawResponse(client.weatherdata)
        self.weatherreport = weatherreport.AsyncWeatherreportResourceWithRawResponse(client.weatherreport)
        self.udl = udl.AsyncUdlResourceWithRawResponse(client.udl)
        self.gnss_observations = gnss_observations.AsyncGnssObservationsResourceWithRawResponse(
            client.gnss_observations
        )
        self.gnss_raw_if = gnss_raw_if.AsyncGnssRawIfResourceWithRawResponse(client.gnss_raw_if)
        self.iono_observation = iono_observation.AsyncIonoObservationResourceWithRawResponse(client.iono_observation)
        self.launch_event = launch_event.AsyncLaunchEventResourceWithRawResponse(client.launch_event)
        self.report_and_activity = report_and_activity.AsyncReportAndActivityResourceWithRawResponse(
            client.report_and_activity
        )
        self.secure_messaging = secure_messaging.AsyncSecureMessagingResourceWithRawResponse(client.secure_messaging)
        self.scs = scs.AsyncScsResourceWithRawResponse(client.scs)
        self.scs_views = scs_views.AsyncScsViewsResourceWithRawResponse(client.scs_views)


class UnifieddatalibraryWithStreamedResponse:
    def __init__(self, client: Unifieddatalibrary) -> None:
        self.air_events = air_events.AirEventsResourceWithStreamingResponse(client.air_events)
        self.air_load_plans = air_load_plans.AirLoadPlansResourceWithStreamingResponse(client.air_load_plans)
        self.air_operations = air_operations.AirOperationsResourceWithStreamingResponse(client.air_operations)
        self.air_tasking_orders = air_tasking_orders.AirTaskingOrdersResourceWithStreamingResponse(
            client.air_tasking_orders
        )
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResourceWithStreamingResponse(
            client.air_transport_missions
        )
        self.aircraft = aircraft.AircraftResourceWithStreamingResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResourceWithStreamingResponse(client.aircraft_sorties)
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResourceWithStreamingResponse(
            client.aircraft_status_remarks
        )
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResourceWithStreamingResponse(
            client.aircraft_statuses
        )
        self.aircraftstatusremark = aircraftstatusremark.AircraftstatusremarkResourceWithStreamingResponse(
            client.aircraftstatusremark
        )
        self.airfield_slots = airfield_slots.AirfieldSlotsResourceWithStreamingResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AirfieldStatusResourceWithStreamingResponse(client.airfield_status)
        self.airfields = airfields.AirfieldsResourceWithStreamingResponse(client.airfields)
        self.airfieldslotconsumptions = airfieldslotconsumptions.AirfieldslotconsumptionsResourceWithStreamingResponse(
            client.airfieldslotconsumptions
        )
        self.airfieldslots = airfieldslots.AirfieldslotsResourceWithStreamingResponse(client.airfieldslots)
        self.airfieldstatus = airfieldstatus.AirfieldstatusResourceWithStreamingResponse(client.airfieldstatus)
        self.airloadplans = airloadplans.AirloadplansResourceWithStreamingResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResourceWithStreamingResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AirtaskingordersResourceWithStreamingResponse(client.airtaskingorders)
        self.ais = ais.AIsResourceWithStreamingResponse(client.ais)
        self.ais_objects = ais_objects.AIsObjectsResourceWithStreamingResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResourceWithStreamingResponse(client.analytic_imagery)
        self.antennas = antennas.AntennasResourceWithStreamingResponse(client.antennas)
        self.attitude_data = attitude_data.AttitudeDataResourceWithStreamingResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AttitudeSetsResourceWithStreamingResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AttitudesetsResourceWithStreamingResponse(client.attitudesets)
        self.batteries = batteries.BatteriesResourceWithStreamingResponse(client.batteries)
        self.batterydetails = batterydetails.BatterydetailsResourceWithStreamingResponse(client.batterydetails)
        self.beam = beam.BeamResourceWithStreamingResponse(client.beam)
        self.beam_contours = beam_contours.BeamContoursResourceWithStreamingResponse(client.beam_contours)
        self.buses = buses.BusesResourceWithStreamingResponse(client.buses)
        self.channels = channels.ChannelsResourceWithStreamingResponse(client.channels)
        self.collect_requests = collect_requests.CollectRequestsResourceWithStreamingResponse(client.collect_requests)
        self.collect_responses = collect_responses.CollectResponsesResourceWithStreamingResponse(
            client.collect_responses
        )
        self.comm = comm.CommResourceWithStreamingResponse(client.comm)
        self.conjunctions = conjunctions.ConjunctionsResourceWithStreamingResponse(client.conjunctions)
        self.cots = cots.CotsResourceWithStreamingResponse(client.cots)
        self.aviationriskmanagement = aviationriskmanagement.AviationriskmanagementResourceWithStreamingResponse(
            client.aviationriskmanagement
        )
        self.dropzone = dropzone.DropzoneResourceWithStreamingResponse(client.dropzone)
        self.emittergeolocation = emittergeolocation.EmittergeolocationResourceWithStreamingResponse(
            client.emittergeolocation
        )
        self.featureassessment = featureassessment.FeatureassessmentResourceWithStreamingResponse(
            client.featureassessment
        )
        self.globalatmosphericmodel = globalatmosphericmodel.GlobalatmosphericmodelResourceWithStreamingResponse(
            client.globalatmosphericmodel
        )
        self.routestats = routestats.RoutestatsResourceWithStreamingResponse(client.routestats)
        self.countries = countries.CountriesResourceWithStreamingResponse(client.countries)
        self.crew = crew.CrewResourceWithStreamingResponse(client.crew)
        self.diffofarrival = diffofarrival.DiffofarrivalResourceWithStreamingResponse(client.diffofarrival)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResourceWithStreamingResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.DriftHistoryResourceWithStreamingResponse(client.drift_history)
        self.ecpsdr = ecpsdr.EcpsdrResourceWithStreamingResponse(client.ecpsdr)
        self.effect_requests = effect_requests.EffectRequestsResourceWithStreamingResponse(client.effect_requests)
        self.effect_responses = effect_responses.EffectResponsesResourceWithStreamingResponse(client.effect_responses)
        self.elsets = elsets.ElsetsResourceWithStreamingResponse(client.elsets)
        self.engine_details = engine_details.EngineDetailsResourceWithStreamingResponse(client.engine_details)
        self.enginedetails = enginedetails.EnginedetailsResourceWithStreamingResponse(client.enginedetails)
        self.engines = engines.EnginesResourceWithStreamingResponse(client.engines)
        self.entities = entities.EntitiesResourceWithStreamingResponse(client.entities)
        self.eo_observations = eo_observations.EoObservationsResourceWithStreamingResponse(client.eo_observations)
        self.eoobservations = eoobservations.EoobservationsResourceWithStreamingResponse(client.eoobservations)
        self.eop = eop.EopResourceWithStreamingResponse(client.eop)
        self.ephemeris = ephemeris.EphemerisResourceWithStreamingResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResourceWithStreamingResponse(client.ephemeris_sets)
        self.equipment = equipment.EquipmentResourceWithStreamingResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.EquipmentremarksResourceWithStreamingResponse(client.equipmentremarks)
        self.evac = evac.EvacResourceWithStreamingResponse(client.evac)
        self.event_evolution = event_evolution.EventEvolutionResourceWithStreamingResponse(client.event_evolution)
        self.flightplan = flightplan.FlightplanResourceWithStreamingResponse(client.flightplan)
        self.geostatus = geostatus.GeostatusResourceWithStreamingResponse(client.geostatus)
        self.gnssobservationset = gnssobservationset.GnssobservationsetResourceWithStreamingResponse(
            client.gnssobservationset
        )
        self.gnssrawif = gnssrawif.GnssrawifResourceWithStreamingResponse(client.gnssrawif)
        self.ground_imagery = ground_imagery.GroundImageryResourceWithStreamingResponse(client.ground_imagery)
        self.groundimagery = groundimagery.GroundimageryResourceWithStreamingResponse(client.groundimagery)
        self.h3geo = h3geo.H3geoResourceWithStreamingResponse(client.h3geo)
        self.h3geohexcell = h3geohexcell.H3geohexcellResourceWithStreamingResponse(client.h3geohexcell)
        self.hazard = hazard.HazardResourceWithStreamingResponse(client.hazard)
        self.ionoobservation = ionoobservation.IonoobservationResourceWithStreamingResponse(client.ionoobservation)
        self.ir = ir.IrResourceWithStreamingResponse(client.ir)
        self.isr_collections = isr_collections.IsrCollectionsResourceWithStreamingResponse(client.isr_collections)
        self.item = item.ItemResourceWithStreamingResponse(client.item)
        self.item_trackings = item_trackings.ItemTrackingsResourceWithStreamingResponse(client.item_trackings)
        self.launchdetection = launchdetection.LaunchdetectionResourceWithStreamingResponse(client.launchdetection)
        self.launchevent = launchevent.LauncheventResourceWithStreamingResponse(client.launchevent)
        self.launchsite = launchsite.LaunchsiteResourceWithStreamingResponse(client.launchsite)
        self.launchsitedetails = launchsitedetails.LaunchsitedetailsResourceWithStreamingResponse(
            client.launchsitedetails
        )
        self.launchvehicle = launchvehicle.LaunchvehicleResourceWithStreamingResponse(client.launchvehicle)
        self.launchvehicledetails = launchvehicledetails.LaunchvehicledetailsResourceWithStreamingResponse(
            client.launchvehicledetails
        )
        self.link_status = link_status.LinkStatusResourceWithStreamingResponse(client.link_status)
        self.location = location.LocationResourceWithStreamingResponse(client.location)
        self.logisticssupport = logisticssupport.LogisticssupportResourceWithStreamingResponse(client.logisticssupport)
        self.maneuvers = maneuvers.ManeuversResourceWithStreamingResponse(client.maneuvers)
        self.manifold = manifold.ManifoldResourceWithStreamingResponse(client.manifold)
        self.manifoldelset = manifoldelset.ManifoldelsetResourceWithStreamingResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.MissileTracksResourceWithStreamingResponse(client.missile_tracks)
        self.missionassignment = missionassignment.MissionassignmentResourceWithStreamingResponse(
            client.missionassignment
        )
        self.monoradar = monoradar.MonoradarResourceWithStreamingResponse(client.monoradar)
        self.mti = mti.MtiResourceWithStreamingResponse(client.mti)
        self.navigation = navigation.NavigationResourceWithStreamingResponse(client.navigation)
        self.navigationalobstruction = navigationalobstruction.NavigationalobstructionResourceWithStreamingResponse(
            client.navigationalobstruction
        )
        self.notification = notification.NotificationResourceWithStreamingResponse(client.notification)
        self.objectofinterest = objectofinterest.ObjectofinterestResourceWithStreamingResponse(client.objectofinterest)
        self.observations = observations.ObservationsResourceWithStreamingResponse(client.observations)
        self.onboardnavigation = onboardnavigation.OnboardnavigationResourceWithStreamingResponse(
            client.onboardnavigation
        )
        self.onorbit = onorbit.OnorbitResourceWithStreamingResponse(client.onorbit)
        self.onorbitantenna = onorbitantenna.OnorbitantennaResourceWithStreamingResponse(client.onorbitantenna)
        self.onorbitbattery = onorbitbattery.OnorbitbatteryResourceWithStreamingResponse(client.onorbitbattery)
        self.onorbitdetails = onorbitdetails.OnorbitdetailsResourceWithStreamingResponse(client.onorbitdetails)
        self.onorbitevent = onorbitevent.OnorbiteventResourceWithStreamingResponse(client.onorbitevent)
        self.onorbitlist = onorbitlist.OnorbitlistResourceWithStreamingResponse(client.onorbitlist)
        self.onorbitsolararray = onorbitsolararray.OnorbitsolararrayResourceWithStreamingResponse(
            client.onorbitsolararray
        )
        self.onorbitthruster = onorbitthruster.OnorbitthrusterResourceWithStreamingResponse(client.onorbitthruster)
        self.onorbitthrusterstatus = onorbitthrusterstatus.OnorbitthrusterstatusResourceWithStreamingResponse(
            client.onorbitthrusterstatus
        )
        self.operatingunit = operatingunit.OperatingunitResourceWithStreamingResponse(client.operatingunit)
        self.operatingunitremark = operatingunitremark.OperatingunitremarkResourceWithStreamingResponse(
            client.operatingunitremark
        )
        self.orbitdetermination = orbitdetermination.OrbitdeterminationResourceWithStreamingResponse(
            client.orbitdetermination
        )
        self.orbittrack = orbittrack.OrbittrackResourceWithStreamingResponse(client.orbittrack)
        self.organization = organization.OrganizationResourceWithStreamingResponse(client.organization)
        self.organizationdetails = organizationdetails.OrganizationdetailsResourceWithStreamingResponse(
            client.organizationdetails
        )
        self.passiveradarobservation = passiveradarobservation.PassiveradarobservationResourceWithStreamingResponse(
            client.passiveradarobservation
        )
        self.personnelrecovery = personnelrecovery.PersonnelrecoveryResourceWithStreamingResponse(
            client.personnelrecovery
        )
        self.poi = poi.PoiResourceWithStreamingResponse(client.poi)
        self.port = port.PortResourceWithStreamingResponse(client.port)
        self.radarobservation = radarobservation.RadarobservationResourceWithStreamingResponse(client.radarobservation)
        self.rfband = rfband.RfbandResourceWithStreamingResponse(client.rfband)
        self.rfbandtype = rfbandtype.RfbandtypeResourceWithStreamingResponse(client.rfbandtype)
        self.rfemitter = rfemitter.RfemitterResourceWithStreamingResponse(client.rfemitter)
        self.rfemitterdetails = rfemitterdetails.RfemitterdetailsResourceWithStreamingResponse(client.rfemitterdetails)
        self.rfobservation = rfobservation.RfobservationResourceWithStreamingResponse(client.rfobservation)
        self.sarobservation = sarobservation.SarobservationResourceWithStreamingResponse(client.sarobservation)
        self.scientific = scientific.ScientificResourceWithStreamingResponse(client.scientific)
        self.sensor = sensor.SensorResourceWithStreamingResponse(client.sensor)
        self.sensormaintenance = sensormaintenance.SensormaintenanceResourceWithStreamingResponse(
            client.sensormaintenance
        )
        self.sensorobservationtype = sensorobservationtype.SensorobservationtypeResourceWithStreamingResponse(
            client.sensorobservationtype
        )
        self.sensorplan = sensorplan.SensorplanResourceWithStreamingResponse(client.sensorplan)
        self.sensortype = sensortype.SensortypeResourceWithStreamingResponse(client.sensortype)
        self.seradatacommdetails = seradatacommdetails.SeradatacommdetailsResourceWithStreamingResponse(
            client.seradatacommdetails
        )
        self.seradataearlywarning = seradataearlywarning.SeradataearlywarningResourceWithStreamingResponse(
            client.seradataearlywarning
        )
        self.seradatanavigation = seradatanavigation.SeradatanavigationResourceWithStreamingResponse(
            client.seradatanavigation
        )
        self.seradataopticalpayload = seradataopticalpayload.SeradataopticalpayloadResourceWithStreamingResponse(
            client.seradataopticalpayload
        )
        self.seradataradarpayload = seradataradarpayload.SeradataradarpayloadResourceWithStreamingResponse(
            client.seradataradarpayload
        )
        self.seradatasigintpayload = seradatasigintpayload.SeradatasigintpayloadResourceWithStreamingResponse(
            client.seradatasigintpayload
        )
        self.seradataspacecraftdetails = (
            seradataspacecraftdetails.SeradataspacecraftdetailsResourceWithStreamingResponse(
                client.seradataspacecraftdetails
            )
        )
        self.sgi = sgi.SgiResourceWithStreamingResponse(client.sgi)
        self.sigact = sigact.SigactResourceWithStreamingResponse(client.sigact)
        self.site = site.SiteResourceWithStreamingResponse(client.site)
        self.siteremark = siteremark.SiteremarkResourceWithStreamingResponse(client.siteremark)
        self.sitestatus = sitestatus.SitestatusResourceWithStreamingResponse(client.sitestatus)
        self.skyimagery = skyimagery.SkyimageryResourceWithStreamingResponse(client.skyimagery)
        self.soiobservationset = soiobservationset.SoiobservationsetResourceWithStreamingResponse(
            client.soiobservationset
        )
        self.solararray = solararray.SolararrayResourceWithStreamingResponse(client.solararray)
        self.solararraydetails = solararraydetails.SolararraydetailsResourceWithStreamingResponse(
            client.solararraydetails
        )
        self.sortieppr = sortieppr.SortiepprResourceWithStreamingResponse(client.sortieppr)
        self.spaceenvobservation = spaceenvobservation.SpaceenvobservationResourceWithStreamingResponse(
            client.spaceenvobservation
        )
        self.stage = stage.StageResourceWithStreamingResponse(client.stage)
        self.starcatalog = starcatalog.StarcatalogResourceWithStreamingResponse(client.starcatalog)
        self.statevector = statevector.StatevectorResourceWithStreamingResponse(client.statevector)
        self.status = status.StatusResourceWithStreamingResponse(client.status)
        self.substatus = substatus.SubstatusResourceWithStreamingResponse(client.substatus)
        self.supporting_data = supporting_data.SupportingDataResourceWithStreamingResponse(client.supporting_data)
        self.surface = surface.SurfaceResourceWithStreamingResponse(client.surface)
        self.surfaceobstruction = surfaceobstruction.SurfaceobstructionResourceWithStreamingResponse(
            client.surfaceobstruction
        )
        self.swir = swir.SwirResourceWithStreamingResponse(client.swir)
        self.taiutc = taiutc.TaiutcResourceWithStreamingResponse(client.taiutc)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResourceWithStreamingResponse(client.tdoa_fdoa)
        self.track = track.TrackResourceWithStreamingResponse(client.track)
        self.trackdetails = trackdetails.TrackdetailsResourceWithStreamingResponse(client.trackdetails)
        self.trackroute = trackroute.TrackrouteResourceWithStreamingResponse(client.trackroute)
        self.transponder = transponder.TransponderResourceWithStreamingResponse(client.transponder)
        self.vessel = vessel.VesselResourceWithStreamingResponse(client.vessel)
        self.video = video.VideoResourceWithStreamingResponse(client.video)
        self.weatherdata = weatherdata.WeatherdataResourceWithStreamingResponse(client.weatherdata)
        self.weatherreport = weatherreport.WeatherreportResourceWithStreamingResponse(client.weatherreport)
        self.udl = udl.UdlResourceWithStreamingResponse(client.udl)
        self.gnss_observations = gnss_observations.GnssObservationsResourceWithStreamingResponse(
            client.gnss_observations
        )
        self.gnss_raw_if = gnss_raw_if.GnssRawIfResourceWithStreamingResponse(client.gnss_raw_if)
        self.iono_observation = iono_observation.IonoObservationResourceWithStreamingResponse(client.iono_observation)
        self.launch_event = launch_event.LaunchEventResourceWithStreamingResponse(client.launch_event)
        self.report_and_activity = report_and_activity.ReportAndActivityResourceWithStreamingResponse(
            client.report_and_activity
        )
        self.secure_messaging = secure_messaging.SecureMessagingResourceWithStreamingResponse(client.secure_messaging)
        self.scs = scs.ScsResourceWithStreamingResponse(client.scs)
        self.scs_views = scs_views.ScsViewsResourceWithStreamingResponse(client.scs_views)


class AsyncUnifieddatalibraryWithStreamedResponse:
    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self.air_events = air_events.AsyncAirEventsResourceWithStreamingResponse(client.air_events)
        self.air_load_plans = air_load_plans.AsyncAirLoadPlansResourceWithStreamingResponse(client.air_load_plans)
        self.air_operations = air_operations.AsyncAirOperationsResourceWithStreamingResponse(client.air_operations)
        self.air_tasking_orders = air_tasking_orders.AsyncAirTaskingOrdersResourceWithStreamingResponse(
            client.air_tasking_orders
        )
        self.air_transport_missions = air_transport_missions.AsyncAirTransportMissionsResourceWithStreamingResponse(
            client.air_transport_missions
        )
        self.aircraft = aircraft.AsyncAircraftResourceWithStreamingResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AsyncAircraftSortiesResourceWithStreamingResponse(
            client.aircraft_sorties
        )
        self.aircraft_status_remarks = aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithStreamingResponse(
            client.aircraft_status_remarks
        )
        self.aircraft_statuses = aircraft_statuses.AsyncAircraftStatusesResourceWithStreamingResponse(
            client.aircraft_statuses
        )
        self.aircraftstatusremark = aircraftstatusremark.AsyncAircraftstatusremarkResourceWithStreamingResponse(
            client.aircraftstatusremark
        )
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResourceWithStreamingResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResourceWithStreamingResponse(client.airfield_status)
        self.airfields = airfields.AsyncAirfieldsResourceWithStreamingResponse(client.airfields)
        self.airfieldslotconsumptions = (
            airfieldslotconsumptions.AsyncAirfieldslotconsumptionsResourceWithStreamingResponse(
                client.airfieldslotconsumptions
            )
        )
        self.airfieldslots = airfieldslots.AsyncAirfieldslotsResourceWithStreamingResponse(client.airfieldslots)
        self.airfieldstatus = airfieldstatus.AsyncAirfieldstatusResourceWithStreamingResponse(client.airfieldstatus)
        self.airloadplans = airloadplans.AsyncAirloadplansResourceWithStreamingResponse(client.airloadplans)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResourceWithStreamingResponse(
            client.airspace_control_orders
        )
        self.airtaskingorders = airtaskingorders.AsyncAirtaskingordersResourceWithStreamingResponse(
            client.airtaskingorders
        )
        self.ais = ais.AsyncAIsResourceWithStreamingResponse(client.ais)
        self.ais_objects = ais_objects.AsyncAIsObjectsResourceWithStreamingResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResourceWithStreamingResponse(
            client.analytic_imagery
        )
        self.antennas = antennas.AsyncAntennasResourceWithStreamingResponse(client.antennas)
        self.attitude_data = attitude_data.AsyncAttitudeDataResourceWithStreamingResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResourceWithStreamingResponse(client.attitude_sets)
        self.attitudesets = attitudesets.AsyncAttitudesetsResourceWithStreamingResponse(client.attitudesets)
        self.batteries = batteries.AsyncBatteriesResourceWithStreamingResponse(client.batteries)
        self.batterydetails = batterydetails.AsyncBatterydetailsResourceWithStreamingResponse(client.batterydetails)
        self.beam = beam.AsyncBeamResourceWithStreamingResponse(client.beam)
        self.beam_contours = beam_contours.AsyncBeamContoursResourceWithStreamingResponse(client.beam_contours)
        self.buses = buses.AsyncBusesResourceWithStreamingResponse(client.buses)
        self.channels = channels.AsyncChannelsResourceWithStreamingResponse(client.channels)
        self.collect_requests = collect_requests.AsyncCollectRequestsResourceWithStreamingResponse(
            client.collect_requests
        )
        self.collect_responses = collect_responses.AsyncCollectResponsesResourceWithStreamingResponse(
            client.collect_responses
        )
        self.comm = comm.AsyncCommResourceWithStreamingResponse(client.comm)
        self.conjunctions = conjunctions.AsyncConjunctionsResourceWithStreamingResponse(client.conjunctions)
        self.cots = cots.AsyncCotsResourceWithStreamingResponse(client.cots)
        self.aviationriskmanagement = aviationriskmanagement.AsyncAviationriskmanagementResourceWithStreamingResponse(
            client.aviationriskmanagement
        )
        self.dropzone = dropzone.AsyncDropzoneResourceWithStreamingResponse(client.dropzone)
        self.emittergeolocation = emittergeolocation.AsyncEmittergeolocationResourceWithStreamingResponse(
            client.emittergeolocation
        )
        self.featureassessment = featureassessment.AsyncFeatureassessmentResourceWithStreamingResponse(
            client.featureassessment
        )
        self.globalatmosphericmodel = globalatmosphericmodel.AsyncGlobalatmosphericmodelResourceWithStreamingResponse(
            client.globalatmosphericmodel
        )
        self.routestats = routestats.AsyncRoutestatsResourceWithStreamingResponse(client.routestats)
        self.countries = countries.AsyncCountriesResourceWithStreamingResponse(client.countries)
        self.crew = crew.AsyncCrewResourceWithStreamingResponse(client.crew)
        self.diffofarrival = diffofarrival.AsyncDiffofarrivalResourceWithStreamingResponse(client.diffofarrival)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResourceWithStreamingResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.AsyncDriftHistoryResourceWithStreamingResponse(client.drift_history)
        self.ecpsdr = ecpsdr.AsyncEcpsdrResourceWithStreamingResponse(client.ecpsdr)
        self.effect_requests = effect_requests.AsyncEffectRequestsResourceWithStreamingResponse(client.effect_requests)
        self.effect_responses = effect_responses.AsyncEffectResponsesResourceWithStreamingResponse(
            client.effect_responses
        )
        self.elsets = elsets.AsyncElsetsResourceWithStreamingResponse(client.elsets)
        self.engine_details = engine_details.AsyncEngineDetailsResourceWithStreamingResponse(client.engine_details)
        self.enginedetails = enginedetails.AsyncEnginedetailsResourceWithStreamingResponse(client.enginedetails)
        self.engines = engines.AsyncEnginesResourceWithStreamingResponse(client.engines)
        self.entities = entities.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.eo_observations = eo_observations.AsyncEoObservationsResourceWithStreamingResponse(client.eo_observations)
        self.eoobservations = eoobservations.AsyncEoobservationsResourceWithStreamingResponse(client.eoobservations)
        self.eop = eop.AsyncEopResourceWithStreamingResponse(client.eop)
        self.ephemeris = ephemeris.AsyncEphemerisResourceWithStreamingResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResourceWithStreamingResponse(client.ephemeris_sets)
        self.equipment = equipment.AsyncEquipmentResourceWithStreamingResponse(client.equipment)
        self.equipmentremarks = equipmentremarks.AsyncEquipmentremarksResourceWithStreamingResponse(
            client.equipmentremarks
        )
        self.evac = evac.AsyncEvacResourceWithStreamingResponse(client.evac)
        self.event_evolution = event_evolution.AsyncEventEvolutionResourceWithStreamingResponse(client.event_evolution)
        self.flightplan = flightplan.AsyncFlightplanResourceWithStreamingResponse(client.flightplan)
        self.geostatus = geostatus.AsyncGeostatusResourceWithStreamingResponse(client.geostatus)
        self.gnssobservationset = gnssobservationset.AsyncGnssobservationsetResourceWithStreamingResponse(
            client.gnssobservationset
        )
        self.gnssrawif = gnssrawif.AsyncGnssrawifResourceWithStreamingResponse(client.gnssrawif)
        self.ground_imagery = ground_imagery.AsyncGroundImageryResourceWithStreamingResponse(client.ground_imagery)
        self.groundimagery = groundimagery.AsyncGroundimageryResourceWithStreamingResponse(client.groundimagery)
        self.h3geo = h3geo.AsyncH3geoResourceWithStreamingResponse(client.h3geo)
        self.h3geohexcell = h3geohexcell.AsyncH3geohexcellResourceWithStreamingResponse(client.h3geohexcell)
        self.hazard = hazard.AsyncHazardResourceWithStreamingResponse(client.hazard)
        self.ionoobservation = ionoobservation.AsyncIonoobservationResourceWithStreamingResponse(client.ionoobservation)
        self.ir = ir.AsyncIrResourceWithStreamingResponse(client.ir)
        self.isr_collections = isr_collections.AsyncIsrCollectionsResourceWithStreamingResponse(client.isr_collections)
        self.item = item.AsyncItemResourceWithStreamingResponse(client.item)
        self.item_trackings = item_trackings.AsyncItemTrackingsResourceWithStreamingResponse(client.item_trackings)
        self.launchdetection = launchdetection.AsyncLaunchdetectionResourceWithStreamingResponse(client.launchdetection)
        self.launchevent = launchevent.AsyncLauncheventResourceWithStreamingResponse(client.launchevent)
        self.launchsite = launchsite.AsyncLaunchsiteResourceWithStreamingResponse(client.launchsite)
        self.launchsitedetails = launchsitedetails.AsyncLaunchsitedetailsResourceWithStreamingResponse(
            client.launchsitedetails
        )
        self.launchvehicle = launchvehicle.AsyncLaunchvehicleResourceWithStreamingResponse(client.launchvehicle)
        self.launchvehicledetails = launchvehicledetails.AsyncLaunchvehicledetailsResourceWithStreamingResponse(
            client.launchvehicledetails
        )
        self.link_status = link_status.AsyncLinkStatusResourceWithStreamingResponse(client.link_status)
        self.location = location.AsyncLocationResourceWithStreamingResponse(client.location)
        self.logisticssupport = logisticssupport.AsyncLogisticssupportResourceWithStreamingResponse(
            client.logisticssupport
        )
        self.maneuvers = maneuvers.AsyncManeuversResourceWithStreamingResponse(client.maneuvers)
        self.manifold = manifold.AsyncManifoldResourceWithStreamingResponse(client.manifold)
        self.manifoldelset = manifoldelset.AsyncManifoldelsetResourceWithStreamingResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResourceWithStreamingResponse(client.missile_tracks)
        self.missionassignment = missionassignment.AsyncMissionassignmentResourceWithStreamingResponse(
            client.missionassignment
        )
        self.monoradar = monoradar.AsyncMonoradarResourceWithStreamingResponse(client.monoradar)
        self.mti = mti.AsyncMtiResourceWithStreamingResponse(client.mti)
        self.navigation = navigation.AsyncNavigationResourceWithStreamingResponse(client.navigation)
        self.navigationalobstruction = (
            navigationalobstruction.AsyncNavigationalobstructionResourceWithStreamingResponse(
                client.navigationalobstruction
            )
        )
        self.notification = notification.AsyncNotificationResourceWithStreamingResponse(client.notification)
        self.objectofinterest = objectofinterest.AsyncObjectofinterestResourceWithStreamingResponse(
            client.objectofinterest
        )
        self.observations = observations.AsyncObservationsResourceWithStreamingResponse(client.observations)
        self.onboardnavigation = onboardnavigation.AsyncOnboardnavigationResourceWithStreamingResponse(
            client.onboardnavigation
        )
        self.onorbit = onorbit.AsyncOnorbitResourceWithStreamingResponse(client.onorbit)
        self.onorbitantenna = onorbitantenna.AsyncOnorbitantennaResourceWithStreamingResponse(client.onorbitantenna)
        self.onorbitbattery = onorbitbattery.AsyncOnorbitbatteryResourceWithStreamingResponse(client.onorbitbattery)
        self.onorbitdetails = onorbitdetails.AsyncOnorbitdetailsResourceWithStreamingResponse(client.onorbitdetails)
        self.onorbitevent = onorbitevent.AsyncOnorbiteventResourceWithStreamingResponse(client.onorbitevent)
        self.onorbitlist = onorbitlist.AsyncOnorbitlistResourceWithStreamingResponse(client.onorbitlist)
        self.onorbitsolararray = onorbitsolararray.AsyncOnorbitsolararrayResourceWithStreamingResponse(
            client.onorbitsolararray
        )
        self.onorbitthruster = onorbitthruster.AsyncOnorbitthrusterResourceWithStreamingResponse(client.onorbitthruster)
        self.onorbitthrusterstatus = onorbitthrusterstatus.AsyncOnorbitthrusterstatusResourceWithStreamingResponse(
            client.onorbitthrusterstatus
        )
        self.operatingunit = operatingunit.AsyncOperatingunitResourceWithStreamingResponse(client.operatingunit)
        self.operatingunitremark = operatingunitremark.AsyncOperatingunitremarkResourceWithStreamingResponse(
            client.operatingunitremark
        )
        self.orbitdetermination = orbitdetermination.AsyncOrbitdeterminationResourceWithStreamingResponse(
            client.orbitdetermination
        )
        self.orbittrack = orbittrack.AsyncOrbittrackResourceWithStreamingResponse(client.orbittrack)
        self.organization = organization.AsyncOrganizationResourceWithStreamingResponse(client.organization)
        self.organizationdetails = organizationdetails.AsyncOrganizationdetailsResourceWithStreamingResponse(
            client.organizationdetails
        )
        self.passiveradarobservation = (
            passiveradarobservation.AsyncPassiveradarobservationResourceWithStreamingResponse(
                client.passiveradarobservation
            )
        )
        self.personnelrecovery = personnelrecovery.AsyncPersonnelrecoveryResourceWithStreamingResponse(
            client.personnelrecovery
        )
        self.poi = poi.AsyncPoiResourceWithStreamingResponse(client.poi)
        self.port = port.AsyncPortResourceWithStreamingResponse(client.port)
        self.radarobservation = radarobservation.AsyncRadarobservationResourceWithStreamingResponse(
            client.radarobservation
        )
        self.rfband = rfband.AsyncRfbandResourceWithStreamingResponse(client.rfband)
        self.rfbandtype = rfbandtype.AsyncRfbandtypeResourceWithStreamingResponse(client.rfbandtype)
        self.rfemitter = rfemitter.AsyncRfemitterResourceWithStreamingResponse(client.rfemitter)
        self.rfemitterdetails = rfemitterdetails.AsyncRfemitterdetailsResourceWithStreamingResponse(
            client.rfemitterdetails
        )
        self.rfobservation = rfobservation.AsyncRfobservationResourceWithStreamingResponse(client.rfobservation)
        self.sarobservation = sarobservation.AsyncSarobservationResourceWithStreamingResponse(client.sarobservation)
        self.scientific = scientific.AsyncScientificResourceWithStreamingResponse(client.scientific)
        self.sensor = sensor.AsyncSensorResourceWithStreamingResponse(client.sensor)
        self.sensormaintenance = sensormaintenance.AsyncSensormaintenanceResourceWithStreamingResponse(
            client.sensormaintenance
        )
        self.sensorobservationtype = sensorobservationtype.AsyncSensorobservationtypeResourceWithStreamingResponse(
            client.sensorobservationtype
        )
        self.sensorplan = sensorplan.AsyncSensorplanResourceWithStreamingResponse(client.sensorplan)
        self.sensortype = sensortype.AsyncSensortypeResourceWithStreamingResponse(client.sensortype)
        self.seradatacommdetails = seradatacommdetails.AsyncSeradatacommdetailsResourceWithStreamingResponse(
            client.seradatacommdetails
        )
        self.seradataearlywarning = seradataearlywarning.AsyncSeradataearlywarningResourceWithStreamingResponse(
            client.seradataearlywarning
        )
        self.seradatanavigation = seradatanavigation.AsyncSeradatanavigationResourceWithStreamingResponse(
            client.seradatanavigation
        )
        self.seradataopticalpayload = seradataopticalpayload.AsyncSeradataopticalpayloadResourceWithStreamingResponse(
            client.seradataopticalpayload
        )
        self.seradataradarpayload = seradataradarpayload.AsyncSeradataradarpayloadResourceWithStreamingResponse(
            client.seradataradarpayload
        )
        self.seradatasigintpayload = seradatasigintpayload.AsyncSeradatasigintpayloadResourceWithStreamingResponse(
            client.seradatasigintpayload
        )
        self.seradataspacecraftdetails = (
            seradataspacecraftdetails.AsyncSeradataspacecraftdetailsResourceWithStreamingResponse(
                client.seradataspacecraftdetails
            )
        )
        self.sgi = sgi.AsyncSgiResourceWithStreamingResponse(client.sgi)
        self.sigact = sigact.AsyncSigactResourceWithStreamingResponse(client.sigact)
        self.site = site.AsyncSiteResourceWithStreamingResponse(client.site)
        self.siteremark = siteremark.AsyncSiteremarkResourceWithStreamingResponse(client.siteremark)
        self.sitestatus = sitestatus.AsyncSitestatusResourceWithStreamingResponse(client.sitestatus)
        self.skyimagery = skyimagery.AsyncSkyimageryResourceWithStreamingResponse(client.skyimagery)
        self.soiobservationset = soiobservationset.AsyncSoiobservationsetResourceWithStreamingResponse(
            client.soiobservationset
        )
        self.solararray = solararray.AsyncSolararrayResourceWithStreamingResponse(client.solararray)
        self.solararraydetails = solararraydetails.AsyncSolararraydetailsResourceWithStreamingResponse(
            client.solararraydetails
        )
        self.sortieppr = sortieppr.AsyncSortiepprResourceWithStreamingResponse(client.sortieppr)
        self.spaceenvobservation = spaceenvobservation.AsyncSpaceenvobservationResourceWithStreamingResponse(
            client.spaceenvobservation
        )
        self.stage = stage.AsyncStageResourceWithStreamingResponse(client.stage)
        self.starcatalog = starcatalog.AsyncStarcatalogResourceWithStreamingResponse(client.starcatalog)
        self.statevector = statevector.AsyncStatevectorResourceWithStreamingResponse(client.statevector)
        self.status = status.AsyncStatusResourceWithStreamingResponse(client.status)
        self.substatus = substatus.AsyncSubstatusResourceWithStreamingResponse(client.substatus)
        self.supporting_data = supporting_data.AsyncSupportingDataResourceWithStreamingResponse(client.supporting_data)
        self.surface = surface.AsyncSurfaceResourceWithStreamingResponse(client.surface)
        self.surfaceobstruction = surfaceobstruction.AsyncSurfaceobstructionResourceWithStreamingResponse(
            client.surfaceobstruction
        )
        self.swir = swir.AsyncSwirResourceWithStreamingResponse(client.swir)
        self.taiutc = taiutc.AsyncTaiutcResourceWithStreamingResponse(client.taiutc)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResourceWithStreamingResponse(client.tdoa_fdoa)
        self.track = track.AsyncTrackResourceWithStreamingResponse(client.track)
        self.trackdetails = trackdetails.AsyncTrackdetailsResourceWithStreamingResponse(client.trackdetails)
        self.trackroute = trackroute.AsyncTrackrouteResourceWithStreamingResponse(client.trackroute)
        self.transponder = transponder.AsyncTransponderResourceWithStreamingResponse(client.transponder)
        self.vessel = vessel.AsyncVesselResourceWithStreamingResponse(client.vessel)
        self.video = video.AsyncVideoResourceWithStreamingResponse(client.video)
        self.weatherdata = weatherdata.AsyncWeatherdataResourceWithStreamingResponse(client.weatherdata)
        self.weatherreport = weatherreport.AsyncWeatherreportResourceWithStreamingResponse(client.weatherreport)
        self.udl = udl.AsyncUdlResourceWithStreamingResponse(client.udl)
        self.gnss_observations = gnss_observations.AsyncGnssObservationsResourceWithStreamingResponse(
            client.gnss_observations
        )
        self.gnss_raw_if = gnss_raw_if.AsyncGnssRawIfResourceWithStreamingResponse(client.gnss_raw_if)
        self.iono_observation = iono_observation.AsyncIonoObservationResourceWithStreamingResponse(
            client.iono_observation
        )
        self.launch_event = launch_event.AsyncLaunchEventResourceWithStreamingResponse(client.launch_event)
        self.report_and_activity = report_and_activity.AsyncReportAndActivityResourceWithStreamingResponse(
            client.report_and_activity
        )
        self.secure_messaging = secure_messaging.AsyncSecureMessagingResourceWithStreamingResponse(
            client.secure_messaging
        )
        self.scs = scs.AsyncScsResourceWithStreamingResponse(client.scs)
        self.scs_views = scs_views.AsyncScsViewsResourceWithStreamingResponse(client.scs_views)


Client = Unifieddatalibrary

AsyncClient = AsyncUnifieddatalibrary
