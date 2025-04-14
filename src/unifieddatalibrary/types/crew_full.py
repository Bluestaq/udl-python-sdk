# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CrewFull", "CrewMember"]


class CrewMember(BaseModel):
    alerted: Optional[bool] = None
    """
    Flag indicating whether this crew member has been alerted of the associated
    task.
    """

    all_sortie: Optional[bool] = FieldInfo(alias="allSortie", default=None)
    """
    Flag indicating this crew member is assigned to all sorties of the crew
    itinerary.
    """

    approved: Optional[bool] = None
    """
    Flag indicating whether this crew member has been approved for the associated
    task.
    """

    attached: Optional[bool] = None
    """Flag indicating whether this crew member is attached to his/her squadron.

    Crew members that are not attached are considered assigned.
    """

    branch: Optional[str] = None
    """The military branch assignment of the crew member."""

    civilian: Optional[bool] = None
    """Flag indicating this crew member is a civilian or non-military person."""

    commander: Optional[bool] = None
    """Flag indicating this person is the aircraft commander."""

    crew_position: Optional[str] = FieldInfo(alias="crewPosition", default=None)
    """The crew position of the crew member."""

    dod_id: Optional[str] = FieldInfo(alias="dodID", default=None)
    """The crew member's 10-digit DoD ID number."""

    duty_position: Optional[str] = FieldInfo(alias="dutyPosition", default=None)
    """The duty position of the crew member."""

    duty_status: Optional[str] = FieldInfo(alias="dutyStatus", default=None)
    """
    The current duty status code of this crew member (e.g., AGR for Active Guard and
    Reserve, IDT for Inactive Duty Training, etc.).
    """

    emailed: Optional[bool] = None
    """
    Flag indicating whether this crew member has been notified of an event by email.
    """

    extra_time: Optional[bool] = FieldInfo(alias="extraTime", default=None)
    """
    Flag indicating whether this crew member requires an additional amount of time
    to report for duty.
    """

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the crew member."""

    flt_currency_exp: Optional[datetime] = FieldInfo(alias="fltCurrencyExp", default=None)
    """
    The earliest flying currency expiration date for this crew member, in ISO 8601
    UTC format with millisecond precision.
    """

    flt_currency_exp_id: Optional[str] = FieldInfo(alias="fltCurrencyExpId", default=None)
    """
    The training task identifier associated with the flying currency expiration date
    for this crew member.
    """

    flt_rec_date: Optional[datetime] = FieldInfo(alias="fltRecDate", default=None)
    """
    The date this crew member's records review was completed, in ISO 8601 UTC format
    with millisecond precision.
    """

    flt_rec_due: Optional[datetime] = FieldInfo(alias="fltRecDue", default=None)
    """
    The date this crew member's records review is due, in ISO 8601 UTC format with
    millisecond precision.
    """

    fly_squadron: Optional[str] = FieldInfo(alias="flySquadron", default=None)
    """The flying squadron assignment of the crew member."""

    funded: Optional[bool] = None
    """Flag indicating whether this crew member is funded."""

    gender: Optional[str] = None
    """Gender of the crew member."""

    gnd_currency_exp: Optional[datetime] = FieldInfo(alias="gndCurrencyExp", default=None)
    """
    The earliest ground currency expiration date for this crew member, in ISO 8601
    UTC format with millisecond precision.
    """

    gnd_currency_exp_id: Optional[str] = FieldInfo(alias="gndCurrencyExpId", default=None)
    """
    The training task identifier associated with the ground currency expiration date
    for this crew member.
    """

    grounded: Optional[bool] = None
    """
    Flag indicating whether this crew member is grounded (i.e., his/her duties do
    not include flying).
    """

    guest_start: Optional[datetime] = FieldInfo(alias="guestStart", default=None)
    """
    Date when this crew member starts acting as guest help for the squadron, in ISO
    8601 UTC format with millisecond precision.
    """

    guest_stop: Optional[datetime] = FieldInfo(alias="guestStop", default=None)
    """
    Date when this crew member stops acting as guest help for the squadron, in ISO
    8601 UTC format with millisecond precision.
    """

    last4_ssn: Optional[str] = FieldInfo(alias="last4SSN", default=None)
    """Last four digits of the crew member's social security number."""

    last_flt_date: Optional[datetime] = FieldInfo(alias="lastFltDate", default=None)
    """
    Date of the last flight for this crew member, in ISO 8601 UTC format with
    millisecond precision.
    """

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the crew member."""

    loaned_to: Optional[str] = FieldInfo(alias="loanedTo", default=None)
    """The squadron the crew member has been temporarily loaned to."""

    lodging: Optional[str] = None
    """Crew member lodging location."""

    member_actual_alert_time: Optional[datetime] = FieldInfo(alias="memberActualAlertTime", default=None)
    """
    Time this crew member was actually alerted for the mission, in ISO 8601 UTC
    format with millisecond precision.
    """

    member_adj_return_time: Optional[datetime] = FieldInfo(alias="memberAdjReturnTime", default=None)
    """
    Adjusted return time for the crew member, in ISO 8601 UTC format with
    millisecond precision.
    """

    member_adj_return_time_approver: Optional[str] = FieldInfo(alias="memberAdjReturnTimeApprover", default=None)
    """Last name of the crew member's adjusted return time approver."""

    member_id: Optional[str] = FieldInfo(alias="memberId", default=None)
    """Unique identifier of the crew member assigned by the originating source."""

    member_init_start_time: Optional[datetime] = FieldInfo(alias="memberInitStartTime", default=None)
    """
    Initial start time of the crew member's linked task that was delinked due to
    mission closure, in ISO 8601 UTC format with millisecond precision.
    """

    member_last_alert_time: Optional[datetime] = FieldInfo(alias="memberLastAlertTime", default=None)
    """
    The latest possible time the crew member can legally be alerted for a task, in
    ISO 8601 UTC format with millisecond precision.
    """

    member_legal_alert_time: Optional[datetime] = FieldInfo(alias="memberLegalAlertTime", default=None)
    """
    Time this crew member becomes eligible to be alerted for the mission, in ISO
    8601 UTC format with millisecond precision.
    """

    member_pickup_time: Optional[datetime] = FieldInfo(alias="memberPickupTime", default=None)
    """
    Time this crew member will be picked up from lodging, in ISO 8601 UTC format
    with millisecond precision.
    """

    member_post_rest_offset: Optional[str] = FieldInfo(alias="memberPostRestOffset", default=None)
    """
    The scheduled delay or adjustment in the start time of a crew member's rest
    period after a mission, expressed as +/-HH:MM.
    """

    member_post_rest_time: Optional[datetime] = FieldInfo(alias="memberPostRestTime", default=None)
    """
    End time of this crew member's rest period after the mission, in ISO 8601 UTC
    format with millisecond precision.
    """

    member_pre_rest_time: Optional[datetime] = FieldInfo(alias="memberPreRestTime", default=None)
    """
    Start time of this crew member's rest period before the mission, in ISO 8601 UTC
    format with millisecond precision.
    """

    member_remarks: Optional[str] = FieldInfo(alias="memberRemarks", default=None)
    """Remarks concerning the crew member."""

    member_return_time: Optional[datetime] = FieldInfo(alias="memberReturnTime", default=None)
    """
    Scheduled return time for this crew member, in ISO 8601 UTC format with
    millisecond precision.
    """

    member_sched_alert_time: Optional[datetime] = FieldInfo(alias="memberSchedAlertTime", default=None)
    """
    Time this crew member is scheduled to be alerted for the mission, in ISO 8601
    UTC format with millisecond precision.
    """

    member_source: Optional[str] = FieldInfo(alias="memberSource", default=None)
    """
    The military component for the crew member (e.g., ACTIVE, RESERVE, GUARD,
    UNKNOWN, etc.).
    """

    member_stage_name: Optional[str] = FieldInfo(alias="memberStageName", default=None)
    """Stage name for the crew member.

    A stage is a pool of crews supporting a given operation plan.
    """

    member_transport_req: Optional[bool] = FieldInfo(alias="memberTransportReq", default=None)
    """
    Flag indicating whether this crew member needs transportation to the departure
    location.
    """

    member_type: Optional[str] = FieldInfo(alias="memberType", default=None)
    """Amplifying details about the crew member type (e.g.

    RAVEN, FCC, COMCAM, AIRCREW, MEP, OTHER, etc.).
    """

    middle_initial: Optional[str] = FieldInfo(alias="middleInitial", default=None)
    """The middle initial of the crew member."""

    notified: Optional[bool] = None
    """Flag indicating whether this crew member has been notified of an event."""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """Crew member lodging phone number."""

    phys_av_code: Optional[str] = FieldInfo(alias="physAvCode", default=None)
    """
    Code indicating a crew member's current physical fitness status and whether they
    are medically cleared to fly (e.g., D for Duties Not Including Flying, E for
    Physical Overdue, etc.).
    """

    phys_av_status: Optional[str] = FieldInfo(alias="physAvStatus", default=None)
    """
    Code indicating a crew member's physical availabiility status (e.g.,
    DISQUALIFIED, OVERDUE, etc.).
    """

    phys_due: Optional[datetime] = FieldInfo(alias="physDue", default=None)
    """
    Due date for the crew member's physical, in ISO 8601 UTC format with millisecond
    precision.
    """

    rank: Optional[str] = None
    """The rank of the crew member."""

    remark_code: Optional[str] = FieldInfo(alias="remarkCode", default=None)
    """Remark code used to designate attributes of this crew member.

    For more information, contact the provider source.
    """

    rms_mds: Optional[str] = FieldInfo(alias="rmsMDS", default=None)
    """
    The primary aircraft type for the crew member according to the personnel
    resource management system indicated in the crewRMS field.
    """

    show_time: Optional[datetime] = FieldInfo(alias="showTime", default=None)
    """
    Time this crew member is required to report for duty before this flight/mission,
    in ISO 8601 UTC format with millisecond precision.
    """

    squadron: Optional[str] = None
    """The squadron the crew member serves."""

    training_date: Optional[datetime] = FieldInfo(alias="trainingDate", default=None)
    """
    The date this crew member accomplished physiological or altitude chamber
    training, in ISO 8601 UTC format with millisecond precision.
    """

    username: Optional[str] = None
    """The Mattermost username of this crew member."""

    wing: Optional[str] = None
    """The wing the crew member serves."""


