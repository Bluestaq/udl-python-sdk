# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "LogisticsSupportListResponse",
    "LogisticsDiscrepancyInfo",
    "LogisticsRemark",
    "LogisticsSupportItem",
    "LogisticsSupportItemLogisticsPart",
    "LogisticsSupportItemLogisticsPartLogisticsStock",
    "LogisticsSupportItemLogisticsRemark",
    "LogisticsSupportItemLogisticsSpecialty",
    "LogisticsTransportationPlan",
    "LogisticsTransportationPlanLogisticsSegment",
    "LogisticsTransportationPlanLogisticsTransportationPlansRemark",
]


class LogisticsDiscrepancyInfo(BaseModel):
    closure_time: Optional[datetime] = FieldInfo(alias="closureTime", default=None)
    """
    The discrepancy closure time, in ISO 8601 UTC format with millisecond precision.
    """

    discrepancy_info: Optional[str] = FieldInfo(alias="discrepancyInfo", default=None)
    """The aircraft discrepancy description."""

    jcn: Optional[str] = None
    """Job Control Number of the discrepancy."""

    job_st_time: Optional[datetime] = FieldInfo(alias="jobStTime", default=None)
    """The job start time, in ISO 8601 UTC format with millisecond precision."""


class LogisticsRemark(BaseModel):
    last_changed: Optional[datetime] = FieldInfo(alias="lastChanged", default=None)
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: Optional[str] = None
    """Text of the remark."""

    username: Optional[str] = None
    """User who published the remark."""


class LogisticsSupportItemLogisticsPartLogisticsStock(BaseModel):
    quantity: Optional[int] = None
    """The quantity of available parts needed from sourceICAO."""

    source_icao: Optional[str] = FieldInfo(alias="sourceICAO", default=None)
    """The ICAO code for the primary location with available parts."""

    stock_check_time: Optional[datetime] = FieldInfo(alias="stockCheckTime", default=None)
    """
    The datetime when the parts were sourced, in ISO 8601 UTC format with
    millisecond precision.
    """

    stock_poc: Optional[str] = FieldInfo(alias="stockPOC", default=None)
    """The point of contact at the sourced location."""


class LogisticsSupportItemLogisticsPart(BaseModel):
    figure_number: Optional[str] = FieldInfo(alias="figureNumber", default=None)
    """Technical order manual figure number for the requested / supplied part."""

    index_number: Optional[str] = FieldInfo(alias="indexNumber", default=None)
    """Technical order manual index number for the requested part."""

    location_verifier: Optional[str] = FieldInfo(alias="locationVerifier", default=None)
    """
    The person who validated that the sourced location has, and can supply, the
    requested parts.
    """

    logistics_stocks: Optional[List[LogisticsSupportItemLogisticsPartLogisticsStock]] = FieldInfo(
        alias="logisticsStocks", default=None
    )
    """The supply stocks for this support item."""

    measurement_unit_code: Optional[str] = FieldInfo(alias="measurementUnitCode", default=None)
    """Code for a unit of measurement."""

    national_stock_number: Optional[str] = FieldInfo(alias="nationalStockNumber", default=None)
    """The National Stock Number of the part being requested or supplied."""

    part_number: Optional[str] = FieldInfo(alias="partNumber", default=None)
    """Requested or supplied part number."""

    request_verifier: Optional[str] = FieldInfo(alias="requestVerifier", default=None)
    """The person who validated the request for parts."""

    supply_document_number: Optional[str] = FieldInfo(alias="supplyDocumentNumber", default=None)
    """The supply document number."""

    technical_order_text: Optional[str] = FieldInfo(alias="technicalOrderText", default=None)
    """
    Indicates the specified Technical Order manual holding the aircraft information
    for use in diagnosing a problem or condition.
    """

    work_unit_code: Optional[str] = FieldInfo(alias="workUnitCode", default=None)
    """Work Unit Code (WUC), or for some aircraft types, the Reference Designator."""


class LogisticsSupportItemLogisticsRemark(BaseModel):
    last_changed: Optional[datetime] = FieldInfo(alias="lastChanged", default=None)
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: Optional[str] = None
    """Text of the remark."""

    username: Optional[str] = None
    """User who published the remark."""


