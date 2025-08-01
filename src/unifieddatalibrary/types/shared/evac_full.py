# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .related_document_full import RelatedDocumentFull

__all__ = [
    "EvacFull",
    "CasualtyInfo",
    "CasualtyInfoAllergy",
    "CasualtyInfoCondition",
    "CasualtyInfoEtiology",
    "CasualtyInfoHealthState",
    "CasualtyInfoInjury",
    "CasualtyInfoMedication",
    "CasualtyInfoTreatment",
    "CasualtyInfoVitalSignData",
    "EnemyData",
]


class CasualtyInfoAllergy(BaseModel):
    comments: Optional[str] = None
    """Additional comments on the patient's allergy information."""

    type: Optional[str] = None
    """Type of patient allergy (e.g. PENICILLIN, SULFA, OTHER)."""


class CasualtyInfoCondition(BaseModel):
    body_part: Optional[str] = FieldInfo(alias="bodyPart", default=None)
    """Body part location or body part referenced in condition.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: Optional[str] = None
    """Additional comments on the patient's condition."""

    time: Optional[datetime] = None
    """Datetime of the condition diagnosis in ISO 8601 UTC datetime format."""

    type: Optional[str] = None
    """Health condition assessment.

    Intended as, but not constrained to, K07.1 Condition Type Enumeration (e.g.
    ACTIVITY HIGH, ACTIVITY LOW, ACTIVITY MEDIUM, ACTIVITY NONE, AVPU ALERT, AVPU
    ALTERED MENTAL STATE, AVPU PAIN, AVPU UNRESPONSIVE, etc.).
    """


class CasualtyInfoEtiology(BaseModel):
    body_part: Optional[str] = FieldInfo(alias="bodyPart", default=None)
    """The body part or location affected from the etiology.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: Optional[str] = None
    """Additional comments on the patient's etiology information."""

    time: Optional[datetime] = None
    """Datetime of the discovery of the etiology state in ISO 8601 UTC format."""

    type: Optional[str] = None
    """The cause or manner of causation of the medical condition.

    Intended as, but not constrained to, K07.1 EtiologyType Enumeration (e.g.
    ASSAULT, BUILDING COLLAPSE, BURN CHEMICAL, BURN ELECTRICAL, BURN, BURN HOT
    LIQUID, BURN RADIATION, BURN THERMAL, etc.).
    """


class CasualtyInfoHealthState(BaseModel):
    health_state_code: Optional[str] = FieldInfo(alias="healthStateCode", default=None)
    """Medical color code used to quickly identify various medical state (e.g.

    AMBER, BLACK, BLUE, GRAY, NORMAL, RED).
    """

    med_conf_factor: Optional[int] = FieldInfo(alias="medConfFactor", default=None)
    """Medical confidence factor."""

    time: Optional[datetime] = None
    """Datetime of the health state diagnosis in ISO 8601 UTC datetime format."""

    type: Optional[str] = None
    """
    Generalized state of health type (BIOLOGICAL, CHEMICAL, COGNITIVE, HYDRATION,
    LIFE SIGN, RADIATION, SHOCK, THERMAL).
    """


class CasualtyInfoInjury(BaseModel):
    body_part: Optional[str] = FieldInfo(alias="bodyPart", default=None)
    """Body part location of the injury.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: Optional[str] = None
    """Additional comments on the patient's injury information."""

    time: Optional[datetime] = None
    """The time of the injury, in ISO 8601 UTC format."""

    type: Optional[str] = None
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


