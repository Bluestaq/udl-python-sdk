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
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_events import AirEventsResource

        return AirEventsResource(self)

    @cached_property
    def air_operations(self) -> AirOperationsResource:
        from .resources.air_operations import AirOperationsResource

        return AirOperationsResource(self)

    @cached_property
    def air_transport_missions(self) -> AirTransportMissionsResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_transport_missions import AirTransportMissionsResource

        return AirTransportMissionsResource(self)

    @cached_property
    def aircraft(self) -> AircraftResource:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft import AircraftResource

        return AircraftResource(self)

    @cached_property
    def aircraft_sorties(self) -> AircraftSortiesResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aircraft_sorties import AircraftSortiesResource

        return AircraftSortiesResource(self)

    @cached_property
    def aircraft_status_remarks(self) -> AircraftStatusRemarksResource:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_status_remarks import AircraftStatusRemarksResource

        return AircraftStatusRemarksResource(self)

    @cached_property
    def aircraft_statuses(self) -> AircraftStatusesResource:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_statuses import AircraftStatusesResource

        return AircraftStatusesResource(self)

    @cached_property
    def airfield_slot_consumptions(self) -> AirfieldSlotConsumptionsResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slot_consumptions import AirfieldSlotConsumptionsResource

        return AirfieldSlotConsumptionsResource(self)

    @cached_property
    def airfield_slots(self) -> AirfieldSlotsResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slots import AirfieldSlotsResource

        return AirfieldSlotsResource(self)

    @cached_property
    def airfield_status(self) -> AirfieldStatusResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_status import AirfieldStatusResource

        return AirfieldStatusResource(self)

    @cached_property
    def airfields(self) -> AirfieldsResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfields import AirfieldsResource

        return AirfieldsResource(self)

    @cached_property
    def airload_plans(self) -> AirloadPlansResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airload_plans import AirloadPlansResource

        return AirloadPlansResource(self)

    @cached_property
    def airspace_control_orders(self) -> AirspaceControlOrdersResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airspace_control_orders import AirspaceControlOrdersResource

        return AirspaceControlOrdersResource(self)

    @cached_property
    def ais(self) -> AIsResource:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais import AIsResource

        return AIsResource(self)

    @cached_property
    def ais_objects(self) -> AIsObjectsResource:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais_objects import AIsObjectsResource

        return AIsObjectsResource(self)

    @cached_property
    def analytic_imagery(self) -> AnalyticImageryResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.analytic_imagery import AnalyticImageryResource

        return AnalyticImageryResource(self)

    @cached_property
    def antennas(self) -> AntennasResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.antennas import AntennasResource

        return AntennasResource(self)

    @cached_property
    def attitude_data(self) -> AttitudeDataResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_data import AttitudeDataResource

        return AttitudeDataResource(self)

    @cached_property
    def attitude_sets(self) -> AttitudeSetsResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_sets import AttitudeSetsResource

        return AttitudeSetsResource(self)

    @cached_property
    def aviation_risk_management(self) -> AviationRiskManagementResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aviation_risk_management import AviationRiskManagementResource

        return AviationRiskManagementResource(self)

    @cached_property
    def batteries(self) -> BatteriesResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batteries import BatteriesResource

        return BatteriesResource(self)

    @cached_property
    def batterydetails(self) -> BatterydetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batterydetails import BatterydetailsResource

        return BatterydetailsResource(self)

    @cached_property
    def beam(self) -> BeamResource:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam import BeamResource

        return BeamResource(self)

    @cached_property
    def beam_contours(self) -> BeamContoursResource:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam_contours import BeamContoursResource

        return BeamContoursResource(self)

    @cached_property
    def buses(self) -> BusesResource:
        """Services for querying and manipulation of satellite buses.

        A bus is the physical and software infrastructure backbone to which on-orbit satellite payloads are attached for power, control, and other support functions.
        """
        from .resources.buses import BusesResource

        return BusesResource(self)

    @cached_property
    def channels(self) -> ChannelsResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.channels import ChannelsResource

        return ChannelsResource(self)

    @cached_property
    def closelyspacedobjects(self) -> CloselyspacedobjectsResource:
        """
        This collection of services provides operations for manipulating and querying of closely spaced objects (on orbit) operations including docking, rendezvous, proximity and reporting of payload zone engagements observed and characterized over a period of time.
        """
        from .resources.closelyspacedobjects import CloselyspacedobjectsResource

        return CloselyspacedobjectsResource(self)

    @cached_property
    def collect_requests(self) -> CollectRequestsResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_requests import CollectRequestsResource

        return CollectRequestsResource(self)

    @cached_property
    def collect_responses(self) -> CollectResponsesResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_responses import CollectResponsesResource

        return CollectResponsesResource(self)

    @cached_property
    def comm(self) -> CommResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.comm import CommResource

        return CommResource(self)

    @cached_property
    def conjunctions(self) -> ConjunctionsResource:
        """
        These services provide operations for manipulation and querying of conjunctions.
        """
        from .resources.conjunctions import ConjunctionsResource

        return ConjunctionsResource(self)

    @cached_property
    def cots(self) -> CotsResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.cots import CotsResource

        return CotsResource(self)

    @cached_property
    def countries(self) -> CountriesResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.countries import CountriesResource

        return CountriesResource(self)

    @cached_property
    def crew(self) -> CrewResource:
        """These services provide operations for posting and querying crew data.

        Crew data contains information about its members and their assignments.
        """
        from .resources.crew import CrewResource

        return CrewResource(self)

    @cached_property
    def deconflictset(self) -> DeconflictsetResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.deconflictset import DeconflictsetResource

        return DeconflictsetResource(self)

    @cached_property
    def diff_of_arrival(self) -> DiffOfArrivalResource:
        """
        These services provide operations for querying and manipulation of Signal time and frequency difference of arrival (TDOA/FDOA) information obtained by using passive RF based sensor phenomenologies and sensor triangulation. The J2000 coordinate frame is the preferred frame for all observations, but in some cases observations may be in another frame depending on the provider.
        """
        from .resources.diff_of_arrival import DiffOfArrivalResource

        return DiffOfArrivalResource(self)

    @cached_property
    def diplomatic_clearance(self) -> DiplomaticClearanceResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.diplomatic_clearance import DiplomaticClearanceResource

        return DiplomaticClearanceResource(self)

    @cached_property
    def drift_history(self) -> DriftHistoryResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.drift_history import DriftHistoryResource

        return DriftHistoryResource(self)

    @cached_property
    def dropzone(self) -> DropzoneResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.dropzone import DropzoneResource

        return DropzoneResource(self)

    @cached_property
    def ecpedr(self) -> EcpedrResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.ecpedr import EcpedrResource

        return EcpedrResource(self)

    @cached_property
    def effect_requests(self) -> EffectRequestsResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_requests import EffectRequestsResource

        return EffectRequestsResource(self)

    @cached_property
    def effect_responses(self) -> EffectResponsesResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_responses import EffectResponsesResource

        return EffectResponsesResource(self)

    @cached_property
    def elsets(self) -> ElsetsResource:
        """
        These services provide operations for querying and manipulation of element set data describing orbital characteristics of on-orbit objects. An element set is a collection of parameters that are used, along with an orbit propagator, to predict the motion of a satellite. The element set, or elset for short, consists of identification data, the classical elements and drag parameters.
        """
        from .resources.elsets import ElsetsResource

        return ElsetsResource(self)

    @cached_property
    def emireport(self) -> EmireportResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emireport import EmireportResource

        return EmireportResource(self)

    @cached_property
    def emitter_geolocation(self) -> EmitterGeolocationResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emitter_geolocation import EmitterGeolocationResource

        return EmitterGeolocationResource(self)

    @cached_property
    def engine_details(self) -> EngineDetailsResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engine_details import EngineDetailsResource

        return EngineDetailsResource(self)

    @cached_property
    def engines(self) -> EnginesResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engines import EnginesResource

        return EnginesResource(self)

    @cached_property
    def entities(self) -> EntitiesResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.entities import EntitiesResource

        return EntitiesResource(self)

    @cached_property
    def eop(self) -> EopResource:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.eop import EopResource

        return EopResource(self)

    @cached_property
    def ephemeris(self) -> EphemerisResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris import EphemerisResource

        return EphemerisResource(self)

    @cached_property
    def ephemeris_sets(self) -> EphemerisSetsResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris_sets import EphemerisSetsResource

        return EphemerisSetsResource(self)

    @cached_property
    def equipment(self) -> EquipmentResource:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment import EquipmentResource

        return EquipmentResource(self)

    @cached_property
    def equipment_remarks(self) -> EquipmentRemarksResource:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment_remarks import EquipmentRemarksResource

        return EquipmentRemarksResource(self)

    @cached_property
    def evac(self) -> EvacResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.evac import EvacResource

        return EvacResource(self)

    @cached_property
    def event_evolution(self) -> EventEvolutionResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.event_evolution import EventEvolutionResource

        return EventEvolutionResource(self)

    @cached_property
    def feature_assessment(self) -> FeatureAssessmentResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.feature_assessment import FeatureAssessmentResource

        return FeatureAssessmentResource(self)

    @cached_property
    def flightplan(self) -> FlightplanResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.flightplan import FlightplanResource

        return FlightplanResource(self)

    @cached_property
    def geo_status(self) -> GeoStatusResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.geo_status import GeoStatusResource

        return GeoStatusResource(self)

    @cached_property
    def global_atmospheric_model(self) -> GlobalAtmosphericModelResource:
        """
        Models and Simulations is a collection of services that allow consumers to interact with data products representing independent models of various phenomenon, artificial intelligence models and predictions, or of mathematical parameters meant to feed mod and sim tools to produce estimates of environmental entities such as atmospheric models and heat maps.
        """
        from .resources.global_atmospheric_model import GlobalAtmosphericModelResource

        return GlobalAtmosphericModelResource(self)

    @cached_property
    def gnss_observations(self) -> GnssObservationsResource:
        from .resources.gnss_observations import GnssObservationsResource

        return GnssObservationsResource(self)

    @cached_property
    def gnss_observationset(self) -> GnssObservationsetResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_observationset import GnssObservationsetResource

        return GnssObservationsetResource(self)

    @cached_property
    def gnss_raw_if(self) -> GnssRawIfResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_raw_if import GnssRawIfResource

        return GnssRawIfResource(self)

    @cached_property
    def ground_imagery(self) -> GroundImageryResource:
        """
        This collection of services provides operations for querying and manipulation of ground imagery of terrestrial regions from on-orbit, air, and other sensors. Includes metadata on the image (time, region, source, etc) as well as binary content (typically GeoTIFF). Binary content must be downloaded individually by ID using the 'getFile' operation. Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.ground_imagery import GroundImageryResource

        return GroundImageryResource(self)

    @cached_property
    def h3_geo(self) -> H3GeoResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo import H3GeoResource

        return H3GeoResource(self)

    @cached_property
    def h3_geo_hex_cell(self) -> H3GeoHexCellResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo_hex_cell import H3GeoHexCellResource

        return H3GeoHexCellResource(self)

    @cached_property
    def hazard(self) -> HazardResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.hazard import HazardResource

        return HazardResource(self)

    @cached_property
    def iono_observations(self) -> IonoObservationsResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.iono_observations import IonoObservationsResource

        return IonoObservationsResource(self)

    @cached_property
    def ir(self) -> IrResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.ir import IrResource

        return IrResource(self)

    @cached_property
    def isr_collections(self) -> IsrCollectionsResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.isr_collections import IsrCollectionsResource

        return IsrCollectionsResource(self)

    @cached_property
    def item(self) -> ItemResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item import ItemResource

        return ItemResource(self)

    @cached_property
    def item_trackings(self) -> ItemTrackingsResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item_trackings import ItemTrackingsResource

        return ItemTrackingsResource(self)

    @cached_property
    def laserdeconflictrequest(self) -> LaserdeconflictrequestResource:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laserdeconflictrequest import LaserdeconflictrequestResource

        return LaserdeconflictrequestResource(self)

    @cached_property
    def laseremitter(self) -> LaseremitterResource:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laseremitter import LaseremitterResource

        return LaseremitterResource(self)

    @cached_property
    def launch_detection(self) -> LaunchDetectionResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_detection import LaunchDetectionResource

        return LaunchDetectionResource(self)

    @cached_property
    def launch_event(self) -> LaunchEventResource:
        """
        These services provide operations for manipulation and querying of LaunchEvent data. Launch Event data are known space launches, either future or historic records containing items such as the launch site, launch epoch, and object.
        """
        from .resources.launch_event import LaunchEventResource

        return LaunchEventResource(self)

    @cached_property
    def launch_site(self) -> LaunchSiteResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site import LaunchSiteResource

        return LaunchSiteResource(self)

    @cached_property
    def launch_site_details(self) -> LaunchSiteDetailsResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site_details import LaunchSiteDetailsResource

        return LaunchSiteDetailsResource(self)

    @cached_property
    def launch_vehicle(self) -> LaunchVehicleResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle import LaunchVehicleResource

        return LaunchVehicleResource(self)

    @cached_property
    def launch_vehicle_details(self) -> LaunchVehicleDetailsResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle_details import LaunchVehicleDetailsResource

        return LaunchVehicleDetailsResource(self)

    @cached_property
    def link_status(self) -> LinkStatusResource:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.link_status import LinkStatusResource

        return LinkStatusResource(self)

    @cached_property
    def linkstatus(self) -> LinkstatusResource:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.linkstatus import LinkstatusResource

        return LinkstatusResource(self)

    @cached_property
    def location(self) -> LocationResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.location import LocationResource

        return LocationResource(self)

    @cached_property
    def logistics_support(self) -> LogisticsSupportResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.logistics_support import LogisticsSupportResource

        return LogisticsSupportResource(self)

    @cached_property
    def maneuvers(self) -> ManeuversResource:
        """
        This service provides operations for querying and manipulation of detected/possible/confirmed on-orbit maneuvers. The J2000 coordinate frame is the preferred frame for all maneuver data, but in some cases data may be in another frame depending on the provider. Check the Storefront 'Data Products' section under the 'Discover' tab for maneuver data provider information.
        """
        from .resources.maneuvers import ManeuversResource

        return ManeuversResource(self)

    @cached_property
    def manifold(self) -> ManifoldResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifold import ManifoldResource

        return ManifoldResource(self)

    @cached_property
    def manifoldelset(self) -> ManifoldelsetResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifoldelset import ManifoldelsetResource

        return ManifoldelsetResource(self)

    @cached_property
    def missile_tracks(self) -> MissileTracksResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.missile_tracks import MissileTracksResource

        return MissileTracksResource(self)

    @cached_property
    def mission_assignment(self) -> MissionAssignmentResource:
        """
        These services provide operations for manipulation and querying of mission assignment objects. MissionAssignment is used by C2 JUs and, optionally, non-C2 JUs to assign missions, designate targets, and provide target information to non-C2 JU platforms. Provision is made for the non-C2 JU platforms to acknowledge the message through receipt/compliance action.
        """
        from .resources.mission_assignment import MissionAssignmentResource

        return MissionAssignmentResource(self)

    @cached_property
    def mti(self) -> MtiResource:
        """
        These services provide operations for posting and querying Moving Target Indicator (MTI) STANAG 4607 data. Detailed MTI data supports activities such as targeting or less detailed data for applications such as situational awareness used/derived by exploitation systems.
        """
        from .resources.mti import MtiResource

        return MtiResource(self)

    @cached_property
    def navigation(self) -> NavigationResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.navigation import NavigationResource

        return NavigationResource(self)

    @cached_property
    def navigational_obstruction(self) -> NavigationalObstructionResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.navigational_obstruction import NavigationalObstructionResource

        return NavigationalObstructionResource(self)

    @cached_property
    def notification(self) -> NotificationResource:
        """
        A Notification Service allowing the broadcast of generic messages to the community. Users can send free-form messages, publish lists, and notify the community about events or alerts across various domains. Notifications and alerts are categorized by a 'msgType' field and are accessible via the UDL Secure Messaging API and REST API services.
        """
        from .resources.notification import NotificationResource

        return NotificationResource(self)

    @cached_property
    def object_of_interest(self) -> ObjectOfInterestResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.object_of_interest import ObjectOfInterestResource

        return ObjectOfInterestResource(self)

    @cached_property
    def observations(self) -> ObservationsResource:
        from .resources.observations import ObservationsResource

        return ObservationsResource(self)

    @cached_property
    def onboardnavigation(self) -> OnboardnavigationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.onboardnavigation import OnboardnavigationResource

        return OnboardnavigationResource(self)

    @cached_property
    def onorbit(self) -> OnorbitResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbit import OnorbitResource

        return OnorbitResource(self)

    @cached_property
    def onorbitantenna(self) -> OnorbitantennaResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitantenna import OnorbitantennaResource

        return OnorbitantennaResource(self)

    @cached_property
    def onorbitbattery(self) -> OnorbitbatteryResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitbattery import OnorbitbatteryResource

        return OnorbitbatteryResource(self)

    @cached_property
    def onorbitdetails(self) -> OnorbitdetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitdetails import OnorbitdetailsResource

        return OnorbitdetailsResource(self)

    @cached_property
    def onorbitevent(self) -> OnorbiteventResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitevent import OnorbiteventResource

        return OnorbiteventResource(self)

    @cached_property
    def onorbitlist(self) -> OnorbitlistResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitlist import OnorbitlistResource

        return OnorbitlistResource(self)

    @cached_property
    def onorbitsolararray(self) -> OnorbitsolararrayResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitsolararray import OnorbitsolararrayResource

        return OnorbitsolararrayResource(self)

    @cached_property
    def onorbitthruster(self) -> OnorbitthrusterResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthruster import OnorbitthrusterResource

        return OnorbitthrusterResource(self)

    @cached_property
    def onorbitthrusterstatus(self) -> OnorbitthrusterstatusResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthrusterstatus import OnorbitthrusterstatusResource

        return OnorbitthrusterstatusResource(self)

    @cached_property
    def onorbitassessment(self) -> OnorbitassessmentResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.onorbitassessment import OnorbitassessmentResource

        return OnorbitassessmentResource(self)

    @cached_property
    def operatingunit(self) -> OperatingunitResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunit import OperatingunitResource

        return OperatingunitResource(self)

    @cached_property
    def operatingunitremark(self) -> OperatingunitremarkResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunitremark import OperatingunitremarkResource

        return OperatingunitremarkResource(self)

    @cached_property
    def orbitdetermination(self) -> OrbitdeterminationResource:
        """
        These services provide operations for manipulating and querying Orbit Determination (OD) data. Orbit Determination data contains algorithm results that describe General Perturbations or Special Perturbations orbital updates.
        """
        from .resources.orbitdetermination import OrbitdeterminationResource

        return OrbitdeterminationResource(self)

    @cached_property
    def orbittrack(self) -> OrbittrackResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.orbittrack import OrbittrackResource

        return OrbittrackResource(self)

    @cached_property
    def organization(self) -> OrganizationResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organization import OrganizationResource

        return OrganizationResource(self)

    @cached_property
    def organizationdetails(self) -> OrganizationdetailsResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organizationdetails import OrganizationdetailsResource

        return OrganizationdetailsResource(self)

    @cached_property
    def personnelrecovery(self) -> PersonnelrecoveryResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.personnelrecovery import PersonnelrecoveryResource

        return PersonnelrecoveryResource(self)

    @cached_property
    def poi(self) -> PoiResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.poi import PoiResource

        return PoiResource(self)

    @cached_property
    def port(self) -> PortResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.port import PortResource

        return PortResource(self)

    @cached_property
    def report_and_activities(self) -> ReportAndActivitiesResource:
        from .resources.report_and_activities import ReportAndActivitiesResource

        return ReportAndActivitiesResource(self)

    @cached_property
    def rf_band(self) -> RfBandResource:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band import RfBandResource

        return RfBandResource(self)

    @cached_property
    def rf_band_type(self) -> RfBandTypeResource:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band_type import RfBandTypeResource

        return RfBandTypeResource(self)

    @cached_property
    def rf_emitter(self) -> RfEmitterResource:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_emitter import RfEmitterResource

        return RfEmitterResource(self)

    @cached_property
    def route_stats(self) -> RouteStatsResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.route_stats import RouteStatsResource

        return RouteStatsResource(self)

    @cached_property
    def sar_observation(self) -> SarObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.sar_observation import SarObservationResource

        return SarObservationResource(self)

    @cached_property
    def scientific(self) -> ScientificResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.scientific import ScientificResource

        return ScientificResource(self)

    @cached_property
    def scs(self) -> ScsResource:
        from .resources.scs import ScsResource

        return ScsResource(self)

    @cached_property
    def secure_messaging(self) -> SecureMessagingResource:
        """
        Secure Messaging is based on Apache Kafka which is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. Kafka provides a unified, high-throughput, low-latency platform for handling real-time data feeds.  All messaging is secured; consumers will not receive messages unless authorized to do so. J2000 is the preferred coordinate frame for all observations, but in some cases observations may be in another frame depending on the provider. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.secure_messaging import SecureMessagingResource

        return SecureMessagingResource(self)

    @cached_property
    def sensor(self) -> SensorResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor import SensorResource

        return SensorResource(self)

    @cached_property
    def sensor_stating(self) -> SensorStatingResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_stating import SensorStatingResource

        return SensorStatingResource(self)

    @cached_property
    def sensor_maintenance(self) -> SensorMaintenanceResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_maintenance import SensorMaintenanceResource

        return SensorMaintenanceResource(self)

    @cached_property
    def sensor_observation_type(self) -> SensorObservationTypeResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_observation_type import SensorObservationTypeResource

        return SensorObservationTypeResource(self)

    @cached_property
    def sensor_plan(self) -> SensorPlanResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.sensor_plan import SensorPlanResource

        return SensorPlanResource(self)

    @cached_property
    def sensor_type(self) -> SensorTypeResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_type import SensorTypeResource

        return SensorTypeResource(self)

    @cached_property
    def sera_data_comm_details(self) -> SeraDataCommDetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.sera_data_comm_details import SeraDataCommDetailsResource

        return SeraDataCommDetailsResource(self)

    @cached_property
    def sera_data_early_warning(self) -> SeraDataEarlyWarningResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_early_warning import SeraDataEarlyWarningResource

        return SeraDataEarlyWarningResource(self)

    @cached_property
    def sera_data_navigation(self) -> SeraDataNavigationResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_navigation import SeraDataNavigationResource

        return SeraDataNavigationResource(self)

    @cached_property
    def seradata_optical_payload(self) -> SeradataOpticalPayloadResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_optical_payload import SeradataOpticalPayloadResource

        return SeradataOpticalPayloadResource(self)

    @cached_property
    def seradata_radar_payload(self) -> SeradataRadarPayloadResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_radar_payload import SeradataRadarPayloadResource

        return SeradataRadarPayloadResource(self)

    @cached_property
    def seradata_sigint_payload(self) -> SeradataSigintPayloadResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_sigint_payload import SeradataSigintPayloadResource

        return SeradataSigintPayloadResource(self)

    @cached_property
    def seradata_spacecraft_details(self) -> SeradataSpacecraftDetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.seradata_spacecraft_details import SeradataSpacecraftDetailsResource

        return SeradataSpacecraftDetailsResource(self)

    @cached_property
    def sgi(self) -> SgiResource:
        """
        This service provides operations for manipulation and querying of space weather/solar, geomagnetic, and radiation belt index data.
        """
        from .resources.sgi import SgiResource

        return SgiResource(self)

    @cached_property
    def sigact(self) -> SigactResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.sigact import SigactResource

        return SigactResource(self)

    @cached_property
    def site(self) -> SiteResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site import SiteResource

        return SiteResource(self)

    @cached_property
    def site_remark(self) -> SiteRemarkResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_remark import SiteRemarkResource

        return SiteRemarkResource(self)

    @cached_property
    def site_status(self) -> SiteStatusResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_status import SiteStatusResource

        return SiteStatusResource(self)

    @cached_property
    def sky_imagery(self) -> SkyImageryResource:
        """
        This collection of services provides operations for querying and manipulation of sky imagery data. Sky imagery is ground or space based telescope imagery of RSO's and includes metadata on the image (time, source, etc) as well as binary image content (e.g. FITS, EOSSA, EOCHIP, MP4). Binary content must be downloaded individually by ID using the 'getFile' operation.
        """
        from .resources.sky_imagery import SkyImageryResource

        return SkyImageryResource(self)

    @cached_property
    def soi_observation_set(self) -> SoiObservationSetResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.soi_observation_set import SoiObservationSetResource

        return SoiObservationSetResource(self)

    @cached_property
    def solar_array(self) -> SolarArrayResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array import SolarArrayResource

        return SolarArrayResource(self)

    @cached_property
    def solar_array_details(self) -> SolarArrayDetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array_details import SolarArrayDetailsResource

        return SolarArrayDetailsResource(self)

    @cached_property
    def sortie_ppr(self) -> SortiePprResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.sortie_ppr import SortiePprResource

        return SortiePprResource(self)

    @cached_property
    def space_env_observation(self) -> SpaceEnvObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.space_env_observation import SpaceEnvObservationResource

        return SpaceEnvObservationResource(self)

    @cached_property
    def stage(self) -> StageResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.stage import StageResource

        return StageResource(self)

    @cached_property
    def star_catalog(self) -> StarCatalogResource:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
        from .resources.star_catalog import StarCatalogResource

        return StarCatalogResource(self)

    @cached_property
    def state_vector(self) -> StateVectorResource:
        """
        This service provides operations for querying and manipulation of state vectors for On-orbit objects. State vectors are cartesian vectors of position (r) and velocity (v) that together with their time (epoch) (t) uniquely determine the trajectory of the orbiting body in space. J2000 is the preferred coordinate frame for all state vector positions/velocities in UDL, but in some cases data may be in another frame depending on the provider and/or datatype. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.state_vector import StateVectorResource

        return StateVectorResource(self)

    @cached_property
    def status(self) -> StatusResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.status import StatusResource

        return StatusResource(self)

    @cached_property
    def substatus(self) -> SubstatusResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.substatus import SubstatusResource

        return SubstatusResource(self)

    @cached_property
    def supporting_data(self) -> SupportingDataResource:
        from .resources.supporting_data import SupportingDataResource

        return SupportingDataResource(self)

    @cached_property
    def surface(self) -> SurfaceResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface import SurfaceResource

        return SurfaceResource(self)

    @cached_property
    def surface_obstruction(self) -> SurfaceObstructionResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface_obstruction import SurfaceObstructionResource

        return SurfaceObstructionResource(self)

    @cached_property
    def swir(self) -> SwirResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.swir import SwirResource

        return SwirResource(self)

    @cached_property
    def tai_utc(self) -> TaiUtcResource:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.tai_utc import TaiUtcResource

        return TaiUtcResource(self)

    @cached_property
    def tdoa_fdoa(self) -> TdoaFdoaResource:
        from .resources.tdoa_fdoa import TdoaFdoaResource

        return TdoaFdoaResource(self)

    @cached_property
    def track(self) -> TrackResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track import TrackResource

        return TrackResource(self)

    @cached_property
    def track_details(self) -> TrackDetailsResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track_details import TrackDetailsResource

        return TrackDetailsResource(self)

    @cached_property
    def track_route(self) -> TrackRouteResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.track_route import TrackRouteResource

        return TrackRouteResource(self)

    @cached_property
    def transponder(self) -> TransponderResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.transponder import TransponderResource

        return TransponderResource(self)

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def vessel(self) -> VesselResource:
        """
        This service provides operations for manipulation and querying of maritime Vessel and Vessel Status data. Vessel contains the static data of the specific vessel: mmsi, cruise speed, max speed, etc.
        """
        from .resources.vessel import VesselResource

        return VesselResource(self)

    @cached_property
    def video(self) -> VideoResource:
        """This collection of services provides operations for video streaming."""
        from .resources.video import VideoResource

        return VideoResource(self)

    @cached_property
    def weather_data(self) -> WeatherDataResource:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_data import WeatherDataResource

        return WeatherDataResource(self)

    @cached_property
    def weather_report(self) -> WeatherReportResource:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
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
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_events import AsyncAirEventsResource

        return AsyncAirEventsResource(self)

    @cached_property
    def air_operations(self) -> AsyncAirOperationsResource:
        from .resources.air_operations import AsyncAirOperationsResource

        return AsyncAirOperationsResource(self)

    @cached_property
    def air_transport_missions(self) -> AsyncAirTransportMissionsResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_transport_missions import AsyncAirTransportMissionsResource

        return AsyncAirTransportMissionsResource(self)

    @cached_property
    def aircraft(self) -> AsyncAircraftResource:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft import AsyncAircraftResource

        return AsyncAircraftResource(self)

    @cached_property
    def aircraft_sorties(self) -> AsyncAircraftSortiesResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aircraft_sorties import AsyncAircraftSortiesResource

        return AsyncAircraftSortiesResource(self)

    @cached_property
    def aircraft_status_remarks(self) -> AsyncAircraftStatusRemarksResource:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_status_remarks import AsyncAircraftStatusRemarksResource

        return AsyncAircraftStatusRemarksResource(self)

    @cached_property
    def aircraft_statuses(self) -> AsyncAircraftStatusesResource:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_statuses import AsyncAircraftStatusesResource

        return AsyncAircraftStatusesResource(self)

    @cached_property
    def airfield_slot_consumptions(self) -> AsyncAirfieldSlotConsumptionsResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slot_consumptions import AsyncAirfieldSlotConsumptionsResource

        return AsyncAirfieldSlotConsumptionsResource(self)

    @cached_property
    def airfield_slots(self) -> AsyncAirfieldSlotsResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slots import AsyncAirfieldSlotsResource

        return AsyncAirfieldSlotsResource(self)

    @cached_property
    def airfield_status(self) -> AsyncAirfieldStatusResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_status import AsyncAirfieldStatusResource

        return AsyncAirfieldStatusResource(self)

    @cached_property
    def airfields(self) -> AsyncAirfieldsResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfields import AsyncAirfieldsResource

        return AsyncAirfieldsResource(self)

    @cached_property
    def airload_plans(self) -> AsyncAirloadPlansResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airload_plans import AsyncAirloadPlansResource

        return AsyncAirloadPlansResource(self)

    @cached_property
    def airspace_control_orders(self) -> AsyncAirspaceControlOrdersResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airspace_control_orders import AsyncAirspaceControlOrdersResource

        return AsyncAirspaceControlOrdersResource(self)

    @cached_property
    def ais(self) -> AsyncAIsResource:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais import AsyncAIsResource

        return AsyncAIsResource(self)

    @cached_property
    def ais_objects(self) -> AsyncAIsObjectsResource:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais_objects import AsyncAIsObjectsResource

        return AsyncAIsObjectsResource(self)

    @cached_property
    def analytic_imagery(self) -> AsyncAnalyticImageryResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.analytic_imagery import AsyncAnalyticImageryResource

        return AsyncAnalyticImageryResource(self)

    @cached_property
    def antennas(self) -> AsyncAntennasResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.antennas import AsyncAntennasResource

        return AsyncAntennasResource(self)

    @cached_property
    def attitude_data(self) -> AsyncAttitudeDataResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_data import AsyncAttitudeDataResource

        return AsyncAttitudeDataResource(self)

    @cached_property
    def attitude_sets(self) -> AsyncAttitudeSetsResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_sets import AsyncAttitudeSetsResource

        return AsyncAttitudeSetsResource(self)

    @cached_property
    def aviation_risk_management(self) -> AsyncAviationRiskManagementResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aviation_risk_management import AsyncAviationRiskManagementResource

        return AsyncAviationRiskManagementResource(self)

    @cached_property
    def batteries(self) -> AsyncBatteriesResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batteries import AsyncBatteriesResource

        return AsyncBatteriesResource(self)

    @cached_property
    def batterydetails(self) -> AsyncBatterydetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batterydetails import AsyncBatterydetailsResource

        return AsyncBatterydetailsResource(self)

    @cached_property
    def beam(self) -> AsyncBeamResource:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam import AsyncBeamResource

        return AsyncBeamResource(self)

    @cached_property
    def beam_contours(self) -> AsyncBeamContoursResource:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam_contours import AsyncBeamContoursResource

        return AsyncBeamContoursResource(self)

    @cached_property
    def buses(self) -> AsyncBusesResource:
        """Services for querying and manipulation of satellite buses.

        A bus is the physical and software infrastructure backbone to which on-orbit satellite payloads are attached for power, control, and other support functions.
        """
        from .resources.buses import AsyncBusesResource

        return AsyncBusesResource(self)

    @cached_property
    def channels(self) -> AsyncChannelsResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.channels import AsyncChannelsResource

        return AsyncChannelsResource(self)

    @cached_property
    def closelyspacedobjects(self) -> AsyncCloselyspacedobjectsResource:
        """
        This collection of services provides operations for manipulating and querying of closely spaced objects (on orbit) operations including docking, rendezvous, proximity and reporting of payload zone engagements observed and characterized over a period of time.
        """
        from .resources.closelyspacedobjects import AsyncCloselyspacedobjectsResource

        return AsyncCloselyspacedobjectsResource(self)

    @cached_property
    def collect_requests(self) -> AsyncCollectRequestsResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_requests import AsyncCollectRequestsResource

        return AsyncCollectRequestsResource(self)

    @cached_property
    def collect_responses(self) -> AsyncCollectResponsesResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_responses import AsyncCollectResponsesResource

        return AsyncCollectResponsesResource(self)

    @cached_property
    def comm(self) -> AsyncCommResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.comm import AsyncCommResource

        return AsyncCommResource(self)

    @cached_property
    def conjunctions(self) -> AsyncConjunctionsResource:
        """
        These services provide operations for manipulation and querying of conjunctions.
        """
        from .resources.conjunctions import AsyncConjunctionsResource

        return AsyncConjunctionsResource(self)

    @cached_property
    def cots(self) -> AsyncCotsResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.cots import AsyncCotsResource

        return AsyncCotsResource(self)

    @cached_property
    def countries(self) -> AsyncCountriesResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.countries import AsyncCountriesResource

        return AsyncCountriesResource(self)

    @cached_property
    def crew(self) -> AsyncCrewResource:
        """These services provide operations for posting and querying crew data.

        Crew data contains information about its members and their assignments.
        """
        from .resources.crew import AsyncCrewResource

        return AsyncCrewResource(self)

    @cached_property
    def deconflictset(self) -> AsyncDeconflictsetResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.deconflictset import AsyncDeconflictsetResource

        return AsyncDeconflictsetResource(self)

    @cached_property
    def diff_of_arrival(self) -> AsyncDiffOfArrivalResource:
        """
        These services provide operations for querying and manipulation of Signal time and frequency difference of arrival (TDOA/FDOA) information obtained by using passive RF based sensor phenomenologies and sensor triangulation. The J2000 coordinate frame is the preferred frame for all observations, but in some cases observations may be in another frame depending on the provider.
        """
        from .resources.diff_of_arrival import AsyncDiffOfArrivalResource

        return AsyncDiffOfArrivalResource(self)

    @cached_property
    def diplomatic_clearance(self) -> AsyncDiplomaticClearanceResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.diplomatic_clearance import AsyncDiplomaticClearanceResource

        return AsyncDiplomaticClearanceResource(self)

    @cached_property
    def drift_history(self) -> AsyncDriftHistoryResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.drift_history import AsyncDriftHistoryResource

        return AsyncDriftHistoryResource(self)

    @cached_property
    def dropzone(self) -> AsyncDropzoneResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.dropzone import AsyncDropzoneResource

        return AsyncDropzoneResource(self)

    @cached_property
    def ecpedr(self) -> AsyncEcpedrResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.ecpedr import AsyncEcpedrResource

        return AsyncEcpedrResource(self)

    @cached_property
    def effect_requests(self) -> AsyncEffectRequestsResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_requests import AsyncEffectRequestsResource

        return AsyncEffectRequestsResource(self)

    @cached_property
    def effect_responses(self) -> AsyncEffectResponsesResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_responses import AsyncEffectResponsesResource

        return AsyncEffectResponsesResource(self)

    @cached_property
    def elsets(self) -> AsyncElsetsResource:
        """
        These services provide operations for querying and manipulation of element set data describing orbital characteristics of on-orbit objects. An element set is a collection of parameters that are used, along with an orbit propagator, to predict the motion of a satellite. The element set, or elset for short, consists of identification data, the classical elements and drag parameters.
        """
        from .resources.elsets import AsyncElsetsResource

        return AsyncElsetsResource(self)

    @cached_property
    def emireport(self) -> AsyncEmireportResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emireport import AsyncEmireportResource

        return AsyncEmireportResource(self)

    @cached_property
    def emitter_geolocation(self) -> AsyncEmitterGeolocationResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emitter_geolocation import AsyncEmitterGeolocationResource

        return AsyncEmitterGeolocationResource(self)

    @cached_property
    def engine_details(self) -> AsyncEngineDetailsResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engine_details import AsyncEngineDetailsResource

        return AsyncEngineDetailsResource(self)

    @cached_property
    def engines(self) -> AsyncEnginesResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engines import AsyncEnginesResource

        return AsyncEnginesResource(self)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.entities import AsyncEntitiesResource

        return AsyncEntitiesResource(self)

    @cached_property
    def eop(self) -> AsyncEopResource:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.eop import AsyncEopResource

        return AsyncEopResource(self)

    @cached_property
    def ephemeris(self) -> AsyncEphemerisResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris import AsyncEphemerisResource

        return AsyncEphemerisResource(self)

    @cached_property
    def ephemeris_sets(self) -> AsyncEphemerisSetsResource:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris_sets import AsyncEphemerisSetsResource

        return AsyncEphemerisSetsResource(self)

    @cached_property
    def equipment(self) -> AsyncEquipmentResource:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment import AsyncEquipmentResource

        return AsyncEquipmentResource(self)

    @cached_property
    def equipment_remarks(self) -> AsyncEquipmentRemarksResource:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment_remarks import AsyncEquipmentRemarksResource

        return AsyncEquipmentRemarksResource(self)

    @cached_property
    def evac(self) -> AsyncEvacResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.evac import AsyncEvacResource

        return AsyncEvacResource(self)

    @cached_property
    def event_evolution(self) -> AsyncEventEvolutionResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.event_evolution import AsyncEventEvolutionResource

        return AsyncEventEvolutionResource(self)

    @cached_property
    def feature_assessment(self) -> AsyncFeatureAssessmentResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.feature_assessment import AsyncFeatureAssessmentResource

        return AsyncFeatureAssessmentResource(self)

    @cached_property
    def flightplan(self) -> AsyncFlightplanResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.flightplan import AsyncFlightplanResource

        return AsyncFlightplanResource(self)

    @cached_property
    def geo_status(self) -> AsyncGeoStatusResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.geo_status import AsyncGeoStatusResource

        return AsyncGeoStatusResource(self)

    @cached_property
    def global_atmospheric_model(self) -> AsyncGlobalAtmosphericModelResource:
        """
        Models and Simulations is a collection of services that allow consumers to interact with data products representing independent models of various phenomenon, artificial intelligence models and predictions, or of mathematical parameters meant to feed mod and sim tools to produce estimates of environmental entities such as atmospheric models and heat maps.
        """
        from .resources.global_atmospheric_model import AsyncGlobalAtmosphericModelResource

        return AsyncGlobalAtmosphericModelResource(self)

    @cached_property
    def gnss_observations(self) -> AsyncGnssObservationsResource:
        from .resources.gnss_observations import AsyncGnssObservationsResource

        return AsyncGnssObservationsResource(self)

    @cached_property
    def gnss_observationset(self) -> AsyncGnssObservationsetResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_observationset import AsyncGnssObservationsetResource

        return AsyncGnssObservationsetResource(self)

    @cached_property
    def gnss_raw_if(self) -> AsyncGnssRawIfResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_raw_if import AsyncGnssRawIfResource

        return AsyncGnssRawIfResource(self)

    @cached_property
    def ground_imagery(self) -> AsyncGroundImageryResource:
        """
        This collection of services provides operations for querying and manipulation of ground imagery of terrestrial regions from on-orbit, air, and other sensors. Includes metadata on the image (time, region, source, etc) as well as binary content (typically GeoTIFF). Binary content must be downloaded individually by ID using the 'getFile' operation. Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.ground_imagery import AsyncGroundImageryResource

        return AsyncGroundImageryResource(self)

    @cached_property
    def h3_geo(self) -> AsyncH3GeoResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo import AsyncH3GeoResource

        return AsyncH3GeoResource(self)

    @cached_property
    def h3_geo_hex_cell(self) -> AsyncH3GeoHexCellResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo_hex_cell import AsyncH3GeoHexCellResource

        return AsyncH3GeoHexCellResource(self)

    @cached_property
    def hazard(self) -> AsyncHazardResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.hazard import AsyncHazardResource

        return AsyncHazardResource(self)

    @cached_property
    def iono_observations(self) -> AsyncIonoObservationsResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.iono_observations import AsyncIonoObservationsResource

        return AsyncIonoObservationsResource(self)

    @cached_property
    def ir(self) -> AsyncIrResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.ir import AsyncIrResource

        return AsyncIrResource(self)

    @cached_property
    def isr_collections(self) -> AsyncIsrCollectionsResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.isr_collections import AsyncIsrCollectionsResource

        return AsyncIsrCollectionsResource(self)

    @cached_property
    def item(self) -> AsyncItemResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item import AsyncItemResource

        return AsyncItemResource(self)

    @cached_property
    def item_trackings(self) -> AsyncItemTrackingsResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item_trackings import AsyncItemTrackingsResource

        return AsyncItemTrackingsResource(self)

    @cached_property
    def laserdeconflictrequest(self) -> AsyncLaserdeconflictrequestResource:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laserdeconflictrequest import AsyncLaserdeconflictrequestResource

        return AsyncLaserdeconflictrequestResource(self)

    @cached_property
    def laseremitter(self) -> AsyncLaseremitterResource:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laseremitter import AsyncLaseremitterResource

        return AsyncLaseremitterResource(self)

    @cached_property
    def launch_detection(self) -> AsyncLaunchDetectionResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_detection import AsyncLaunchDetectionResource

        return AsyncLaunchDetectionResource(self)

    @cached_property
    def launch_event(self) -> AsyncLaunchEventResource:
        """
        These services provide operations for manipulation and querying of LaunchEvent data. Launch Event data are known space launches, either future or historic records containing items such as the launch site, launch epoch, and object.
        """
        from .resources.launch_event import AsyncLaunchEventResource

        return AsyncLaunchEventResource(self)

    @cached_property
    def launch_site(self) -> AsyncLaunchSiteResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site import AsyncLaunchSiteResource

        return AsyncLaunchSiteResource(self)

    @cached_property
    def launch_site_details(self) -> AsyncLaunchSiteDetailsResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site_details import AsyncLaunchSiteDetailsResource

        return AsyncLaunchSiteDetailsResource(self)

    @cached_property
    def launch_vehicle(self) -> AsyncLaunchVehicleResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle import AsyncLaunchVehicleResource

        return AsyncLaunchVehicleResource(self)

    @cached_property
    def launch_vehicle_details(self) -> AsyncLaunchVehicleDetailsResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle_details import AsyncLaunchVehicleDetailsResource

        return AsyncLaunchVehicleDetailsResource(self)

    @cached_property
    def link_status(self) -> AsyncLinkStatusResource:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.link_status import AsyncLinkStatusResource

        return AsyncLinkStatusResource(self)

    @cached_property
    def linkstatus(self) -> AsyncLinkstatusResource:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.linkstatus import AsyncLinkstatusResource

        return AsyncLinkstatusResource(self)

    @cached_property
    def location(self) -> AsyncLocationResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.location import AsyncLocationResource

        return AsyncLocationResource(self)

    @cached_property
    def logistics_support(self) -> AsyncLogisticsSupportResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.logistics_support import AsyncLogisticsSupportResource

        return AsyncLogisticsSupportResource(self)

    @cached_property
    def maneuvers(self) -> AsyncManeuversResource:
        """
        This service provides operations for querying and manipulation of detected/possible/confirmed on-orbit maneuvers. The J2000 coordinate frame is the preferred frame for all maneuver data, but in some cases data may be in another frame depending on the provider. Check the Storefront 'Data Products' section under the 'Discover' tab for maneuver data provider information.
        """
        from .resources.maneuvers import AsyncManeuversResource

        return AsyncManeuversResource(self)

    @cached_property
    def manifold(self) -> AsyncManifoldResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifold import AsyncManifoldResource

        return AsyncManifoldResource(self)

    @cached_property
    def manifoldelset(self) -> AsyncManifoldelsetResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifoldelset import AsyncManifoldelsetResource

        return AsyncManifoldelsetResource(self)

    @cached_property
    def missile_tracks(self) -> AsyncMissileTracksResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.missile_tracks import AsyncMissileTracksResource

        return AsyncMissileTracksResource(self)

    @cached_property
    def mission_assignment(self) -> AsyncMissionAssignmentResource:
        """
        These services provide operations for manipulation and querying of mission assignment objects. MissionAssignment is used by C2 JUs and, optionally, non-C2 JUs to assign missions, designate targets, and provide target information to non-C2 JU platforms. Provision is made for the non-C2 JU platforms to acknowledge the message through receipt/compliance action.
        """
        from .resources.mission_assignment import AsyncMissionAssignmentResource

        return AsyncMissionAssignmentResource(self)

    @cached_property
    def mti(self) -> AsyncMtiResource:
        """
        These services provide operations for posting and querying Moving Target Indicator (MTI) STANAG 4607 data. Detailed MTI data supports activities such as targeting or less detailed data for applications such as situational awareness used/derived by exploitation systems.
        """
        from .resources.mti import AsyncMtiResource

        return AsyncMtiResource(self)

    @cached_property
    def navigation(self) -> AsyncNavigationResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.navigation import AsyncNavigationResource

        return AsyncNavigationResource(self)

    @cached_property
    def navigational_obstruction(self) -> AsyncNavigationalObstructionResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.navigational_obstruction import AsyncNavigationalObstructionResource

        return AsyncNavigationalObstructionResource(self)

    @cached_property
    def notification(self) -> AsyncNotificationResource:
        """
        A Notification Service allowing the broadcast of generic messages to the community. Users can send free-form messages, publish lists, and notify the community about events or alerts across various domains. Notifications and alerts are categorized by a 'msgType' field and are accessible via the UDL Secure Messaging API and REST API services.
        """
        from .resources.notification import AsyncNotificationResource

        return AsyncNotificationResource(self)

    @cached_property
    def object_of_interest(self) -> AsyncObjectOfInterestResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.object_of_interest import AsyncObjectOfInterestResource

        return AsyncObjectOfInterestResource(self)

    @cached_property
    def observations(self) -> AsyncObservationsResource:
        from .resources.observations import AsyncObservationsResource

        return AsyncObservationsResource(self)

    @cached_property
    def onboardnavigation(self) -> AsyncOnboardnavigationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.onboardnavigation import AsyncOnboardnavigationResource

        return AsyncOnboardnavigationResource(self)

    @cached_property
    def onorbit(self) -> AsyncOnorbitResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbit import AsyncOnorbitResource

        return AsyncOnorbitResource(self)

    @cached_property
    def onorbitantenna(self) -> AsyncOnorbitantennaResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitantenna import AsyncOnorbitantennaResource

        return AsyncOnorbitantennaResource(self)

    @cached_property
    def onorbitbattery(self) -> AsyncOnorbitbatteryResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitbattery import AsyncOnorbitbatteryResource

        return AsyncOnorbitbatteryResource(self)

    @cached_property
    def onorbitdetails(self) -> AsyncOnorbitdetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitdetails import AsyncOnorbitdetailsResource

        return AsyncOnorbitdetailsResource(self)

    @cached_property
    def onorbitevent(self) -> AsyncOnorbiteventResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitevent import AsyncOnorbiteventResource

        return AsyncOnorbiteventResource(self)

    @cached_property
    def onorbitlist(self) -> AsyncOnorbitlistResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitlist import AsyncOnorbitlistResource

        return AsyncOnorbitlistResource(self)

    @cached_property
    def onorbitsolararray(self) -> AsyncOnorbitsolararrayResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitsolararray import AsyncOnorbitsolararrayResource

        return AsyncOnorbitsolararrayResource(self)

    @cached_property
    def onorbitthruster(self) -> AsyncOnorbitthrusterResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthruster import AsyncOnorbitthrusterResource

        return AsyncOnorbitthrusterResource(self)

    @cached_property
    def onorbitthrusterstatus(self) -> AsyncOnorbitthrusterstatusResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthrusterstatus import AsyncOnorbitthrusterstatusResource

        return AsyncOnorbitthrusterstatusResource(self)

    @cached_property
    def onorbitassessment(self) -> AsyncOnorbitassessmentResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.onorbitassessment import AsyncOnorbitassessmentResource

        return AsyncOnorbitassessmentResource(self)

    @cached_property
    def operatingunit(self) -> AsyncOperatingunitResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunit import AsyncOperatingunitResource

        return AsyncOperatingunitResource(self)

    @cached_property
    def operatingunitremark(self) -> AsyncOperatingunitremarkResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunitremark import AsyncOperatingunitremarkResource

        return AsyncOperatingunitremarkResource(self)

    @cached_property
    def orbitdetermination(self) -> AsyncOrbitdeterminationResource:
        """
        These services provide operations for manipulating and querying Orbit Determination (OD) data. Orbit Determination data contains algorithm results that describe General Perturbations or Special Perturbations orbital updates.
        """
        from .resources.orbitdetermination import AsyncOrbitdeterminationResource

        return AsyncOrbitdeterminationResource(self)

    @cached_property
    def orbittrack(self) -> AsyncOrbittrackResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.orbittrack import AsyncOrbittrackResource

        return AsyncOrbittrackResource(self)

    @cached_property
    def organization(self) -> AsyncOrganizationResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organization import AsyncOrganizationResource

        return AsyncOrganizationResource(self)

    @cached_property
    def organizationdetails(self) -> AsyncOrganizationdetailsResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organizationdetails import AsyncOrganizationdetailsResource

        return AsyncOrganizationdetailsResource(self)

    @cached_property
    def personnelrecovery(self) -> AsyncPersonnelrecoveryResource:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.personnelrecovery import AsyncPersonnelrecoveryResource

        return AsyncPersonnelrecoveryResource(self)

    @cached_property
    def poi(self) -> AsyncPoiResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.poi import AsyncPoiResource

        return AsyncPoiResource(self)

    @cached_property
    def port(self) -> AsyncPortResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.port import AsyncPortResource

        return AsyncPortResource(self)

    @cached_property
    def report_and_activities(self) -> AsyncReportAndActivitiesResource:
        from .resources.report_and_activities import AsyncReportAndActivitiesResource

        return AsyncReportAndActivitiesResource(self)

    @cached_property
    def rf_band(self) -> AsyncRfBandResource:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band import AsyncRfBandResource

        return AsyncRfBandResource(self)

    @cached_property
    def rf_band_type(self) -> AsyncRfBandTypeResource:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band_type import AsyncRfBandTypeResource

        return AsyncRfBandTypeResource(self)

    @cached_property
    def rf_emitter(self) -> AsyncRfEmitterResource:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_emitter import AsyncRfEmitterResource

        return AsyncRfEmitterResource(self)

    @cached_property
    def route_stats(self) -> AsyncRouteStatsResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.route_stats import AsyncRouteStatsResource

        return AsyncRouteStatsResource(self)

    @cached_property
    def sar_observation(self) -> AsyncSarObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.sar_observation import AsyncSarObservationResource

        return AsyncSarObservationResource(self)

    @cached_property
    def scientific(self) -> AsyncScientificResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.scientific import AsyncScientificResource

        return AsyncScientificResource(self)

    @cached_property
    def scs(self) -> AsyncScsResource:
        from .resources.scs import AsyncScsResource

        return AsyncScsResource(self)

    @cached_property
    def secure_messaging(self) -> AsyncSecureMessagingResource:
        """
        Secure Messaging is based on Apache Kafka which is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. Kafka provides a unified, high-throughput, low-latency platform for handling real-time data feeds.  All messaging is secured; consumers will not receive messages unless authorized to do so. J2000 is the preferred coordinate frame for all observations, but in some cases observations may be in another frame depending on the provider. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.secure_messaging import AsyncSecureMessagingResource

        return AsyncSecureMessagingResource(self)

    @cached_property
    def sensor(self) -> AsyncSensorResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor import AsyncSensorResource

        return AsyncSensorResource(self)

    @cached_property
    def sensor_stating(self) -> AsyncSensorStatingResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_stating import AsyncSensorStatingResource

        return AsyncSensorStatingResource(self)

    @cached_property
    def sensor_maintenance(self) -> AsyncSensorMaintenanceResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_maintenance import AsyncSensorMaintenanceResource

        return AsyncSensorMaintenanceResource(self)

    @cached_property
    def sensor_observation_type(self) -> AsyncSensorObservationTypeResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_observation_type import AsyncSensorObservationTypeResource

        return AsyncSensorObservationTypeResource(self)

    @cached_property
    def sensor_plan(self) -> AsyncSensorPlanResource:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.sensor_plan import AsyncSensorPlanResource

        return AsyncSensorPlanResource(self)

    @cached_property
    def sensor_type(self) -> AsyncSensorTypeResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_type import AsyncSensorTypeResource

        return AsyncSensorTypeResource(self)

    @cached_property
    def sera_data_comm_details(self) -> AsyncSeraDataCommDetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.sera_data_comm_details import AsyncSeraDataCommDetailsResource

        return AsyncSeraDataCommDetailsResource(self)

    @cached_property
    def sera_data_early_warning(self) -> AsyncSeraDataEarlyWarningResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_early_warning import AsyncSeraDataEarlyWarningResource

        return AsyncSeraDataEarlyWarningResource(self)

    @cached_property
    def sera_data_navigation(self) -> AsyncSeraDataNavigationResource:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_navigation import AsyncSeraDataNavigationResource

        return AsyncSeraDataNavigationResource(self)

    @cached_property
    def seradata_optical_payload(self) -> AsyncSeradataOpticalPayloadResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_optical_payload import AsyncSeradataOpticalPayloadResource

        return AsyncSeradataOpticalPayloadResource(self)

    @cached_property
    def seradata_radar_payload(self) -> AsyncSeradataRadarPayloadResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_radar_payload import AsyncSeradataRadarPayloadResource

        return AsyncSeradataRadarPayloadResource(self)

    @cached_property
    def seradata_sigint_payload(self) -> AsyncSeradataSigintPayloadResource:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_sigint_payload import AsyncSeradataSigintPayloadResource

        return AsyncSeradataSigintPayloadResource(self)

    @cached_property
    def seradata_spacecraft_details(self) -> AsyncSeradataSpacecraftDetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.seradata_spacecraft_details import AsyncSeradataSpacecraftDetailsResource

        return AsyncSeradataSpacecraftDetailsResource(self)

    @cached_property
    def sgi(self) -> AsyncSgiResource:
        """
        This service provides operations for manipulation and querying of space weather/solar, geomagnetic, and radiation belt index data.
        """
        from .resources.sgi import AsyncSgiResource

        return AsyncSgiResource(self)

    @cached_property
    def sigact(self) -> AsyncSigactResource:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.sigact import AsyncSigactResource

        return AsyncSigactResource(self)

    @cached_property
    def site(self) -> AsyncSiteResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site import AsyncSiteResource

        return AsyncSiteResource(self)

    @cached_property
    def site_remark(self) -> AsyncSiteRemarkResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_remark import AsyncSiteRemarkResource

        return AsyncSiteRemarkResource(self)

    @cached_property
    def site_status(self) -> AsyncSiteStatusResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_status import AsyncSiteStatusResource

        return AsyncSiteStatusResource(self)

    @cached_property
    def sky_imagery(self) -> AsyncSkyImageryResource:
        """
        This collection of services provides operations for querying and manipulation of sky imagery data. Sky imagery is ground or space based telescope imagery of RSO's and includes metadata on the image (time, source, etc) as well as binary image content (e.g. FITS, EOSSA, EOCHIP, MP4). Binary content must be downloaded individually by ID using the 'getFile' operation.
        """
        from .resources.sky_imagery import AsyncSkyImageryResource

        return AsyncSkyImageryResource(self)

    @cached_property
    def soi_observation_set(self) -> AsyncSoiObservationSetResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.soi_observation_set import AsyncSoiObservationSetResource

        return AsyncSoiObservationSetResource(self)

    @cached_property
    def solar_array(self) -> AsyncSolarArrayResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array import AsyncSolarArrayResource

        return AsyncSolarArrayResource(self)

    @cached_property
    def solar_array_details(self) -> AsyncSolarArrayDetailsResource:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array_details import AsyncSolarArrayDetailsResource

        return AsyncSolarArrayDetailsResource(self)

    @cached_property
    def sortie_ppr(self) -> AsyncSortiePprResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.sortie_ppr import AsyncSortiePprResource

        return AsyncSortiePprResource(self)

    @cached_property
    def space_env_observation(self) -> AsyncSpaceEnvObservationResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.space_env_observation import AsyncSpaceEnvObservationResource

        return AsyncSpaceEnvObservationResource(self)

    @cached_property
    def stage(self) -> AsyncStageResource:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.stage import AsyncStageResource

        return AsyncStageResource(self)

    @cached_property
    def star_catalog(self) -> AsyncStarCatalogResource:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
        from .resources.star_catalog import AsyncStarCatalogResource

        return AsyncStarCatalogResource(self)

    @cached_property
    def state_vector(self) -> AsyncStateVectorResource:
        """
        This service provides operations for querying and manipulation of state vectors for On-orbit objects. State vectors are cartesian vectors of position (r) and velocity (v) that together with their time (epoch) (t) uniquely determine the trajectory of the orbiting body in space. J2000 is the preferred coordinate frame for all state vector positions/velocities in UDL, but in some cases data may be in another frame depending on the provider and/or datatype. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.state_vector import AsyncStateVectorResource

        return AsyncStateVectorResource(self)

    @cached_property
    def status(self) -> AsyncStatusResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.status import AsyncStatusResource

        return AsyncStatusResource(self)

    @cached_property
    def substatus(self) -> AsyncSubstatusResource:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.substatus import AsyncSubstatusResource

        return AsyncSubstatusResource(self)

    @cached_property
    def supporting_data(self) -> AsyncSupportingDataResource:
        from .resources.supporting_data import AsyncSupportingDataResource

        return AsyncSupportingDataResource(self)

    @cached_property
    def surface(self) -> AsyncSurfaceResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface import AsyncSurfaceResource

        return AsyncSurfaceResource(self)

    @cached_property
    def surface_obstruction(self) -> AsyncSurfaceObstructionResource:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface_obstruction import AsyncSurfaceObstructionResource

        return AsyncSurfaceObstructionResource(self)

    @cached_property
    def swir(self) -> AsyncSwirResource:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.swir import AsyncSwirResource

        return AsyncSwirResource(self)

    @cached_property
    def tai_utc(self) -> AsyncTaiUtcResource:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.tai_utc import AsyncTaiUtcResource

        return AsyncTaiUtcResource(self)

    @cached_property
    def tdoa_fdoa(self) -> AsyncTdoaFdoaResource:
        from .resources.tdoa_fdoa import AsyncTdoaFdoaResource

        return AsyncTdoaFdoaResource(self)

    @cached_property
    def track(self) -> AsyncTrackResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track import AsyncTrackResource

        return AsyncTrackResource(self)

    @cached_property
    def track_details(self) -> AsyncTrackDetailsResource:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track_details import AsyncTrackDetailsResource

        return AsyncTrackDetailsResource(self)

    @cached_property
    def track_route(self) -> AsyncTrackRouteResource:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.track_route import AsyncTrackRouteResource

        return AsyncTrackRouteResource(self)

    @cached_property
    def transponder(self) -> AsyncTransponderResource:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.transponder import AsyncTransponderResource

        return AsyncTransponderResource(self)

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def vessel(self) -> AsyncVesselResource:
        """
        This service provides operations for manipulation and querying of maritime Vessel and Vessel Status data. Vessel contains the static data of the specific vessel: mmsi, cruise speed, max speed, etc.
        """
        from .resources.vessel import AsyncVesselResource

        return AsyncVesselResource(self)

    @cached_property
    def video(self) -> AsyncVideoResource:
        """This collection of services provides operations for video streaming."""
        from .resources.video import AsyncVideoResource

        return AsyncVideoResource(self)

    @cached_property
    def weather_data(self) -> AsyncWeatherDataResource:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_data import AsyncWeatherDataResource

        return AsyncWeatherDataResource(self)

    @cached_property
    def weather_report(self) -> AsyncWeatherReportResource:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
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
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_events import AirEventsResourceWithRawResponse

        return AirEventsResourceWithRawResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AirOperationsResourceWithRawResponse:
        from .resources.air_operations import AirOperationsResourceWithRawResponse

        return AirOperationsResourceWithRawResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AirTransportMissionsResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_transport_missions import AirTransportMissionsResourceWithRawResponse

        return AirTransportMissionsResourceWithRawResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AircraftResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft import AircraftResourceWithRawResponse

        return AircraftResourceWithRawResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AircraftSortiesResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aircraft_sorties import AircraftSortiesResourceWithRawResponse

        return AircraftSortiesResourceWithRawResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(self) -> aircraft_status_remarks.AircraftStatusRemarksResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_status_remarks import AircraftStatusRemarksResourceWithRawResponse

        return AircraftStatusRemarksResourceWithRawResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AircraftStatusesResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_statuses import AircraftStatusesResourceWithRawResponse

        return AircraftStatusesResourceWithRawResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(self) -> airfield_slot_consumptions.AirfieldSlotConsumptionsResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slot_consumptions import AirfieldSlotConsumptionsResourceWithRawResponse

        return AirfieldSlotConsumptionsResourceWithRawResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AirfieldSlotsResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slots import AirfieldSlotsResourceWithRawResponse

        return AirfieldSlotsResourceWithRawResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AirfieldStatusResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_status import AirfieldStatusResourceWithRawResponse

        return AirfieldStatusResourceWithRawResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AirfieldsResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfields import AirfieldsResourceWithRawResponse

        return AirfieldsResourceWithRawResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AirloadPlansResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airload_plans import AirloadPlansResourceWithRawResponse

        return AirloadPlansResourceWithRawResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(self) -> airspace_control_orders.AirspaceControlOrdersResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airspace_control_orders import AirspaceControlOrdersResourceWithRawResponse

        return AirspaceControlOrdersResourceWithRawResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AIsResourceWithRawResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais import AIsResourceWithRawResponse

        return AIsResourceWithRawResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AIsObjectsResourceWithRawResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais_objects import AIsObjectsResourceWithRawResponse

        return AIsObjectsResourceWithRawResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AnalyticImageryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.analytic_imagery import AnalyticImageryResourceWithRawResponse

        return AnalyticImageryResourceWithRawResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AntennasResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.antennas import AntennasResourceWithRawResponse

        return AntennasResourceWithRawResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AttitudeDataResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_data import AttitudeDataResourceWithRawResponse

        return AttitudeDataResourceWithRawResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AttitudeSetsResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_sets import AttitudeSetsResourceWithRawResponse

        return AttitudeSetsResourceWithRawResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(self) -> aviation_risk_management.AviationRiskManagementResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aviation_risk_management import AviationRiskManagementResourceWithRawResponse

        return AviationRiskManagementResourceWithRawResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.BatteriesResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batteries import BatteriesResourceWithRawResponse

        return BatteriesResourceWithRawResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.BatterydetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batterydetails import BatterydetailsResourceWithRawResponse

        return BatterydetailsResourceWithRawResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.BeamResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam import BeamResourceWithRawResponse

        return BeamResourceWithRawResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.BeamContoursResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam_contours import BeamContoursResourceWithRawResponse

        return BeamContoursResourceWithRawResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.BusesResourceWithRawResponse:
        """Services for querying and manipulation of satellite buses.

        A bus is the physical and software infrastructure backbone to which on-orbit satellite payloads are attached for power, control, and other support functions.
        """
        from .resources.buses import BusesResourceWithRawResponse

        return BusesResourceWithRawResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.channels import ChannelsResourceWithRawResponse

        return ChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.CloselyspacedobjectsResourceWithRawResponse:
        """
        This collection of services provides operations for manipulating and querying of closely spaced objects (on orbit) operations including docking, rendezvous, proximity and reporting of payload zone engagements observed and characterized over a period of time.
        """
        from .resources.closelyspacedobjects import CloselyspacedobjectsResourceWithRawResponse

        return CloselyspacedobjectsResourceWithRawResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.CollectRequestsResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_requests import CollectRequestsResourceWithRawResponse

        return CollectRequestsResourceWithRawResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.CollectResponsesResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_responses import CollectResponsesResourceWithRawResponse

        return CollectResponsesResourceWithRawResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.CommResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.comm import CommResourceWithRawResponse

        return CommResourceWithRawResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.ConjunctionsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of conjunctions.
        """
        from .resources.conjunctions import ConjunctionsResourceWithRawResponse

        return ConjunctionsResourceWithRawResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.CotsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.cots import CotsResourceWithRawResponse

        return CotsResourceWithRawResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.CountriesResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.countries import CountriesResourceWithRawResponse

        return CountriesResourceWithRawResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.CrewResourceWithRawResponse:
        """These services provide operations for posting and querying crew data.

        Crew data contains information about its members and their assignments.
        """
        from .resources.crew import CrewResourceWithRawResponse

        return CrewResourceWithRawResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.DeconflictsetResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.deconflictset import DeconflictsetResourceWithRawResponse

        return DeconflictsetResourceWithRawResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.DiffOfArrivalResourceWithRawResponse:
        """
        These services provide operations for querying and manipulation of Signal time and frequency difference of arrival (TDOA/FDOA) information obtained by using passive RF based sensor phenomenologies and sensor triangulation. The J2000 coordinate frame is the preferred frame for all observations, but in some cases observations may be in another frame depending on the provider.
        """
        from .resources.diff_of_arrival import DiffOfArrivalResourceWithRawResponse

        return DiffOfArrivalResourceWithRawResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.DiplomaticClearanceResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.diplomatic_clearance import DiplomaticClearanceResourceWithRawResponse

        return DiplomaticClearanceResourceWithRawResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.DriftHistoryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.drift_history import DriftHistoryResourceWithRawResponse

        return DriftHistoryResourceWithRawResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.DropzoneResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.dropzone import DropzoneResourceWithRawResponse

        return DropzoneResourceWithRawResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.EcpedrResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.ecpedr import EcpedrResourceWithRawResponse

        return EcpedrResourceWithRawResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.EffectRequestsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_requests import EffectRequestsResourceWithRawResponse

        return EffectRequestsResourceWithRawResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.EffectResponsesResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_responses import EffectResponsesResourceWithRawResponse

        return EffectResponsesResourceWithRawResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.ElsetsResourceWithRawResponse:
        """
        These services provide operations for querying and manipulation of element set data describing orbital characteristics of on-orbit objects. An element set is a collection of parameters that are used, along with an orbit propagator, to predict the motion of a satellite. The element set, or elset for short, consists of identification data, the classical elements and drag parameters.
        """
        from .resources.elsets import ElsetsResourceWithRawResponse

        return ElsetsResourceWithRawResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.EmireportResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emireport import EmireportResourceWithRawResponse

        return EmireportResourceWithRawResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.EmitterGeolocationResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emitter_geolocation import EmitterGeolocationResourceWithRawResponse

        return EmitterGeolocationResourceWithRawResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.EngineDetailsResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engine_details import EngineDetailsResourceWithRawResponse

        return EngineDetailsResourceWithRawResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.EnginesResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engines import EnginesResourceWithRawResponse

        return EnginesResourceWithRawResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.entities import EntitiesResourceWithRawResponse

        return EntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.EopResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.eop import EopResourceWithRawResponse

        return EopResourceWithRawResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.EphemerisResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris import EphemerisResourceWithRawResponse

        return EphemerisResourceWithRawResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.EphemerisSetsResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris_sets import EphemerisSetsResourceWithRawResponse

        return EphemerisSetsResourceWithRawResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.EquipmentResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment import EquipmentResourceWithRawResponse

        return EquipmentResourceWithRawResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.EquipmentRemarksResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment_remarks import EquipmentRemarksResourceWithRawResponse

        return EquipmentRemarksResourceWithRawResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.EvacResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.evac import EvacResourceWithRawResponse

        return EvacResourceWithRawResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.EventEvolutionResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.event_evolution import EventEvolutionResourceWithRawResponse

        return EventEvolutionResourceWithRawResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.FeatureAssessmentResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.feature_assessment import FeatureAssessmentResourceWithRawResponse

        return FeatureAssessmentResourceWithRawResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.FlightplanResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.flightplan import FlightplanResourceWithRawResponse

        return FlightplanResourceWithRawResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.GeoStatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.geo_status import GeoStatusResourceWithRawResponse

        return GeoStatusResourceWithRawResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(self) -> global_atmospheric_model.GlobalAtmosphericModelResourceWithRawResponse:
        """
        Models and Simulations is a collection of services that allow consumers to interact with data products representing independent models of various phenomenon, artificial intelligence models and predictions, or of mathematical parameters meant to feed mod and sim tools to produce estimates of environmental entities such as atmospheric models and heat maps.
        """
        from .resources.global_atmospheric_model import GlobalAtmosphericModelResourceWithRawResponse

        return GlobalAtmosphericModelResourceWithRawResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.GnssObservationsResourceWithRawResponse:
        from .resources.gnss_observations import GnssObservationsResourceWithRawResponse

        return GnssObservationsResourceWithRawResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.GnssObservationsetResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_observationset import GnssObservationsetResourceWithRawResponse

        return GnssObservationsetResourceWithRawResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.GnssRawIfResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_raw_if import GnssRawIfResourceWithRawResponse

        return GnssRawIfResourceWithRawResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.GroundImageryResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of ground imagery of terrestrial regions from on-orbit, air, and other sensors. Includes metadata on the image (time, region, source, etc) as well as binary content (typically GeoTIFF). Binary content must be downloaded individually by ID using the 'getFile' operation. Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.ground_imagery import GroundImageryResourceWithRawResponse

        return GroundImageryResourceWithRawResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.H3GeoResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo import H3GeoResourceWithRawResponse

        return H3GeoResourceWithRawResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.H3GeoHexCellResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo_hex_cell import H3GeoHexCellResourceWithRawResponse

        return H3GeoHexCellResourceWithRawResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.HazardResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.hazard import HazardResourceWithRawResponse

        return HazardResourceWithRawResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.IonoObservationsResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.iono_observations import IonoObservationsResourceWithRawResponse

        return IonoObservationsResourceWithRawResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.IrResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.ir import IrResourceWithRawResponse

        return IrResourceWithRawResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.IsrCollectionsResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.isr_collections import IsrCollectionsResourceWithRawResponse

        return IsrCollectionsResourceWithRawResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.ItemResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item import ItemResourceWithRawResponse

        return ItemResourceWithRawResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.ItemTrackingsResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item_trackings import ItemTrackingsResourceWithRawResponse

        return ItemTrackingsResourceWithRawResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.LaserdeconflictrequestResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laserdeconflictrequest import LaserdeconflictrequestResourceWithRawResponse

        return LaserdeconflictrequestResourceWithRawResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.LaseremitterResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laseremitter import LaseremitterResourceWithRawResponse

        return LaseremitterResourceWithRawResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.LaunchDetectionResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_detection import LaunchDetectionResourceWithRawResponse

        return LaunchDetectionResourceWithRawResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.LaunchEventResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of LaunchEvent data. Launch Event data are known space launches, either future or historic records containing items such as the launch site, launch epoch, and object.
        """
        from .resources.launch_event import LaunchEventResourceWithRawResponse

        return LaunchEventResourceWithRawResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.LaunchSiteResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site import LaunchSiteResourceWithRawResponse

        return LaunchSiteResourceWithRawResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.LaunchSiteDetailsResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site_details import LaunchSiteDetailsResourceWithRawResponse

        return LaunchSiteDetailsResourceWithRawResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.LaunchVehicleResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle import LaunchVehicleResourceWithRawResponse

        return LaunchVehicleResourceWithRawResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.LaunchVehicleDetailsResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle_details import LaunchVehicleDetailsResourceWithRawResponse

        return LaunchVehicleDetailsResourceWithRawResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.LinkStatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.link_status import LinkStatusResourceWithRawResponse

        return LinkStatusResourceWithRawResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.LinkstatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.linkstatus import LinkstatusResourceWithRawResponse

        return LinkstatusResourceWithRawResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.LocationResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.location import LocationResourceWithRawResponse

        return LocationResourceWithRawResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.LogisticsSupportResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.logistics_support import LogisticsSupportResourceWithRawResponse

        return LogisticsSupportResourceWithRawResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.ManeuversResourceWithRawResponse:
        """
        This service provides operations for querying and manipulation of detected/possible/confirmed on-orbit maneuvers. The J2000 coordinate frame is the preferred frame for all maneuver data, but in some cases data may be in another frame depending on the provider. Check the Storefront 'Data Products' section under the 'Discover' tab for maneuver data provider information.
        """
        from .resources.maneuvers import ManeuversResourceWithRawResponse

        return ManeuversResourceWithRawResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.ManifoldResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifold import ManifoldResourceWithRawResponse

        return ManifoldResourceWithRawResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.ManifoldelsetResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifoldelset import ManifoldelsetResourceWithRawResponse

        return ManifoldelsetResourceWithRawResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.MissileTracksResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.missile_tracks import MissileTracksResourceWithRawResponse

        return MissileTracksResourceWithRawResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.MissionAssignmentResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of mission assignment objects. MissionAssignment is used by C2 JUs and, optionally, non-C2 JUs to assign missions, designate targets, and provide target information to non-C2 JU platforms. Provision is made for the non-C2 JU platforms to acknowledge the message through receipt/compliance action.
        """
        from .resources.mission_assignment import MissionAssignmentResourceWithRawResponse

        return MissionAssignmentResourceWithRawResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.MtiResourceWithRawResponse:
        """
        These services provide operations for posting and querying Moving Target Indicator (MTI) STANAG 4607 data. Detailed MTI data supports activities such as targeting or less detailed data for applications such as situational awareness used/derived by exploitation systems.
        """
        from .resources.mti import MtiResourceWithRawResponse

        return MtiResourceWithRawResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.NavigationResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.navigation import NavigationResourceWithRawResponse

        return NavigationResourceWithRawResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(self) -> navigational_obstruction.NavigationalObstructionResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.navigational_obstruction import NavigationalObstructionResourceWithRawResponse

        return NavigationalObstructionResourceWithRawResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.NotificationResourceWithRawResponse:
        """
        A Notification Service allowing the broadcast of generic messages to the community. Users can send free-form messages, publish lists, and notify the community about events or alerts across various domains. Notifications and alerts are categorized by a 'msgType' field and are accessible via the UDL Secure Messaging API and REST API services.
        """
        from .resources.notification import NotificationResourceWithRawResponse

        return NotificationResourceWithRawResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.ObjectOfInterestResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.object_of_interest import ObjectOfInterestResourceWithRawResponse

        return ObjectOfInterestResourceWithRawResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.ObservationsResourceWithRawResponse:
        from .resources.observations import ObservationsResourceWithRawResponse

        return ObservationsResourceWithRawResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.OnboardnavigationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.onboardnavigation import OnboardnavigationResourceWithRawResponse

        return OnboardnavigationResourceWithRawResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.OnorbitResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbit import OnorbitResourceWithRawResponse

        return OnorbitResourceWithRawResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.OnorbitantennaResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitantenna import OnorbitantennaResourceWithRawResponse

        return OnorbitantennaResourceWithRawResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.OnorbitbatteryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitbattery import OnorbitbatteryResourceWithRawResponse

        return OnorbitbatteryResourceWithRawResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.OnorbitdetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitdetails import OnorbitdetailsResourceWithRawResponse

        return OnorbitdetailsResourceWithRawResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.OnorbiteventResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitevent import OnorbiteventResourceWithRawResponse

        return OnorbiteventResourceWithRawResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.OnorbitlistResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitlist import OnorbitlistResourceWithRawResponse

        return OnorbitlistResourceWithRawResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.OnorbitsolararrayResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitsolararray import OnorbitsolararrayResourceWithRawResponse

        return OnorbitsolararrayResourceWithRawResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.OnorbitthrusterResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthruster import OnorbitthrusterResourceWithRawResponse

        return OnorbitthrusterResourceWithRawResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.OnorbitthrusterstatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthrusterstatus import OnorbitthrusterstatusResourceWithRawResponse

        return OnorbitthrusterstatusResourceWithRawResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.OnorbitassessmentResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.onorbitassessment import OnorbitassessmentResourceWithRawResponse

        return OnorbitassessmentResourceWithRawResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.OperatingunitResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunit import OperatingunitResourceWithRawResponse

        return OperatingunitResourceWithRawResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.OperatingunitremarkResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunitremark import OperatingunitremarkResourceWithRawResponse

        return OperatingunitremarkResourceWithRawResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.OrbitdeterminationResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Orbit Determination (OD) data. Orbit Determination data contains algorithm results that describe General Perturbations or Special Perturbations orbital updates.
        """
        from .resources.orbitdetermination import OrbitdeterminationResourceWithRawResponse

        return OrbitdeterminationResourceWithRawResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.OrbittrackResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.orbittrack import OrbittrackResourceWithRawResponse

        return OrbittrackResourceWithRawResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organization import OrganizationResourceWithRawResponse

        return OrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.OrganizationdetailsResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organizationdetails import OrganizationdetailsResourceWithRawResponse

        return OrganizationdetailsResourceWithRawResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.PersonnelrecoveryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.personnelrecovery import PersonnelrecoveryResourceWithRawResponse

        return PersonnelrecoveryResourceWithRawResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.PoiResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.poi import PoiResourceWithRawResponse

        return PoiResourceWithRawResponse(self._client.poi)

    @cached_property
    def port(self) -> port.PortResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.port import PortResourceWithRawResponse

        return PortResourceWithRawResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.ReportAndActivitiesResourceWithRawResponse:
        from .resources.report_and_activities import ReportAndActivitiesResourceWithRawResponse

        return ReportAndActivitiesResourceWithRawResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.RfBandResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band import RfBandResourceWithRawResponse

        return RfBandResourceWithRawResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.RfBandTypeResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band_type import RfBandTypeResourceWithRawResponse

        return RfBandTypeResourceWithRawResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.RfEmitterResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_emitter import RfEmitterResourceWithRawResponse

        return RfEmitterResourceWithRawResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.RouteStatsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.route_stats import RouteStatsResourceWithRawResponse

        return RouteStatsResourceWithRawResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.SarObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.sar_observation import SarObservationResourceWithRawResponse

        return SarObservationResourceWithRawResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.ScientificResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.scientific import ScientificResourceWithRawResponse

        return ScientificResourceWithRawResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.ScsResourceWithRawResponse:
        from .resources.scs import ScsResourceWithRawResponse

        return ScsResourceWithRawResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.SecureMessagingResourceWithRawResponse:
        """
        Secure Messaging is based on Apache Kafka which is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. Kafka provides a unified, high-throughput, low-latency platform for handling real-time data feeds.  All messaging is secured; consumers will not receive messages unless authorized to do so. J2000 is the preferred coordinate frame for all observations, but in some cases observations may be in another frame depending on the provider. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.secure_messaging import SecureMessagingResourceWithRawResponse

        return SecureMessagingResourceWithRawResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.SensorResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor import SensorResourceWithRawResponse

        return SensorResourceWithRawResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.SensorStatingResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_stating import SensorStatingResourceWithRawResponse

        return SensorStatingResourceWithRawResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.SensorMaintenanceResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_maintenance import SensorMaintenanceResourceWithRawResponse

        return SensorMaintenanceResourceWithRawResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(self) -> sensor_observation_type.SensorObservationTypeResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_observation_type import SensorObservationTypeResourceWithRawResponse

        return SensorObservationTypeResourceWithRawResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.SensorPlanResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.sensor_plan import SensorPlanResourceWithRawResponse

        return SensorPlanResourceWithRawResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.SensorTypeResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_type import SensorTypeResourceWithRawResponse

        return SensorTypeResourceWithRawResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.SeraDataCommDetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.sera_data_comm_details import SeraDataCommDetailsResourceWithRawResponse

        return SeraDataCommDetailsResourceWithRawResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.SeraDataEarlyWarningResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_early_warning import SeraDataEarlyWarningResourceWithRawResponse

        return SeraDataEarlyWarningResourceWithRawResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.SeraDataNavigationResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_navigation import SeraDataNavigationResourceWithRawResponse

        return SeraDataNavigationResourceWithRawResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(self) -> seradata_optical_payload.SeradataOpticalPayloadResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_optical_payload import SeradataOpticalPayloadResourceWithRawResponse

        return SeradataOpticalPayloadResourceWithRawResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.SeradataRadarPayloadResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_radar_payload import SeradataRadarPayloadResourceWithRawResponse

        return SeradataRadarPayloadResourceWithRawResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(self) -> seradata_sigint_payload.SeradataSigintPayloadResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_sigint_payload import SeradataSigintPayloadResourceWithRawResponse

        return SeradataSigintPayloadResourceWithRawResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.SeradataSpacecraftDetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.seradata_spacecraft_details import SeradataSpacecraftDetailsResourceWithRawResponse

        return SeradataSpacecraftDetailsResourceWithRawResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.SgiResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of space weather/solar, geomagnetic, and radiation belt index data.
        """
        from .resources.sgi import SgiResourceWithRawResponse

        return SgiResourceWithRawResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.SigactResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.sigact import SigactResourceWithRawResponse

        return SigactResourceWithRawResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.SiteResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site import SiteResourceWithRawResponse

        return SiteResourceWithRawResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.SiteRemarkResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_remark import SiteRemarkResourceWithRawResponse

        return SiteRemarkResourceWithRawResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.SiteStatusResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_status import SiteStatusResourceWithRawResponse

        return SiteStatusResourceWithRawResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.SkyImageryResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of sky imagery data. Sky imagery is ground or space based telescope imagery of RSO's and includes metadata on the image (time, source, etc) as well as binary image content (e.g. FITS, EOSSA, EOCHIP, MP4). Binary content must be downloaded individually by ID using the 'getFile' operation.
        """
        from .resources.sky_imagery import SkyImageryResourceWithRawResponse

        return SkyImageryResourceWithRawResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.SoiObservationSetResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.soi_observation_set import SoiObservationSetResourceWithRawResponse

        return SoiObservationSetResourceWithRawResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.SolarArrayResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array import SolarArrayResourceWithRawResponse

        return SolarArrayResourceWithRawResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.SolarArrayDetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array_details import SolarArrayDetailsResourceWithRawResponse

        return SolarArrayDetailsResourceWithRawResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.SortiePprResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.sortie_ppr import SortiePprResourceWithRawResponse

        return SortiePprResourceWithRawResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.SpaceEnvObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.space_env_observation import SpaceEnvObservationResourceWithRawResponse

        return SpaceEnvObservationResourceWithRawResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.StageResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.stage import StageResourceWithRawResponse

        return StageResourceWithRawResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.StarCatalogResourceWithRawResponse:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
        from .resources.star_catalog import StarCatalogResourceWithRawResponse

        return StarCatalogResourceWithRawResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.StateVectorResourceWithRawResponse:
        """
        This service provides operations for querying and manipulation of state vectors for On-orbit objects. State vectors are cartesian vectors of position (r) and velocity (v) that together with their time (epoch) (t) uniquely determine the trajectory of the orbiting body in space. J2000 is the preferred coordinate frame for all state vector positions/velocities in UDL, but in some cases data may be in another frame depending on the provider and/or datatype. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.state_vector import StateVectorResourceWithRawResponse

        return StateVectorResourceWithRawResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.StatusResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.status import StatusResourceWithRawResponse

        return StatusResourceWithRawResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.SubstatusResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.substatus import SubstatusResourceWithRawResponse

        return SubstatusResourceWithRawResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.SupportingDataResourceWithRawResponse:
        from .resources.supporting_data import SupportingDataResourceWithRawResponse

        return SupportingDataResourceWithRawResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.SurfaceResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface import SurfaceResourceWithRawResponse

        return SurfaceResourceWithRawResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.SurfaceObstructionResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface_obstruction import SurfaceObstructionResourceWithRawResponse

        return SurfaceObstructionResourceWithRawResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.SwirResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.swir import SwirResourceWithRawResponse

        return SwirResourceWithRawResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.TaiUtcResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.tai_utc import TaiUtcResourceWithRawResponse

        return TaiUtcResourceWithRawResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.TdoaFdoaResourceWithRawResponse:
        from .resources.tdoa_fdoa import TdoaFdoaResourceWithRawResponse

        return TdoaFdoaResourceWithRawResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.TrackResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track import TrackResourceWithRawResponse

        return TrackResourceWithRawResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.TrackDetailsResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track_details import TrackDetailsResourceWithRawResponse

        return TrackDetailsResourceWithRawResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.TrackRouteResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.track_route import TrackRouteResourceWithRawResponse

        return TrackRouteResourceWithRawResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.TransponderResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.transponder import TransponderResourceWithRawResponse

        return TransponderResourceWithRawResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.VesselResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of maritime Vessel and Vessel Status data. Vessel contains the static data of the specific vessel: mmsi, cruise speed, max speed, etc.
        """
        from .resources.vessel import VesselResourceWithRawResponse

        return VesselResourceWithRawResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.VideoResourceWithRawResponse:
        """This collection of services provides operations for video streaming."""
        from .resources.video import VideoResourceWithRawResponse

        return VideoResourceWithRawResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.WeatherDataResourceWithRawResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_data import WeatherDataResourceWithRawResponse

        return WeatherDataResourceWithRawResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.WeatherReportResourceWithRawResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_report import WeatherReportResourceWithRawResponse

        return WeatherReportResourceWithRawResponse(self._client.weather_report)


class AsyncUnifieddatalibraryWithRawResponse:
    _client: AsyncUnifieddatalibrary

    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self._client = client

    @cached_property
    def air_events(self) -> air_events.AsyncAirEventsResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_events import AsyncAirEventsResourceWithRawResponse

        return AsyncAirEventsResourceWithRawResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AsyncAirOperationsResourceWithRawResponse:
        from .resources.air_operations import AsyncAirOperationsResourceWithRawResponse

        return AsyncAirOperationsResourceWithRawResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AsyncAirTransportMissionsResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_transport_missions import AsyncAirTransportMissionsResourceWithRawResponse

        return AsyncAirTransportMissionsResourceWithRawResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AsyncAircraftResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft import AsyncAircraftResourceWithRawResponse

        return AsyncAircraftResourceWithRawResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AsyncAircraftSortiesResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aircraft_sorties import AsyncAircraftSortiesResourceWithRawResponse

        return AsyncAircraftSortiesResourceWithRawResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(self) -> aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_status_remarks import AsyncAircraftStatusRemarksResourceWithRawResponse

        return AsyncAircraftStatusRemarksResourceWithRawResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AsyncAircraftStatusesResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_statuses import AsyncAircraftStatusesResourceWithRawResponse

        return AsyncAircraftStatusesResourceWithRawResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(
        self,
    ) -> airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slot_consumptions import AsyncAirfieldSlotConsumptionsResourceWithRawResponse

        return AsyncAirfieldSlotConsumptionsResourceWithRawResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AsyncAirfieldSlotsResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slots import AsyncAirfieldSlotsResourceWithRawResponse

        return AsyncAirfieldSlotsResourceWithRawResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AsyncAirfieldStatusResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_status import AsyncAirfieldStatusResourceWithRawResponse

        return AsyncAirfieldStatusResourceWithRawResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AsyncAirfieldsResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfields import AsyncAirfieldsResourceWithRawResponse

        return AsyncAirfieldsResourceWithRawResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AsyncAirloadPlansResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airload_plans import AsyncAirloadPlansResourceWithRawResponse

        return AsyncAirloadPlansResourceWithRawResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(self) -> airspace_control_orders.AsyncAirspaceControlOrdersResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airspace_control_orders import AsyncAirspaceControlOrdersResourceWithRawResponse

        return AsyncAirspaceControlOrdersResourceWithRawResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AsyncAIsResourceWithRawResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais import AsyncAIsResourceWithRawResponse

        return AsyncAIsResourceWithRawResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AsyncAIsObjectsResourceWithRawResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais_objects import AsyncAIsObjectsResourceWithRawResponse

        return AsyncAIsObjectsResourceWithRawResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AsyncAnalyticImageryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.analytic_imagery import AsyncAnalyticImageryResourceWithRawResponse

        return AsyncAnalyticImageryResourceWithRawResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AsyncAntennasResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.antennas import AsyncAntennasResourceWithRawResponse

        return AsyncAntennasResourceWithRawResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AsyncAttitudeDataResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_data import AsyncAttitudeDataResourceWithRawResponse

        return AsyncAttitudeDataResourceWithRawResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AsyncAttitudeSetsResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_sets import AsyncAttitudeSetsResourceWithRawResponse

        return AsyncAttitudeSetsResourceWithRawResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(self) -> aviation_risk_management.AsyncAviationRiskManagementResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aviation_risk_management import AsyncAviationRiskManagementResourceWithRawResponse

        return AsyncAviationRiskManagementResourceWithRawResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.AsyncBatteriesResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batteries import AsyncBatteriesResourceWithRawResponse

        return AsyncBatteriesResourceWithRawResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.AsyncBatterydetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batterydetails import AsyncBatterydetailsResourceWithRawResponse

        return AsyncBatterydetailsResourceWithRawResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.AsyncBeamResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam import AsyncBeamResourceWithRawResponse

        return AsyncBeamResourceWithRawResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.AsyncBeamContoursResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam_contours import AsyncBeamContoursResourceWithRawResponse

        return AsyncBeamContoursResourceWithRawResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.AsyncBusesResourceWithRawResponse:
        """Services for querying and manipulation of satellite buses.

        A bus is the physical and software infrastructure backbone to which on-orbit satellite payloads are attached for power, control, and other support functions.
        """
        from .resources.buses import AsyncBusesResourceWithRawResponse

        return AsyncBusesResourceWithRawResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.channels import AsyncChannelsResourceWithRawResponse

        return AsyncChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.AsyncCloselyspacedobjectsResourceWithRawResponse:
        """
        This collection of services provides operations for manipulating and querying of closely spaced objects (on orbit) operations including docking, rendezvous, proximity and reporting of payload zone engagements observed and characterized over a period of time.
        """
        from .resources.closelyspacedobjects import AsyncCloselyspacedobjectsResourceWithRawResponse

        return AsyncCloselyspacedobjectsResourceWithRawResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.AsyncCollectRequestsResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_requests import AsyncCollectRequestsResourceWithRawResponse

        return AsyncCollectRequestsResourceWithRawResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.AsyncCollectResponsesResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_responses import AsyncCollectResponsesResourceWithRawResponse

        return AsyncCollectResponsesResourceWithRawResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.AsyncCommResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.comm import AsyncCommResourceWithRawResponse

        return AsyncCommResourceWithRawResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.AsyncConjunctionsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of conjunctions.
        """
        from .resources.conjunctions import AsyncConjunctionsResourceWithRawResponse

        return AsyncConjunctionsResourceWithRawResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.AsyncCotsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.cots import AsyncCotsResourceWithRawResponse

        return AsyncCotsResourceWithRawResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.AsyncCountriesResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.countries import AsyncCountriesResourceWithRawResponse

        return AsyncCountriesResourceWithRawResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.AsyncCrewResourceWithRawResponse:
        """These services provide operations for posting and querying crew data.

        Crew data contains information about its members and their assignments.
        """
        from .resources.crew import AsyncCrewResourceWithRawResponse

        return AsyncCrewResourceWithRawResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.AsyncDeconflictsetResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.deconflictset import AsyncDeconflictsetResourceWithRawResponse

        return AsyncDeconflictsetResourceWithRawResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.AsyncDiffOfArrivalResourceWithRawResponse:
        """
        These services provide operations for querying and manipulation of Signal time and frequency difference of arrival (TDOA/FDOA) information obtained by using passive RF based sensor phenomenologies and sensor triangulation. The J2000 coordinate frame is the preferred frame for all observations, but in some cases observations may be in another frame depending on the provider.
        """
        from .resources.diff_of_arrival import AsyncDiffOfArrivalResourceWithRawResponse

        return AsyncDiffOfArrivalResourceWithRawResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.AsyncDiplomaticClearanceResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.diplomatic_clearance import AsyncDiplomaticClearanceResourceWithRawResponse

        return AsyncDiplomaticClearanceResourceWithRawResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.AsyncDriftHistoryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.drift_history import AsyncDriftHistoryResourceWithRawResponse

        return AsyncDriftHistoryResourceWithRawResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.AsyncDropzoneResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.dropzone import AsyncDropzoneResourceWithRawResponse

        return AsyncDropzoneResourceWithRawResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.AsyncEcpedrResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.ecpedr import AsyncEcpedrResourceWithRawResponse

        return AsyncEcpedrResourceWithRawResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.AsyncEffectRequestsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_requests import AsyncEffectRequestsResourceWithRawResponse

        return AsyncEffectRequestsResourceWithRawResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.AsyncEffectResponsesResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_responses import AsyncEffectResponsesResourceWithRawResponse

        return AsyncEffectResponsesResourceWithRawResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.AsyncElsetsResourceWithRawResponse:
        """
        These services provide operations for querying and manipulation of element set data describing orbital characteristics of on-orbit objects. An element set is a collection of parameters that are used, along with an orbit propagator, to predict the motion of a satellite. The element set, or elset for short, consists of identification data, the classical elements and drag parameters.
        """
        from .resources.elsets import AsyncElsetsResourceWithRawResponse

        return AsyncElsetsResourceWithRawResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.AsyncEmireportResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emireport import AsyncEmireportResourceWithRawResponse

        return AsyncEmireportResourceWithRawResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.AsyncEmitterGeolocationResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emitter_geolocation import AsyncEmitterGeolocationResourceWithRawResponse

        return AsyncEmitterGeolocationResourceWithRawResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.AsyncEngineDetailsResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engine_details import AsyncEngineDetailsResourceWithRawResponse

        return AsyncEngineDetailsResourceWithRawResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.AsyncEnginesResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engines import AsyncEnginesResourceWithRawResponse

        return AsyncEnginesResourceWithRawResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.entities import AsyncEntitiesResourceWithRawResponse

        return AsyncEntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.AsyncEopResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.eop import AsyncEopResourceWithRawResponse

        return AsyncEopResourceWithRawResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.AsyncEphemerisResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris import AsyncEphemerisResourceWithRawResponse

        return AsyncEphemerisResourceWithRawResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.AsyncEphemerisSetsResourceWithRawResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris_sets import AsyncEphemerisSetsResourceWithRawResponse

        return AsyncEphemerisSetsResourceWithRawResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.AsyncEquipmentResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment import AsyncEquipmentResourceWithRawResponse

        return AsyncEquipmentResourceWithRawResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.AsyncEquipmentRemarksResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment_remarks import AsyncEquipmentRemarksResourceWithRawResponse

        return AsyncEquipmentRemarksResourceWithRawResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.AsyncEvacResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.evac import AsyncEvacResourceWithRawResponse

        return AsyncEvacResourceWithRawResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.AsyncEventEvolutionResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.event_evolution import AsyncEventEvolutionResourceWithRawResponse

        return AsyncEventEvolutionResourceWithRawResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.AsyncFeatureAssessmentResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.feature_assessment import AsyncFeatureAssessmentResourceWithRawResponse

        return AsyncFeatureAssessmentResourceWithRawResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.AsyncFlightplanResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.flightplan import AsyncFlightplanResourceWithRawResponse

        return AsyncFlightplanResourceWithRawResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.AsyncGeoStatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.geo_status import AsyncGeoStatusResourceWithRawResponse

        return AsyncGeoStatusResourceWithRawResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(self) -> global_atmospheric_model.AsyncGlobalAtmosphericModelResourceWithRawResponse:
        """
        Models and Simulations is a collection of services that allow consumers to interact with data products representing independent models of various phenomenon, artificial intelligence models and predictions, or of mathematical parameters meant to feed mod and sim tools to produce estimates of environmental entities such as atmospheric models and heat maps.
        """
        from .resources.global_atmospheric_model import AsyncGlobalAtmosphericModelResourceWithRawResponse

        return AsyncGlobalAtmosphericModelResourceWithRawResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.AsyncGnssObservationsResourceWithRawResponse:
        from .resources.gnss_observations import AsyncGnssObservationsResourceWithRawResponse

        return AsyncGnssObservationsResourceWithRawResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.AsyncGnssObservationsetResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_observationset import AsyncGnssObservationsetResourceWithRawResponse

        return AsyncGnssObservationsetResourceWithRawResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.AsyncGnssRawIfResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_raw_if import AsyncGnssRawIfResourceWithRawResponse

        return AsyncGnssRawIfResourceWithRawResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.AsyncGroundImageryResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of ground imagery of terrestrial regions from on-orbit, air, and other sensors. Includes metadata on the image (time, region, source, etc) as well as binary content (typically GeoTIFF). Binary content must be downloaded individually by ID using the 'getFile' operation. Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.ground_imagery import AsyncGroundImageryResourceWithRawResponse

        return AsyncGroundImageryResourceWithRawResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.AsyncH3GeoResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo import AsyncH3GeoResourceWithRawResponse

        return AsyncH3GeoResourceWithRawResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.AsyncH3GeoHexCellResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo_hex_cell import AsyncH3GeoHexCellResourceWithRawResponse

        return AsyncH3GeoHexCellResourceWithRawResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.AsyncHazardResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.hazard import AsyncHazardResourceWithRawResponse

        return AsyncHazardResourceWithRawResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.AsyncIonoObservationsResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.iono_observations import AsyncIonoObservationsResourceWithRawResponse

        return AsyncIonoObservationsResourceWithRawResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.AsyncIrResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.ir import AsyncIrResourceWithRawResponse

        return AsyncIrResourceWithRawResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.AsyncIsrCollectionsResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.isr_collections import AsyncIsrCollectionsResourceWithRawResponse

        return AsyncIsrCollectionsResourceWithRawResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.AsyncItemResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item import AsyncItemResourceWithRawResponse

        return AsyncItemResourceWithRawResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.AsyncItemTrackingsResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item_trackings import AsyncItemTrackingsResourceWithRawResponse

        return AsyncItemTrackingsResourceWithRawResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.AsyncLaserdeconflictrequestResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laserdeconflictrequest import AsyncLaserdeconflictrequestResourceWithRawResponse

        return AsyncLaserdeconflictrequestResourceWithRawResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.AsyncLaseremitterResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laseremitter import AsyncLaseremitterResourceWithRawResponse

        return AsyncLaseremitterResourceWithRawResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.AsyncLaunchDetectionResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_detection import AsyncLaunchDetectionResourceWithRawResponse

        return AsyncLaunchDetectionResourceWithRawResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.AsyncLaunchEventResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of LaunchEvent data. Launch Event data are known space launches, either future or historic records containing items such as the launch site, launch epoch, and object.
        """
        from .resources.launch_event import AsyncLaunchEventResourceWithRawResponse

        return AsyncLaunchEventResourceWithRawResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.AsyncLaunchSiteResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site import AsyncLaunchSiteResourceWithRawResponse

        return AsyncLaunchSiteResourceWithRawResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.AsyncLaunchSiteDetailsResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site_details import AsyncLaunchSiteDetailsResourceWithRawResponse

        return AsyncLaunchSiteDetailsResourceWithRawResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.AsyncLaunchVehicleResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle import AsyncLaunchVehicleResourceWithRawResponse

        return AsyncLaunchVehicleResourceWithRawResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.AsyncLaunchVehicleDetailsResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle_details import AsyncLaunchVehicleDetailsResourceWithRawResponse

        return AsyncLaunchVehicleDetailsResourceWithRawResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.AsyncLinkStatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.link_status import AsyncLinkStatusResourceWithRawResponse

        return AsyncLinkStatusResourceWithRawResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.AsyncLinkstatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.linkstatus import AsyncLinkstatusResourceWithRawResponse

        return AsyncLinkstatusResourceWithRawResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.location import AsyncLocationResourceWithRawResponse

        return AsyncLocationResourceWithRawResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.AsyncLogisticsSupportResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.logistics_support import AsyncLogisticsSupportResourceWithRawResponse

        return AsyncLogisticsSupportResourceWithRawResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.AsyncManeuversResourceWithRawResponse:
        """
        This service provides operations for querying and manipulation of detected/possible/confirmed on-orbit maneuvers. The J2000 coordinate frame is the preferred frame for all maneuver data, but in some cases data may be in another frame depending on the provider. Check the Storefront 'Data Products' section under the 'Discover' tab for maneuver data provider information.
        """
        from .resources.maneuvers import AsyncManeuversResourceWithRawResponse

        return AsyncManeuversResourceWithRawResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.AsyncManifoldResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifold import AsyncManifoldResourceWithRawResponse

        return AsyncManifoldResourceWithRawResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.AsyncManifoldelsetResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifoldelset import AsyncManifoldelsetResourceWithRawResponse

        return AsyncManifoldelsetResourceWithRawResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.AsyncMissileTracksResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.missile_tracks import AsyncMissileTracksResourceWithRawResponse

        return AsyncMissileTracksResourceWithRawResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.AsyncMissionAssignmentResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of mission assignment objects. MissionAssignment is used by C2 JUs and, optionally, non-C2 JUs to assign missions, designate targets, and provide target information to non-C2 JU platforms. Provision is made for the non-C2 JU platforms to acknowledge the message through receipt/compliance action.
        """
        from .resources.mission_assignment import AsyncMissionAssignmentResourceWithRawResponse

        return AsyncMissionAssignmentResourceWithRawResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.AsyncMtiResourceWithRawResponse:
        """
        These services provide operations for posting and querying Moving Target Indicator (MTI) STANAG 4607 data. Detailed MTI data supports activities such as targeting or less detailed data for applications such as situational awareness used/derived by exploitation systems.
        """
        from .resources.mti import AsyncMtiResourceWithRawResponse

        return AsyncMtiResourceWithRawResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.AsyncNavigationResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.navigation import AsyncNavigationResourceWithRawResponse

        return AsyncNavigationResourceWithRawResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(self) -> navigational_obstruction.AsyncNavigationalObstructionResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.navigational_obstruction import AsyncNavigationalObstructionResourceWithRawResponse

        return AsyncNavigationalObstructionResourceWithRawResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.AsyncNotificationResourceWithRawResponse:
        """
        A Notification Service allowing the broadcast of generic messages to the community. Users can send free-form messages, publish lists, and notify the community about events or alerts across various domains. Notifications and alerts are categorized by a 'msgType' field and are accessible via the UDL Secure Messaging API and REST API services.
        """
        from .resources.notification import AsyncNotificationResourceWithRawResponse

        return AsyncNotificationResourceWithRawResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.AsyncObjectOfInterestResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.object_of_interest import AsyncObjectOfInterestResourceWithRawResponse

        return AsyncObjectOfInterestResourceWithRawResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.AsyncObservationsResourceWithRawResponse:
        from .resources.observations import AsyncObservationsResourceWithRawResponse

        return AsyncObservationsResourceWithRawResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.AsyncOnboardnavigationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.onboardnavigation import AsyncOnboardnavigationResourceWithRawResponse

        return AsyncOnboardnavigationResourceWithRawResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.AsyncOnorbitResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbit import AsyncOnorbitResourceWithRawResponse

        return AsyncOnorbitResourceWithRawResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.AsyncOnorbitantennaResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitantenna import AsyncOnorbitantennaResourceWithRawResponse

        return AsyncOnorbitantennaResourceWithRawResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.AsyncOnorbitbatteryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitbattery import AsyncOnorbitbatteryResourceWithRawResponse

        return AsyncOnorbitbatteryResourceWithRawResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.AsyncOnorbitdetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitdetails import AsyncOnorbitdetailsResourceWithRawResponse

        return AsyncOnorbitdetailsResourceWithRawResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.AsyncOnorbiteventResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitevent import AsyncOnorbiteventResourceWithRawResponse

        return AsyncOnorbiteventResourceWithRawResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.AsyncOnorbitlistResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitlist import AsyncOnorbitlistResourceWithRawResponse

        return AsyncOnorbitlistResourceWithRawResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.AsyncOnorbitsolararrayResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitsolararray import AsyncOnorbitsolararrayResourceWithRawResponse

        return AsyncOnorbitsolararrayResourceWithRawResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.AsyncOnorbitthrusterResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthruster import AsyncOnorbitthrusterResourceWithRawResponse

        return AsyncOnorbitthrusterResourceWithRawResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.AsyncOnorbitthrusterstatusResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthrusterstatus import AsyncOnorbitthrusterstatusResourceWithRawResponse

        return AsyncOnorbitthrusterstatusResourceWithRawResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.AsyncOnorbitassessmentResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.onorbitassessment import AsyncOnorbitassessmentResourceWithRawResponse

        return AsyncOnorbitassessmentResourceWithRawResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.AsyncOperatingunitResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunit import AsyncOperatingunitResourceWithRawResponse

        return AsyncOperatingunitResourceWithRawResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.AsyncOperatingunitremarkResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunitremark import AsyncOperatingunitremarkResourceWithRawResponse

        return AsyncOperatingunitremarkResourceWithRawResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.AsyncOrbitdeterminationResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Orbit Determination (OD) data. Orbit Determination data contains algorithm results that describe General Perturbations or Special Perturbations orbital updates.
        """
        from .resources.orbitdetermination import AsyncOrbitdeterminationResourceWithRawResponse

        return AsyncOrbitdeterminationResourceWithRawResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.AsyncOrbittrackResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.orbittrack import AsyncOrbittrackResourceWithRawResponse

        return AsyncOrbittrackResourceWithRawResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organization import AsyncOrganizationResourceWithRawResponse

        return AsyncOrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.AsyncOrganizationdetailsResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organizationdetails import AsyncOrganizationdetailsResourceWithRawResponse

        return AsyncOrganizationdetailsResourceWithRawResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.AsyncPersonnelrecoveryResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.personnelrecovery import AsyncPersonnelrecoveryResourceWithRawResponse

        return AsyncPersonnelrecoveryResourceWithRawResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.AsyncPoiResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.poi import AsyncPoiResourceWithRawResponse

        return AsyncPoiResourceWithRawResponse(self._client.poi)

    @cached_property
    def port(self) -> port.AsyncPortResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.port import AsyncPortResourceWithRawResponse

        return AsyncPortResourceWithRawResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.AsyncReportAndActivitiesResourceWithRawResponse:
        from .resources.report_and_activities import AsyncReportAndActivitiesResourceWithRawResponse

        return AsyncReportAndActivitiesResourceWithRawResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.AsyncRfBandResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band import AsyncRfBandResourceWithRawResponse

        return AsyncRfBandResourceWithRawResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.AsyncRfBandTypeResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band_type import AsyncRfBandTypeResourceWithRawResponse

        return AsyncRfBandTypeResourceWithRawResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.AsyncRfEmitterResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_emitter import AsyncRfEmitterResourceWithRawResponse

        return AsyncRfEmitterResourceWithRawResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.AsyncRouteStatsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.route_stats import AsyncRouteStatsResourceWithRawResponse

        return AsyncRouteStatsResourceWithRawResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.AsyncSarObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.sar_observation import AsyncSarObservationResourceWithRawResponse

        return AsyncSarObservationResourceWithRawResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.AsyncScientificResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.scientific import AsyncScientificResourceWithRawResponse

        return AsyncScientificResourceWithRawResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.AsyncScsResourceWithRawResponse:
        from .resources.scs import AsyncScsResourceWithRawResponse

        return AsyncScsResourceWithRawResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.AsyncSecureMessagingResourceWithRawResponse:
        """
        Secure Messaging is based on Apache Kafka which is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. Kafka provides a unified, high-throughput, low-latency platform for handling real-time data feeds.  All messaging is secured; consumers will not receive messages unless authorized to do so. J2000 is the preferred coordinate frame for all observations, but in some cases observations may be in another frame depending on the provider. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.secure_messaging import AsyncSecureMessagingResourceWithRawResponse

        return AsyncSecureMessagingResourceWithRawResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.AsyncSensorResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor import AsyncSensorResourceWithRawResponse

        return AsyncSensorResourceWithRawResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.AsyncSensorStatingResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_stating import AsyncSensorStatingResourceWithRawResponse

        return AsyncSensorStatingResourceWithRawResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.AsyncSensorMaintenanceResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_maintenance import AsyncSensorMaintenanceResourceWithRawResponse

        return AsyncSensorMaintenanceResourceWithRawResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(self) -> sensor_observation_type.AsyncSensorObservationTypeResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_observation_type import AsyncSensorObservationTypeResourceWithRawResponse

        return AsyncSensorObservationTypeResourceWithRawResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.AsyncSensorPlanResourceWithRawResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.sensor_plan import AsyncSensorPlanResourceWithRawResponse

        return AsyncSensorPlanResourceWithRawResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.AsyncSensorTypeResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_type import AsyncSensorTypeResourceWithRawResponse

        return AsyncSensorTypeResourceWithRawResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.AsyncSeraDataCommDetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.sera_data_comm_details import AsyncSeraDataCommDetailsResourceWithRawResponse

        return AsyncSeraDataCommDetailsResourceWithRawResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.AsyncSeraDataEarlyWarningResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_early_warning import AsyncSeraDataEarlyWarningResourceWithRawResponse

        return AsyncSeraDataEarlyWarningResourceWithRawResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.AsyncSeraDataNavigationResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_navigation import AsyncSeraDataNavigationResourceWithRawResponse

        return AsyncSeraDataNavigationResourceWithRawResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(self) -> seradata_optical_payload.AsyncSeradataOpticalPayloadResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_optical_payload import AsyncSeradataOpticalPayloadResourceWithRawResponse

        return AsyncSeradataOpticalPayloadResourceWithRawResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.AsyncSeradataRadarPayloadResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_radar_payload import AsyncSeradataRadarPayloadResourceWithRawResponse

        return AsyncSeradataRadarPayloadResourceWithRawResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(self) -> seradata_sigint_payload.AsyncSeradataSigintPayloadResourceWithRawResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_sigint_payload import AsyncSeradataSigintPayloadResourceWithRawResponse

        return AsyncSeradataSigintPayloadResourceWithRawResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.seradata_spacecraft_details import AsyncSeradataSpacecraftDetailsResourceWithRawResponse

        return AsyncSeradataSpacecraftDetailsResourceWithRawResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.AsyncSgiResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of space weather/solar, geomagnetic, and radiation belt index data.
        """
        from .resources.sgi import AsyncSgiResourceWithRawResponse

        return AsyncSgiResourceWithRawResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.AsyncSigactResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.sigact import AsyncSigactResourceWithRawResponse

        return AsyncSigactResourceWithRawResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.AsyncSiteResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site import AsyncSiteResourceWithRawResponse

        return AsyncSiteResourceWithRawResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.AsyncSiteRemarkResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_remark import AsyncSiteRemarkResourceWithRawResponse

        return AsyncSiteRemarkResourceWithRawResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.AsyncSiteStatusResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_status import AsyncSiteStatusResourceWithRawResponse

        return AsyncSiteStatusResourceWithRawResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.AsyncSkyImageryResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of sky imagery data. Sky imagery is ground or space based telescope imagery of RSO's and includes metadata on the image (time, source, etc) as well as binary image content (e.g. FITS, EOSSA, EOCHIP, MP4). Binary content must be downloaded individually by ID using the 'getFile' operation.
        """
        from .resources.sky_imagery import AsyncSkyImageryResourceWithRawResponse

        return AsyncSkyImageryResourceWithRawResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.AsyncSoiObservationSetResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.soi_observation_set import AsyncSoiObservationSetResourceWithRawResponse

        return AsyncSoiObservationSetResourceWithRawResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.AsyncSolarArrayResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array import AsyncSolarArrayResourceWithRawResponse

        return AsyncSolarArrayResourceWithRawResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.AsyncSolarArrayDetailsResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array_details import AsyncSolarArrayDetailsResourceWithRawResponse

        return AsyncSolarArrayDetailsResourceWithRawResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.AsyncSortiePprResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.sortie_ppr import AsyncSortiePprResourceWithRawResponse

        return AsyncSortiePprResourceWithRawResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.AsyncSpaceEnvObservationResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.space_env_observation import AsyncSpaceEnvObservationResourceWithRawResponse

        return AsyncSpaceEnvObservationResourceWithRawResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.AsyncStageResourceWithRawResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.stage import AsyncStageResourceWithRawResponse

        return AsyncStageResourceWithRawResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.AsyncStarCatalogResourceWithRawResponse:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
        from .resources.star_catalog import AsyncStarCatalogResourceWithRawResponse

        return AsyncStarCatalogResourceWithRawResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.AsyncStateVectorResourceWithRawResponse:
        """
        This service provides operations for querying and manipulation of state vectors for On-orbit objects. State vectors are cartesian vectors of position (r) and velocity (v) that together with their time (epoch) (t) uniquely determine the trajectory of the orbiting body in space. J2000 is the preferred coordinate frame for all state vector positions/velocities in UDL, but in some cases data may be in another frame depending on the provider and/or datatype. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.state_vector import AsyncStateVectorResourceWithRawResponse

        return AsyncStateVectorResourceWithRawResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.status import AsyncStatusResourceWithRawResponse

        return AsyncStatusResourceWithRawResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.AsyncSubstatusResourceWithRawResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.substatus import AsyncSubstatusResourceWithRawResponse

        return AsyncSubstatusResourceWithRawResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.AsyncSupportingDataResourceWithRawResponse:
        from .resources.supporting_data import AsyncSupportingDataResourceWithRawResponse

        return AsyncSupportingDataResourceWithRawResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.AsyncSurfaceResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface import AsyncSurfaceResourceWithRawResponse

        return AsyncSurfaceResourceWithRawResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.AsyncSurfaceObstructionResourceWithRawResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface_obstruction import AsyncSurfaceObstructionResourceWithRawResponse

        return AsyncSurfaceObstructionResourceWithRawResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.AsyncSwirResourceWithRawResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.swir import AsyncSwirResourceWithRawResponse

        return AsyncSwirResourceWithRawResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.AsyncTaiUtcResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.tai_utc import AsyncTaiUtcResourceWithRawResponse

        return AsyncTaiUtcResourceWithRawResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.AsyncTdoaFdoaResourceWithRawResponse:
        from .resources.tdoa_fdoa import AsyncTdoaFdoaResourceWithRawResponse

        return AsyncTdoaFdoaResourceWithRawResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.AsyncTrackResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track import AsyncTrackResourceWithRawResponse

        return AsyncTrackResourceWithRawResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.AsyncTrackDetailsResourceWithRawResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track_details import AsyncTrackDetailsResourceWithRawResponse

        return AsyncTrackDetailsResourceWithRawResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.AsyncTrackRouteResourceWithRawResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.track_route import AsyncTrackRouteResourceWithRawResponse

        return AsyncTrackRouteResourceWithRawResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.AsyncTransponderResourceWithRawResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.transponder import AsyncTransponderResourceWithRawResponse

        return AsyncTransponderResourceWithRawResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.AsyncVesselResourceWithRawResponse:
        """
        This service provides operations for manipulation and querying of maritime Vessel and Vessel Status data. Vessel contains the static data of the specific vessel: mmsi, cruise speed, max speed, etc.
        """
        from .resources.vessel import AsyncVesselResourceWithRawResponse

        return AsyncVesselResourceWithRawResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.AsyncVideoResourceWithRawResponse:
        """This collection of services provides operations for video streaming."""
        from .resources.video import AsyncVideoResourceWithRawResponse

        return AsyncVideoResourceWithRawResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.AsyncWeatherDataResourceWithRawResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_data import AsyncWeatherDataResourceWithRawResponse

        return AsyncWeatherDataResourceWithRawResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.AsyncWeatherReportResourceWithRawResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_report import AsyncWeatherReportResourceWithRawResponse

        return AsyncWeatherReportResourceWithRawResponse(self._client.weather_report)


class UnifieddatalibraryWithStreamedResponse:
    _client: Unifieddatalibrary

    def __init__(self, client: Unifieddatalibrary) -> None:
        self._client = client

    @cached_property
    def air_events(self) -> air_events.AirEventsResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_events import AirEventsResourceWithStreamingResponse

        return AirEventsResourceWithStreamingResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AirOperationsResourceWithStreamingResponse:
        from .resources.air_operations import AirOperationsResourceWithStreamingResponse

        return AirOperationsResourceWithStreamingResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AirTransportMissionsResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_transport_missions import AirTransportMissionsResourceWithStreamingResponse

        return AirTransportMissionsResourceWithStreamingResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AircraftResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft import AircraftResourceWithStreamingResponse

        return AircraftResourceWithStreamingResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AircraftSortiesResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aircraft_sorties import AircraftSortiesResourceWithStreamingResponse

        return AircraftSortiesResourceWithStreamingResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(self) -> aircraft_status_remarks.AircraftStatusRemarksResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_status_remarks import AircraftStatusRemarksResourceWithStreamingResponse

        return AircraftStatusRemarksResourceWithStreamingResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AircraftStatusesResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_statuses import AircraftStatusesResourceWithStreamingResponse

        return AircraftStatusesResourceWithStreamingResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(
        self,
    ) -> airfield_slot_consumptions.AirfieldSlotConsumptionsResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slot_consumptions import AirfieldSlotConsumptionsResourceWithStreamingResponse

        return AirfieldSlotConsumptionsResourceWithStreamingResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AirfieldSlotsResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slots import AirfieldSlotsResourceWithStreamingResponse

        return AirfieldSlotsResourceWithStreamingResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AirfieldStatusResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_status import AirfieldStatusResourceWithStreamingResponse

        return AirfieldStatusResourceWithStreamingResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AirfieldsResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfields import AirfieldsResourceWithStreamingResponse

        return AirfieldsResourceWithStreamingResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AirloadPlansResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airload_plans import AirloadPlansResourceWithStreamingResponse

        return AirloadPlansResourceWithStreamingResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(self) -> airspace_control_orders.AirspaceControlOrdersResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airspace_control_orders import AirspaceControlOrdersResourceWithStreamingResponse

        return AirspaceControlOrdersResourceWithStreamingResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AIsResourceWithStreamingResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais import AIsResourceWithStreamingResponse

        return AIsResourceWithStreamingResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AIsObjectsResourceWithStreamingResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais_objects import AIsObjectsResourceWithStreamingResponse

        return AIsObjectsResourceWithStreamingResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AnalyticImageryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.analytic_imagery import AnalyticImageryResourceWithStreamingResponse

        return AnalyticImageryResourceWithStreamingResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AntennasResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.antennas import AntennasResourceWithStreamingResponse

        return AntennasResourceWithStreamingResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AttitudeDataResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_data import AttitudeDataResourceWithStreamingResponse

        return AttitudeDataResourceWithStreamingResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AttitudeSetsResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_sets import AttitudeSetsResourceWithStreamingResponse

        return AttitudeSetsResourceWithStreamingResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(self) -> aviation_risk_management.AviationRiskManagementResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aviation_risk_management import AviationRiskManagementResourceWithStreamingResponse

        return AviationRiskManagementResourceWithStreamingResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.BatteriesResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batteries import BatteriesResourceWithStreamingResponse

        return BatteriesResourceWithStreamingResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.BatterydetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batterydetails import BatterydetailsResourceWithStreamingResponse

        return BatterydetailsResourceWithStreamingResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.BeamResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam import BeamResourceWithStreamingResponse

        return BeamResourceWithStreamingResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.BeamContoursResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam_contours import BeamContoursResourceWithStreamingResponse

        return BeamContoursResourceWithStreamingResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.BusesResourceWithStreamingResponse:
        """Services for querying and manipulation of satellite buses.

        A bus is the physical and software infrastructure backbone to which on-orbit satellite payloads are attached for power, control, and other support functions.
        """
        from .resources.buses import BusesResourceWithStreamingResponse

        return BusesResourceWithStreamingResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.channels import ChannelsResourceWithStreamingResponse

        return ChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.CloselyspacedobjectsResourceWithStreamingResponse:
        """
        This collection of services provides operations for manipulating and querying of closely spaced objects (on orbit) operations including docking, rendezvous, proximity and reporting of payload zone engagements observed and characterized over a period of time.
        """
        from .resources.closelyspacedobjects import CloselyspacedobjectsResourceWithStreamingResponse

        return CloselyspacedobjectsResourceWithStreamingResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.CollectRequestsResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_requests import CollectRequestsResourceWithStreamingResponse

        return CollectRequestsResourceWithStreamingResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.CollectResponsesResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_responses import CollectResponsesResourceWithStreamingResponse

        return CollectResponsesResourceWithStreamingResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.CommResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.comm import CommResourceWithStreamingResponse

        return CommResourceWithStreamingResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.ConjunctionsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of conjunctions.
        """
        from .resources.conjunctions import ConjunctionsResourceWithStreamingResponse

        return ConjunctionsResourceWithStreamingResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.CotsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.cots import CotsResourceWithStreamingResponse

        return CotsResourceWithStreamingResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.CountriesResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.countries import CountriesResourceWithStreamingResponse

        return CountriesResourceWithStreamingResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.CrewResourceWithStreamingResponse:
        """These services provide operations for posting and querying crew data.

        Crew data contains information about its members and their assignments.
        """
        from .resources.crew import CrewResourceWithStreamingResponse

        return CrewResourceWithStreamingResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.DeconflictsetResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.deconflictset import DeconflictsetResourceWithStreamingResponse

        return DeconflictsetResourceWithStreamingResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.DiffOfArrivalResourceWithStreamingResponse:
        """
        These services provide operations for querying and manipulation of Signal time and frequency difference of arrival (TDOA/FDOA) information obtained by using passive RF based sensor phenomenologies and sensor triangulation. The J2000 coordinate frame is the preferred frame for all observations, but in some cases observations may be in another frame depending on the provider.
        """
        from .resources.diff_of_arrival import DiffOfArrivalResourceWithStreamingResponse

        return DiffOfArrivalResourceWithStreamingResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.DiplomaticClearanceResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.diplomatic_clearance import DiplomaticClearanceResourceWithStreamingResponse

        return DiplomaticClearanceResourceWithStreamingResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.DriftHistoryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.drift_history import DriftHistoryResourceWithStreamingResponse

        return DriftHistoryResourceWithStreamingResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.DropzoneResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.dropzone import DropzoneResourceWithStreamingResponse

        return DropzoneResourceWithStreamingResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.EcpedrResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.ecpedr import EcpedrResourceWithStreamingResponse

        return EcpedrResourceWithStreamingResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.EffectRequestsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_requests import EffectRequestsResourceWithStreamingResponse

        return EffectRequestsResourceWithStreamingResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.EffectResponsesResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_responses import EffectResponsesResourceWithStreamingResponse

        return EffectResponsesResourceWithStreamingResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.ElsetsResourceWithStreamingResponse:
        """
        These services provide operations for querying and manipulation of element set data describing orbital characteristics of on-orbit objects. An element set is a collection of parameters that are used, along with an orbit propagator, to predict the motion of a satellite. The element set, or elset for short, consists of identification data, the classical elements and drag parameters.
        """
        from .resources.elsets import ElsetsResourceWithStreamingResponse

        return ElsetsResourceWithStreamingResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.EmireportResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emireport import EmireportResourceWithStreamingResponse

        return EmireportResourceWithStreamingResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.EmitterGeolocationResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emitter_geolocation import EmitterGeolocationResourceWithStreamingResponse

        return EmitterGeolocationResourceWithStreamingResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.EngineDetailsResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engine_details import EngineDetailsResourceWithStreamingResponse

        return EngineDetailsResourceWithStreamingResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.EnginesResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engines import EnginesResourceWithStreamingResponse

        return EnginesResourceWithStreamingResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.EntitiesResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.entities import EntitiesResourceWithStreamingResponse

        return EntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.EopResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.eop import EopResourceWithStreamingResponse

        return EopResourceWithStreamingResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.EphemerisResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris import EphemerisResourceWithStreamingResponse

        return EphemerisResourceWithStreamingResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.EphemerisSetsResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris_sets import EphemerisSetsResourceWithStreamingResponse

        return EphemerisSetsResourceWithStreamingResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.EquipmentResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment import EquipmentResourceWithStreamingResponse

        return EquipmentResourceWithStreamingResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.EquipmentRemarksResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment_remarks import EquipmentRemarksResourceWithStreamingResponse

        return EquipmentRemarksResourceWithStreamingResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.EvacResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.evac import EvacResourceWithStreamingResponse

        return EvacResourceWithStreamingResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.EventEvolutionResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.event_evolution import EventEvolutionResourceWithStreamingResponse

        return EventEvolutionResourceWithStreamingResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.FeatureAssessmentResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.feature_assessment import FeatureAssessmentResourceWithStreamingResponse

        return FeatureAssessmentResourceWithStreamingResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.FlightplanResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.flightplan import FlightplanResourceWithStreamingResponse

        return FlightplanResourceWithStreamingResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.GeoStatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.geo_status import GeoStatusResourceWithStreamingResponse

        return GeoStatusResourceWithStreamingResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(self) -> global_atmospheric_model.GlobalAtmosphericModelResourceWithStreamingResponse:
        """
        Models and Simulations is a collection of services that allow consumers to interact with data products representing independent models of various phenomenon, artificial intelligence models and predictions, or of mathematical parameters meant to feed mod and sim tools to produce estimates of environmental entities such as atmospheric models and heat maps.
        """
        from .resources.global_atmospheric_model import GlobalAtmosphericModelResourceWithStreamingResponse

        return GlobalAtmosphericModelResourceWithStreamingResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.GnssObservationsResourceWithStreamingResponse:
        from .resources.gnss_observations import GnssObservationsResourceWithStreamingResponse

        return GnssObservationsResourceWithStreamingResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.GnssObservationsetResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_observationset import GnssObservationsetResourceWithStreamingResponse

        return GnssObservationsetResourceWithStreamingResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.GnssRawIfResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_raw_if import GnssRawIfResourceWithStreamingResponse

        return GnssRawIfResourceWithStreamingResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.GroundImageryResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of ground imagery of terrestrial regions from on-orbit, air, and other sensors. Includes metadata on the image (time, region, source, etc) as well as binary content (typically GeoTIFF). Binary content must be downloaded individually by ID using the 'getFile' operation. Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.ground_imagery import GroundImageryResourceWithStreamingResponse

        return GroundImageryResourceWithStreamingResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.H3GeoResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo import H3GeoResourceWithStreamingResponse

        return H3GeoResourceWithStreamingResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.H3GeoHexCellResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo_hex_cell import H3GeoHexCellResourceWithStreamingResponse

        return H3GeoHexCellResourceWithStreamingResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.HazardResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.hazard import HazardResourceWithStreamingResponse

        return HazardResourceWithStreamingResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.IonoObservationsResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.iono_observations import IonoObservationsResourceWithStreamingResponse

        return IonoObservationsResourceWithStreamingResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.IrResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.ir import IrResourceWithStreamingResponse

        return IrResourceWithStreamingResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.IsrCollectionsResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.isr_collections import IsrCollectionsResourceWithStreamingResponse

        return IsrCollectionsResourceWithStreamingResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.ItemResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item import ItemResourceWithStreamingResponse

        return ItemResourceWithStreamingResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.ItemTrackingsResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item_trackings import ItemTrackingsResourceWithStreamingResponse

        return ItemTrackingsResourceWithStreamingResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.LaserdeconflictrequestResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laserdeconflictrequest import LaserdeconflictrequestResourceWithStreamingResponse

        return LaserdeconflictrequestResourceWithStreamingResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.LaseremitterResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laseremitter import LaseremitterResourceWithStreamingResponse

        return LaseremitterResourceWithStreamingResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.LaunchDetectionResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_detection import LaunchDetectionResourceWithStreamingResponse

        return LaunchDetectionResourceWithStreamingResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.LaunchEventResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of LaunchEvent data. Launch Event data are known space launches, either future or historic records containing items such as the launch site, launch epoch, and object.
        """
        from .resources.launch_event import LaunchEventResourceWithStreamingResponse

        return LaunchEventResourceWithStreamingResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.LaunchSiteResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site import LaunchSiteResourceWithStreamingResponse

        return LaunchSiteResourceWithStreamingResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.LaunchSiteDetailsResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site_details import LaunchSiteDetailsResourceWithStreamingResponse

        return LaunchSiteDetailsResourceWithStreamingResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.LaunchVehicleResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle import LaunchVehicleResourceWithStreamingResponse

        return LaunchVehicleResourceWithStreamingResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.LaunchVehicleDetailsResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle_details import LaunchVehicleDetailsResourceWithStreamingResponse

        return LaunchVehicleDetailsResourceWithStreamingResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.LinkStatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.link_status import LinkStatusResourceWithStreamingResponse

        return LinkStatusResourceWithStreamingResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.LinkstatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.linkstatus import LinkstatusResourceWithStreamingResponse

        return LinkstatusResourceWithStreamingResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.LocationResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.location import LocationResourceWithStreamingResponse

        return LocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.LogisticsSupportResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.logistics_support import LogisticsSupportResourceWithStreamingResponse

        return LogisticsSupportResourceWithStreamingResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.ManeuversResourceWithStreamingResponse:
        """
        This service provides operations for querying and manipulation of detected/possible/confirmed on-orbit maneuvers. The J2000 coordinate frame is the preferred frame for all maneuver data, but in some cases data may be in another frame depending on the provider. Check the Storefront 'Data Products' section under the 'Discover' tab for maneuver data provider information.
        """
        from .resources.maneuvers import ManeuversResourceWithStreamingResponse

        return ManeuversResourceWithStreamingResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.ManifoldResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifold import ManifoldResourceWithStreamingResponse

        return ManifoldResourceWithStreamingResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.ManifoldelsetResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifoldelset import ManifoldelsetResourceWithStreamingResponse

        return ManifoldelsetResourceWithStreamingResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.MissileTracksResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.missile_tracks import MissileTracksResourceWithStreamingResponse

        return MissileTracksResourceWithStreamingResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.MissionAssignmentResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of mission assignment objects. MissionAssignment is used by C2 JUs and, optionally, non-C2 JUs to assign missions, designate targets, and provide target information to non-C2 JU platforms. Provision is made for the non-C2 JU platforms to acknowledge the message through receipt/compliance action.
        """
        from .resources.mission_assignment import MissionAssignmentResourceWithStreamingResponse

        return MissionAssignmentResourceWithStreamingResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.MtiResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying Moving Target Indicator (MTI) STANAG 4607 data. Detailed MTI data supports activities such as targeting or less detailed data for applications such as situational awareness used/derived by exploitation systems.
        """
        from .resources.mti import MtiResourceWithStreamingResponse

        return MtiResourceWithStreamingResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.NavigationResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.navigation import NavigationResourceWithStreamingResponse

        return NavigationResourceWithStreamingResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(self) -> navigational_obstruction.NavigationalObstructionResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.navigational_obstruction import NavigationalObstructionResourceWithStreamingResponse

        return NavigationalObstructionResourceWithStreamingResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.NotificationResourceWithStreamingResponse:
        """
        A Notification Service allowing the broadcast of generic messages to the community. Users can send free-form messages, publish lists, and notify the community about events or alerts across various domains. Notifications and alerts are categorized by a 'msgType' field and are accessible via the UDL Secure Messaging API and REST API services.
        """
        from .resources.notification import NotificationResourceWithStreamingResponse

        return NotificationResourceWithStreamingResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.ObjectOfInterestResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.object_of_interest import ObjectOfInterestResourceWithStreamingResponse

        return ObjectOfInterestResourceWithStreamingResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.ObservationsResourceWithStreamingResponse:
        from .resources.observations import ObservationsResourceWithStreamingResponse

        return ObservationsResourceWithStreamingResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.OnboardnavigationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.onboardnavigation import OnboardnavigationResourceWithStreamingResponse

        return OnboardnavigationResourceWithStreamingResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.OnorbitResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbit import OnorbitResourceWithStreamingResponse

        return OnorbitResourceWithStreamingResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.OnorbitantennaResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitantenna import OnorbitantennaResourceWithStreamingResponse

        return OnorbitantennaResourceWithStreamingResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.OnorbitbatteryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitbattery import OnorbitbatteryResourceWithStreamingResponse

        return OnorbitbatteryResourceWithStreamingResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.OnorbitdetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitdetails import OnorbitdetailsResourceWithStreamingResponse

        return OnorbitdetailsResourceWithStreamingResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.OnorbiteventResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitevent import OnorbiteventResourceWithStreamingResponse

        return OnorbiteventResourceWithStreamingResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.OnorbitlistResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitlist import OnorbitlistResourceWithStreamingResponse

        return OnorbitlistResourceWithStreamingResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.OnorbitsolararrayResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitsolararray import OnorbitsolararrayResourceWithStreamingResponse

        return OnorbitsolararrayResourceWithStreamingResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.OnorbitthrusterResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthruster import OnorbitthrusterResourceWithStreamingResponse

        return OnorbitthrusterResourceWithStreamingResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.OnorbitthrusterstatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthrusterstatus import OnorbitthrusterstatusResourceWithStreamingResponse

        return OnorbitthrusterstatusResourceWithStreamingResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.OnorbitassessmentResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.onorbitassessment import OnorbitassessmentResourceWithStreamingResponse

        return OnorbitassessmentResourceWithStreamingResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.OperatingunitResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunit import OperatingunitResourceWithStreamingResponse

        return OperatingunitResourceWithStreamingResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.OperatingunitremarkResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunitremark import OperatingunitremarkResourceWithStreamingResponse

        return OperatingunitremarkResourceWithStreamingResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.OrbitdeterminationResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Orbit Determination (OD) data. Orbit Determination data contains algorithm results that describe General Perturbations or Special Perturbations orbital updates.
        """
        from .resources.orbitdetermination import OrbitdeterminationResourceWithStreamingResponse

        return OrbitdeterminationResourceWithStreamingResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.OrbittrackResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.orbittrack import OrbittrackResourceWithStreamingResponse

        return OrbittrackResourceWithStreamingResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organization import OrganizationResourceWithStreamingResponse

        return OrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.OrganizationdetailsResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organizationdetails import OrganizationdetailsResourceWithStreamingResponse

        return OrganizationdetailsResourceWithStreamingResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.PersonnelrecoveryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.personnelrecovery import PersonnelrecoveryResourceWithStreamingResponse

        return PersonnelrecoveryResourceWithStreamingResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.PoiResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.poi import PoiResourceWithStreamingResponse

        return PoiResourceWithStreamingResponse(self._client.poi)

    @cached_property
    def port(self) -> port.PortResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.port import PortResourceWithStreamingResponse

        return PortResourceWithStreamingResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.ReportAndActivitiesResourceWithStreamingResponse:
        from .resources.report_and_activities import ReportAndActivitiesResourceWithStreamingResponse

        return ReportAndActivitiesResourceWithStreamingResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.RfBandResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band import RfBandResourceWithStreamingResponse

        return RfBandResourceWithStreamingResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.RfBandTypeResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band_type import RfBandTypeResourceWithStreamingResponse

        return RfBandTypeResourceWithStreamingResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.RfEmitterResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_emitter import RfEmitterResourceWithStreamingResponse

        return RfEmitterResourceWithStreamingResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.RouteStatsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.route_stats import RouteStatsResourceWithStreamingResponse

        return RouteStatsResourceWithStreamingResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.SarObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.sar_observation import SarObservationResourceWithStreamingResponse

        return SarObservationResourceWithStreamingResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.ScientificResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.scientific import ScientificResourceWithStreamingResponse

        return ScientificResourceWithStreamingResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.ScsResourceWithStreamingResponse:
        from .resources.scs import ScsResourceWithStreamingResponse

        return ScsResourceWithStreamingResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.SecureMessagingResourceWithStreamingResponse:
        """
        Secure Messaging is based on Apache Kafka which is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. Kafka provides a unified, high-throughput, low-latency platform for handling real-time data feeds.  All messaging is secured; consumers will not receive messages unless authorized to do so. J2000 is the preferred coordinate frame for all observations, but in some cases observations may be in another frame depending on the provider. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.secure_messaging import SecureMessagingResourceWithStreamingResponse

        return SecureMessagingResourceWithStreamingResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.SensorResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor import SensorResourceWithStreamingResponse

        return SensorResourceWithStreamingResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.SensorStatingResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_stating import SensorStatingResourceWithStreamingResponse

        return SensorStatingResourceWithStreamingResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.SensorMaintenanceResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_maintenance import SensorMaintenanceResourceWithStreamingResponse

        return SensorMaintenanceResourceWithStreamingResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(self) -> sensor_observation_type.SensorObservationTypeResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_observation_type import SensorObservationTypeResourceWithStreamingResponse

        return SensorObservationTypeResourceWithStreamingResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.SensorPlanResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.sensor_plan import SensorPlanResourceWithStreamingResponse

        return SensorPlanResourceWithStreamingResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.SensorTypeResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_type import SensorTypeResourceWithStreamingResponse

        return SensorTypeResourceWithStreamingResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.SeraDataCommDetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.sera_data_comm_details import SeraDataCommDetailsResourceWithStreamingResponse

        return SeraDataCommDetailsResourceWithStreamingResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.SeraDataEarlyWarningResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_early_warning import SeraDataEarlyWarningResourceWithStreamingResponse

        return SeraDataEarlyWarningResourceWithStreamingResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.SeraDataNavigationResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_navigation import SeraDataNavigationResourceWithStreamingResponse

        return SeraDataNavigationResourceWithStreamingResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(self) -> seradata_optical_payload.SeradataOpticalPayloadResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_optical_payload import SeradataOpticalPayloadResourceWithStreamingResponse

        return SeradataOpticalPayloadResourceWithStreamingResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.SeradataRadarPayloadResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_radar_payload import SeradataRadarPayloadResourceWithStreamingResponse

        return SeradataRadarPayloadResourceWithStreamingResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(self) -> seradata_sigint_payload.SeradataSigintPayloadResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_sigint_payload import SeradataSigintPayloadResourceWithStreamingResponse

        return SeradataSigintPayloadResourceWithStreamingResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.SeradataSpacecraftDetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.seradata_spacecraft_details import SeradataSpacecraftDetailsResourceWithStreamingResponse

        return SeradataSpacecraftDetailsResourceWithStreamingResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.SgiResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of space weather/solar, geomagnetic, and radiation belt index data.
        """
        from .resources.sgi import SgiResourceWithStreamingResponse

        return SgiResourceWithStreamingResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.SigactResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.sigact import SigactResourceWithStreamingResponse

        return SigactResourceWithStreamingResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.SiteResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site import SiteResourceWithStreamingResponse

        return SiteResourceWithStreamingResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.SiteRemarkResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_remark import SiteRemarkResourceWithStreamingResponse

        return SiteRemarkResourceWithStreamingResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.SiteStatusResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_status import SiteStatusResourceWithStreamingResponse

        return SiteStatusResourceWithStreamingResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.SkyImageryResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of sky imagery data. Sky imagery is ground or space based telescope imagery of RSO's and includes metadata on the image (time, source, etc) as well as binary image content (e.g. FITS, EOSSA, EOCHIP, MP4). Binary content must be downloaded individually by ID using the 'getFile' operation.
        """
        from .resources.sky_imagery import SkyImageryResourceWithStreamingResponse

        return SkyImageryResourceWithStreamingResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.SoiObservationSetResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.soi_observation_set import SoiObservationSetResourceWithStreamingResponse

        return SoiObservationSetResourceWithStreamingResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.SolarArrayResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array import SolarArrayResourceWithStreamingResponse

        return SolarArrayResourceWithStreamingResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.SolarArrayDetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array_details import SolarArrayDetailsResourceWithStreamingResponse

        return SolarArrayDetailsResourceWithStreamingResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.SortiePprResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.sortie_ppr import SortiePprResourceWithStreamingResponse

        return SortiePprResourceWithStreamingResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.SpaceEnvObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.space_env_observation import SpaceEnvObservationResourceWithStreamingResponse

        return SpaceEnvObservationResourceWithStreamingResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.StageResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.stage import StageResourceWithStreamingResponse

        return StageResourceWithStreamingResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.StarCatalogResourceWithStreamingResponse:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
        from .resources.star_catalog import StarCatalogResourceWithStreamingResponse

        return StarCatalogResourceWithStreamingResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.StateVectorResourceWithStreamingResponse:
        """
        This service provides operations for querying and manipulation of state vectors for On-orbit objects. State vectors are cartesian vectors of position (r) and velocity (v) that together with their time (epoch) (t) uniquely determine the trajectory of the orbiting body in space. J2000 is the preferred coordinate frame for all state vector positions/velocities in UDL, but in some cases data may be in another frame depending on the provider and/or datatype. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.state_vector import StateVectorResourceWithStreamingResponse

        return StateVectorResourceWithStreamingResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.StatusResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.status import StatusResourceWithStreamingResponse

        return StatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.SubstatusResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.substatus import SubstatusResourceWithStreamingResponse

        return SubstatusResourceWithStreamingResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.SupportingDataResourceWithStreamingResponse:
        from .resources.supporting_data import SupportingDataResourceWithStreamingResponse

        return SupportingDataResourceWithStreamingResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.SurfaceResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface import SurfaceResourceWithStreamingResponse

        return SurfaceResourceWithStreamingResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.SurfaceObstructionResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface_obstruction import SurfaceObstructionResourceWithStreamingResponse

        return SurfaceObstructionResourceWithStreamingResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.SwirResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.swir import SwirResourceWithStreamingResponse

        return SwirResourceWithStreamingResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.TaiUtcResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.tai_utc import TaiUtcResourceWithStreamingResponse

        return TaiUtcResourceWithStreamingResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.TdoaFdoaResourceWithStreamingResponse:
        from .resources.tdoa_fdoa import TdoaFdoaResourceWithStreamingResponse

        return TdoaFdoaResourceWithStreamingResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.TrackResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track import TrackResourceWithStreamingResponse

        return TrackResourceWithStreamingResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.TrackDetailsResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track_details import TrackDetailsResourceWithStreamingResponse

        return TrackDetailsResourceWithStreamingResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.TrackRouteResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.track_route import TrackRouteResourceWithStreamingResponse

        return TrackRouteResourceWithStreamingResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.TransponderResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.transponder import TransponderResourceWithStreamingResponse

        return TransponderResourceWithStreamingResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.VesselResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of maritime Vessel and Vessel Status data. Vessel contains the static data of the specific vessel: mmsi, cruise speed, max speed, etc.
        """
        from .resources.vessel import VesselResourceWithStreamingResponse

        return VesselResourceWithStreamingResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.VideoResourceWithStreamingResponse:
        """This collection of services provides operations for video streaming."""
        from .resources.video import VideoResourceWithStreamingResponse

        return VideoResourceWithStreamingResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.WeatherDataResourceWithStreamingResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_data import WeatherDataResourceWithStreamingResponse

        return WeatherDataResourceWithStreamingResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.WeatherReportResourceWithStreamingResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_report import WeatherReportResourceWithStreamingResponse

        return WeatherReportResourceWithStreamingResponse(self._client.weather_report)


class AsyncUnifieddatalibraryWithStreamedResponse:
    _client: AsyncUnifieddatalibrary

    def __init__(self, client: AsyncUnifieddatalibrary) -> None:
        self._client = client

    @cached_property
    def air_events(self) -> air_events.AsyncAirEventsResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_events import AsyncAirEventsResourceWithStreamingResponse

        return AsyncAirEventsResourceWithStreamingResponse(self._client.air_events)

    @cached_property
    def air_operations(self) -> air_operations.AsyncAirOperationsResourceWithStreamingResponse:
        from .resources.air_operations import AsyncAirOperationsResourceWithStreamingResponse

        return AsyncAirOperationsResourceWithStreamingResponse(self._client.air_operations)

    @cached_property
    def air_transport_missions(self) -> air_transport_missions.AsyncAirTransportMissionsResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.air_transport_missions import AsyncAirTransportMissionsResourceWithStreamingResponse

        return AsyncAirTransportMissionsResourceWithStreamingResponse(self._client.air_transport_missions)

    @cached_property
    def aircraft(self) -> aircraft.AsyncAircraftResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft import AsyncAircraftResourceWithStreamingResponse

        return AsyncAircraftResourceWithStreamingResponse(self._client.aircraft)

    @cached_property
    def aircraft_sorties(self) -> aircraft_sorties.AsyncAircraftSortiesResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aircraft_sorties import AsyncAircraftSortiesResourceWithStreamingResponse

        return AsyncAircraftSortiesResourceWithStreamingResponse(self._client.aircraft_sorties)

    @cached_property
    def aircraft_status_remarks(
        self,
    ) -> aircraft_status_remarks.AsyncAircraftStatusRemarksResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_status_remarks import AsyncAircraftStatusRemarksResourceWithStreamingResponse

        return AsyncAircraftStatusRemarksResourceWithStreamingResponse(self._client.aircraft_status_remarks)

    @cached_property
    def aircraft_statuses(self) -> aircraft_statuses.AsyncAircraftStatusesResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of Aircraft and Aircraft Status data. Aircraft contains the static data of the specific aircraft: tail number, cruise speed, max speed, minimum required runway length, etc. The Aircraft Status contains the dynamic data associated with the specific aircraft: remaining fuel, mission readiness, and inventory for example.
        """
        from .resources.aircraft_statuses import AsyncAircraftStatusesResourceWithStreamingResponse

        return AsyncAircraftStatusesResourceWithStreamingResponse(self._client.aircraft_statuses)

    @cached_property
    def airfield_slot_consumptions(
        self,
    ) -> airfield_slot_consumptions.AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slot_consumptions import AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse

        return AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse(self._client.airfield_slot_consumptions)

    @cached_property
    def airfield_slots(self) -> airfield_slots.AsyncAirfieldSlotsResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_slots import AsyncAirfieldSlotsResourceWithStreamingResponse

        return AsyncAirfieldSlotsResourceWithStreamingResponse(self._client.airfield_slots)

    @cached_property
    def airfield_status(self) -> airfield_status.AsyncAirfieldStatusResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfield_status import AsyncAirfieldStatusResourceWithStreamingResponse

        return AsyncAirfieldStatusResourceWithStreamingResponse(self._client.airfield_status)

    @cached_property
    def airfields(self) -> airfields.AsyncAirfieldsResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.airfields import AsyncAirfieldsResourceWithStreamingResponse

        return AsyncAirfieldsResourceWithStreamingResponse(self._client.airfields)

    @cached_property
    def airload_plans(self) -> airload_plans.AsyncAirloadPlansResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airload_plans import AsyncAirloadPlansResourceWithStreamingResponse

        return AsyncAirloadPlansResourceWithStreamingResponse(self._client.airload_plans)

    @cached_property
    def airspace_control_orders(
        self,
    ) -> airspace_control_orders.AsyncAirspaceControlOrdersResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.airspace_control_orders import AsyncAirspaceControlOrdersResourceWithStreamingResponse

        return AsyncAirspaceControlOrdersResourceWithStreamingResponse(self._client.airspace_control_orders)

    @cached_property
    def ais(self) -> ais.AsyncAIsResourceWithStreamingResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais import AsyncAIsResourceWithStreamingResponse

        return AsyncAIsResourceWithStreamingResponse(self._client.ais)

    @cached_property
    def ais_objects(self) -> ais_objects.AsyncAIsObjectsResourceWithStreamingResponse:
        """
        These services provide for posting and querying of self-reported information obtained from the Automatic Identification System (AIS) equipment. This contains information such as unique identification, status, position, course, and speed. The AIS is an automatic tracking system that uses transceivers on ships and is used by vessel traffic services. Although technically and operationally distinct, the AIS system is analogous to ADS-B which performs a similar function for aircraft. AIS is intended to assist a vessel's watchstanding officers and allow maritime authorities to track and monitor vessel movements. AIS integrates a standardized VHF transceiver with a positioning system, such as Global Positioning System receiver, with other electronic navigation sensors, such as gyrocompass or rate of turn indicator. Vessels fitted with AIS transceivers can be tracked by AIS base stations located along coastlines or, when out of range of terrestrial networks, through a growing number of satellites that are fitted with special AIS receivers that are capable of deconflicting a large number of signatures.
        """
        from .resources.ais_objects import AsyncAIsObjectsResourceWithStreamingResponse

        return AsyncAIsObjectsResourceWithStreamingResponse(self._client.ais_objects)

    @cached_property
    def analytic_imagery(self) -> analytic_imagery.AsyncAnalyticImageryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.analytic_imagery import AsyncAnalyticImageryResourceWithStreamingResponse

        return AsyncAnalyticImageryResourceWithStreamingResponse(self._client.analytic_imagery)

    @cached_property
    def antennas(self) -> antennas.AsyncAntennasResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.antennas import AsyncAntennasResourceWithStreamingResponse

        return AsyncAntennasResourceWithStreamingResponse(self._client.antennas)

    @cached_property
    def attitude_data(self) -> attitude_data.AsyncAttitudeDataResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_data import AsyncAttitudeDataResourceWithStreamingResponse

        return AsyncAttitudeDataResourceWithStreamingResponse(self._client.attitude_data)

    @cached_property
    def attitude_sets(self) -> attitude_sets.AsyncAttitudeSetsResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.attitude_sets import AsyncAttitudeSetsResourceWithStreamingResponse

        return AsyncAttitudeSetsResourceWithStreamingResponse(self._client.attitude_sets)

    @cached_property
    def aviation_risk_management(
        self,
    ) -> aviation_risk_management.AsyncAviationRiskManagementResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.aviation_risk_management import AsyncAviationRiskManagementResourceWithStreamingResponse

        return AsyncAviationRiskManagementResourceWithStreamingResponse(self._client.aviation_risk_management)

    @cached_property
    def batteries(self) -> batteries.AsyncBatteriesResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batteries import AsyncBatteriesResourceWithStreamingResponse

        return AsyncBatteriesResourceWithStreamingResponse(self._client.batteries)

    @cached_property
    def batterydetails(self) -> batterydetails.AsyncBatterydetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.batterydetails import AsyncBatterydetailsResourceWithStreamingResponse

        return AsyncBatterydetailsResourceWithStreamingResponse(self._client.batterydetails)

    @cached_property
    def beam(self) -> beam.AsyncBeamResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam import AsyncBeamResourceWithStreamingResponse

        return AsyncBeamResourceWithStreamingResponse(self._client.beam)

    @cached_property
    def beam_contours(self) -> beam_contours.AsyncBeamContoursResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of satellite antenna beams, and querying of beam contours and service areas.   Beam contours are the geographic representation of the relative gain levels of beam power off of the maximum gain boresight points.  Similarly, service areas are the geographic footprints of the areas served by a particular beam, and may be made up of multiple service regions.  Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.beam_contours import AsyncBeamContoursResourceWithStreamingResponse

        return AsyncBeamContoursResourceWithStreamingResponse(self._client.beam_contours)

    @cached_property
    def buses(self) -> buses.AsyncBusesResourceWithStreamingResponse:
        """Services for querying and manipulation of satellite buses.

        A bus is the physical and software infrastructure backbone to which on-orbit satellite payloads are attached for power, control, and other support functions.
        """
        from .resources.buses import AsyncBusesResourceWithStreamingResponse

        return AsyncBusesResourceWithStreamingResponse(self._client.buses)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.channels import AsyncChannelsResourceWithStreamingResponse

        return AsyncChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def closelyspacedobjects(self) -> closelyspacedobjects.AsyncCloselyspacedobjectsResourceWithStreamingResponse:
        """
        This collection of services provides operations for manipulating and querying of closely spaced objects (on orbit) operations including docking, rendezvous, proximity and reporting of payload zone engagements observed and characterized over a period of time.
        """
        from .resources.closelyspacedobjects import AsyncCloselyspacedobjectsResourceWithStreamingResponse

        return AsyncCloselyspacedobjectsResourceWithStreamingResponse(self._client.closelyspacedobjects)

    @cached_property
    def collect_requests(self) -> collect_requests.AsyncCollectRequestsResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_requests import AsyncCollectRequestsResourceWithStreamingResponse

        return AsyncCollectRequestsResourceWithStreamingResponse(self._client.collect_requests)

    @cached_property
    def collect_responses(self) -> collect_responses.AsyncCollectResponsesResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.collect_responses import AsyncCollectResponsesResourceWithStreamingResponse

        return AsyncCollectResponsesResourceWithStreamingResponse(self._client.collect_responses)

    @cached_property
    def comm(self) -> comm.AsyncCommResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.comm import AsyncCommResourceWithStreamingResponse

        return AsyncCommResourceWithStreamingResponse(self._client.comm)

    @cached_property
    def conjunctions(self) -> conjunctions.AsyncConjunctionsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of conjunctions.
        """
        from .resources.conjunctions import AsyncConjunctionsResourceWithStreamingResponse

        return AsyncConjunctionsResourceWithStreamingResponse(self._client.conjunctions)

    @cached_property
    def cots(self) -> cots.AsyncCotsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.cots import AsyncCotsResourceWithStreamingResponse

        return AsyncCotsResourceWithStreamingResponse(self._client.cots)

    @cached_property
    def countries(self) -> countries.AsyncCountriesResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.countries import AsyncCountriesResourceWithStreamingResponse

        return AsyncCountriesResourceWithStreamingResponse(self._client.countries)

    @cached_property
    def crew(self) -> crew.AsyncCrewResourceWithStreamingResponse:
        """These services provide operations for posting and querying crew data.

        Crew data contains information about its members and their assignments.
        """
        from .resources.crew import AsyncCrewResourceWithStreamingResponse

        return AsyncCrewResourceWithStreamingResponse(self._client.crew)

    @cached_property
    def deconflictset(self) -> deconflictset.AsyncDeconflictsetResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.deconflictset import AsyncDeconflictsetResourceWithStreamingResponse

        return AsyncDeconflictsetResourceWithStreamingResponse(self._client.deconflictset)

    @cached_property
    def diff_of_arrival(self) -> diff_of_arrival.AsyncDiffOfArrivalResourceWithStreamingResponse:
        """
        These services provide operations for querying and manipulation of Signal time and frequency difference of arrival (TDOA/FDOA) information obtained by using passive RF based sensor phenomenologies and sensor triangulation. The J2000 coordinate frame is the preferred frame for all observations, but in some cases observations may be in another frame depending on the provider.
        """
        from .resources.diff_of_arrival import AsyncDiffOfArrivalResourceWithStreamingResponse

        return AsyncDiffOfArrivalResourceWithStreamingResponse(self._client.diff_of_arrival)

    @cached_property
    def diplomatic_clearance(self) -> diplomatic_clearance.AsyncDiplomaticClearanceResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.diplomatic_clearance import AsyncDiplomaticClearanceResourceWithStreamingResponse

        return AsyncDiplomaticClearanceResourceWithStreamingResponse(self._client.diplomatic_clearance)

    @cached_property
    def drift_history(self) -> drift_history.AsyncDriftHistoryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.drift_history import AsyncDriftHistoryResourceWithStreamingResponse

        return AsyncDriftHistoryResourceWithStreamingResponse(self._client.drift_history)

    @cached_property
    def dropzone(self) -> dropzone.AsyncDropzoneResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.dropzone import AsyncDropzoneResourceWithStreamingResponse

        return AsyncDropzoneResourceWithStreamingResponse(self._client.dropzone)

    @cached_property
    def ecpedr(self) -> ecpedr.AsyncEcpedrResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.ecpedr import AsyncEcpedrResourceWithStreamingResponse

        return AsyncEcpedrResourceWithStreamingResponse(self._client.ecpedr)

    @cached_property
    def effect_requests(self) -> effect_requests.AsyncEffectRequestsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_requests import AsyncEffectRequestsResourceWithStreamingResponse

        return AsyncEffectRequestsResourceWithStreamingResponse(self._client.effect_requests)

    @cached_property
    def effect_responses(self) -> effect_responses.AsyncEffectResponsesResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.effect_responses import AsyncEffectResponsesResourceWithStreamingResponse

        return AsyncEffectResponsesResourceWithStreamingResponse(self._client.effect_responses)

    @cached_property
    def elsets(self) -> elsets.AsyncElsetsResourceWithStreamingResponse:
        """
        These services provide operations for querying and manipulation of element set data describing orbital characteristics of on-orbit objects. An element set is a collection of parameters that are used, along with an orbit propagator, to predict the motion of a satellite. The element set, or elset for short, consists of identification data, the classical elements and drag parameters.
        """
        from .resources.elsets import AsyncElsetsResourceWithStreamingResponse

        return AsyncElsetsResourceWithStreamingResponse(self._client.elsets)

    @cached_property
    def emireport(self) -> emireport.AsyncEmireportResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emireport import AsyncEmireportResourceWithStreamingResponse

        return AsyncEmireportResourceWithStreamingResponse(self._client.emireport)

    @cached_property
    def emitter_geolocation(self) -> emitter_geolocation.AsyncEmitterGeolocationResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.emitter_geolocation import AsyncEmitterGeolocationResourceWithStreamingResponse

        return AsyncEmitterGeolocationResourceWithStreamingResponse(self._client.emitter_geolocation)

    @cached_property
    def engine_details(self) -> engine_details.AsyncEngineDetailsResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engine_details import AsyncEngineDetailsResourceWithStreamingResponse

        return AsyncEngineDetailsResourceWithStreamingResponse(self._client.engine_details)

    @cached_property
    def engines(self) -> engines.AsyncEnginesResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.engines import AsyncEnginesResourceWithStreamingResponse

        return AsyncEnginesResourceWithStreamingResponse(self._client.engines)

    @cached_property
    def entities(self) -> entities.AsyncEntitiesResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.entities import AsyncEntitiesResourceWithStreamingResponse

        return AsyncEntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def eop(self) -> eop.AsyncEopResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.eop import AsyncEopResourceWithStreamingResponse

        return AsyncEopResourceWithStreamingResponse(self._client.eop)

    @cached_property
    def ephemeris(self) -> ephemeris.AsyncEphemerisResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris import AsyncEphemerisResourceWithStreamingResponse

        return AsyncEphemerisResourceWithStreamingResponse(self._client.ephemeris)

    @cached_property
    def ephemeris_sets(self) -> ephemeris_sets.AsyncEphemerisSetsResourceWithStreamingResponse:
        """
        These services provide operations for the posting and querying of satellite Ephemeris Point data. Each point contains a position and velocity vector and optionally, an acceleration vector and/or covariance matrix at a specified time. ECI J2K is the preferred reference frame for ephemeris and covariance, however, several user specified reference frames are accommodated. The EphemerisSet ID (esId) identifies the 'EphemerisSet' record which contains details of the underlying data and models used in the generation of the ephemeris as well as a collection of ephemeris points. Points must be retrieved by first identifying a desired EphemerisSet and pulling its points by that EphemerisSet 'esId'.
        """
        from .resources.ephemeris_sets import AsyncEphemerisSetsResourceWithStreamingResponse

        return AsyncEphemerisSetsResourceWithStreamingResponse(self._client.ephemeris_sets)

    @cached_property
    def equipment(self) -> equipment.AsyncEquipmentResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment import AsyncEquipmentResourceWithStreamingResponse

        return AsyncEquipmentResourceWithStreamingResponse(self._client.equipment)

    @cached_property
    def equipment_remarks(self) -> equipment_remarks.AsyncEquipmentRemarksResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of equipment related data.
        """
        from .resources.equipment_remarks import AsyncEquipmentRemarksResourceWithStreamingResponse

        return AsyncEquipmentRemarksResourceWithStreamingResponse(self._client.equipment_remarks)

    @cached_property
    def evac(self) -> evac.AsyncEvacResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.evac import AsyncEvacResourceWithStreamingResponse

        return AsyncEvacResourceWithStreamingResponse(self._client.evac)

    @cached_property
    def event_evolution(self) -> event_evolution.AsyncEventEvolutionResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.event_evolution import AsyncEventEvolutionResourceWithStreamingResponse

        return AsyncEventEvolutionResourceWithStreamingResponse(self._client.event_evolution)

    @cached_property
    def feature_assessment(self) -> feature_assessment.AsyncFeatureAssessmentResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.feature_assessment import AsyncFeatureAssessmentResourceWithStreamingResponse

        return AsyncFeatureAssessmentResourceWithStreamingResponse(self._client.feature_assessment)

    @cached_property
    def flightplan(self) -> flightplan.AsyncFlightplanResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.flightplan import AsyncFlightplanResourceWithStreamingResponse

        return AsyncFlightplanResourceWithStreamingResponse(self._client.flightplan)

    @cached_property
    def geo_status(self) -> geo_status.AsyncGeoStatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.geo_status import AsyncGeoStatusResourceWithStreamingResponse

        return AsyncGeoStatusResourceWithStreamingResponse(self._client.geo_status)

    @cached_property
    def global_atmospheric_model(
        self,
    ) -> global_atmospheric_model.AsyncGlobalAtmosphericModelResourceWithStreamingResponse:
        """
        Models and Simulations is a collection of services that allow consumers to interact with data products representing independent models of various phenomenon, artificial intelligence models and predictions, or of mathematical parameters meant to feed mod and sim tools to produce estimates of environmental entities such as atmospheric models and heat maps.
        """
        from .resources.global_atmospheric_model import AsyncGlobalAtmosphericModelResourceWithStreamingResponse

        return AsyncGlobalAtmosphericModelResourceWithStreamingResponse(self._client.global_atmospheric_model)

    @cached_property
    def gnss_observations(self) -> gnss_observations.AsyncGnssObservationsResourceWithStreamingResponse:
        from .resources.gnss_observations import AsyncGnssObservationsResourceWithStreamingResponse

        return AsyncGnssObservationsResourceWithStreamingResponse(self._client.gnss_observations)

    @cached_property
    def gnss_observationset(self) -> gnss_observationset.AsyncGnssObservationsetResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_observationset import AsyncGnssObservationsetResourceWithStreamingResponse

        return AsyncGnssObservationsetResourceWithStreamingResponse(self._client.gnss_observationset)

    @cached_property
    def gnss_raw_if(self) -> gnss_raw_if.AsyncGnssRawIfResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.gnss_raw_if import AsyncGnssRawIfResourceWithStreamingResponse

        return AsyncGnssRawIfResourceWithStreamingResponse(self._client.gnss_raw_if)

    @cached_property
    def ground_imagery(self) -> ground_imagery.AsyncGroundImageryResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of ground imagery of terrestrial regions from on-orbit, air, and other sensors. Includes metadata on the image (time, region, source, etc) as well as binary content (typically GeoTIFF). Binary content must be downloaded individually by ID using the 'getFile' operation. Well-Known Text (WKT) and GeoJSON formats are used for GIS representation and query support (see https://www.opengeospatial.org/standards/wkt-crs and https://geojson.org/ for more information on these formats).
        """
        from .resources.ground_imagery import AsyncGroundImageryResourceWithStreamingResponse

        return AsyncGroundImageryResourceWithStreamingResponse(self._client.ground_imagery)

    @cached_property
    def h3_geo(self) -> h3_geo.AsyncH3GeoResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo import AsyncH3GeoResourceWithStreamingResponse

        return AsyncH3GeoResourceWithStreamingResponse(self._client.h3_geo)

    @cached_property
    def h3_geo_hex_cell(self) -> h3_geo_hex_cell.AsyncH3GeoHexCellResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.h3_geo_hex_cell import AsyncH3GeoHexCellResourceWithStreamingResponse

        return AsyncH3GeoHexCellResourceWithStreamingResponse(self._client.h3_geo_hex_cell)

    @cached_property
    def hazard(self) -> hazard.AsyncHazardResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.hazard import AsyncHazardResourceWithStreamingResponse

        return AsyncHazardResourceWithStreamingResponse(self._client.hazard)

    @cached_property
    def iono_observations(self) -> iono_observations.AsyncIonoObservationsResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.iono_observations import AsyncIonoObservationsResourceWithStreamingResponse

        return AsyncIonoObservationsResourceWithStreamingResponse(self._client.iono_observations)

    @cached_property
    def ir(self) -> ir.AsyncIrResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.ir import AsyncIrResourceWithStreamingResponse

        return AsyncIrResourceWithStreamingResponse(self._client.ir)

    @cached_property
    def isr_collections(self) -> isr_collections.AsyncIsrCollectionsResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.isr_collections import AsyncIsrCollectionsResourceWithStreamingResponse

        return AsyncIsrCollectionsResourceWithStreamingResponse(self._client.isr_collections)

    @cached_property
    def item(self) -> item.AsyncItemResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item import AsyncItemResourceWithStreamingResponse

        return AsyncItemResourceWithStreamingResponse(self._client.item)

    @cached_property
    def item_trackings(self) -> item_trackings.AsyncItemTrackingsResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.item_trackings import AsyncItemTrackingsResourceWithStreamingResponse

        return AsyncItemTrackingsResourceWithStreamingResponse(self._client.item_trackings)

    @cached_property
    def laserdeconflictrequest(self) -> laserdeconflictrequest.AsyncLaserdeconflictrequestResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laserdeconflictrequest import AsyncLaserdeconflictrequestResourceWithStreamingResponse

        return AsyncLaserdeconflictrequestResourceWithStreamingResponse(self._client.laserdeconflictrequest)

    @cached_property
    def laseremitter(self) -> laseremitter.AsyncLaseremitterResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of laser related information to include the laser emitters, the laser deconflict requests, and laser deconflict responses.
        """
        from .resources.laseremitter import AsyncLaseremitterResourceWithStreamingResponse

        return AsyncLaseremitterResourceWithStreamingResponse(self._client.laseremitter)

    @cached_property
    def launch_detection(self) -> launch_detection.AsyncLaunchDetectionResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_detection import AsyncLaunchDetectionResourceWithStreamingResponse

        return AsyncLaunchDetectionResourceWithStreamingResponse(self._client.launch_detection)

    @cached_property
    def launch_event(self) -> launch_event.AsyncLaunchEventResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of LaunchEvent data. Launch Event data are known space launches, either future or historic records containing items such as the launch site, launch epoch, and object.
        """
        from .resources.launch_event import AsyncLaunchEventResourceWithStreamingResponse

        return AsyncLaunchEventResourceWithStreamingResponse(self._client.launch_event)

    @cached_property
    def launch_site(self) -> launch_site.AsyncLaunchSiteResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site import AsyncLaunchSiteResourceWithStreamingResponse

        return AsyncLaunchSiteResourceWithStreamingResponse(self._client.launch_site)

    @cached_property
    def launch_site_details(self) -> launch_site_details.AsyncLaunchSiteDetailsResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_site_details import AsyncLaunchSiteDetailsResourceWithStreamingResponse

        return AsyncLaunchSiteDetailsResourceWithStreamingResponse(self._client.launch_site_details)

    @cached_property
    def launch_vehicle(self) -> launch_vehicle.AsyncLaunchVehicleResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle import AsyncLaunchVehicleResourceWithStreamingResponse

        return AsyncLaunchVehicleResourceWithStreamingResponse(self._client.launch_vehicle)

    @cached_property
    def launch_vehicle_details(self) -> launch_vehicle_details.AsyncLaunchVehicleDetailsResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.launch_vehicle_details import AsyncLaunchVehicleDetailsResourceWithStreamingResponse

        return AsyncLaunchVehicleDetailsResourceWithStreamingResponse(self._client.launch_vehicle_details)

    @cached_property
    def link_status(self) -> link_status.AsyncLinkStatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.link_status import AsyncLinkStatusResourceWithStreamingResponse

        return AsyncLinkStatusResourceWithStreamingResponse(self._client.link_status)

    @cached_property
    def linkstatus(self) -> linkstatus.AsyncLinkstatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying tactical data links and link statuses of beams or a satellite constellation. Communication link statuses provide definitions and status such as, positional endpoints, where each endpoint may be associated with a specific beam or with a satellite constellation. Data links provide detailed instructions regarding the operational use of a tactical data link and interface coordination through various message formats.
        """
        from .resources.linkstatus import AsyncLinkstatusResourceWithStreamingResponse

        return AsyncLinkstatusResourceWithStreamingResponse(self._client.linkstatus)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.location import AsyncLocationResourceWithStreamingResponse

        return AsyncLocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def logistics_support(self) -> logistics_support.AsyncLogisticsSupportResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.logistics_support import AsyncLogisticsSupportResourceWithStreamingResponse

        return AsyncLogisticsSupportResourceWithStreamingResponse(self._client.logistics_support)

    @cached_property
    def maneuvers(self) -> maneuvers.AsyncManeuversResourceWithStreamingResponse:
        """
        This service provides operations for querying and manipulation of detected/possible/confirmed on-orbit maneuvers. The J2000 coordinate frame is the preferred frame for all maneuver data, but in some cases data may be in another frame depending on the provider. Check the Storefront 'Data Products' section under the 'Discover' tab for maneuver data provider information.
        """
        from .resources.maneuvers import AsyncManeuversResourceWithStreamingResponse

        return AsyncManeuversResourceWithStreamingResponse(self._client.maneuvers)

    @cached_property
    def manifold(self) -> manifold.AsyncManifoldResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifold import AsyncManifoldResourceWithStreamingResponse

        return AsyncManifoldResourceWithStreamingResponse(self._client.manifold)

    @cached_property
    def manifoldelset(self) -> manifoldelset.AsyncManifoldelsetResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.manifoldelset import AsyncManifoldelsetResourceWithStreamingResponse

        return AsyncManifoldelsetResourceWithStreamingResponse(self._client.manifoldelset)

    @cached_property
    def missile_tracks(self) -> missile_tracks.AsyncMissileTracksResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.missile_tracks import AsyncMissileTracksResourceWithStreamingResponse

        return AsyncMissileTracksResourceWithStreamingResponse(self._client.missile_tracks)

    @cached_property
    def mission_assignment(self) -> mission_assignment.AsyncMissionAssignmentResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of mission assignment objects. MissionAssignment is used by C2 JUs and, optionally, non-C2 JUs to assign missions, designate targets, and provide target information to non-C2 JU platforms. Provision is made for the non-C2 JU platforms to acknowledge the message through receipt/compliance action.
        """
        from .resources.mission_assignment import AsyncMissionAssignmentResourceWithStreamingResponse

        return AsyncMissionAssignmentResourceWithStreamingResponse(self._client.mission_assignment)

    @cached_property
    def mti(self) -> mti.AsyncMtiResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying Moving Target Indicator (MTI) STANAG 4607 data. Detailed MTI data supports activities such as targeting or less detailed data for applications such as situational awareness used/derived by exploitation systems.
        """
        from .resources.mti import AsyncMtiResourceWithStreamingResponse

        return AsyncMtiResourceWithStreamingResponse(self._client.mti)

    @cached_property
    def navigation(self) -> navigation.AsyncNavigationResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.navigation import AsyncNavigationResourceWithStreamingResponse

        return AsyncNavigationResourceWithStreamingResponse(self._client.navigation)

    @cached_property
    def navigational_obstruction(
        self,
    ) -> navigational_obstruction.AsyncNavigationalObstructionResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.navigational_obstruction import AsyncNavigationalObstructionResourceWithStreamingResponse

        return AsyncNavigationalObstructionResourceWithStreamingResponse(self._client.navigational_obstruction)

    @cached_property
    def notification(self) -> notification.AsyncNotificationResourceWithStreamingResponse:
        """
        A Notification Service allowing the broadcast of generic messages to the community. Users can send free-form messages, publish lists, and notify the community about events or alerts across various domains. Notifications and alerts are categorized by a 'msgType' field and are accessible via the UDL Secure Messaging API and REST API services.
        """
        from .resources.notification import AsyncNotificationResourceWithStreamingResponse

        return AsyncNotificationResourceWithStreamingResponse(self._client.notification)

    @cached_property
    def object_of_interest(self) -> object_of_interest.AsyncObjectOfInterestResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.object_of_interest import AsyncObjectOfInterestResourceWithStreamingResponse

        return AsyncObjectOfInterestResourceWithStreamingResponse(self._client.object_of_interest)

    @cached_property
    def observations(self) -> observations.AsyncObservationsResourceWithStreamingResponse:
        from .resources.observations import AsyncObservationsResourceWithStreamingResponse

        return AsyncObservationsResourceWithStreamingResponse(self._client.observations)

    @cached_property
    def onboardnavigation(self) -> onboardnavigation.AsyncOnboardnavigationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.onboardnavigation import AsyncOnboardnavigationResourceWithStreamingResponse

        return AsyncOnboardnavigationResourceWithStreamingResponse(self._client.onboardnavigation)

    @cached_property
    def onorbit(self) -> onorbit.AsyncOnorbitResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbit import AsyncOnorbitResourceWithStreamingResponse

        return AsyncOnorbitResourceWithStreamingResponse(self._client.onorbit)

    @cached_property
    def onorbitantenna(self) -> onorbitantenna.AsyncOnorbitantennaResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitantenna import AsyncOnorbitantennaResourceWithStreamingResponse

        return AsyncOnorbitantennaResourceWithStreamingResponse(self._client.onorbitantenna)

    @cached_property
    def onorbitbattery(self) -> onorbitbattery.AsyncOnorbitbatteryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitbattery import AsyncOnorbitbatteryResourceWithStreamingResponse

        return AsyncOnorbitbatteryResourceWithStreamingResponse(self._client.onorbitbattery)

    @cached_property
    def onorbitdetails(self) -> onorbitdetails.AsyncOnorbitdetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitdetails import AsyncOnorbitdetailsResourceWithStreamingResponse

        return AsyncOnorbitdetailsResourceWithStreamingResponse(self._client.onorbitdetails)

    @cached_property
    def onorbitevent(self) -> onorbitevent.AsyncOnorbiteventResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitevent import AsyncOnorbiteventResourceWithStreamingResponse

        return AsyncOnorbiteventResourceWithStreamingResponse(self._client.onorbitevent)

    @cached_property
    def onorbitlist(self) -> onorbitlist.AsyncOnorbitlistResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitlist import AsyncOnorbitlistResourceWithStreamingResponse

        return AsyncOnorbitlistResourceWithStreamingResponse(self._client.onorbitlist)

    @cached_property
    def onorbitsolararray(self) -> onorbitsolararray.AsyncOnorbitsolararrayResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitsolararray import AsyncOnorbitsolararrayResourceWithStreamingResponse

        return AsyncOnorbitsolararrayResourceWithStreamingResponse(self._client.onorbitsolararray)

    @cached_property
    def onorbitthruster(self) -> onorbitthruster.AsyncOnorbitthrusterResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthruster import AsyncOnorbitthrusterResourceWithStreamingResponse

        return AsyncOnorbitthrusterResourceWithStreamingResponse(self._client.onorbitthruster)

    @cached_property
    def onorbitthrusterstatus(self) -> onorbitthrusterstatus.AsyncOnorbitthrusterstatusResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.onorbitthrusterstatus import AsyncOnorbitthrusterstatusResourceWithStreamingResponse

        return AsyncOnorbitthrusterstatusResourceWithStreamingResponse(self._client.onorbitthrusterstatus)

    @cached_property
    def onorbitassessment(self) -> onorbitassessment.AsyncOnorbitassessmentResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.onorbitassessment import AsyncOnorbitassessmentResourceWithStreamingResponse

        return AsyncOnorbitassessmentResourceWithStreamingResponse(self._client.onorbitassessment)

    @cached_property
    def operatingunit(self) -> operatingunit.AsyncOperatingunitResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunit import AsyncOperatingunitResourceWithStreamingResponse

        return AsyncOperatingunitResourceWithStreamingResponse(self._client.operatingunit)

    @cached_property
    def operatingunitremark(self) -> operatingunitremark.AsyncOperatingunitremarkResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.operatingunitremark import AsyncOperatingunitremarkResourceWithStreamingResponse

        return AsyncOperatingunitremarkResourceWithStreamingResponse(self._client.operatingunitremark)

    @cached_property
    def orbitdetermination(self) -> orbitdetermination.AsyncOrbitdeterminationResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Orbit Determination (OD) data. Orbit Determination data contains algorithm results that describe General Perturbations or Special Perturbations orbital updates.
        """
        from .resources.orbitdetermination import AsyncOrbitdeterminationResourceWithStreamingResponse

        return AsyncOrbitdeterminationResourceWithStreamingResponse(self._client.orbitdetermination)

    @cached_property
    def orbittrack(self) -> orbittrack.AsyncOrbittrackResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.orbittrack import AsyncOrbittrackResourceWithStreamingResponse

        return AsyncOrbittrackResourceWithStreamingResponse(self._client.orbittrack)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organization import AsyncOrganizationResourceWithStreamingResponse

        return AsyncOrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def organizationdetails(self) -> organizationdetails.AsyncOrganizationdetailsResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.organizationdetails import AsyncOrganizationdetailsResourceWithStreamingResponse

        return AsyncOrganizationdetailsResourceWithStreamingResponse(self._client.organizationdetails)

    @cached_property
    def personnelrecovery(self) -> personnelrecovery.AsyncPersonnelrecoveryResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Mission Ops information.
        """
        from .resources.personnelrecovery import AsyncPersonnelrecoveryResourceWithStreamingResponse

        return AsyncPersonnelrecoveryResourceWithStreamingResponse(self._client.personnelrecovery)

    @cached_property
    def poi(self) -> poi.AsyncPoiResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.poi import AsyncPoiResourceWithStreamingResponse

        return AsyncPoiResourceWithStreamingResponse(self._client.poi)

    @cached_property
    def port(self) -> port.AsyncPortResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.port import AsyncPortResourceWithStreamingResponse

        return AsyncPortResourceWithStreamingResponse(self._client.port)

    @cached_property
    def report_and_activities(self) -> report_and_activities.AsyncReportAndActivitiesResourceWithStreamingResponse:
        from .resources.report_and_activities import AsyncReportAndActivitiesResourceWithStreamingResponse

        return AsyncReportAndActivitiesResourceWithStreamingResponse(self._client.report_and_activities)

    @cached_property
    def rf_band(self) -> rf_band.AsyncRfBandResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band import AsyncRfBandResourceWithStreamingResponse

        return AsyncRfBandResourceWithStreamingResponse(self._client.rf_band)

    @cached_property
    def rf_band_type(self) -> rf_band_type.AsyncRfBandTypeResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_band_type import AsyncRfBandTypeResourceWithStreamingResponse

        return AsyncRfBandTypeResourceWithStreamingResponse(self._client.rf_band_type)

    @cached_property
    def rf_emitter(self) -> rf_emitter.AsyncRfEmitterResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of RF related information to include RFEmitters which could potentially interfere with communications/operations of space related entities, and RFBands commonly used by various space related entities.
        """
        from .resources.rf_emitter import AsyncRfEmitterResourceWithStreamingResponse

        return AsyncRfEmitterResourceWithStreamingResponse(self._client.rf_emitter)

    @cached_property
    def route_stats(self) -> route_stats.AsyncRouteStatsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.route_stats import AsyncRouteStatsResourceWithStreamingResponse

        return AsyncRouteStatsResourceWithStreamingResponse(self._client.route_stats)

    @cached_property
    def sar_observation(self) -> sar_observation.AsyncSarObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.sar_observation import AsyncSarObservationResourceWithStreamingResponse

        return AsyncSarObservationResourceWithStreamingResponse(self._client.sar_observation)

    @cached_property
    def scientific(self) -> scientific.AsyncScientificResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.scientific import AsyncScientificResourceWithStreamingResponse

        return AsyncScientificResourceWithStreamingResponse(self._client.scientific)

    @cached_property
    def scs(self) -> scs.AsyncScsResourceWithStreamingResponse:
        from .resources.scs import AsyncScsResourceWithStreamingResponse

        return AsyncScsResourceWithStreamingResponse(self._client.scs)

    @cached_property
    def secure_messaging(self) -> secure_messaging.AsyncSecureMessagingResourceWithStreamingResponse:
        """
        Secure Messaging is based on Apache Kafka which is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. Kafka provides a unified, high-throughput, low-latency platform for handling real-time data feeds.  All messaging is secured; consumers will not receive messages unless authorized to do so. J2000 is the preferred coordinate frame for all observations, but in some cases observations may be in another frame depending on the provider. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.secure_messaging import AsyncSecureMessagingResourceWithStreamingResponse

        return AsyncSecureMessagingResourceWithStreamingResponse(self._client.secure_messaging)

    @cached_property
    def sensor(self) -> sensor.AsyncSensorResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor import AsyncSensorResourceWithStreamingResponse

        return AsyncSensorResourceWithStreamingResponse(self._client.sensor)

    @cached_property
    def sensor_stating(self) -> sensor_stating.AsyncSensorStatingResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_stating import AsyncSensorStatingResourceWithStreamingResponse

        return AsyncSensorStatingResourceWithStreamingResponse(self._client.sensor_stating)

    @cached_property
    def sensor_maintenance(self) -> sensor_maintenance.AsyncSensorMaintenanceResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_maintenance import AsyncSensorMaintenanceResourceWithStreamingResponse

        return AsyncSensorMaintenanceResourceWithStreamingResponse(self._client.sensor_maintenance)

    @cached_property
    def sensor_observation_type(
        self,
    ) -> sensor_observation_type.AsyncSensorObservationTypeResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_observation_type import AsyncSensorObservationTypeResourceWithStreamingResponse

        return AsyncSensorObservationTypeResourceWithStreamingResponse(self._client.sensor_observation_type)

    @cached_property
    def sensor_plan(self) -> sensor_plan.AsyncSensorPlanResourceWithStreamingResponse:
        """These services provide operations for posting and querying Sensor Tasking data."""
        from .resources.sensor_plan import AsyncSensorPlanResourceWithStreamingResponse

        return AsyncSensorPlanResourceWithStreamingResponse(self._client.sensor_plan)

    @cached_property
    def sensor_type(self) -> sensor_type.AsyncSensorTypeResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.sensor_type import AsyncSensorTypeResourceWithStreamingResponse

        return AsyncSensorTypeResourceWithStreamingResponse(self._client.sensor_type)

    @cached_property
    def sera_data_comm_details(self) -> sera_data_comm_details.AsyncSeraDataCommDetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.sera_data_comm_details import AsyncSeraDataCommDetailsResourceWithStreamingResponse

        return AsyncSeraDataCommDetailsResourceWithStreamingResponse(self._client.sera_data_comm_details)

    @cached_property
    def sera_data_early_warning(self) -> sera_data_early_warning.AsyncSeraDataEarlyWarningResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_early_warning import AsyncSeraDataEarlyWarningResourceWithStreamingResponse

        return AsyncSeraDataEarlyWarningResourceWithStreamingResponse(self._client.sera_data_early_warning)

    @cached_property
    def sera_data_navigation(self) -> sera_data_navigation.AsyncSeraDataNavigationResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit payloads.
        """
        from .resources.sera_data_navigation import AsyncSeraDataNavigationResourceWithStreamingResponse

        return AsyncSeraDataNavigationResourceWithStreamingResponse(self._client.sera_data_navigation)

    @cached_property
    def seradata_optical_payload(
        self,
    ) -> seradata_optical_payload.AsyncSeradataOpticalPayloadResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_optical_payload import AsyncSeradataOpticalPayloadResourceWithStreamingResponse

        return AsyncSeradataOpticalPayloadResourceWithStreamingResponse(self._client.seradata_optical_payload)

    @cached_property
    def seradata_radar_payload(self) -> seradata_radar_payload.AsyncSeradataRadarPayloadResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_radar_payload import AsyncSeradataRadarPayloadResourceWithStreamingResponse

        return AsyncSeradataRadarPayloadResourceWithStreamingResponse(self._client.seradata_radar_payload)

    @cached_property
    def seradata_sigint_payload(
        self,
    ) -> seradata_sigint_payload.AsyncSeradataSigintPayloadResourceWithStreamingResponse:
        """This service provides operations for querying and manipulation of sensor data.

        Sensors are terrestrial or on-orbit equipment capable of taking measurements or 'observations' of on-orbit objects via several phenomenologies such as Electro-Optical (EO), Radar, and Radio Frequency (RF). This collection of operations includes 'SensorMaintenance' schedules which define known/planned future maintenance and associated operational impact of sensors as well as 'SensorCalibration' records which contains data about a sensor's overall accuracy and is used to adjust sensor settings.
        """
        from .resources.seradata_sigint_payload import AsyncSeradataSigintPayloadResourceWithStreamingResponse

        return AsyncSeradataSigintPayloadResourceWithStreamingResponse(self._client.seradata_sigint_payload)

    @cached_property
    def seradata_spacecraft_details(
        self,
    ) -> seradata_spacecraft_details.AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.seradata_spacecraft_details import AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse

        return AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse(self._client.seradata_spacecraft_details)

    @cached_property
    def sgi(self) -> sgi.AsyncSgiResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of space weather/solar, geomagnetic, and radiation belt index data.
        """
        from .resources.sgi import AsyncSgiResourceWithStreamingResponse

        return AsyncSgiResourceWithStreamingResponse(self._client.sgi)

    @cached_property
    def sigact(self) -> sigact.AsyncSigactResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of Report and Activity information. This information includes analytic reports, significant events, route statistics, EMI Reports, and other georeferenced reports and activities.
        """
        from .resources.sigact import AsyncSigactResourceWithStreamingResponse

        return AsyncSigactResourceWithStreamingResponse(self._client.sigact)

    @cached_property
    def site(self) -> site.AsyncSiteResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site import AsyncSiteResourceWithStreamingResponse

        return AsyncSiteResourceWithStreamingResponse(self._client.site)

    @cached_property
    def site_remark(self) -> site_remark.AsyncSiteRemarkResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_remark import AsyncSiteRemarkResourceWithStreamingResponse

        return AsyncSiteRemarkResourceWithStreamingResponse(self._client.site_remark)

    @cached_property
    def site_status(self) -> site_status.AsyncSiteStatusResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.site_status import AsyncSiteStatusResourceWithStreamingResponse

        return AsyncSiteStatusResourceWithStreamingResponse(self._client.site_status)

    @cached_property
    def sky_imagery(self) -> sky_imagery.AsyncSkyImageryResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of sky imagery data. Sky imagery is ground or space based telescope imagery of RSO's and includes metadata on the image (time, source, etc) as well as binary image content (e.g. FITS, EOSSA, EOCHIP, MP4). Binary content must be downloaded individually by ID using the 'getFile' operation.
        """
        from .resources.sky_imagery import AsyncSkyImageryResourceWithStreamingResponse

        return AsyncSkyImageryResourceWithStreamingResponse(self._client.sky_imagery)

    @cached_property
    def soi_observation_set(self) -> soi_observation_set.AsyncSoiObservationSetResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.soi_observation_set import AsyncSoiObservationSetResourceWithStreamingResponse

        return AsyncSoiObservationSetResourceWithStreamingResponse(self._client.soi_observation_set)

    @cached_property
    def solar_array(self) -> solar_array.AsyncSolarArrayResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array import AsyncSolarArrayResourceWithStreamingResponse

        return AsyncSolarArrayResourceWithStreamingResponse(self._client.solar_array)

    @cached_property
    def solar_array_details(self) -> solar_array_details.AsyncSolarArrayDetailsResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit objects of interest, their components, and various lists and status of those objects.
        """
        from .resources.solar_array_details import AsyncSolarArrayDetailsResourceWithStreamingResponse

        return AsyncSolarArrayDetailsResourceWithStreamingResponse(self._client.solar_array_details)

    @cached_property
    def sortie_ppr(self) -> sortie_ppr.AsyncSortiePprResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.sortie_ppr import AsyncSortiePprResourceWithStreamingResponse

        return AsyncSortiePprResourceWithStreamingResponse(self._client.sortie_ppr)

    @cached_property
    def space_env_observation(self) -> space_env_observation.AsyncSpaceEnvObservationResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.space_env_observation import AsyncSpaceEnvObservationResourceWithStreamingResponse

        return AsyncSpaceEnvObservationResourceWithStreamingResponse(self._client.space_env_observation)

    @cached_property
    def stage(self) -> stage.AsyncStageResourceWithStreamingResponse:
        """
        Collection of launch related services which provide operations for querying and manipulation of launch site data and detailed information on launch vehicles including engines, stages, and manufacturers. Sites, engines, and stages can each have multiple 'detail' records which may be compiled by different sources.
        """
        from .resources.stage import AsyncStageResourceWithStreamingResponse

        return AsyncStageResourceWithStreamingResponse(self._client.stage)

    @cached_property
    def star_catalog(self) -> star_catalog.AsyncStarCatalogResourceWithStreamingResponse:
        """These services provide operations for posting and querying Star Catalog data.

        The Star Catalog model is a representation of astronomical data and photometric data for stars. Astronomical data includes positional information, proper motions, parallaxes and their respective uncertainties. Photometric data contains optical and near-infrared magnitudes, and their uncertainties across multiple bandpasses. Note: Multiple source catalogs may contribute to a single record.
        """
        from .resources.star_catalog import AsyncStarCatalogResourceWithStreamingResponse

        return AsyncStarCatalogResourceWithStreamingResponse(self._client.star_catalog)

    @cached_property
    def state_vector(self) -> state_vector.AsyncStateVectorResourceWithStreamingResponse:
        """
        This service provides operations for querying and manipulation of state vectors for On-orbit objects. State vectors are cartesian vectors of position (r) and velocity (v) that together with their time (epoch) (t) uniquely determine the trajectory of the orbiting body in space. J2000 is the preferred coordinate frame for all state vector positions/velocities in UDL, but in some cases data may be in another frame depending on the provider and/or datatype. Please see the 'Discover' tab in the storefront to confirm coordinate frames by data provider.
        """
        from .resources.state_vector import AsyncStateVectorResourceWithStreamingResponse

        return AsyncStateVectorResourceWithStreamingResponse(self._client.state_vector)

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.status import AsyncStatusResourceWithStreamingResponse

        return AsyncStatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def substatus(self) -> substatus.AsyncSubstatusResourceWithStreamingResponse:
        """
        Service operations for querying and manipulation of miscellaneous supporting data such as countries (which can represent countries, multi-national consortiums, and international organizations), data owners, locations, entities, organizations, etc.
        """
        from .resources.substatus import AsyncSubstatusResourceWithStreamingResponse

        return AsyncSubstatusResourceWithStreamingResponse(self._client.substatus)

    @cached_property
    def supporting_data(self) -> supporting_data.AsyncSupportingDataResourceWithStreamingResponse:
        from .resources.supporting_data import AsyncSupportingDataResourceWithStreamingResponse

        return AsyncSupportingDataResourceWithStreamingResponse(self._client.supporting_data)

    @cached_property
    def surface(self) -> surface.AsyncSurfaceResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface import AsyncSurfaceResourceWithStreamingResponse

        return AsyncSurfaceResourceWithStreamingResponse(self._client.surface)

    @cached_property
    def surface_obstruction(self) -> surface_obstruction.AsyncSurfaceObstructionResourceWithStreamingResponse:
        """
        This collection of services provide operations for manipulating and querying of various site related data, including site status, site operations, and site type-specific records.
        """
        from .resources.surface_obstruction import AsyncSurfaceObstructionResourceWithStreamingResponse

        return AsyncSurfaceObstructionResourceWithStreamingResponse(self._client.surface_obstruction)

    @cached_property
    def swir(self) -> swir.AsyncSwirResourceWithStreamingResponse:
        """
        This collection of services provides operations for querying and manipulation of electro-optical (EO), radar, radio frequency (RF), Global Navigation Satellite Systems (GNSS), Ionospheric (IONO), Infrared (SWIR), and Space Environment observation data. The J2000 coordinate frame is the preferred frame for all observations, as applicable, but in some cases observations may be in an alternate frame depending on the provider and/or datatype.
        """
        from .resources.swir import AsyncSwirResourceWithStreamingResponse

        return AsyncSwirResourceWithStreamingResponse(self._client.swir)

    @cached_property
    def tai_utc(self) -> tai_utc.AsyncTaiUtcResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of earth orientation parameter (EOP) data. Earth Orientation Parameters (EOP) are produced by the IERS (International Earth Rotation and Reference Systems Service). Earth Orientation Parameters describe the irregularities of the earth's rotation. Technically, they are the parameters which provide the rotation of the ITRS (International Terrestrial Reference System) to the ICRS (International Celestial Reference System) as a function of time. Universal time -- Universal time (UT1) is the time of the earth clock, which performs one revolution in about 24h. It is practically proportional to the sidereal time. The excess revolution time is called length of day (LOD). Coordinates of the pole -- x and y are the coordinates of the Celestial Ephemeris Pole (CEP) relative to the IRP, the IERS Reference Pole. The CEP differs from the instantaneous rotation axis by quasi-diurnal terms with amplitudes under 0.01" (see Seidelmann, 1982). The x-axis is in the direction of the ITRF zero-meridian; the y-axis is in the direction 90 degrees West longitude. Celestial pole offsets -- Celestial pole offsets are described in the IAU Precession and Nutation models. The observed differences with respect to the conventional celestial pole position defined by the models are monitored and reported by the IERS. IERS Bulletins A and B provide current information on the Earth's orientation in the IERS Reference System. This includes Universal Time, coordinates of the terrestrial pole, and celestial pole offsets. Bulletin A gives an advanced solution updated weekly; the standard solution is given monthly in Bulletin B. Fields suffixed with ''B'' are Bulletin B values. All solutions are continuous within their respective uncertainties. Bulletin A is issued by the IERS Rapid Service/Prediction Centre at the U.S. Naval Observatory, Washington, DC and Bulletin B is issued by the IERS Earth Orientation Centre at the Paris Observatory. IERS Bulletin A reports the latest determinations for polar motion, UT1-UTC, and nutation offsets at daily intervals based on a combination of contributed analysis results using data from Very Long Baseline Interferometry (VLBI), Satellite Laser Ranging (SLR), Global Positioning System (GPS) satellites, and Lunar Laser Ranging (LLR). Predictions for variations a year into the future are also provided. Meteorological predictions of variations in Atmospheric Angular Momentum (AAM) are used to aid in the prediction of near-term UT1-UTC changes. This publication is prepared by the IERS Rapid Service/Prediction Center.
        """
        from .resources.tai_utc import AsyncTaiUtcResourceWithStreamingResponse

        return AsyncTaiUtcResourceWithStreamingResponse(self._client.tai_utc)

    @cached_property
    def tdoa_fdoa(self) -> tdoa_fdoa.AsyncTdoaFdoaResourceWithStreamingResponse:
        from .resources.tdoa_fdoa import AsyncTdoaFdoaResourceWithStreamingResponse

        return AsyncTdoaFdoaResourceWithStreamingResponse(self._client.tdoa_fdoa)

    @cached_property
    def track(self) -> track.AsyncTrackResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track import AsyncTrackResourceWithStreamingResponse

        return AsyncTrackResourceWithStreamingResponse(self._client.track)

    @cached_property
    def track_details(self) -> track_details.AsyncTrackDetailsResourceWithStreamingResponse:
        """
        These services provide operations for posting and querying of air, space, and ground 'tracks'. A track is a position and optionally a heading/velocity of an object at a particular timestamp.
        """
        from .resources.track_details import AsyncTrackDetailsResourceWithStreamingResponse

        return AsyncTrackDetailsResourceWithStreamingResponse(self._client.track_details)

    @cached_property
    def track_route(self) -> track_route.AsyncTrackRouteResourceWithStreamingResponse:
        """
        These services provide operations for manipulating and querying Aircraft Sortie, Aircraft Mission, Item Tracking, Flight Plan, Air Event, Sortie Prior Permission Required (PPR), Diplomatic Clearance, Diplomatic Clearance Country, Airspace Control Order, Air Tasking Order, Navigational Obstruction, Logistics Support, Track Route, Air Load Plan, and Aviation Risk Management data. Aircraft Sortie information contains static and dynamic aircraft assignments, departure and arrival times, and remarks. Aircraft Mission information contains static data for mission planning to include assigned aircraft and crews, cargo pickup and dropoff locations, unique identifiers, and prioritization. Item Tracking information contains data for tracking an item from its origin to destination and how it may be configured during transport. Flight Plan information contains schedule and route details. Air Event provides information concerning various aerial events such as fuel transfer and air drops, as well as the associated aircraft involved. Sortie PPR information contains details on operational access to a runway, taxiway, or airport service. Diplomatic Clearance information contains details on the issuance and coordination of aircraft clearance requests. Diplomatic Clearance Country provides information such as entry/exit points, requirements, and points of contact for countries diplomatic clearances are being created for. Airspace Control Order provides information concerning the allocation, restriction, and deconfliction of airspace. Air Tasking Order information contains details on the coordination of air missions and their tasks, resources, and timelines. Navigational Obstruction provides the locations, characteristics, and boundaries of obstacles and structures that can restrict or interfere with navigation. Logistics Support contains information regarding the transport and maintenance of resources and equipment to sustain air operations. Track Route information defines specific flight paths used by aircraft during the transport of fuel and other resources. Air Load Plan information provides mission actuals concerning the loading and air transport of cargo and passengers. Aviation Risk Management information help aid in mission planning by accounting for factors such as mission complexity and crew fatigue.
        """
        from .resources.track_route import AsyncTrackRouteResourceWithStreamingResponse

        return AsyncTrackRouteResourceWithStreamingResponse(self._client.track_route)

    @cached_property
    def transponder(self) -> transponder.AsyncTransponderResourceWithStreamingResponse:
        """
        These services provide operations for manipulation and querying of on-orbit communications payloads (Comm), including supporting data such as transponders and channels, etc.
        """
        from .resources.transponder import AsyncTransponderResourceWithStreamingResponse

        return AsyncTransponderResourceWithStreamingResponse(self._client.transponder)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def vessel(self) -> vessel.AsyncVesselResourceWithStreamingResponse:
        """
        This service provides operations for manipulation and querying of maritime Vessel and Vessel Status data. Vessel contains the static data of the specific vessel: mmsi, cruise speed, max speed, etc.
        """
        from .resources.vessel import AsyncVesselResourceWithStreamingResponse

        return AsyncVesselResourceWithStreamingResponse(self._client.vessel)

    @cached_property
    def video(self) -> video.AsyncVideoResourceWithStreamingResponse:
        """This collection of services provides operations for video streaming."""
        from .resources.video import AsyncVideoResourceWithStreamingResponse

        return AsyncVideoResourceWithStreamingResponse(self._client.video)

    @cached_property
    def weather_data(self) -> weather_data.AsyncWeatherDataResourceWithStreamingResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_data import AsyncWeatherDataResourceWithStreamingResponse

        return AsyncWeatherDataResourceWithStreamingResponse(self._client.weather_data)

    @cached_property
    def weather_report(self) -> weather_report.AsyncWeatherReportResourceWithStreamingResponse:
        """
        These services provide for posting and querying terrestrial weather conditions over a target area or region and raw sensor data used to produce condition reports. Weather Reports describe current weather conditions over a target point or region to include general temperatures, pressures, and moisture accumulation, as well as navigational considerations such as altimeter settings, visibility, wind speeds, and cloud heights etc. Weather Data contains algorithmic parameters and dynamic, raw measurements collected by individual sensors such as signal power, noise level, etc., which are generally processed across multiple sensors to produce weather reports.
        """
        from .resources.weather_report import AsyncWeatherReportResourceWithStreamingResponse

        return AsyncWeatherReportResourceWithStreamingResponse(self._client.weather_report)


Client = Unifieddatalibrary

AsyncClient = AsyncUnifieddatalibrary
