# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AirTransportMissionAbridged", "HazMat", "Remark", "Requirement"]


class HazMat(BaseModel):
    applicable_notes: Optional[str] = FieldInfo(alias="applicableNotes", default=None)
    """
    Comma delimited list of Note IDs for Item Class Segregation groups, specific to
    GDSS systems.
    """

    cgc: Optional[str] = None
    """
    Compatibility group code used to specify the controls for the transportation and
    storage of hazardous materials according to the Hazardous Materials Regulations
    issued by the U.S. Department of Transportation.
    """

    cgn: Optional[str] = None
    """
    Comma delimited list of Note IDs for compatibility groups, specific to GDSS
    systems.
    """

    class_div: Optional[float] = FieldInfo(alias="classDiv", default=None)
    """
    Class and division of the hazardous material according to the Hazardous
    Materials Regulations issued by the U.S. Department of Transportation.
    """

    ext_haz_mat_id: Optional[str] = FieldInfo(alias="extHazMatId", default=None)
    """The hazMat identifier provided by the originating source."""

    item_name: Optional[str] = FieldInfo(alias="itemName", default=None)
    """
    United Nations proper shipping name of the hazardous material according to the
    Hazardous Materials Regulations issued by the U.S. Department of Transportation.
    """

    net_exp_wt: Optional[float] = FieldInfo(alias="netExpWt", default=None)
    """Net explosive weight of the hazardous material, in kilograms."""

    off_icao: Optional[str] = FieldInfo(alias="offICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    hazardous material is unloaded.
    """

    off_itin: Optional[int] = FieldInfo(alias="offItin", default=None)
    """Itinerary number that identifies where the hazardous material is unloaded."""

    on_icao: Optional[str] = FieldInfo(alias="onICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    hazardous material is loaded.
    """

    on_itin: Optional[int] = FieldInfo(alias="onItin", default=None)
    """Itinerary number that identifies where the hazardous material is loaded."""

    pieces: Optional[int] = None
    """Number of pieces of hazardous cargo."""

    planned: Optional[str] = None
    """
    Flag indicating if hazardous material is associated with this air transport
    mission. Possible values are P (planned to be associated with the mission) or A
    (actually associated with the mission). Enum: [P, A].
    """

    un_num: Optional[str] = FieldInfo(alias="unNum", default=None)
    """
    United Nations number or North America number that identifies hazardous
    materials according to the Hazardous Materials Regulations issued by the U.S.
    Department of Transportation.
    """

    weight: Optional[float] = None
    """Total weight of hazardous cargo, including non-explosive parts, in kilograms."""


class Remark(BaseModel):
    date: Optional[datetime] = None
    """
    Date the remark was published, in ISO 8601 UTC format, with millisecond
    precision.
    """

    gdss_remark_id: Optional[str] = FieldInfo(alias="gdssRemarkId", default=None)
    """Global Decision Support System (GDSS) remark identifier."""

    itinerary_num: Optional[int] = FieldInfo(alias="itineraryNum", default=None)
    """
    If the remark is sortie specific, this is the number of the sortie it applies
    to.
    """

    text: Optional[str] = None
    """Text of the remark."""

    type: Optional[str] = None
    """Remark type."""

    user: Optional[str] = None
    """User who published the remark."""


class Requirement(BaseModel):
    bulk_weight: Optional[float] = FieldInfo(alias="bulkWeight", default=None)
    """Total weight of the bulk cargo, in kilograms."""

    ead: Optional[datetime] = None
    """
    Earliest available date the cargo can be picked up, in ISO 8601 UTC format with
    millisecond precision.
    """

    gdss_req_id: Optional[str] = FieldInfo(alias="gdssReqId", default=None)
    """Global Decision Support System (GDSS) mission requirement identifier."""

    lad: Optional[datetime] = None
    """
    Latest available date the cargo may be delivered, in ISO 8601 UTC format with
    millisecond precision.
    """

    num_ambulatory: Optional[int] = FieldInfo(alias="numAmbulatory", default=None)
    """Number of ambulatory patients tasked for the mission."""

    num_attendant: Optional[int] = FieldInfo(alias="numAttendant", default=None)
    """Number of attendants tasked for the mission."""

    num_litter: Optional[int] = FieldInfo(alias="numLitter", default=None)
    """Number of litter patients tasked for the mission."""

    num_pax: Optional[int] = FieldInfo(alias="numPax", default=None)
    """Number of passengers associated with the mission."""

    offload_id: Optional[int] = FieldInfo(alias="offloadId", default=None)
    """Identifier of the offload itinerary location."""

    offload_lo_code: Optional[str] = FieldInfo(alias="offloadLOCode", default=None)
    """Offload location code."""

    onload_id: Optional[int] = FieldInfo(alias="onloadId", default=None)
    """Identifier of the onload itinerary location."""

    onload_lo_code: Optional[str] = FieldInfo(alias="onloadLOCode", default=None)
    """Onload location code."""

    oplan: Optional[str] = None
    """
    Identification number of the Operation Plan (OPLAN) associated with this
    mission.
    """

    outsize_weight: Optional[float] = FieldInfo(alias="outsizeWeight", default=None)
    """Total weight of the outsize cargo, in kilograms."""

    oversize_weight: Optional[float] = FieldInfo(alias="oversizeWeight", default=None)
    """Total weight of the oversized cargo, in kilograms."""

    proj_name: Optional[str] = FieldInfo(alias="projName", default=None)
    """Project name."""

    trans_req_num: Optional[str] = FieldInfo(alias="transReqNum", default=None)
    """Transportation requirement number."""

    uln: Optional[str] = None
    """Unit line number."""


class AirTransportMissionAbridged(BaseModel):
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

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    abp: Optional[str] = None
    """
    The Air Battle Plan used to coordinate and integrate air assets for this
    mission.
    """

    alias: Optional[str] = None
    """Mission alias."""

    allocated_unit: Optional[str] = FieldInfo(alias="allocatedUnit", default=None)
    """The unit the mission is allocated to."""

    amc_mission_id: Optional[str] = FieldInfo(alias="amcMissionId", default=None)
    """
    Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
    (MAF) Encode/Decode procedures.
    """

    apacs_id: Optional[str] = FieldInfo(alias="apacsId", default=None)
    """
    The Aircraft and Personnel Automated Clearance System (APACS) system identifier
    used to process and approve clearance requests.
    """

    ato_call_sign: Optional[str] = FieldInfo(alias="atoCallSign", default=None)
    """
    The call sign assigned to this mission according to the Air Tasking Order (ATO).
    """

    ato_mission_id: Optional[str] = FieldInfo(alias="atoMissionId", default=None)
    """The mission number according to the Air Tasking Order (ATO)."""

    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign for this mission."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    cw: Optional[bool] = None
    """Flag indicating this is a close watch mission."""

    dip_worksheet_name: Optional[str] = FieldInfo(alias="dipWorksheetName", default=None)
    """
    Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
    clearance requests.
    """

    first_pick_up: Optional[str] = FieldInfo(alias="firstPickUp", default=None)
    """
    The International Civil Aviation Organization (ICAO) site code of first cargo
    pick up.
    """

    gdss_mission_id: Optional[str] = FieldInfo(alias="gdssMissionId", default=None)
    """Global Decision Support System (GDSS) mission unique identifier."""

    haz_mat: Optional[List[HazMat]] = FieldInfo(alias="hazMat", default=None)
    """
    Collection of Hazardous Material information planned to be associated with this
    Air Transport Mission.
    """

    jcs_priority: Optional[str] = FieldInfo(alias="jcsPriority", default=None)
    """Highest Joint Chiefs of Staff priority of this mission."""

    last_drop_off: Optional[str] = FieldInfo(alias="lastDropOff", default=None)
    """
    The International Civil Aviation Organization (ICAO) site code of last cargo
    drop off.
    """

    load_category_type: Optional[str] = FieldInfo(alias="loadCategoryType", default=None)
    """Load type of this mission (e.g. CARGO, MIXED, PASSENGER)."""

    m1: Optional[str] = None
    """
    Mode-1 interrogation response (mission code), indicating mission or aircraft
    type.
    """

    m2: Optional[str] = None
    """Mode-2 interrogation response (military identification code)."""

    m3a: Optional[str] = None
    """
    Mode-3/A interrogation response (aircraft identification), provides a 4-digit
    octal identification code for the aircraft, assigned by the air traffic
    controller. Mode-3/A is shared military/civilian use.
    """

    naf: Optional[str] = None
    """Numbered Air Force (NAF) organization that owns the mission."""

    next_amc_mission_id: Optional[str] = FieldInfo(alias="nextAMCMissionId", default=None)
    """Air Mobility Command (AMC) mission identifier of the next air transport mission.

    Provides a method for AMC to link air transport missions together
    chronologically for tasking and planning purposes.
    """

    next_mission_id: Optional[str] = FieldInfo(alias="nextMissionId", default=None)
    """Unique identifier of the next mission provided by the originating source.

    Provides a method for the data provider to link air transport missions together
    chronologically for tasking and planning purposes.
    """

    node: Optional[str] = None
    """
    Designates the location responsible for mission transportation, logistics, or
    distribution activities for an Area of Responsibility (AOR) within USTRANSCOM.
    """

    objective: Optional[str] = None
    """A description of this mission's objective."""

    operation: Optional[str] = None
    """The name of the operation that this mission supports."""

    origin: Optional[str] = None
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_mission_id: Optional[str] = FieldInfo(alias="origMissionId", default=None)
    """The mission identifier provided by the originating source."""

    orig_network: Optional[str] = FieldInfo(alias="origNetwork", default=None)
    """
    The originating source network on which this record was created, auto-populated
    by the system.
    """

    prev_amc_mission_id: Optional[str] = FieldInfo(alias="prevAMCMissionId", default=None)
    """
    Air Mobility Command (AMC) mission identifier of the previous air transport
    mission. Provides a method for AMC to link air transport missions together
    chronologically for tasking and planning purposes.
    """

    prev_mission_id: Optional[str] = FieldInfo(alias="prevMissionId", default=None)
    """
    Unique identifier of the previous air transport mission provided by the
    originating source. Provides a method for the data provider to link air
    transport missions together chronologically for tasking and planning purposes.
    """

    purpose: Optional[str] = None
    """A description of this mission's purpose (e.g.

    why this mission needs to happen, what is the mission supporting, etc.).
    """

    remarks: Optional[List[Remark]] = None
    """
    Information related to the planning, load, status, and deployment or dispatch of
    one aircraft to carry out a mission.
    """

    requirements: Optional[List[Requirement]] = None
    """
    Collection of Requirements planned to be associated with this Air Transport
    Mission.
    """

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    source_sys_deviation: Optional[float] = FieldInfo(alias="sourceSysDeviation", default=None)
    """
    The number of minutes a mission is off schedule based on the source system's
    business rules. Positive numbers are early, negative numbers are late.
    """

    state: Optional[str] = None
    """Current state of the mission."""

    type: Optional[str] = None
    """The type of mission (e.g. SAAM, CHNL, etc.)."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
