# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LogisticsSupportUnvalidatedPublishParams",
    "Body",
    "BodyLogisticsDiscrepancyInfo",
    "BodyLogisticsRemark",
    "BodyLogisticsSupportItem",
    "BodyLogisticsSupportItemLogisticsPart",
    "BodyLogisticsSupportItemLogisticsPartLogisticsStock",
    "BodyLogisticsSupportItemLogisticsRemark",
    "BodyLogisticsSupportItemLogisticsSpecialty",
    "BodyLogisticsTransportationPlan",
    "BodyLogisticsTransportationPlanLogisticsSegment",
    "BodyLogisticsTransportationPlanLogisticsTransportationPlansRemark",
]


class LogisticsSupportUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyLogisticsDiscrepancyInfo(TypedDict, total=False):
    closure_time: Annotated[Union[str, datetime], PropertyInfo(alias="closureTime", format="iso8601")]
    """
    The discrepancy closure time, in ISO 8601 UTC format with millisecond precision.
    """

    discrepancy_info: Annotated[str, PropertyInfo(alias="discrepancyInfo")]
    """The aircraft discrepancy description."""

    jcn: str
    """Job Control Number of the discrepancy."""

    job_st_time: Annotated[Union[str, datetime], PropertyInfo(alias="jobStTime", format="iso8601")]
    """The job start time, in ISO 8601 UTC format with millisecond precision."""


class BodyLogisticsRemark(TypedDict, total=False):
    last_changed: Annotated[Union[str, datetime], PropertyInfo(alias="lastChanged", format="iso8601")]
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: str
    """Text of the remark."""

    username: str
    """User who published the remark."""


class BodyLogisticsSupportItemLogisticsPartLogisticsStock(TypedDict, total=False):
    quantity: int
    """The quantity of available parts needed from sourceICAO."""

    source_icao: Annotated[str, PropertyInfo(alias="sourceICAO")]
    """The ICAO code for the primary location with available parts."""

    stock_check_time: Annotated[Union[str, datetime], PropertyInfo(alias="stockCheckTime", format="iso8601")]
    """
    The datetime when the parts were sourced, in ISO 8601 UTC format with
    millisecond precision.
    """

    stock_poc: Annotated[str, PropertyInfo(alias="stockPOC")]
    """The point of contact at the sourced location."""


class BodyLogisticsSupportItemLogisticsPart(TypedDict, total=False):
    figure_number: Annotated[str, PropertyInfo(alias="figureNumber")]
    """Technical order manual figure number for the requested / supplied part."""

    index_number: Annotated[str, PropertyInfo(alias="indexNumber")]
    """Technical order manual index number for the requested part."""

    location_verifier: Annotated[str, PropertyInfo(alias="locationVerifier")]
    """
    The person who validated that the sourced location has, and can supply, the
    requested parts.
    """

    logistics_stocks: Annotated[
        Iterable[BodyLogisticsSupportItemLogisticsPartLogisticsStock], PropertyInfo(alias="logisticsStocks")
    ]
    """The supply stocks for this support item."""

    measurement_unit_code: Annotated[str, PropertyInfo(alias="measurementUnitCode")]
    """Code for a unit of measurement."""

    national_stock_number: Annotated[str, PropertyInfo(alias="nationalStockNumber")]
    """The National Stock Number of the part being requested or supplied."""

    part_number: Annotated[str, PropertyInfo(alias="partNumber")]
    """Requested or supplied part number."""

    request_verifier: Annotated[str, PropertyInfo(alias="requestVerifier")]
    """The person who validated the request for parts."""

    supply_document_number: Annotated[str, PropertyInfo(alias="supplyDocumentNumber")]
    """The supply document number."""

    technical_order_text: Annotated[str, PropertyInfo(alias="technicalOrderText")]
    """
    Indicates the specified Technical Order manual holding the aircraft information
    for use in diagnosing a problem or condition.
    """

    work_unit_code: Annotated[str, PropertyInfo(alias="workUnitCode")]
    """Work Unit Code (WUC), or for some aircraft types, the Reference Designator."""