class CasualtyInfoMedication(BaseModel):
    admin_route: Optional[str] = FieldInfo(alias="adminRoute", default=None)
    """Route of medication delivery (e.g. INJECTION, ORAL, etc.)."""

    body_part: Optional[str] = FieldInfo(alias="bodyPart", default=None)
    """Body part location or body part referenced for medication.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: Optional[str] = None
    """Additional comments on the patient's medication information."""

    dose: Optional[str] = None
    """
    Quantity of medicine or drug administered or recommended to be taken at a
    particular time.
    """

    time: Optional[datetime] = None
    """The time that the medication was administered in ISO 8601 UTC format."""

    type: Optional[str] = None
    """The type of medication administered.

    Intended as, but not constrained to, K07.1 Medication Enumeration (CEFOTETAN,
    ABRASION, ABX, AMOXILOXACIN, ANALGESIC, COLLOID, CRYOPECIPITATES, CRYSTALLOID,
    EPINEPHRINE, ERTAPENEM, FENTANYL, HEXTEND, LACTATED RINGERS, MOBIC, MORPHINE,
    NARCOTIC, NS, PENICILLIN, PLASMA, PLATELETS, PRBC, TYLENOL, WHOLE BLOOD MT).
    """


class CasualtyInfoTreatment(BaseModel):
    body_part: Optional[str] = FieldInfo(alias="bodyPart", default=None)
    """Body part location or body part treated or to be treated.

    Intended as, but not constrained to, K07.1 Body Location Enumeration (e.g. ANKLE
    LEFT BACK, ANKLE LEFT FRONT, ANKLE RIGHT BACK, ANKLE RIGHT FRONT, ARM LEFT BACK,
    ARM LEFT ELBOW BACK, ARM LEFT ELBOW FRONT, ARM LEFT FRONT, ARM LEFT LOWER BACK,
    etc.).
    """

    comments: Optional[str] = None
    """Additional comments on the patient's treatment information."""

    time: Optional[datetime] = None
    """Datetime of the treatment in ISO 8601 UTC format."""

    type: Optional[str] = None
    """Type of treatment administered or to be administered.

    Intended as, but not constrained to, K07.1 Treatment Type Enumeration (e.g.
    AIRWAY ADJUNCT, AIRWAY ASSISTED VENTILATION, AIRWAY COMBI TUBE USED, AIRWAY ET
    NT, AIRWAY INTUBATED, AIRWAY NPA OPA APPLIED, AIRWAY PATIENT, AIRWAY POSITIONAL,
    AIRWAY SURGICAL CRIC, BREATHING CHEST SEAL, BREATHING CHEST TUBE, etc.).
    """


class CasualtyInfoVitalSignData(BaseModel):
    med_conf_factor: Optional[int] = FieldInfo(alias="medConfFactor", default=None)
    """Medical confidence factor."""

    time: Optional[datetime] = None
    """Datetime of the vital sign measurement in ISO 8601 UTC datetime format."""

    vital_sign: Optional[str] = FieldInfo(alias="vitalSign", default=None)
    """Patient vital sign measured (e.g.

    HEART RATE, PULSE RATE, RESPIRATION RATE, TEMPERATURE CORE, etc.).
    """

    vital_sign1: Optional[float] = FieldInfo(alias="vitalSign1", default=None)
    """Vital sign value 1.

    The content of this field is dependent on the type of vital sign being measured
    (see the vitalSign field).
    """

    vital_sign2: Optional[float] = FieldInfo(alias="vitalSign2", default=None)
    """Vital sign value 2.

    The content of this field is dependent on the type of vital sign being measured
    (see the vitalSign field).
    """


