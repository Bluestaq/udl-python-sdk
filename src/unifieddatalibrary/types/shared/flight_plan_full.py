# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FlightPlanFull",
    "AirRefuelEvent",
    "FlightPlanMessage",
    "FlightPlanPointGroup",
    "FlightPlanPointGroupFlightPlanPoint",
    "FlightPlanWaypoint",
]


class AirRefuelEvent(BaseModel):
    ar_degrade: Optional[float] = FieldInfo(alias="arDegrade", default=None)
    """
    Additional degrade for air refueling, cumulative with fuelDegrade field percent.
    """

    ar_exchanged_fuel: Optional[float] = FieldInfo(alias="arExchangedFuel", default=None)
    """
    Fuel onloaded (use positive numbers) or fuel offloaded (use negative numbers) in
    pounds.
    """

    ar_num: Optional[int] = FieldInfo(alias="arNum", default=None)
    """The number of this air refueling event within the flight plan."""

    divert_fuel: Optional[float] = FieldInfo(alias="divertFuel", default=None)
    """
    Fuel required to fly from air refueling exit point to air refueling divert
    alternate airfield in pounds.
    """

    exit_fuel: Optional[float] = FieldInfo(alias="exitFuel", default=None)
    """Fuel remaining at the air refueling exit in pounds."""


class FlightPlanMessage(BaseModel):
    msg_text: Optional[str] = FieldInfo(alias="msgText", default=None)
    """The text of the message."""

    route_path: Optional[str] = FieldInfo(alias="routePath", default=None)
    """The flight path that generated the message (PRIMARY, ALTERNATE, etc.)."""

    severity: Optional[str] = None
    """The severity of the message."""

    wp_num: Optional[str] = FieldInfo(alias="wpNum", default=None)
    """
    The waypoint number for which the message was generated, or enter "PLAN" for a
    message impacting the entire route.
    """


class FlightPlanPointGroupFlightPlanPoint(BaseModel):
    fpp_eta: Optional[datetime] = FieldInfo(alias="fppEta", default=None)
    """
    Estimated Time of Arrival (ETA) at this point in ISO 8601 UTC format, with
    millisecond precision.
    """

    fpp_lat: Optional[float] = FieldInfo(alias="fppLat", default=None)
    """WGS84 latitude of the point location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    fpp_lon: Optional[float] = FieldInfo(alias="fppLon", default=None)
    """WGS84 longitude of the point location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    fpp_req_fuel: Optional[float] = FieldInfo(alias="fppReqFuel", default=None)
    """
    Fuel required at this point to execute an Equal Time Point (ETP) or Extended
    Operations (ETOPS) plan in pounds.
    """

    point_name: Optional[str] = FieldInfo(alias="pointName", default=None)
    """Name of this point."""


