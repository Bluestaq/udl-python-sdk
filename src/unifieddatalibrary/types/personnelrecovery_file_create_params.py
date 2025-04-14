# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PersonnelrecoveryFileCreateParams",
    "Body",
    "BodyExecutionInfo",
    "BodyExecutionInfoEscortVehicle",
    "BodyExecutionInfoRecoveryVehicle",
    "BodyObjectiveAreaInfo",
    "BodyObjectiveAreaInfoEnemyData",
]


class PersonnelrecoveryFileCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyExecutionInfoEscortVehicle(TypedDict, total=False):
    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """The call sign of the recovery vehicle."""

    primary_freq: Annotated[float, PropertyInfo(alias="primaryFreq")]
    """Primary contact frequency of the recovery vehicle."""

    strength: int
    """
    The number of objects or units moving as a group and represented as a single
    entity in this recovery vehicle message. If null, the strength is assumed to
    represent a single object. Note that if this recovery derives from a J-series
    message then special definitions apply for the following values: 13 indicates an
    estimated 2-7 units, 14 indicates an estimated more than 7 units, and 15
    indicates an estimated more than 12 units.
    """

    type: str
    """The particular type of recovery vehicle to be used."""


class BodyExecutionInfoRecoveryVehicle(TypedDict, total=False):
    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """The call sign of the recovery vehicle."""

    primary_freq: Annotated[float, PropertyInfo(alias="primaryFreq")]
    """Primary contact frequency of the recovery vehicle."""

    strength: int
    """
    The number of objects or units moving as a group and represented as a single
    entity in this recovery vehicle message. If null, the strength is assumed to
    represent a single object. Note that if this recovery derives from a J-series
    message then special definitions apply for the following values: 13 indicates an
    estimated 2-7 units, 14 indicates an estimated more than 7 units, and 15
    indicates an estimated more than 12 units.
    """

    type: str
    """The particular type of recovery vehicle to be used."""


class BodyExecutionInfo(TypedDict, total=False):
    egress: float
    """The heading, in degrees, of leaving the recovery zone."""

    egress_point: Annotated[Iterable[float], PropertyInfo(alias="egressPoint")]
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the egress location. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    escort_vehicle: Annotated[BodyExecutionInfoEscortVehicle, PropertyInfo(alias="escortVehicle")]

    ingress: float
    """The heading, in degrees clockwise from North, of entering the recovery zone."""

    initial_point: Annotated[Iterable[float], PropertyInfo(alias="initialPoint")]
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the initial location. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    obj_strategy: Annotated[str, PropertyInfo(alias="objStrategy")]
    """Description of the objective strategy plan."""

    recovery_vehicle: Annotated[BodyExecutionInfoRecoveryVehicle, PropertyInfo(alias="recoveryVehicle")]


class BodyObjectiveAreaInfoEnemyData(TypedDict, total=False):
    dir_to_enemy: Annotated[str, PropertyInfo(alias="dirToEnemy")]
    """
    Directions to known enemies in the operation area (NORTH, NORTHEAST, EAST,
    SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST, SURROUNDED).
    """

    friendlies_remarks: Annotated[str, PropertyInfo(alias="friendliesRemarks")]
    """Comments provided by friendlies about the evac zone."""

    hlz_remarks: Annotated[str, PropertyInfo(alias="hlzRemarks")]
    """Hot Landing Zone remarks."""

    hostile_fire_type: Annotated[str, PropertyInfo(alias="hostileFireType")]
    """The type of hostile fire received (SMALL ARMS, MORTAR, ARTILLERY, ROCKETS)."""


