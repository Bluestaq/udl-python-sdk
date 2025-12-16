# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        ir,
        ais,
        eop,
        mti,
        poi,
        scs,
        sgi,
        beam,
        comm,
        cots,
        crew,
        evac,
        item,
        port,
        site,
        swir,
        user,
        buses,
        stage,
        track,
        video,
        ecpedr,
        elsets,
        h3_geo,
        hazard,
        sensor,
        sigact,
        status,
        vessel,
        engines,
        onorbit,
        rf_band,
        surface,
        tai_utc,
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
        emireport,
        ephemeris,
        equipment,
        maneuvers,
        substatus,
        tdoa_fdoa,
        air_events,
        flightplan,
        geo_status,
        linkstatus,
        navigation,
        orbittrack,
        rf_emitter,
        scientific,
        sortie_ppr,
        ais_objects,
        gnss_raw_if,
        launch_site,
        link_status,
        onorbitlist,
        route_stats,
        sensor_plan,
        sensor_type,
        site_remark,
        site_status,
        sky_imagery,
        solar_array,
        track_route,
        transponder,
        conjunctions,
        laseremitter,
        launch_event,
        notification,
        observations,
        onorbitevent,
        organization,
        rf_band_type,
        star_catalog,
        state_vector,
        weather_data,
        airload_plans,
        attitude_data,
        attitude_sets,
        beam_contours,
        deconflictset,
        drift_history,
        manifoldelset,
        operatingunit,
        track_details,
        air_operations,
        airfield_slots,
        batterydetails,
        engine_details,
        ephemeris_sets,
        ground_imagery,
        item_trackings,
        launch_vehicle,
        missile_tracks,
        onorbitantenna,
        onorbitbattery,
        onorbitdetails,
        sensor_stating,
        weather_report,
        airfield_status,
        diff_of_arrival,
        effect_requests,
        event_evolution,
        h3_geo_hex_cell,
        isr_collections,
        onorbitthruster,
        sar_observation,
        supporting_data,
        aircraft_sorties,
        analytic_imagery,
        collect_requests,
        effect_responses,
        launch_detection,
        secure_messaging,
        aircraft_statuses,
        collect_responses,
        equipment_remarks,
        gnss_observations,
        iono_observations,
        logistics_support,
        onboardnavigation,
        onorbitassessment,
        onorbitsolararray,
        personnelrecovery,
        feature_assessment,
        mission_assignment,
        object_of_interest,
        orbitdetermination,
        sensor_maintenance,
        emitter_geolocation,
        gnss_observationset,
        launch_site_details,
        operatingunitremark,
        organizationdetails,
        soi_observation_set,
        solar_array_details,
        surface_obstruction,
        closelyspacedobjects,
        diplomatic_clearance,
        sera_data_navigation,
        onorbitthrusterstatus,
        report_and_activities,
        space_env_observation,
        air_transport_missions,
        laserdeconflictrequest,
        launch_vehicle_details,
        sera_data_comm_details,
        seradata_radar_payload,
        aircraft_status_remarks,
        airspace_control_orders,
        sensor_observation_type,
        sera_data_early_warning,
        seradata_sigint_payload,
        aviation_risk_management,
        global_atmospheric_model,
        navigational_obstruction,
        seradata_optical_payload,
        airfield_slot_consumptions,
        seradata_spacecraft_details,
    )
    from .resources.ir import IrResource, AsyncIrResource
    from .resources.poi import PoiResource, AsyncPoiResource
    from .resources.beam import BeamResource, AsyncBeamResource
    from .resources.comm import CommResource, AsyncCommResource
    from .resources.cots import CotsResource, AsyncCotsResource
    from .resources.crew import CrewResource, AsyncCrewResource
    from .resources.item import ItemResource, AsyncItemResource
    from .resources.port import PortResource, AsyncPortResource
    from .resources.user import UserResource, AsyncUserResource
    from .resources.buses import BusesResource, AsyncBusesResource
    from .resources.stage import StageResource, AsyncStageResource
    from .resources.status import StatusResource, AsyncStatusResource
    from .resources.vessel import VesselResource, AsyncVesselResource
    from .resources.ais.ais import AIsResource, AsyncAIsResource
    from .resources.engines import EnginesResource, AsyncEnginesResource
    from .resources.eop.eop import EopResource, AsyncEopResource
    from .resources.mti.mti import MtiResource, AsyncMtiResource
    from .resources.rf_band import RfBandResource, AsyncRfBandResource
    from .resources.scs.scs import ScsResource, AsyncScsResource
    from .resources.sgi.sgi import SgiResource, AsyncSgiResource
    from .resources.surface import SurfaceResource, AsyncSurfaceResource
    from .resources.aircraft import AircraftResource, AsyncAircraftResource
    from .resources.antennas import AntennasResource, AsyncAntennasResource
    from .resources.channels import ChannelsResource, AsyncChannelsResource
    from .resources.dropzone import DropzoneResource, AsyncDropzoneResource
    from .resources.entities import EntitiesResource, AsyncEntitiesResource
    from .resources.location import LocationResource, AsyncLocationResource
    from .resources.manifold import ManifoldResource, AsyncManifoldResource
    from .resources.airfields import AirfieldsResource, AsyncAirfieldsResource
    from .resources.batteries import BatteriesResource, AsyncBatteriesResource
    from .resources.countries import CountriesResource, AsyncCountriesResource
    from .resources.equipment import EquipmentResource, AsyncEquipmentResource
    from .resources.evac.evac import EvacResource, AsyncEvacResource
    from .resources.site.site import SiteResource, AsyncSiteResource
    from .resources.substatus import SubstatusResource, AsyncSubstatusResource
    from .resources.swir.swir import SwirResource, AsyncSwirResource
    from .resources.air_events import AirEventsResource, AsyncAirEventsResource
    from .resources.flightplan import FlightplanResource, AsyncFlightplanResource
    from .resources.linkstatus import LinkstatusResource, AsyncLinkstatusResource
    from .resources.navigation import NavigationResource, AsyncNavigationResource
    from .resources.scientific import ScientificResource, AsyncScientificResource
    from .resources.ais_objects import AIsObjectsResource, AsyncAIsObjectsResource
    from .resources.launch_site import LaunchSiteResource, AsyncLaunchSiteResource
    from .resources.onorbitlist import OnorbitlistResource, AsyncOnorbitlistResource
    from .resources.route_stats import RouteStatsResource, AsyncRouteStatsResource
    from .resources.sensor_type import SensorTypeResource, AsyncSensorTypeResource
    from .resources.site_remark import SiteRemarkResource, AsyncSiteRemarkResource
    from .resources.solar_array import SolarArrayResource, AsyncSolarArrayResource
    from .resources.track.track import TrackResource, AsyncTrackResource
    from .resources.transponder import TransponderResource, AsyncTransponderResource
    from .resources.video.video import VideoResource, AsyncVideoResource
    from .resources.onorbitevent import OnorbiteventResource, AsyncOnorbiteventResource
    from .resources.organization import OrganizationResource, AsyncOrganizationResource
    from .resources.rf_band_type import RfBandTypeResource, AsyncRfBandTypeResource
    from .resources.airload_plans import AirloadPlansResource, AsyncAirloadPlansResource
    from .resources.attitude_data import AttitudeDataResource, AsyncAttitudeDataResource
    from .resources.beam_contours import BeamContoursResource, AsyncBeamContoursResource
    from .resources.drift_history import DriftHistoryResource, AsyncDriftHistoryResource
    from .resources.ecpedr.ecpedr import EcpedrResource, AsyncEcpedrResource
    from .resources.elsets.elsets import ElsetsResource, AsyncElsetsResource
    from .resources.h3_geo.h3_geo import H3GeoResource, AsyncH3GeoResource
    from .resources.hazard.hazard import HazardResource, AsyncHazardResource
    from .resources.manifoldelset import ManifoldelsetResource, AsyncManifoldelsetResource
    from .resources.operatingunit import OperatingunitResource, AsyncOperatingunitResource
    from .resources.sensor.sensor import SensorResource, AsyncSensorResource
    from .resources.sigact.sigact import SigactResource, AsyncSigactResource
    from .resources.airfield_slots import AirfieldSlotsResource, AsyncAirfieldSlotsResource
    from .resources.batterydetails import BatterydetailsResource, AsyncBatterydetailsResource
    from .resources.engine_details import EngineDetailsResource, AsyncEngineDetailsResource
    from .resources.launch_vehicle import LaunchVehicleResource, AsyncLaunchVehicleResource
    from .resources.onorbitantenna import OnorbitantennaResource, AsyncOnorbitantennaResource
    from .resources.onorbitbattery import OnorbitbatteryResource, AsyncOnorbitbatteryResource
    from .resources.onorbitdetails import OnorbitdetailsResource, AsyncOnorbitdetailsResource
    from .resources.sensor_stating import SensorStatingResource, AsyncSensorStatingResource
    from .resources.h3_geo_hex_cell import H3GeoHexCellResource, AsyncH3GeoHexCellResource
    from .resources.onorbit.onorbit import OnorbitResource, AsyncOnorbitResource
    from .resources.onorbitthruster import OnorbitthrusterResource, AsyncOnorbitthrusterResource
    from .resources.tai_utc.tai_utc import TaiUtcResource, AsyncTaiUtcResource
    from .resources.aircraft_sorties import AircraftSortiesResource, AsyncAircraftSortiesResource
    from .resources.launch_detection import LaunchDetectionResource, AsyncLaunchDetectionResource
    from .resources.secure_messaging import SecureMessagingResource, AsyncSecureMessagingResource
    from .resources.equipment_remarks import EquipmentRemarksResource, AsyncEquipmentRemarksResource
    from .resources.onorbitsolararray import OnorbitsolararrayResource, AsyncOnorbitsolararrayResource
    from .resources.object_of_interest import ObjectOfInterestResource, AsyncObjectOfInterestResource
    from .resources.emireport.emireport import EmireportResource, AsyncEmireportResource
    from .resources.emitter_geolocation import EmitterGeolocationResource, AsyncEmitterGeolocationResource
    from .resources.ephemeris.ephemeris import EphemerisResource, AsyncEphemerisResource
    from .resources.launch_site_details import LaunchSiteDetailsResource, AsyncLaunchSiteDetailsResource
    from .resources.maneuvers.maneuvers import ManeuversResource, AsyncManeuversResource
    from .resources.operatingunitremark import OperatingunitremarkResource, AsyncOperatingunitremarkResource
    from .resources.organizationdetails import OrganizationdetailsResource, AsyncOrganizationdetailsResource
    from .resources.solar_array_details import SolarArrayDetailsResource, AsyncSolarArrayDetailsResource
    from .resources.surface_obstruction import SurfaceObstructionResource, AsyncSurfaceObstructionResource
    from .resources.tdoa_fdoa.tdoa_fdoa import TdoaFdoaResource, AsyncTdoaFdoaResource
    from .resources.sera_data_navigation import SeraDataNavigationResource, AsyncSeraDataNavigationResource
    from .resources.geo_status.geo_status import GeoStatusResource, AsyncGeoStatusResource
    from .resources.orbittrack.orbittrack import OrbittrackResource, AsyncOrbittrackResource
    from .resources.rf_emitter.rf_emitter import RfEmitterResource, AsyncRfEmitterResource
    from .resources.sortie_ppr.sortie_ppr import SortiePprResource, AsyncSortiePprResource
    from .resources.launch_vehicle_details import LaunchVehicleDetailsResource, AsyncLaunchVehicleDetailsResource
    from .resources.sera_data_comm_details import SeraDataCommDetailsResource, AsyncSeraDataCommDetailsResource
    from .resources.seradata_radar_payload import SeradataRadarPayloadResource, AsyncSeradataRadarPayloadResource
    from .resources.aircraft_status_remarks import AircraftStatusRemarksResource, AsyncAircraftStatusRemarksResource
    from .resources.airspace_control_orders import AirspaceControlOrdersResource, AsyncAirspaceControlOrdersResource
    from .resources.gnss_raw_if.gnss_raw_if import GnssRawIfResource, AsyncGnssRawIfResource
    from .resources.link_status.link_status import LinkStatusResource, AsyncLinkStatusResource
    from .resources.sensor_observation_type import SensorObservationTypeResource, AsyncSensorObservationTypeResource
    from .resources.sensor_plan.sensor_plan import SensorPlanResource, AsyncSensorPlanResource
    from .resources.sera_data_early_warning import SeraDataEarlyWarningResource, AsyncSeraDataEarlyWarningResource
    from .resources.seradata_sigint_payload import SeradataSigintPayloadResource, AsyncSeradataSigintPayloadResource
    from .resources.site_status.site_status import SiteStatusResource, AsyncSiteStatusResource
    from .resources.sky_imagery.sky_imagery import SkyImageryResource, AsyncSkyImageryResource
    from .resources.track_route.track_route import TrackRouteResource, AsyncTrackRouteResource
    from .resources.aviation_risk_management import AviationRiskManagementResource, AsyncAviationRiskManagementResource
    from .resources.navigational_obstruction import (
        NavigationalObstructionResource,
        AsyncNavigationalObstructionResource,
    )
    from .resources.seradata_optical_payload import SeradataOpticalPayloadResource, AsyncSeradataOpticalPayloadResource
    from .resources.conjunctions.conjunctions import ConjunctionsResource, AsyncConjunctionsResource
    from .resources.laseremitter.laseremitter import LaseremitterResource, AsyncLaseremitterResource
    from .resources.launch_event.launch_event import LaunchEventResource, AsyncLaunchEventResource
    from .resources.notification.notification import NotificationResource, AsyncNotificationResource
    from .resources.observations.observations import ObservationsResource, AsyncObservationsResource
    from .resources.star_catalog.star_catalog import StarCatalogResource, AsyncStarCatalogResource
    from .resources.state_vector.state_vector import StateVectorResource, AsyncStateVectorResource
    from .resources.weather_data.weather_data import WeatherDataResource, AsyncWeatherDataResource
    from .resources.airfield_slot_consumptions import (
        AirfieldSlotConsumptionsResource,
        AsyncAirfieldSlotConsumptionsResource,
    )
    from .resources.attitude_sets.attitude_sets import AttitudeSetsResource, AsyncAttitudeSetsResource
    from .resources.deconflictset.deconflictset import DeconflictsetResource, AsyncDeconflictsetResource
    from .resources.seradata_spacecraft_details import (
        SeradataSpacecraftDetailsResource,
        AsyncSeradataSpacecraftDetailsResource,
    )
    from .resources.track_details.track_details import TrackDetailsResource, AsyncTrackDetailsResource
    from .resources.air_operations.air_operations import AirOperationsResource, AsyncAirOperationsResource
    from .resources.ephemeris_sets.ephemeris_sets import EphemerisSetsResource, AsyncEphemerisSetsResource
    from .resources.ground_imagery.ground_imagery import GroundImageryResource, AsyncGroundImageryResource
    from .resources.item_trackings.item_trackings import ItemTrackingsResource, AsyncItemTrackingsResource
    from .resources.missile_tracks.missile_tracks import MissileTracksResource, AsyncMissileTracksResource
    from .resources.weather_report.weather_report import WeatherReportResource, AsyncWeatherReportResource
    from .resources.airfield_status.airfield_status import AirfieldStatusResource, AsyncAirfieldStatusResource
    from .resources.diff_of_arrival.diff_of_arrival import DiffOfArrivalResource, AsyncDiffOfArrivalResource
    from .resources.effect_requests.effect_requests import EffectRequestsResource, AsyncEffectRequestsResource
    from .resources.event_evolution.event_evolution import EventEvolutionResource, AsyncEventEvolutionResource
    from .resources.isr_collections.isr_collections import IsrCollectionsResource, AsyncIsrCollectionsResource
    from .resources.sar_observation.sar_observation import SarObservationResource, AsyncSarObservationResource
    from .resources.supporting_data.supporting_data import SupportingDataResource, AsyncSupportingDataResource
    from .resources.analytic_imagery.analytic_imagery import AnalyticImageryResource, AsyncAnalyticImageryResource
    from .resources.collect_requests.collect_requests import CollectRequestsResource, AsyncCollectRequestsResource
    from .resources.effect_responses.effect_responses import EffectResponsesResource, AsyncEffectResponsesResource
    from .resources.aircraft_statuses.aircraft_statuses import AircraftStatusesResource, AsyncAircraftStatusesResource
    from .resources.collect_responses.collect_responses import CollectResponsesResource, AsyncCollectResponsesResource
    from .resources.gnss_observations.gnss_observations import GnssObservationsResource, AsyncGnssObservationsResource
    from .resources.iono_observations.iono_observations import IonoObservationsResource, AsyncIonoObservationsResource
    from .resources.logistics_support.logistics_support import LogisticsSupportResource, AsyncLogisticsSupportResource
    from .resources.onboardnavigation.onboardnavigation import OnboardnavigationResource, AsyncOnboardnavigationResource
    from .resources.onorbitassessment.onorbitassessment import OnorbitassessmentResource, AsyncOnorbitassessmentResource
    from .resources.personnelrecovery.personnelrecovery import PersonnelrecoveryResource, AsyncPersonnelrecoveryResource
    from .resources.feature_assessment.feature_assessment import (
        FeatureAssessmentResource,
        AsyncFeatureAssessmentResource,
    )
    from .resources.mission_assignment.mission_assignment import (
        MissionAssignmentResource,
        AsyncMissionAssignmentResource,
    )
    from .resources.orbitdetermination.orbitdetermination import (
        OrbitdeterminationResource,
        AsyncOrbitdeterminationResource,
    )
    from .resources.sensor_maintenance.sensor_maintenance import (
        SensorMaintenanceResource,
        AsyncSensorMaintenanceResource,
    )
    from .resources.gnss_observationset.gnss_observationset import (
        GnssObservationsetResource,
        AsyncGnssObservationsetResource,
    )
    from .resources.soi_observation_set.soi_observation_set import (
        SoiObservationSetResource,
        AsyncSoiObservationSetResource,
    )
    from .resources.closelyspacedobjects.closelyspacedobjects import (
        CloselyspacedobjectsResource,
        AsyncCloselyspacedobjectsResource,
    )
    from .resources.diplomatic_clearance.diplomatic_clearance import (
        DiplomaticClearanceResource,
        AsyncDiplomaticClearanceResource,
    )
    from .resources.onorbitthrusterstatus.onorbitthrusterstatus import (
        OnorbitthrusterstatusResource,
        AsyncOnorbitthrusterstatusResource,
    )
    from .resources.report_and_activities.report_and_activities import (
        ReportAndActivitiesResource,
        AsyncReportAndActivitiesResource,
    )
    from .resources.space_env_observation.space_env_observation import (
        SpaceEnvObservationResource,
        AsyncSpaceEnvObservationResource,
    )
    from .resources.air_transport_missions.air_transport_missions import (
        AirTransportMissionsResource,
        AsyncAirTransportMissionsResource,
    )
    from .resources.laserdeconflictrequest.laserdeconflictrequest import (
        LaserdeconflictrequestResource,
        AsyncLaserdeconflictrequestResource,
    )
    from .resources.global_atmospheric_model.global_atmospheric_model import (
        GlobalAtmosphericModelResource,
        AsyncGlobalAtmosphericModelResource,
    )

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
    # client options
    access_token: str | None
    password: str | None
    username: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        password: str | None = None,
        username: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        - `access_token` from `UDL_ACCESS_TOKEN`
        - `password` from `UDL_AUTH_PASSWORD`
        - `username` from `UDL_AUTH_USERNAME`
        """
        if access_token is None:
            access_token = os.environ.get("UDL_ACCESS_TOKEN")
        self.access_token = access_token

        if password is None:
            password = os.environ.get("UDL_AUTH_PASSWORD")
        self.password = password

        if username is None:
            username = os.environ.get("UDL_AUTH_USERNAME")
        self.username = username

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

    @cached_property
    def air_events(self) -> AirEventsResource:
        from .resources.air_events import AirEventsResource

        return AirEventsResource(self)

    @cached_property
    def air_operations(self) -> AirOperationsResource:
        from .resources.air_operations import AirOperationsResource

        return AirOperationsResource(self)

    @cached_property
    def air_transport_missions(self) -> AirTransportMissionsResource:
        from .resources.air_transport_missions import AirTransportMissionsResource

        return AirTransportMissionsResource(self)

    @cached_property
    def aircraft(self) -> AircraftResource:
        from .resources.aircraft import AircraftResource

        return AircraftResource(self)

    @cached_property
    def aircraft_sorties(self) -> AircraftSortiesResource:
        from .resources.aircraft_sorties import AircraftSortiesResource

        return AircraftSortiesResource(self)

    @cached_property
    def aircraft_status_remarks(self) -> AircraftStatusRemarksResource:
        from .resources.aircraft_status_remarks import AircraftStatusRemarksResource

        return AircraftStatusRemarksResource(self)

    @cached_property
    def aircraft_statuses(self) -> AircraftStatusesResource:
        from .resources.aircraft_statuses import AircraftStatusesResource

        return AircraftStatusesResource(self)

    @cached_property
    def airfield_slot_consumptions(self) -> AirfieldSlotConsumptionsResource:
        from .resources.airfield_slot_consumptions import AirfieldSlotConsumptionsResource

        return AirfieldSlotConsumptionsResource(self)

    @cached_property
    def airfield_slots(self) -> AirfieldSlotsResource:
        from .resources.airfield_slots import AirfieldSlotsResource

        return AirfieldSlotsResource(self)

    @cached_property
    def airfield_status(self) -> AirfieldStatusResource:
        from .resources.airfield_status import AirfieldStatusResource

        return AirfieldStatusResource(self)

    @cached_property
    def airfields(self) -> AirfieldsResource:
        from .resources.airfields import AirfieldsResource

        return AirfieldsResource(self)

    @cached_property
    def airload_plans(self) -> AirloadPlansResource:
        from .resources.airload_plans import AirloadPlansResource

        return AirloadPlansResource(self)

    @cached_property
    def airspace_control_orders(self) -> AirspaceControlOrdersResource:
        from .resources.airspace_control_orders import AirspaceControlOrdersResource

        return AirspaceControlOrdersResource(self)

    @cached_property
    def ais(self) -> AIsResource:
        from .resources.ais import AIsResource

        return AIsResource(self)

    @cached_property
    def ais_objects(self) -> AIsObjectsResource:
        from .resources.ais_objects import AIsObjectsResource

        return AIsObjectsResource(self)

    @cached_property
    def analytic_imagery(self) -> AnalyticImageryResource:
        from .resources.analytic_imagery import AnalyticImageryResource

        return AnalyticImageryResource(self)

    @cached_property
    def antennas(self) -> AntennasResource:
        from .resources.antennas import AntennasResource

        return AntennasResource(self)

    @cached_property
    def attitude_data(self) -> AttitudeDataResource:
        from .resources.attitude_data import AttitudeDataResource

        return AttitudeDataResource(self)

    @cached_property
    def attitude_sets(self) -> AttitudeSetsResource:
        from .resources.attitude_sets import AttitudeSetsResource

        return AttitudeSetsResource(self)

    @cached_property
    def aviation_risk_management(self) -> AviationRiskManagementResource:
        from .resources.aviation_risk_management import AviationRiskManagementResource

        return AviationRiskManagementResource(self)

    @cached_property
    def batteries(self) -> BatteriesResource:
        from .resources.batteries import BatteriesResource

        return BatteriesResource(self)

    @cached_property
    def batterydetails(self) -> BatterydetailsResource:
        from .resources.batterydetails import BatterydetailsResource

        return BatterydetailsResource(self)

    @cached_property
    def beam(self) -> BeamResource:
        from .resources.beam import BeamResource

        return BeamResource(self)

    @cached_property
    def beam_contours(self) -> BeamContoursResource:
        from .resources.beam_contours import BeamContoursResource

        return BeamContoursResource(self)

    @cached_property
    def buses(self) -> BusesResource:
        from .resources.buses import BusesResource

        return BusesResource(self)

    @cached_property
    def channels(self) -> ChannelsResource:
        from .resources.channels import ChannelsResource

        return ChannelsResource(self)

    @cached_property
    def closelyspacedobjects(self) -> CloselyspacedobjectsResource:
        from .resources.closelyspacedobjects import CloselyspacedobjectsResource

        return CloselyspacedobjectsResource(self)

    @cached_property
    def collect_requests(self) -> CollectRequestsResource:
        from .resources.collect_requests import CollectRequestsResource

        return CollectRequestsResource(self)

    @cached_property
    def collect_responses(self) -> CollectResponsesResource:
        from .resources.collect_responses import CollectResponsesResource

        return CollectResponsesResource(self)

    @cached_property
    def comm(self) -> CommResource:
        from .resources.comm import CommResource

        return CommResource(self)

    @cached_property
    def conjunctions(self) -> ConjunctionsResource:
        from .resources.conjunctions import ConjunctionsResource

        return ConjunctionsResource(self)

    @cached_property
    def cots(self) -> CotsResource:
        from .resources.cots import CotsResource

        return CotsResource(self)

    @cached_property
    def countries(self) -> CountriesResource:
        from .resources.countries import CountriesResource

        return CountriesResource(self)

    @cached_property
    def crew(self) -> CrewResource:
        from .resources.crew import CrewResource

        return CrewResource(self)

    @cached_property
    def deconflictset(self) -> DeconflictsetResource:
        from .resources.deconflictset import DeconflictsetResource

        return DeconflictsetResource(self)

    @cached_property
    def diff_of_arrival(self) -> DiffOfArrivalResource:
        from .resources.diff_of_arrival import DiffOfArrivalResource

        return DiffOfArrivalResource(self)

    @cached_property
    def diplomatic_clearance(self) -> DiplomaticClearanceResource:
        from .resources.diplomatic_clearance import DiplomaticClearanceResource

        return DiplomaticClearanceResource(self)

    @cached_property
    def drift_history(self) -> DriftHistoryResource:
        from .resources.drift_history import DriftHistoryResource

        return DriftHistoryResource(self)

    @cached_property
    def dropzone(self) -> DropzoneResource:
        from .resources.dropzone import DropzoneResource

        return DropzoneResource(self)

    @cached_property
    def ecpedr(self) -> EcpedrResource:
        from .resources.ecpedr import EcpedrResource

        return EcpedrResource(self)

    @cached_property
    def effect_requests(self) -> EffectRequestsResource:
        from .resources.effect_requests import EffectRequestsResource

        return EffectRequestsResource(self)

    @cached_property
    def effect_responses(self) -> EffectResponsesResource:
        from .resources.effect_responses import EffectResponsesResource

        return EffectResponsesResource(self)

    @cached_property
    def elsets(self) -> ElsetsResource:
        from .resources.elsets import ElsetsResource

        return ElsetsResource(self)

    @cached_property
    def emireport(self) -> EmireportResource:
        from .resources.emireport import EmireportResource

        return EmireportResource(self)

    @cached_property
    def emitter_geolocation(self) -> EmitterGeolocationResource:
        from .resources.emitter_geolocation import EmitterGeolocationResource

        return EmitterGeolocationResource(self)

    @cached_property
    def engine_details(self) -> EngineDetailsResource:
        from .resources.engine_details import EngineDetailsResource

        return EngineDetailsResource(self)

    @cached_property
    def engines(self) -> EnginesResource:
        from .resources.engines import EnginesResource

        return EnginesResource(self)

    @cached_property
    def entities(self) -> EntitiesResource:
        from .resources.entities import EntitiesResource

        return EntitiesResource(self)

    @cached_property
    def eop(self) -> EopResource:
        from .resources.eop import EopResource

        return EopResource(self)

    @cached_property
    def ephemeris(self) -> EphemerisResource:
        from .resources.ephemeris import EphemerisResource

        return EphemerisResource(self)

    @cached_property
    def ephemeris_sets(self) -> EphemerisSetsResource:
        from .resources.ephemeris_sets import EphemerisSetsResource

        return EphemerisSetsResource(self)

    @cached_property
    def equipment(self) -> EquipmentResource:
        from .resources.equipment import EquipmentResource

        return EquipmentResource(self)

    @cached_property
    def equipment_remarks(self) -> EquipmentRemarksResource:
        from .resources.equipment_remarks import EquipmentRemarksResource

        return EquipmentRemarksResource(self)

    @cached_property
    def evac(self) -> EvacResource:
        from .resources.evac import EvacResource

        return EvacResource(self)

    @cached_property
    def event_evolution(self) -> EventEvolutionResource:
        from .resources.event_evolution import EventEvolutionResource

        return EventEvolutionResource(self)

    @cached_property
    def feature_assessment(self) -> FeatureAssessmentResource:
        from .resources.feature_assessment import FeatureAssessmentResource

        return FeatureAssessmentResource(self)

    @cached_property
    def flightplan(self) -> FlightplanResource:
        from .resources.flightplan import FlightplanResource

        return FlightplanResource(self)

    @cached_property
    def geo_status(self) -> GeoStatusResource:
        from .resources.geo_status import GeoStatusResource

        return GeoStatusResource(self)

    @cached_property
    def global_atmospheric_model(self) -> GlobalAtmosphericModelResource:
        from .resources.global_atmospheric_model import GlobalAtmosphericModelResource

        return GlobalAtmosphericModelResource(self)

    @cached_property
    def gnss_observations(self) -> GnssObservationsResource:
        from .resources.gnss_observations import GnssObservationsResource

        return GnssObservationsResource(self)

    @cached_property
    def gnss_observationset(self) -> GnssObservationsetResource:
        from .resources.gnss_observationset import GnssObservationsetResource

        return GnssObservationsetResource(self)

    @cached_property
    def gnss_raw_if(self) -> GnssRawIfResource:
        from .resources.gnss_raw_if import GnssRawIfResource

        return GnssRawIfResource(self)

    @cached_property
    def ground_imagery(self) -> GroundImageryResource:
        from .resources.ground_imagery import GroundImageryResource

        return GroundImageryResource(self)

    @cached_property
    def h3_geo(self) -> H3GeoResource:
        from .resources.h3_geo import H3GeoResource

        return H3GeoResource(self)

    @cached_property
    def h3_geo_hex_cell(self) -> H3GeoHexCellResource:
        from .resources.h3_geo_hex_cell import H3GeoHexCellResource

        return H3GeoHexCellResource(self)

    @cached_property
    def hazard(self) -> HazardResource:
        from .resources.hazard import HazardResource

        return HazardResource(self)

    @cached_property
    def iono_observations(self) -> IonoObservationsResource:
        from .resources.iono_observations import IonoObservationsResource

        return IonoObservationsResource(self)

    @cached_property
    def ir(self) -> IrResource:
        from .resources.ir import IrResource

        return IrResource(self)

    @cached_property
    def isr_collections(self) -> IsrCollectionsResource:
        from .resources.isr_collections import IsrCollectionsResource

        return IsrCollectionsResource(self)

    @cached_property
    def item(self) -> ItemResource:
        from .resources.item import ItemResource

        return ItemResource(self)

    @cached_property
    def item_trackings(self) -> ItemTrackingsResource:
        from .resources.item_trackings import ItemTrackingsResource

        return ItemTrackingsResource(self)

    @cached_property
    def laserdeconflictrequest(self) -> LaserdeconflictrequestResource:
        from .resources.laserdeconflictrequest import LaserdeconflictrequestResource

        return LaserdeconflictrequestResource(self)

    @cached_property
    def laseremitter(self) -> LaseremitterResource:
        from .resources.laseremitter import LaseremitterResource

        return LaseremitterResource(self)

    @cached_property
    def launch_detection(self) -> LaunchDetectionResource:
        from .resources.launch_detection import LaunchDetectionResource

        return LaunchDetectionResource(self)

    @cached_property
    def launch_event(self) -> LaunchEventResource:
        from .resources.launch_event import LaunchEventResource

        return LaunchEventResource(self)

    @cached_property
    def launch_site(self) -> LaunchSiteResource:
        from .resources.launch_site import LaunchSiteResource

        return LaunchSiteResource(self)

    @cached_property
    def launch_site_details(self) -> LaunchSiteDetailsResource:
        from .resources.launch_site_details import LaunchSiteDetailsResource

        return LaunchSiteDetailsResource(self)

    @cached_property
    def launch_vehicle(self) -> LaunchVehicleResource:
        from .resources.launch_vehicle import LaunchVehicleResource

        return LaunchVehicleResource(self)

    @cached_property
    def launch_vehicle_details(self) -> LaunchVehicleDetailsResource:
        from .resources.launch_vehicle_details import LaunchVehicleDetailsResource

        return LaunchVehicleDetailsResource(self)

    @cached_property
    def link_status(self) -> LinkStatusResource:
        from .resources.link_status import LinkStatusResource

        return LinkStatusResource(self)

    @cached_property
    def linkstatus(self) -> LinkstatusResource:
        from .resources.linkstatus import LinkstatusResource

        return LinkstatusResource(self)

    @cached_property
    def location(self) -> LocationResource:
        from .resources.location import LocationResource

        return LocationResource(self)

    @cached_property
    def logistics_support(self) -> LogisticsSupportResource:
        from .resources.logistics_support import LogisticsSupportResource

        return LogisticsSupportResource(self)

    @cached_property
    def maneuvers(self) -> ManeuversResource:
        from .resources.maneuvers import ManeuversResource

        return ManeuversResource(self)

    @cached_property
    def manifold(self) -> ManifoldResource:
        from .resources.manifold import ManifoldResource

        return ManifoldResource(self)

    @cached_property
    def manifoldelset(self) -> ManifoldelsetResource:
        from .resources.manifoldelset import ManifoldelsetResource

        return ManifoldelsetResource(self)

    @cached_property
    def missile_tracks(self) -> MissileTracksResource:
        from .resources.missile_tracks import MissileTracksResource

        return MissileTracksResource(self)

    @cached_property
    def mission_assignment(self) -> MissionAssignmentResource:
        from .resources.mission_assignment import MissionAssignmentResource

        return MissionAssignmentResource(self)

    @cached_property
    def mti(self) -> MtiResource:
        from .resources.mti import MtiResource

        return MtiResource(self)

    @cached_property
    def navigation(self) -> NavigationResource:
        from .resources.navigation import NavigationResource

        return NavigationResource(self)

    @cached_property
    def navigational_obstruction(self) -> NavigationalObstructionResource:
        from .resources.navigational_obstruction import NavigationalObstructionResource

        return NavigationalObstructionResource(self)

    @cached_property
    def notification(self) -> NotificationResource:
        from .resources.notification import NotificationResource

        return NotificationResource(self)

    @cached_property
    def object_of_interest(self) -> ObjectOfInterestResource:
        from .resources.object_of_interest import ObjectOfInterestResource

        return ObjectOfInterestResource(self)

    @cached_property
    def observations(self) -> ObservationsResource:
        from .resources.observations import ObservationsResource

        return ObservationsResource(self)

    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResource:
        from .resources.onboardnavigation import OnboardnavigationResource

        return OnboardnavigationResource(self)

    @cached_property
    def onorbit(self) -> OnorbitResource:
        from .resources.onorbit import OnorbitResource

        return OnorbitResource(self)

    @cached_property
    def onorbitantenna(self) -> OnorbitantennaResource:
        from .resources.onorbitantenna import OnorbitantennaResource

        return OnorbitantennaResource(self)

    @cached_property
    def onorbitbattery(self) -> OnorbitbatteryResource:
        from .resources.onorbitbattery import OnorbitbatteryResource

        return OnorbitbatteryResource(self)

    @cached_property
    def onorbitdetails(self) -> OnorbitdetailsResource:
        from .resources.onorbitdetails import OnorbitdetailsResource

        return OnorbitdetailsResource(self)

    @cached_property
    def onorbitevent(self) -> OnorbiteventResource:
        from .resources.onorbitevent import OnorbiteventResource

        return OnorbiteventResource(self)

    @cached_property
    def onorbitlist(self) -> OnorbitlistResource:
        from .resources.onorbitlist import OnorbitlistResource

        return OnorbitlistResource(self)

    @cached_property
    def onorbitsolararray(self) -> OnorbitsolararrayResource:
        from .resources.onorbitsolararray import OnorbitsolararrayResource

        return OnorbitsolararrayResource(self)

    @cached_property
    def onorbitthruster(self) -> OnorbitthrusterResource:
        from .resources.onorbitthruster import OnorbitthrusterResource

        return OnorbitthrusterResource(self)

    @cached_property
    def onorbitthrusterstatus(self) -> OnorbitthrusterstatusResource:
        from .resources.onorbitthrusterstatus import OnorbitthrusterstatusResource

        return OnorbitthrusterstatusResource(self)

    @cached_property
    def onorbitassessment(self) -> OnorbitassessmentResource:
        from .resources.onorbitassessment import OnorbitassessmentResource

        return OnorbitassessmentResource(self)

    @cached_property
    def operatingunit(self) -> OperatingunitResource:
        from .resources.operatingunit import OperatingunitResource

        return OperatingunitResource(self)

    @cached_property
    def operatingunitremark(self) -> OperatingunitremarkResource:
        from .resources.operatingunitremark import OperatingunitremarkResource

        return OperatingunitremarkResource(self)

    @cached_property
    def orbitdetermination(self) -> OrbitdeterminationResource:
        from .resources.orbitdetermination import OrbitdeterminationResource

        return OrbitdeterminationResource(self)

    @cached_property
    def orbittrack(self) -> OrbittrackResource:
        from .resources.orbittrack import OrbittrackResource

        return OrbittrackResource(self)

    @cached_property
    def organization(self) -> OrganizationResource:
        from .resources.organization import OrganizationResource

        return OrganizationResource(self)

    @cached_property
    def organizationdetails(self) -> OrganizationdetailsResource:
        from .resources.organizationdetails import OrganizationdetailsResource

        return OrganizationdetailsResource(self)

    @cached_property
    def personnelrecovery(self) -> PersonnelrecoveryResource:
        from .resources.personnelrecovery import PersonnelrecoveryResource

        return PersonnelrecoveryResource(self)

    @cached_property
    def poi(self) -> PoiResource:
        from .resources.poi import PoiResource

        return PoiResource(self)

    @cached_property
    def port(self) -> PortResource:
        from .resources.port import PortResource

        return PortResource(self)

    @cached_property
    def report_and_activities(self) -> ReportAndActivitiesResource:
        from .resources.report_and_activities import ReportAndActivitiesResource

        return ReportAndActivitiesResource(self)

    @cached_property
    def rf_band(self) -> RfBandResource:
        from .resources.rf_band import RfBandResource

        return RfBandResource(self)

    @cached_property
    def rf_band_type(self) -> RfBandTypeResource:
        from .resources.rf_band_type import RfBandTypeResource

        return RfBandTypeResource(self)

    @cached_property
    def rf_emitter(self) -> RfEmitterResource:
        from .resources.rf_emitter import RfEmitterResource

        return RfEmitterResource(self)

    @cached_property
    def route_stats(self) -> RouteStatsResource:
        from .resources.route_stats import RouteStatsResource

        return RouteStatsResource(self)

    @cached_property
    def sar_observation(self) -> SarObservationResource:
        from .resources.sar_observation import SarObservationResource

        return SarObservationResource(self)

    @cached_property
    def scientific(self) -> ScientificResource:
        from .resources.scientific import ScientificResource

        return ScientificResource(self)

    @cached_property
    def scs(self) -> ScsResource:
        from .resources.scs import ScsResource

        return ScsResource(self)

    @cached_property
    def secure_messaging(self) -> SecureMessagingResource:
        from .resources.secure_messaging import SecureMessagingResource

        return SecureMessagingResource(self)

    @cached_property
    def sensor(self) -> SensorResource:
        from .resources.sensor import SensorResource

        return SensorResource(self)

    @cached_property
    def sensor_stating(self) -> SensorStatingResource:
        from .resources.sensor_stating import SensorStatingResource

        return SensorStatingResource(self)

    @cached_property
    def sensor_maintenance(self) -> SensorMaintenanceResource:
        from .resources.sensor_maintenance import SensorMaintenanceResource

        return SensorMaintenanceResource(self)

    @cached_property
    def sensor_observation_type(self) -> SensorObservationTypeResource:
        from .resources.sensor_observation_type import SensorObservationTypeResource

        return SensorObservationTypeResource(self)

    @cached_property
    def sensor_plan(self) -> SensorPlanResource:
        from .resources.sensor_plan import SensorPlanResource

        return SensorPlanResource(self)

    @cached_property
    def sensor_type(self) -> SensorTypeResource:
        from .resources.sensor_type import SensorTypeResource

        return SensorTypeResource(self)

    @cached_property
    def sera_data_comm_details(self) -> SeraDataCommDetailsResource:
        from .resources.sera_data_comm_details import SeraDataCommDetailsResource

        return SeraDataCommDetailsResource(self)

    @cached_property
    def sera_data_early_warning(self) -> SeraDataEarlyWarningResource:
        from .resources.sera_data_early_warning import SeraDataEarlyWarningResource

        return SeraDataEarlyWarningResource(self)

    @cached_property
    def sera_data_navigation(self) -> SeraDataNavigationResource:
        from .resources.sera_data_navigation import SeraDataNavigationResource

        return SeraDataNavigationResource(self)

    @cached_property
    def seradata_optical_payload(self) -> SeradataOpticalPayloadResource:
        from .resources.seradata_optical_payload import SeradataOpticalPayloadResource

        return SeradataOpticalPayloadResource(self)

    @cached_property
    def seradata_radar_payload(self) -> SeradataRadarPayloadResource:
        from .resources.seradata_radar_payload import SeradataRadarPayloadResource

        return SeradataRadarPayloadResource(self)

    @cached_property
    def seradata_sigint_payload(self) -> SeradataSigintPayloadResource:
        from .resources.seradata_sigint_payload import SeradataSigintPayloadResource

        return SeradataSigintPayloadResource(self)

    @cached_property
    def seradata_spacecraft_details(self) -> SeradataSpacecraftDetailsResource:
        from .resources.seradata_spacecraft_details import SeradataSpacecraftDetailsResource

        return SeradataSpacecraftDetailsResource(self)

    @cached_property
    def sgi(self) -> SgiResource:
        from .resources.sgi import SgiResource

        return SgiResource(self)

    @cached_property
    def sigact(self) -> SigactResource:
        from .resources.sigact import SigactResource

        return SigactResource(self)

    @cached_property
    def site(self) -> SiteResource:
        from .resources.site import SiteResource

        return SiteResource(self)

    @cached_property
    def site_remark(self) -> SiteRemarkResource:
        from .resources.site_remark import SiteRemarkResource

        return SiteRemarkResource(self)

    @cached_property
    def site_status(self) -> SiteStatusResource:
        from .resources.site_status import SiteStatusResource

        return SiteStatusResource(self)

    @cached_property
    def sky_imagery(self) -> SkyImageryResource:
        from .resources.sky_imagery import SkyImageryResource

        return SkyImageryResource(self)

    @cached_property
    def soi_observation_set(self) -> SoiObservationSetResource:
        from .resources.soi_observation_set import SoiObservationSetResource

        return SoiObservationSetResource(self)

    @cached_property
    def solar_array(self) -> SolarArrayResource:
        from .resources.solar_array import SolarArrayResource

        return SolarArrayResource(self)

    @cached_property
    def solar_array_details(self) -> SolarArrayDetailsResource:
        from .resources.solar_array_details import SolarArrayDetailsResource

        return SolarArrayDetailsResource(self)

    @cached_property
    def sortie_ppr(self) -> SortiePprResource:
        from .resources.sortie_ppr import SortiePprResource

        return SortiePprResource(self)

    @cached_property
    def space_env_observation(self) -> SpaceEnvObservationResource:
        from .resources.space_env_observation import SpaceEnvObservationResource

        return SpaceEnvObservationResource(self)

    @cached_property
    def stage(self) -> StageResource:
        from .resources.stage import StageResource

        return StageResource(self)

    @cached_property
    def star_catalog(self) -> StarCatalogResource:
        from .resources.star_catalog import StarCatalogResource

        return StarCatalogResource(self)

    @cached_property
    def state_vector(self) -> StateVectorResource:
        from .resources.state_vector import StateVectorResource

        return StateVectorResource(self)

    @cached_property
    def status(self) -> StatusResource:
        from .resources.status import StatusResource

        return StatusResource(self)

    @cached_property
    def substatus(self) -> SubstatusResource:
        from .resources.substatus import SubstatusResource

        return SubstatusResource(self)

    @cached_property
    def supporting_data(self) -> SupportingDataResource:
        from .resources.supporting_data import SupportingDataResource

        return SupportingDataResource(self)

    @cached_property
    def surface(self) -> SurfaceResource:
        from .resources.surface import SurfaceResource

        return SurfaceResource(self)

    @cached_property
    def surface_obstruction(self) -> SurfaceObstructionResource:
        from .resources.surface_obstruction import SurfaceObstructionResource

        return SurfaceObstructionResource(self)

    @cached_property
    def swir(self) -> SwirResource:
        from .resources.swir import SwirResource

        return SwirResource(self)

    @cached_property
    def tai_utc(self) -> TaiUtcResource:
        from .resources.tai_utc import TaiUtcResource

        return TaiUtcResource(self)

    @cached_property
    def tdoa_fdoa(self) -> TdoaFdoaResource:
        from .resources.tdoa_fdoa import TdoaFdoaResource

        return TdoaFdoaResource(self)

    @cached_property
    def track(self) -> TrackResource:
        from .resources.track import TrackResource

        return TrackResource(self)

    @cached_property
    def track_details(self) -> TrackDetailsResource:
        from .resources.track_details import TrackDetailsResource

        return TrackDetailsResource(self)

    @cached_property
    def track_route(self) -> TrackRouteResource:
        from .resources.track_route import TrackRouteResource

        return TrackRouteResource(self)

    @cached_property
    def transponder(self) -> TransponderResource:
        from .resources.transponder import TransponderResource

        return TransponderResource(self)

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def vessel(self) -> VesselResource:
        from .resources.vessel import VesselResource

        return VesselResource(self)

    @cached_property
    def video(self) -> VideoResource:
        from .resources.video import VideoResource

        return VideoResource(self)

    @cached_property
    def weather_data(self) -> WeatherDataResource:
        from .resources.weather_data import WeatherDataResource

        return WeatherDataResource(self)

    @cached_property
    def weather_report(self) -> WeatherReportResource:
        from .resources.weather_report import WeatherReportResource

        return WeatherReportResource(self)

    @cached_property
    def with_raw_response(self) -> UnifieddatalibraryWithRawResponse:
        return UnifieddatalibraryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnifieddatalibraryWithStreamedResponse:
        return UnifieddatalibraryWithStreamedResponse(self)

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
        access_token: str | None = None,
        password: str | None = None,
        username: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            access_token=access_token or self.access_token,
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
    # client options
    access_token: str | None
    password: str | None
    username: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        password: str | None = None,
        username: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        - `access_token` from `UDL_ACCESS_TOKEN`
        - `password` from `UDL_AUTH_PASSWORD`
        - `username` from `UDL_AUTH_USERNAME`
        """
        if access_token is None:
            access_token = os.environ.get("UDL_ACCESS_TOKEN")
        self.access_token = access_token

        if password is None:
            password = os.environ.get("UDL_AUTH_PASSWORD")
        self.password = password

        if username is None:
            username = os.environ.get("UDL_AUTH_USERNAME")
        self.username = username

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

    @cached_property
    def air_events(self) -> AsyncAirEventsResource:
        from .resources.air_events import AsyncAirEventsResource

        return AsyncAirEventsResource(self)

    @cached_property
    def air_operations(self) -> AsyncAirOperationsResource:
        from .resources.air_operations import AsyncAirOperationsResource

        return AsyncAirOperationsResource(self)

    @cached_property
    def air_transport_missions(self) -> AsyncAirTransportMissionsResource:
        from .resources.air_transport_missions import AsyncAirTransportMissionsResource

        return AsyncAirTransportMissionsResource(self)

    @cached_property
    def aircraft(self) -> AsyncAircraftResource:
        from .resources.aircraft import AsyncAircraftResource

        return AsyncAircraftResource(self)

    @cached_property
    def aircraft_sorties(self) -> AsyncAircraftSortiesResource:
        from .resources.aircraft_sorties import AsyncAircraftSortiesResource

        return AsyncAircraftSortiesResource(self)

    @cached_property
    def aircraft_status_remarks(self) -> AsyncAircraftStatusRemarksResource:
        from .resources.aircraft_status_remarks import AsyncAircraftStatusRemarksResource

        return AsyncAircraftStatusRemarksResource(self)

    @cached_property
    def aircraft_statuses(self) -> AsyncAircraftStatusesResource:
        from .resources.aircraft_statuses import AsyncAircraftStatusesResource

        return AsyncAircraftStatusesResource(self)

    @cached_property
    def airfield_slot_consumptions(self) -> AsyncAirfieldSlotConsumptionsResource:
        from .resources.airfield_slot_consumptions import AsyncAirfieldSlotConsumptionsResource

        return AsyncAirfieldSlotConsumptionsResource(self)

    @cached_property
    def airfield_slots(self) -> AsyncAirfieldSlotsResource:
        from .resources.airfield_slots import AsyncAirfieldSlotsResource

        return AsyncAirfieldSlotsResource(self)

    @cached_property
    def airfield_status(self) -> AsyncAirfieldStatusResource:
        from .resources.airfield_status import AsyncAirfieldStatusResource

        return AsyncAirfieldStatusResource(self)

    @cached_property
    def airfields(self) -> AsyncAirfieldsResource:
        from .resources.airfields import AsyncAirfieldsResource

        return AsyncAirfieldsResource(self)

    @cached_property
    def airload_plans(self) -> AsyncAirloadPlansResource:
        from .resources.airload_plans import AsyncAirloadPlansResource

        return AsyncAirloadPlansResource(self)

    @cached_property
    def airspace_control_orders(self) -> AsyncAirspaceControlOrdersResource:
        from .resources.airspace_control_orders import AsyncAirspaceControlOrdersResource

        return AsyncAirspaceControlOrdersResource(self)

    @cached_property
    def ais(self) -> AsyncAIsResource:
        from .resources.ais import AsyncAIsResource

        return AsyncAIsResource(self)

    @cached_property
    def ais_objects(self) -> AsyncAIsObjectsResource:
        from .resources.ais_objects import AsyncAIsObjectsResource

        return AsyncAIsObjectsResource(self)

    @cached_property
    def analytic_imagery(self) -> AsyncAnalyticImageryResource:
        from .resources.analytic_imagery import AsyncAnalyticImageryResource

        return AsyncAnalyticImageryResource(self)

    @cached_property
    def antennas(self) -> AsyncAntennasResource:
        from .resources.antennas import AsyncAntennasResource

        return AsyncAntennasResource(self)

    @cached_property
    def attitude_data(self) -> AsyncAttitudeDataResource:
        from .resources.attitude_data import AsyncAttitudeDataResource

        return AsyncAttitudeDataResource(self)

    @cached_property
    def attitude_sets(self) -> AsyncAttitudeSetsResource:
        from .resources.attitude_sets import AsyncAttitudeSetsResource

        return AsyncAttitudeSetsResource(self)

    @cached_property
    def aviation_risk_management(self) -> AsyncAviationRiskManagementResource:
        from .resources.aviation_risk_management import AsyncAviationRiskManagementResource

        return AsyncAviationRiskManagementResource(self)

    @cached_property
    def batteries(self) -> AsyncBatteriesResource:
        from .resources.batteries import AsyncBatteriesResource

        return AsyncBatteriesResource(self)

    @cached_property
    def batterydetails(self) -> AsyncBatterydetailsResource:
        from .resources.batterydetails import AsyncBatterydetailsResource

        return AsyncBatterydetailsResource(self)

    @cached_property
    def beam(self) -> AsyncBeamResource:
        from .resources.beam import AsyncBeamResource

        return AsyncBeamResource(self)

    @cached_property
    def beam_contours(self) -> AsyncBeamContoursResource:
        from .resources.beam_contours import AsyncBeamContoursResource

        return AsyncBeamContoursResource(self)

    @cached_property
    def buses(self) -> AsyncBusesResource:
        from .resources.buses import AsyncBusesResource

        return AsyncBusesResource(self)

    @cached_property
    def channels(self) -> AsyncChannelsResource:
        from .resources.channels import AsyncChannelsResource

        return AsyncChannelsResource(self)

    @cached_property
    def closelyspacedobjects(self) -> AsyncCloselyspacedobjectsResource:
        from .resources.closelyspacedobjects import AsyncCloselyspacedobjectsResource

        return AsyncCloselyspacedobjectsResource(self)

    @cached_property
    def collect_requests(self) -> AsyncCollectRequestsResource:
        from .resources.collect_requests import AsyncCollectRequestsResource

        return AsyncCollectRequestsResource(self)

    @cached_property
    def collect_responses(self) -> AsyncCollectResponsesResource:
        from .resources.collect_responses import AsyncCollectResponsesResource

        return AsyncCollectResponsesResource(self)

    @cached_property
    def comm(self) -> AsyncCommResource:
        from .resources.comm import AsyncCommResource

        return AsyncCommResource(self)

    @cached_property
    def conjunctions(self) -> AsyncConjunctionsResource:
        from .resources.conjunctions import AsyncConjunctionsResource

        return AsyncConjunctionsResource(self)

    @cached_property
    def cots(self) -> AsyncCotsResource:
        from .resources.cots import AsyncCotsResource

        return AsyncCotsResource(self)

    @cached_property
    def countries(self) -> AsyncCountriesResource:
        from .resources.countries import AsyncCountriesResource

        return AsyncCountriesResource(self)

    @cached_property
    def crew(self) -> AsyncCrewResource:
        from .resources.crew import AsyncCrewResource

        return AsyncCrewResource(self)

    @cached_property
    def deconflictset(self) -> AsyncDeconflictsetResource:
        from .resources.deconflictset import AsyncDeconflictsetResource

        return AsyncDeconflictsetResource(self)

    @cached_property
    def diff_of_arrival(self) -> AsyncDiffOfArrivalResource:
        from .resources.diff_of_arrival import AsyncDiffOfArrivalResource

        return AsyncDiffOfArrivalResource(self)

    @cached_property
    def diplomatic_clearance(self) -> AsyncDiplomaticClearanceResource:
        from .resources.diplomatic_clearance import AsyncDiplomaticClearanceResource

        return AsyncDiplomaticClearanceResource(self)

    @cached_property
    def drift_history(self) -> AsyncDriftHistoryResource:
        from .resources.drift_history import AsyncDriftHistoryResource

        return AsyncDriftHistoryResource(self)

    @cached_property
    def dropzone(self) -> AsyncDropzoneResource:
        from .resources.dropzone import AsyncDropzoneResource

        return AsyncDropzoneResource(self)

    @cached_property
    def ecpedr(self) -> AsyncEcpedrResource:
        from .resources.ecpedr import AsyncEcpedrResource

        return AsyncEcpedrResource(self)

    @cached_property
    def effect_requests(self) -> AsyncEffectRequestsResource:
        from .resources.effect_requests import AsyncEffectRequestsResource

        return AsyncEffectRequestsResource(self)

    @cached_property
    def effect_responses(self) -> AsyncEffectResponsesResource:
        from .resources.effect_responses import AsyncEffectResponsesResource

        return AsyncEffectResponsesResource(self)

    @cached_property
    def elsets(self) -> AsyncElsetsResource:
        from .resources.elsets import AsyncElsetsResource

        return AsyncElsetsResource(self)

    @cached_property
    def emireport(self) -> AsyncEmireportResource:
        from .resources.emireport import AsyncEmireportResource

        return AsyncEmireportResource(self)

    @cached_property
    def emitter_geolocation(self) -> AsyncEmitterGeolocationResource:
        from .resources.emitter_geolocation import AsyncEmitterGeolocationResource

        return AsyncEmitterGeolocationResource(self)

    @cached_property
    def engine_details(self) -> AsyncEngineDetailsResource:
        from .resources.engine_details import AsyncEngineDetailsResource

        return AsyncEngineDetailsResource(self)

    @cached_property
    def engines(self) -> AsyncEnginesResource:
        from .resources.engines import AsyncEnginesResource

        return AsyncEnginesResource(self)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        from .resources.entities import AsyncEntitiesResource

        return AsyncEntitiesResource(self)

    @cached_property
    def eop(self) -> AsyncEopResource:
        from .resources.eop import AsyncEopResource

        return AsyncEopResource(self)

    @cached_property
    def ephemeris(self) -> AsyncEphemerisResource:
        from .resources.ephemeris import AsyncEphemerisResource

        return AsyncEphemerisResource(self)

    @cached_property
    def ephemeris_sets(self) -> AsyncEphemerisSetsResource:
        from .resources.ephemeris_sets import AsyncEphemerisSetsResource

        return AsyncEphemerisSetsResource(self)

    @cached_property
    def equipment(self) -> AsyncEquipmentResource:
        from .resources.equipment import AsyncEquipmentResource

        return AsyncEquipmentResource(self)

    @cached_property
    def equipment_remarks(self) -> AsyncEquipmentRemarksResource:
        from .resources.equipment_remarks import AsyncEquipmentRemarksResource

        return AsyncEquipmentRemarksResource(self)

    @cached_property
    def evac(self) -> AsyncEvacResource:
        from .resources.evac import AsyncEvacResource

        return AsyncEvacResource(self)

    @cached_property
    def event_evolution(self) -> AsyncEventEvolutionResource:
        from .resources.event_evolution import AsyncEventEvolutionResource

        return AsyncEventEvolutionResource(self)

    @cached_property
    def feature_assessment(self) -> AsyncFeatureAssessmentResource:
        from .resources.feature_assessment import AsyncFeatureAssessmentResource

        return AsyncFeatureAssessmentResource(self)

    @cached_property
    def flightplan(self) -> AsyncFlightplanResource:
        from .resources.flightplan import AsyncFlightplanResource

        return AsyncFlightplanResource(self)

    @cached_property
    def geo_status(self) -> AsyncGeoStatusResource:
        from .resources.geo_status import AsyncGeoStatusResource

        return AsyncGeoStatusResource(self)

    @cached_property
    def global_atmospheric_model(self) -> AsyncGlobalAtmosphericModelResource:
        from .resources.global_atmospheric_model import AsyncGlobalAtmosphericModelResource

        return AsyncGlobalAtmosphericModelResource(self)

    @cached_property
    def gnss_observations(self) -> AsyncGnssObservationsResource:
        from .resources.gnss_observations import AsyncGnssObservationsResource

        return AsyncGnssObservationsResource(self)

    @cached_property
    def gnss_observationset(self) -> AsyncGnssObservationsetResource:
        from .resources.gnss_observationset import AsyncGnssObservationsetResource

        return AsyncGnssObservationsetResource(self)

    @cached_property
    def gnss_raw_if(self) -> AsyncGnssRawIfResource:
        from .resources.gnss_raw_if import AsyncGnssRawIfResource

        return AsyncGnssRawIfResource(self)

    @cached_property
    def ground_imagery(self) -> AsyncGroundImageryResource:
        from .resources.ground_imagery import AsyncGroundImageryResource

        return AsyncGroundImageryResource(self)

    @cached_property
    def h3_geo(self) -> AsyncH3GeoResource:
        from .resources.h3_geo import AsyncH3GeoResource

        return AsyncH3GeoResource(self)

    @cached_property
    def h3_geo_hex_cell(self) -> AsyncH3GeoHexCellResource:
        from .resources.h3_geo_hex_cell import AsyncH3GeoHexCellResource

        return AsyncH3GeoHexCellResource(self)

    @cached_property
    def hazard(self) -> AsyncHazardResource:
        from .resources.hazard import AsyncHazardResource

        return AsyncHazardResource(self)

    @cached_property
    def iono_observations(self) -> AsyncIonoObservationsResource:
        from .resources.iono_observations import AsyncIonoObservationsResource

        return AsyncIonoObservationsResource(self)

    @cached_property
    def ir(self) -> AsyncIrResource:
        from .resources.ir import AsyncIrResource

        return AsyncIrResource(self)

    @cached_property
    def isr_collections(self) -> AsyncIsrCollectionsResource:
        from .resources.isr_collections import AsyncIsrCollectionsResource

        return AsyncIsrCollectionsResource(self)

    @cached_property
    def item(self) -> AsyncItemResource:
        from .resources.item import AsyncItemResource

        return AsyncItemResource(self)

    @cached_property
    def item_trackings(self) -> AsyncItemTrackingsResource:
        from .resources.item_trackings import AsyncItemTrackingsResource

        return AsyncItemTrackingsResource(self)

    @cached_property
    def laserdeconflictrequest(self) -> AsyncLaserdeconflictrequestResource:
        from .resources.laserdeconflictrequest import AsyncLaserdeconflictrequestResource

        return AsyncLaserdeconflictrequestResource(self)

    @cached_property
    def laseremitter(self) -> AsyncLaseremitterResource:
        from .resources.laseremitter import AsyncLaseremitterResource

        return AsyncLaseremitterResource(self)

    @cached_property
    def launch_detection(self) -> AsyncLaunchDetectionResource:
        from .resources.launch_detection import AsyncLaunchDetectionResource

        return AsyncLaunchDetectionResource(self)

    @cached_property
    def launch_event(self) -> AsyncLaunchEventResource:
        from .resources.launch_event import AsyncLaunchEventResource

        return AsyncLaunchEventResource(self)

    @cached_property
    def launch_site(self) -> AsyncLaunchSiteResource:
        from .resources.launch_site import AsyncLaunchSiteResource

        return AsyncLaunchSiteResource(self)

    @cached_property
    def launch_site_details(self) -> AsyncLaunchSiteDetailsResource:
        from .resources.launch_site_details import AsyncLaunchSiteDetailsResource

        return AsyncLaunchSiteDetailsResource(self)

    @cached_property
    def launch_vehicle(self) -> AsyncLaunchVehicleResource:
        from .resources.launch_vehicle import AsyncLaunchVehicleResource

        return AsyncLaunchVehicleResource(self)

    @cached_property
    def launch_vehicle_details(self) -> AsyncLaunchVehicleDetailsResource:
        from .resources.launch_vehicle_details import AsyncLaunchVehicleDetailsResource

        return AsyncLaunchVehicleDetailsResource(self)

    @cached_property
    def link_status(self) -> AsyncLinkStatusResource:
        from .resources.link_status import AsyncLinkStatusResource

        return AsyncLinkStatusResource(self)

    @cached_property
    def linkstatus(self) -> AsyncLinkstatusResource:
        from .resources.linkstatus import AsyncLinkstatusResource

        return AsyncLinkstatusResource(self)

    @cached_property
    def location(self) -> AsyncLocationResource:
        from .resources.location import AsyncLocationResource

        return AsyncLocationResource(self)

    @cached_property
    def logistics_support(self) -> AsyncLogisticsSupportResource:
        from .resources.logistics_support import AsyncLogisticsSupportResource

        return AsyncLogisticsSupportResource(self)

    @cached_property
    def maneuvers(self) -> AsyncManeuversResource:
        from .resources.maneuvers import AsyncManeuversResource

        return AsyncManeuversResource(self)

    @cached_property
    def manifold(self) -> AsyncManifoldResource:
        from .resources.manifold import AsyncManifoldResource

        return AsyncManifoldResource(self)

    @cached_property
    def manifoldelset(self) -> AsyncManifoldelsetResource:
        from .resources.manifoldelset import AsyncManifoldelsetResource

        return AsyncManifoldelsetResource(self)

    @cached_property
    def missile_tracks(self) -> AsyncMissileTracksResource:
        from .resources.missile_tracks import AsyncMissileTracksResource

        return AsyncMissileTracksResource(self)

    @cached_property
    def mission_assignment(self) -> AsyncMissionAssignmentResource:
        from .resources.mission_assignment import AsyncMissionAssignmentResource

        return AsyncMissionAssignmentResource(self)

    @cached_property
    def mti(self) -> AsyncMtiResource:
        from .resources.mti import AsyncMtiResource

        return AsyncMtiResource(self)

    @cached_property
    def navigation(self) -> AsyncNavigationResource:
        from .resources.navigation import AsyncNavigationResource

        return AsyncNavigationResource(self)

    @cached_property
    def navigational_obstruction(self) -> AsyncNavigationalObstructionResource:
        from .resources.navigational_obstruction import AsyncNavigationalObstructionResource

        return AsyncNavigationalObstructionResource(self)

    @cached_property
    def notification(self) -> AsyncNotificationResource:
        from .resources.notification import AsyncNotificationResource

        return AsyncNotificationResource(self)

    @cached_property
    def object_of_interest(self) -> AsyncObjectOfInterestResource:
        from .resources.object_of_interest import AsyncObjectOfInterestResource

        return AsyncObjectOfInterestResource(self)

    @cached_property
    def observations(self) -> AsyncObservationsResource:
        from .resources.observations import AsyncObservationsResource

        return AsyncObservationsResource(self)

    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResource:
        from .resources.onboardnavigation import AsyncOnboardnavigationResource

        return AsyncOnboardnavigationResource(self)

    @cached_property
    def onorbit(self) -> AsyncOnorbitResource:
        from .resources.onorbit import AsyncOnorbitResource

        return AsyncOnorbitResource(self)

    @cached_property
    def onorbitantenna(self) -> AsyncOnorbitantennaResource:
        from .resources.onorbitantenna import AsyncOnorbitantennaResource

        return AsyncOnorbitantennaResource(self)

    @cached_property
    def onorbitbattery(self) -> AsyncOnorbitbatteryResource:
        from .resources.onorbitbattery import AsyncOnorbitbatteryResource

        return AsyncOnorbitbatteryResource(self)

    @cached_property
    def onorbitdetails(self) -> AsyncOnorbitdetailsResource:
        from .resources.onorbitdetails import AsyncOnorbitdetailsResource

        return AsyncOnorbitdetailsResource(self)

    @cached_property
    def onorbitevent(self) -> AsyncOnorbiteventResource:
        from .resources.onorbitevent import AsyncOnorbiteventResource

        return AsyncOnorbiteventResource(self)

    @cached_property
    def onorbitlist(self) -> AsyncOnorbitlistResource:
        from .resources.onorbitlist import AsyncOnorbitlistResource

        return AsyncOnorbitlistResource(self)

    @cached_property
    def onorbitsolararray(self) -> AsyncOnorbitsolararrayResource:
        from .resources.onorbitsolararray import AsyncOnorbitsolararrayResource

        return AsyncOnorbitsolararrayResource(self)

    @cached_property
    def onorbitthruster(self) -> AsyncOnorbitthrusterResource:
        from .resources.onorbitthruster import AsyncOnorbitthrusterResource

        return AsyncOnorbitthrusterResource(self)

    @cached_property
    def onorbitthrusterstatus(self) -> AsyncOnorbitthrusterstatusResource:
        from .resources.onorbitthrusterstatus import AsyncOnorbitthrusterstatusResource

        return AsyncOnorbitthrusterstatusResource(self)

    @cached_property
    def onorbitassessment(self) -> AsyncOnorbitassessmentResource:
        from .resources.onorbitassessment import AsyncOnorbitassessmentResource

        return AsyncOnorbitassessmentResource(self)

    @cached_property
    def operatingunit(self) -> AsyncOperatingunitResource:
        from .resources.operatingunit import AsyncOperatingunitResource

        return AsyncOperatingunitResource(self)

    @cached_property
    def operatingunitremark(self) -> AsyncOperatingunitremarkResource:
        from .resources.operatingunitremark import AsyncOperatingunitremarkResource

        return AsyncOperatingunitremarkResource(self)

    @cached_property
    def orbitdetermination(self) -> AsyncOrbitdeterminationResource:
        from .resources.orbitdetermination import AsyncOrbitdeterminationResource

        return AsyncOrbitdeterminationResource(self)

    @cached_property
    def orbittrack(self) -> AsyncOrbittrackResource:
        from .resources.orbittrack import AsyncOrbittrackResource

        return AsyncOrbittrackResource(self)

    @cached_property
    def organization(self) -> AsyncOrganizationResource:
        from .resources.organization import AsyncOrganizationResource

        return AsyncOrganizationResource(self)

    @cached_property
    def organizationdetails(self) -> AsyncOrganizationdetailsResource:
        from .resources.organizationdetails import AsyncOrganizationdetailsResource

        return AsyncOrganizationdetailsResource(self)

    @cached_property
    def personnelrecovery(self) -> AsyncPersonnelrecoveryResource:
        from .resources.personnelrecovery import AsyncPersonnelrecoveryResource

        return AsyncPersonnelrecoveryResource(self)

    @cached_property
    def poi(self) -> AsyncPoiResource:
        from .resources.poi import AsyncPoiResource

        return AsyncPoiResource(self)

    @cached_property
    def port(self) -> AsyncPortResource:
        from .resources.port import AsyncPortResource

        return AsyncPortResource(self)

    @cached_property
    def report_and_activities(self) -> AsyncReportAndActivitiesResource:
        from .resources.report_and_activities import AsyncReportAndActivitiesResource

        return AsyncReportAndActivitiesResource(self)

    @cached_property
    def rf_band(self) -> AsyncRfBandResource:
        from .resources.rf_band import AsyncRfBandResource

        return AsyncRfBandResource(self)

    @cached_property
    def rf_band_type(self) -> AsyncRfBandTypeResource:
        from .resources.rf_band_type import AsyncRfBandTypeResource

        return AsyncRfBandTypeResource(self)

    @cached_property
    def rf_emitter(self) -> AsyncRfEmitterResource:
        from .resources.rf_emitter import AsyncRfEmitterResource

        return AsyncRfEmitterResource(self)

    @cached_property
    def route_stats(self) -> AsyncRouteStatsResource:
        from .resources.route_stats import AsyncRouteStatsResource

        return AsyncRouteStatsResource(self)

    @cached_property
    def sar_observation(self) -> AsyncSarObservationResource:
        from .resources.sar_observation import AsyncSarObservationResource

        return AsyncSarObservationResource(self)

    @cached_property
    def scientific(self) -> AsyncScientificResource:
        from .resources.scientific import AsyncScientificResource

        return AsyncScientificResource(self)

    @cached_property
    def scs(self) -> AsyncScsResource:
        from .resources.scs import AsyncScsResource

        return AsyncScsResource(self)

    @cached_property
    def secure_messaging(self) -> AsyncSecureMessagingResource:
        from .resources.secure_messaging import AsyncSecureMessagingResource

        return AsyncSecureMessagingResource(self)

    @cached_property
    def sensor(self) -> AsyncSensorResource:
        from .resources.sensor import AsyncSensorResource

        return AsyncSensorResource(self)

    @cached_property
    def sensor_stating(self) -> AsyncSensorStatingResource:
        from .resources.sensor_stating import AsyncSensorStatingResource

        return AsyncSensorStatingResource(self)

    @cached_property
    def sensor_maintenance(self) -> AsyncSensorMaintenanceResource:
        from .resources.sensor_maintenance import AsyncSensorMaintenanceResource

        return AsyncSensorMaintenanceResource(self)

    @cached_property
    def sensor_observation_type(self) -> AsyncSensorObservationTypeResource:
        from .resources.sensor_observation_type import AsyncSensorObservationTypeResource

        return AsyncSensorObservationTypeResource(self)

    @cached_property
    def sensor_plan(self) -> AsyncSensorPlanResource:
        from .resources.sensor_plan import AsyncSensorPlanResource

        return AsyncSensorPlanResource(self)

    @cached_property
    def sensor_type(self) -> AsyncSensorTypeResource:
        from .resources.sensor_type import AsyncSensorTypeResource

        return AsyncSensorTypeResource(self)

    @cached_property
    def sera_data_comm_details(self) -> AsyncSeraDataCommDetailsResource:
        from .resources.sera_data_comm_details import AsyncSeraDataCommDetailsResource

        return AsyncSeraDataCommDetailsResource(self)

    @cached_property
    def sera_data_early_warning(self) -> AsyncSeraDataEarlyWarningResource:
        from .resources.sera_data_early_warning import AsyncSeraDataEarlyWarningResource

        return AsyncSeraDataEarlyWarningResource(self)

    @cached_property
    def sera_data_navigation(self) -> AsyncSeraDataNavigationResource:
        from .resources.sera_data_navigation import AsyncSeraDataNavigationResource

        return AsyncSeraDataNavigationResource(self)

    @cached_property
    def seradata_optical_payload(self) -> AsyncSeradataOpticalPayloadResource:
        from .resources.seradata_optical_payload import AsyncSeradataOpticalPayloadResource

        return AsyncSeradataOpticalPayloadResource(self)

    @cached_property
    def seradata_radar_payload(self) -> AsyncSeradataRadarPayloadResource:
        from .resources.seradata_radar_payload import AsyncSeradataRadarPayloadResource

        return AsyncSeradataRadarPayloadResource(self)

    @cached_property
    def seradata_sigint_payload(self) -> AsyncSeradataSigintPayloadResource:
        from .resources.seradata_sigint_payload import AsyncSeradataSigintPayloadResource

        return AsyncSeradataSigintPayloadResource(self)

    @cached_property
    def seradata_spacecraft_details(self) -> AsyncSeradataSpacecraftDetailsResource:
        from .resources.seradata_spacecraft_details import AsyncSeradataSpacecraftDetailsResource

        return AsyncSeradataSpacecraftDetailsResource(self)

    @cached_property
    def sgi(self) -> AsyncSgiResource:
        from .resources.sgi import AsyncSgiResource

        return AsyncSgiResource(self)

    @cached_property
    def sigact(self) -> AsyncSigactResource:
        from .resources.sigact import AsyncSigactResource

        return AsyncSigactResource(self)

    @cached_property
    def site(self) -> AsyncSiteResource:
        from .resources.site import AsyncSiteResource

        return AsyncSiteResource(self)

    @cached_property
    def site_remark(self) -> AsyncSiteRemarkResource:
        from .resources.site_remark import AsyncSiteRemarkResource

        return AsyncSiteRemarkResource(self)

    @cached_property
    def site_status(self) -> AsyncSiteStatusResource:
        from .resources.site_status import AsyncSiteStatusResource

        return AsyncSiteStatusResource(self)

    @cached_property
    def sky_imagery(self) -> AsyncSkyImageryResource:
        from .resources.sky_imagery import AsyncSkyImageryResource

        return AsyncSkyImageryResource(self)

    @cached_property
    def soi_observation_set(self) -> AsyncSoiObservationSetResource:
        from .resources.soi_observation_set import AsyncSoiObservationSetResource

        return AsyncSoiObservationSetResource(self)

    @cached_property
    def solar_array(self) -> AsyncSolarArrayResource:
        from .resources.solar_array import AsyncSolarArrayResource

        return AsyncSolarArrayResource(self)

    @cached_property
    def solar_array_details(self) -> AsyncSolarArrayDetailsResource:
        from .resources.solar_array_details import AsyncSolarArrayDetailsResource

        return AsyncSolarArrayDetailsResource(self)

    @cached_property
    def sortie_ppr(self) -> AsyncSortiePprResource:
        from .resources.sortie_ppr import AsyncSortiePprResource

        return AsyncSortiePprResource(self)

    @cached_property
    def space_env_observation(self) -> AsyncSpaceEnvObservationResource:
        from .resources.space_env_observation import AsyncSpaceEnvObservationResource

        return AsyncSpaceEnvObservationResource(self)

    @cached_property
    def stage(self) -> AsyncStageResource:
        from .resources.stage import AsyncStageResource

        return AsyncStageResource(self)

    @cached_property
    def star_catalog(self) -> AsyncStarCatalogResource:
        from .resources.star_catalog import AsyncStarCatalogResource

        return AsyncStarCatalogResource(self)

    @cached_property
    def state_vector(self) -> AsyncStateVectorResource:
        from .resources.state_vector import AsyncStateVectorResource

        return AsyncStateVectorResource(self)

    @cached_property
    def status(self) -> AsyncStatusResource:
        from .resources.status import AsyncStatusResource

        return AsyncStatusResource(self)

    @cached_property
    def substatus(self) -> AsyncSubstatusResource:
        from .resources.substatus import AsyncSubstatusResource

        return AsyncSubstatusResource(self)

    @cached_property
    def supporting_data(self) -> AsyncSupportingDataResource:
        from .resources.supporting_data import AsyncSupportingDataResource

        return AsyncSupportingDataResource(self)

    @cached_property
    def surface(self) -> AsyncSurfaceResource:
        from .resources.surface import AsyncSurfaceResource

        return AsyncSurfaceResource(self)

    @cached_property
    def surface_obstruction(self) -> AsyncSurfaceObstructionResource:
        from .resources.surface_obstruction import AsyncSurfaceObstructionResource

        return AsyncSurfaceObstructionResource(self)

    @cached_property
    def swir(self) -> AsyncSwirResource:
        from .resources.swir import AsyncSwirResource

        return AsyncSwirResource(self)

    @cached_property
    def tai_utc(self) -> AsyncTaiUtcResource:
        from .resources.tai_utc import AsyncTaiUtcResource

        return AsyncTaiUtcResource(self)

    @cached_property
    def tdoa_fdoa(self) -> AsyncTdoaFdoaResource:
        from .resources.tdoa_fdoa import AsyncTdoaFdoaResource

        return AsyncTdoaFdoaResource(self)

    @cached_property
    def track(self) -> AsyncTrackResource:
        from .resources.track import AsyncTrackResource

        return AsyncTrackResource(self)

    @cached_property
    def track_details(self) -> AsyncTrackDetailsResource:
        from .resources.track_details import AsyncTrackDetailsResource

        return AsyncTrackDetailsResource(self)

    @cached_property
    def track_route(self) -> AsyncTrackRouteResource:
        from .resources.track_route import AsyncTrackRouteResource

        return AsyncTrackRouteResource(self)

    @cached_property
    def transponder(self) -> AsyncTransponderResource:
        from .resources.transponder import AsyncTransponderResource

        return AsyncTransponderResource(self)

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def vessel(self) -> AsyncVesselResource:
        from .resources.vessel import AsyncVesselResource

        return AsyncVesselResource(self)

    @cached_property
    def video(self) -> AsyncVideoResource:
        from .resources.video import AsyncVideoResource

        return AsyncVideoResource(self)

    @cached_property
    def weather_data(self) -> AsyncWeatherDataResource:
        from .resources.weather_data import AsyncWeatherDataResource

        return AsyncWeatherDataResource(self)

    @cached_property
    def weather_report(self) -> AsyncWeatherReportResource:
        from .resources.weather_report import AsyncWeatherReportResource

        return AsyncWeatherReportResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncUnifieddatalibraryWithRawResponse:
        return AsyncUnifieddatalibraryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnifieddatalibraryWithStreamedResponse:
        return AsyncUnifieddatalibraryWithStreamedResponse(self)

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
        access_token: str | None = None,
        password: str | None = None,
        username: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            access_token=access_token or self.access_token,
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
    _client: Unifieddatalibrary

    def __init__(self, client: Unifieddatalibrary) -> None:
        self._client = client

    @cached_property
    def air_events(self) -> air_events.AirEventsResourceWithRawResponse:
        from .resources.air_events import AirEventsResourceWithRawResponse

        return AirEventsResourceWithRawResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AirOperationsResourceWithRawResponse:
        from .resources.air_operations import AirOperationsResourceWithRawResponse

        return AirOperationsResourceWithRawResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AirTransportMissionsResourceWithRawResponse:
        from .resources.air_transport_missions import AirTransportMissionsResourceWithRawResponse

        return AirTransportMissionsResourceWithRawResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AircraftResourceWithRawResponse:
        from .resources.aircraft import AircraftResourceWithRawResponse

        return AircraftResourceWithRawResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AircraftSortiesResourceWithRawResponse:
        from .resources.aircraft_sorties import AircraftSortiesResourceWithRawResponse

        return AircraftSortiesResourceWithRawResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(self) -> aircraft_status_remarks.AircraftStatusRemarksResourceWithRawResponse:
        from .resources.aircraft_status_remarks import AircraftStatusRemarksResourceWithRawResponse

        return AircraftStatusRemarksResourceWithRawResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AircraftStatusesResourceWithRawResponse:
        from .resources.aircraft_statuses import AircraftStatusesResourceWithRawResponse

        return AircraftStatusesResourceWithRawResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(self) -> airfield_slot_consumptions.AirfieldSlotConsumptionsResourceWithRawResponse:
        from .resources.airfield_slot_consumptions import AirfieldSlotConsumptionsResourceWithRawResponse

        return AirfieldSlotConsumptionsResourceWithRawResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AirfieldSlotsResourceWithRawResponse:
        from .resources.airfield_slots import AirfieldSlotsResourceWithRawResponse

        return AirfieldSlotsResourceWithRawResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AirfieldStatusResourceWithRawResponse:
        from .resources.airfield_status import AirfieldStatusResourceWithRawResponse

        return AirfieldStatusResourceWithRawResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AirfieldsResourceWithRawResponse:
        from .resources.airfields import AirfieldsResourceWithRawResponse

        return AirfieldsResourceWithRawResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AirloadPlansResourceWithRawResponse:
        from .resources.airload_plans import AirloadPlansResourceWithRawResponse

        return AirloadPlansResourceWithRawResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(self) -> airspace_control_orders.AirspaceControlOrdersResourceWithRawResponse:
        from .resources.airspace_control_orders import AirspaceControlOrdersResourceWithRawResponse

        return AirspaceControlOrdersResourceWithRawResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AIsResourceWithRawResponse:
        from .resources.ais import AIsResourceWithRawResponse

        return AIsResourceWithRawResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AIsObjectsResourceWithRawResponse:
        from .resources.ais_objects import AIsObjectsResourceWithRawResponse

        return AIsObjectsResourceWithRawResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AnalyticImageryResourceWithRawResponse:
        from .resources.analytic_imagery import AnalyticImageryResourceWithRawResponse

        return AnalyticImageryResourceWithRawResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AntennasResourceWithRawResponse:
        from .resources.antennas import AntennasResourceWithRawResponse

        return AntennasResourceWithRawResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AttitudeDataResourceWithRawResponse:
        from .resources.attitude_data import AttitudeDataResourceWithRawResponse

        return AttitudeDataResourceWithRawResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AttitudeSetsResourceWithRawResponse:
        from .resources.attitude_sets import AttitudeSetsResourceWithRawResponse

        return AttitudeSetsResourceWithRawResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(self) -> aviation_risk_management.AviationRiskManagementResourceWithRawResponse:
        from .resources.aviation_risk_management import AviationRiskManagementResourceWithRawResponse

        return AviationRiskManagementResourceWithRawResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.BatteriesResourceWithRawResponse:
        from .resources.batteries import BatteriesResourceWithRawResponse

        return BatteriesResourceWithRawResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.BatterydetailsResourceWithRawResponse:
        from .resources.batterydetails import BatterydetailsResourceWithRawResponse

        return BatterydetailsResourceWithRawResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.BeamResourceWithRawResponse:
        from .resources.beam import BeamResourceWithRawResponse

        return BeamResourceWithRawResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.BeamContoursResourceWithRawResponse:
        from .resources.beam_contours import BeamContoursResourceWithRawResponse

        return BeamContoursResourceWithRawResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.BusesResourceWithRawResponse:
        from .resources.buses import BusesResourceWithRawResponse

        return BusesResourceWithRawResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithRawResponse:
        from .resources.channels import ChannelsResourceWithRawResponse

        return ChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.CloselyspacedobjectsResourceWithRawResponse:
        from .resources.closelyspacedobjects import CloselyspacedobjectsResourceWithRawResponse

        return CloselyspacedobjectsResourceWithRawResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.CollectRequestsResourceWithRawResponse:
        from .resources.collect_requests import CollectRequestsResourceWithRawResponse

        return CollectRequestsResourceWithRawResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.CollectResponsesResourceWithRawResponse:
        from .resources.collect_responses import CollectResponsesResourceWithRawResponse

        return CollectResponsesResourceWithRawResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.CommResourceWithRawResponse:
        from .resources.comm import CommResourceWithRawResponse

        return CommResourceWithRawResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.ConjunctionsResourceWithRawResponse:
        from .resources.conjunctions import ConjunctionsResourceWithRawResponse

        return ConjunctionsResourceWithRawResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.CotsResourceWithRawResponse:
        from .resources.cots import CotsResourceWithRawResponse

        return CotsResourceWithRawResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.CountriesResourceWithRawResponse:
        from .resources.countries import CountriesResourceWithRawResponse

        return CountriesResourceWithRawResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.CrewResourceWithRawResponse:
        from .resources.crew import CrewResourceWithRawResponse

        return CrewResourceWithRawResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.DeconflictsetResourceWithRawResponse:
        from .resources.deconflictset import DeconflictsetResourceWithRawResponse

        return DeconflictsetResourceWithRawResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.DiffOfArrivalResourceWithRawResponse:
        from .resources.diff_of_arrival import DiffOfArrivalResourceWithRawResponse

        return DiffOfArrivalResourceWithRawResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.DiplomaticClearanceResourceWithRawResponse:
        from .resources.diplomatic_clearance import DiplomaticClearanceResourceWithRawResponse

        return DiplomaticClearanceResourceWithRawResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.DriftHistoryResourceWithRawResponse:
        from .resources.drift_history import DriftHistoryResourceWithRawResponse

        return DriftHistoryResourceWithRawResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.DropzoneResourceWithRawResponse:
        from .resources.dropzone import DropzoneResourceWithRawResponse

        return DropzoneResourceWithRawResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.EcpedrResourceWithRawResponse:
        from .resources.ecpedr import EcpedrResourceWithRawResponse

        return EcpedrResourceWithRawResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.EffectRequestsResourceWithRawResponse:
        from .resources.effect_requests import EffectRequestsResourceWithRawResponse

        return EffectRequestsResourceWithRawResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.EffectResponsesResourceWithRawResponse:
        from .resources.effect_responses import EffectResponsesResourceWithRawResponse

        return EffectResponsesResourceWithRawResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.ElsetsResourceWithRawResponse:
        from .resources.elsets import ElsetsResourceWithRawResponse

        return ElsetsResourceWithRawResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.EmireportResourceWithRawResponse:
        from .resources.emireport import EmireportResourceWithRawResponse

        return EmireportResourceWithRawResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.EmitterGeolocationResourceWithRawResponse:
        from .resources.emitter_geolocation import EmitterGeolocationResourceWithRawResponse

        return EmitterGeolocationResourceWithRawResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.EngineDetailsResourceWithRawResponse:
        from .resources.engine_details import EngineDetailsResourceWithRawResponse

        return EngineDetailsResourceWithRawResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.EnginesResourceWithRawResponse:
        from .resources.engines import EnginesResourceWithRawResponse

        return EnginesResourceWithRawResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithRawResponse:
        from .resources.entities import EntitiesResourceWithRawResponse

        return EntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.EopResourceWithRawResponse:
        from .resources.eop import EopResourceWithRawResponse

        return EopResourceWithRawResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.EphemerisResourceWithRawResponse:
        from .resources.ephemeris import EphemerisResourceWithRawResponse

        return EphemerisResourceWithRawResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.EphemerisSetsResourceWithRawResponse:
        from .resources.ephemeris_sets import EphemerisSetsResourceWithRawResponse

        return EphemerisSetsResourceWithRawResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.EquipmentResourceWithRawResponse:
        from .resources.equipment import EquipmentResourceWithRawResponse

        return EquipmentResourceWithRawResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.EquipmentRemarksResourceWithRawResponse:
        from .resources.equipment_remarks import EquipmentRemarksResourceWithRawResponse

        return EquipmentRemarksResourceWithRawResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.EvacResourceWithRawResponse:
        from .resources.evac import EvacResourceWithRawResponse

        return EvacResourceWithRawResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.EventEvolutionResourceWithRawResponse:
        from .resources.event_evolution import EventEvolutionResourceWithRawResponse

        return EventEvolutionResourceWithRawResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.FeatureAssessmentResourceWithRawResponse:
        from .resources.feature_assessment import FeatureAssessmentResourceWithRawResponse

        return FeatureAssessmentResourceWithRawResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.FlightplanResourceWithRawResponse:
        from .resources.flightplan import FlightplanResourceWithRawResponse

        return FlightplanResourceWithRawResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.GeoStatusResourceWithRawResponse:
        from .resources.geo_status import GeoStatusResourceWithRawResponse

        return GeoStatusResourceWithRawResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(self) -> global_atmospheric_model.GlobalAtmosphericModelResourceWithRawResponse:
        from .resources.global_atmospheric_model import GlobalAtmosphericModelResourceWithRawResponse

        return GlobalAtmosphericModelResourceWithRawResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.GnssObservationsResourceWithRawResponse:
        from .resources.gnss_observations import GnssObservationsResourceWithRawResponse

        return GnssObservationsResourceWithRawResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.GnssObservationsetResourceWithRawResponse:
        from .resources.gnss_observationset import GnssObservationsetResourceWithRawResponse

        return GnssObservationsetResourceWithRawResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.GnssRawIfResourceWithRawResponse:
        from .resources.gnss_raw_if import GnssRawIfResourceWithRawResponse

        return GnssRawIfResourceWithRawResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.GroundImageryResourceWithRawResponse:
        from .resources.ground_imagery import GroundImageryResourceWithRawResponse

        return GroundImageryResourceWithRawResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.H3GeoResourceWithRawResponse:
        from .resources.h3_geo import H3GeoResourceWithRawResponse

        return H3GeoResourceWithRawResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.H3GeoHexCellResourceWithRawResponse:
        from .resources.h3_geo_hex_cell import H3GeoHexCellResourceWithRawResponse

        return H3GeoHexCellResourceWithRawResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.HazardResourceWithRawResponse:
        from .resources.hazard import HazardResourceWithRawResponse

        return HazardResourceWithRawResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.IonoObservationsResourceWithRawResponse:
        from .resources.iono_observations import IonoObservationsResourceWithRawResponse

        return IonoObservationsResourceWithRawResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.IrResourceWithRawResponse:
        from .resources.ir import IrResourceWithRawResponse

        return IrResourceWithRawResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.IsrCollectionsResourceWithRawResponse:
        from .resources.isr_collections import IsrCollectionsResourceWithRawResponse

        return IsrCollectionsResourceWithRawResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.ItemResourceWithRawResponse:
        from .resources.item import ItemResourceWithRawResponse

        return ItemResourceWithRawResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.ItemTrackingsResourceWithRawResponse:
        from .resources.item_trackings import ItemTrackingsResourceWithRawResponse

        return ItemTrackingsResourceWithRawResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.LaserdeconflictrequestResourceWithRawResponse:
        from .resources.laserdeconflictrequest import LaserdeconflictrequestResourceWithRawResponse

        return LaserdeconflictrequestResourceWithRawResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.LaseremitterResourceWithRawResponse:
        from .resources.laseremitter import LaseremitterResourceWithRawResponse

        return LaseremitterResourceWithRawResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.LaunchDetectionResourceWithRawResponse:
        from .resources.launch_detection import LaunchDetectionResourceWithRawResponse

        return LaunchDetectionResourceWithRawResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.LaunchEventResourceWithRawResponse:
        from .resources.launch_event import LaunchEventResourceWithRawResponse

        return LaunchEventResourceWithRawResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.LaunchSiteResourceWithRawResponse:
        from .resources.launch_site import LaunchSiteResourceWithRawResponse

        return LaunchSiteResourceWithRawResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.LaunchSiteDetailsResourceWithRawResponse:
        from .resources.launch_site_details import LaunchSiteDetailsResourceWithRawResponse

        return LaunchSiteDetailsResourceWithRawResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.LaunchVehicleResourceWithRawResponse:
        from .resources.launch_vehicle import LaunchVehicleResourceWithRawResponse

        return LaunchVehicleResourceWithRawResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.LaunchVehicleDetailsResourceWithRawResponse:
        from .resources.launch_vehicle_details import LaunchVehicleDetailsResourceWithRawResponse

        return LaunchVehicleDetailsResourceWithRawResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.LinkStatusResourceWithRawResponse:
        from .resources.link_status import LinkStatusResourceWithRawResponse

        return LinkStatusResourceWithRawResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.LinkstatusResourceWithRawResponse:
        from .resources.linkstatus import LinkstatusResourceWithRawResponse

        return LinkstatusResourceWithRawResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.LocationResourceWithRawResponse:
        from .resources.location import LocationResourceWithRawResponse

        return LocationResourceWithRawResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.LogisticsSupportResourceWithRawResponse:
        from .resources.logistics_support import LogisticsSupportResourceWithRawResponse

        return LogisticsSupportResourceWithRawResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.ManeuversResourceWithRawResponse:
        from .resources.maneuvers import ManeuversResourceWithRawResponse

        return ManeuversResourceWithRawResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.ManifoldResourceWithRawResponse:
        from .resources.manifold import ManifoldResourceWithRawResponse

        return ManifoldResourceWithRawResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.ManifoldelsetResourceWithRawResponse:
        from .resources.manifoldelset import ManifoldelsetResourceWithRawResponse

        return ManifoldelsetResourceWithRawResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.MissileTracksResourceWithRawResponse:
        from .resources.missile_tracks import MissileTracksResourceWithRawResponse

        return MissileTracksResourceWithRawResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.MissionAssignmentResourceWithRawResponse:
        from .resources.mission_assignment import MissionAssignmentResourceWithRawResponse

        return MissionAssignmentResourceWithRawResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.MtiResourceWithRawResponse:
        from .resources.mti import MtiResourceWithRawResponse

        return MtiResourceWithRawResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.NavigationResourceWithRawResponse:
        from .resources.navigation import NavigationResourceWithRawResponse

        return NavigationResourceWithRawResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(self) -> navigational_obstruction.NavigationalObstructionResourceWithRawResponse:
        from .resources.navigational_obstruction import NavigationalObstructionResourceWithRawResponse

        return NavigationalObstructionResourceWithRawResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.NotificationResourceWithRawResponse:
        from .resources.notification import NotificationResourceWithRawResponse

        return NotificationResourceWithRawResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.ObjectOfInterestResourceWithRawResponse:
        from .resources.object_of_interest import ObjectOfInterestResourceWithRawResponse

        return ObjectOfInterestResourceWithRawResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.ObservationsResourceWithRawResponse:
        from .resources.observations import ObservationsResourceWithRawResponse

        return ObservationsResourceWithRawResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.OnboardnavigationResourceWithRawResponse:
        from .resources.onboardnavigation import OnboardnavigationResourceWithRawResponse

        return OnboardnavigationResourceWithRawResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.OnorbitResourceWithRawResponse:
        from .resources.onorbit import OnorbitResourceWithRawResponse

        return OnorbitResourceWithRawResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.OnorbitantennaResourceWithRawResponse:
        from .resources.onorbitantenna import OnorbitantennaResourceWithRawResponse

        return OnorbitantennaResourceWithRawResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.OnorbitbatteryResourceWithRawResponse:
        from .resources.onorbitbattery import OnorbitbatteryResourceWithRawResponse

        return OnorbitbatteryResourceWithRawResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.OnorbitdetailsResourceWithRawResponse:
        from .resources.onorbitdetails import OnorbitdetailsResourceWithRawResponse

        return OnorbitdetailsResourceWithRawResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.OnorbiteventResourceWithRawResponse:
        from .resources.onorbitevent import OnorbiteventResourceWithRawResponse

        return OnorbiteventResourceWithRawResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.OnorbitlistResourceWithRawResponse:
        from .resources.onorbitlist import OnorbitlistResourceWithRawResponse

        return OnorbitlistResourceWithRawResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.OnorbitsolararrayResourceWithRawResponse:
        from .resources.onorbitsolararray import OnorbitsolararrayResourceWithRawResponse

        return OnorbitsolararrayResourceWithRawResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.OnorbitthrusterResourceWithRawResponse:
        from .resources.onorbitthruster import OnorbitthrusterResourceWithRawResponse

        return OnorbitthrusterResourceWithRawResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.OnorbitthrusterstatusResourceWithRawResponse:
        from .resources.onorbitthrusterstatus import OnorbitthrusterstatusResourceWithRawResponse

        return OnorbitthrusterstatusResourceWithRawResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.OnorbitassessmentResourceWithRawResponse:
        from .resources.onorbitassessment import OnorbitassessmentResourceWithRawResponse

        return OnorbitassessmentResourceWithRawResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.OperatingunitResourceWithRawResponse:
        from .resources.operatingunit import OperatingunitResourceWithRawResponse

        return OperatingunitResourceWithRawResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.OperatingunitremarkResourceWithRawResponse:
        from .resources.operatingunitremark import OperatingunitremarkResourceWithRawResponse

        return OperatingunitremarkResourceWithRawResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.OrbitdeterminationResourceWithRawResponse:
        from .resources.orbitdetermination import OrbitdeterminationResourceWithRawResponse

        return OrbitdeterminationResourceWithRawResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.OrbittrackResourceWithRawResponse:
        from .resources.orbittrack import OrbittrackResourceWithRawResponse

        return OrbittrackResourceWithRawResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithRawResponse:
        from .resources.organization import OrganizationResourceWithRawResponse

        return OrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.OrganizationdetailsResourceWithRawResponse:
        from .resources.organizationdetails import OrganizationdetailsResourceWithRawResponse

        return OrganizationdetailsResourceWithRawResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.PersonnelrecoveryResourceWithRawResponse:
        from .resources.personnelrecovery import PersonnelrecoveryResourceWithRawResponse

        return PersonnelrecoveryResourceWithRawResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.PoiResourceWithRawResponse:
        from .resources.poi import PoiResourceWithRawResponse

        return PoiResourceWithRawResponse(self._client.poi)

    @cached_property
    def port(self) -> port.PortResourceWithRawResponse:
        from .resources.port import PortResourceWithRawResponse

        return PortResourceWithRawResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.ReportAndActivitiesResourceWithRawResponse:
        from .resources.report_and_activities import ReportAndActivitiesResourceWithRawResponse

        return ReportAndActivitiesResourceWithRawResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.RfBandResourceWithRawResponse:
        from .resources.rf_band import RfBandResourceWithRawResponse

        return RfBandResourceWithRawResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.RfBandTypeResourceWithRawResponse:
        from .resources.rf_band_type import RfBandTypeResourceWithRawResponse

        return RfBandTypeResourceWithRawResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.RfEmitterResourceWithRawResponse:
        from .resources.rf_emitter import RfEmitterResourceWithRawResponse

        return RfEmitterResourceWithRawResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.RouteStatsResourceWithRawResponse:
        from .resources.route_stats import RouteStatsResourceWithRawResponse

        return RouteStatsResourceWithRawResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.SarObservationResourceWithRawResponse:
        from .resources.sar_observation import SarObservationResourceWithRawResponse

        return SarObservationResourceWithRawResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.ScientificResourceWithRawResponse:
        from .resources.scientific import ScientificResourceWithRawResponse

        return ScientificResourceWithRawResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.ScsResourceWithRawResponse:
        from .resources.scs import ScsResourceWithRawResponse

        return ScsResourceWithRawResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.SecureMessagingResourceWithRawResponse:
        from .resources.secure_messaging import SecureMessagingResourceWithRawResponse

        return SecureMessagingResourceWithRawResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.SensorResourceWithRawResponse:
        from .resources.sensor import SensorResourceWithRawResponse

        return SensorResourceWithRawResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.SensorStatingResourceWithRawResponse:
        from .resources.sensor_stating import SensorStatingResourceWithRawResponse

        return SensorStatingResourceWithRawResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.SensorMaintenanceResourceWithRawResponse:
        from .resources.sensor_maintenance import SensorMaintenanceResourceWithRawResponse

        return SensorMaintenanceResourceWithRawResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(self) -> sensor_observation_type.SensorObservationTypeResourceWithRawResponse:
        from .resources.sensor_observation_type import SensorObservationTypeResourceWithRawResponse

        return SensorObservationTypeResourceWithRawResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.SensorPlanResourceWithRawResponse:
        from .resources.sensor_plan import SensorPlanResourceWithRawResponse

        return SensorPlanResourceWithRawResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.SensorTypeResourceWithRawResponse:
        from .resources.sensor_type import SensorTypeResourceWithRawResponse

        return SensorTypeResourceWithRawResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.SeraDataCommDetailsResourceWithRawResponse:
        from .resources.sera_data_comm_details import SeraDataCommDetailsResourceWithRawResponse

        return SeraDataCommDetailsResourceWithRawResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.SeraDataEarlyWarningResourceWithRawResponse:
        from .resources.sera_data_early_warning import SeraDataEarlyWarningResourceWithRawResponse

        return SeraDataEarlyWarningResourceWithRawResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.SeraDataNavigationResourceWithRawResponse:
        from .resources.sera_data_navigation import SeraDataNavigationResourceWithRawResponse

        return SeraDataNavigationResourceWithRawResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(self) -> seradata_optical_payload.SeradataOpticalPayloadResourceWithRawResponse:
        from .resources.seradata_optical_payload import SeradataOpticalPayloadResourceWithRawResponse

        return SeradataOpticalPayloadResourceWithRawResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.SeradataRadarPayloadResourceWithRawResponse:
        from .resources.seradata_radar_payload import SeradataRadarPayloadResourceWithRawResponse

        return SeradataRadarPayloadResourceWithRawResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(self) -> seradata_sigint_payload.SeradataSigintPayloadResourceWithRawResponse:
        from .resources.seradata_sigint_payload import SeradataSigintPayloadResourceWithRawResponse

        return SeradataSigintPayloadResourceWithRawResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.SeradataSpacecraftDetailsResourceWithRawResponse:
        from .resources.seradata_spacecraft_details import SeradataSpacecraftDetailsResourceWithRawResponse

        return SeradataSpacecraftDetailsResourceWithRawResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.SgiResourceWithRawResponse:
        from .resources.sgi import SgiResourceWithRawResponse

        return SgiResourceWithRawResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.SigactResourceWithRawResponse:
        from .resources.sigact import SigactResourceWithRawResponse

        return SigactResourceWithRawResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.SiteResourceWithRawResponse:
        from .resources.site import SiteResourceWithRawResponse

        return SiteResourceWithRawResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.SiteRemarkResourceWithRawResponse:
        from .resources.site_remark import SiteRemarkResourceWithRawResponse

        return SiteRemarkResourceWithRawResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.SiteStatusResourceWithRawResponse:
        from .resources.site_status import SiteStatusResourceWithRawResponse

        return SiteStatusResourceWithRawResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.SkyImageryResourceWithRawResponse:
        from .resources.sky_imagery import SkyImageryResourceWithRawResponse

        return SkyImageryResourceWithRawResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.SoiObservationSetResourceWithRawResponse:
        from .resources.soi_observation_set import SoiObservationSetResourceWithRawResponse

        return SoiObservationSetResourceWithRawResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.SolarArrayResourceWithRawResponse:
        from .resources.solar_array import SolarArrayResourceWithRawResponse

        return SolarArrayResourceWithRawResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.SolarArrayDetailsResourceWithRawResponse:
        from .resources.solar_array_details import SolarArrayDetailsResourceWithRawResponse

        return SolarArrayDetailsResourceWithRawResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.SortiePprResourceWithRawResponse:
        from .resources.sortie_ppr import SortiePprResourceWithRawResponse

        return SortiePprResourceWithRawResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.SpaceEnvObservationResourceWithRawResponse:
        from .resources.space_env_observation import SpaceEnvObservationResourceWithRawResponse

        return SpaceEnvObservationResourceWithRawResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.StageResourceWithRawResponse:
        from .resources.stage import StageResourceWithRawResponse

        return StageResourceWithRawResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.StarCatalogResourceWithRawResponse:
        from .resources.star_catalog import StarCatalogResourceWithRawResponse

        return StarCatalogResourceWithRawResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.StateVectorResourceWithRawResponse:
        from .resources.state_vector import StateVectorResourceWithRawResponse

        return StateVectorResourceWithRawResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.StatusResourceWithRawResponse:
        from .resources.status import StatusResourceWithRawResponse

        return StatusResourceWithRawResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.SubstatusResourceWithRawResponse:
        from .resources.substatus import SubstatusResourceWithRawResponse

        return SubstatusResourceWithRawResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.SupportingDataResourceWithRawResponse:
        from .resources.supporting_data import SupportingDataResourceWithRawResponse

        return SupportingDataResourceWithRawResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.SurfaceResourceWithRawResponse:
        from .resources.surface import SurfaceResourceWithRawResponse

        return SurfaceResourceWithRawResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.SurfaceObstructionResourceWithRawResponse:
        from .resources.surface_obstruction import SurfaceObstructionResourceWithRawResponse

        return SurfaceObstructionResourceWithRawResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.SwirResourceWithRawResponse:
        from .resources.swir import SwirResourceWithRawResponse

        return SwirResourceWithRawResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.TaiUtcResourceWithRawResponse:
        from .resources.tai_utc import TaiUtcResourceWithRawResponse

        return TaiUtcResourceWithRawResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.TdoaFdoaResourceWithRawResponse:
        from .resources.tdoa_fdoa import TdoaFdoaResourceWithRawResponse

        return TdoaFdoaResourceWithRawResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.TrackResourceWithRawResponse:
        from .resources.track import TrackResourceWithRawResponse

        return TrackResourceWithRawResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.TrackDetailsResourceWithRawResponse:
        from .resources.track_details import TrackDetailsResourceWithRawResponse

        return TrackDetailsResourceWithRawResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.TrackRouteResourceWithRawResponse:
        from .resources.track_route import TrackRouteResourceWithRawResponse

        return TrackRouteResourceWithRawResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.TransponderResourceWithRawResponse:
        from .resources.transponder import TransponderResourceWithRawResponse

        return TransponderResourceWithRawResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.VesselResourceWithRawResponse:
        from .resources.vessel import VesselResourceWithRawResponse

        return VesselResourceWithRawResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.VideoResourceWithRawResponse:
        from .resources.video import VideoResourceWithRawResponse

        return VideoResourceWithRawResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.WeatherDataResourceWithRawResponse:
        from .resources.weather_data import WeatherDataResourceWithRawResponse

        return WeatherDataResourceWithRawResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.WeatherReportResourceWithRawResponse:
        from .resources.weather_report import WeatherReportResourceWithRawResponse

        return WeatherReportResourceWithRawResponse(self._client.weather_report)


