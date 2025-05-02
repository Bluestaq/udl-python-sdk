# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PersonnelrecoveryListResponse",
    "ExecutionInfo",
    "ExecutionInfoEscortVehicle",
    "ExecutionInfoRecoveryVehicle",
    "ObjectiveAreaInfo",
    "ObjectiveAreaInfoEnemyData",
]


class ExecutionInfoEscortVehicle(BaseModel):
    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign of the recovery vehicle."""

    primary_freq: Optional[float] = FieldInfo(alias="primaryFreq", default=None)
    """Primary contact frequency of the recovery vehicle."""

    strength: Optional[int] = None
    """
    The number of objects or units moving as a group and represented as a single
    entity in this recovery vehicle message. If null, the strength is assumed to
    represent a single object. Note that if this recovery derives from a J-series
    message then special definitions apply for the following values: 13 indicates an
    estimated 2-7 units, 14 indicates an estimated more than 7 units, and 15
    indicates an estimated more than 12 units.
    """

    type: Optional[str] = None
    """The particular type of recovery vehicle to be used."""


class ExecutionInfoRecoveryVehicle(BaseModel):
    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign of the recovery vehicle."""

    primary_freq: Optional[float] = FieldInfo(alias="primaryFreq", default=None)
    """Primary contact frequency of the recovery vehicle."""

    strength: Optional[int] = None
    """
    The number of objects or units moving as a group and represented as a single
    entity in this recovery vehicle message. If null, the strength is assumed to
    represent a single object. Note that if this recovery derives from a J-series
    message then special definitions apply for the following values: 13 indicates an
    estimated 2-7 units, 14 indicates an estimated more than 7 units, and 15
    indicates an estimated more than 12 units.
    """

    type: Optional[str] = None
    """The particular type of recovery vehicle to be used."""


class ExecutionInfo(BaseModel):
    egress: Optional[float] = None
    """The heading, in degrees, of leaving the recovery zone."""

    egress_point: Optional[List[float]] = FieldInfo(alias="egressPoint", default=None)
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the egress location. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    escort_vehicle: Optional[ExecutionInfoEscortVehicle] = FieldInfo(alias="escortVehicle", default=None)

    ingress: Optional[float] = None
    """The heading, in degrees clockwise from North, of entering the recovery zone."""

    initial_point: Optional[List[float]] = FieldInfo(alias="initialPoint", default=None)
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the initial location. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    obj_strategy: Optional[str] = FieldInfo(alias="objStrategy", default=None)
    """Description of the objective strategy plan."""

    recovery_vehicle: Optional[ExecutionInfoRecoveryVehicle] = FieldInfo(alias="recoveryVehicle", default=None)


class ObjectiveAreaInfoEnemyData(BaseModel):
    dir_to_enemy: Optional[str] = FieldInfo(alias="dirToEnemy", default=None)
    """
    Directions to known enemies in the operation area (NORTH, NORTHEAST, EAST,
    SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST, SURROUNDED).
    """

    friendlies_remarks: Optional[str] = FieldInfo(alias="friendliesRemarks", default=None)
    """Comments provided by friendlies about the evac zone."""

    hlz_remarks: Optional[str] = FieldInfo(alias="hlzRemarks", default=None)
    """Hot Landing Zone remarks."""

    hostile_fire_type: Optional[str] = FieldInfo(alias="hostileFireType", default=None)
    """The type of hostile fire received (SMALL ARMS, MORTAR, ARTILLERY, ROCKETS)."""