class FlightPlanPointGroup(BaseModel):
    avg_fuel_flow: Optional[float] = FieldInfo(alias="avgFuelFlow", default=None)
    """Average fuel flow at which the fuel was calculated in pounds per hour."""

    etops_avg_wind_factor: Optional[float] = FieldInfo(alias="etopsAvgWindFactor", default=None)
    """
    Average wind factor from the Extended Operations (ETOPS) point to the recovery
    airfield in knots.
    """

    etops_distance: Optional[float] = FieldInfo(alias="etopsDistance", default=None)
    """
    Distance from the Extended Operations (ETOPS) point to the recovery airfield in
    nautical miles.
    """

    etops_req_fuel: Optional[float] = FieldInfo(alias="etopsReqFuel", default=None)
    """
    Fuel required to fly from the Extended Operations (ETOPS) point to the recovery
    airfield in pounds.
    """

    etops_temp_dev: Optional[float] = FieldInfo(alias="etopsTempDev", default=None)
    """
    Temperature deviation from the Extended Operations (ETOPS) point to the recovery
    airfield in degrees Celsius.
    """

    etops_time: Optional[str] = FieldInfo(alias="etopsTime", default=None)
    """
    Time to fly from the Extended Operations (ETOPS) point to the recovery airfield
    expressed in HH:MM format.
    """

    flight_plan_points: Optional[List[FlightPlanPointGroupFlightPlanPoint]] = FieldInfo(
        alias="flightPlanPoints", default=None
    )
    """Array of point data for this Point Group."""

    from_takeoff_time: Optional[str] = FieldInfo(alias="fromTakeoffTime", default=None)
    """Total time from takeoff when the point is reached expressed in HH:MM format."""

    fsaf_avg_wind_factor: Optional[float] = FieldInfo(alias="fsafAvgWindFactor", default=None)
    """
    Average wind factor from the Equal Time Point (ETP) to the first suitable
    airfield in knots.
    """

    fsaf_distance: Optional[float] = FieldInfo(alias="fsafDistance", default=None)
    """
    Distance from the Equal Time Point (ETP) to the first suitable airfield in
    nautical miles.
    """

    fsaf_req_fuel: Optional[float] = FieldInfo(alias="fsafReqFuel", default=None)
    """
    Fuel required to fly from the Equal Time Point (ETP) to the first suitable
    airfield in pounds.
    """

    fsaf_temp_dev: Optional[float] = FieldInfo(alias="fsafTempDev", default=None)
    """
    Temperature deviation from the Equal Time Point (ETP) to the first suitable
    airfield in degrees Celsius.
    """

    fsaf_time: Optional[str] = FieldInfo(alias="fsafTime", default=None)
    """
    Time to fly from the Equal Time Point (ETP) to the first suitable airfield
    expressed in HH:MM format.
    """

    fuel_calc_alt: Optional[float] = FieldInfo(alias="fuelCalcAlt", default=None)
    """Flight level of the point at which the fuel was calculated in feet."""

    fuel_calc_spd: Optional[float] = FieldInfo(alias="fuelCalcSpd", default=None)
    """True airspeed at which the fuel was calculated in knots."""

    lsaf_avg_wind_factor: Optional[float] = FieldInfo(alias="lsafAvgWindFactor", default=None)
    """
    Average wind factor from the Equal Time Point (ETP) to the last suitable
    airfield in knots.
    """

    lsaf_distance: Optional[float] = FieldInfo(alias="lsafDistance", default=None)
    """
    Distance from the Equal Time Point (ETP) to the last suitable airfield in
    nautical miles.
    """

    lsaf_name: Optional[str] = FieldInfo(alias="lsafName", default=None)
    """
    Name of the last suitable airfield, International Civil Aviation Organization
    (ICAO) code preferred.
    """

    lsaf_req_fuel: Optional[float] = FieldInfo(alias="lsafReqFuel", default=None)
    """
    Fuel required to fly from the Equal Time Point (ETP) to the last suitable
    airfield in pounds.
    """

    lsaf_temp_dev: Optional[float] = FieldInfo(alias="lsafTempDev", default=None)
    """
    Temperature deviation from the Equal Time Point (ETP) to the last suitable
    airfield in degrees Celsius.
    """

    lsaf_time: Optional[str] = FieldInfo(alias="lsafTime", default=None)
    """
    Time to fly from the Equal Time Point (ETP) to the last suitable airfield
    expressed in HH:MM format.
    """

    planned_fuel: Optional[float] = FieldInfo(alias="plannedFuel", default=None)
    """Amount of planned fuel on board when the point is reached in pounds."""

    point_group_name: Optional[str] = FieldInfo(alias="pointGroupName", default=None)
    """
    Name of the point group, usually Extended Operations (ETOPS), Critical Fuel
    Point, and Equal Time Point (ETP) sections.
    """

    worst_fuel_case: Optional[str] = FieldInfo(alias="worstFuelCase", default=None)
    """Specifies which Point Group case requires the most fuel."""


