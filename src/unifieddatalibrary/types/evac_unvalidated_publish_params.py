# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EvacUnvalidatedPublishParams",
    "Body",
    "BodyCasualtyInfo",
    "BodyCasualtyInfoAllergy",
    "BodyCasualtyInfoCondition",
    "BodyCasualtyInfoEtiology",
    "BodyCasualtyInfoHealthState",
    "BodyCasualtyInfoInjury",
    "BodyCasualtyInfoMedication",
    "BodyCasualtyInfoTreatment",
    "BodyCasualtyInfoVitalSignData",
    "BodyEnemyData",
]


class EvacUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyCasualtyInfoAllergy(TypedDict, total=False):
    comments: str
    """Additional comments on the patient's allergy information."""

    type: str
    """Type of patient allergy (e.g. PENICILLIN, SULFA, OTHER)."""


class BodyCasualtyInfoCondition(TypedDict, total=False):
    body_part: Annotated[str, PropertyInfo(alias="bodyPart")]
    """Body part location or body part referenced in condition.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: str
    """Additional comments on the patient's condition."""

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Datetime of the condition diagnosis in ISO 8601 UTC datetime format."""

    type: str
    """Health condition assessment.

    Intended as, but not constrained to, K07.1 Condition Type Enumeration (e.g.
    ACTIVITY HIGH, ACTIVITY LOW, ACTIVITY MEDIUM, ACTIVITY NONE, AVPU ALERT, AVPU
    ALTERED MENTAL STATE, AVPU PAIN, AVPU UNRESPONSIVE, etc.).
    """


class BodyCasualtyInfoEtiology(TypedDict, total=False):
    body_part: Annotated[str, PropertyInfo(alias="bodyPart")]
    """The body part or location affected from the etiology.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: str
    """Additional comments on the patient's etiology information."""

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Datetime of the discovery of the etiology state in ISO 8601 UTC format."""

    type: str
    """The cause or manner of causation of the medical condition.

    Intended as, but not constrained to, K07.1 EtiologyType Enumeration (e.g.
    ASSAULT, BUILDING COLLAPSE, BURN CHEMICAL, BURN ELECTRICAL, BURN, BURN HOT
    LIQUID, BURN RADIATION, BURN THERMAL, etc.).
    """


class BodyCasualtyInfoHealthState(TypedDict, total=False):
    health_state_code: Annotated[str, PropertyInfo(alias="healthStateCode")]
    """Medical color code used to quickly identify various medical state (e.g.

    AMBER, BLACK, BLUE, GRAY, NORMAL, RED).
    """

    med_conf_factor: Annotated[int, PropertyInfo(alias="medConfFactor")]
    """Medical confidence factor."""

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Datetime of the health state diagnosis in ISO 8601 UTC datetime format."""

    type: str
    """
    Generalized state of health type (BIOLOGICAL, CHEMICAL, COGNITIVE, HYDRATION,
    LIFE SIGN, RADIATION, SHOCK, THERMAL).
    """