class CasualtyInfo(BaseModel):
    age: Optional[int] = None
    """The patient age, in years."""

    allergy: Optional[List[CasualtyInfoAllergy]] = None
    """Allergy information."""

    blood_type: Optional[str] = FieldInfo(alias="bloodType", default=None)
    """
    The patient blood type (A POS, B POS, AB POS, O POS, A NEG, B NEG, AB NEG, O
    NEG).
    """

    body_part: Optional[str] = FieldInfo(alias="bodyPart", default=None)
    """
    The body part involved for the patient (HEAD, NECK, ABDOMEN, UPPER EXTREMITIES,
    BACK, FACE, LOWER EXTREMITIES, FRONT, OBSTETRICAL GYNECOLOGICAL, OTHER BODY
    PART).
    """

    burial_location: Optional[List[float]] = FieldInfo(alias="burialLocation", default=None)
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the burial location. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign of this patient."""

    care_provider_urn: Optional[str] = FieldInfo(alias="careProviderUrn", default=None)
    """Unique identifier for the patient care provider."""

    casualty_key: Optional[str] = FieldInfo(alias="casualtyKey", default=None)
    """Optional casualty key."""

    casualty_type: Optional[str] = FieldInfo(alias="casualtyType", default=None)
    """
    The type of medical issue resulting in the need to evacuate the patient (NON
    BATTLE, CUT, BURN, SICK, FRACTURE, AMPUTATION, PERFORATION, NUCLEAR, EXHAUSTION,
    BIOLOGICAL, CHEMICAL, SHOCK, PUNCTURE WOUND, OTHER CUT, WOUNDED IN ACTION,
    DENIAL, COMBAT STRESS).
    """

    collection_point: Optional[List[float]] = FieldInfo(alias="collectionPoint", default=None)
    """
    Array of the WGS-84 latitude (-90 to 90, negative values south of the equator)
    in degrees, longitude (-180 to 180, negative values west of Prime Meridian) in
    degrees, and altitude, in meters, of the collection point. This array must
    contain a minimum of 2 elements (latitude and longitude), and may contain an
    optional 3rd element (altitude).
    """

    comments: Optional[str] = None
    """Additional comments on the patient's casualty information."""

    condition: Optional[List[CasualtyInfoCondition]] = None
    """Health condition information."""

    contam_type: Optional[str] = FieldInfo(alias="contamType", default=None)
    """
    The contamination specified for the patient (NONE, RADIATION, BIOLOGICAL,
    CHEMICAL).
    """

    disposition: Optional[str] = None
    """
    The patient's general medical state (SICK IN QUARTERS, RETURN TO DUTY, EVACUATE
    WOUNDED, EVACUATE DECEASED, INTERRED).
    """

    disposition_type: Optional[str] = FieldInfo(alias="dispositionType", default=None)
    """
    The expected disposition of this patient (R T D, EVACUATE, EVACUATE TO FORWARD
    SURGICAL TEAM, EVACUATE TO COMBAT SUPPORT HOSPITAL, EVACUATE TO AERO MEDICAL
    STAGING FACILITY, EVACUATE TO SUSTAINING BASE MEDICAL TREATMENT FACILITY).
    """

    etiology: Optional[List[CasualtyInfoEtiology]] = None
    """Medical condition causation information."""

    evac_type: Optional[str] = FieldInfo(alias="evacType", default=None)
    """The required evacuation method for this patient (AIR, GROUND, NOT EVACUATED)."""

    gender: Optional[str] = None
    """The patient sex (MALE, FEMALE)."""

    health_state: Optional[List[CasualtyInfoHealthState]] = FieldInfo(alias="healthState", default=None)
    """Health state information."""

    injury: Optional[List[CasualtyInfoInjury]] = None
    """Injury specifics."""

    last4_ssn: Optional[str] = FieldInfo(alias="last4SSN", default=None)
    """Last 4 characters of the patient social security code, or equivalent."""

    medication: Optional[List[CasualtyInfoMedication]] = None
    """Medication specifics."""

    name: Optional[str] = None
    """The patient common or legal name."""

    nationality: Optional[str] = None
    """The country code indicating the citizenship of the patient."""

    occ_speciality: Optional[str] = FieldInfo(alias="occSpeciality", default=None)
    """The career field of this patient."""

    patient_identity: Optional[str] = FieldInfo(alias="patientIdentity", default=None)
    """
    The patient service identity (UNKNOWN MILITARY, UNKNOWN CIVILIAN, FRIEND
    MILITARY, FRIEND CIVILIAN, NEUTRAL MILITARY, NEUTRAL CIVILIAN, HOSTILE MILITARY,
    HOSTILE CIVILIAN).
    """

    patient_status: Optional[str] = FieldInfo(alias="patientStatus", default=None)
    """
    The patient service status (US MILITARY, US CIVILIAN, NON US MILITARY, NON US
    CIVILIAN, ENEMY POW).
    """

    pay_grade: Optional[str] = FieldInfo(alias="payGrade", default=None)
    """
    The patient pay grade or rank designation (O-10, O-9, O-8, O-7, O-6, O-5, O-4,
    O-3, O-2, O-1, CWO-5, CWO-4, CWO-2, CWO-1, E -9, E-8, E-7, E-6, E-5, E-4, E-3,
    E-2, E-1, NONE, CIVILIAN).
    """

    priority: Optional[str] = None
    """
    The priority of the medevac mission for this patient (URGENT, PRIORITY, ROUTINE,
    URGENT SURGERY, CONVENIENCE).
    """

    report_gen: Optional[str] = FieldInfo(alias="reportGen", default=None)
    """
    The method used to generate this medevac report (DEVICE, GROUND COMBAT
    PERSONNEL, EVACUATION PERSONNEL, ECHELON1 PERSONNEL, ECHELON2 PERSONNEL).
    """

    report_time: Optional[datetime] = FieldInfo(alias="reportTime", default=None)
    """
    Datetime of the compiling of the patients casualty report, in ISO 8601 UTC
    format.
    """

    service: Optional[str] = None
    """
    The patient branch of service (AIR FORCE, ARMY, NAVY, MARINES, CIV, CONTR,
    UNKNOWN SERVICE).
    """

    spec_med_equip: Optional[List[str]] = FieldInfo(alias="specMedEquip", default=None)
    """
    Array specifying if any special equipment is need for each of the evacuation of
    this patient (EXTRACTION EQUIPMENT, SEMI RIGID LITTER, BACKBOARD, CERVICAL
    COLLAR ,JUNGLE PENETRATOR, OXYGEN, WHOLE BLOOD, VENTILATOR, HOIST, NONE).
    """

    treatment: Optional[List[CasualtyInfoTreatment]] = None
    """Treatment information."""

    vital_sign_data: Optional[List[CasualtyInfoVitalSignData]] = FieldInfo(alias="vitalSignData", default=None)
    """Information obtained for vital signs."""