class AsyncUnifieddatalibraryWithRawResponse:
    _client: AsyncUnifieddatalibrary

    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self._client = client

    @cached_property
    def air_events(self) -> air_events.AsyncAirEventsResourceWithRawResponse:
        from .resources.air_events import AsyncAirEventsResourceWithRawResponse

        return AsyncAirEventsResourceWithRawResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AsyncAirOperationsResourceWithRawResponse:
        from .resources.air_operations import AsyncAirOperationsResourceWithRawResponse

        return AsyncAirOperationsResourceWithRawResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AsyncAirTransportMissionsResourceWithRawResponse:
        from .resources.air_transport_missions import AsyncAirTransportMissionsResourceWithRawResponse

        return AsyncAirTransportMissionsResourceWithRawResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AsyncAircraftResourceWithRawResponse:
        from .resources.aircraft import AsyncAircraftResourceWithRawResponse

        return AsyncAircraftResourceWithRawResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AsyncAircraftSortiesResourceWithRawResponse:
        from .resources.aircraft_sorties import AsyncAircraftSortiesResourceWithRawResponse

        return AsyncAircraftSortiesResourceWithRawResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(self) -> aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithRawResponse:
        from .resources.aircraft_status_remarks import AsyncAircraftStatusRemarksResourceWithRawResponse

        return AsyncAircraftStatusRemarksResourceWithRawResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AsyncAircraftStatusesResourceWithRawResponse:
        from .resources.aircraft_statuses import AsyncAircraftStatusesResourceWithRawResponse

        return AsyncAircraftStatusesResourceWithRawResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(
        self,
    ) -> airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResourceWithRawResponse:
        from .resources.airfield_slot_consumptions import AsyncAirfieldSlotConsumptionsResourceWithRawResponse

        return AsyncAirfieldSlotConsumptionsResourceWithRawResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AsyncAirfieldSlotsResourceWithRawResponse:
        from .resources.airfield_slots import AsyncAirfieldSlotsResourceWithRawResponse

        return AsyncAirfieldSlotsResourceWithRawResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AsyncAirfieldStatusResourceWithRawResponse:
        from .resources.airfield_status import AsyncAirfieldStatusResourceWithRawResponse

        return AsyncAirfieldStatusResourceWithRawResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AsyncAirfieldsResourceWithRawResponse:
        from .resources.airfields import AsyncAirfieldsResourceWithRawResponse

        return AsyncAirfieldsResourceWithRawResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AsyncAirloadPlansResourceWithRawResponse:
        from .resources.airload_plans import AsyncAirloadPlansResourceWithRawResponse

        return AsyncAirloadPlansResourceWithRawResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(self) -> airspace_control_orders.AsyncAirspaceControlOrdersResourceWithRawResponse:
        from .resources.airspace_control_orders import AsyncAirspaceControlOrdersResourceWithRawResponse

        return AsyncAirspaceControlOrdersResourceWithRawResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AsyncAIsResourceWithRawResponse:
        from .resources.ais import AsyncAIsResourceWithRawResponse

        return AsyncAIsResourceWithRawResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AsyncAIsObjectsResourceWithRawResponse:
        from .resources.ais_objects import AsyncAIsObjectsResourceWithRawResponse

        return AsyncAIsObjectsResourceWithRawResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AsyncAnalyticImageryResourceWithRawResponse:
        from .resources.analytic_imagery import AsyncAnalyticImageryResourceWithRawResponse

        return AsyncAnalyticImageryResourceWithRawResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AsyncAntennasResourceWithRawResponse:
        from .resources.antennas import AsyncAntennasResourceWithRawResponse

        return AsyncAntennasResourceWithRawResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AsyncAttitudeDataResourceWithRawResponse:
        from .resources.attitude_data import AsyncAttitudeDataResourceWithRawResponse

        return AsyncAttitudeDataResourceWithRawResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AsyncAttitudeSetsResourceWithRawResponse:
        from .resources.attitude_sets import AsyncAttitudeSetsResourceWithRawResponse

        return AsyncAttitudeSetsResourceWithRawResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(self) -> aviation_risk_management.AsyncAviationRiskManagementResourceWithRawResponse:
        from .resources.aviation_risk_management import AsyncAviationRiskManagementResourceWithRawResponse

        return AsyncAviationRiskManagementResourceWithRawResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.AsyncBatteriesResourceWithRawResponse:
        from .resources.batteries import AsyncBatteriesResourceWithRawResponse

        return AsyncBatteriesResourceWithRawResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.AsyncBatterydetailsResourceWithRawResponse:
        from .resources.batterydetails import AsyncBatterydetailsResourceWithRawResponse

        return AsyncBatterydetailsResourceWithRawResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.AsyncBeamResourceWithRawResponse:
        from .resources.beam import AsyncBeamResourceWithRawResponse

        return AsyncBeamResourceWithRawResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.AsyncBeamContoursResourceWithRawResponse:
        from .resources.beam_contours import AsyncBeamContoursResourceWithRawResponse

        return AsyncBeamContoursResourceWithRawResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.AsyncBusesResourceWithRawResponse:
        from .resources.buses import AsyncBusesResourceWithRawResponse

        return AsyncBusesResourceWithRawResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithRawResponse:
        from .resources.channels import AsyncChannelsResourceWithRawResponse

        return AsyncChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.AsyncCloselyspacedobjectsResourceWithRawResponse:
        from .resources.closelyspacedobjects import AsyncCloselyspacedobjectsResourceWithRawResponse

        return AsyncCloselyspacedobjectsResourceWithRawResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.AsyncCollectRequestsResourceWithRawResponse:
        from .resources.collect_requests import AsyncCollectRequestsResourceWithRawResponse

        return AsyncCollectRequestsResourceWithRawResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.AsyncCollectResponsesResourceWithRawResponse:
        from .resources.collect_responses import AsyncCollectResponsesResourceWithRawResponse

        return AsyncCollectResponsesResourceWithRawResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.AsyncCommResourceWithRawResponse:
        from .resources.comm import AsyncCommResourceWithRawResponse

        return AsyncCommResourceWithRawResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.AsyncConjunctionsResourceWithRawResponse:
        from .resources.conjunctions import AsyncConjunctionsResourceWithRawResponse

        return AsyncConjunctionsResourceWithRawResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.AsyncCotsResourceWithRawResponse:
        from .resources.cots import AsyncCotsResourceWithRawResponse

        return AsyncCotsResourceWithRawResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.AsyncCountriesResourceWithRawResponse:
        from .resources.countries import AsyncCountriesResourceWithRawResponse

        return AsyncCountriesResourceWithRawResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.AsyncCrewResourceWithRawResponse:
        from .resources.crew import AsyncCrewResourceWithRawResponse

        return AsyncCrewResourceWithRawResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.AsyncDeconflictsetResourceWithRawResponse:
        from .resources.deconflictset import AsyncDeconflictsetResourceWithRawResponse

        return AsyncDeconflictsetResourceWithRawResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.AsyncDiffOfArrivalResourceWithRawResponse:
        from .resources.diff_of_arrival import AsyncDiffOfArrivalResourceWithRawResponse

        return AsyncDiffOfArrivalResourceWithRawResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.AsyncDiplomaticClearanceResourceWithRawResponse:
        from .resources.diplomatic_clearance import AsyncDiplomaticClearanceResourceWithRawResponse

        return AsyncDiplomaticClearanceResourceWithRawResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.AsyncDriftHistoryResourceWithRawResponse:
        from .resources.drift_history import AsyncDriftHistoryResourceWithRawResponse

        return AsyncDriftHistoryResourceWithRawResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.AsyncDropzoneResourceWithRawResponse:
        from .resources.dropzone import AsyncDropzoneResourceWithRawResponse

        return AsyncDropzoneResourceWithRawResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.AsyncEcpedrResourceWithRawResponse:
        from .resources.ecpedr import AsyncEcpedrResourceWithRawResponse

        return AsyncEcpedrResourceWithRawResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.AsyncEffectRequestsResourceWithRawResponse:
        from .resources.effect_requests import AsyncEffectRequestsResourceWithRawResponse

        return AsyncEffectRequestsResourceWithRawResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.AsyncEffectResponsesResourceWithRawResponse:
        from .resources.effect_responses import AsyncEffectResponsesResourceWithRawResponse

        return AsyncEffectResponsesResourceWithRawResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.AsyncElsetsResourceWithRawResponse:
        from .resources.elsets import AsyncElsetsResourceWithRawResponse

        return AsyncElsetsResourceWithRawResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.AsyncEmireportResourceWithRawResponse:
        from .resources.emireport import AsyncEmireportResourceWithRawResponse

        return AsyncEmireportResourceWithRawResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.AsyncEmitterGeolocationResourceWithRawResponse:
        from .resources.emitter_geolocation import AsyncEmitterGeolocationResourceWithRawResponse

        return AsyncEmitterGeolocationResourceWithRawResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.AsyncEngineDetailsResourceWithRawResponse:
        from .resources.engine_details import AsyncEngineDetailsResourceWithRawResponse

        return AsyncEngineDetailsResourceWithRawResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.AsyncEnginesResourceWithRawResponse:
        from .resources.engines import AsyncEnginesResourceWithRawResponse

        return AsyncEnginesResourceWithRawResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithRawResponse:
        from .resources.entities import AsyncEntitiesResourceWithRawResponse

        return AsyncEntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.AsyncEopResourceWithRawResponse:
        from .resources.eop import AsyncEopResourceWithRawResponse

        return AsyncEopResourceWithRawResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.AsyncEphemerisResourceWithRawResponse:
        from .resources.ephemeris import AsyncEphemerisResourceWithRawResponse

        return AsyncEphemerisResourceWithRawResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.AsyncEphemerisSetsResourceWithRawResponse:
        from .resources.ephemeris_sets import AsyncEphemerisSetsResourceWithRawResponse

        return AsyncEphemerisSetsResourceWithRawResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.AsyncEquipmentResourceWithRawResponse:
        from .resources.equipment import AsyncEquipmentResourceWithRawResponse

        return AsyncEquipmentResourceWithRawResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.AsyncEquipmentRemarksResourceWithRawResponse:
        from .resources.equipment_remarks import AsyncEquipmentRemarksResourceWithRawResponse

        return AsyncEquipmentRemarksResourceWithRawResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.AsyncEvacResourceWithRawResponse:
        from .resources.evac import AsyncEvacResourceWithRawResponse

        return AsyncEvacResourceWithRawResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.AsyncEventEvolutionResourceWithRawResponse:
        from .resources.event_evolution import AsyncEventEvolutionResourceWithRawResponse

        return AsyncEventEvolutionResourceWithRawResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.AsyncFeatureAssessmentResourceWithRawResponse:
        from .resources.feature_assessment import AsyncFeatureAssessmentResourceWithRawResponse

        return AsyncFeatureAssessmentResourceWithRawResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.AsyncFlightplanResourceWithRawResponse:
        from .resources.flightplan import AsyncFlightplanResourceWithRawResponse

        return AsyncFlightplanResourceWithRawResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.AsyncGeoStatusResourceWithRawResponse:
        from .resources.geo_status import AsyncGeoStatusResourceWithRawResponse

        return AsyncGeoStatusResourceWithRawResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(self) -> global_atmospheric_model.AsyncGlobalAtmosphericModelResourceWithRawResponse:
        from .resources.global_atmospheric_model import AsyncGlobalAtmosphericModelResourceWithRawResponse

        return AsyncGlobalAtmosphericModelResourceWithRawResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.AsyncGnssObservationsResourceWithRawResponse:
        from .resources.gnss_observations import AsyncGnssObservationsResourceWithRawResponse

        return AsyncGnssObservationsResourceWithRawResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.AsyncGnssObservationsetResourceWithRawResponse:
        from .resources.gnss_observationset import AsyncGnssObservationsetResourceWithRawResponse

        return AsyncGnssObservationsetResourceWithRawResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.AsyncGnssRawIfResourceWithRawResponse:
        from .resources.gnss_raw_if import AsyncGnssRawIfResourceWithRawResponse

        return AsyncGnssRawIfResourceWithRawResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.AsyncGroundImageryResourceWithRawResponse:
        from .resources.ground_imagery import AsyncGroundImageryResourceWithRawResponse

        return AsyncGroundImageryResourceWithRawResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.AsyncH3GeoResourceWithRawResponse:
        from .resources.h3_geo import AsyncH3GeoResourceWithRawResponse

        return AsyncH3GeoResourceWithRawResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.AsyncH3GeoHexCellResourceWithRawResponse:
        from .resources.h3_geo_hex_cell import AsyncH3GeoHexCellResourceWithRawResponse

        return AsyncH3GeoHexCellResourceWithRawResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.AsyncHazardResourceWithRawResponse:
        from .resources.hazard import AsyncHazardResourceWithRawResponse

        return AsyncHazardResourceWithRawResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.AsyncIonoObservationsResourceWithRawResponse:
        from .resources.iono_observations import AsyncIonoObservationsResourceWithRawResponse

        return AsyncIonoObservationsResourceWithRawResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.AsyncIrResourceWithRawResponse:
        from .resources.ir import AsyncIrResourceWithRawResponse

        return AsyncIrResourceWithRawResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.AsyncIsrCollectionsResourceWithRawResponse:
        from .resources.isr_collections import AsyncIsrCollectionsResourceWithRawResponse

        return AsyncIsrCollectionsResourceWithRawResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.AsyncItemResourceWithRawResponse:
        from .resources.item import AsyncItemResourceWithRawResponse

        return AsyncItemResourceWithRawResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.AsyncItemTrackingsResourceWithRawResponse:
        from .resources.item_trackings import AsyncItemTrackingsResourceWithRawResponse

        return AsyncItemTrackingsResourceWithRawResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.AsyncLaserdeconflictrequestResourceWithRawResponse:
        from .resources.laserdeconflictrequest import AsyncLaserdeconflictrequestResourceWithRawResponse

        return AsyncLaserdeconflictrequestResourceWithRawResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.AsyncLaseremitterResourceWithRawResponse:
        from .resources.laseremitter import AsyncLaseremitterResourceWithRawResponse

        return AsyncLaseremitterResourceWithRawResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.AsyncLaunchDetectionResourceWithRawResponse:
        from .resources.launch_detection import AsyncLaunchDetectionResourceWithRawResponse

        return AsyncLaunchDetectionResourceWithRawResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.AsyncLaunchEventResourceWithRawResponse:
        from .resources.launch_event import AsyncLaunchEventResourceWithRawResponse

        return AsyncLaunchEventResourceWithRawResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.AsyncLaunchSiteResourceWithRawResponse:
        from .resources.launch_site import AsyncLaunchSiteResourceWithRawResponse

        return AsyncLaunchSiteResourceWithRawResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.AsyncLaunchSiteDetailsResourceWithRawResponse:
        from .resources.launch_site_details import AsyncLaunchSiteDetailsResourceWithRawResponse

        return AsyncLaunchSiteDetailsResourceWithRawResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.AsyncLaunchVehicleResourceWithRawResponse:
        from .resources.launch_vehicle import AsyncLaunchVehicleResourceWithRawResponse

        return AsyncLaunchVehicleResourceWithRawResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.AsyncLaunchVehicleDetailsResourceWithRawResponse:
        from .resources.launch_vehicle_details import AsyncLaunchVehicleDetailsResourceWithRawResponse

        return AsyncLaunchVehicleDetailsResourceWithRawResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.AsyncLinkStatusResourceWithRawResponse:
        from .resources.link_status import AsyncLinkStatusResourceWithRawResponse

        return AsyncLinkStatusResourceWithRawResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.AsyncLinkstatusResourceWithRawResponse:
        from .resources.linkstatus import AsyncLinkstatusResourceWithRawResponse

        return AsyncLinkstatusResourceWithRawResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithRawResponse:
        from .resources.location import AsyncLocationResourceWithRawResponse

        return AsyncLocationResourceWithRawResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.AsyncLogisticsSupportResourceWithRawResponse:
        from .resources.logistics_support import AsyncLogisticsSupportResourceWithRawResponse

        return AsyncLogisticsSupportResourceWithRawResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.AsyncManeuversResourceWithRawResponse:
        from .resources.maneuvers import AsyncManeuversResourceWithRawResponse

        return AsyncManeuversResourceWithRawResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.AsyncManifoldResourceWithRawResponse:
        from .resources.manifold import AsyncManifoldResourceWithRawResponse

        return AsyncManifoldResourceWithRawResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.AsyncManifoldelsetResourceWithRawResponse:
        from .resources.manifoldelset import AsyncManifoldelsetResourceWithRawResponse

        return AsyncManifoldelsetResourceWithRawResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.AsyncMissileTracksResourceWithRawResponse:
        from .resources.missile_tracks import AsyncMissileTracksResourceWithRawResponse

        return AsyncMissileTracksResourceWithRawResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.AsyncMissionAssignmentResourceWithRawResponse:
        from .resources.mission_assignment import AsyncMissionAssignmentResourceWithRawResponse

        return AsyncMissionAssignmentResourceWithRawResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.AsyncMtiResourceWithRawResponse:
        from .resources.mti import AsyncMtiResourceWithRawResponse

        return AsyncMtiResourceWithRawResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.AsyncNavigationResourceWithRawResponse:
        from .resources.navigation import AsyncNavigationResourceWithRawResponse

        return AsyncNavigationResourceWithRawResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(self) -> navigational_obstruction.AsyncNavigationalObstructionResourceWithRawResponse:
        from .resources.navigational_obstruction import AsyncNavigationalObstructionResourceWithRawResponse

        return AsyncNavigationalObstructionResourceWithRawResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.AsyncNotificationResourceWithRawResponse:
        from .resources.notification import AsyncNotificationResourceWithRawResponse

        return AsyncNotificationResourceWithRawResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.AsyncObjectOfInterestResourceWithRawResponse:
        from .resources.object_of_interest import AsyncObjectOfInterestResourceWithRawResponse

        return AsyncObjectOfInterestResourceWithRawResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.AsyncObservationsResourceWithRawResponse:
        from .resources.observations import AsyncObservationsResourceWithRawResponse

        return AsyncObservationsResourceWithRawResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.AsyncOnboardnavigationResourceWithRawResponse:
        from .resources.onboardnavigation import AsyncOnboardnavigationResourceWithRawResponse

        return AsyncOnboardnavigationResourceWithRawResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.AsyncOnorbitResourceWithRawResponse:
        from .resources.onorbit import AsyncOnorbitResourceWithRawResponse

        return AsyncOnorbitResourceWithRawResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.AsyncOnorbitantennaResourceWithRawResponse:
        from .resources.onorbitantenna import AsyncOnorbitantennaResourceWithRawResponse

        return AsyncOnorbitantennaResourceWithRawResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.AsyncOnorbitbatteryResourceWithRawResponse:
        from .resources.onorbitbattery import AsyncOnorbitbatteryResourceWithRawResponse

        return AsyncOnorbitbatteryResourceWithRawResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.AsyncOnorbitdetailsResourceWithRawResponse:
        from .resources.onorbitdetails import AsyncOnorbitdetailsResourceWithRawResponse

        return AsyncOnorbitdetailsResourceWithRawResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.AsyncOnorbiteventResourceWithRawResponse:
        from .resources.onorbitevent import AsyncOnorbiteventResourceWithRawResponse

        return AsyncOnorbiteventResourceWithRawResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.AsyncOnorbitlistResourceWithRawResponse:
        from .resources.onorbitlist import AsyncOnorbitlistResourceWithRawResponse

        return AsyncOnorbitlistResourceWithRawResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.AsyncOnorbitsolararrayResourceWithRawResponse:
        from .resources.onorbitsolararray import AsyncOnorbitsolararrayResourceWithRawResponse

        return AsyncOnorbitsolararrayResourceWithRawResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.AsyncOnorbitthrusterResourceWithRawResponse:
        from .resources.onorbitthruster import AsyncOnorbitthrusterResourceWithRawResponse

        return AsyncOnorbitthrusterResourceWithRawResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.AsyncOnorbitthrusterstatusResourceWithRawResponse:
        from .resources.onorbitthrusterstatus import AsyncOnorbitthrusterstatusResourceWithRawResponse

        return AsyncOnorbitthrusterstatusResourceWithRawResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.AsyncOnorbitassessmentResourceWithRawResponse:
        from .resources.onorbitassessment import AsyncOnorbitassessmentResourceWithRawResponse

        return AsyncOnorbitassessmentResourceWithRawResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.AsyncOperatingunitResourceWithRawResponse:
        from .resources.operatingunit import AsyncOperatingunitResourceWithRawResponse

        return AsyncOperatingunitResourceWithRawResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.AsyncOperatingunitremarkResourceWithRawResponse:
        from .resources.operatingunitremark import AsyncOperatingunitremarkResourceWithRawResponse

        return AsyncOperatingunitremarkResourceWithRawResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.AsyncOrbitdeterminationResourceWithRawResponse:
        from .resources.orbitdetermination import AsyncOrbitdeterminationResourceWithRawResponse

        return AsyncOrbitdeterminationResourceWithRawResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.AsyncOrbittrackResourceWithRawResponse:
        from .resources.orbittrack import AsyncOrbittrackResourceWithRawResponse

        return AsyncOrbittrackResourceWithRawResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithRawResponse:
        from .resources.organization import AsyncOrganizationResourceWithRawResponse

        return AsyncOrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.AsyncOrganizationdetailsResourceWithRawResponse:
        from .resources.organizationdetails import AsyncOrganizationdetailsResourceWithRawResponse

        return AsyncOrganizationdetailsResourceWithRawResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.AsyncPersonnelrecoveryResourceWithRawResponse:
        from .resources.personnelrecovery import AsyncPersonnelrecoveryResourceWithRawResponse

        return AsyncPersonnelrecoveryResourceWithRawResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.AsyncPoiResourceWithRawResponse:
        from .resources.poi import AsyncPoiResourceWithRawResponse

        return AsyncPoiResourceWithRawResponse(self._client.poi)

    @cached_property
    def port(self) -> port.AsyncPortResourceWithRawResponse:
        from .resources.port import AsyncPortResourceWithRawResponse

        return AsyncPortResourceWithRawResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.AsyncReportAndActivitiesResourceWithRawResponse:
        from .resources.report_and_activities import AsyncReportAndActivitiesResourceWithRawResponse

        return AsyncReportAndActivitiesResourceWithRawResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.AsyncRfBandResourceWithRawResponse:
        from .resources.rf_band import AsyncRfBandResourceWithRawResponse

        return AsyncRfBandResourceWithRawResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.AsyncRfBandTypeResourceWithRawResponse:
        from .resources.rf_band_type import AsyncRfBandTypeResourceWithRawResponse

        return AsyncRfBandTypeResourceWithRawResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.AsyncRfEmitterResourceWithRawResponse:
        from .resources.rf_emitter import AsyncRfEmitterResourceWithRawResponse

        return AsyncRfEmitterResourceWithRawResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.AsyncRouteStatsResourceWithRawResponse:
        from .resources.route_stats import AsyncRouteStatsResourceWithRawResponse

        return AsyncRouteStatsResourceWithRawResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.AsyncSarObservationResourceWithRawResponse:
        from .resources.sar_observation import AsyncSarObservationResourceWithRawResponse

        return AsyncSarObservationResourceWithRawResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.AsyncScientificResourceWithRawResponse:
        from .resources.scientific import AsyncScientificResourceWithRawResponse

        return AsyncScientificResourceWithRawResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.AsyncScsResourceWithRawResponse:
        from .resources.scs import AsyncScsResourceWithRawResponse

        return AsyncScsResourceWithRawResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.AsyncSecureMessagingResourceWithRawResponse:
        from .resources.secure_messaging import AsyncSecureMessagingResourceWithRawResponse

        return AsyncSecureMessagingResourceWithRawResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.AsyncSensorResourceWithRawResponse:
        from .resources.sensor import AsyncSensorResourceWithRawResponse

        return AsyncSensorResourceWithRawResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.AsyncSensorStatingResourceWithRawResponse:
        from .resources.sensor_stating import AsyncSensorStatingResourceWithRawResponse

        return AsyncSensorStatingResourceWithRawResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.AsyncSensorMaintenanceResourceWithRawResponse:
        from .resources.sensor_maintenance import AsyncSensorMaintenanceResourceWithRawResponse

        return AsyncSensorMaintenanceResourceWithRawResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(self) -> sensor_observation_type.AsyncSensorObservationTypeResourceWithRawResponse:
        from .resources.sensor_observation_type import AsyncSensorObservationTypeResourceWithRawResponse

        return AsyncSensorObservationTypeResourceWithRawResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.AsyncSensorPlanResourceWithRawResponse:
        from .resources.sensor_plan import AsyncSensorPlanResourceWithRawResponse

        return AsyncSensorPlanResourceWithRawResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.AsyncSensorTypeResourceWithRawResponse:
        from .resources.sensor_type import AsyncSensorTypeResourceWithRawResponse

        return AsyncSensorTypeResourceWithRawResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.AsyncSeraDataCommDetailsResourceWithRawResponse:
        from .resources.sera_data_comm_details import AsyncSeraDataCommDetailsResourceWithRawResponse

        return AsyncSeraDataCommDetailsResourceWithRawResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.AsyncSeraDataEarlyWarningResourceWithRawResponse:
        from .resources.sera_data_early_warning import AsyncSeraDataEarlyWarningResourceWithRawResponse

        return AsyncSeraDataEarlyWarningResourceWithRawResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.AsyncSeraDataNavigationResourceWithRawResponse:
        from .resources.sera_data_navigation import AsyncSeraDataNavigationResourceWithRawResponse

        return AsyncSeraDataNavigationResourceWithRawResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(self) -> seradata_optical_payload.AsyncSeradataOpticalPayloadResourceWithRawResponse:
        from .resources.seradata_optical_payload import AsyncSeradataOpticalPayloadResourceWithRawResponse

        return AsyncSeradataOpticalPayloadResourceWithRawResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.AsyncSeradataRadarPayloadResourceWithRawResponse:
        from .resources.seradata_radar_payload import AsyncSeradataRadarPayloadResourceWithRawResponse

        return AsyncSeradataRadarPayloadResourceWithRawResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(self) -> seradata_sigint_payload.AsyncSeradataSigintPayloadResourceWithRawResponse:
        from .resources.seradata_sigint_payload import AsyncSeradataSigintPayloadResourceWithRawResponse

        return AsyncSeradataSigintPayloadResourceWithRawResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResourceWithRawResponse:
        from .resources.seradata_spacecraft_details import AsyncSeradataSpacecraftDetailsResourceWithRawResponse

        return AsyncSeradataSpacecraftDetailsResourceWithRawResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.AsyncSgiResourceWithRawResponse:
        from .resources.sgi import AsyncSgiResourceWithRawResponse

        return AsyncSgiResourceWithRawResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.AsyncSigactResourceWithRawResponse:
        from .resources.sigact import AsyncSigactResourceWithRawResponse

        return AsyncSigactResourceWithRawResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.AsyncSiteResourceWithRawResponse:
        from .resources.site import AsyncSiteResourceWithRawResponse

        return AsyncSiteResourceWithRawResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.AsyncSiteRemarkResourceWithRawResponse:
        from .resources.site_remark import AsyncSiteRemarkResourceWithRawResponse

        return AsyncSiteRemarkResourceWithRawResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.AsyncSiteStatusResourceWithRawResponse:
        from .resources.site_status import AsyncSiteStatusResourceWithRawResponse

        return AsyncSiteStatusResourceWithRawResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.AsyncSkyImageryResourceWithRawResponse:
        from .resources.sky_imagery import AsyncSkyImageryResourceWithRawResponse

        return AsyncSkyImageryResourceWithRawResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.AsyncSoiObservationSetResourceWithRawResponse:
        from .resources.soi_observation_set import AsyncSoiObservationSetResourceWithRawResponse

        return AsyncSoiObservationSetResourceWithRawResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.AsyncSolarArrayResourceWithRawResponse:
        from .resources.solar_array import AsyncSolarArrayResourceWithRawResponse

        return AsyncSolarArrayResourceWithRawResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.AsyncSolarArrayDetailsResourceWithRawResponse:
        from .resources.solar_array_details import AsyncSolarArrayDetailsResourceWithRawResponse

        return AsyncSolarArrayDetailsResourceWithRawResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.AsyncSortiePprResourceWithRawResponse:
        from .resources.sortie_ppr import AsyncSortiePprResourceWithRawResponse

        return AsyncSortiePprResourceWithRawResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.AsyncSpaceEnvObservationResourceWithRawResponse:
        from .resources.space_env_observation import AsyncSpaceEnvObservationResourceWithRawResponse

        return AsyncSpaceEnvObservationResourceWithRawResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.AsyncStageResourceWithRawResponse:
        from .resources.stage import AsyncStageResourceWithRawResponse

        return AsyncStageResourceWithRawResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.AsyncStarCatalogResourceWithRawResponse:
        from .resources.star_catalog import AsyncStarCatalogResourceWithRawResponse

        return AsyncStarCatalogResourceWithRawResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.AsyncStateVectorResourceWithRawResponse:
        from .resources.state_vector import AsyncStateVectorResourceWithRawResponse

        return AsyncStateVectorResourceWithRawResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithRawResponse:
        from .resources.status import AsyncStatusResourceWithRawResponse

        return AsyncStatusResourceWithRawResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.AsyncSubstatusResourceWithRawResponse:
        from .resources.substatus import AsyncSubstatusResourceWithRawResponse

        return AsyncSubstatusResourceWithRawResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.AsyncSupportingDataResourceWithRawResponse:
        from .resources.supporting_data import AsyncSupportingDataResourceWithRawResponse

        return AsyncSupportingDataResourceWithRawResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.AsyncSurfaceResourceWithRawResponse:
        from .resources.surface import AsyncSurfaceResourceWithRawResponse

        return AsyncSurfaceResourceWithRawResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.AsyncSurfaceObstructionResourceWithRawResponse:
        from .resources.surface_obstruction import AsyncSurfaceObstructionResourceWithRawResponse

        return AsyncSurfaceObstructionResourceWithRawResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.AsyncSwirResourceWithRawResponse:
        from .resources.swir import AsyncSwirResourceWithRawResponse

        return AsyncSwirResourceWithRawResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.AsyncTaiUtcResourceWithRawResponse:
        from .resources.tai_utc import AsyncTaiUtcResourceWithRawResponse

        return AsyncTaiUtcResourceWithRawResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.AsyncTdoaFdoaResourceWithRawResponse:
        from .resources.tdoa_fdoa import AsyncTdoaFdoaResourceWithRawResponse

        return AsyncTdoaFdoaResourceWithRawResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.AsyncTrackResourceWithRawResponse:
        from .resources.track import AsyncTrackResourceWithRawResponse

        return AsyncTrackResourceWithRawResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.AsyncTrackDetailsResourceWithRawResponse:
        from .resources.track_details import AsyncTrackDetailsResourceWithRawResponse

        return AsyncTrackDetailsResourceWithRawResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.AsyncTrackRouteResourceWithRawResponse:
        from .resources.track_route import AsyncTrackRouteResourceWithRawResponse

        return AsyncTrackRouteResourceWithRawResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.AsyncTransponderResourceWithRawResponse:
        from .resources.transponder import AsyncTransponderResourceWithRawResponse

        return AsyncTransponderResourceWithRawResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.AsyncVesselResourceWithRawResponse:
        from .resources.vessel import AsyncVesselResourceWithRawResponse

        return AsyncVesselResourceWithRawResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.AsyncVideoResourceWithRawResponse:
        from .resources.video import AsyncVideoResourceWithRawResponse

        return AsyncVideoResourceWithRawResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.AsyncWeatherDataResourceWithRawResponse:
        from .resources.weather_data import AsyncWeatherDataResourceWithRawResponse

        return AsyncWeatherDataResourceWithRawResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.AsyncWeatherReportResourceWithRawResponse:
        from .resources.weather_report import AsyncWeatherReportResourceWithRawResponse

        return AsyncWeatherReportResourceWithRawResponse(self._client.weather_report)