class BodyObjectiveAreaInfo(TypedDict, total=False):
    enemy_data: Annotated[Iterable[BodyObjectiveAreaInfoEnemyData], PropertyInfo(alias="enemyData")]
    """Information detailing knowledge of enemies in the area."""

    osc_call_sign: Annotated[str, PropertyInfo(alias="oscCallSign")]
    """The call sign of the on-scene commander."""

    osc_freq: Annotated[float, PropertyInfo(alias="oscFreq")]
    """The radio frequency of the on-scene commander."""

    pz_desc: Annotated[str, PropertyInfo(alias="pzDesc")]
    """Description of the pickup zone location."""

    pz_location: Annotated[Iterable[float], PropertyInfo(alias="pzLocation")]
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the pz location. This array must contain a
    minimum of 2 elements (latitude and longitude), and may contain an optional 3rd
    element (altitude).
    """


class Body(TypedDict, total=False):
    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    data_mode: Required[Annotated[Literal["REAL", "TEST", "SIMULATED", "EXERCISE"], PropertyInfo(alias="dataMode")]]
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

    msg_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="msgTime", format="iso8601")]]
    """Time stamp of the original personnel recovery message, in ISO 8601 UTC format."""

    pickup_lat: Required[Annotated[float, PropertyInfo(alias="pickupLat")]]
    """WGS-84 latitude of the pickup location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    pickup_lon: Required[Annotated[float, PropertyInfo(alias="pickupLon")]]
    """WGS-84 longitude of the pickup location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    source: Required[str]
    """Source of the data."""

    type: Required[str]
    """Specifies the type of incident resulting in a recovery or evacuation mission.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Emergency Type (e.g. NO
    STATEMENT, DOWN AIRCRAFT, MAN IN WATER, DITCHING, BAILOUT, DISTRESSED VEHICLE,
    GROUND INCIDENT, MEDICAL, ISOLATED PERSONS, etc.).
    """

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    auth_method: Annotated[str, PropertyInfo(alias="authMethod")]
    """Mechanism used to verify the survivors identity."""

    auth_status: Annotated[str, PropertyInfo(alias="authStatus")]
    """The confirmation status of the isolated personnel identity.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Authentication Status,
    Isolated Personnel (NO STATEMENT, AUTHENTICATED, NOT AUTHENTICATED,
    AUTHENTICATED UNDER DURESS, NOT APPLICABLE):

    AUTHENTICATED: Confirmed Friend

    NOT AUTHENTICATED: Unconfirmed status

    AUTHENTICATED UNDER DURESS: Authentication comprised by hostiles.

    NOT APPLICABLE: Authentication not required.
    """

    beacon_ind: Annotated[bool, PropertyInfo(alias="beaconInd")]
    """Flag indicating whether a radio identifier is reported."""

    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """The call sign of the personnel to be recovered."""

    comm_eq1: Annotated[str, PropertyInfo(alias="commEq1")]
    """Survivor communications equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Communications Equipment,
    Isolated Personnel (NO STATEMENT, SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL
    MIRROR, SMOKE FLARE, IR SIGNALLING DEVICE, SIGNALLING PANEL, FRIENDLY FORCE
    TRACKER, GPS BEACON, LL PHONE, TACTICAL RADIO LOS, TACTICAL RADIO BLOS).
    """

    comm_eq2: Annotated[str, PropertyInfo(alias="commEq2")]
    """Survivor communications equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Communications Equipment,
    Isolated Personnel (NO STATEMENT, SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL
    MIRROR, SMOKE FLARE, IR SIGNALLING DEVICE, SIGNALLING PANEL, FRIENDLY FORCE
    TRACKER, GPS BEACON, LL PHONE, TACTICAL RADIO LOS, TACTICAL RADIO BLOS).
    """

    comm_eq3: Annotated[str, PropertyInfo(alias="commEq3")]
    """Survivor communications equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Communications Equipment,
    Isolated Personnel (NO STATEMENT, SURVIVAL RADIO, RADIO BEACON, EPLRS, SIGNAL
    MIRROR, SMOKE FLARE, IR SIGNALLING DEVICE, SIGNALLING PANEL, FRIENDLY FORCE
    TRACKER, GPS BEACON, LL PHONE, TACTICAL RADIO LOS, TACTICAL RADIO BLOS).
    """

    execution_info: Annotated[BodyExecutionInfo, PropertyInfo(alias="executionInfo")]

    identity: str
    """
    The survivor service identity (UNKNOWN MILITARY, UNKNOWN CIVILIAN, FRIEND
    MILITARY, FRIEND CIVIILIAN, NEUTRAL MILITARY, NEUTRAL CIVILIAN, HOSTILE
    MILITARY, HOSTILE CIVILIAN).
    """

    id_weather_report: Annotated[str, PropertyInfo(alias="idWeatherReport")]
    """Unique identifier of a weather report associated with this recovery."""

    mil_class: Annotated[str, PropertyInfo(alias="milClass")]
    """The military classification of the personnel to be recovered.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Isolated Personnel
    Classification (NO STATEMENT, MILITARY, GOVERNMENT CIVILIAN, GOVERNMENT
    CONTRACTOR, CIVILIAN, MULTIPLE CLASSIFICATIONS).
    """

    nat_alliance: Annotated[int, PropertyInfo(alias="natAlliance")]
    """
    The country of origin or political entity of an isolated person subject to
    rescue or evacuation. If natAlliance is set to 126, then natAlliance1 must be
    non 0. If natAlliance is any number other than 126, then natAlliance1 will be
    set to 0 regardless. Defined in MIL-STD-6016 J6.1 Nationality/Alliance isolated
    person(s).
    """

    nat_alliance1: Annotated[int, PropertyInfo(alias="natAlliance1")]
    """
    Extended country of origin or political entity of an isolated person subject to
    rescue or evacuation. Specify an entry here only if natAlliance is 126. Defined
    in MIL-STD-6016 J6.1 Nationality/Alliance isolated person(s), 1.
    """

    num_ambulatory: Annotated[int, PropertyInfo(alias="numAmbulatory")]
    """Number of ambulatory personnel requiring recovery."""

    num_ambulatory_injured: Annotated[int, PropertyInfo(alias="numAmbulatoryInjured")]
    """Number of injured, but ambulatory, personnel requiring recovery."""

    num_non_ambulatory: Annotated[int, PropertyInfo(alias="numNonAmbulatory")]
    """Number of littered personnel requiring recovery."""

    num_persons: Annotated[int, PropertyInfo(alias="numPersons")]
    """The count of persons requiring recovery."""

    objective_area_info: Annotated[BodyObjectiveAreaInfo, PropertyInfo(alias="objectiveAreaInfo")]

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    pickup_alt: Annotated[float, PropertyInfo(alias="pickupAlt")]
    """Altitude relative to WGS-84 ellipsoid, in meters.

    Positive values indicate a point height above ellipsoid, and negative values
    indicate a point eight below ellipsoid.
    """

    recov_id: Annotated[str, PropertyInfo(alias="recovId")]
    """
    UUID identifying the Personnel Recovery mission, which should remain the same on
    subsequent posts related to the same recovery mission.
    """

    rx_freq: Annotated[float, PropertyInfo(alias="rxFreq")]
    """Receive voice frequency in 5Hz increments.

    This field will auto populate with the txFreq value if the post element is null.
    """

    survivor_messages: Annotated[str, PropertyInfo(alias="survivorMessages")]
    """Preloaded message conveying the situation confronting the isolated person(s).

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Survivor Radio Messages
    (e.g. INJURED CANT MOVE NO KNOWN HOSTILES, INJURED CANT MOVE HOSTILES NEARBY,
    UNINJURED CANT MOVE HOSTILES NEARBY, UNINJURED NO KNOWN HOSTILES, INJURED
    LIMITED MOBILITY).
    """

    survivor_radio: Annotated[str, PropertyInfo(alias="survivorRadio")]
    """Survivor radio equipment.

    Intended as, but not constrained to, MIL-STD-6016 J6.1 Survivor Radio Type (NO
    STATEMENT, PRQ7SEL, PRC90, PRC112, PRC112B B1, PRC112C, PRC112D, PRC148 MBITR,
    PRC148 JEM, PRC149, PRC152, ACRPLB, OTHER).
    """

    term_ind: Annotated[bool, PropertyInfo(alias="termInd")]
    """Flag indicating the cancellation of this recovery."""

    text_msg: Annotated[str, PropertyInfo(alias="textMsg")]
    """Additional specific messages received from survivor."""

    tx_freq: Annotated[float, PropertyInfo(alias="txFreq")]
    """Transmit voice frequency in 5Hz increments."""