class EnemyData(BaseModel):
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


class EvacFull(BaseModel):
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

    pickup_lat: float = FieldInfo(alias="pickupLat")
    """WGS-84 latitude of the pickup location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    pickup_lon: float = FieldInfo(alias="pickupLon")
    """WGS-84 longitude of the pickup location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    req_time: datetime = FieldInfo(alias="reqTime")
    """The request time, in ISO 8601 UTC format."""

    source: str
    """Source of the data."""

    type: Literal["REQUEST", "RESPONSE"]
    """The type of this medevac record (REQUEST, RESPONSE)."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    casualty_info: Optional[List[CasualtyInfo]] = FieldInfo(alias="casualtyInfo", default=None)
    """Identity and medical information on the patient to be evacuated."""

    ce: Optional[float] = None
    """
    Radius of circular area about lat/lon point, in meters (1-sigma, if representing
    error).
    """

    cntct_freq: Optional[float] = FieldInfo(alias="cntctFreq", default=None)
    """The contact frequency, in Hz, of the agency or zone controller."""

    comments: Optional[str] = None
    """Additional comments for the medevac mission."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    enemy_data: Optional[List[EnemyData]] = FieldInfo(alias="enemyData", default=None)
    """Data defining any enemy intelligence reported by the requestor."""

    id_weather_report: Optional[str] = FieldInfo(alias="idWeatherReport", default=None)
    """Unique identifier of a weather report associated with this evacuation."""

    le: Optional[float] = None
    """Height above lat/lon point, in meters (1-sigma, if representing linear error)."""

    medevac_id: Optional[str] = FieldInfo(alias="medevacId", default=None)
    """
    UUID identifying the medevac mission, which should remain the same on subsequent
    posts related to the same medevac mission.
    """

    medic_req: Optional[bool] = FieldInfo(alias="medicReq", default=None)
    """Flag indicating whether the mission requires medical personnel."""

    mission_type: Optional[str] = FieldInfo(alias="missionType", default=None)
    """The operation type of the evacuation. (NOT SPECIFIED, AIR, GROUND, SURFACE)."""

    num_ambulatory: Optional[int] = FieldInfo(alias="numAmbulatory", default=None)
    """Number of ambulatory personnel requiring evacuation."""

    num_casualties: Optional[int] = FieldInfo(alias="numCasualties", default=None)
    """The count of people requiring medevac."""

    num_kia: Optional[int] = FieldInfo(alias="numKIA", default=None)
    """Number of people Killed In Action."""

    num_litter: Optional[int] = FieldInfo(alias="numLitter", default=None)
    """Number of littered personnel requiring evacuation."""

    num_wia: Optional[int] = FieldInfo(alias="numWIA", default=None)
    """Number of people Wounded In Action."""

    obstacles_remarks: Optional[str] = FieldInfo(alias="obstaclesRemarks", default=None)
    """
    Amplifying data for the terrain describing important obstacles in or around the
    zone.
    """

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
    indicate a point height below ellipsoid.
    """

    pickup_time: Optional[datetime] = FieldInfo(alias="pickupTime", default=None)
    """The expected pickup time, in ISO 8601 UTC format."""

    related_docs: Optional[List[RelatedDocumentFull]] = FieldInfo(alias="relatedDocs", default=None)
    """Related document ids."""

    req_call_sign: Optional[str] = FieldInfo(alias="reqCallSign", default=None)
    """The call sign of this medevac requestor."""

    req_num: Optional[str] = FieldInfo(alias="reqNum", default=None)
    """Externally provided Medevac request number (e.g. MED.1.223908)."""

    terrain: Optional[str] = None
    """
    Short description of the terrain features of the pickup location (WOODS, TREES,
    PLOWED FIELDS, FLAT, STANDING WATER, MARSH, URBAN BUILT-UP AREA, MOUNTAIN, HILL,
    SAND TD, ROCKY, VALLEY, METAMORPHIC ICE, UNKNOWN TD, SEA, NO STATEMENT).
    """

    terrain_remarks: Optional[str] = FieldInfo(alias="terrainRemarks", default=None)
    """
    Amplifying data for the terrain describing any notable additional terrain
    features.
    """

    zone_contr_call_sign: Optional[str] = FieldInfo(alias="zoneContrCallSign", default=None)
    """The call sign of the zone controller."""

    zone_hot: Optional[bool] = FieldInfo(alias="zoneHot", default=None)
    """Flag indicating that the pickup site is hot and hostiles are in the area."""

    zone_marking: Optional[str] = FieldInfo(alias="zoneMarking", default=None)
    """
    The expected marker identifying the pickup site (SMOKE ZONE MARKING, FLARES,
    MIRROR, GLIDE ANGLE INDICATOR LIGHT, LIGHT ZONE MARKING, PANELS, FIRE, LASER
    DESIGNATOR, STROBE LIGHTS, VEHICLE LIGHTS, COLORED SMOKE, WHITE PHOSPHERUS,
    INFRARED, ILLUMINATION, FRATRICIDE FENCE).
    """

    zone_marking_color: Optional[str] = FieldInfo(alias="zoneMarkingColor", default=None)
    """
    Color used for the pickup site marking (RED, WHITE, BLUE, YELLOW, GREEN, ORANGE,
    BLACK, PURPLE, BROWN, TAN, GRAY, SILVER, CAMOUFLAGE, OTHER COLOR).
    """

    zone_name: Optional[str] = FieldInfo(alias="zoneName", default=None)
    """The name of the zone."""

    zone_security: Optional[str] = FieldInfo(alias="zoneSecurity", default=None)
    """
    The pickup site security (UNKNOWN ZONESECURITY, NO ENEMY, POSSIBLE ENEMY, ENEMY
    IN AREA USE CAUTION, ENEMY IN AREA ARMED ESCORT REQUIRED).
    """