class UnifieddatalibraryWithStreamedResponse:
    _client: Unifieddatalibrary

    def __init__(self, client: Unifieddatalibrary) -> None:
        self._client = client

    @cached_property
    def air_events(self) -> air_events.AirEventsResourceWithStreamingResponse:
        from .resources.air_events import AirEventsResourceWithStreamingResponse

        return AirEventsResourceWithStreamingResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AirOperationsResourceWithStreamingResponse:
        from .resources.air_operations import AirOperationsResourceWithStreamingResponse

        return AirOperationsResourceWithStreamingResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AirTransportMissionsResourceWithStreamingResponse:
        from .resources.air_transport_missions import AirTransportMissionsResourceWithStreamingResponse

        return AirTransportMissionsResourceWithStreamingResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AircraftResourceWithStreamingResponse:
        from .resources.aircraft import AircraftResourceWithStreamingResponse

        return AircraftResourceWithStreamingResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AircraftSortiesResourceWithStreamingResponse:
        from .resources.aircraft_sorties import AircraftSortiesResourceWithStreamingResponse

        return AircraftSortiesResourceWithStreamingResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(self) -> aircraft_status_remarks.AircraftStatusRemarksResourceWithStreamingResponse:
        from .resources.aircraft_status_remarks import AircraftStatusRemarksResourceWithStreamingResponse

        return AircraftStatusRemarksResourceWithStreamingResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AircraftStatusesResourceWithStreamingResponse:
        from .resources.aircraft_statuses import AircraftStatusesResourceWithStreamingResponse

        return AircraftStatusesResourceWithStreamingResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(
        self,
    ) -> airfield_slot_consumptions.AirfieldSlotConsumptionsResourceWithStreamingResponse:
        from .resources.airfield_slot_consumptions import AirfieldSlotConsumptionsResourceWithStreamingResponse

        return AirfieldSlotConsumptionsResourceWithStreamingResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AirfieldSlotsResourceWithStreamingResponse:
        from .resources.airfield_slots import AirfieldSlotsResourceWithStreamingResponse

        return AirfieldSlotsResourceWithStreamingResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AirfieldStatusResourceWithStreamingResponse:
        from .resources.airfield_status import AirfieldStatusResourceWithStreamingResponse

        return AirfieldStatusResourceWithStreamingResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AirfieldsResourceWithStreamingResponse:
        from .resources.airfields import AirfieldsResourceWithStreamingResponse

        return AirfieldsResourceWithStreamingResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AirloadPlansResourceWithStreamingResponse:
        from .resources.airload_plans import AirloadPlansResourceWithStreamingResponse

        return AirloadPlansResourceWithStreamingResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(self) -> airspace_control_orders.AirspaceControlOrdersResourceWithStreamingResponse:
        from .resources.airspace_control_orders import AirspaceControlOrdersResourceWithStreamingResponse

        return AirspaceControlOrdersResourceWithStreamingResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AIsResourceWithStreamingResponse:
        from .resources.ais import AIsResourceWithStreamingResponse

        return AIsResourceWithStreamingResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AIsObjectsResourceWithStreamingResponse:
        from .resources.ais_objects import AIsObjectsResourceWithStreamingResponse

        return AIsObjectsResourceWithStreamingResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AnalyticImageryResourceWithStreamingResponse:
        from .resources.analytic_imagery import AnalyticImageryResourceWithStreamingResponse

        return AnalyticImageryResourceWithStreamingResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AntennasResourceWithStreamingResponse:
        from .resources.antennas import AntennasResourceWithStreamingResponse

        return AntennasResourceWithStreamingResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AttitudeDataResourceWithStreamingResponse:
        from .resources.attitude_data import AttitudeDataResourceWithStreamingResponse

        return AttitudeDataResourceWithStreamingResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AttitudeSetsResourceWithStreamingResponse:
        from .resources.attitude_sets import AttitudeSetsResourceWithStreamingResponse

        return AttitudeSetsResourceWithStreamingResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(self) -> aviation_risk_management.AviationRiskManagementResourceWithStreamingResponse:
        from .resources.aviation_risk_management import AviationRiskManagementResourceWithStreamingResponse

        return AviationRiskManagementResourceWithStreamingResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.BatteriesResourceWithStreamingResponse:
        from .resources.batteries import BatteriesResourceWithStreamingResponse

        return BatteriesResourceWithStreamingResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.BatterydetailsResourceWithStreamingResponse:
        from .resources.batterydetails import BatterydetailsResourceWithStreamingResponse

        return BatterydetailsResourceWithStreamingResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.BeamResourceWithStreamingResponse:
        from .resources.beam import BeamResourceWithStreamingResponse

        return BeamResourceWithStreamingResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.BeamContoursResourceWithStreamingResponse:
        from .resources.beam_contours import BeamContoursResourceWithStreamingResponse

        return BeamContoursResourceWithStreamingResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.BusesResourceWithStreamingResponse:
        from .resources.buses import BusesResourceWithStreamingResponse

        return BusesResourceWithStreamingResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithStreamingResponse:
        from .resources.channels import ChannelsResourceWithStreamingResponse

        return ChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.CloselyspacedobjectsResourceWithStreamingResponse:
        from .resources.closelyspacedobjects import CloselyspacedobjectsResourceWithStreamingResponse

        return CloselyspacedobjectsResourceWithStreamingResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.CollectRequestsResourceWithStreamingResponse:
        from .resources.collect_requests import CollectRequestsResourceWithStreamingResponse

        return CollectRequestsResourceWithStreamingResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.CollectResponsesResourceWithStreamingResponse:
        from .resources.collect_responses import CollectResponsesResourceWithStreamingResponse

        return CollectResponsesResourceWithStreamingResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.CommResourceWithStreamingResponse:
        from .resources.comm import CommResourceWithStreamingResponse

        return CommResourceWithStreamingResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.ConjunctionsResourceWithStreamingResponse:
        from .resources.conjunctions import ConjunctionsResourceWithStreamingResponse

        return ConjunctionsResourceWithStreamingResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.CotsResourceWithStreamingResponse:
        from .resources.cots import CotsResourceWithStreamingResponse

        return CotsResourceWithStreamingResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.CountriesResourceWithStreamingResponse:
        from .resources.countries import CountriesResourceWithStreamingResponse

        return CountriesResourceWithStreamingResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.CrewResourceWithStreamingResponse:
        from .resources.crew import CrewResourceWithStreamingResponse

        return CrewResourceWithStreamingResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.DeconflictsetResourceWithStreamingResponse:
        from .resources.deconflictset import DeconflictsetResourceWithStreamingResponse

        return DeconflictsetResourceWithStreamingResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.DiffOfArrivalResourceWithStreamingResponse:
        from .resources.diff_of_arrival import DiffOfArrivalResourceWithStreamingResponse

        return DiffOfArrivalResourceWithStreamingResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.DiplomaticClearanceResourceWithStreamingResponse:
        from .resources.diplomatic_clearance import DiplomaticClearanceResourceWithStreamingResponse

        return DiplomaticClearanceResourceWithStreamingResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.DriftHistoryResourceWithStreamingResponse:
        from .resources.drift_history import DriftHistoryResourceWithStreamingResponse

        return DriftHistoryResourceWithStreamingResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.DropzoneResourceWithStreamingResponse:
        from .resources.dropzone import DropzoneResourceWithStreamingResponse

        return DropzoneResourceWithStreamingResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.EcpedrResourceWithStreamingResponse:
        from .resources.ecpedr import EcpedrResourceWithStreamingResponse

        return EcpedrResourceWithStreamingResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.EffectRequestsResourceWithStreamingResponse:
        from .resources.effect_requests import EffectRequestsResourceWithStreamingResponse

        return EffectRequestsResourceWithStreamingResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.EffectResponsesResourceWithStreamingResponse:
        from .resources.effect_responses import EffectResponsesResourceWithStreamingResponse

        return EffectResponsesResourceWithStreamingResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.ElsetsResourceWithStreamingResponse:
        from .resources.elsets import ElsetsResourceWithStreamingResponse

        return ElsetsResourceWithStreamingResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.EmireportResourceWithStreamingResponse:
        from .resources.emireport import EmireportResourceWithStreamingResponse

        return EmireportResourceWithStreamingResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.EmitterGeolocationResourceWithStreamingResponse:
        from .resources.emitter_geolocation import EmitterGeolocationResourceWithStreamingResponse

        return EmitterGeolocationResourceWithStreamingResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.EngineDetailsResourceWithStreamingResponse:
        from .resources.engine_details import EngineDetailsResourceWithStreamingResponse

        return EngineDetailsResourceWithStreamingResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.EnginesResourceWithStreamingResponse:
        from .resources.engines import EnginesResourceWithStreamingResponse

        return EnginesResourceWithStreamingResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithStreamingResponse:
        from .resources.entities import EntitiesResourceWithStreamingResponse

        return EntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.EopResourceWithStreamingResponse:
        from .resources.eop import EopResourceWithStreamingResponse

        return EopResourceWithStreamingResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.EphemerisResourceWithStreamingResponse:
        from .resources.ephemeris import EphemerisResourceWithStreamingResponse

        return EphemerisResourceWithStreamingResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.EphemerisSetsResourceWithStreamingResponse:
        from .resources.ephemeris_sets import EphemerisSetsResourceWithStreamingResponse

        return EphemerisSetsResourceWithStreamingResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.EquipmentResourceWithStreamingResponse:
        from .resources.equipment import EquipmentResourceWithStreamingResponse

        return EquipmentResourceWithStreamingResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.EquipmentRemarksResourceWithStreamingResponse:
        from .resources.equipment_remarks import EquipmentRemarksResourceWithStreamingResponse

        return EquipmentRemarksResourceWithStreamingResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.EvacResourceWithStreamingResponse:
        from .resources.evac import EvacResourceWithStreamingResponse

        return EvacResourceWithStreamingResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.EventEvolutionResourceWithStreamingResponse:
        from .resources.event_evolution import EventEvolutionResourceWithStreamingResponse

        return EventEvolutionResourceWithStreamingResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.FeatureAssessmentResourceWithStreamingResponse:
        from .resources.feature_assessment import FeatureAssessmentResourceWithStreamingResponse

        return FeatureAssessmentResourceWithStreamingResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.FlightplanResourceWithStreamingResponse:
        from .resources.flightplan import FlightplanResourceWithStreamingResponse

        return FlightplanResourceWithStreamingResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.GeoStatusResourceWithStreamingResponse:
        from .resources.geo_status import GeoStatusResourceWithStreamingResponse

        return GeoStatusResourceWithStreamingResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(self) -> global_atmospheric_model.GlobalAtmosphericModelResourceWithStreamingResponse:
        from .resources.global_atmospheric_model import GlobalAtmosphericModelResourceWithStreamingResponse

        return GlobalAtmosphericModelResourceWithStreamingResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.GnssObservationsResourceWithStreamingResponse:
        from .resources.gnss_observations import GnssObservationsResourceWithStreamingResponse

        return GnssObservationsResourceWithStreamingResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.GnssObservationsetResourceWithStreamingResponse:
        from .resources.gnss_observationset import GnssObservationsetResourceWithStreamingResponse

        return GnssObservationsetResourceWithStreamingResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.GnssRawIfResourceWithStreamingResponse:
        from .resources.gnss_raw_if import GnssRawIfResourceWithStreamingResponse

        return GnssRawIfResourceWithStreamingResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.GroundImageryResourceWithStreamingResponse:
        from .resources.ground_imagery import GroundImageryResourceWithStreamingResponse

        return GroundImageryResourceWithStreamingResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.H3GeoResourceWithStreamingResponse:
        from .resources.h3_geo import H3GeoResourceWithStreamingResponse

        return H3GeoResourceWithStreamingResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.H3GeoHexCellResourceWithStreamingResponse:
        from .resources.h3_geo_hex_cell import H3GeoHexCellResourceWithStreamingResponse

        return H3GeoHexCellResourceWithStreamingResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.HazardResourceWithStreamingResponse:
        from .resources.hazard import HazardResourceWithStreamingResponse

        return HazardResourceWithStreamingResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.IonoObservationsResourceWithStreamingResponse:
        from .resources.iono_observations import IonoObservationsResourceWithStreamingResponse

        return IonoObservationsResourceWithStreamingResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.IrResourceWithStreamingResponse:
        from .resources.ir import IrResourceWithStreamingResponse

        return IrResourceWithStreamingResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.IsrCollectionsResourceWithStreamingResponse:
        from .resources.isr_collections import IsrCollectionsResourceWithStreamingResponse

        return IsrCollectionsResourceWithStreamingResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.ItemResourceWithStreamingResponse:
        from .resources.item import ItemResourceWithStreamingResponse

        return ItemResourceWithStreamingResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.ItemTrackingsResourceWithStreamingResponse:
        from .resources.item_trackings import ItemTrackingsResourceWithStreamingResponse

        return ItemTrackingsResourceWithStreamingResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.LaserdeconflictrequestResourceWithStreamingResponse:
        from .resources.laserdeconflictrequest import LaserdeconflictrequestResourceWithStreamingResponse

        return LaserdeconflictrequestResourceWithStreamingResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.LaseremitterResourceWithStreamingResponse:
        from .resources.laseremitter import LaseremitterResourceWithStreamingResponse

        return LaseremitterResourceWithStreamingResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.LaunchDetectionResourceWithStreamingResponse:
        from .resources.launch_detection import LaunchDetectionResourceWithStreamingResponse

        return LaunchDetectionResourceWithStreamingResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.LaunchEventResourceWithStreamingResponse:
        from .resources.launch_event import LaunchEventResourceWithStreamingResponse

        return LaunchEventResourceWithStreamingResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.LaunchSiteResourceWithStreamingResponse:
        from .resources.launch_site import LaunchSiteResourceWithStreamingResponse

        return LaunchSiteResourceWithStreamingResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.LaunchSiteDetailsResourceWithStreamingResponse:
        from .resources.launch_site_details import LaunchSiteDetailsResourceWithStreamingResponse

        return LaunchSiteDetailsResourceWithStreamingResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.LaunchVehicleResourceWithStreamingResponse:
        from .resources.launch_vehicle import LaunchVehicleResourceWithStreamingResponse

        return LaunchVehicleResourceWithStreamingResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.LaunchVehicleDetailsResourceWithStreamingResponse:
        from .resources.launch_vehicle_details import LaunchVehicleDetailsResourceWithStreamingResponse

        return LaunchVehicleDetailsResourceWithStreamingResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.LinkStatusResourceWithStreamingResponse:
        from .resources.link_status import LinkStatusResourceWithStreamingResponse

        return LinkStatusResourceWithStreamingResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.LinkstatusResourceWithStreamingResponse:
        from .resources.linkstatus import LinkstatusResourceWithStreamingResponse

        return LinkstatusResourceWithStreamingResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.LocationResourceWithStreamingResponse:
        from .resources.location import LocationResourceWithStreamingResponse

        return LocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.LogisticsSupportResourceWithStreamingResponse:
        from .resources.logistics_support import LogisticsSupportResourceWithStreamingResponse

        return LogisticsSupportResourceWithStreamingResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.ManeuversResourceWithStreamingResponse:
        from .resources.maneuvers import ManeuversResourceWithStreamingResponse

        return ManeuversResourceWithStreamingResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.ManifoldResourceWithStreamingResponse:
        from .resources.manifold import ManifoldResourceWithStreamingResponse

        return ManifoldResourceWithStreamingResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.ManifoldelsetResourceWithStreamingResponse:
        from .resources.manifoldelset import ManifoldelsetResourceWithStreamingResponse

        return ManifoldelsetResourceWithStreamingResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.MissileTracksResourceWithStreamingResponse:
        from .resources.missile_tracks import MissileTracksResourceWithStreamingResponse

        return MissileTracksResourceWithStreamingResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.MissionAssignmentResourceWithStreamingResponse:
        from .resources.mission_assignment import MissionAssignmentResourceWithStreamingResponse

        return MissionAssignmentResourceWithStreamingResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.MtiResourceWithStreamingResponse:
        from .resources.mti import MtiResourceWithStreamingResponse

        return MtiResourceWithStreamingResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.NavigationResourceWithStreamingResponse:
        from .resources.navigation import NavigationResourceWithStreamingResponse

        return NavigationResourceWithStreamingResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(self) -> navigational_obstruction.NavigationalObstructionResourceWithStreamingResponse:
        from .resources.navigational_obstruction import NavigationalObstructionResourceWithStreamingResponse

        return NavigationalObstructionResourceWithStreamingResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.NotificationResourceWithStreamingResponse:
        from .resources.notification import NotificationResourceWithStreamingResponse

        return NotificationResourceWithStreamingResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.ObjectOfInterestResourceWithStreamingResponse:
        from .resources.object_of_interest import ObjectOfInterestResourceWithStreamingResponse

        return ObjectOfInterestResourceWithStreamingResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.ObservationsResourceWithStreamingResponse:
        from .resources.observations import ObservationsResourceWithStreamingResponse

        return ObservationsResourceWithStreamingResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.OnboardnavigationResourceWithStreamingResponse:
        from .resources.onboardnavigation import OnboardnavigationResourceWithStreamingResponse

        return OnboardnavigationResourceWithStreamingResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.OnorbitResourceWithStreamingResponse:
        from .resources.onorbit import OnorbitResourceWithStreamingResponse

        return OnorbitResourceWithStreamingResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.OnorbitantennaResourceWithStreamingResponse:
        from .resources.onorbitantenna import OnorbitantennaResourceWithStreamingResponse

        return OnorbitantennaResourceWithStreamingResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.OnorbitbatteryResourceWithStreamingResponse:
        from .resources.onorbitbattery import OnorbitbatteryResourceWithStreamingResponse

        return OnorbitbatteryResourceWithStreamingResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.OnorbitdetailsResourceWithStreamingResponse:
        from .resources.onorbitdetails import OnorbitdetailsResourceWithStreamingResponse

        return OnorbitdetailsResourceWithStreamingResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.OnorbiteventResourceWithStreamingResponse:
        from .resources.onorbitevent import OnorbiteventResourceWithStreamingResponse

        return OnorbiteventResourceWithStreamingResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.OnorbitlistResourceWithStreamingResponse:
        from .resources.onorbitlist import OnorbitlistResourceWithStreamingResponse

        return OnorbitlistResourceWithStreamingResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.OnorbitsolararrayResourceWithStreamingResponse:
        from .resources.onorbitsolararray import OnorbitsolararrayResourceWithStreamingResponse

        return OnorbitsolararrayResourceWithStreamingResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.OnorbitthrusterResourceWithStreamingResponse:
        from .resources.onorbitthruster import OnorbitthrusterResourceWithStreamingResponse

        return OnorbitthrusterResourceWithStreamingResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.OnorbitthrusterstatusResourceWithStreamingResponse:
        from .resources.onorbitthrusterstatus import OnorbitthrusterstatusResourceWithStreamingResponse

        return OnorbitthrusterstatusResourceWithStreamingResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.OnorbitassessmentResourceWithStreamingResponse:
        from .resources.onorbitassessment import OnorbitassessmentResourceWithStreamingResponse

        return OnorbitassessmentResourceWithStreamingResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.OperatingunitResourceWithStreamingResponse:
        from .resources.operatingunit import OperatingunitResourceWithStreamingResponse

        return OperatingunitResourceWithStreamingResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.OperatingunitremarkResourceWithStreamingResponse:
        from .resources.operatingunitremark import OperatingunitremarkResourceWithStreamingResponse

        return OperatingunitremarkResourceWithStreamingResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.OrbitdeterminationResourceWithStreamingResponse:
        from .resources.orbitdetermination import OrbitdeterminationResourceWithStreamingResponse

        return OrbitdeterminationResourceWithStreamingResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.OrbittrackResourceWithStreamingResponse:
        from .resources.orbittrack import OrbittrackResourceWithStreamingResponse

        return OrbittrackResourceWithStreamingResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithStreamingResponse:
        from .resources.organization import OrganizationResourceWithStreamingResponse

        return OrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.OrganizationdetailsResourceWithStreamingResponse:
        from .resources.organizationdetails import OrganizationdetailsResourceWithStreamingResponse

        return OrganizationdetailsResourceWithStreamingResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.PersonnelrecoveryResourceWithStreamingResponse:
        from .resources.personnelrecovery import PersonnelrecoveryResourceWithStreamingResponse

        return PersonnelrecoveryResourceWithStreamingResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.PoiResourceWithStreamingResponse:
        from .resources.poi import PoiResourceWithStreamingResponse

        return PoiResourceWithStreamingResponse(self._client.poi)

    @cached_property
    def port(self) -> port.PortResourceWithStreamingResponse:
        from .resources.port import PortResourceWithStreamingResponse

        return PortResourceWithStreamingResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.ReportAndActivitiesResourceWithStreamingResponse:
        from .resources.report_and_activities import ReportAndActivitiesResourceWithStreamingResponse

        return ReportAndActivitiesResourceWithStreamingResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.RfBandResourceWithStreamingResponse:
        from .resources.rf_band import RfBandResourceWithStreamingResponse

        return RfBandResourceWithStreamingResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.RfBandTypeResourceWithStreamingResponse:
        from .resources.rf_band_type import RfBandTypeResourceWithStreamingResponse

        return RfBandTypeResourceWithStreamingResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.RfEmitterResourceWithStreamingResponse:
        from .resources.rf_emitter import RfEmitterResourceWithStreamingResponse

        return RfEmitterResourceWithStreamingResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.RouteStatsResourceWithStreamingResponse:
        from .resources.route_stats import RouteStatsResourceWithStreamingResponse

        return RouteStatsResourceWithStreamingResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.SarObservationResourceWithStreamingResponse:
        from .resources.sar_observation import SarObservationResourceWithStreamingResponse

        return SarObservationResourceWithStreamingResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.ScientificResourceWithStreamingResponse:
        from .resources.scientific import ScientificResourceWithStreamingResponse

        return ScientificResourceWithStreamingResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.ScsResourceWithStreamingResponse:
        from .resources.scs import ScsResourceWithStreamingResponse

        return ScsResourceWithStreamingResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.SecureMessagingResourceWithStreamingResponse:
        from .resources.secure_messaging import SecureMessagingResourceWithStreamingResponse

        return SecureMessagingResourceWithStreamingResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.SensorResourceWithStreamingResponse:
        from .resources.sensor import SensorResourceWithStreamingResponse

        return SensorResourceWithStreamingResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.SensorStatingResourceWithStreamingResponse:
        from .resources.sensor_stating import SensorStatingResourceWithStreamingResponse

        return SensorStatingResourceWithStreamingResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.SensorMaintenanceResourceWithStreamingResponse:
        from .resources.sensor_maintenance import SensorMaintenanceResourceWithStreamingResponse

        return SensorMaintenanceResourceWithStreamingResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(self) -> sensor_observation_type.SensorObservationTypeResourceWithStreamingResponse:
        from .resources.sensor_observation_type import SensorObservationTypeResourceWithStreamingResponse

        return SensorObservationTypeResourceWithStreamingResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.SensorPlanResourceWithStreamingResponse:
        from .resources.sensor_plan import SensorPlanResourceWithStreamingResponse

        return SensorPlanResourceWithStreamingResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.SensorTypeResourceWithStreamingResponse:
        from .resources.sensor_type import SensorTypeResourceWithStreamingResponse

        return SensorTypeResourceWithStreamingResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.SeraDataCommDetailsResourceWithStreamingResponse:
        from .resources.sera_data_comm_details import SeraDataCommDetailsResourceWithStreamingResponse

        return SeraDataCommDetailsResourceWithStreamingResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.SeraDataEarlyWarningResourceWithStreamingResponse:
        from .resources.sera_data_early_warning import SeraDataEarlyWarningResourceWithStreamingResponse

        return SeraDataEarlyWarningResourceWithStreamingResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.SeraDataNavigationResourceWithStreamingResponse:
        from .resources.sera_data_navigation import SeraDataNavigationResourceWithStreamingResponse

        return SeraDataNavigationResourceWithStreamingResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(self) -> seradata_optical_payload.SeradataOpticalPayloadResourceWithStreamingResponse:
        from .resources.seradata_optical_payload import SeradataOpticalPayloadResourceWithStreamingResponse

        return SeradataOpticalPayloadResourceWithStreamingResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.SeradataRadarPayloadResourceWithStreamingResponse:
        from .resources.seradata_radar_payload import SeradataRadarPayloadResourceWithStreamingResponse

        return SeradataRadarPayloadResourceWithStreamingResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(self) -> seradata_sigint_payload.SeradataSigintPayloadResourceWithStreamingResponse:
        from .resources.seradata_sigint_payload import SeradataSigintPayloadResourceWithStreamingResponse

        return SeradataSigintPayloadResourceWithStreamingResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.SeradataSpacecraftDetailsResourceWithStreamingResponse:
        from .resources.seradata_spacecraft_details import SeradataSpacecraftDetailsResourceWithStreamingResponse

        return SeradataSpacecraftDetailsResourceWithStreamingResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.SgiResourceWithStreamingResponse:
        from .resources.sgi import SgiResourceWithStreamingResponse

        return SgiResourceWithStreamingResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.SigactResourceWithStreamingResponse:
        from .resources.sigact import SigactResourceWithStreamingResponse

        return SigactResourceWithStreamingResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.SiteResourceWithStreamingResponse:
        from .resources.site import SiteResourceWithStreamingResponse

        return SiteResourceWithStreamingResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.SiteRemarkResourceWithStreamingResponse:
        from .resources.site_remark import SiteRemarkResourceWithStreamingResponse

        return SiteRemarkResourceWithStreamingResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.SiteStatusResourceWithStreamingResponse:
        from .resources.site_status import SiteStatusResourceWithStreamingResponse

        return SiteStatusResourceWithStreamingResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.SkyImageryResourceWithStreamingResponse:
        from .resources.sky_imagery import SkyImageryResourceWithStreamingResponse

        return SkyImageryResourceWithStreamingResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.SoiObservationSetResourceWithStreamingResponse:
        from .resources.soi_observation_set import SoiObservationSetResourceWithStreamingResponse

        return SoiObservationSetResourceWithStreamingResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.SolarArrayResourceWithStreamingResponse:
        from .resources.solar_array import SolarArrayResourceWithStreamingResponse

        return SolarArrayResourceWithStreamingResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.SolarArrayDetailsResourceWithStreamingResponse:
        from .resources.solar_array_details import SolarArrayDetailsResourceWithStreamingResponse

        return SolarArrayDetailsResourceWithStreamingResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.SortiePprResourceWithStreamingResponse:
        from .resources.sortie_ppr import SortiePprResourceWithStreamingResponse

        return SortiePprResourceWithStreamingResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.SpaceEnvObservationResourceWithStreamingResponse:
        from .resources.space_env_observation import SpaceEnvObservationResourceWithStreamingResponse

        return SpaceEnvObservationResourceWithStreamingResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.StageResourceWithStreamingResponse:
        from .resources.stage import StageResourceWithStreamingResponse

        return StageResourceWithStreamingResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.StarCatalogResourceWithStreamingResponse:
        from .resources.star_catalog import StarCatalogResourceWithStreamingResponse

        return StarCatalogResourceWithStreamingResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.StateVectorResourceWithStreamingResponse:
        from .resources.state_vector import StateVectorResourceWithStreamingResponse

        return StateVectorResourceWithStreamingResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.StatusResourceWithStreamingResponse:
        from .resources.status import StatusResourceWithStreamingResponse

        return StatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.SubstatusResourceWithStreamingResponse:
        from .resources.substatus import SubstatusResourceWithStreamingResponse

        return SubstatusResourceWithStreamingResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.SupportingDataResourceWithStreamingResponse:
        from .resources.supporting_data import SupportingDataResourceWithStreamingResponse

        return SupportingDataResourceWithStreamingResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.SurfaceResourceWithStreamingResponse:
        from .resources.surface import SurfaceResourceWithStreamingResponse

        return SurfaceResourceWithStreamingResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.SurfaceObstructionResourceWithStreamingResponse:
        from .resources.surface_obstruction import SurfaceObstructionResourceWithStreamingResponse

        return SurfaceObstructionResourceWithStreamingResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.SwirResourceWithStreamingResponse:
        from .resources.swir import SwirResourceWithStreamingResponse

        return SwirResourceWithStreamingResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.TaiUtcResourceWithStreamingResponse:
        from .resources.tai_utc import TaiUtcResourceWithStreamingResponse

        return TaiUtcResourceWithStreamingResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.TdoaFdoaResourceWithStreamingResponse:
        from .resources.tdoa_fdoa import TdoaFdoaResourceWithStreamingResponse

        return TdoaFdoaResourceWithStreamingResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.TrackResourceWithStreamingResponse:
        from .resources.track import TrackResourceWithStreamingResponse

        return TrackResourceWithStreamingResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.TrackDetailsResourceWithStreamingResponse:
        from .resources.track_details import TrackDetailsResourceWithStreamingResponse

        return TrackDetailsResourceWithStreamingResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.TrackRouteResourceWithStreamingResponse:
        from .resources.track_route import TrackRouteResourceWithStreamingResponse

        return TrackRouteResourceWithStreamingResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.TransponderResourceWithStreamingResponse:
        from .resources.transponder import TransponderResourceWithStreamingResponse

        return TransponderResourceWithStreamingResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.VesselResourceWithStreamingResponse:
        from .resources.vessel import VesselResourceWithStreamingResponse

        return VesselResourceWithStreamingResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.VideoResourceWithStreamingResponse:
        from .resources.video import VideoResourceWithStreamingResponse

        return VideoResourceWithStreamingResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.WeatherDataResourceWithStreamingResponse:
        from .resources.weather_data import WeatherDataResourceWithStreamingResponse

        return WeatherDataResourceWithStreamingResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.WeatherReportResourceWithStreamingResponse:
        from .resources.weather_report import WeatherReportResourceWithStreamingResponse

        return WeatherReportResourceWithStreamingResponse(self._client.weather_report)


