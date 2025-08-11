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
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    ir,
    poi,
    beam,
    comm,
    cots,
    crew,
    item,
    port,
    buses,
    stage,
    status,
    vessel,
    ecp_sdr,
    engines,
    rf_band,
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
    scs_views,
    substatus,
    air_events,
    flightplan,
    navigation,
    rf_emitter,
    scientific,
    ais_objects,
    launch_site,
    onorbitlist,
    route_stats,
    sensor_type,
    site_remark,
    solar_array,
    transponder,
    onorbitevent,
    organization,
    rf_band_type,
    airload_plans,
    attitude_data,
    beam_contours,
    drift_history,
    manifoldelset,
    operatingunit,
    airfield_slots,
    batterydetails,
    engine_details,
    launch_vehicle,
    onorbitantenna,
    onorbitbattery,
    onorbitdetails,
    h3_geo_hex_cell,
    onorbitthruster,
    aircraft_sorties,
    analytic_imagery,
    launch_detection,
    secure_messaging,
    equipment_remarks,
    onorbitsolararray,
    object_of_interest,
    rf_emitter_details,
    emitter_geolocation,
    launch_site_details,
    operatingunitremark,
    organizationdetails,
    solar_array_details,
    surface_obstruction,
    sera_data_navigation,
    launch_vehicle_details,
    sera_data_comm_details,
    seradata_radar_payload,
    aircraft_status_remarks,
    airspace_control_orders,
    sensor_observation_type,
    sera_data_early_warning,
    seradata_sigint_payload,
    aviation_risk_management,
    navigational_obstruction,
    seradata_optical_payload,
    airfield_slot_consumptions,
    seradata_spacecraft_details,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.ais import ais