class LogisticsSupportItemLogisticsSpecialty(BaseModel):
    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the specialist."""

    last4_ssn: Optional[str] = FieldInfo(alias="last4Ssn", default=None)
    """The last four digits of the specialist's social security number."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the specialist."""

    rank_code: Optional[str] = FieldInfo(alias="rankCode", default=None)
    """Military service rank designation."""

    role_type_code: Optional[str] = FieldInfo(alias="roleTypeCode", default=None)
    """Type code that determines role of the mission response team member.

    TC - Team Chief, TM - Team Member.
    """

    skill_level: Optional[int] = FieldInfo(alias="skillLevel", default=None)
    """Skill level of the mission response team member."""

    specialty: Optional[str] = None
    """
    Indicates where the repairs will be performed, or which shop specialty has been
    assigned responsibility for correcting the discrepancy. Shop specialties are
    normally listed in abbreviated format.
    """


class LogisticsSupportItem(BaseModel):
    cannibalized: Optional[bool] = None
    """
    This element indicates whether or not the supplied item is contained within
    another item.
    """

    deploy_plan_number: Optional[str] = FieldInfo(alias="deployPlanNumber", default=None)
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    description: Optional[str] = None
    """The technical order name of the part ordered."""

    item_last_changed_date: Optional[datetime] = FieldInfo(alias="itemLastChangedDate", default=None)
    """
    The last time this supported item was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    job_control_number: Optional[str] = FieldInfo(alias="jobControlNumber", default=None)
    """
    A number assigned by Job Control to monitor and record maintenance actions
    required to correct the associated aircraft maintenance discrepancy. It is
    seven, nine or twelve characters, depending on the base-specific numbering
    scheme. If seven characters: characters 1-3 are Julian date, 4-7 are sequence
    numbers. If nine characters: characters 1-2 are last two digits of the year,
    characters 3-5 are Julian date, 6-9 are sequence numbers. If twelve characters:
    characters 1-2 are last two digits of the year, 3-5 are Julian date, 6-9 are
    sequence numbers, and 10-12 are a three-digit supplemental number.
    """

    logistics_parts: Optional[List[LogisticsSupportItemLogisticsPart]] = FieldInfo(alias="logisticsParts", default=None)
    """The parts associated with this support item."""

    logistics_remarks: Optional[List[LogisticsSupportItemLogisticsRemark]] = FieldInfo(
        alias="logisticsRemarks", default=None
    )
    """Remarks associated with this support item."""

    logistics_specialties: Optional[List[LogisticsSupportItemLogisticsSpecialty]] = FieldInfo(
        alias="logisticsSpecialties", default=None
    )
    """The specialties required to implement this support item."""

    quantity: Optional[int] = None
    """Military aircraft discrepancy logistics requisition ordered quantity.

    The quantity of equipment ordered that is required to fix the aircraft.
    """

    ready_time: Optional[datetime] = FieldInfo(alias="readyTime", default=None)
    """The time the item is ready, in ISO 8601 UTC format with millisecond precision."""

    received_time: Optional[datetime] = FieldInfo(alias="receivedTime", default=None)
    """
    The time the item is received, in ISO 8601 UTC format with millisecond
    precision.
    """

    recovery_request_type_code: Optional[str] = FieldInfo(alias="recoveryRequestTypeCode", default=None)
    """The type of recovery request needed. Contact the source provider for details."""

    redeploy_plan_number: Optional[str] = FieldInfo(alias="redeployPlanNumber", default=None)
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    redeploy_shipment_unit_id: Optional[str] = FieldInfo(alias="redeployShipmentUnitId", default=None)
    """
    This is the Redeploy (return) Transportation Control Number/Tracking Reference
    Number for the selected item.
    """

    request_number: Optional[str] = FieldInfo(alias="requestNumber", default=None)
    """The request or record number for this item type (Equipent, Part, or MRT)."""

    resupport_flag: Optional[bool] = FieldInfo(alias="resupportFlag", default=None)
    """
    This element indicates if the supplied item is characterized as additional
    support.
    """

    shipment_unit_id: Optional[str] = FieldInfo(alias="shipmentUnitId", default=None)
    """
    Shipment Unit Identifier is the Transportation Control Number (TCN) for shipping
    that piece of equipment being requested.
    """

    si_poc: Optional[str] = FieldInfo(alias="siPOC", default=None)
    """
    The point of contact is a free text field to add information about the
    individual(s) with knowledge of the referenced requested or supplied item(s).
    The default value for this field is the last name, first name, and middle
    initial of the operator who created the records and/or generated the
    transaction.
    """

    source_icao: Optional[str] = FieldInfo(alias="sourceICAO", default=None)
    """
    The code that represents the International Civil Aviation Organization (ICAO)
    designations of an airport.
    """


class LogisticsTransportationPlanLogisticsSegment(BaseModel):
    arrival_icao: Optional[str] = FieldInfo(alias="arrivalICAO", default=None)
    """Airport ICAO arrival code."""

    departure_icao: Optional[str] = FieldInfo(alias="departureICAO", default=None)
    """Airport ICAO departure code."""

    ext_mission_id: Optional[str] = FieldInfo(alias="extMissionId", default=None)
    """The GDSS mission ID for this segment."""

    id_mission: Optional[str] = FieldInfo(alias="idMission", default=None)
    """
    The unique identifier of the mission to which this logistics record is assigned.
    """

    itin: Optional[int] = None
    """Start air mission itinerary point identifier."""

    mission_number: Optional[str] = FieldInfo(alias="missionNumber", default=None)
    """The user generated identifier for an air mission subgroup."""

    mission_type: Optional[str] = FieldInfo(alias="missionType", default=None)
    """The type of mission (e.g. SAAM, CHNL, etc.)."""

    mode_code: Optional[str] = FieldInfo(alias="modeCode", default=None)
    """Transportation mode.

    AMC airlift, Commercial airlift, Other, or surface transportation.
    """

    seg_act_arr_time: Optional[datetime] = FieldInfo(alias="segActArrTime", default=None)
    """
    Actual arrival time to segment destination, in ISO 8601 UTC format with
    millisecond precision.
    """

    seg_act_dep_time: Optional[datetime] = FieldInfo(alias="segActDepTime", default=None)
    """
    Actual departure time to the segment destination, in ISO 8601 UTC format with
    millisecond precision.
    """

    seg_aircraft_mds: Optional[str] = FieldInfo(alias="segAircraftMDS", default=None)
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    seg_est_arr_time: Optional[datetime] = FieldInfo(alias="segEstArrTime", default=None)
    """GC.

    LGTPS_C_DT_EST_ARR. GD2: Estimated arrival time to the segment destination. Only
    supplied when the segment is not attached to a Mission, otherwise the ETA is
    derived from the Mission segment destination point. This datetime should be in
    ISO 8601 UTC format with millisecond precision.
    """

    seg_est_dep_time: Optional[datetime] = FieldInfo(alias="segEstDepTime", default=None)
    """GC.

    LGTPS_C_DT_EST_DEP. GD2: Estimated departure time from the segment origin. Only
    supplied when the segment is not attached to a Mission, otherwise the ETD is
    derived from the Mission segment origin point. This datetime should be in ISO
    8601 UTC format with millisecond precision.
    """

    segment_number: Optional[int] = FieldInfo(alias="segmentNumber", default=None)
    """Used to sequence the segments in the transportation plan."""

    seg_tail_number: Optional[str] = FieldInfo(alias="segTailNumber", default=None)
    """The identifier that represents a specific aircraft within an aircraft type."""


class LogisticsTransportationPlanLogisticsTransportationPlansRemark(BaseModel):
    last_changed: Optional[datetime] = FieldInfo(alias="lastChanged", default=None)
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: Optional[str] = None
    """Text of the remark."""

    username: Optional[str] = None
    """User who published the remark."""


class LogisticsTransportationPlan(BaseModel):
    act_dep_time: Optional[datetime] = FieldInfo(alias="actDepTime", default=None)
    """
    Actual time of departure of first segment, in ISO 8601 UTC format with
    millisecond precision.
    """

    aircraft_status: Optional[str] = FieldInfo(alias="aircraftStatus", default=None)
    """
    These are the initial maintenance values entered based on the pilot descriptions
    or the official maintenance evaluation code.
    """

    approx_arr_time: Optional[datetime] = FieldInfo(alias="approxArrTime", default=None)
    """
    Approximate time of arrival of final segement, in ISO 8601 UTC format with
    millisecond precision.
    """

    cancelled_date: Optional[datetime] = FieldInfo(alias="cancelledDate", default=None)
    """GC.

    LGTP_CANX_DT. GD2: Date when the transportation plan was cancelled, in ISO 8601
    UTC format with millisecond precision.
    """

    closed_date: Optional[datetime] = FieldInfo(alias="closedDate", default=None)
    """GC.

    LGTP_CLSD_DT. GD2: Date when the transportation plan was closed, in ISO 8601 UTC
    format with millisecond precision.
    """

    coordinator: Optional[str] = None
    """The AMS username of the operator who alters the coordination status.

    Automatically captured by the system.
    """

    coordinator_unit: Optional[str] = FieldInfo(alias="coordinatorUnit", default=None)
    """The AMS user unit_id of the operator who alters the coordination status.

    Automatically captured by the system from table AMS_USER.
    """

    destination_icao: Optional[str] = FieldInfo(alias="destinationICAO", default=None)
    """Destination location ICAO."""

    duration: Optional[str] = None
    """Transportation plan duration, expressed in the format MMM:SS."""

    est_arr_time: Optional[datetime] = FieldInfo(alias="estArrTime", default=None)
    """ETA of the final segment, in ISO 8601 UTC format with millisecond precision."""

    est_dep_time: Optional[datetime] = FieldInfo(alias="estDepTime", default=None)
    """ETD of the first segment, in ISO 8601 UTC format with millisecond precision."""

    last_changed_date: Optional[datetime] = FieldInfo(alias="lastChangedDate", default=None)
    """
    Last time transportation plan was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    logistic_master_record_id: Optional[str] = FieldInfo(alias="logisticMasterRecordId", default=None)
    """The identifier that represents a Logistics Master Record."""

    logistics_segments: Optional[List[LogisticsTransportationPlanLogisticsSegment]] = FieldInfo(
        alias="logisticsSegments", default=None
    )
    """The transportation segments associated with this transportation plan."""

    logistics_transportation_plans_remarks: Optional[
        List[LogisticsTransportationPlanLogisticsTransportationPlansRemark]
    ] = FieldInfo(alias="logisticsTransportationPlansRemarks", default=None)
    """Remarks associated with this transportation plan."""

    majcom: Optional[str] = None
    """The major command for the current unit."""

    mission_change: Optional[bool] = FieldInfo(alias="missionChange", default=None)
    """
    Indicates whether there have been changes to changes to ICAOs, estArrTime, or
    estDepTime since this Transportation Plan was last edited.
    """

    num_enroute_stops: Optional[int] = FieldInfo(alias="numEnrouteStops", default=None)
    """Transportation plan enroute stops."""

    num_trans_loads: Optional[int] = FieldInfo(alias="numTransLoads", default=None)
    """The number of transloads for this Transportation Plan."""

    origin_icao: Optional[str] = FieldInfo(alias="originICAO", default=None)
    """The origin location."""

    plan_definition: Optional[str] = FieldInfo(alias="planDefinition", default=None)
    """Defines the transporation plan as either a deployment or redeployment."""

    plans_number: Optional[str] = FieldInfo(alias="plansNumber", default=None)
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """
    GDSS2 uses an 8 character serial number to uniquely identify the aircraft and
    MDS combination. This is a portion of the full manufacturer serial number.
    """

    status_code: Optional[str] = FieldInfo(alias="statusCode", default=None)
    """Transporation Coordination status code.

    Cancel, Send to APCC, working, agree, disapprove or blank.
    """

    tp_aircraft_mds: Optional[str] = FieldInfo(alias="tpAircraftMDS", default=None)
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    tp_tail_number: Optional[str] = FieldInfo(alias="tpTailNumber", default=None)
    """Contains the tail number displayed by GDSS2."""