class BodyCasualtyInfoInjury(TypedDict, total=False):
    body_part: Annotated[str, PropertyInfo(alias="bodyPart")]
    """Body part location of the injury.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: str
    """Additional comments on the patient's injury information."""

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time of the injury, in ISO 8601 UTC format."""

    type: str
    """
    Classification of the injury type (ABRASION, AMPUTATION IT, AVULATION,
    BALLISTIC, BLAST WAVE, BURN 1ST DEGREE, BURN 2ND DEGREE, BURN 3RD DEGREE, BURN
    INHALATION, BURN LOWER AIRWAY, CHEST FLAIL, CHEST OPEN, DEGLOVING, ECCHYMOSIS,
    FRACTURE CLOSED, FRACTURE CREPITUS, FRACTURE IT, FRACTURE OPEN, HEMATOMA,
    IRREGULAR CONSISTENCY, IRREGULAR CONSISTENCY RIDGED, IRREGULAR CONSISTENCY
    SWOLLEN, IRREGULAR CONSISTENCY SWOLLEN DISTENDED, IRREGULAR CONSISTENCY TENDER,
    IRREGULAR POSITION, IRREGULAR SHAPE, IRREGULAR SHAPE MISSHAPED, IRREGULAR SHAPE
    NON SYMMETRICAL, LACERATION, NEUROVASCULAR COMPROMISE, NEUROVASCULAR INTACT,
    PUNCTURE, SEAT BELT SIGN, STAB, TIC TIM).
    """


class BodyCasualtyInfoMedication(TypedDict, total=False):
    admin_route: Annotated[str, PropertyInfo(alias="adminRoute")]
    """Route of medication delivery (e.g. INJECTION, ORAL, etc.)."""

    body_part: Annotated[str, PropertyInfo(alias="bodyPart")]
    """Body part location or body part referenced for medication.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: str
    """Additional comments on the patient's medication information."""

    dose: str
    """
    Quantity of medicine or drug administered or recommended to be taken at a
    particular time.
    """

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time that the medication was administered in ISO 8601 UTC format."""

    type: str
    """The type of medication administered.

    Intended as, but not constrained to, K07.1 Medication Enumeration (CEFOTETAN,
    ABRASION, ABX, AMOXILOXACIN, ANALGESIC, COLLOID, CRYOPECIPITATES, CRYSTALLOID,
    EPINEPHRINE, ERTAPENEM, FENTANYL, HEXTEND, LACTATED RINGERS, MOBIC, MORPHINE,
    NARCOTIC, NS, PENICILLIN, PLASMA, PLATELETS, PRBC, TYLENOL, WHOLE BLOOD MT).
    """


class BodyCasualtyInfoTreatment(TypedDict, total=False):
    body_part: Annotated[str, PropertyInfo(alias="bodyPart")]
    """Body part location or body part treated or to be treated.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: str
    """Additional comments on the patient's treatment information."""

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Datetime of the treatment in ISO 8601 UTC format."""

    type: str
    """Type of treatment administered or to be administered.

    Intended as, but not constrained to, K07.1 Treatment Type Enumeration (e.g.
    AIRWAY ADJUNCT, AIRWAY ASSISTED VENTILATION, AIRWAY COMBI TUBE USED, AIRWAY ET
    NT, AIRWAY INTUBATED, AIRWAY NPA OPA APPLIED, AIRWAY PATIENT, AIRWAY POSITIONAL,
    AIRWAY SURGICAL CRIC, BREATHING CHEST SEAL, BREATHING CHEST TUBE, etc.).
    """


class BodyCasualtyInfoVitalSignData(TypedDict, total=False):
    med_conf_factor: Annotated[int, PropertyInfo(alias="medConfFactor")]
    """Medical confidence factor."""

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Datetime of the vital sign measurement in ISO 8601 UTC datetime format."""

    vital_sign: Annotated[str, PropertyInfo(alias="vitalSign")]
    """Patient vital sign measured (e.g.

    HEART RATE, PULSE RATE, RESPIRATION RATE, TEMPERATURE CORE, etc.).
    """

    vital_sign1: Annotated[float, PropertyInfo(alias="vitalSign1")]
    """Vital sign value 1.

    The content of this field is dependent on the type of vital sign being measured
    (see the vitalSign field).
    """

    vital_sign2: Annotated[float, PropertyInfo(alias="vitalSign2")]
    """Vital sign value 2.

    The content of this field is dependent on the type of vital sign being measured
    (see the vitalSign field).
    """