class FlightPlanWaypoint(BaseModel):
    type: str
    """Points are designated by type as either a comment point or a waypoint.

    A comment point conveys important information about the point for pilots but is
    not entered into a flight management system. A waypoint is a point that is
    entered into a flight management system and/or filed with Air Traffic Control.
    """

    waypoint_name: str = FieldInfo(alias="waypointName")
    """Name of the point.

    The name of a comment point identifies important information about that point,
    e.g. Top of Climb. The name of a waypoint identifies the location of that point.
    """

    aa_tacan_channel: Optional[str] = FieldInfo(alias="aaTacanChannel", default=None)
    """
    The air-to-air Tactical Air Navigation (TACAN) channels used by the
    receiver/tanker during air refueling.
    """

    air_distance: Optional[float] = FieldInfo(alias="airDistance", default=None)
    """The air distance of this leg in nautical miles."""

    airway: Optional[str] = None
    """The flight path flown for this leg."""

    alt: Optional[float] = None
    """Altitude of a level, point, or object measured in feet above mean sea level."""

    ar_id: Optional[str] = FieldInfo(alias="arId", default=None)
    """The ID of the air refueling track/anchor or fixed track."""

    arpt: Optional[str] = None
    """Point identifying an air refueling track/anchor or fixed track."""

    ata: Optional[datetime] = None
    """
    Actual Time of Arrival (ATA) at this waypoint in ISO 8601 UTC format, with
    millisecond precision.
    """

    avg_cal_airspeed: Optional[float] = FieldInfo(alias="avgCalAirspeed", default=None)
    """The average calibrated airspeed (CAS) for this leg in knots."""

    avg_drift_ang: Optional[float] = FieldInfo(alias="avgDriftAng", default=None)
    """The average drift angle for this leg in degrees from true north."""

    avg_ground_speed: Optional[float] = FieldInfo(alias="avgGroundSpeed", default=None)
    """The average ground speed for this leg in knots."""

    avg_true_airspeed: Optional[float] = FieldInfo(alias="avgTrueAirspeed", default=None)
    """The average true airspeed (TAS) for this leg in knots."""

    avg_wind_dir: Optional[float] = FieldInfo(alias="avgWindDir", default=None)
    """The average wind direction for this leg in degrees from true north."""

    avg_wind_speed: Optional[float] = FieldInfo(alias="avgWindSpeed", default=None)
    """The average wind speed for this leg in knots."""

    day_low_alt: Optional[float] = FieldInfo(alias="dayLowAlt", default=None)
    """
    The day low level altitude in feet above sea level for the leg ending at this
    waypoint.
    """

    eta: Optional[datetime] = None
    """
    Estimated Time of Arrival (ETA) at this waypoint in ISO 8601 UTC format, with
    millisecond precision.
    """

    exchanged_fuel: Optional[float] = FieldInfo(alias="exchangedFuel", default=None)
    """
    The amount of fuel onloaded or offloaded at this waypoint in pounds (negative
    value for offload).
    """

    fuel_flow: Optional[float] = FieldInfo(alias="fuelFlow", default=None)
    """The leg fuel flow in pounds per hour."""

    ice_cat: Optional[str] = FieldInfo(alias="iceCat", default=None)
    """The icing intensity classification for this flight (LIGHT, MODERATE, etc)."""

    lat: Optional[float] = None
    """WGS84 latitude of the point location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    leg_alternate: Optional[str] = FieldInfo(alias="legAlternate", default=None)
    """
    The planned alternate leg based on user-defined constraints, International Civil
    Aviation Organization (ICAO) code preferred.
    """

    leg_drag_index: Optional[float] = FieldInfo(alias="legDragIndex", default=None)
    """The percent degrade due to drag for this aircraft for this leg."""

    leg_fuel_degrade: Optional[float] = FieldInfo(alias="legFuelDegrade", default=None)
    """The fuel degrade percentage used for this leg."""

    leg_mach: Optional[float] = FieldInfo(alias="legMach", default=None)
    """The average Mach speed for this leg."""

    leg_msn_index: Optional[float] = FieldInfo(alias="legMsnIndex", default=None)
    """The mission index value for this leg.

    The mission index is the ratio of time-related cost of aircraft operation to the
    cost of fuel.
    """

    leg_wind_fac: Optional[float] = FieldInfo(alias="legWindFac", default=None)
    """The wind factor for this leg in knots.

    A positive value indicates a headwind, while a negative value indicates a
    tailwind.
    """

    lon: Optional[float] = None
    """WGS84 longitude of the point location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    mag_course: Optional[float] = FieldInfo(alias="magCourse", default=None)
    """The magnetic course at leg midpoint in degrees from true north."""

    mag_heading: Optional[float] = FieldInfo(alias="magHeading", default=None)
    """The magnetic heading at leg midpoint in degrees from true north."""

    mag_var: Optional[float] = FieldInfo(alias="magVar", default=None)
    """The magnetic variation for this leg in degrees."""

    navaid: Optional[str] = None
    """Navigational Aid (NAVAID) identification code."""

    night_low_alt: Optional[float] = FieldInfo(alias="nightLowAlt", default=None)
    """
    The night low level altitude in feet above sea level for the leg ending at this
    waypoint.
    """

    nvg_low_alt: Optional[float] = FieldInfo(alias="nvgLowAlt", default=None)
    """
    The night vision goggle low level altitude in feet above sea level for the leg
    ending at this waypoint.
    """

    point_wind_dir: Optional[float] = FieldInfo(alias="pointWindDir", default=None)
    """The wind direction at this specific point in degrees from true north."""

    point_wind_speed: Optional[float] = FieldInfo(alias="pointWindSpeed", default=None)
    """The wind velocity at this specific point in knots."""

    pri_freq: Optional[float] = FieldInfo(alias="priFreq", default=None)
    """
    The primary UHF radio frequency used for the air refueling track or anchor in
    megahertz.
    """

    sec_freq: Optional[float] = FieldInfo(alias="secFreq", default=None)
    """
    The secondary UHF radio frequency used for the air refueling track or anchor in
    megahertz.
    """

    tacan_channel: Optional[str] = FieldInfo(alias="tacanChannel", default=None)
    """Tactical Air Navigation (TACAN) channel for the Navigational Aid (NAVAID)."""

    temp_dev: Optional[float] = FieldInfo(alias="tempDev", default=None)
    """
    Average temperature deviation from standard day profile for this leg in degrees
    Celsius.
    """

    thunder_cat: Optional[str] = FieldInfo(alias="thunderCat", default=None)
    """
    The thunderstorm intensity classification for this flight (LIGHT, MODERATE,
    etc).
    """

    total_air_distance: Optional[float] = FieldInfo(alias="totalAirDistance", default=None)
    """The total air distance to this waypoint in nautical miles."""

    total_flown_distance: Optional[float] = FieldInfo(alias="totalFlownDistance", default=None)
    """
    The total distance flown to this waypoint calculated from point of departure in
    nautical miles.
    """

    total_rem_distance: Optional[float] = FieldInfo(alias="totalRemDistance", default=None)
    """
    The total distance remaining from this waypoint to the point of arrival in
    nautical miles.
    """

    total_rem_fuel: Optional[float] = FieldInfo(alias="totalRemFuel", default=None)
    """The total fuel remaining at this waypoint in pounds."""

    total_time: Optional[str] = FieldInfo(alias="totalTime", default=None)
    """The total time accumulated from takeoff to this waypoint expressed as HH:MM."""

    total_time_rem: Optional[str] = FieldInfo(alias="totalTimeRem", default=None)
    """
    The total time remaining from this waypoint to the point of arrival expressed as
    HH:MM.
    """

    total_used_fuel: Optional[float] = FieldInfo(alias="totalUsedFuel", default=None)
    """The total fuel used to this waypoint from point of departure in pounds."""

    total_weight: Optional[float] = FieldInfo(alias="totalWeight", default=None)
    """The total weight of the aircraft at this waypoint in pounds."""

    true_course: Optional[float] = FieldInfo(alias="trueCourse", default=None)
    """The true course at leg midpoint in degrees from true north."""

    turb_cat: Optional[str] = FieldInfo(alias="turbCat", default=None)
    """The turbulence intensity classification for this flight (LIGHT, MODERATE, etc)."""

    vor_freq: Optional[float] = FieldInfo(alias="vorFreq", default=None)
    """
    VHF Omni-directional Range (VOR) frequency for the Navigational Aid (NAVAID) in
    megahertz.
    """

    waypoint_num: Optional[int] = FieldInfo(alias="waypointNum", default=None)
    """The waypoint number on the route. Comment points do not get a waypoint number."""

    zone_distance: Optional[float] = FieldInfo(alias="zoneDistance", default=None)
    """The zone/leg distance flown in nautical miles."""

    zone_fuel: Optional[float] = FieldInfo(alias="zoneFuel", default=None)
    """The amount of fuel used on this zone/leg in pounds."""

    zone_time: Optional[float] = FieldInfo(alias="zoneTime", default=None)
    """The time to fly this zone/leg in minutes."""