class ObjectiveAreaInfo(BaseModel):
    enemy_data: Optional[List[ObjectiveAreaInfoEnemyData]] = FieldInfo(alias="enemyData", default=None)
    """Information detailing knowledge of enemies in the area."""

    osc_call_sign: Optional[str] = FieldInfo(alias="oscCallSign", default=None)
    """The call sign of the on-scene commander."""

    osc_freq: Optional[float] = FieldInfo(alias="oscFreq", default=None)
    """The radio frequency of the on-scene commander."""

    pz_desc: Optional[str] = FieldInfo(alias="pzDesc", default=None)
    """Description of the pickup zone location."""

    pz_location: Optional[List[float]] = FieldInfo(alias="pzLocation", default=None)
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the pz location. This array must contain a
    minimum of 2 elements (latitude and longitude), and may contain an optional 3rd
    element (altitude).
    """


class PersonnelrecoveryListResponse(BaseModel):
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

    msg_time: datetime = FieldInfo(alias="msgTime")
    """Time stamp of the original personnel recovery message, in ISO 8601 UTC format."""

    pickup_lat: float = FieldInfo(alias="pickupLat")
    """WGS-84 latitude of the pickup location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    pickup_lon: float = FieldInfo(alias="pickupLon")
    """WGS-84 longitude of the pickup location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    source: str
    """Source of the data."""

    type: str
    """Specifies the type of incident resulting in a recovery or evacuation mission.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Emergency Type (e.g. NO
    STATEMENT, DOWN AIRCRAFT, MAN IN WATER, DITCHING, BAILOUT, DISTRESSED VEHICLE,
    GROUND INCIDENT, MEDICAL, ISOLATED PERSONS, etc.).
    """

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    auth_method: Optional[str] = FieldInfo(alias="authMethod", default=None)
    """Mechanism used to verify the survivors identity."""

    auth_status: Optional[str] = FieldInfo(alias="authStatus", default=None)
    """The confirmation status of the isolated personnel identity.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Authentication Status,
    Isolated Personnel (NO STATEMENT, AUTHENTICATED, NOT AUTHENTICATED,
    AUTHENTICATED UNDER DURESS, NOT APPLICABLE):

    AUTHENTICATED: Confirmed Friend

    NOT AUTHENTICATED: Unconfirmed status

    AUTHENTICATED UNDER DURESS: Authentication comprised by hostiles.

    NOT APPLICABLE: Authentication not required.
    """

    beacon_ind: Optional[bool] = FieldInfo(alias="beaconInd", default=None)
    """Flag indicating whether a radio identifier is reported."""

    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign of the personnel to be recovered."""

    comm_eq1: Optional[str] = FieldInfo(alias="commEq1", default=None)
    """Survivor communications equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Communications Equipment,
    Isolated Personnel (NO STATEMENT, SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL
    MIRROR, SMOKE FLARE, IR SIGNALLING DEVICE, SIGNALLING PANEL, FRIENDLY FORCE
    TRACKER, GPS BEACON, LL PHONE, TACTICAL RADIO LOS, TACTICAL RADIO BLOS).
    """

    comm_eq2: Optional[str] = FieldInfo(alias="commEq2", default=None)
    """Survivor communications equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Communications Equipment,
    Isolated Personnel (NO STATEMENT, SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL
    MIRROR, SMOKE FLARE, IR SIGNALLING DEVICE, SIGNALLING PANEL, FRIENDLY FORCE
    TRACKER, GPS BEACON, LL PHONE, TACTICAL RADIO LOS, TACTICAL RADIO BLOS).
    """

    comm_eq3: Optional[str] = FieldInfo(alias="commEq3", default=None)
    """Survivor communications equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Communications Equipment,
    Isolated Personnel (NO STATEMENT, SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL
    MIRROR, SMOKE FLARE, IR SIGNALLING DEVICE, SIGNALLING PANEL, FRIENDLY FORCE
    TRACKER, GPS BEACON, LL PHONE, TACTICAL RADIO LOS, TACTICAL RADIO BLOS).
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    execution_info: Optional[ExecutionInfo] = FieldInfo(alias="executionInfo", default=None)

    identity: Optional[str] = None
    """
    The survivor service identity (UNKNOWN MILITARY, UNKNOWN CIVILIAN, FRIEND
    MILITARY, FRIEND CIVIILIAN, NEUTRAL MILITARY, NEUTRAL CIVILIAN, HOSTILE
    MILITARY, HOSTILE CIVILIAN).
    """

    id_weather_report: Optional[str] = FieldInfo(alias="idWeatherReport", default=None)
    """Unique identifier of a weather report associated with this recovery."""

    mil_class: Optional[str] = FieldInfo(alias="milClass", default=None)
    """The military classification of the personnel to be recovered.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Isolated Personnel
    Classification (NO STATEMENT, MILITARY, GOVERNMENT CIVILIAN, GOVERNMENT
    CONTRACTOR, CIVILIAN, MULTIPLE CLASSIFICATIONS).
    """

    nat_alliance: Optional[int] = FieldInfo(alias="natAlliance", default=None)
    """
    The country of origin or political entity of an isolated person subject to
    rescue or evacuation. If natAlliance is set to 126, then natAlliance1 must be
    non 0. If natAlliance is any number other than 126, then natAlliance1 will be
    set to 0 regardless. Defined in MIL-STD-6016 J6.1 Nationality/Alliance isolated
    person(s).
    """

    nat_alliance1: Optional[int] = FieldInfo(alias="natAlliance1", default=None)
    """
    Extended country of origin or political entity of an isolated person subject to
    rescue or evacuation. Specify an entry here only if natAlliance is 126. Defined
    in MIL-STD-6016 J6.1 Nationality/Alliance isolated person(s), 1.
    """

    num_ambulatory: Optional[int] = FieldInfo(alias="numAmbulatory", default=None)
    """Number of ambulatory personnel requiring recovery."""

    num_ambulatory_injured: Optional[int] = FieldInfo(alias="numAmbulatoryInjured", default=None)
    """Number of injured, but ambulatory, personnel requiring recovery."""

    num_non_ambulatory: Optional[int] = FieldInfo(alias="numNonAmbulatory", default=None)
    """Number of littered personnel requiring recovery."""

    num_persons: Optional[int] = FieldInfo(alias="numPersons", default=None)
    """The count of persons requiring recovery."""

    objective_area_info: Optional[ObjectiveAreaInfo] = FieldInfo(alias="objectiveAreaInfo", default=None)

    origin: Optional[str] = None
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_network: Optional[str] = FieldInfo(alias="origNetwork", default=None)
    """
    The originating source network on which this record was created, auto-populated
    by the system.
    """

    pickup_alt: Optional[float] = FieldInfo(alias="pickupAlt", default=None)
    """Altitude relative to WGS-84 ellipsoid, in meters.

    Positive values indicate a point height above ellipsoid, and negative values
    indicate a point eight below ellipsoid.
    """

    recov_id: Optional[str] = FieldInfo(alias="recovId", default=None)
    """
    UUID identifying the Personnel Recovery mission, which should remain the same on
    subsequent posts related to the same recovery mission.
    """

    rx_freq: Optional[float] = FieldInfo(alias="rxFreq", default=None)
    """Receive voice frequency in 5Hz increments.

    This field will auto populate with the txFreq value if the post element is null.
    """

    survivor_messages: Optional[str] = FieldInfo(alias="survivorMessages", default=None)
    """Preloaded message conveying the situation confronting the isolated person(s).

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Survivor Radio Messages
    (e.g. INJURED CANT MOVE NO KNOWN HOSTILES, INJURED CANT MOVE HOSTILES NEARBY,
    UNINJURED CANT MOVE HOSTILES NEARBY, UNINJURED NO KNOWN HOSTILES, INJURED
    LIMITED MOBILITY).
    """

    survivor_radio: Optional[str] = FieldInfo(alias="survivorRadio", default=None)
    """Survivor radio equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Survivor Radio Type (NO
    STATEMENT, PRQ7SEL, PRC90, PRC112, PRC112B B1, PRC112C, PRC112D, PRC148 MBITR,
    PRC148 JEM, PRC149, PRC152, ACRPLB, OTHER).
    """

    term_ind: Optional[bool] = FieldInfo(alias="termInd", default=None)
    """Flag indicating the cancellation of this recovery."""

    text_msg: Optional[str] = FieldInfo(alias="textMsg", default=None)
    """Additional specific messages received from survivor."""

    tx_freq: Optional[float] = FieldInfo(alias="txFreq", default=None)
    """Transmit voice frequency in 5Hz increments."""