class AsyncUnifieddatalibraryWithStreamedResponse:
    _client: AsyncUnifieddatalibrary

    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self._client = client

    @cached_property
    def air_events(self) -> air_events.AsyncAirEventsResourceWithStreamingResponse:
        from .resources.air_events import AsyncAirEventsResourceWithStreamingResponse

        return AsyncAirEventsResourceWithStreamingResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AsyncAirOperationsResourceWithStreamingResponse:
        from .resources.air_operations import AsyncAirOperationsResourceWithStreamingResponse

        return AsyncAirOperationsResourceWithStreamingResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AsyncAirTransportMissionsResourceWithStreamingResponse:
        from .resources.air_transport_missions import AsyncAirTransportMissionsResourceWithStreamingResponse

        return AsyncAirTransportMissionsResourceWithStreamingResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AsyncAircraftResourceWithStreamingResponse:
        from .resources.aircraft import AsyncAircraftResourceWithStreamingResponse

        return AsyncAircraftResourceWithStreamingResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AsyncAircraftSortiesResourceWithStreamingResponse:
        from .resources.aircraft_sorties import AsyncAircraftSortiesResourceWithStreamingResponse

        return AsyncAircraftSortiesResourceWithStreamingResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(
        self,
    ) -> aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithStreamingResponse:
        from .resources.aircraft_status_remarks import AsyncAircraftStatusRemarksResourceWithStreamingResponse

        return AsyncAircraftStatusRemarksResourceWithStreamingResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AsyncAircraftStatusesResourceWithStreamingResponse:
        from .resources.aircraft_statuses import AsyncAircraftStatusesResourceWithStreamingResponse

        return AsyncAircraftStatusesResourceWithStreamingResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(
        self,
    ) -> airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse:
        from .resources.airfield_slot_consumptions import AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse

        return AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AsyncAirfieldSlotsResourceWithStreamingResponse:
        from .resources.airfield_slots import AsyncAirfieldSlotsResourceWithStreamingResponse

        return AsyncAirfieldSlotsResourceWithStreamingResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AsyncAirfieldStatusResourceWithStreamingResponse:
        from .resources.airfield_status import AsyncAirfieldStatusResourceWithStreamingResponse

        return AsyncAirfieldStatusResourceWithStreamingResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AsyncAirfieldsResourceWithStreamingResponse:
        from .resources.airfields import AsyncAirfieldsResourceWithStreamingResponse

        return AsyncAirfieldsResourceWithStreamingResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AsyncAirloadPlansResourceWithStreamingResponse:
        from .resources.airload_plans import AsyncAirloadPlansResourceWithStreamingResponse

        return AsyncAirloadPlansResourceWithStreamingResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(
        self,
    ) -> airspace_control_orders.AsyncAirspaceControlOrdersResourceWithStreamingResponse:
        from .resources.airspace_control_orders import AsyncAirspaceControlOrdersResourceWithStreamingResponse

        return AsyncAirspaceControlOrdersResourceWithStreamingResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AsyncAIsResourceWithStreamingResponse:
        from .resources.ais import AsyncAIsResourceWithStreamingResponse

        return AsyncAIsResourceWithStreamingResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AsyncAIsObjectsResourceWithStreamingResponse:
        from .resources.ais_objects import AsyncAIsObjectsResourceWithStreamingResponse

        return AsyncAIsObjectsResourceWithStreamingResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AsyncAnalyticImageryResourceWithStreamingResponse:
        from .resources.analytic_imagery import AsyncAnalyticImageryResourceWithStreamingResponse

        return AsyncAnalyticImageryResourceWithStreamingResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AsyncAntennasResourceWithStreamingResponse:
        from .resources.antennas import AsyncAntennasResourceWithStreamingResponse

        return AsyncAntennasResourceWithStreamingResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AsyncAttitudeDataResourceWithStreamingResponse:
        from .resources.attitude_data import AsyncAttitudeDataResourceWithStreamingResponse

        return AsyncAttitudeDataResourceWithStreamingResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AsyncAttitudeSetsResourceWithStreamingResponse:
        from .resources.attitude_sets import AsyncAttitudeSetsResourceWithStreamingResponse

        return AsyncAttitudeSetsResourceWithStreamingResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(
        self,
    ) -> aviation_risk_management.AsyncAviationRiskManagementResourceWithStreamingResponse:
        from .resources.aviation_risk_management import AsyncAviationRiskManagementResourceWithStreamingResponse

        return AsyncAviationRiskManagementResourceWithStreamingResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.AsyncBatteriesResourceWithStreamingResponse:
        from .resources.batteries import AsyncBatteriesResourceWithStreamingResponse

        return AsyncBatteriesResourceWithStreamingResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.AsyncBatterydetailsResourceWithStreamingResponse:
        from .resources.batterydetails import AsyncBatterydetailsResourceWithStreamingResponse

        return AsyncBatterydetailsResourceWithStreamingResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.AsyncBeamResourceWithStreamingResponse:
        from .resources.beam import AsyncBeamResourceWithStreamingResponse

        return AsyncBeamResourceWithStreamingResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.AsyncBeamContoursResourceWithStreamingResponse:
        from .resources.beam_contours import AsyncBeamContoursResourceWithStreamingResponse

        return AsyncBeamContoursResourceWithStreamingResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.AsyncBusesResourceWithStreamingResponse:
        from .resources.buses import AsyncBusesResourceWithStreamingResponse

        return AsyncBusesResourceWithStreamingResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithStreamingResponse:
        from .resources.channels import AsyncChannelsResourceWithStreamingResponse

        return AsyncChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.AsyncCloselyspacedobjectsResourceWithStreamingResponse:
        from .resources.closelyspacedobjects import AsyncCloselyspacedobjectsResourceWithStreamingResponse

        return AsyncCloselyspacedobjectsResourceWithStreamingResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.AsyncCollectRequestsResourceWithStreamingResponse:
        from .resources.collect_requests import AsyncCollectRequestsResourceWithStreamingResponse

        return AsyncCollectRequestsResourceWithStreamingResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.AsyncCollectResponsesResourceWithStreamingResponse:
        from .resources.collect_responses import AsyncCollectResponsesResourceWithStreamingResponse

        return AsyncCollectResponsesResourceWithStreamingResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.AsyncCommResourceWithStreamingResponse:
        from .resources.comm import AsyncCommResourceWithStreamingResponse

        return AsyncCommResourceWithStreamingResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.AsyncConjunctionsResourceWithStreamingResponse:
        from .resources.conjunctions import AsyncConjunctionsResourceWithStreamingResponse

        return AsyncConjunctionsResourceWithStreamingResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.AsyncCotsResourceWithStreamingResponse:
        from .resources.cots import AsyncCotsResourceWithStreamingResponse

        return AsyncCotsResourceWithStreamingResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.AsyncCountriesResourceWithStreamingResponse:
        from .resources.countries import AsyncCountriesResourceWithStreamingResponse

        return AsyncCountriesResourceWithStreamingResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.AsyncCrewResourceWithStreamingResponse:
        from .resources.crew import AsyncCrewResourceWithStreamingResponse

        return AsyncCrewResourceWithStreamingResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.AsyncDeconflictsetResourceWithStreamingResponse:
        from .resources.deconflictset import AsyncDeconflictsetResourceWithStreamingResponse

        return AsyncDeconflictsetResourceWithStreamingResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.AsyncDiffOfArrivalResourceWithStreamingResponse:
        from .resources.diff_of_arrival import AsyncDiffOfArrivalResourceWithStreamingResponse

        return AsyncDiffOfArrivalResourceWithStreamingResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.AsyncDiplomaticClearanceResourceWithStreamingResponse:
        from .resources.diplomatic_clearance import AsyncDiplomaticClearanceResourceWithStreamingResponse

        return AsyncDiplomaticClearanceResourceWithStreamingResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.AsyncDriftHistoryResourceWithStreamingResponse:
        from .resources.drift_history import AsyncDriftHistoryResourceWithStreamingResponse

        return AsyncDriftHistoryResourceWithStreamingResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.AsyncDropzoneResourceWithStreamingResponse:
        from .resources.dropzone import AsyncDropzoneResourceWithStreamingResponse

        return AsyncDropzoneResourceWithStreamingResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.AsyncEcpedrResourceWithStreamingResponse:
        from .resources.ecpedr import AsyncEcpedrResourceWithStreamingResponse

        return AsyncEcpedrResourceWithStreamingResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.AsyncEffectRequestsResourceWithStreamingResponse:
        from .resources.effect_requests import AsyncEffectRequestsResourceWithStreamingResponse

        return AsyncEffectRequestsResourceWithStreamingResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.AsyncEffectResponsesResourceWithStreamingResponse:
        from .resources.effect_responses import AsyncEffectResponsesResourceWithStreamingResponse

        return AsyncEffectResponsesResourceWithStreamingResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.AsyncElsetsResourceWithStreamingResponse:
        from .resources.elsets import AsyncElsetsResourceWithStreamingResponse

        return AsyncElsetsResourceWithStreamingResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.AsyncEmireportResourceWithStreamingResponse:
        from .resources.emireport import AsyncEmireportResourceWithStreamingResponse

        return AsyncEmireportResourceWithStreamingResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.AsyncEmitterGeolocationResourceWithStreamingResponse:
        from .resources.emitter_geolocation import AsyncEmitterGeolocationResourceWithStreamingResponse

        return AsyncEmitterGeolocationResourceWithStreamingResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.AsyncEngineDetailsResourceWithStreamingResponse:
        from .resources.engine_details import AsyncEngineDetailsResourceWithStreamingResponse

        return AsyncEngineDetailsResourceWithStreamingResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.AsyncEnginesResourceWithStreamingResponse:
        from .resources.engines import AsyncEnginesResourceWithStreamingResponse

        return AsyncEnginesResourceWithStreamingResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithStreamingResponse:
        from .resources.entities import AsyncEntitiesResourceWithStreamingResponse

        return AsyncEntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.AsyncEopResourceWithStreamingResponse:
        from .resources.eop import AsyncEopResourceWithStreamingResponse

        return AsyncEopResourceWithStreamingResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.AsyncEphemerisResourceWithStreamingResponse:
        from .resources.ephemeris import AsyncEphemerisResourceWithStreamingResponse

        return AsyncEphemerisResourceWithStreamingResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.AsyncEphemerisSetsResourceWithStreamingResponse:
        from .resources.ephemeris_sets import AsyncEphemerisSetsResourceWithStreamingResponse

        return AsyncEphemerisSetsResourceWithStreamingResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.AsyncEquipmentResourceWithStreamingResponse:
        from .resources.equipment import AsyncEquipmentResourceWithStreamingResponse

        return AsyncEquipmentResourceWithStreamingResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.AsyncEquipmentRemarksResourceWithStreamingResponse:
        from .resources.equipment_remarks import AsyncEquipmentRemarksResourceWithStreamingResponse

        return AsyncEquipmentRemarksResourceWithStreamingResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.AsyncEvacResourceWithStreamingResponse:
        from .resources.evac import AsyncEvacResourceWithStreamingResponse

        return AsyncEvacResourceWithStreamingResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.AsyncEventEvolutionResourceWithStreamingResponse:
        from .resources.event_evolution import AsyncEventEvolutionResourceWithStreamingResponse

        return AsyncEventEvolutionResourceWithStreamingResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.AsyncFeatureAssessmentResourceWithStreamingResponse:
        from .resources.feature_assessment import AsyncFeatureAssessmentResourceWithStreamingResponse

        return AsyncFeatureAssessmentResourceWithStreamingResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.AsyncFlightplanResourceWithStreamingResponse:
        from .resources.flightplan import AsyncFlightplanResourceWithStreamingResponse

        return AsyncFlightplanResourceWithStreamingResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.AsyncGeoStatusResourceWithStreamingResponse:
        from .resources.geo_status import AsyncGeoStatusResourceWithStreamingResponse

        return AsyncGeoStatusResourceWithStreamingResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(
        self,
    ) -> global_atmospheric_model.AsyncGlobalAtmosphericModelResourceWithStreamingResponse:
        from .resources.global_atmospheric_model import AsyncGlobalAtmosphericModelResourceWithStreamingResponse

        return AsyncGlobalAtmosphericModelResourceWithStreamingResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.AsyncGnssObservationsResourceWithStreamingResponse:
        from .resources.gnss_observations import AsyncGnssObservationsResourceWithStreamingResponse

        return AsyncGnssObservationsResourceWithStreamingResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.AsyncGnssObservationsetResourceWithStreamingResponse:
        from .resources.gnss_observationset import AsyncGnssObservationsetResourceWithStreamingResponse

        return AsyncGnssObservationsetResourceWithStreamingResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.AsyncGnssRawIfResourceWithStreamingResponse:
        from .resources.gnss_raw_if import AsyncGnssRawIfResourceWithStreamingResponse

        return AsyncGnssRawIfResourceWithStreamingResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.AsyncGroundImageryResourceWithStreamingResponse:
        from .resources.ground_imagery import AsyncGroundImageryResourceWithStreamingResponse

        return AsyncGroundImageryResourceWithStreamingResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.AsyncH3GeoResourceWithStreamingResponse:
        from .resources.h3_geo import AsyncH3GeoResourceWithStreamingResponse

        return AsyncH3GeoResourceWithStreamingResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.AsyncH3GeoHexCellResourceWithStreamingResponse:
        from .resources.h3_geo_hex_cell import AsyncH3GeoHexCellResourceWithStreamingResponse

        return AsyncH3GeoHexCellResourceWithStreamingResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.AsyncHazardResourceWithStreamingResponse:
        from .resources.hazard import AsyncHazardResourceWithStreamingResponse

        return AsyncHazardResourceWithStreamingResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.AsyncIonoObservationsResourceWithStreamingResponse:
        from .resources.iono_observations import AsyncIonoObservationsResourceWithStreamingResponse

        return AsyncIonoObservationsResourceWithStreamingResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.AsyncIrResourceWithStreamingResponse:
        from .resources.ir import AsyncIrResourceWithStreamingResponse

        return AsyncIrResourceWithStreamingResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.AsyncIsrCollectionsResourceWithStreamingResponse:
        from .resources.isr_collections import AsyncIsrCollectionsResourceWithStreamingResponse

        return AsyncIsrCollectionsResourceWithStreamingResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.AsyncItemResourceWithStreamingResponse:
        from .resources.item import AsyncItemResourceWithStreamingResponse

        return AsyncItemResourceWithStreamingResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.AsyncItemTrackingsResourceWithStreamingResponse:
        from .resources.item_trackings import AsyncItemTrackingsResourceWithStreamingResponse

        return AsyncItemTrackingsResourceWithStreamingResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.AsyncLaserdeconflictrequestResourceWithStreamingResponse:
        from .resources.laserdeconflictrequest import AsyncLaserdeconflictrequestResourceWithStreamingResponse

        return AsyncLaserdeconflictrequestResourceWithStreamingResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.AsyncLaseremitterResourceWithStreamingResponse:
        from .resources.laseremitter import AsyncLaseremitterResourceWithStreamingResponse

        return AsyncLaseremitterResourceWithStreamingResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.AsyncLaunchDetectionResourceWithStreamingResponse:
        from .resources.launch_detection import AsyncLaunchDetectionResourceWithStreamingResponse

        return AsyncLaunchDetectionResourceWithStreamingResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.AsyncLaunchEventResourceWithStreamingResponse:
        from .resources.launch_event import AsyncLaunchEventResourceWithStreamingResponse

        return AsyncLaunchEventResourceWithStreamingResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.AsyncLaunchSiteResourceWithStreamingResponse:
        from .resources.launch_site import AsyncLaunchSiteResourceWithStreamingResponse

        return AsyncLaunchSiteResourceWithStreamingResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.AsyncLaunchSiteDetailsResourceWithStreamingResponse:
        from .resources.launch_site_details import AsyncLaunchSiteDetailsResourceWithStreamingResponse

        return AsyncLaunchSiteDetailsResourceWithStreamingResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.AsyncLaunchVehicleResourceWithStreamingResponse:
        from .resources.launch_vehicle import AsyncLaunchVehicleResourceWithStreamingResponse

        return AsyncLaunchVehicleResourceWithStreamingResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.AsyncLaunchVehicleDetailsResourceWithStreamingResponse:
        from .resources.launch_vehicle_details import AsyncLaunchVehicleDetailsResourceWithStreamingResponse

        return AsyncLaunchVehicleDetailsResourceWithStreamingResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.AsyncLinkStatusResourceWithStreamingResponse:
        from .resources.link_status import AsyncLinkStatusResourceWithStreamingResponse

        return AsyncLinkStatusResourceWithStreamingResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.AsyncLinkstatusResourceWithStreamingResponse:
        from .resources.linkstatus import AsyncLinkstatusResourceWithStreamingResponse

        return AsyncLinkstatusResourceWithStreamingResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithStreamingResponse:
        from .resources.location import AsyncLocationResourceWithStreamingResponse

        return AsyncLocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.AsyncLogisticsSupportResourceWithStreamingResponse:
        from .resources.logistics_support import AsyncLogisticsSupportResourceWithStreamingResponse

        return AsyncLogisticsSupportResourceWithStreamingResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.AsyncManeuversResourceWithStreamingResponse:
        from .resources.maneuvers import AsyncManeuversResourceWithStreamingResponse

        return AsyncManeuversResourceWithStreamingResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.AsyncManifoldResourceWithStreamingResponse:
        from .resources.manifold import AsyncManifoldResourceWithStreamingResponse

        return AsyncManifoldResourceWithStreamingResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.AsyncManifoldelsetResourceWithStreamingResponse:
        from .resources.manifoldelset import AsyncManifoldelsetResourceWithStreamingResponse

        return AsyncManifoldelsetResourceWithStreamingResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.AsyncMissileTracksResourceWithStreamingResponse:
        from .resources.missile_tracks import AsyncMissileTracksResourceWithStreamingResponse

        return AsyncMissileTracksResourceWithStreamingResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.AsyncMissionAssignmentResourceWithStreamingResponse:
        from .resources.mission_assignment import AsyncMissionAssignmentResourceWithStreamingResponse

        return AsyncMissionAssignmentResourceWithStreamingResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.AsyncMtiResourceWithStreamingResponse:
        from .resources.mti import AsyncMtiResourceWithStreamingResponse

        return AsyncMtiResourceWithStreamingResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.AsyncNavigationResourceWithStreamingResponse:
        from .resources.navigation import AsyncNavigationResourceWithStreamingResponse

        return AsyncNavigationResourceWithStreamingResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(
        self,
    ) -> navigational_obstruction.AsyncNavigationalObstructionResourceWithStreamingResponse:
        from .resources.navigational_obstruction import AsyncNavigationalObstructionResourceWithStreamingResponse

        return AsyncNavigationalObstructionResourceWithStreamingResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.AsyncNotificationResourceWithStreamingResponse:
        from .resources.notification import AsyncNotificationResourceWithStreamingResponse

        return AsyncNotificationResourceWithStreamingResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.AsyncObjectOfInterestResourceWithStreamingResponse:
        from .resources.object_of_interest import AsyncObjectOfInterestResourceWithStreamingResponse

        return AsyncObjectOfInterestResourceWithStreamingResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.AsyncObservationsResourceWithStreamingResponse:
        from .resources.observations import AsyncObservationsResourceWithStreamingResponse

        return AsyncObservationsResourceWithStreamingResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.AsyncOnboardnavigationResourceWithStreamingResponse:
        from .resources.onboardnavigation import AsyncOnboardnavigationResourceWithStreamingResponse

        return AsyncOnboardnavigationResourceWithStreamingResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.AsyncOnorbitResourceWithStreamingResponse:
        from .resources.onorbit import AsyncOnorbitResourceWithStreamingResponse

        return AsyncOnorbitResourceWithStreamingResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.AsyncOnorbitantennaResourceWithStreamingResponse:
        from .resources.onorbitantenna import AsyncOnorbitantennaResourceWithStreamingResponse

        return AsyncOnorbitantennaResourceWithStreamingResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.AsyncOnorbitbatteryResourceWithStreamingResponse:
        from .resources.onorbitbattery import AsyncOnorbitbatteryResourceWithStreamingResponse

        return AsyncOnorbitbatteryResourceWithStreamingResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.AsyncOnorbitdetailsResourceWithStreamingResponse:
        from .resources.onorbitdetails import AsyncOnorbitdetailsResourceWithStreamingResponse

        return AsyncOnorbitdetailsResourceWithStreamingResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.AsyncOnorbiteventResourceWithStreamingResponse:
        from .resources.onorbitevent import AsyncOnorbiteventResourceWithStreamingResponse

        return AsyncOnorbiteventResourceWithStreamingResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.AsyncOnorbitlistResourceWithStreamingResponse:
        from .resources.onorbitlist import AsyncOnorbitlistResourceWithStreamingResponse

        return AsyncOnorbitlistResourceWithStreamingResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.AsyncOnorbitsolararrayResourceWithStreamingResponse:
        from .resources.onorbitsolararray import AsyncOnorbitsolararrayResourceWithStreamingResponse

        return AsyncOnorbitsolararrayResourceWithStreamingResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.AsyncOnorbitthrusterResourceWithStreamingResponse:
        from .resources.onorbitthruster import AsyncOnorbitthrusterResourceWithStreamingResponse

        return AsyncOnorbitthrusterResourceWithStreamingResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.AsyncOnorbitthrusterstatusResourceWithStreamingResponse:
        from .resources.onorbitthrusterstatus import AsyncOnorbitthrusterstatusResourceWithStreamingResponse

        return AsyncOnorbitthrusterstatusResourceWithStreamingResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.AsyncOnorbitassessmentResourceWithStreamingResponse:
        from .resources.onorbitassessment import AsyncOnorbitassessmentResourceWithStreamingResponse

        return AsyncOnorbitassessmentResourceWithStreamingResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.AsyncOperatingunitResourceWithStreamingResponse:
        from .resources.operatingunit import AsyncOperatingunitResourceWithStreamingResponse

        return AsyncOperatingunitResourceWithStreamingResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.AsyncOperatingunitremarkResourceWithStreamingResponse:
        from .resources.operatingunitremark import AsyncOperatingunitremarkResourceWithStreamingResponse

        return AsyncOperatingunitremarkResourceWithStreamingResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.AsyncOrbitdeterminationResourceWithStreamingResponse:
        from .resources.orbitdetermination import AsyncOrbitdeterminationResourceWithStreamingResponse

        return AsyncOrbitdeterminationResourceWithStreamingResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.AsyncOrbittrackResourceWithStreamingResponse:
        from .resources.orbittrack import AsyncOrbittrackResourceWithStreamingResponse

        return AsyncOrbittrackResourceWithStreamingResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithStreamingResponse:
        from .resources.organization import AsyncOrganizationResourceWithStreamingResponse

        return AsyncOrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.AsyncOrganizationdetailsResourceWithStreamingResponse:
        from .resources.organizationdetails import AsyncOrganizationdetailsResourceWithStreamingResponse

        return AsyncOrganizationdetailsResourceWithStreamingResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.AsyncPersonnelrecoveryResourceWithStreamingResponse:
        from .resources.personnelrecovery import AsyncPersonnelrecoveryResourceWithStreamingResponse

        return AsyncPersonnelrecoveryResourceWithStreamingResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.AsyncPoiResourceWithStreamingResponse:
        from .resources.poi import AsyncPoiResourceWithStreamingResponse

        return AsyncPoiResourceWithStreamingResponse(self._client.poi)

    @cached_property
    def port(self) -> port.AsyncPortResourceWithStreamingResponse:
        from .resources.port import AsyncPortResourceWithStreamingResponse

        return AsyncPortResourceWithStreamingResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.AsyncReportAndActivitiesResourceWithStreamingResponse:
        from .resources.report_and_activities import AsyncReportAndActivitiesResourceWithStreamingResponse

        return AsyncReportAndActivitiesResourceWithStreamingResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.AsyncRfBandResourceWithStreamingResponse:
        from .resources.rf_band import AsyncRfBandResourceWithStreamingResponse

        return AsyncRfBandResourceWithStreamingResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.AsyncRfBandTypeResourceWithStreamingResponse:
        from .resources.rf_band_type import AsyncRfBandTypeResourceWithStreamingResponse

        return AsyncRfBandTypeResourceWithStreamingResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.AsyncRfEmitterResourceWithStreamingResponse:
        from .resources.rf_emitter import AsyncRfEmitterResourceWithStreamingResponse

        return AsyncRfEmitterResourceWithStreamingResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.AsyncRouteStatsResourceWithStreamingResponse:
        from .resources.route_stats import AsyncRouteStatsResourceWithStreamingResponse

        return AsyncRouteStatsResourceWithStreamingResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.AsyncSarObservationResourceWithStreamingResponse:
        from .resources.sar_observation import AsyncSarObservationResourceWithStreamingResponse

        return AsyncSarObservationResourceWithStreamingResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.AsyncScientificResourceWithStreamingResponse:
        from .resources.scientific import AsyncScientificResourceWithStreamingResponse

        return AsyncScientificResourceWithStreamingResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.AsyncScsResourceWithStreamingResponse:
        from .resources.scs import AsyncScsResourceWithStreamingResponse

        return AsyncScsResourceWithStreamingResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.AsyncSecureMessagingResourceWithStreamingResponse:
        from .resources.secure_messaging import AsyncSecureMessagingResourceWithStreamingResponse

        return AsyncSecureMessagingResourceWithStreamingResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.AsyncSensorResourceWithStreamingResponse:
        from .resources.sensor import AsyncSensorResourceWithStreamingResponse

        return AsyncSensorResourceWithStreamingResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.AsyncSensorStatingResourceWithStreamingResponse:
        from .resources.sensor_stating import AsyncSensorStatingResourceWithStreamingResponse

        return AsyncSensorStatingResourceWithStreamingResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.AsyncSensorMaintenanceResourceWithStreamingResponse:
        from .resources.sensor_maintenance import AsyncSensorMaintenanceResourceWithStreamingResponse

        return AsyncSensorMaintenanceResourceWithStreamingResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(
        self,
    ) -> sensor_observation_type.AsyncSensorObservationTypeResourceWithStreamingResponse:
        from .resources.sensor_observation_type import AsyncSensorObservationTypeResourceWithStreamingResponse

        return AsyncSensorObservationTypeResourceWithStreamingResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.AsyncSensorPlanResourceWithStreamingResponse:
        from .resources.sensor_plan import AsyncSensorPlanResourceWithStreamingResponse

        return AsyncSensorPlanResourceWithStreamingResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.AsyncSensorTypeResourceWithStreamingResponse:
        from .resources.sensor_type import AsyncSensorTypeResourceWithStreamingResponse

        return AsyncSensorTypeResourceWithStreamingResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.AsyncSeraDataCommDetailsResourceWithStreamingResponse:
        from .resources.sera_data_comm_details import AsyncSeraDataCommDetailsResourceWithStreamingResponse

        return AsyncSeraDataCommDetailsResourceWithStreamingResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.AsyncSeraDataEarlyWarningResourceWithStreamingResponse:
        from .resources.sera_data_early_warning import AsyncSeraDataEarlyWarningResourceWithStreamingResponse

        return AsyncSeraDataEarlyWarningResourceWithStreamingResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.AsyncSeraDataNavigationResourceWithStreamingResponse:
        from .resources.sera_data_navigation import AsyncSeraDataNavigationResourceWithStreamingResponse

        return AsyncSeraDataNavigationResourceWithStreamingResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(
        self,
    ) -> seradata_optical_payload.AsyncSeradataOpticalPayloadResourceWithStreamingResponse:
        from .resources.seradata_optical_payload import AsyncSeradataOpticalPayloadResourceWithStreamingResponse

        return AsyncSeradataOpticalPayloadResourceWithStreamingResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.AsyncSeradataRadarPayloadResourceWithStreamingResponse:
        from .resources.seradata_radar_payload import AsyncSeradataRadarPayloadResourceWithStreamingResponse

        return AsyncSeradataRadarPayloadResourceWithStreamingResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(
        self,
    ) -> seradata_sigint_payload.AsyncSeradataSigintPayloadResourceWithStreamingResponse:
        from .resources.seradata_sigint_payload import AsyncSeradataSigintPayloadResourceWithStreamingResponse

        return AsyncSeradataSigintPayloadResourceWithStreamingResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse:
        from .resources.seradata_spacecraft_details import AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse

        return AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.AsyncSgiResourceWithStreamingResponse:
        from .resources.sgi import AsyncSgiResourceWithStreamingResponse

        return AsyncSgiResourceWithStreamingResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.AsyncSigactResourceWithStreamingResponse:
        from .resources.sigact import AsyncSigactResourceWithStreamingResponse

        return AsyncSigactResourceWithStreamingResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.AsyncSiteResourceWithStreamingResponse:
        from .resources.site import AsyncSiteResourceWithStreamingResponse

        return AsyncSiteResourceWithStreamingResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.AsyncSiteRemarkResourceWithStreamingResponse:
        from .resources.site_remark import AsyncSiteRemarkResourceWithStreamingResponse

        return AsyncSiteRemarkResourceWithStreamingResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.AsyncSiteStatusResourceWithStreamingResponse:
        from .resources.site_status import AsyncSiteStatusResourceWithStreamingResponse

        return AsyncSiteStatusResourceWithStreamingResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.AsyncSkyImageryResourceWithStreamingResponse:
        from .resources.sky_imagery import AsyncSkyImageryResourceWithStreamingResponse

        return AsyncSkyImageryResourceWithStreamingResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.AsyncSoiObservationSetResourceWithStreamingResponse:
        from .resources.soi_observation_set import AsyncSoiObservationSetResourceWithStreamingResponse

        return AsyncSoiObservationSetResourceWithStreamingResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.AsyncSolarArrayResourceWithStreamingResponse:
        from .resources.solar_array import AsyncSolarArrayResourceWithStreamingResponse

        return AsyncSolarArrayResourceWithStreamingResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.AsyncSolarArrayDetailsResourceWithStreamingResponse:
        from .resources.solar_array_details import AsyncSolarArrayDetailsResourceWithStreamingResponse

        return AsyncSolarArrayDetailsResourceWithStreamingResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.AsyncSortiePprResourceWithStreamingResponse:
        from .resources.sortie_ppr import AsyncSortiePprResourceWithStreamingResponse

        return AsyncSortiePprResourceWithStreamingResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.AsyncSpaceEnvObservationResourceWithStreamingResponse:
        from .resources.space_env_observation import AsyncSpaceEnvObservationResourceWithStreamingResponse

        return AsyncSpaceEnvObservationResourceWithStreamingResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.AsyncStageResourceWithStreamingResponse:
        from .resources.stage import AsyncStageResourceWithStreamingResponse

        return AsyncStageResourceWithStreamingResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.AsyncStarCatalogResourceWithStreamingResponse:
        from .resources.star_catalog import AsyncStarCatalogResourceWithStreamingResponse

        return AsyncStarCatalogResourceWithStreamingResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.AsyncStateVectorResourceWithStreamingResponse:
        from .resources.state_vector import AsyncStateVectorResourceWithStreamingResponse

        return AsyncStateVectorResourceWithStreamingResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithStreamingResponse:
        from .resources.status import AsyncStatusResourceWithStreamingResponse

        return AsyncStatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.AsyncSubstatusResourceWithStreamingResponse:
        from .resources.substatus import AsyncSubstatusResourceWithStreamingResponse

        return AsyncSubstatusResourceWithStreamingResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.AsyncSupportingDataResourceWithStreamingResponse:
        from .resources.supporting_data import AsyncSupportingDataResourceWithStreamingResponse

        return AsyncSupportingDataResourceWithStreamingResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.AsyncSurfaceResourceWithStreamingResponse:
        from .resources.surface import AsyncSurfaceResourceWithStreamingResponse

        return AsyncSurfaceResourceWithStreamingResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.AsyncSurfaceObstructionResourceWithStreamingResponse:
        from .resources.surface_obstruction import AsyncSurfaceObstructionResourceWithStreamingResponse

        return AsyncSurfaceObstructionResourceWithStreamingResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.AsyncSwirResourceWithStreamingResponse:
        from .resources.swir import AsyncSwirResourceWithStreamingResponse

        return AsyncSwirResourceWithStreamingResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.AsyncTaiUtcResourceWithStreamingResponse:
        from .resources.tai_utc import AsyncTaiUtcResourceWithStreamingResponse

        return AsyncTaiUtcResourceWithStreamingResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.AsyncTdoaFdoaResourceWithStreamingResponse:
        from .resources.tdoa_fdoa import AsyncTdoaFdoaResourceWithStreamingResponse

        return AsyncTdoaFdoaResourceWithStreamingResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.AsyncTrackResourceWithStreamingResponse:
        from .resources.track import AsyncTrackResourceWithStreamingResponse

        return AsyncTrackResourceWithStreamingResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.AsyncTrackDetailsResourceWithStreamingResponse:
        from .resources.track_details import AsyncTrackDetailsResourceWithStreamingResponse

        return AsyncTrackDetailsResourceWithStreamingResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.AsyncTrackRouteResourceWithStreamingResponse:
        from .resources.track_route import AsyncTrackRouteResourceWithStreamingResponse

        return AsyncTrackRouteResourceWithStreamingResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.AsyncTransponderResourceWithStreamingResponse:
        from .resources.transponder import AsyncTransponderResourceWithStreamingResponse

        return AsyncTransponderResourceWithStreamingResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.AsyncVesselResourceWithStreamingResponse:
        from .resources.vessel import AsyncVesselResourceWithStreamingResponse

        return AsyncVesselResourceWithStreamingResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.AsyncVideoResourceWithStreamingResponse:
        from .resources.video import AsyncVideoResourceWithStreamingResponse

        return AsyncVideoResourceWithStreamingResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.AsyncWeatherDataResourceWithStreamingResponse:
        from .resources.weather_data import AsyncWeatherDataResourceWithStreamingResponse

        return AsyncWeatherDataResourceWithStreamingResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.AsyncWeatherReportResourceWithStreamingResponse:
        from .resources.weather_report import AsyncWeatherReportResourceWithStreamingResponse

        return AsyncWeatherReportResourceWithStreamingResponse(self._client.weather_report)


Client = Unifieddatalibrary

AsyncClient = AsyncUnifieddatalibrary