class CrewFull(BaseModel):
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

    orig_crew_id: str = FieldInfo(alias="origCrewId")
    """Unique identifier of the formed crew provided by the originating source.

    Provided for systems that require tracking of an internal system generated ID.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    adj_return_time: Optional[datetime] = FieldInfo(alias="adjReturnTime", default=None)
    """Adjusted return time, in ISO 8601 UTC format with millisecond precision."""

    adj_return_time_approver: Optional[str] = FieldInfo(alias="adjReturnTimeApprover", default=None)
    """Last name of the adjusted return time approver."""

    aircraft_mds: Optional[str] = FieldInfo(alias="aircraftMDS", default=None)
    """The aircraft Model Design Series designation assigned for this crew."""

    alerted_time: Optional[datetime] = FieldInfo(alias="alertedTime", default=None)
    """Time the crew was alerted, in ISO 8601 UTC format with millisecond precision."""

    alert_type: Optional[str] = FieldInfo(alias="alertType", default=None)
    """
    Type of alert for the crew (e.g., ALPHA for maximum readiness, BRAVO for
    standby, etc.).
    """

    arms_crew_unit: Optional[str] = FieldInfo(alias="armsCrewUnit", default=None)
    """The crew's Aviation Resource Management System (ARMS) unit.

    If multiple units exist, use the Aircraft Commander's Unit.
    """

    assigned_qual_code: Optional[List[str]] = FieldInfo(alias="assignedQualCode", default=None)
    """
    Array of qualification codes assigned to this crew (e.g., AL for Aircraft
    Leader, CS for Combat Systems Operator, etc.).
    """

    commander_id: Optional[str] = FieldInfo(alias="commanderId", default=None)
    """Unique identifier of the crew commander assigned by the originating source."""

    commander_last4_ssn: Optional[str] = FieldInfo(alias="commanderLast4SSN", default=None)
    """Last four digits of the crew commander's social security number."""

    commander_name: Optional[str] = FieldInfo(alias="commanderName", default=None)
    """The name of the crew commander."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    crew_home: Optional[bool] = FieldInfo(alias="crewHome", default=None)
    """
    Flag indicating whether this crew task takes the crew home and out of the stage.
    """

    crew_members: Optional[List[CrewMember]] = FieldInfo(alias="crewMembers", default=None)
    """CrewMembers Collection."""

    crew_name: Optional[str] = FieldInfo(alias="crewName", default=None)
    """Name of the formed crew."""

    crew_rms: Optional[str] = FieldInfo(alias="crewRMS", default=None)
    """The resource management system managing and reporting data on this crew."""

    crew_role: Optional[str] = FieldInfo(alias="crewRole", default=None)
    """The crew's role on the mission (e.g., DEADHEAD, MEDICAL, PRIMARY)."""

    crew_source: Optional[str] = FieldInfo(alias="crewSource", default=None)
    """
    The military component that comprises the crew (e.g., ACTIVE, RESERVE, GUARD,
    MIXED, UNKNOWN, etc.).
    """

    crew_squadron: Optional[str] = FieldInfo(alias="crewSquadron", default=None)
    """The squadron the crew serves."""

    crew_type: Optional[str] = FieldInfo(alias="crewType", default=None)
    """
    The type of crew required to meet mission objectives (e.g., AIRDROP, AIRLAND,
    AIR REFUELING, etc.).
    """

    crew_unit: Optional[str] = FieldInfo(alias="crewUnit", default=None)
    """The crew's squadron as identified in its resource management system.

    If the crew is composed of members from multiple units, then the Crew
    Commander's unit should be indicated as the crew unit.
    """

    crew_wing: Optional[str] = FieldInfo(alias="crewWing", default=None)
    """The wing the crew serves."""

    current_icao: Optional[str] = FieldInfo(alias="currentICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the airfield at
    which the crew is currently located.
    """

    fdp_elig_type: Optional[str] = FieldInfo(alias="fdpEligType", default=None)
    """Crew Flight Duty Period (FDP) eligibility type."""

    fdp_type: Optional[str] = FieldInfo(alias="fdpType", default=None)
    """Flight Duty Period (FDP) type."""

    female_enlisted_qty: Optional[int] = FieldInfo(alias="femaleEnlistedQty", default=None)
    """The number of female enlisted crew members."""

    female_officer_qty: Optional[int] = FieldInfo(alias="femaleOfficerQty", default=None)
    """The number of female officer crew members."""

    flt_auth_num: Optional[str] = FieldInfo(alias="fltAuthNum", default=None)
    """Authorization number used on the flight order."""

    id_site_current: Optional[str] = FieldInfo(alias="idSiteCurrent", default=None)
    """Unique identifier of the Site at which the crew is currently located.

    This ID can be used to obtain additional information on a Site using the 'get by
    ID' operation (e.g. /udl/site/{id}). For example, the Site object with idSite =
    abc would be queried as /udl/site/abc.
    """

    id_sortie: Optional[str] = FieldInfo(alias="idSortie", default=None)
    """Unique identifier of the Aircraft Sortie associated with this crew record."""

    init_start_time: Optional[datetime] = FieldInfo(alias="initStartTime", default=None)
    """
    Initial start time of the crew's linked task that was delinked due to mission
    closure, in ISO 8601 UTC format with millisecond precision.
    """

    last_alert_time: Optional[datetime] = FieldInfo(alias="lastAlertTime", default=None)
    """
    The last time the crew can be alerted, in ISO 8601 UTC format with millisecond
    precision.
    """

    legal_alert_time: Optional[datetime] = FieldInfo(alias="legalAlertTime", default=None)
    """
    Time the crew is legal for alert, in ISO 8601 UTC format with millisecond
    precision.
    """

    legal_bravo_time: Optional[datetime] = FieldInfo(alias="legalBravoTime", default=None)
    """
    Time the crew is legally authorized or scheduled to remain on standby for duty,
    in ISO 8601 UTC format with millisecond precision.
    """

    linked_task: Optional[bool] = FieldInfo(alias="linkedTask", default=None)
    """Flag indicating whether this crew is part of a linked flying task."""

    male_enlisted_qty: Optional[int] = FieldInfo(alias="maleEnlistedQty", default=None)
    """The number of male enlisted crew members."""

    male_officer_qty: Optional[int] = FieldInfo(alias="maleOfficerQty", default=None)
    """The number of male officer crew members."""

    mission_alias: Optional[str] = FieldInfo(alias="missionAlias", default=None)
    """User-defined alias designation for the mission."""

    mission_id: Optional[str] = FieldInfo(alias="missionId", default=None)
    """The mission ID the crew is supporting according to the source system."""

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

    personnel_type: Optional[str] = FieldInfo(alias="personnelType", default=None)
    """The type of personnel that comprises the crew (e.g., AIRCREW, MEDCREW, etc.)."""

    pickup_time: Optional[datetime] = FieldInfo(alias="pickupTime", default=None)
    """
    Time the crew will be picked up from lodging, in ISO 8601 UTC format with
    millisecond precision.
    """

    post_rest_applied: Optional[bool] = FieldInfo(alias="postRestApplied", default=None)
    """
    Flag indicating whether post-mission crew rest is applied to the last sortie of
    a crew's task.
    """

    post_rest_end: Optional[datetime] = FieldInfo(alias="postRestEnd", default=None)
    """
    End time of the crew rest period after the mission, in ISO 8601 UTC format with
    millisecond precision.
    """

    post_rest_offset: Optional[str] = FieldInfo(alias="postRestOffset", default=None)
    """
    The scheduled delay or adjustment in the start time of a crew's rest period
    after a mission, expressed as +/-HH:MM.
    """

    pre_rest_applied: Optional[bool] = FieldInfo(alias="preRestApplied", default=None)
    """
    Flag indicating whether pre-mission crew rest is applied to the first sortie of
    a crew's task.
    """

    pre_rest_start: Optional[datetime] = FieldInfo(alias="preRestStart", default=None)
    """
    Start time of the crew rest period before the mission, in ISO 8601 UTC format
    with millisecond precision.
    """

    req_qual_code: Optional[List[str]] = FieldInfo(alias="reqQualCode", default=None)
    """
    Array of qualification codes required for this crew (e.g., AL for Aircraft
    Leader, CS for Combat Systems Operator, etc.).
    """

    return_time: Optional[datetime] = FieldInfo(alias="returnTime", default=None)
    """Scheduled return time, in ISO 8601 UTC format with millisecond precision."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    stage1_qual: Optional[str] = FieldInfo(alias="stage1Qual", default=None)
    """
    The stage 1 qualifications the crew must have for a mission, such as having
    basic knowledge of crew operations and aircraft systems.
    """

    stage2_qual: Optional[str] = FieldInfo(alias="stage2Qual", default=None)
    """
    The stage 2 qualifications the crew must have for a mission, such as completion
    of advanced mission-specific training.
    """

    stage3_qual: Optional[str] = FieldInfo(alias="stage3Qual", default=None)
    """
    The stage 3 qualifications the crew must have for a mission, such as full
    mission-ready certification and the capability of leading complex operations.
    """

    stage_name: Optional[str] = FieldInfo(alias="stageName", default=None)
    """Stage name for the crew.

    A stage is a pool of crews supporting a given operation plan.
    """

    stage_time: Optional[datetime] = FieldInfo(alias="stageTime", default=None)
    """
    Time the crew entered the stage, in ISO 8601 UTC format with millisecond
    precision.
    """

    status: Optional[str] = None
    """Crew status (e.g.

    NEEDCREW, ASSIGNED, APPROVED, NOTIFIED, PARTIAL, UNKNOWN, etc.).
    """

    transport_req: Optional[bool] = FieldInfo(alias="transportReq", default=None)
    """
    Flag indicating that one or more crew members requires transportation to the
    departure location.
    """

    trip_kit: Optional[str] = FieldInfo(alias="tripKit", default=None)
    """Identifies the trip kit needed by the crew.

    A trip kit contains charts, regulations, maps, etc. carried by the crew during
    missions.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