class LogisticsSupportListResponse(BaseModel):
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

    rpt_created_time: datetime = FieldInfo(alias="rptCreatedTime")
    """
    The time this report was created, in ISO 8601 UTC format with millisecond
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

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """Application user who created the row in the database."""

    curr_icao: Optional[str] = FieldInfo(alias="currICAO", default=None)
    """
    The current ICAO of the aircraft that is the subject of this
    LogisticsSupportDetails record.
    """

    etic: Optional[datetime] = None
    """
    The estimated time mission capable for the aircraft, in ISO 8601 UCT format with
    millisecond precision. This is the estimated time when the aircraft is mission
    ready.
    """

    etmc: Optional[datetime] = None
    """Logistics estimated time mission capable."""

    ext_system_id: Optional[str] = FieldInfo(alias="extSystemId", default=None)
    """Optional system identifier from external systs.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    logistic_action: Optional[str] = FieldInfo(alias="logisticAction", default=None)
    """
    This field identifies the pacing event for bringing the aircraft to Mission
    Capable status. It is used in calculating the Estimated Time Mission Capable
    (ETMC) value. Acceptable values are WA (Will Advise), INW (In Work), P+hhh.h
    (where P=parts and hhh.h is the number of hours up to 999 plus tenths of hours),
    EQ+hhh.h (EQ=equipment), MRT+hhh.h (MRT=maintenance recovery team).
    """

    logistics_discrepancy_infos: Optional[List[LogisticsDiscrepancyInfo]] = FieldInfo(
        alias="logisticsDiscrepancyInfos", default=None
    )
    """Discrepancy information associated with this LogisticsSupport record."""

    logistics_record_id: Optional[str] = FieldInfo(alias="logisticsRecordId", default=None)
    """The identifier that represents a Logistics Master Record."""

    logistics_remarks: Optional[List[LogisticsRemark]] = FieldInfo(alias="logisticsRemarks", default=None)
    """Remarks associated with this LogisticsSupport record."""

    logistics_support_items: Optional[List[LogisticsSupportItem]] = FieldInfo(
        alias="logisticsSupportItems", default=None
    )
    """Support items associated with this LogisticsSupport record."""

    logistics_transportation_plans: Optional[List[LogisticsTransportationPlan]] = FieldInfo(
        alias="logisticsTransportationPlans", default=None
    )
    """
    Transportation plans associated with this LogisticsSupport record, used to
    coordinate maintenance efforts.
    """

    maint_status_code: Optional[str] = FieldInfo(alias="maintStatusCode", default=None)
    """
    The maintenance status code of the aircraft which may be based on pilot
    descriptions or evaluation codes. Contact the source provider for details.
    """

    mc_time: Optional[datetime] = FieldInfo(alias="mcTime", default=None)
    """
    The time indicating when all mission essential problems with a given aircraft
    have been fixed and is mission capable. This datetime should be in ISO 8601 UTC
    format with millisecond precision.
    """

    me_time: Optional[datetime] = FieldInfo(alias="meTime", default=None)
    """The time indicating when a given aircraft breaks for a mission essential reason.

    This datetime should be in ISO 8601 UTC format with millisecond precision.
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

    owner: Optional[str] = None
    """The organization that owns this logistics record."""

    reopen_flag: Optional[bool] = FieldInfo(alias="reopenFlag", default=None)
    """This is used to indicate whether a closed master record has been reopened."""

    rpt_closed_time: Optional[datetime] = FieldInfo(alias="rptClosedTime", default=None)
    """
    The time this report was closed, in ISO 8601 UTC format with millisecond
    precision.
    """

    supp_icao: Optional[str] = FieldInfo(alias="suppICAO", default=None)
    """
    The supplying ICAO of the aircraft that is the subject of this
    LogisticsSupportDetails record.
    """

    tail_number: Optional[str] = FieldInfo(alias="tailNumber", default=None)
    """
    The tail number of the aircraft that is the subject of this
    LogisticsSupportDetails record.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