from .resources.eop import eop
from .resources.mti import mti
from .resources.scs import scs
from .resources.sgi import sgi
from .resources.evac import evac
from .resources.site import site
from .resources.swir import swir
from .resources.track import track
from .resources.video import video
from .resources.elsets import elsets
from .resources.h3_geo import h3_geo
from .resources.hazard import hazard
from .resources.sensor import sensor
from .resources.sigact import sigact
from .resources.onorbit import onorbit
from .resources.tai_utc import tai_utc
from .resources.ephemeris import ephemeris
from .resources.maneuvers import maneuvers
from .resources.tdoa_fdoa import tdoa_fdoa
from .resources.geo_status import geo_status
from .resources.orbittrack import orbittrack
from .resources.sortie_ppr import sortie_ppr
from .resources.gnss_raw_if import gnss_raw_if
from .resources.link_status import link_status
from .resources.sensor_plan import sensor_plan
from .resources.site_status import site_status
from .resources.sky_imagery import sky_imagery
from .resources.track_route import track_route
from .resources.conjunctions import conjunctions
from .resources.launch_event import launch_event
from .resources.notification import notification
from .resources.observations import observations
from .resources.star_catalog import star_catalog
from .resources.state_vector import state_vector
from .resources.weather_data import weather_data
from .resources.attitude_sets import attitude_sets
from .resources.track_details import track_details
from .resources.air_operations import air_operations
from .resources.ephemeris_sets import ephemeris_sets
from .resources.ground_imagery import ground_imagery
from .resources.item_trackings import item_trackings
from .resources.missile_tracks import missile_tracks
from .resources.weather_report import weather_report
from .resources.airfield_status import airfield_status
from .resources.diff_of_arrival import diff_of_arrival
from .resources.effect_requests import effect_requests
from .resources.event_evolution import event_evolution
from .resources.isr_collections import isr_collections
from .resources.sar_observation import sar_observation
from .resources.supporting_data import supporting_data
from .resources.collect_requests import collect_requests
from .resources.effect_responses import effect_responses
from .resources.aircraft_statuses import aircraft_statuses
from .resources.collect_responses import collect_responses
from .resources.gnss_observations import gnss_observations
from .resources.iono_observations import iono_observations
from .resources.logistics_support import logistics_support
from .resources.onboardnavigation import onboardnavigation
from .resources.personnelrecovery import personnelrecovery
from .resources.feature_assessment import feature_assessment
from .resources.mission_assignment import mission_assignment
from .resources.orbitdetermination import orbitdetermination
from .resources.sensor_maintenance import sensor_maintenance
from .resources.gnss_observationset import gnss_observationset
from .resources.soi_observation_set import soi_observation_set
from .resources.diplomatic_clearance import diplomatic_clearance
from .resources.onorbitthrusterstatus import onorbitthrusterstatus
from .resources.report_and_activities import report_and_activities
from .resources.space_env_observation import space_env_observation
from .resources.air_transport_missions import air_transport_missions
from .resources.global_atmospheric_model import global_atmospheric_model

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
    air_operations: air_operations.AirOperationsResource
    air_transport_missions: air_transport_missions.AirTransportMissionsResource
    aircraft: aircraft.AircraftResource
    aircraft_sorties: aircraft_sorties.AircraftSortiesResource
    aircraft_status_remarks: aircraft_status_remarks.AircraftStatusRemarksResource
    aircraft_statuses: aircraft_statuses.AircraftStatusesResource
    airfield_slots: airfield_slots.AirfieldSlotsResource
    airfield_status: airfield_status.AirfieldStatusResource
    airfields: airfields.AirfieldsResource
    airfield_slot_consumptions: airfield_slot_consumptions.AirfieldSlotConsumptionsResource
    airload_plans: airload_plans.AirloadPlansResource
    airspace_control_orders: airspace_control_orders.AirspaceControlOrdersResource
    ais: ais.AIsResource
    ais_objects: ais_objects.AIsObjectsResource
    analytic_imagery: analytic_imagery.AnalyticImageryResource
    antennas: antennas.AntennasResource
    attitude_data: attitude_data.AttitudeDataResource
    attitude_sets: attitude_sets.AttitudeSetsResource
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
    aviation_risk_management: aviation_risk_management.AviationRiskManagementResource
    dropzone: dropzone.DropzoneResource
    emitter_geolocation: emitter_geolocation.EmitterGeolocationResource
    feature_assessment: feature_assessment.FeatureAssessmentResource
    global_atmospheric_model: global_atmospheric_model.GlobalAtmosphericModelResource
    route_stats: route_stats.RouteStatsResource
    countries: countries.CountriesResource
    crew: crew.CrewResource
    diff_of_arrival: diff_of_arrival.DiffOfArrivalResource
    diplomatic_clearance: diplomatic_clearance.DiplomaticClearanceResource
    drift_history: drift_history.DriftHistoryResource
    ecp_sdr: ecp_sdr.EcpSdrResource
    effect_requests: effect_requests.EffectRequestsResource
    effect_responses: effect_responses.EffectResponsesResource
    elsets: elsets.ElsetsResource
    engine_details: engine_details.EngineDetailsResource
    engines: engines.EnginesResource
    entities: entities.EntitiesResource
    eop: eop.EopResource
    ephemeris: ephemeris.EphemerisResource
    ephemeris_sets: ephemeris_sets.EphemerisSetsResource
    equipment: equipment.EquipmentResource
    equipment_remarks: equipment_remarks.EquipmentRemarksResource
    evac: evac.EvacResource
    event_evolution: event_evolution.EventEvolutionResource
    flightplan: flightplan.FlightplanResource
    geo_status: geo_status.GeoStatusResource
    gnss_observationset: gnss_observationset.GnssObservationsetResource
    ground_imagery: ground_imagery.GroundImageryResource
    h3_geo: h3_geo.H3GeoResource
    h3_geo_hex_cell: h3_geo_hex_cell.H3GeoHexCellResource
    hazard: hazard.HazardResource
    ir: ir.IrResource
    isr_collections: isr_collections.IsrCollectionsResource
    item: item.ItemResource
    item_trackings: item_trackings.ItemTrackingsResource
    launch_detection: launch_detection.LaunchDetectionResource
    launch_event: launch_event.LaunchEventResource
    launch_site: launch_site.LaunchSiteResource
    launch_site_details: launch_site_details.LaunchSiteDetailsResource
    launch_vehicle: launch_vehicle.LaunchVehicleResource
    launch_vehicle_details: launch_vehicle_details.LaunchVehicleDetailsResource
    link_status: link_status.LinkStatusResource
    location: location.LocationResource
    logistics_support: logistics_support.LogisticsSupportResource
    maneuvers: maneuvers.ManeuversResource
    manifold: manifold.ManifoldResource
    manifoldelset: manifoldelset.ManifoldelsetResource
    missile_tracks: missile_tracks.MissileTracksResource
    mission_assignment: mission_assignment.MissionAssignmentResource
    mti: mti.MtiResource
    navigation: navigation.NavigationResource
    navigational_obstruction: navigational_obstruction.NavigationalObstructionResource
    notification: notification.NotificationResource
    object_of_interest: object_of_interest.ObjectOfInterestResource
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
    personnelrecovery: personnelrecovery.PersonnelrecoveryResource
    poi: poi.PoiResource
    port: port.PortResource
    rf_band: rf_band.RfBandResource
    rf_band_type: rf_band_type.RfBandTypeResource
    rf_emitter: rf_emitter.RfEmitterResource
    rf_emitter_details: rf_emitter_details.RfEmitterDetailsResource
    sar_observation: sar_observation.SarObservationResource
    scientific: scientific.ScientificResource
    sensor: sensor.SensorResource
    sensor_maintenance: sensor_maintenance.SensorMaintenanceResource
    sensor_observation_type: sensor_observation_type.SensorObservationTypeResource
    sensor_plan: sensor_plan.SensorPlanResource
    sensor_type: sensor_type.SensorTypeResource
    sera_data_comm_details: sera_data_comm_details.SeraDataCommDetailsResource
    sera_data_early_warning: sera_data_early_warning.SeraDataEarlyWarningResource
    sera_data_navigation: sera_data_navigation.SeraDataNavigationResource
    seradata_optical_payload: seradata_optical_payload.SeradataOpticalPayloadResource
    seradata_radar_payload: seradata_radar_payload.SeradataRadarPayloadResource
    seradata_sigint_payload: seradata_sigint_payload.SeradataSigintPayloadResource
    seradata_spacecraft_details: seradata_spacecraft_details.SeradataSpacecraftDetailsResource
    sgi: sgi.SgiResource
    sigact: sigact.SigactResource
    site: site.SiteResource
    site_remark: site_remark.SiteRemarkResource
    site_status: site_status.SiteStatusResource
    sky_imagery: sky_imagery.SkyImageryResource
    soi_observation_set: soi_observation_set.SoiObservationSetResource
    solar_array: solar_array.SolarArrayResource
    solar_array_details: solar_array_details.SolarArrayDetailsResource
    sortie_ppr: sortie_ppr.SortiePprResource
    space_env_observation: space_env_observation.SpaceEnvObservationResource
    stage: stage.StageResource
    star_catalog: star_catalog.StarCatalogResource
    state_vector: state_vector.StateVectorResource
    status: status.StatusResource
    substatus: substatus.SubstatusResource
    supporting_data: supporting_data.SupportingDataResource
    surface: surface.SurfaceResource
    surface_obstruction: surface_obstruction.SurfaceObstructionResource
    swir: swir.SwirResource
    tai_utc: tai_utc.TaiUtcResource
    tdoa_fdoa: tdoa_fdoa.TdoaFdoaResource
    track: track.TrackResource
    track_details: track_details.TrackDetailsResource
    track_route: track_route.TrackRouteResource
    transponder: transponder.TransponderResource
    vessel: vessel.VesselResource
    video: video.VideoResource
    weather_data: weather_data.WeatherDataResource
    weather_report: weather_report.WeatherReportResource
    gnss_observations: gnss_observations.GnssObservationsResource
    gnss_raw_if: gnss_raw_if.GnssRawIfResource
    iono_observations: iono_observations.IonoObservationsResource
    report_and_activities: report_and_activities.ReportAndActivitiesResource
    secure_messaging: secure_messaging.SecureMessagingResource
    scs: scs.ScsResource
    scs_views: scs_views.ScsViewsResource
    with_raw_response: UnifieddatalibraryWithRawResponse
    with_streaming_response: UnifieddatalibraryWithStreamedResponse

    # client options
    password: str | None
    username: str | None
    access_token: str | None

    def __init__(
        self,
        *,
        password: str | None = None,
        username: str | None = None,
        access_token: str | None = None,
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
        - `access_token` from `UDL_ACCESS_TOKEN`
        """
        if password is None:
            password = os.environ.get("UDL_AUTH_PASSWORD")
        self.password = password

        if username is None:
            username = os.environ.get("UDL_AUTH_USERNAME")
        self.username = username

        if access_token is None:
            access_token = os.environ.get("UDL_ACCESS_TOKEN")
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("UNIFIEDDATALIBRARY_BASE_URL")
        self._base_url_overridden = base_url is not None
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
        self.air_operations = air_operations.AirOperationsResource(self)
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResource(self)
        self.aircraft = aircraft.AircraftResource(self)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResource(self)
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResource(self)
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResource(self)
        self.airfield_slots = airfield_slots.AirfieldSlotsResource(self)
        self.airfield_status = airfield_status.AirfieldStatusResource(self)
        self.airfields = airfields.AirfieldsResource(self)
        self.airfield_slot_consumptions = airfield_slot_consumptions.AirfieldSlotConsumptionsResource(self)
        self.airload_plans = airload_plans.AirloadPlansResource(self)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResource(self)
        self.ais = ais.AIsResource(self)
        self.ais_objects = ais_objects.AIsObjectsResource(self)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResource(self)
        self.antennas = antennas.AntennasResource(self)
        self.attitude_data = attitude_data.AttitudeDataResource(self)
        self.attitude_sets = attitude_sets.AttitudeSetsResource(self)
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
        self.aviation_risk_management = aviation_risk_management.AviationRiskManagementResource(self)
        self.dropzone = dropzone.DropzoneResource(self)
        self.emitter_geolocation = emitter_geolocation.EmitterGeolocationResource(self)
        self.feature_assessment = feature_assessment.FeatureAssessmentResource(self)
        self.global_atmospheric_model = global_atmospheric_model.GlobalAtmosphericModelResource(self)
        self.route_stats = route_stats.RouteStatsResource(self)
        self.countries = countries.CountriesResource(self)
        self.crew = crew.CrewResource(self)
        self.diff_of_arrival = diff_of_arrival.DiffOfArrivalResource(self)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResource(self)
        self.drift_history = drift_history.DriftHistoryResource(self)
        self.ecp_sdr = ecp_sdr.EcpSdrResource(self)
        self.effect_requests = effect_requests.EffectRequestsResource(self)
        self.effect_responses = effect_responses.EffectResponsesResource(self)
        self.elsets = elsets.ElsetsResource(self)
        self.engine_details = engine_details.EngineDetailsResource(self)
        self.engines = engines.EnginesResource(self)
        self.entities = entities.EntitiesResource(self)
        self.eop = eop.EopResource(self)
        self.ephemeris = ephemeris.EphemerisResource(self)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResource(self)
        self.equipment = equipment.EquipmentResource(self)
        self.equipment_remarks = equipment_remarks.EquipmentRemarksResource(self)
        self.evac = evac.EvacResource(self)
        self.event_evolution = event_evolution.EventEvolutionResource(self)
        self.flightplan = flightplan.FlightplanResource(self)
        self.geo_status = geo_status.GeoStatusResource(self)
        self.gnss_observationset = gnss_observationset.GnssObservationsetResource(self)
        self.ground_imagery = ground_imagery.GroundImageryResource(self)
        self.h3_geo = h3_geo.H3GeoResource(self)
        self.h3_geo_hex_cell = h3_geo_hex_cell.H3GeoHexCellResource(self)
        self.hazard = hazard.HazardResource(self)
        self.ir = ir.IrResource(self)
        self.isr_collections = isr_collections.IsrCollectionsResource(self)
        self.item = item.ItemResource(self)
        self.item_trackings = item_trackings.ItemTrackingsResource(self)
        self.launch_detection = launch_detection.LaunchDetectionResource(self)
        self.launch_event = launch_event.LaunchEventResource(self)
        self.launch_site = launch_site.LaunchSiteResource(self)
        self.launch_site_details = launch_site_details.LaunchSiteDetailsResource(self)
        self.launch_vehicle = launch_vehicle.LaunchVehicleResource(self)
        self.launch_vehicle_details = launch_vehicle_details.LaunchVehicleDetailsResource(self)
        self.link_status = link_status.LinkStatusResource(self)
        self.location = location.LocationResource(self)
        self.logistics_support = logistics_support.LogisticsSupportResource(self)
        self.maneuvers = maneuvers.ManeuversResource(self)
        self.manifold = manifold.ManifoldResource(self)
        self.manifoldelset = manifoldelset.ManifoldelsetResource(self)
        self.missile_tracks = missile_tracks.MissileTracksResource(self)
        self.mission_assignment = mission_assignment.MissionAssignmentResource(self)
        self.mti = mti.MtiResource(self)
        self.navigation = navigation.NavigationResource(self)
        self.navigational_obstruction = navigational_obstruction.NavigationalObstructionResource(self)
        self.notification = notification.NotificationResource(self)
        self.object_of_interest = object_of_interest.ObjectOfInterestResource(self)
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
        self.personnelrecovery = personnelrecovery.PersonnelrecoveryResource(self)
        self.poi = poi.PoiResource(self)
        self.port = port.PortResource(self)
        self.rf_band = rf_band.RfBandResource(self)
        self.rf_band_type = rf_band_type.RfBandTypeResource(self)
        self.rf_emitter = rf_emitter.RfEmitterResource(self)
        self.rf_emitter_details = rf_emitter_details.RfEmitterDetailsResource(self)
        self.sar_observation = sar_observation.SarObservationResource(self)
        self.scientific = scientific.ScientificResource(self)
        self.sensor = sensor.SensorResource(self)
        self.sensor_maintenance = sensor_maintenance.SensorMaintenanceResource(self)
        self.sensor_observation_type = sensor_observation_type.SensorObservationTypeResource(self)
        self.sensor_plan = sensor_plan.SensorPlanResource(self)
        self.sensor_type = sensor_type.SensorTypeResource(self)
        self.sera_data_comm_details = sera_data_comm_details.SeraDataCommDetailsResource(self)
        self.sera_data_early_warning = sera_data_early_warning.SeraDataEarlyWarningResource(self)
        self.sera_data_navigation = sera_data_navigation.SeraDataNavigationResource(self)
        self.seradata_optical_payload = seradata_optical_payload.SeradataOpticalPayloadResource(self)
        self.seradata_radar_payload = seradata_radar_payload.SeradataRadarPayloadResource(self)
        self.seradata_sigint_payload = seradata_sigint_payload.SeradataSigintPayloadResource(self)
        self.seradata_spacecraft_details = seradata_spacecraft_details.SeradataSpacecraftDetailsResource(self)
        self.sgi = sgi.SgiResource(self)
        self.sigact = sigact.SigactResource(self)
        self.site = site.SiteResource(self)
        self.site_remark = site_remark.SiteRemarkResource(self)
        self.site_status = site_status.SiteStatusResource(self)
        self.sky_imagery = sky_imagery.SkyImageryResource(self)
        self.soi_observation_set = soi_observation_set.SoiObservationSetResource(self)
        self.solar_array = solar_array.SolarArrayResource(self)
        self.solar_array_details = solar_array_details.SolarArrayDetailsResource(self)
        self.sortie_ppr = sortie_ppr.SortiePprResource(self)
        self.space_env_observation = space_env_observation.SpaceEnvObservationResource(self)
        self.stage = stage.StageResource(self)
        self.star_catalog = star_catalog.StarCatalogResource(self)
        self.state_vector = state_vector.StateVectorResource(self)
        self.status = status.StatusResource(self)
        self.substatus = substatus.SubstatusResource(self)
        self.supporting_data = supporting_data.SupportingDataResource(self)
        self.surface = surface.SurfaceResource(self)
        self.surface_obstruction = surface_obstruction.SurfaceObstructionResource(self)
        self.swir = swir.SwirResource(self)
        self.tai_utc = tai_utc.TaiUtcResource(self)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResource(self)
        self.track = track.TrackResource(self)
        self.track_details = track_details.TrackDetailsResource(self)
        self.track_route = track_route.TrackRouteResource(self)
        self.transponder = transponder.TransponderResource(self)
        self.vessel = vessel.VesselResource(self)
        self.video = video.VideoResource(self)
        self.weather_data = weather_data.WeatherDataResource(self)
        self.weather_report = weather_report.WeatherReportResource(self)
        self.gnss_observations = gnss_observations.GnssObservationsResource(self)
        self.gnss_raw_if = gnss_raw_if.GnssRawIfResource(self)
        self.iono_observations = iono_observations.IonoObservationsResource(self)
        self.report_and_activities = report_and_activities.ReportAndActivitiesResource(self)
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
        return {**self._basic_auth, **self._bearer_auth}

    @property
    def _basic_auth(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.username and self.password and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.access_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either username, password or access_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        password: str | None = None,
        username: str | None = None,
        access_token: str | None = None,
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
        client = self.__class__(
            password=password or self.password,
            username=username or self.username,
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

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
    air_operations: air_operations.AsyncAirOperationsResource
    air_transport_missions: air_transport_missions.AsyncAirTransportMissionsResource
    aircraft: aircraft.AsyncAircraftResource
    aircraft_sorties: aircraft_sorties.AsyncAircraftSortiesResource
    aircraft_status_remarks: aircraft_status_remarks.AsyncAircraftStatusRemarksResource
    aircraft_statuses: aircraft_statuses.AsyncAircraftStatusesResource
    airfield_slots: airfield_slots.AsyncAirfieldSlotsResource
    airfield_status: airfield_status.AsyncAirfieldStatusResource
    airfields: airfields.AsyncAirfieldsResource
    airfield_slot_consumptions: airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResource
    airload_plans: airload_plans.AsyncAirloadPlansResource
    airspace_control_orders: airspace_control_orders.AsyncAirspaceControlOrdersResource
    ais: ais.AsyncAIsResource
    ais_objects: ais_objects.AsyncAIsObjectsResource
    analytic_imagery: analytic_imagery.AsyncAnalyticImageryResource
    antennas: antennas.AsyncAntennasResource
    attitude_data: attitude_data.AsyncAttitudeDataResource
    attitude_sets: attitude_sets.AsyncAttitudeSetsResource
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
    aviation_risk_management: aviation_risk_management.AsyncAviationRiskManagementResource
    dropzone: dropzone.AsyncDropzoneResource
    emitter_geolocation: emitter_geolocation.AsyncEmitterGeolocationResource
    feature_assessment: feature_assessment.AsyncFeatureAssessmentResource
    global_atmospheric_model: global_atmospheric_model.AsyncGlobalAtmosphericModelResource
    route_stats: route_stats.AsyncRouteStatsResource
    countries: countries.AsyncCountriesResource
    crew: crew.AsyncCrewResource
    diff_of_arrival: diff_of_arrival.AsyncDiffOfArrivalResource
    diplomatic_clearance: diplomatic_clearance.AsyncDiplomaticClearanceResource
    drift_history: drift_history.AsyncDriftHistoryResource
    ecp_sdr: ecp_sdr.AsyncEcpSdrResource
    effect_requests: effect_requests.AsyncEffectRequestsResource
    effect_responses: effect_responses.AsyncEffectResponsesResource
    elsets: elsets.AsyncElsetsResource
    engine_details: engine_details.AsyncEngineDetailsResource
    engines: engines.AsyncEnginesResource
    entities: entities.AsyncEntitiesResource
    eop: eop.AsyncEopResource
    ephemeris: ephemeris.AsyncEphemerisResource
    ephemeris_sets: ephemeris_sets.AsyncEphemerisSetsResource
    equipment: equipment.AsyncEquipmentResource
    equipment_remarks: equipment_remarks.AsyncEquipmentRemarksResource
    evac: evac.AsyncEvacResource
    event_evolution: event_evolution.AsyncEventEvolutionResource
    flightplan: flightplan.AsyncFlightplanResource
    geo_status: geo_status.AsyncGeoStatusResource
    gnss_observationset: gnss_observationset.AsyncGnssObservationsetResource
    ground_imagery: ground_imagery.AsyncGroundImageryResource
    h3_geo: h3_geo.AsyncH3GeoResource
    h3_geo_hex_cell: h3_geo_hex_cell.AsyncH3GeoHexCellResource
    hazard: hazard.AsyncHazardResource
    ir: ir.AsyncIrResource
    isr_collections: isr_collections.AsyncIsrCollectionsResource
    item: item.AsyncItemResource
    item_trackings: item_trackings.AsyncItemTrackingsResource
    launch_detection: launch_detection.AsyncLaunchDetectionResource
    launch_event: launch_event.AsyncLaunchEventResource
    launch_site: launch_site.AsyncLaunchSiteResource
    launch_site_details: launch_site_details.AsyncLaunchSiteDetailsResource
    launch_vehicle: launch_vehicle.AsyncLaunchVehicleResource
    launch_vehicle_details: launch_vehicle_details.AsyncLaunchVehicleDetailsResource
    link_status: link_status.AsyncLinkStatusResource
    location: location.AsyncLocationResource
    logistics_support: logistics_support.AsyncLogisticsSupportResource
    maneuvers: maneuvers.AsyncManeuversResource
    manifold: manifold.AsyncManifoldResource
    manifoldelset: manifoldelset.AsyncManifoldelsetResource
    missile_tracks: missile_tracks.AsyncMissileTracksResource
    mission_assignment: mission_assignment.AsyncMissionAssignmentResource
    mti: mti.AsyncMtiResource
    navigation: navigation.AsyncNavigationResource
    navigational_obstruction: navigational_obstruction.AsyncNavigationalObstructionResource
    notification: notification.AsyncNotificationResource
    object_of_interest: object_of_interest.AsyncObjectOfInterestResource
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
    personnelrecovery: personnelrecovery.AsyncPersonnelrecoveryResource
    poi: poi.AsyncPoiResource
    port: port.AsyncPortResource
    rf_band: rf_band.AsyncRfBandResource
    rf_band_type: rf_band_type.AsyncRfBandTypeResource
    rf_emitter: rf_emitter.AsyncRfEmitterResource
    rf_emitter_details: rf_emitter_details.AsyncRfEmitterDetailsResource
    sar_observation: sar_observation.AsyncSarObservationResource
    scientific: scientific.AsyncScientificResource
    sensor: sensor.AsyncSensorResource
    sensor_maintenance: sensor_maintenance.AsyncSensorMaintenanceResource
    sensor_observation_type: sensor_observation_type.AsyncSensorObservationTypeResource
    sensor_plan: sensor_plan.AsyncSensorPlanResource
    sensor_type: sensor_type.AsyncSensorTypeResource
    sera_data_comm_details: sera_data_comm_details.AsyncSeraDataCommDetailsResource
    sera_data_early_warning: sera_data_early_warning.AsyncSeraDataEarlyWarningResource
    sera_data_navigation: sera_data_navigation.AsyncSeraDataNavigationResource
    seradata_optical_payload: seradata_optical_payload.AsyncSeradataOpticalPayloadResource
    seradata_radar_payload: seradata_radar_payload.AsyncSeradataRadarPayloadResource
    seradata_sigint_payload: seradata_sigint_payload.AsyncSeradataSigintPayloadResource
    seradata_spacecraft_details: seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResource
    sgi: sgi.AsyncSgiResource
    sigact: sigact.AsyncSigactResource
    site: site.AsyncSiteResource
    site_remark: site_remark.AsyncSiteRemarkResource
    site_status: site_status.AsyncSiteStatusResource
    sky_imagery: sky_imagery.AsyncSkyImageryResource
    soi_observation_set: soi_observation_set.AsyncSoiObservationSetResource
    solar_array: solar_array.AsyncSolarArrayResource
    solar_array_details: solar_array_details.AsyncSolarArrayDetailsResource
    sortie_ppr: sortie_ppr.AsyncSortiePprResource
    space_env_observation: space_env_observation.AsyncSpaceEnvObservationResource
    stage: stage.AsyncStageResource
    star_catalog: star_catalog.AsyncStarCatalogResource
    state_vector: state_vector.AsyncStateVectorResource
    status: status.AsyncStatusResource
    substatus: substatus.AsyncSubstatusResource
    supporting_data: supporting_data.AsyncSupportingDataResource
    surface: surface.AsyncSurfaceResource
    surface_obstruction: surface_obstruction.AsyncSurfaceObstructionResource
    swir: swir.AsyncSwirResource
    tai_utc: tai_utc.AsyncTaiUtcResource
    tdoa_fdoa: tdoa_fdoa.AsyncTdoaFdoaResource
    track: track.AsyncTrackResource
    track_details: track_details.AsyncTrackDetailsResource
    track_route: track_route.AsyncTrackRouteResource
    transponder: transponder.AsyncTransponderResource
    vessel: vessel.AsyncVesselResource
    video: video.AsyncVideoResource
    weather_data: weather_data.AsyncWeatherDataResource
    weather_report: weather_report.AsyncWeatherReportResource
    gnss_observations: gnss_observations.AsyncGnssObservationsResource
    gnss_raw_if: gnss_raw_if.AsyncGnssRawIfResource
    iono_observations: iono_observations.AsyncIonoObservationsResource
    report_and_activities: report_and_activities.AsyncReportAndActivitiesResource
    secure_messaging: secure_messaging.AsyncSecureMessagingResource
    scs: scs.AsyncScsResource
    scs_views: scs_views.AsyncScsViewsResource
    with_raw_response: AsyncUnifieddatalibraryWithRawResponse
    with_streaming_response: AsyncUnifieddatalibraryWithStreamedResponse

    # client options
    password: str | None
    username: str | None
    access_token: str | None

    def __init__(
        self,
        *,
        password: str | None = None,
        username: str | None = None,
        access_token: str | None = None,
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
        - `access_token` from `UDL_ACCESS_TOKEN`
        """
        if password is None:
            password = os.environ.get("UDL_AUTH_PASSWORD")
        self.password = password

        if username is None:
            username = os.environ.get("UDL_AUTH_USERNAME")
        self.username = username

        if access_token is None:
            access_token = os.environ.get("UDL_ACCESS_TOKEN")
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("UNIFIEDDATALIBRARY_BASE_URL")
        self._base_url_overridden = base_url is not None
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
        self.air_operations = air_operations.AsyncAirOperationsResource(self)
        self.air_transport_missions = air_transport_missions.AsyncAirTransportMissionsResource(self)
        self.aircraft = aircraft.AsyncAircraftResource(self)
        self.aircraft_sorties = aircraft_sorties.AsyncAircraftSortiesResource(self)
        self.aircraft_status_remarks = aircraft_status_remarks.AsyncAircraftStatusRemarksResource(self)
        self.aircraft_statuses = aircraft_statuses.AsyncAircraftStatusesResource(self)
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResource(self)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResource(self)
        self.airfields = airfields.AsyncAirfieldsResource(self)
        self.airfield_slot_consumptions = airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResource(self)
        self.airload_plans = airload_plans.AsyncAirloadPlansResource(self)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResource(self)
        self.ais = ais.AsyncAIsResource(self)
        self.ais_objects = ais_objects.AsyncAIsObjectsResource(self)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResource(self)
        self.antennas = antennas.AsyncAntennasResource(self)
        self.attitude_data = attitude_data.AsyncAttitudeDataResource(self)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResource(self)
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
        self.aviation_risk_management = aviation_risk_management.AsyncAviationRiskManagementResource(self)
        self.dropzone = dropzone.AsyncDropzoneResource(self)
        self.emitter_geolocation = emitter_geolocation.AsyncEmitterGeolocationResource(self)
        self.feature_assessment = feature_assessment.AsyncFeatureAssessmentResource(self)
        self.global_atmospheric_model = global_atmospheric_model.AsyncGlobalAtmosphericModelResource(self)
        self.route_stats = route_stats.AsyncRouteStatsResource(self)
        self.countries = countries.AsyncCountriesResource(self)
        self.crew = crew.AsyncCrewResource(self)
        self.diff_of_arrival = diff_of_arrival.AsyncDiffOfArrivalResource(self)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResource(self)
        self.drift_history = drift_history.AsyncDriftHistoryResource(self)
        self.ecp_sdr = ecp_sdr.AsyncEcpSdrResource(self)
        self.effect_requests = effect_requests.AsyncEffectRequestsResource(self)
        self.effect_responses = effect_responses.AsyncEffectResponsesResource(self)
        self.elsets = elsets.AsyncElsetsResource(self)
        self.engine_details = engine_details.AsyncEngineDetailsResource(self)
        self.engines = engines.AsyncEnginesResource(self)
        self.entities = entities.AsyncEntitiesResource(self)
        self.eop = eop.AsyncEopResource(self)
        self.ephemeris = ephemeris.AsyncEphemerisResource(self)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResource(self)
        self.equipment = equipment.AsyncEquipmentResource(self)
        self.equipment_remarks = equipment_remarks.AsyncEquipmentRemarksResource(self)
        self.evac = evac.AsyncEvacResource(self)
        self.event_evolution = event_evolution.AsyncEventEvolutionResource(self)
        self.flightplan = flightplan.AsyncFlightplanResource(self)
        self.geo_status = geo_status.AsyncGeoStatusResource(self)
        self.gnss_observationset = gnss_observationset.AsyncGnssObservationsetResource(self)
        self.ground_imagery = ground_imagery.AsyncGroundImageryResource(self)
        self.h3_geo = h3_geo.AsyncH3GeoResource(self)
        self.h3_geo_hex_cell = h3_geo_hex_cell.AsyncH3GeoHexCellResource(self)
        self.hazard = hazard.AsyncHazardResource(self)
        self.ir = ir.AsyncIrResource(self)
        self.isr_collections = isr_collections.AsyncIsrCollectionsResource(self)
        self.item = item.AsyncItemResource(self)
        self.item_trackings = item_trackings.AsyncItemTrackingsResource(self)
        self.launch_detection = launch_detection.AsyncLaunchDetectionResource(self)
        self.launch_event = launch_event.AsyncLaunchEventResource(self)
        self.launch_site = launch_site.AsyncLaunchSiteResource(self)
        self.launch_site_details = launch_site_details.AsyncLaunchSiteDetailsResource(self)
        self.launch_vehicle = launch_vehicle.AsyncLaunchVehicleResource(self)
        self.launch_vehicle_details = launch_vehicle_details.AsyncLaunchVehicleDetailsResource(self)
        self.link_status = link_status.AsyncLinkStatusResource(self)
        self.location = location.AsyncLocationResource(self)
        self.logistics_support = logistics_support.AsyncLogisticsSupportResource(self)
        self.maneuvers = maneuvers.AsyncManeuversResource(self)
        self.manifold = manifold.AsyncManifoldResource(self)
        self.manifoldelset = manifoldelset.AsyncManifoldelsetResource(self)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResource(self)
        self.mission_assignment = mission_assignment.AsyncMissionAssignmentResource(self)
        self.mti = mti.AsyncMtiResource(self)
        self.navigation = navigation.AsyncNavigationResource(self)
        self.navigational_obstruction = navigational_obstruction.AsyncNavigationalObstructionResource(self)
        self.notification = notification.AsyncNotificationResource(self)
        self.object_of_interest = object_of_interest.AsyncObjectOfInterestResource(self)
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
        self.personnelrecovery = personnelrecovery.AsyncPersonnelrecoveryResource(self)
        self.poi = poi.AsyncPoiResource(self)
        self.port = port.AsyncPortResource(self)
        self.rf_band = rf_band.AsyncRfBandResource(self)
        self.rf_band_type = rf_band_type.AsyncRfBandTypeResource(self)
        self.rf_emitter = rf_emitter.AsyncRfEmitterResource(self)
        self.rf_emitter_details = rf_emitter_details.AsyncRfEmitterDetailsResource(self)
        self.sar_observation = sar_observation.AsyncSarObservationResource(self)
        self.scientific = scientific.AsyncScientificResource(self)
        self.sensor = sensor.AsyncSensorResource(self)
        self.sensor_maintenance = sensor_maintenance.AsyncSensorMaintenanceResource(self)
        self.sensor_observation_type = sensor_observation_type.AsyncSensorObservationTypeResource(self)
        self.sensor_plan = sensor_plan.AsyncSensorPlanResource(self)
        self.sensor_type = sensor_type.AsyncSensorTypeResource(self)
        self.sera_data_comm_details = sera_data_comm_details.AsyncSeraDataCommDetailsResource(self)
        self.sera_data_early_warning = sera_data_early_warning.AsyncSeraDataEarlyWarningResource(self)
        self.sera_data_navigation = sera_data_navigation.AsyncSeraDataNavigationResource(self)
        self.seradata_optical_payload = seradata_optical_payload.AsyncSeradataOpticalPayloadResource(self)
        self.seradata_radar_payload = seradata_radar_payload.AsyncSeradataRadarPayloadResource(self)
        self.seradata_sigint_payload = seradata_sigint_payload.AsyncSeradataSigintPayloadResource(self)
        self.seradata_spacecraft_details = seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResource(self)
        self.sgi = sgi.AsyncSgiResource(self)
        self.sigact = sigact.AsyncSigactResource(self)
        self.site = site.AsyncSiteResource(self)
        self.site_remark = site_remark.AsyncSiteRemarkResource(self)
        self.site_status = site_status.AsyncSiteStatusResource(self)
        self.sky_imagery = sky_imagery.AsyncSkyImageryResource(self)
        self.soi_observation_set = soi_observation_set.AsyncSoiObservationSetResource(self)
        self.solar_array = solar_array.AsyncSolarArrayResource(self)
        self.solar_array_details = solar_array_details.AsyncSolarArrayDetailsResource(self)
        self.sortie_ppr = sortie_ppr.AsyncSortiePprResource(self)
        self.space_env_observation = space_env_observation.AsyncSpaceEnvObservationResource(self)
        self.stage = stage.AsyncStageResource(self)
        self.star_catalog = star_catalog.AsyncStarCatalogResource(self)
        self.state_vector = state_vector.AsyncStateVectorResource(self)
        self.status = status.AsyncStatusResource(self)
        self.substatus = substatus.AsyncSubstatusResource(self)
        self.supporting_data = supporting_data.AsyncSupportingDataResource(self)
        self.surface = surface.AsyncSurfaceResource(self)
        self.surface_obstruction = surface_obstruction.AsyncSurfaceObstructionResource(self)
        self.swir = swir.AsyncSwirResource(self)
        self.tai_utc = tai_utc.AsyncTaiUtcResource(self)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResource(self)
        self.track = track.AsyncTrackResource(self)
        self.track_details = track_details.AsyncTrackDetailsResource(self)
        self.track_route = track_route.AsyncTrackRouteResource(self)
        self.transponder = transponder.AsyncTransponderResource(self)
        self.vessel = vessel.AsyncVesselResource(self)
        self.video = video.AsyncVideoResource(self)
        self.weather_data = weather_data.AsyncWeatherDataResource(self)
        self.weather_report = weather_report.AsyncWeatherReportResource(self)
        self.gnss_observations = gnss_observations.AsyncGnssObservationsResource(self)
        self.gnss_raw_if = gnss_raw_if.AsyncGnssRawIfResource(self)
        self.iono_observations = iono_observations.AsyncIonoObservationsResource(self)
        self.report_and_activities = report_and_activities.AsyncReportAndActivitiesResource(self)
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
        return {**self._basic_auth, **self._bearer_auth}

    @property
    def _basic_auth(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.username and self.password and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.access_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either username, password or access_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        password: str | None = None,
        username: str | None = None,
        access_token: str | None = None,
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
        client = self.__class__(
            password=password or self.password,
            username=username or self.username,
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

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
        self.air_operations = air_operations.AirOperationsResourceWithRawResponse(client.air_operations)
        self.air_transport_missions = air_transport_missions.AirTransportMissionsResourceWithRawResponse(
            client.air_transport_missions
        )
        self.aircraft = aircraft.AircraftResourceWithRawResponse(client.aircraft)
        self.aircraft_sorties = aircraft_sorties.AircraftSortiesResourceWithRawResponse(client.aircraft_sorties)
        self.aircraft_status_remarks = aircraft_status_remarks.AircraftStatusRemarksResourceWithRawResponse(
            client.aircraft_status_remarks
        )
        self.aircraft_statuses = aircraft_statuses.AircraftStatusesResourceWithRawResponse(client.aircraft_statuses)
        self.airfield_slots = airfield_slots.AirfieldSlotsResourceWithRawResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AirfieldStatusResourceWithRawResponse(client.airfield_status)
        self.airfields = airfields.AirfieldsResourceWithRawResponse(client.airfields)
        self.airfield_slot_consumptions = airfield_slot_consumptions.AirfieldSlotConsumptionsResourceWithRawResponse(
            client.airfield_slot_consumptions
        )
        self.airload_plans = airload_plans.AirloadPlansResourceWithRawResponse(client.airload_plans)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResourceWithRawResponse(
            client.airspace_control_orders
        )
        self.ais = ais.AIsResourceWithRawResponse(client.ais)
        self.ais_objects = ais_objects.AIsObjectsResourceWithRawResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResourceWithRawResponse(client.analytic_imagery)
        self.antennas = antennas.AntennasResourceWithRawResponse(client.antennas)
        self.attitude_data = attitude_data.AttitudeDataResourceWithRawResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AttitudeSetsResourceWithRawResponse(client.attitude_sets)
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
        self.aviation_risk_management = aviation_risk_management.AviationRiskManagementResourceWithRawResponse(
            client.aviation_risk_management
        )
        self.dropzone = dropzone.DropzoneResourceWithRawResponse(client.dropzone)
        self.emitter_geolocation = emitter_geolocation.EmitterGeolocationResourceWithRawResponse(
            client.emitter_geolocation
        )
        self.feature_assessment = feature_assessment.FeatureAssessmentResourceWithRawResponse(client.feature_assessment)
        self.global_atmospheric_model = global_atmospheric_model.GlobalAtmosphericModelResourceWithRawResponse(
            client.global_atmospheric_model
        )
        self.route_stats = route_stats.RouteStatsResourceWithRawResponse(client.route_stats)
        self.countries = countries.CountriesResourceWithRawResponse(client.countries)
        self.crew = crew.CrewResourceWithRawResponse(client.crew)
        self.diff_of_arrival = diff_of_arrival.DiffOfArrivalResourceWithRawResponse(client.diff_of_arrival)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResourceWithRawResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.DriftHistoryResourceWithRawResponse(client.drift_history)
        self.ecp_sdr = ecp_sdr.EcpSdrResourceWithRawResponse(client.ecp_sdr)
        self.effect_requests = effect_requests.EffectRequestsResourceWithRawResponse(client.effect_requests)
        self.effect_responses = effect_responses.EffectResponsesResourceWithRawResponse(client.effect_responses)
        self.elsets = elsets.ElsetsResourceWithRawResponse(client.elsets)
        self.engine_details = engine_details.EngineDetailsResourceWithRawResponse(client.engine_details)
        self.engines = engines.EnginesResourceWithRawResponse(client.engines)
        self.entities = entities.EntitiesResourceWithRawResponse(client.entities)
        self.eop = eop.EopResourceWithRawResponse(client.eop)
        self.ephemeris = ephemeris.EphemerisResourceWithRawResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResourceWithRawResponse(client.ephemeris_sets)
        self.equipment = equipment.EquipmentResourceWithRawResponse(client.equipment)
        self.equipment_remarks = equipment_remarks.EquipmentRemarksResourceWithRawResponse(client.equipment_remarks)
        self.evac = evac.EvacResourceWithRawResponse(client.evac)
        self.event_evolution = event_evolution.EventEvolutionResourceWithRawResponse(client.event_evolution)
        self.flightplan = flightplan.FlightplanResourceWithRawResponse(client.flightplan)
        self.geo_status = geo_status.GeoStatusResourceWithRawResponse(client.geo_status)
        self.gnss_observationset = gnss_observationset.GnssObservationsetResourceWithRawResponse(
            client.gnss_observationset
        )
        self.ground_imagery = ground_imagery.GroundImageryResourceWithRawResponse(client.ground_imagery)
        self.h3_geo = h3_geo.H3GeoResourceWithRawResponse(client.h3_geo)
        self.h3_geo_hex_cell = h3_geo_hex_cell.H3GeoHexCellResourceWithRawResponse(client.h3_geo_hex_cell)
        self.hazard = hazard.HazardResourceWithRawResponse(client.hazard)
        self.ir = ir.IrResourceWithRawResponse(client.ir)
        self.isr_collections = isr_collections.IsrCollectionsResourceWithRawResponse(client.isr_collections)
        self.item = item.ItemResourceWithRawResponse(client.item)
        self.item_trackings = item_trackings.ItemTrackingsResourceWithRawResponse(client.item_trackings)
        self.launch_detection = launch_detection.LaunchDetectionResourceWithRawResponse(client.launch_detection)
        self.launch_event = launch_event.LaunchEventResourceWithRawResponse(client.launch_event)
        self.launch_site = launch_site.LaunchSiteResourceWithRawResponse(client.launch_site)
        self.launch_site_details = launch_site_details.LaunchSiteDetailsResourceWithRawResponse(
            client.launch_site_details
        )
        self.launch_vehicle = launch_vehicle.LaunchVehicleResourceWithRawResponse(client.launch_vehicle)
        self.launch_vehicle_details = launch_vehicle_details.LaunchVehicleDetailsResourceWithRawResponse(
            client.launch_vehicle_details
        )
        self.link_status = link_status.LinkStatusResourceWithRawResponse(client.link_status)
        self.location = location.LocationResourceWithRawResponse(client.location)
        self.logistics_support = logistics_support.LogisticsSupportResourceWithRawResponse(client.logistics_support)
        self.maneuvers = maneuvers.ManeuversResourceWithRawResponse(client.maneuvers)
        self.manifold = manifold.ManifoldResourceWithRawResponse(client.manifold)
        self.manifoldelset = manifoldelset.ManifoldelsetResourceWithRawResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.MissileTracksResourceWithRawResponse(client.missile_tracks)
        self.mission_assignment = mission_assignment.MissionAssignmentResourceWithRawResponse(client.mission_assignment)
        self.mti = mti.MtiResourceWithRawResponse(client.mti)
        self.navigation = navigation.NavigationResourceWithRawResponse(client.navigation)
        self.navigational_obstruction = navigational_obstruction.NavigationalObstructionResourceWithRawResponse(
            client.navigational_obstruction
        )
        self.notification = notification.NotificationResourceWithRawResponse(client.notification)
        self.object_of_interest = object_of_interest.ObjectOfInterestResourceWithRawResponse(client.object_of_interest)
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
        self.personnelrecovery = personnelrecovery.PersonnelrecoveryResourceWithRawResponse(client.personnelrecovery)
        self.poi = poi.PoiResourceWithRawResponse(client.poi)
        self.port = port.PortResourceWithRawResponse(client.port)
        self.rf_band = rf_band.RfBandResourceWithRawResponse(client.rf_band)
        self.rf_band_type = rf_band_type.RfBandTypeResourceWithRawResponse(client.rf_band_type)
        self.rf_emitter = rf_emitter.RfEmitterResourceWithRawResponse(client.rf_emitter)
        self.rf_emitter_details = rf_emitter_details.RfEmitterDetailsResourceWithRawResponse(client.rf_emitter_details)
        self.sar_observation = sar_observation.SarObservationResourceWithRawResponse(client.sar_observation)
        self.scientific = scientific.ScientificResourceWithRawResponse(client.scientific)
        self.sensor = sensor.SensorResourceWithRawResponse(client.sensor)
        self.sensor_maintenance = sensor_maintenance.SensorMaintenanceResourceWithRawResponse(client.sensor_maintenance)
        self.sensor_observation_type = sensor_observation_type.SensorObservationTypeResourceWithRawResponse(
            client.sensor_observation_type
        )
        self.sensor_plan = sensor_plan.SensorPlanResourceWithRawResponse(client.sensor_plan)
        self.sensor_type = sensor_type.SensorTypeResourceWithRawResponse(client.sensor_type)
        self.sera_data_comm_details = sera_data_comm_details.SeraDataCommDetailsResourceWithRawResponse(
            client.sera_data_comm_details
        )
        self.sera_data_early_warning = sera_data_early_warning.SeraDataEarlyWarningResourceWithRawResponse(
            client.sera_data_early_warning
        )
        self.sera_data_navigation = sera_data_navigation.SeraDataNavigationResourceWithRawResponse(
            client.sera_data_navigation
        )
        self.seradata_optical_payload = seradata_optical_payload.SeradataOpticalPayloadResourceWithRawResponse(
            client.seradata_optical_payload
        )
        self.seradata_radar_payload = seradata_radar_payload.SeradataRadarPayloadResourceWithRawResponse(
            client.seradata_radar_payload
        )
        self.seradata_sigint_payload = seradata_sigint_payload.SeradataSigintPayloadResourceWithRawResponse(
            client.seradata_sigint_payload
        )
        self.seradata_spacecraft_details = seradata_spacecraft_details.SeradataSpacecraftDetailsResourceWithRawResponse(
            client.seradata_spacecraft_details
        )
        self.sgi = sgi.SgiResourceWithRawResponse(client.sgi)
        self.sigact = sigact.SigactResourceWithRawResponse(client.sigact)
        self.site = site.SiteResourceWithRawResponse(client.site)
        self.site_remark = site_remark.SiteRemarkResourceWithRawResponse(client.site_remark)
        self.site_status = site_status.SiteStatusResourceWithRawResponse(client.site_status)
        self.sky_imagery = sky_imagery.SkyImageryResourceWithRawResponse(client.sky_imagery)
        self.soi_observation_set = soi_observation_set.SoiObservationSetResourceWithRawResponse(
            client.soi_observation_set
        )
        self.solar_array = solar_array.SolarArrayResourceWithRawResponse(client.solar_array)
        self.solar_array_details = solar_array_details.SolarArrayDetailsResourceWithRawResponse(
            client.solar_array_details
        )
        self.sortie_ppr = sortie_ppr.SortiePprResourceWithRawResponse(client.sortie_ppr)
        self.space_env_observation = space_env_observation.SpaceEnvObservationResourceWithRawResponse(
            client.space_env_observation
        )
        self.stage = stage.StageResourceWithRawResponse(client.stage)
        self.star_catalog = star_catalog.StarCatalogResourceWithRawResponse(client.star_catalog)
        self.state_vector = state_vector.StateVectorResourceWithRawResponse(client.state_vector)
        self.status = status.StatusResourceWithRawResponse(client.status)
        self.substatus = substatus.SubstatusResourceWithRawResponse(client.substatus)
        self.supporting_data = supporting_data.SupportingDataResourceWithRawResponse(client.supporting_data)
        self.surface = surface.SurfaceResourceWithRawResponse(client.surface)
        self.surface_obstruction = surface_obstruction.SurfaceObstructionResourceWithRawResponse(
            client.surface_obstruction
        )
        self.swir = swir.SwirResourceWithRawResponse(client.swir)
        self.tai_utc = tai_utc.TaiUtcResourceWithRawResponse(client.tai_utc)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResourceWithRawResponse(client.tdoa_fdoa)
        self.track = track.TrackResourceWithRawResponse(client.track)
        self.track_details = track_details.TrackDetailsResourceWithRawResponse(client.track_details)
        self.track_route = track_route.TrackRouteResourceWithRawResponse(client.track_route)
        self.transponder = transponder.TransponderResourceWithRawResponse(client.transponder)
        self.vessel = vessel.VesselResourceWithRawResponse(client.vessel)
        self.video = video.VideoResourceWithRawResponse(client.video)
        self.weather_data = weather_data.WeatherDataResourceWithRawResponse(client.weather_data)
        self.weather_report = weather_report.WeatherReportResourceWithRawResponse(client.weather_report)
        self.gnss_observations = gnss_observations.GnssObservationsResourceWithRawResponse(client.gnss_observations)
        self.gnss_raw_if = gnss_raw_if.GnssRawIfResourceWithRawResponse(client.gnss_raw_if)
        self.iono_observations = iono_observations.IonoObservationsResourceWithRawResponse(client.iono_observations)
        self.report_and_activities = report_and_activities.ReportAndActivitiesResourceWithRawResponse(
            client.report_and_activities
        )
        self.secure_messaging = secure_messaging.SecureMessagingResourceWithRawResponse(client.secure_messaging)
        self.scs = scs.ScsResourceWithRawResponse(client.scs)
        self.scs_views = scs_views.ScsViewsResourceWithRawResponse(client.scs_views)


class AsyncUnifieddatalibraryWithRawResponse:
    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self.air_events = air_events.AsyncAirEventsResourceWithRawResponse(client.air_events)
        self.air_operations = air_operations.AsyncAirOperationsResourceWithRawResponse(client.air_operations)
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
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResourceWithRawResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResourceWithRawResponse(client.airfield_status)
        self.airfields = airfields.AsyncAirfieldsResourceWithRawResponse(client.airfields)
        self.airfield_slot_consumptions = (
            airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResourceWithRawResponse(
                client.airfield_slot_consumptions
            )
        )
        self.airload_plans = airload_plans.AsyncAirloadPlansResourceWithRawResponse(client.airload_plans)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResourceWithRawResponse(
            client.airspace_control_orders
        )
        self.ais = ais.AsyncAIsResourceWithRawResponse(client.ais)
        self.ais_objects = ais_objects.AsyncAIsObjectsResourceWithRawResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResourceWithRawResponse(client.analytic_imagery)
        self.antennas = antennas.AsyncAntennasResourceWithRawResponse(client.antennas)
        self.attitude_data = attitude_data.AsyncAttitudeDataResourceWithRawResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResourceWithRawResponse(client.attitude_sets)
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
        self.aviation_risk_management = aviation_risk_management.AsyncAviationRiskManagementResourceWithRawResponse(
            client.aviation_risk_management
        )
        self.dropzone = dropzone.AsyncDropzoneResourceWithRawResponse(client.dropzone)
        self.emitter_geolocation = emitter_geolocation.AsyncEmitterGeolocationResourceWithRawResponse(
            client.emitter_geolocation
        )
        self.feature_assessment = feature_assessment.AsyncFeatureAssessmentResourceWithRawResponse(
            client.feature_assessment
        )
        self.global_atmospheric_model = global_atmospheric_model.AsyncGlobalAtmosphericModelResourceWithRawResponse(
            client.global_atmospheric_model
        )
        self.route_stats = route_stats.AsyncRouteStatsResourceWithRawResponse(client.route_stats)
        self.countries = countries.AsyncCountriesResourceWithRawResponse(client.countries)
        self.crew = crew.AsyncCrewResourceWithRawResponse(client.crew)
        self.diff_of_arrival = diff_of_arrival.AsyncDiffOfArrivalResourceWithRawResponse(client.diff_of_arrival)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResourceWithRawResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.AsyncDriftHistoryResourceWithRawResponse(client.drift_history)
        self.ecp_sdr = ecp_sdr.AsyncEcpSdrResourceWithRawResponse(client.ecp_sdr)
        self.effect_requests = effect_requests.AsyncEffectRequestsResourceWithRawResponse(client.effect_requests)
        self.effect_responses = effect_responses.AsyncEffectResponsesResourceWithRawResponse(client.effect_responses)
        self.elsets = elsets.AsyncElsetsResourceWithRawResponse(client.elsets)
        self.engine_details = engine_details.AsyncEngineDetailsResourceWithRawResponse(client.engine_details)
        self.engines = engines.AsyncEnginesResourceWithRawResponse(client.engines)
        self.entities = entities.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.eop = eop.AsyncEopResourceWithRawResponse(client.eop)
        self.ephemeris = ephemeris.AsyncEphemerisResourceWithRawResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResourceWithRawResponse(client.ephemeris_sets)
        self.equipment = equipment.AsyncEquipmentResourceWithRawResponse(client.equipment)
        self.equipment_remarks = equipment_remarks.AsyncEquipmentRemarksResourceWithRawResponse(
            client.equipment_remarks
        )
        self.evac = evac.AsyncEvacResourceWithRawResponse(client.evac)
        self.event_evolution = event_evolution.AsyncEventEvolutionResourceWithRawResponse(client.event_evolution)
        self.flightplan = flightplan.AsyncFlightplanResourceWithRawResponse(client.flightplan)
        self.geo_status = geo_status.AsyncGeoStatusResourceWithRawResponse(client.geo_status)
        self.gnss_observationset = gnss_observationset.AsyncGnssObservationsetResourceWithRawResponse(
            client.gnss_observationset
        )
        self.ground_imagery = ground_imagery.AsyncGroundImageryResourceWithRawResponse(client.ground_imagery)
        self.h3_geo = h3_geo.AsyncH3GeoResourceWithRawResponse(client.h3_geo)
        self.h3_geo_hex_cell = h3_geo_hex_cell.AsyncH3GeoHexCellResourceWithRawResponse(client.h3_geo_hex_cell)
        self.hazard = hazard.AsyncHazardResourceWithRawResponse(client.hazard)
        self.ir = ir.AsyncIrResourceWithRawResponse(client.ir)
        self.isr_collections = isr_collections.AsyncIsrCollectionsResourceWithRawResponse(client.isr_collections)
        self.item = item.AsyncItemResourceWithRawResponse(client.item)
        self.item_trackings = item_trackings.AsyncItemTrackingsResourceWithRawResponse(client.item_trackings)
        self.launch_detection = launch_detection.AsyncLaunchDetectionResourceWithRawResponse(client.launch_detection)
        self.launch_event = launch_event.AsyncLaunchEventResourceWithRawResponse(client.launch_event)
        self.launch_site = launch_site.AsyncLaunchSiteResourceWithRawResponse(client.launch_site)
        self.launch_site_details = launch_site_details.AsyncLaunchSiteDetailsResourceWithRawResponse(
            client.launch_site_details
        )
        self.launch_vehicle = launch_vehicle.AsyncLaunchVehicleResourceWithRawResponse(client.launch_vehicle)
        self.launch_vehicle_details = launch_vehicle_details.AsyncLaunchVehicleDetailsResourceWithRawResponse(
            client.launch_vehicle_details
        )
        self.link_status = link_status.AsyncLinkStatusResourceWithRawResponse(client.link_status)
        self.location = location.AsyncLocationResourceWithRawResponse(client.location)
        self.logistics_support = logistics_support.AsyncLogisticsSupportResourceWithRawResponse(
            client.logistics_support
        )
        self.maneuvers = maneuvers.AsyncManeuversResourceWithRawResponse(client.maneuvers)
        self.manifold = manifold.AsyncManifoldResourceWithRawResponse(client.manifold)
        self.manifoldelset = manifoldelset.AsyncManifoldelsetResourceWithRawResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResourceWithRawResponse(client.missile_tracks)
        self.mission_assignment = mission_assignment.AsyncMissionAssignmentResourceWithRawResponse(
            client.mission_assignment
        )
        self.mti = mti.AsyncMtiResourceWithRawResponse(client.mti)
        self.navigation = navigation.AsyncNavigationResourceWithRawResponse(client.navigation)
        self.navigational_obstruction = navigational_obstruction.AsyncNavigationalObstructionResourceWithRawResponse(
            client.navigational_obstruction
        )
        self.notification = notification.AsyncNotificationResourceWithRawResponse(client.notification)
        self.object_of_interest = object_of_interest.AsyncObjectOfInterestResourceWithRawResponse(
            client.object_of_interest
        )
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
        self.personnelrecovery = personnelrecovery.AsyncPersonnelrecoveryResourceWithRawResponse(
            client.personnelrecovery
        )
        self.poi = poi.AsyncPoiResourceWithRawResponse(client.poi)
        self.port = port.AsyncPortResourceWithRawResponse(client.port)
        self.rf_band = rf_band.AsyncRfBandResourceWithRawResponse(client.rf_band)
        self.rf_band_type = rf_band_type.AsyncRfBandTypeResourceWithRawResponse(client.rf_band_type)
        self.rf_emitter = rf_emitter.AsyncRfEmitterResourceWithRawResponse(client.rf_emitter)
        self.rf_emitter_details = rf_emitter_details.AsyncRfEmitterDetailsResourceWithRawResponse(
            client.rf_emitter_details
        )
        self.sar_observation = sar_observation.AsyncSarObservationResourceWithRawResponse(client.sar_observation)
        self.scientific = scientific.AsyncScientificResourceWithRawResponse(client.scientific)
        self.sensor = sensor.AsyncSensorResourceWithRawResponse(client.sensor)
        self.sensor_maintenance = sensor_maintenance.AsyncSensorMaintenanceResourceWithRawResponse(
            client.sensor_maintenance
        )
        self.sensor_observation_type = sensor_observation_type.AsyncSensorObservationTypeResourceWithRawResponse(
            client.sensor_observation_type
        )
        self.sensor_plan = sensor_plan.AsyncSensorPlanResourceWithRawResponse(client.sensor_plan)
        self.sensor_type = sensor_type.AsyncSensorTypeResourceWithRawResponse(client.sensor_type)
        self.sera_data_comm_details = sera_data_comm_details.AsyncSeraDataCommDetailsResourceWithRawResponse(
            client.sera_data_comm_details
        )
        self.sera_data_early_warning = sera_data_early_warning.AsyncSeraDataEarlyWarningResourceWithRawResponse(
            client.sera_data_early_warning
        )
        self.sera_data_navigation = sera_data_navigation.AsyncSeraDataNavigationResourceWithRawResponse(
            client.sera_data_navigation
        )
        self.seradata_optical_payload = seradata_optical_payload.AsyncSeradataOpticalPayloadResourceWithRawResponse(
            client.seradata_optical_payload
        )
        self.seradata_radar_payload = seradata_radar_payload.AsyncSeradataRadarPayloadResourceWithRawResponse(
            client.seradata_radar_payload
        )
        self.seradata_sigint_payload = seradata_sigint_payload.AsyncSeradataSigintPayloadResourceWithRawResponse(
            client.seradata_sigint_payload
        )
        self.seradata_spacecraft_details = (
            seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResourceWithRawResponse(
                client.seradata_spacecraft_details
            )
        )
        self.sgi = sgi.AsyncSgiResourceWithRawResponse(client.sgi)
        self.sigact = sigact.AsyncSigactResourceWithRawResponse(client.sigact)
        self.site = site.AsyncSiteResourceWithRawResponse(client.site)
        self.site_remark = site_remark.AsyncSiteRemarkResourceWithRawResponse(client.site_remark)
        self.site_status = site_status.AsyncSiteStatusResourceWithRawResponse(client.site_status)
        self.sky_imagery = sky_imagery.AsyncSkyImageryResourceWithRawResponse(client.sky_imagery)
        self.soi_observation_set = soi_observation_set.AsyncSoiObservationSetResourceWithRawResponse(
            client.soi_observation_set
        )
        self.solar_array = solar_array.AsyncSolarArrayResourceWithRawResponse(client.solar_array)
        self.solar_array_details = solar_array_details.AsyncSolarArrayDetailsResourceWithRawResponse(
            client.solar_array_details
        )
        self.sortie_ppr = sortie_ppr.AsyncSortiePprResourceWithRawResponse(client.sortie_ppr)
        self.space_env_observation = space_env_observation.AsyncSpaceEnvObservationResourceWithRawResponse(
            client.space_env_observation
        )
        self.stage = stage.AsyncStageResourceWithRawResponse(client.stage)
        self.star_catalog = star_catalog.AsyncStarCatalogResourceWithRawResponse(client.star_catalog)
        self.state_vector = state_vector.AsyncStateVectorResourceWithRawResponse(client.state_vector)
        self.status = status.AsyncStatusResourceWithRawResponse(client.status)
        self.substatus = substatus.AsyncSubstatusResourceWithRawResponse(client.substatus)
        self.supporting_data = supporting_data.AsyncSupportingDataResourceWithRawResponse(client.supporting_data)
        self.surface = surface.AsyncSurfaceResourceWithRawResponse(client.surface)
        self.surface_obstruction = surface_obstruction.AsyncSurfaceObstructionResourceWithRawResponse(
            client.surface_obstruction
        )
        self.swir = swir.AsyncSwirResourceWithRawResponse(client.swir)
        self.tai_utc = tai_utc.AsyncTaiUtcResourceWithRawResponse(client.tai_utc)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResourceWithRawResponse(client.tdoa_fdoa)
        self.track = track.AsyncTrackResourceWithRawResponse(client.track)
        self.track_details = track_details.AsyncTrackDetailsResourceWithRawResponse(client.track_details)
        self.track_route = track_route.AsyncTrackRouteResourceWithRawResponse(client.track_route)
        self.transponder = transponder.AsyncTransponderResourceWithRawResponse(client.transponder)
        self.vessel = vessel.AsyncVesselResourceWithRawResponse(client.vessel)
        self.video = video.AsyncVideoResourceWithRawResponse(client.video)
        self.weather_data = weather_data.AsyncWeatherDataResourceWithRawResponse(client.weather_data)
        self.weather_report = weather_report.AsyncWeatherReportResourceWithRawResponse(client.weather_report)
        self.gnss_observations = gnss_observations.AsyncGnssObservationsResourceWithRawResponse(
            client.gnss_observations
        )
        self.gnss_raw_if = gnss_raw_if.AsyncGnssRawIfResourceWithRawResponse(client.gnss_raw_if)
        self.iono_observations = iono_observations.AsyncIonoObservationsResourceWithRawResponse(
            client.iono_observations
        )
        self.report_and_activities = report_and_activities.AsyncReportAndActivitiesResourceWithRawResponse(
            client.report_and_activities
        )
        self.secure_messaging = secure_messaging.AsyncSecureMessagingResourceWithRawResponse(client.secure_messaging)
        self.scs = scs.AsyncScsResourceWithRawResponse(client.scs)
        self.scs_views = scs_views.AsyncScsViewsResourceWithRawResponse(client.scs_views)


class UnifieddatalibraryWithStreamedResponse:
    def __init__(self, client: Unifieddatalibrary) -> None:
        self.air_events = air_events.AirEventsResourceWithStreamingResponse(client.air_events)
        self.air_operations = air_operations.AirOperationsResourceWithStreamingResponse(client.air_operations)
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
        self.airfield_slots = airfield_slots.AirfieldSlotsResourceWithStreamingResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AirfieldStatusResourceWithStreamingResponse(client.airfield_status)
        self.airfields = airfields.AirfieldsResourceWithStreamingResponse(client.airfields)
        self.airfield_slot_consumptions = (
            airfield_slot_consumptions.AirfieldSlotConsumptionsResourceWithStreamingResponse(
                client.airfield_slot_consumptions
            )
        )
        self.airload_plans = airload_plans.AirloadPlansResourceWithStreamingResponse(client.airload_plans)
        self.airspace_control_orders = airspace_control_orders.AirspaceControlOrdersResourceWithStreamingResponse(
            client.airspace_control_orders
        )
        self.ais = ais.AIsResourceWithStreamingResponse(client.ais)
        self.ais_objects = ais_objects.AIsObjectsResourceWithStreamingResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AnalyticImageryResourceWithStreamingResponse(client.analytic_imagery)
        self.antennas = antennas.AntennasResourceWithStreamingResponse(client.antennas)
        self.attitude_data = attitude_data.AttitudeDataResourceWithStreamingResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AttitudeSetsResourceWithStreamingResponse(client.attitude_sets)
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
        self.aviation_risk_management = aviation_risk_management.AviationRiskManagementResourceWithStreamingResponse(
            client.aviation_risk_management
        )
        self.dropzone = dropzone.DropzoneResourceWithStreamingResponse(client.dropzone)
        self.emitter_geolocation = emitter_geolocation.EmitterGeolocationResourceWithStreamingResponse(
            client.emitter_geolocation
        )
        self.feature_assessment = feature_assessment.FeatureAssessmentResourceWithStreamingResponse(
            client.feature_assessment
        )
        self.global_atmospheric_model = global_atmospheric_model.GlobalAtmosphericModelResourceWithStreamingResponse(
            client.global_atmospheric_model
        )
        self.route_stats = route_stats.RouteStatsResourceWithStreamingResponse(client.route_stats)
        self.countries = countries.CountriesResourceWithStreamingResponse(client.countries)
        self.crew = crew.CrewResourceWithStreamingResponse(client.crew)
        self.diff_of_arrival = diff_of_arrival.DiffOfArrivalResourceWithStreamingResponse(client.diff_of_arrival)
        self.diplomatic_clearance = diplomatic_clearance.DiplomaticClearanceResourceWithStreamingResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.DriftHistoryResourceWithStreamingResponse(client.drift_history)
        self.ecp_sdr = ecp_sdr.EcpSdrResourceWithStreamingResponse(client.ecp_sdr)
        self.effect_requests = effect_requests.EffectRequestsResourceWithStreamingResponse(client.effect_requests)
        self.effect_responses = effect_responses.EffectResponsesResourceWithStreamingResponse(client.effect_responses)
        self.elsets = elsets.ElsetsResourceWithStreamingResponse(client.elsets)
        self.engine_details = engine_details.EngineDetailsResourceWithStreamingResponse(client.engine_details)
        self.engines = engines.EnginesResourceWithStreamingResponse(client.engines)
        self.entities = entities.EntitiesResourceWithStreamingResponse(client.entities)
        self.eop = eop.EopResourceWithStreamingResponse(client.eop)
        self.ephemeris = ephemeris.EphemerisResourceWithStreamingResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.EphemerisSetsResourceWithStreamingResponse(client.ephemeris_sets)
        self.equipment = equipment.EquipmentResourceWithStreamingResponse(client.equipment)
        self.equipment_remarks = equipment_remarks.EquipmentRemarksResourceWithStreamingResponse(
            client.equipment_remarks
        )
        self.evac = evac.EvacResourceWithStreamingResponse(client.evac)
        self.event_evolution = event_evolution.EventEvolutionResourceWithStreamingResponse(client.event_evolution)
        self.flightplan = flightplan.FlightplanResourceWithStreamingResponse(client.flightplan)
        self.geo_status = geo_status.GeoStatusResourceWithStreamingResponse(client.geo_status)
        self.gnss_observationset = gnss_observationset.GnssObservationsetResourceWithStreamingResponse(
            client.gnss_observationset
        )
        self.ground_imagery = ground_imagery.GroundImageryResourceWithStreamingResponse(client.ground_imagery)
        self.h3_geo = h3_geo.H3GeoResourceWithStreamingResponse(client.h3_geo)
        self.h3_geo_hex_cell = h3_geo_hex_cell.H3GeoHexCellResourceWithStreamingResponse(client.h3_geo_hex_cell)
        self.hazard = hazard.HazardResourceWithStreamingResponse(client.hazard)
        self.ir = ir.IrResourceWithStreamingResponse(client.ir)
        self.isr_collections = isr_collections.IsrCollectionsResourceWithStreamingResponse(client.isr_collections)
        self.item = item.ItemResourceWithStreamingResponse(client.item)
        self.item_trackings = item_trackings.ItemTrackingsResourceWithStreamingResponse(client.item_trackings)
        self.launch_detection = launch_detection.LaunchDetectionResourceWithStreamingResponse(client.launch_detection)
        self.launch_event = launch_event.LaunchEventResourceWithStreamingResponse(client.launch_event)
        self.launch_site = launch_site.LaunchSiteResourceWithStreamingResponse(client.launch_site)
        self.launch_site_details = launch_site_details.LaunchSiteDetailsResourceWithStreamingResponse(
            client.launch_site_details
        )
        self.launch_vehicle = launch_vehicle.LaunchVehicleResourceWithStreamingResponse(client.launch_vehicle)
        self.launch_vehicle_details = launch_vehicle_details.LaunchVehicleDetailsResourceWithStreamingResponse(
            client.launch_vehicle_details
        )
        self.link_status = link_status.LinkStatusResourceWithStreamingResponse(client.link_status)
        self.location = location.LocationResourceWithStreamingResponse(client.location)
        self.logistics_support = logistics_support.LogisticsSupportResourceWithStreamingResponse(
            client.logistics_support
        )
        self.maneuvers = maneuvers.ManeuversResourceWithStreamingResponse(client.maneuvers)
        self.manifold = manifold.ManifoldResourceWithStreamingResponse(client.manifold)
        self.manifoldelset = manifoldelset.ManifoldelsetResourceWithStreamingResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.MissileTracksResourceWithStreamingResponse(client.missile_tracks)
        self.mission_assignment = mission_assignment.MissionAssignmentResourceWithStreamingResponse(
            client.mission_assignment
        )
        self.mti = mti.MtiResourceWithStreamingResponse(client.mti)
        self.navigation = navigation.NavigationResourceWithStreamingResponse(client.navigation)
        self.navigational_obstruction = navigational_obstruction.NavigationalObstructionResourceWithStreamingResponse(
            client.navigational_obstruction
        )
        self.notification = notification.NotificationResourceWithStreamingResponse(client.notification)
        self.object_of_interest = object_of_interest.ObjectOfInterestResourceWithStreamingResponse(
            client.object_of_interest
        )
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
        self.personnelrecovery = personnelrecovery.PersonnelrecoveryResourceWithStreamingResponse(
            client.personnelrecovery
        )
        self.poi = poi.PoiResourceWithStreamingResponse(client.poi)
        self.port = port.PortResourceWithStreamingResponse(client.port)
        self.rf_band = rf_band.RfBandResourceWithStreamingResponse(client.rf_band)
        self.rf_band_type = rf_band_type.RfBandTypeResourceWithStreamingResponse(client.rf_band_type)
        self.rf_emitter = rf_emitter.RfEmitterResourceWithStreamingResponse(client.rf_emitter)
        self.rf_emitter_details = rf_emitter_details.RfEmitterDetailsResourceWithStreamingResponse(
            client.rf_emitter_details
        )
        self.sar_observation = sar_observation.SarObservationResourceWithStreamingResponse(client.sar_observation)
        self.scientific = scientific.ScientificResourceWithStreamingResponse(client.scientific)
        self.sensor = sensor.SensorResourceWithStreamingResponse(client.sensor)
        self.sensor_maintenance = sensor_maintenance.SensorMaintenanceResourceWithStreamingResponse(
            client.sensor_maintenance
        )
        self.sensor_observation_type = sensor_observation_type.SensorObservationTypeResourceWithStreamingResponse(
            client.sensor_observation_type
        )
        self.sensor_plan = sensor_plan.SensorPlanResourceWithStreamingResponse(client.sensor_plan)
        self.sensor_type = sensor_type.SensorTypeResourceWithStreamingResponse(client.sensor_type)
        self.sera_data_comm_details = sera_data_comm_details.SeraDataCommDetailsResourceWithStreamingResponse(
            client.sera_data_comm_details
        )
        self.sera_data_early_warning = sera_data_early_warning.SeraDataEarlyWarningResourceWithStreamingResponse(
            client.sera_data_early_warning
        )
        self.sera_data_navigation = sera_data_navigation.SeraDataNavigationResourceWithStreamingResponse(
            client.sera_data_navigation
        )
        self.seradata_optical_payload = seradata_optical_payload.SeradataOpticalPayloadResourceWithStreamingResponse(
            client.seradata_optical_payload
        )
        self.seradata_radar_payload = seradata_radar_payload.SeradataRadarPayloadResourceWithStreamingResponse(
            client.seradata_radar_payload
        )
        self.seradata_sigint_payload = seradata_sigint_payload.SeradataSigintPayloadResourceWithStreamingResponse(
            client.seradata_sigint_payload
        )
        self.seradata_spacecraft_details = (
            seradata_spacecraft_details.SeradataSpacecraftDetailsResourceWithStreamingResponse(
                client.seradata_spacecraft_details
            )
        )
        self.sgi = sgi.SgiResourceWithStreamingResponse(client.sgi)
        self.sigact = sigact.SigactResourceWithStreamingResponse(client.sigact)
        self.site = site.SiteResourceWithStreamingResponse(client.site)
        self.site_remark = site_remark.SiteRemarkResourceWithStreamingResponse(client.site_remark)
        self.site_status = site_status.SiteStatusResourceWithStreamingResponse(client.site_status)
        self.sky_imagery = sky_imagery.SkyImageryResourceWithStreamingResponse(client.sky_imagery)
        self.soi_observation_set = soi_observation_set.SoiObservationSetResourceWithStreamingResponse(
            client.soi_observation_set
        )
        self.solar_array = solar_array.SolarArrayResourceWithStreamingResponse(client.solar_array)
        self.solar_array_details = solar_array_details.SolarArrayDetailsResourceWithStreamingResponse(
            client.solar_array_details
        )
        self.sortie_ppr = sortie_ppr.SortiePprResourceWithStreamingResponse(client.sortie_ppr)
        self.space_env_observation = space_env_observation.SpaceEnvObservationResourceWithStreamingResponse(
            client.space_env_observation
        )
        self.stage = stage.StageResourceWithStreamingResponse(client.stage)
        self.star_catalog = star_catalog.StarCatalogResourceWithStreamingResponse(client.star_catalog)
        self.state_vector = state_vector.StateVectorResourceWithStreamingResponse(client.state_vector)
        self.status = status.StatusResourceWithStreamingResponse(client.status)
        self.substatus = substatus.SubstatusResourceWithStreamingResponse(client.substatus)
        self.supporting_data = supporting_data.SupportingDataResourceWithStreamingResponse(client.supporting_data)
        self.surface = surface.SurfaceResourceWithStreamingResponse(client.surface)
        self.surface_obstruction = surface_obstruction.SurfaceObstructionResourceWithStreamingResponse(
            client.surface_obstruction
        )
        self.swir = swir.SwirResourceWithStreamingResponse(client.swir)
        self.tai_utc = tai_utc.TaiUtcResourceWithStreamingResponse(client.tai_utc)
        self.tdoa_fdoa = tdoa_fdoa.TdoaFdoaResourceWithStreamingResponse(client.tdoa_fdoa)
        self.track = track.TrackResourceWithStreamingResponse(client.track)
        self.track_details = track_details.TrackDetailsResourceWithStreamingResponse(client.track_details)
        self.track_route = track_route.TrackRouteResourceWithStreamingResponse(client.track_route)
        self.transponder = transponder.TransponderResourceWithStreamingResponse(client.transponder)
        self.vessel = vessel.VesselResourceWithStreamingResponse(client.vessel)
        self.video = video.VideoResourceWithStreamingResponse(client.video)
        self.weather_data = weather_data.WeatherDataResourceWithStreamingResponse(client.weather_data)
        self.weather_report = weather_report.WeatherReportResourceWithStreamingResponse(client.weather_report)
        self.gnss_observations = gnss_observations.GnssObservationsResourceWithStreamingResponse(
            client.gnss_observations
        )
        self.gnss_raw_if = gnss_raw_if.GnssRawIfResourceWithStreamingResponse(client.gnss_raw_if)
        self.iono_observations = iono_observations.IonoObservationsResourceWithStreamingResponse(
            client.iono_observations
        )
        self.report_and_activities = report_and_activities.ReportAndActivitiesResourceWithStreamingResponse(
            client.report_and_activities
        )
        self.secure_messaging = secure_messaging.SecureMessagingResourceWithStreamingResponse(client.secure_messaging)
        self.scs = scs.ScsResourceWithStreamingResponse(client.scs)
        self.scs_views = scs_views.ScsViewsResourceWithStreamingResponse(client.scs_views)


class AsyncUnifieddatalibraryWithStreamedResponse:
    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self.air_events = air_events.AsyncAirEventsResourceWithStreamingResponse(client.air_events)
        self.air_operations = air_operations.AsyncAirOperationsResourceWithStreamingResponse(client.air_operations)
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
        self.airfield_slots = airfield_slots.AsyncAirfieldSlotsResourceWithStreamingResponse(client.airfield_slots)
        self.airfield_status = airfield_status.AsyncAirfieldStatusResourceWithStreamingResponse(client.airfield_status)
        self.airfields = airfields.AsyncAirfieldsResourceWithStreamingResponse(client.airfields)
        self.airfield_slot_consumptions = (
            airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse(
                client.airfield_slot_consumptions
            )
        )
        self.airload_plans = airload_plans.AsyncAirloadPlansResourceWithStreamingResponse(client.airload_plans)
        self.airspace_control_orders = airspace_control_orders.AsyncAirspaceControlOrdersResourceWithStreamingResponse(
            client.airspace_control_orders
        )
        self.ais = ais.AsyncAIsResourceWithStreamingResponse(client.ais)
        self.ais_objects = ais_objects.AsyncAIsObjectsResourceWithStreamingResponse(client.ais_objects)
        self.analytic_imagery = analytic_imagery.AsyncAnalyticImageryResourceWithStreamingResponse(
            client.analytic_imagery
        )
        self.antennas = antennas.AsyncAntennasResourceWithStreamingResponse(client.antennas)
        self.attitude_data = attitude_data.AsyncAttitudeDataResourceWithStreamingResponse(client.attitude_data)
        self.attitude_sets = attitude_sets.AsyncAttitudeSetsResourceWithStreamingResponse(client.attitude_sets)
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
        self.aviation_risk_management = (
            aviation_risk_management.AsyncAviationRiskManagementResourceWithStreamingResponse(
                client.aviation_risk_management
            )
        )
        self.dropzone = dropzone.AsyncDropzoneResourceWithStreamingResponse(client.dropzone)
        self.emitter_geolocation = emitter_geolocation.AsyncEmitterGeolocationResourceWithStreamingResponse(
            client.emitter_geolocation
        )
        self.feature_assessment = feature_assessment.AsyncFeatureAssessmentResourceWithStreamingResponse(
            client.feature_assessment
        )
        self.global_atmospheric_model = (
            global_atmospheric_model.AsyncGlobalAtmosphericModelResourceWithStreamingResponse(
                client.global_atmospheric_model
            )
        )
        self.route_stats = route_stats.AsyncRouteStatsResourceWithStreamingResponse(client.route_stats)
        self.countries = countries.AsyncCountriesResourceWithStreamingResponse(client.countries)
        self.crew = crew.AsyncCrewResourceWithStreamingResponse(client.crew)
        self.diff_of_arrival = diff_of_arrival.AsyncDiffOfArrivalResourceWithStreamingResponse(client.diff_of_arrival)
        self.diplomatic_clearance = diplomatic_clearance.AsyncDiplomaticClearanceResourceWithStreamingResponse(
            client.diplomatic_clearance
        )
        self.drift_history = drift_history.AsyncDriftHistoryResourceWithStreamingResponse(client.drift_history)
        self.ecp_sdr = ecp_sdr.AsyncEcpSdrResourceWithStreamingResponse(client.ecp_sdr)
        self.effect_requests = effect_requests.AsyncEffectRequestsResourceWithStreamingResponse(client.effect_requests)
        self.effect_responses = effect_responses.AsyncEffectResponsesResourceWithStreamingResponse(
            client.effect_responses
        )
        self.elsets = elsets.AsyncElsetsResourceWithStreamingResponse(client.elsets)
        self.engine_details = engine_details.AsyncEngineDetailsResourceWithStreamingResponse(client.engine_details)
        self.engines = engines.AsyncEnginesResourceWithStreamingResponse(client.engines)
        self.entities = entities.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.eop = eop.AsyncEopResourceWithStreamingResponse(client.eop)
        self.ephemeris = ephemeris.AsyncEphemerisResourceWithStreamingResponse(client.ephemeris)
        self.ephemeris_sets = ephemeris_sets.AsyncEphemerisSetsResourceWithStreamingResponse(client.ephemeris_sets)
        self.equipment = equipment.AsyncEquipmentResourceWithStreamingResponse(client.equipment)
        self.equipment_remarks = equipment_remarks.AsyncEquipmentRemarksResourceWithStreamingResponse(
            client.equipment_remarks
        )
        self.evac = evac.AsyncEvacResourceWithStreamingResponse(client.evac)
        self.event_evolution = event_evolution.AsyncEventEvolutionResourceWithStreamingResponse(client.event_evolution)
        self.flightplan = flightplan.AsyncFlightplanResourceWithStreamingResponse(client.flightplan)
        self.geo_status = geo_status.AsyncGeoStatusResourceWithStreamingResponse(client.geo_status)
        self.gnss_observationset = gnss_observationset.AsyncGnssObservationsetResourceWithStreamingResponse(
            client.gnss_observationset
        )
        self.ground_imagery = ground_imagery.AsyncGroundImageryResourceWithStreamingResponse(client.ground_imagery)
        self.h3_geo = h3_geo.AsyncH3GeoResourceWithStreamingResponse(client.h3_geo)
        self.h3_geo_hex_cell = h3_geo_hex_cell.AsyncH3GeoHexCellResourceWithStreamingResponse(client.h3_geo_hex_cell)
        self.hazard = hazard.AsyncHazardResourceWithStreamingResponse(client.hazard)
        self.ir = ir.AsyncIrResourceWithStreamingResponse(client.ir)
        self.isr_collections = isr_collections.AsyncIsrCollectionsResourceWithStreamingResponse(client.isr_collections)
        self.item = item.AsyncItemResourceWithStreamingResponse(client.item)
        self.item_trackings = item_trackings.AsyncItemTrackingsResourceWithStreamingResponse(client.item_trackings)
        self.launch_detection = launch_detection.AsyncLaunchDetectionResourceWithStreamingResponse(
            client.launch_detection
        )
        self.launch_event = launch_event.AsyncLaunchEventResourceWithStreamingResponse(client.launch_event)
        self.launch_site = launch_site.AsyncLaunchSiteResourceWithStreamingResponse(client.launch_site)
        self.launch_site_details = launch_site_details.AsyncLaunchSiteDetailsResourceWithStreamingResponse(
            client.launch_site_details
        )
        self.launch_vehicle = launch_vehicle.AsyncLaunchVehicleResourceWithStreamingResponse(client.launch_vehicle)
        self.launch_vehicle_details = launch_vehicle_details.AsyncLaunchVehicleDetailsResourceWithStreamingResponse(
            client.launch_vehicle_details
        )
        self.link_status = link_status.AsyncLinkStatusResourceWithStreamingResponse(client.link_status)
        self.location = location.AsyncLocationResourceWithStreamingResponse(client.location)
        self.logistics_support = logistics_support.AsyncLogisticsSupportResourceWithStreamingResponse(
            client.logistics_support
        )
        self.maneuvers = maneuvers.AsyncManeuversResourceWithStreamingResponse(client.maneuvers)
        self.manifold = manifold.AsyncManifoldResourceWithStreamingResponse(client.manifold)
        self.manifoldelset = manifoldelset.AsyncManifoldelsetResourceWithStreamingResponse(client.manifoldelset)
        self.missile_tracks = missile_tracks.AsyncMissileTracksResourceWithStreamingResponse(client.missile_tracks)
        self.mission_assignment = mission_assignment.AsyncMissionAssignmentResourceWithStreamingResponse(
            client.mission_assignment
        )
        self.mti = mti.AsyncMtiResourceWithStreamingResponse(client.mti)
        self.navigation = navigation.AsyncNavigationResourceWithStreamingResponse(client.navigation)
        self.navigational_obstruction = (
            navigational_obstruction.AsyncNavigationalObstructionResourceWithStreamingResponse(
                client.navigational_obstruction
            )
        )
        self.notification = notification.AsyncNotificationResourceWithStreamingResponse(client.notification)
        self.object_of_interest = object_of_interest.AsyncObjectOfInterestResourceWithStreamingResponse(
            client.object_of_interest
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
        self.personnelrecovery = personnelrecovery.AsyncPersonnelrecoveryResourceWithStreamingResponse(
            client.personnelrecovery
        )
        self.poi = poi.AsyncPoiResourceWithStreamingResponse(client.poi)
        self.port = port.AsyncPortResourceWithStreamingResponse(client.port)
        self.rf_band = rf_band.AsyncRfBandResourceWithStreamingResponse(client.rf_band)
        self.rf_band_type = rf_band_type.AsyncRfBandTypeResourceWithStreamingResponse(client.rf_band_type)
        self.rf_emitter = rf_emitter.AsyncRfEmitterResourceWithStreamingResponse(client.rf_emitter)
        self.rf_emitter_details = rf_emitter_details.AsyncRfEmitterDetailsResourceWithStreamingResponse(
            client.rf_emitter_details
        )
        self.sar_observation = sar_observation.AsyncSarObservationResourceWithStreamingResponse(client.sar_observation)
        self.scientific = scientific.AsyncScientificResourceWithStreamingResponse(client.scientific)
        self.sensor = sensor.AsyncSensorResourceWithStreamingResponse(client.sensor)
        self.sensor_maintenance = sensor_maintenance.AsyncSensorMaintenanceResourceWithStreamingResponse(
            client.sensor_maintenance
        )
        self.sensor_observation_type = sensor_observation_type.AsyncSensorObservationTypeResourceWithStreamingResponse(
            client.sensor_observation_type
        )
        self.sensor_plan = sensor_plan.AsyncSensorPlanResourceWithStreamingResponse(client.sensor_plan)
        self.sensor_type = sensor_type.AsyncSensorTypeResourceWithStreamingResponse(client.sensor_type)
        self.sera_data_comm_details = sera_data_comm_details.AsyncSeraDataCommDetailsResourceWithStreamingResponse(
            client.sera_data_comm_details
        )
        self.sera_data_early_warning = sera_data_early_warning.AsyncSeraDataEarlyWarningResourceWithStreamingResponse(
            client.sera_data_early_warning
        )
        self.sera_data_navigation = sera_data_navigation.AsyncSeraDataNavigationResourceWithStreamingResponse(
            client.sera_data_navigation
        )
        self.seradata_optical_payload = (
            seradata_optical_payload.AsyncSeradataOpticalPayloadResourceWithStreamingResponse(
                client.seradata_optical_payload
            )
        )
        self.seradata_radar_payload = seradata_radar_payload.AsyncSeradataRadarPayloadResourceWithStreamingResponse(
            client.seradata_radar_payload
        )
        self.seradata_sigint_payload = seradata_sigint_payload.AsyncSeradataSigintPayloadResourceWithStreamingResponse(
            client.seradata_sigint_payload
        )
        self.seradata_spacecraft_details = (
            seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse(
                client.seradata_spacecraft_details
            )
        )
        self.sgi = sgi.AsyncSgiResourceWithStreamingResponse(client.sgi)
        self.sigact = sigact.AsyncSigactResourceWithStreamingResponse(client.sigact)
        self.site = site.AsyncSiteResourceWithStreamingResponse(client.site)
        self.site_remark = site_remark.AsyncSiteRemarkResourceWithStreamingResponse(client.site_remark)
        self.site_status = site_status.AsyncSiteStatusResourceWithStreamingResponse(client.site_status)
        self.sky_imagery = sky_imagery.AsyncSkyImageryResourceWithStreamingResponse(client.sky_imagery)
        self.soi_observation_set = soi_observation_set.AsyncSoiObservationSetResourceWithStreamingResponse(
            client.soi_observation_set
        )
        self.solar_array = solar_array.AsyncSolarArrayResourceWithStreamingResponse(client.solar_array)
        self.solar_array_details = solar_array_details.AsyncSolarArrayDetailsResourceWithStreamingResponse(
            client.solar_array_details
        )
        self.sortie_ppr = sortie_ppr.AsyncSortiePprResourceWithStreamingResponse(client.sortie_ppr)
        self.space_env_observation = space_env_observation.AsyncSpaceEnvObservationResourceWithStreamingResponse(
            client.space_env_observation
        )
        self.stage = stage.AsyncStageResourceWithStreamingResponse(client.stage)
        self.star_catalog = star_catalog.AsyncStarCatalogResourceWithStreamingResponse(client.star_catalog)
        self.state_vector = state_vector.AsyncStateVectorResourceWithStreamingResponse(client.state_vector)
        self.status = status.AsyncStatusResourceWithStreamingResponse(client.status)
        self.substatus = substatus.AsyncSubstatusResourceWithStreamingResponse(client.substatus)
        self.supporting_data = supporting_data.AsyncSupportingDataResourceWithStreamingResponse(client.supporting_data)
        self.surface = surface.AsyncSurfaceResourceWithStreamingResponse(client.surface)
        self.surface_obstruction = surface_obstruction.AsyncSurfaceObstructionResourceWithStreamingResponse(
            client.surface_obstruction
        )
        self.swir = swir.AsyncSwirResourceWithStreamingResponse(client.swir)
        self.tai_utc = tai_utc.AsyncTaiUtcResourceWithStreamingResponse(client.tai_utc)
        self.tdoa_fdoa = tdoa_fdoa.AsyncTdoaFdoaResourceWithStreamingResponse(client.tdoa_fdoa)
        self.track = track.AsyncTrackResourceWithStreamingResponse(client.track)
        self.track_details = track_details.AsyncTrackDetailsResourceWithStreamingResponse(client.track_details)
        self.track_route = track_route.AsyncTrackRouteResourceWithStreamingResponse(client.track_route)
        self.transponder = transponder.AsyncTransponderResourceWithStreamingResponse(client.transponder)
        self.vessel = vessel.AsyncVesselResourceWithStreamingResponse(client.vessel)
        self.video = video.AsyncVideoResourceWithStreamingResponse(client.video)
        self.weather_data = weather_data.AsyncWeatherDataResourceWithStreamingResponse(client.weather_data)
        self.weather_report = weather_report.AsyncWeatherReportResourceWithStreamingResponse(client.weather_report)
        self.gnss_observations = gnss_observations.AsyncGnssObservationsResourceWithStreamingResponse(
            client.gnss_observations
        )
        self.gnss_raw_if = gnss_raw_if.AsyncGnssRawIfResourceWithStreamingResponse(client.gnss_raw_if)
        self.iono_observations = iono_observations.AsyncIonoObservationsResourceWithStreamingResponse(
            client.iono_observations
        )
        self.report_and_activities = report_and_activities.AsyncReportAndActivitiesResourceWithStreamingResponse(
            client.report_and_activities
        )
        self.secure_messaging = secure_messaging.AsyncSecureMessagingResourceWithStreamingResponse(
            client.secure_messaging
        )
        self.scs = scs.AsyncScsResourceWithStreamingResponse(client.scs)
        self.scs_views = scs_views.AsyncScsViewsResourceWithStreamingResponse(client.scs_views)


Client = Unifieddatalibrary

AsyncClient = AsyncUnifieddatalibrary