class FlightPlanFull(BaseModel):
    arr_airfield: str = FieldInfo(alias="arrAirfield")
    """
    The airfield identifier of the arrival location, International Civil Aviation
    Organization (ICAO) code preferred.
    """

    classification_marking: str = FieldInfo(alias="classificationMarking")
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"] = FieldInfo(alias="dataMode")
    """Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

    EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
    may include both real and simulated data.

    REAL:&nbsp;Data collected or produced that pertains to real-world objects,
    events, and analysis.

    SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
    datasets.

    TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
    requirements, and for validating technical, functional, and performance
    characteristics.
    """

    dep_airfield: str = FieldInfo(alias="depAirfield")
    """
    The airfield identifier of the departure location, International Civil Aviation
    Organization (ICAO) code preferred.
    """

    gen_ts: datetime = FieldInfo(alias="genTS")
    """
    The generation time of this flight plan in ISO 8601 UTC format, with millisecond
    precision.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    aircraft_mds: Optional[str] = FieldInfo(alias="aircraftMDS", default=None)
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of the aircraft associated with
    this flight plan. Intended as, but not constrained to, MIL-STD-6016 environment
    dependent specific type designations.
    """

    air_refuel_events: Optional[List[AirRefuelEvent]] = FieldInfo(alias="airRefuelEvents", default=None)
    """Collection of air refueling events occurring on this flight."""

    amc_mission_id: Optional[str] = FieldInfo(alias="amcMissionId", default=None)
    """
    Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
    (MAF) encode/decode procedures.
    """

    app_landing_fuel: Optional[float] = FieldInfo(alias="appLandingFuel", default=None)
    """Fuel burned from the initial approach point to landing in pounds."""

    arr_alternate1: Optional[str] = FieldInfo(alias="arrAlternate1", default=None)
    """
    The first designated alternate arrival airfield, International Civil Aviation
    Organization (ICAO) code preferred.
    """

    arr_alternate1_fuel: Optional[float] = FieldInfo(alias="arrAlternate1Fuel", default=None)
    """Fuel required to fly to alternate landing site 1 and land in pounds."""

    arr_alternate2: Optional[str] = FieldInfo(alias="arrAlternate2", default=None)
    """
    The second designated alternate arrival airfield, International Civil Aviation
    Organization (ICAO) code preferred.
    """

    arr_alternate2_fuel: Optional[float] = FieldInfo(alias="arrAlternate2Fuel", default=None)
    """Fuel required to fly to alternate landing site 2 and land in pounds."""

    arr_ice_fuel: Optional[float] = FieldInfo(alias="arrIceFuel", default=None)
    """
    Additional fuel burned at landing/missed approach for icing during arrival in
    pounds.
    """

    arr_runway: Optional[str] = FieldInfo(alias="arrRunway", default=None)
    """The arrival runway for this flight."""

    atc_addresses: Optional[List[str]] = FieldInfo(alias="atcAddresses", default=None)
    """Array of Air Traffic Control (ATC) addresses."""

    avg_temp_dev: Optional[float] = FieldInfo(alias="avgTempDev", default=None)
    """
    Average temperature deviation of the primary, divert, and alternate path for the
    route between first Top of Climb and last Top of Descent in degrees Celsius.
    """

    burned_fuel: Optional[float] = FieldInfo(alias="burnedFuel", default=None)
    """Fuel planned to be burned during the flight in pounds."""

    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign assigned to the aircraft for this flight plan."""

    cargo_remark: Optional[str] = FieldInfo(alias="cargoRemark", default=None)
    """Remarks about the planned cargo associated with this flight plan."""

    climb_fuel: Optional[float] = FieldInfo(alias="climbFuel", default=None)
    """Fuel required from brake release to Top of Climb in pounds."""

    climb_time: Optional[str] = FieldInfo(alias="climbTime", default=None)
    """Time required from brake release to Top of Climb expressed as HH:MM."""

    contingency_fuel: Optional[float] = FieldInfo(alias="contingencyFuel", default=None)
    """The amount of contingency fuel in pounds."""

    country_codes: Optional[List[str]] = FieldInfo(alias="countryCodes", default=None)
    """
    Array of country codes for the countries overflown during this flight in ISO
    3166-1 Alpha-2 format.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    dep_alternate: Optional[str] = FieldInfo(alias="depAlternate", default=None)
    """
    The designated alternate departure airfield, International Civil Aviation
    Organization (ICAO) code preferred.
    """

    depress_fuel: Optional[float] = FieldInfo(alias="depressFuel", default=None)
    """
    The depressurization fuel required to fly from the Equal Time Point to the Last
    Suitable/First Suitable airfield at depressurization altitude in pounds.
    """

    dep_runway: Optional[str] = FieldInfo(alias="depRunway", default=None)
    """The departure runway for this flight."""

    drag_index: Optional[float] = FieldInfo(alias="dragIndex", default=None)
    """The percent degrade due to drag for this aircraft."""

    early_descent_fuel: Optional[float] = FieldInfo(alias="earlyDescentFuel", default=None)
    """
    Additional fuel burned at landing/missed approach for an early descent in
    pounds.
    """

    endurance_time: Optional[str] = FieldInfo(alias="enduranceTime", default=None)
    """Total endurance time based on the fuel on board expressed as HH:MM."""

    enroute_fuel: Optional[float] = FieldInfo(alias="enrouteFuel", default=None)
    """Fuel required to fly from Top of Climb to Top of Descent in pounds."""

    enroute_time: Optional[str] = FieldInfo(alias="enrouteTime", default=None)
    """Time required to fly from Top of Climb to Top of Descent expressed as HH:MM."""

    equipment: Optional[str] = None
    """
    The list of equipment on the aircraft as defined in the Flight Information
    Publications (FLIP) General Planning (GP) manual.
    """

    est_dep_time: Optional[datetime] = FieldInfo(alias="estDepTime", default=None)
    """
    The estimated time of departure for the aircraft, in ISO 8601 UTC format, with
    millisecond precision.
    """

    etops_airfields: Optional[List[str]] = FieldInfo(alias="etopsAirfields", default=None)
    """
    Array of Extended Operations (ETOPS) adequate landing airfields that are within
    the mission region.
    """

    etops_alt_airfields: Optional[List[str]] = FieldInfo(alias="etopsAltAirfields", default=None)
    """
    Array of Extended Operations (ETOPS) alternate suitable landing airfields that
    are within the mission region.
    """

    etops_rating: Optional[str] = FieldInfo(alias="etopsRating", default=None)
    """The Extended Operations (ETOPS) rating used to calculate this flight plan."""

    etops_val_window: Optional[str] = FieldInfo(alias="etopsValWindow", default=None)
    """The Extended Operations (ETOPS) validity window for the alternate airfield."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """The source ID of the flight plan from the generating system."""

    flight_plan_messages: Optional[List[FlightPlanMessage]] = FieldInfo(alias="flightPlanMessages", default=None)
    """
    Collection of messages associated with this flight plan indicating the severity,
    the point where the message was generated, the path (Primary, Alternate, etc.),
    and the text of the message.
    """

    flight_plan_point_groups: Optional[List[FlightPlanPointGroup]] = FieldInfo(
        alias="flightPlanPointGroups", default=None
    )
    """Collection of point groups generated for this flight plan.

    Groups include point sets for Extended Operations (ETOPS), Critical Fuel Point,
    and Equal Time Point (ETP).
    """

    flight_plan_waypoints: Optional[List[FlightPlanWaypoint]] = FieldInfo(alias="flightPlanWaypoints", default=None)
    """Collection of waypoints associated with this flight plan."""

    flight_rules: Optional[str] = FieldInfo(alias="flightRules", default=None)
    """The flight rules this flight plan is being filed under."""

    flight_type: Optional[str] = FieldInfo(alias="flightType", default=None)
    """The type of flight (MILITARY, CIVILIAN, etc)."""

    fuel_degrade: Optional[float] = FieldInfo(alias="fuelDegrade", default=None)
    """The fuel degrade percentage used for this mission."""

    gps_raim: Optional[str] = FieldInfo(alias="gpsRAIM", default=None)
    """The GPS Receiver Autonomous Integrity Monitoring (RAIM) message.

    A RAIM system assesses the integrity of the GPS signals. This system predicts
    outages for a specified geographical area. These predictions are based on the
    location, path, and scheduled GPS satellite outages.
    """

    hold_down_fuel: Optional[float] = FieldInfo(alias="holdDownFuel", default=None)
    """Additional fuel burned at Top of Climb in pounds."""

    hold_fuel: Optional[float] = FieldInfo(alias="holdFuel", default=None)
    """Additional fuel burned at the destination for holding in pounds."""

    hold_time: Optional[str] = FieldInfo(alias="holdTime", default=None)
    """Additional time for holding at the destination expressed as HH:MM."""

    id_aircraft: Optional[str] = FieldInfo(alias="idAircraft", default=None)
    """The UDL unique identifier of the aircraft associated with this flight plan."""

    id_arr_airfield: Optional[str] = FieldInfo(alias="idArrAirfield", default=None)
    """
    The UDL unique identifier of the arrival airfield associated with this flight
    plan.
    """

    id_dep_airfield: Optional[str] = FieldInfo(alias="idDepAirfield", default=None)
    """
    The UDL unique identifier of the departure airfield associated with this flight
    plan.
    """

    ident_extra_fuel: Optional[float] = FieldInfo(alias="identExtraFuel", default=None)
    """
    The amount of identified extra fuel carried and not available in the burn plan
    in pounds.
    """

    id_sortie: Optional[str] = FieldInfo(alias="idSortie", default=None)
    """
    The UDL unique identifier of the aircraft sortie associated with this flight
    plan.
    """

    initial_cruise_speed: Optional[str] = FieldInfo(alias="initialCruiseSpeed", default=None)
    """
    A character string representation of the initial filed cruise speed for this
    flight (prepended values of K, N, and M represent kilometers per hour, knots,
    and Mach, respectively).
    """

    initial_flight_level: Optional[str] = FieldInfo(alias="initialFlightLevel", default=None)
    """
    A character string representation of the initial filed altitude level for this
    flight (prepended values of F, S, A, and M represent flight level in hundreds of
    feet, standard metric level in tens of meters, altitude in hundreds of feet, and
    altitude in tens of meters, respectively).
    """

    landing_fuel: Optional[float] = FieldInfo(alias="landingFuel", default=None)
    """Fuel planned to be remaining on the airplane at landing in pounds."""

    leg_num: Optional[int] = FieldInfo(alias="legNum", default=None)
    """The leg number of this flight plan."""

    min_divert_fuel: Optional[float] = FieldInfo(alias="minDivertFuel", default=None)
    """The minimum fuel on board required to divert in pounds."""

    msn_index: Optional[float] = FieldInfo(alias="msnIndex", default=None)
    """The mission index value for this mission.

    The mission index is the ratio of time-related cost of aircraft operation to the
    cost of fuel.
    """

    notes: Optional[str] = None
    """Additional remarks for air traffic control for this flight."""

    num_aircraft: Optional[int] = FieldInfo(alias="numAircraft", default=None)
    """The number of aircraft flying this flight plan."""

    op_condition_fuel: Optional[float] = FieldInfo(alias="opConditionFuel", default=None)
    """
    Additional fuel burned at Top of Descent for the operational condition in
    pounds.
    """

    op_weight: Optional[float] = FieldInfo(alias="opWeight", default=None)
    """Operating weight of the aircraft in pounds."""

    origin: Optional[str] = None
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    originator: Optional[str] = None
    """Air Traffic Control address filing the flight plan."""

    orig_network: Optional[str] = FieldInfo(alias="origNetwork", default=None)
    """
    The originating source network on which this record was created, auto-populated
    by the system.
    """

    planner_remark: Optional[str] = FieldInfo(alias="plannerRemark", default=None)
    """Remarks from the planners concerning this flight plan."""

    ramp_fuel: Optional[float] = FieldInfo(alias="rampFuel", default=None)
    """
    Total of all fuel required to complete the flight in pounds, including fuel to
    be dispensed on a refueling mission.
    """

    rem_alternate1_fuel: Optional[float] = FieldInfo(alias="remAlternate1Fuel", default=None)
    """Total fuel remaining at alternate landing site 1 in pounds."""

    rem_alternate2_fuel: Optional[float] = FieldInfo(alias="remAlternate2Fuel", default=None)
    """Total fuel remaining at alternate landing site 2 in pounds."""

    reserve_fuel: Optional[float] = FieldInfo(alias="reserveFuel", default=None)
    """The amount of reserve fuel in pounds."""

    route_string: Optional[str] = FieldInfo(alias="routeString", default=None)
    """The 1801 fileable route of flight string for this flight.

    The route of flight string contains route designators, significant points,
    change of speed/altitude, change of flight rules, and cruise climbs.
    """

    sid: Optional[str] = None
    """Name of the planned Standard Instrument Departure (SID) procedure."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    star: Optional[str] = None
    """Name of the planned Standard Terminal Arrival (STAR) procedure."""

    status: Optional[str] = None
    """Status of this flight plan (e.g., ACTIVE, APPROVED, PLANNED, etc.)."""

    tail_number: Optional[str] = FieldInfo(alias="tailNumber", default=None)
    """The tail number of the aircraft associated with this flight plan."""

    takeoff_fuel: Optional[float] = FieldInfo(alias="takeoffFuel", default=None)
    """
    Fuel at takeoff, which is calculated as the ramp fuel minus the taxi fuel in
    pounds.
    """

    taxi_fuel: Optional[float] = FieldInfo(alias="taxiFuel", default=None)
    """Fuel required to start engines and taxi to the end of the runway in pounds."""

    thunder_avoid_fuel: Optional[float] = FieldInfo(alias="thunderAvoidFuel", default=None)
    """Additional fuel burned at Top of Descent for thunderstorm avoidance in pounds."""

    toc_fuel: Optional[float] = FieldInfo(alias="tocFuel", default=None)
    """Fuel remaining at Top of Climb in pounds."""

    toc_ice_fuel: Optional[float] = FieldInfo(alias="tocIceFuel", default=None)
    """Additional fuel burned at Top of Climb for icing in pounds."""

    tod_fuel: Optional[float] = FieldInfo(alias="todFuel", default=None)
    """Fuel remaining at Top of Descent in pounds."""

    tod_ice_fuel: Optional[float] = FieldInfo(alias="todIceFuel", default=None)
    """Additional fuel burned at Top of Descent for icing in pounds."""

    unident_extra_fuel: Optional[float] = FieldInfo(alias="unidentExtraFuel", default=None)
    """The amount of unidentified extra fuel required to get to min landing in pounds."""

    unusable_fuel: Optional[float] = FieldInfo(alias="unusableFuel", default=None)
    """The amount of unusable fuel in pounds."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was last updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    wake_turb_cat: Optional[str] = FieldInfo(alias="wakeTurbCat", default=None)
    """The wake turbulence category for this flight.

    The categories are assigned by the International Civil Aviation Organization
    (ICAO) and are based on maximum certified takeoff mass for the purpose of
    separating aircraft in flight due to wake turbulence. Valid values include
    LIGHT, MEDIUM, LARGE, HEAVY, and SUPER.
    """

    wind_fac1: Optional[float] = FieldInfo(alias="windFac1", default=None)
    """Wind factor for the first half of the route.

    This is the average wind factor from first Top of Climb to the mid-time of the
    entire route in knots. A positive value indicates a headwind, while a negative
    value indicates a tailwind.
    """

    wind_fac2: Optional[float] = FieldInfo(alias="windFac2", default=None)
    """Wind factor for the second half of the route.

    This is the average wind factor from the mid-time of the entire route to last
    Top of Descent in knots. A positive value indicates a headwind, while a negative
    value indicates a tailwind.
    """

    wind_fac_avg: Optional[float] = FieldInfo(alias="windFacAvg", default=None)
    """Average wind factor from Top of Climb to Top of Descent in knots.

    A positive value indicates a headwind, while a negative value indicates a
    tailwind.
    """

    wx_valid_end: Optional[datetime] = FieldInfo(alias="wxValidEnd", default=None)
    """
    The date and time the weather valid period ends in ISO 8601 UTC format, with
    millisecond precision.
    """

    wx_valid_start: Optional[datetime] = FieldInfo(alias="wxValidStart", default=None)
    """
    The date and time the weather valid period begins in ISO 8601 UTC format, with
    millisecond precision.
    """