class BodyCasualtyInfo(TypedDict, total=False):
    age: int
    """The patient age, in years."""

    allergy: Iterable[BodyCasualtyInfoAllergy]
    """Allergy information."""

    blood_type: Annotated[str, PropertyInfo(alias="bloodType")]
    """
    The patient blood type (A POS, B POS, AB POS, O POS, A NEG, B NEG, AB NEG, O
    NEG).
    """

    body_part: Annotated[str, PropertyInfo(alias="bodyPart")]
    """
    The body part involved for the patient (HEAD, NECK, ABDOMEN, UPPER EXTREMITIES,
    BACK, FACE, LOWER EXTREMITIES, FRONT, OBSTETRICAL GYNECOLOGICAL, OTHER BODY
    PART).
    """

    burial_location: Annotated[Iterable[float], PropertyInfo(alias="burialLocation")]
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the burial location. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """The call sign of this patient."""

    care_provider_urn: Annotated[str, PropertyInfo(alias="careProviderUrn")]
    """Unique identifier for the patient care provider."""

    casualty_key: Annotated[str, PropertyInfo(alias="casualtyKey")]
    """Optional casualty key."""

    casualty_type: Annotated[str, PropertyInfo(alias="casualtyType")]
    """
    The type of medical issue resulting in the need to evacuate the patient (NON
    BATTLE, CUT, BURN, SICK, FRACTURE, AMPUTATION, PERFORATION, NUCLEAR, EXHAUSTION,
    BIOLOGICAL, CHEMICAL, SHOCK, PUNCTURE WOUND, OTHER CUT, WOUNDED IN ACTION,
    DENIAL, COMBAT STRESS).
    """

    collection_point: Annotated[Iterable[float], PropertyInfo(alias="collectionPoint")]
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the collection point. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    comments: str
    """Additional comments on the patient's casualty information."""

    condition: Iterable[BodyCasualtyInfoCondition]
    """Health condition information."""

    contam_type: Annotated[str, PropertyInfo(alias="contamType")]
    """
    The contamination specified for the patient (NONE, RADIATION, BIOLOGICAL,
    CHEMICAL).
    """

    disposition: str
    """
    The patient's general medical state (SICK IN QUARTERS, RETURN TO DUTY, EVACUATE
    WOUNDED, EVACUATE DECEASED, INTERRED).
    """

    disposition_type: Annotated[str, PropertyInfo(alias="dispositionType")]
    """
    The expected disposition of this patient (R T D, EVACUATE, EVACUATE TO FORWARD
    SURGICAL TEAM, EVACUATE TO COMBAT SUPPORT HOSPITAL, EVACUATE TO AERO MEDICAL
    STAGING FACILITY, EVACUATE TO SUSTAINING BASE MEDICAL TREATMENT FACILITY).
    """

    etiology: Iterable[BodyCasualtyInfoEtiology]
    """Medical condition causation information."""

    evac_type: Annotated[str, PropertyInfo(alias="evacType")]
    """The required evacuation method for this patient (AIR, GROUND, NOT EVACUATED)."""

    gender: str
    """The patient sex (MALE, FEMALE)."""

    health_state: Annotated[Iterable[BodyCasualtyInfoHealthState], PropertyInfo(alias="healthState")]
    """Health state information."""

    injury: Iterable[BodyCasualtyInfoInjury]
    """Injury specifics."""

    last4_ssn: Annotated[str, PropertyInfo(alias="last4SSN")]
    """Last 4 characters of the patient social security code, or equivalent."""

    medication: Iterable[BodyCasualtyInfoMedication]
    """Medication specifics."""

    name: str
    """The patient common or legal name."""

    nationality: str
    """The country code indicating the citizenship of the patient."""

    occ_speciality: Annotated[str, PropertyInfo(alias="occSpeciality")]
    """The career field of this patient."""

    patient_identity: Annotated[str, PropertyInfo(alias="patientIdentity")]
    """
    The patient service identity (UNKNOWN MILITARY, UNKNOWN CIVILIAN, FRIEND
    MILITARY, FRIEND CIVILIAN, NEUTRAL MILITARY, NEUTRAL CIVILIAN, HOSTILE MILITARY,
    HOSTILE CIVILIAN).
    """

    patient_status: Annotated[str, PropertyInfo(alias="patientStatus")]
    """
    The patient service status (US MILITARY, US CIVILIAN, NON US MILITARY, NON US
    CIVILIAN, ENEMY POW).
    """

    pay_grade: Annotated[str, PropertyInfo(alias="payGrade")]
    """
    The patient pay grade or rank designation (O-10, O-9, O-8, O-7, O-6, O-5, O-4,
    O-3, O-2, O-1, CWO-5, CWO-4, CWO-2, CWO-1, E -9, E-8, E-7, E-6, E-5, E-4, E-3,
    E-2, E-1, NONE, CIVILIAN).
    """

    priority: str
    """
    The priority of the medevac mission for this patient (URGENT, PRIORITY, ROUTINE,
    URGENT SURGERY, CONVENIENCE).
    """

    report_gen: Annotated[str, PropertyInfo(alias="reportGen")]
    """
    The method used to generate this medevac report (DEVICE, GROUND COMBAT
    PERSONNEL, EVACUATION PERSONNEL, ECHELON1 PERSONNEL, ECHELON2 PERSONNEL).
    """

    report_time: Annotated[Union[str, datetime], PropertyInfo(alias="reportTime", format="iso8601")]
    """
    Datetime of the compiling of the patients casualty report, in ISO 8601 UTC
    format.
    """

    service: str
    """
    The patient branch of service (AIR FORCE, ARMY, NAVY, MARINES, CIV, CONTR,
    UNKNOWN SERVICE).
    """

    spec_med_equip: Annotated[List[str], PropertyInfo(alias="specMedEquip")]
    """
    Array specifying if any special equipment is need for each of the evacuation of
    this patient (EXTRACTION EQUIPMENT, SEMI RIGID LITTER, BACKBOARD, CERVICAL
    COLLAR ,JUNGLE PENETRATOR, OXYGEN, WHOLE BLOOD, VENTILATOR, HOIST, NONE).
    """

    treatment: Iterable[BodyCasualtyInfoTreatment]
    """Treatment information."""

    vital_sign_data: Annotated[Iterable[BodyCasualtyInfoVitalSignData], PropertyInfo(alias="vitalSignData")]
    """Information obtained for vital signs."""