class BodyLogisticsSupportItemLogisticsRemark(TypedDict, total=False):
    last_changed: Annotated[Union[str, datetime], PropertyInfo(alias="lastChanged", format="iso8601")]
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: str
    """Text of the remark."""

    username: str
    """User who published the remark."""


class BodyLogisticsSupportItemLogisticsSpecialty(TypedDict, total=False):
    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The first name of the specialist."""

    last4_ssn: Annotated[str, PropertyInfo(alias="last4Ssn")]
    """The last four digits of the specialist's social security number."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The last name of the specialist."""

    rank_code: Annotated[str, PropertyInfo(alias="rankCode")]
    """Military service rank designation."""

    role_type_code: Annotated[str, PropertyInfo(alias="roleTypeCode")]
    """Type code that determines role of the mission response team member.

    TC - Team Chief, TM - Team Member.
    """

    skill_level: Annotated[int, PropertyInfo(alias="skillLevel")]
    """Skill level of the mission response team member."""

    specialty: str
    """
    Indicates where the repairs will be performed, or which shop specialty has been
    assigned responsibility for correcting the discrepancy. Shop specialties are
    normally listed in abbreviated format.
    """


class BodyLogisticsSupportItem(TypedDict, total=False):
    cannibalized: bool
    """
    This element indicates whether or not the supplied item is contained within
    another item.
    """

    deploy_plan_number: Annotated[str, PropertyInfo(alias="deployPlanNumber")]
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    description: str
    """The technical order name of the part ordered."""

    item_last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="itemLastChangedDate", format="iso8601")]
    """
    The last time this supported item was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    job_control_number: Annotated[str, PropertyInfo(alias="jobControlNumber")]
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

    logistics_parts: Annotated[Iterable[BodyLogisticsSupportItemLogisticsPart], PropertyInfo(alias="logisticsParts")]
    """The parts associated with this support item."""

    logistics_remarks: Annotated[
        Iterable[BodyLogisticsSupportItemLogisticsRemark], PropertyInfo(alias="logisticsRemarks")
    ]
    """Remarks associated with this support item."""

    logistics_specialties: Annotated[
        Iterable[BodyLogisticsSupportItemLogisticsSpecialty], PropertyInfo(alias="logisticsSpecialties")
    ]
    """The specialties required to implement this support item."""

    quantity: int
    """Military aircraft discrepancy logistics requisition ordered quantity.

    The quantity of equipment ordered that is required to fix the aircraft.
    """

    ready_time: Annotated[Union[str, datetime], PropertyInfo(alias="readyTime", format="iso8601")]
    """The time the item is ready, in ISO 8601 UTC format with millisecond precision."""

    received_time: Annotated[Union[str, datetime], PropertyInfo(alias="receivedTime", format="iso8601")]
    """
    The time the item is received, in ISO 8601 UTC format with millisecond
    precision.
    """

    recovery_request_type_code: Annotated[str, PropertyInfo(alias="recoveryRequestTypeCode")]
    """The type of recovery request needed. Contact the source provider for details."""

    redeploy_plan_number: Annotated[str, PropertyInfo(alias="redeployPlanNumber")]
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    redeploy_shipment_unit_id: Annotated[str, PropertyInfo(alias="redeployShipmentUnitId")]
    """
    This is the Redeploy (return) Transportation Control Number/Tracking Reference
    Number for the selected item.
    """

    request_number: Annotated[str, PropertyInfo(alias="requestNumber")]
    """The request or record number for this item type (Equipent, Part, or MRT)."""

    resupport_flag: Annotated[bool, PropertyInfo(alias="resupportFlag")]
    """
    This element indicates if the supplied item is characterized as additional
    support.
    """

    shipment_unit_id: Annotated[str, PropertyInfo(alias="shipmentUnitId")]
    """
    Shipment Unit Identifier is the Transportation Control Number (TCN) for shipping
    that piece of equipment being requested.
    """

    si_poc: Annotated[str, PropertyInfo(alias="siPOC")]
    """
    The point of contact is a free text field to add information about the
    individual(s) with knowledge of the referenced requested or supplied item(s).
    The default value for this field is the last name, first name, and middle
    initial of the operator who created the records and/or generated the
    transaction.
    """

    source_icao: Annotated[str, PropertyInfo(alias="sourceICAO")]
    """
    The code that represents the International Civil Aviation Organization (ICAO)
    designations of an airport.
    """


class BodyLogisticsTransportationPlanLogisticsSegment(TypedDict, total=False):
    arrival_icao: Annotated[str, PropertyInfo(alias="arrivalICAO")]
    """Airport ICAO arrival code."""

    departure_icao: Annotated[str, PropertyInfo(alias="departureICAO")]
    """Airport ICAO departure code."""

    ext_mission_id: Annotated[str, PropertyInfo(alias="extMissionId")]
    """The GDSS mission ID for this segment."""

    id_mission: Annotated[str, PropertyInfo(alias="idMission")]
    """
    The unique identifier of the mission to which this logistics record is assigned.
    """

    itin: int
    """Start air mission itinerary point identifier."""

    mission_number: Annotated[str, PropertyInfo(alias="missionNumber")]
    """The user generated identifier for an air mission subgroup."""

    mission_type: Annotated[str, PropertyInfo(alias="missionType")]
    """The type of mission (e.g. SAAM, CHNL, etc.)."""

    mode_code: Annotated[str, PropertyInfo(alias="modeCode")]
    """Transportation mode.

    AMC airlift, Commercial airlift, Other, or surface transportation.
    """

    seg_act_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="segActArrTime", format="iso8601")]
    """
    Actual arrival time to segment destination, in ISO 8601 UTC format with
    millisecond precision.
    """

    seg_act_dep_time: Annotated[Union[str, datetime], PropertyInfo(alias="segActDepTime", format="iso8601")]
    """
    Actual departure time to the segment destination, in ISO 8601 UTC format with
    millisecond precision.
    """

    seg_aircraft_mds: Annotated[str, PropertyInfo(alias="segAircraftMDS")]
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    seg_est_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="segEstArrTime", format="iso8601")]
    """GC.

    LGTPS_C_DT_EST_ARR. GD2: Estimated arrival time to the segment destination. Only
    supplied when the segment is not attached to a Mission, otherwise the ETA is
    derived from the Mission segment destination point. This datetime should be in
    ISO 8601 UTC format with millisecond precision.
    """

    seg_est_dep_time: Annotated[Union[str, datetime], PropertyInfo(alias="segEstDepTime", format="iso8601")]
    """GC.

    LGTPS_C_DT_EST_DEP. GD2: Estimated departure time from the segment origin. Only
    supplied when the segment is not attached to a Mission, otherwise the ETD is
    derived from the Mission segment origin point. This datetime should be in ISO
    8601 UTC format with millisecond precision.
    """

    segment_number: Annotated[int, PropertyInfo(alias="segmentNumber")]
    """Used to sequence the segments in the transportation plan."""

    seg_tail_number: Annotated[str, PropertyInfo(alias="segTailNumber")]
    """The identifier that represents a specific aircraft within an aircraft type."""


class BodyLogisticsTransportationPlanLogisticsTransportationPlansRemark(TypedDict, total=False):
    last_changed: Annotated[Union[str, datetime], PropertyInfo(alias="lastChanged", format="iso8601")]
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: str
    """Text of the remark."""

    username: str
    """User who published the remark."""


class BodyLogisticsTransportationPlan(TypedDict, total=False):
    act_dep_time: Annotated[Union[str, datetime], PropertyInfo(alias="actDepTime", format="iso8601")]
    """
    Actual time of departure of first segment, in ISO 8601 UTC format with
    millisecond precision.
    """

    aircraft_status: Annotated[str, PropertyInfo(alias="aircraftStatus")]
    """
    These are the initial maintenance values entered based on the pilot descriptions
    or the official maintenance evaluation code.
    """

    approx_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="approxArrTime", format="iso8601")]
    """
    Approximate time of arrival of final segement, in ISO 8601 UTC format with
    millisecond precision.
    """

    cancelled_date: Annotated[Union[str, datetime], PropertyInfo(alias="cancelledDate", format="iso8601")]
    """GC.

    LGTP_CANX_DT. GD2: Date when the transportation plan was cancelled, in ISO 8601
    UTC format with millisecond precision.
    """

    closed_date: Annotated[Union[str, datetime], PropertyInfo(alias="closedDate", format="iso8601")]
    """GC.

    LGTP_CLSD_DT. GD2: Date when the transportation plan was closed, in ISO 8601 UTC
    format with millisecond precision.
    """

    coordinator: str
    """The AMS username of the operator who alters the coordination status.

    Automatically captured by the system.
    """

    coordinator_unit: Annotated[str, PropertyInfo(alias="coordinatorUnit")]
    """The AMS user unit_id of the operator who alters the coordination status.

    Automatically captured by the system from table AMS_USER.
    """

    destination_icao: Annotated[str, PropertyInfo(alias="destinationICAO")]
    """Destination location ICAO."""

    duration: str
    """Transportation plan duration, expressed in the format MMM:SS."""

    est_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="estArrTime", format="iso8601")]
    """ETA of the final segment, in ISO 8601 UTC format with millisecond precision."""

    est_dep_time: Annotated[Union[str, datetime], PropertyInfo(alias="estDepTime", format="iso8601")]
    """ETD of the first segment, in ISO 8601 UTC format with millisecond precision."""

    last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="lastChangedDate", format="iso8601")]
    """
    Last time transportation plan was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    logistic_master_record_id: Annotated[str, PropertyInfo(alias="logisticMasterRecordId")]
    """The identifier that represents a Logistics Master Record."""

    logistics_segments: Annotated[
        Iterable[BodyLogisticsTransportationPlanLogisticsSegment], PropertyInfo(alias="logisticsSegments")
    ]
    """The transportation segments associated with this transportation plan."""

    logistics_transportation_plans_remarks: Annotated[
        Iterable[BodyLogisticsTransportationPlanLogisticsTransportationPlansRemark],
        PropertyInfo(alias="logisticsTransportationPlansRemarks"),
    ]
    """Remarks associated with this transportation plan."""

    majcom: str
    """The major command for the current unit."""

    mission_change: Annotated[bool, PropertyInfo(alias="missionChange")]
    """
    Indicates whether there have been changes to changes to ICAOs, estArrTime, or
    estDepTime since this Transportation Plan was last edited.
    """

    num_enroute_stops: Annotated[int, PropertyInfo(alias="numEnrouteStops")]
    """Transportation plan enroute stops."""

    num_trans_loads: Annotated[int, PropertyInfo(alias="numTransLoads")]
    """The number of transloads for this Transportation Plan."""

    origin_icao: Annotated[str, PropertyInfo(alias="originICAO")]
    """The origin location."""

    plan_definition: Annotated[str, PropertyInfo(alias="planDefinition")]
    """Defines the transporation plan as either a deployment or redeployment."""

    plans_number: Annotated[str, PropertyInfo(alias="plansNumber")]
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """
    GDSS2 uses an 8 character serial number to uniquely identify the aircraft and
    MDS combination. This is a portion of the full manufacturer serial number.
    """

    status_code: Annotated[str, PropertyInfo(alias="statusCode")]
    """Transporation Coordination status code.

    Cancel, Send to APCC, working, agree, disapprove or blank.
    """

    tp_aircraft_mds: Annotated[str, PropertyInfo(alias="tpAircraftMDS")]
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    tp_tail_number: Annotated[str, PropertyInfo(alias="tpTailNumber")]
    """Contains the tail number displayed by GDSS2."""


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

    rpt_created_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="rptCreatedTime", format="iso8601")]]
    """
    The time this report was created, in ISO 8601 UTC format with millisecond
    precision.
    """

    source: Required[str]
    """Source of the data."""

    id: str
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    aircraft_mds: Annotated[str, PropertyInfo(alias="aircraftMDS")]
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    curr_icao: Annotated[str, PropertyInfo(alias="currICAO")]
    """
    The current ICAO of the aircraft that is the subject of this
    LogisticsSupportDetails record.
    """

    etic: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The estimated time mission capable for the aircraft, in ISO 8601 UCT format with
    millisecond precision. This is the estimated time when the aircraft is mission
    ready.
    """

    etmc: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Logistics estimated time mission capable."""

    ext_system_id: Annotated[str, PropertyInfo(alias="extSystemId")]
    """Optional system identifier from external systs.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    logistic_action: Annotated[str, PropertyInfo(alias="logisticAction")]
    """
    This field identifies the pacing event for bringing the aircraft to Mission
    Capable status. It is used in calculating the Estimated Time Mission Capable
    (ETMC) value. Acceptable values are WA (Will Advise), INW (In Work), P+hhh.h
    (where P=parts and hhh.h is the number of hours up to 999 plus tenths of hours),
    EQ+hhh.h (EQ=equipment), MRT+hhh.h (MRT=maintenance recovery team).
    """

    logistics_discrepancy_infos: Annotated[
        Iterable[BodyLogisticsDiscrepancyInfo], PropertyInfo(alias="logisticsDiscrepancyInfos")
    ]
    """Discrepancy information associated with this LogisticsSupport record."""

    logistics_record_id: Annotated[str, PropertyInfo(alias="logisticsRecordId")]
    """The identifier that represents a Logistics Master Record."""

    logistics_remarks: Annotated[Iterable[BodyLogisticsRemark], PropertyInfo(alias="logisticsRemarks")]
    """Remarks associated with this LogisticsSupport record."""

    logistics_support_items: Annotated[Iterable[BodyLogisticsSupportItem], PropertyInfo(alias="logisticsSupportItems")]
    """Support items associated with this LogisticsSupport record."""

    logistics_transportation_plans: Annotated[
        Iterable[BodyLogisticsTransportationPlan], PropertyInfo(alias="logisticsTransportationPlans")
    ]
    """
    Transportation plans associated with this LogisticsSupport record, used to
    coordinate maintenance efforts.
    """

    maint_status_code: Annotated[str, PropertyInfo(alias="maintStatusCode")]
    """
    The maintenance status code of the aircraft which may be based on pilot
    descriptions or evaluation codes. Contact the source provider for details.
    """

    mc_time: Annotated[Union[str, datetime], PropertyInfo(alias="mcTime", format="iso8601")]
    """
    The time indicating when all mission essential problems with a given aircraft
    have been fixed and is mission capable. This datetime should be in ISO 8601 UTC
    format with millisecond precision.
    """

    me_time: Annotated[Union[str, datetime], PropertyInfo(alias="meTime", format="iso8601")]
    """The time indicating when a given aircraft breaks for a mission essential reason.

    This datetime should be in ISO 8601 UTC format with millisecond precision.
    """

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    owner: str
    """The organization that owns this logistics record."""

    reopen_flag: Annotated[bool, PropertyInfo(alias="reopenFlag")]
    """This is used to indicate whether a closed master record has been reopened."""

    rpt_closed_time: Annotated[Union[str, datetime], PropertyInfo(alias="rptClosedTime", format="iso8601")]
    """
    The time this report was closed, in ISO 8601 UTC format with millisecond
    precision.
    """

    supp_icao: Annotated[str, PropertyInfo(alias="suppICAO")]
    """
    The supplying ICAO of the aircraft that is the subject of this
    LogisticsSupportDetails record.
    """

    tail_number: Annotated[str, PropertyInfo(alias="tailNumber")]
    """
    The tail number of the aircraft that is the subject of this
    LogisticsSupportDetails record.
    """