class BodyEnemyData(TypedDict, total=False):
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

    pickup_lat: Required[Annotated[float, PropertyInfo(alias="pickupLat")]]
    """WGS-84 latitude of the pickup location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    pickup_lon: Required[Annotated[float, PropertyInfo(alias="pickupLon")]]
    """WGS-84 longitude of the pickup location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    req_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="reqTime", format="iso8601")]]
    """The request time, in ISO 8601 UTC format."""

    source: Required[str]
    """Source of the data."""

    type: Required[Literal["REQUEST", "RESPONSE"]]
    """The type of this medevac record (REQUEST, RESPONSE)."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    casualty_info: Annotated[Iterable[BodyCasualtyInfo], PropertyInfo(alias="casualtyInfo")]
    """Identity and medical information on the patient to be evacuated."""

    ce: float
    """
    Radius of circular area about lat/lon point, in meters (1-sigma, if representing
    error).
    """

    cntct_freq: Annotated[float, PropertyInfo(alias="cntctFreq")]
    """The contact frequency, in Hz, of the agency or zone controller."""

    comments: str
    """Additional comments for the medevac mission."""

    enemy_data: Annotated[Iterable[BodyEnemyData], PropertyInfo(alias="enemyData")]
    """Data defining any enemy intelligence reported by the requestor."""

    id_weather_report: Annotated[str, PropertyInfo(alias="idWeatherReport")]
    """Unique identifier of a weather report associated with this evacuation."""

    le: float
    """Height above lat/lon point, in meters (1-sigma, if representing linear error)."""

    medevac_id: Annotated[str, PropertyInfo(alias="medevacId")]
    """
    UUID identifying the medevac mission, which should remain the same on subsequent
    posts related to the same medevac mission.
    """

    medic_req: Annotated[bool, PropertyInfo(alias="medicReq")]
    """Flag indicating whether the mission requires medical personnel."""

    mission_type: Annotated[str, PropertyInfo(alias="missionType")]
    """The operation type of the evacuation. (NOT SPECIFIED, AIR, GROUND, SURFACE)."""

    num_ambulatory: Annotated[int, PropertyInfo(alias="numAmbulatory")]
    """Number of ambulatory personnel requiring evacuation."""

    num_casualties: Annotated[int, PropertyInfo(alias="numCasualties")]
    """The count of people requiring medevac."""

    num_kia: Annotated[int, PropertyInfo(alias="numKIA")]
    """Number of people Killed In Action."""

    num_litter: Annotated[int, PropertyInfo(alias="numLitter")]
    """Number of littered personnel requiring evacuation."""

    num_wia: Annotated[int, PropertyInfo(alias="numWIA")]
    """Number of people Wounded In Action."""

    obstacles_remarks: Annotated[str, PropertyInfo(alias="obstaclesRemarks")]
    """
    Amplifying data for the terrain describing important obstacles in or around the
    zone.
    """

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
    indicate a point height below ellipsoid.
    """

    pickup_time: Annotated[Union[str, datetime], PropertyInfo(alias="pickupTime", format="iso8601")]
    """The expected pickup time, in ISO 8601 UTC format."""

    req_call_sign: Annotated[str, PropertyInfo(alias="reqCallSign")]
    """The call sign of this medevac requestor."""

    req_num: Annotated[str, PropertyInfo(alias="reqNum")]
    """Externally provided Medevac request number (e.g. MED.1.223908)."""

    terrain: str
    """
    Short description of the terrain features of the pickup location (WOODS, TREES,
    PLOWED FIELDS, FLAT, STANDING WATER, MARSH, URBAN BUILT-UP AREA, MOUNTAIN, HILL,
    SAND TD, ROCKY, VALLEY, METAMORPHIC ICE, UNKNOWN TD, SEA, NO STATEMENT).
    """

    terrain_remarks: Annotated[str, PropertyInfo(alias="terrainRemarks")]
    """
    Amplifying data for the terrain describing any notable additional terrain
    features.
    """

    zone_contr_call_sign: Annotated[str, PropertyInfo(alias="zoneContrCallSign")]
    """The call sign of the zone controller."""

    zone_hot: Annotated[bool, PropertyInfo(alias="zoneHot")]
    """Flag indicating that the pickup site is hot and hostiles are in the area."""

    zone_marking: Annotated[str, PropertyInfo(alias="zoneMarking")]
    """
    The expected marker identifying the pickup site (SMOKE ZONE MARKING, FLARES,
    MIRROR, GLIDE ANGLE INDICATOR LIGHT, LIGHT ZONE MARKING, PANELS, FIRE, LASER
    DESIGNATOR, STROBE LIGHTS, VEHICLE LIGHTS, COLORED SMOKE, WHITE PHOSPHERUS,
    INFRARED, ILLUMINATION, FRATRICIDE FENCE).
    """

    zone_marking_color: Annotated[str, PropertyInfo(alias="zoneMarkingColor")]
    """
    Color used for the pickup site marking (RED, WHITE, BLUE, YELLOW, GREEN, ORANGE,
    BLACK, PURPLE, BROWN, TAN, GRAY, SILVER, CAMOUFLAGE, OTHER COLOR).
    """

    zone_name: Annotated[str, PropertyInfo(alias="zoneName")]
    """The name of the zone."""

    zone_security: Annotated[str, PropertyInfo(alias="zoneSecurity")]
    """
    The pickup site security (UNKNOWN ZONESECURITY, NO ENEMY, POSSIBLE ENEMY, ENEMY
    IN AREA USE CAUTION, ENEMY IN AREA ARMED ESCORT REQUIRED).
    """
