# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DatalinkTupleResponse",
    "DatalinkTupleResponseItem",
    "DatalinkTupleResponseItemMultiDuty",
    "DatalinkTupleResponseItemMultiDutyMultiDutyVoiceCoord",
    "DatalinkTupleResponseItemOp",
    "DatalinkTupleResponseItemReference",
    "DatalinkTupleResponseItemRefPoint",
    "DatalinkTupleResponseItemRemark",
    "DatalinkTupleResponseItemSpecTrack",
    "DatalinkTupleResponseItemVoiceCoord",
]


class DatalinkTupleResponseItemMultiDutyMultiDutyVoiceCoord(BaseModel):
    multi_comm_pri: Optional[str] = FieldInfo(alias="multiCommPri", default=None)
    """
    Priority of a communication circuit, channel or frequency for multilink
    coordination (e.g. P - Primary, M - Monitor).
    """

    multi_freq_des: Optional[str] = FieldInfo(alias="multiFreqDes", default=None)
    """
    Designator used in nonsecure communications to refer to a radio frequency for
    multilink coordination.
    """

    multi_tele_freq_nums: Optional[List[str]] = FieldInfo(alias="multiTeleFreqNums", default=None)
    """
    Array of telephone numbers or contact frequencies used for interface control for
    multilink coordination.
    """

    multi_voice_net_des: Optional[str] = FieldInfo(alias="multiVoiceNetDes", default=None)
    """
    Designator assigned to a voice interface control and coordination net for
    multilink coordination (e.g. ADCCN, DCN, VPN, etc.).
    """


class DatalinkTupleResponseItemMultiDuty(BaseModel):
    duty: Optional[str] = None
    """Specific duties assigned for multilink coordination (e.g. ICO, RICO, SICO)."""

    duty_tele_freq_nums: Optional[List[str]] = FieldInfo(alias="dutyTeleFreqNums", default=None)
    """
    Array of telephone numbers or the frequency values for radio transmission of the
    person to be contacted for multilink coordination.
    """

    multi_duty_voice_coord: Optional[List[DatalinkTupleResponseItemMultiDutyMultiDutyVoiceCoord]] = FieldInfo(
        alias="multiDutyVoiceCoord", default=None
    )
    """
    Collection of information regarding the function, frequency, and priority of
    interface control and coordination nets for multilink coordination. There can be
    0 to many DataLinkMultiVoiceCoord collections within a DataLinkMultiDuty
    collection.
    """

    name: Optional[str] = None
    """The name of the person to be contacted for multilink coordination."""

    rank: Optional[str] = None
    """The rank or position of the person to be contacted for multilink coordination."""

    unit_des: Optional[str] = FieldInfo(alias="unitDes", default=None)
    """
    Designated force of unit specified by ship name, unit call sign, or unit
    designator.
    """


class DatalinkTupleResponseItemOp(BaseModel):
    link_details: Optional[str] = FieldInfo(alias="linkDetails", default=None)
    """Detailed characteristics of the data link."""

    link_name: Optional[str] = FieldInfo(alias="linkName", default=None)
    """Name of the data link."""

    link_start_time: Optional[datetime] = FieldInfo(alias="linkStartTime", default=None)
    """
    The start of the effective time period of the data link, in ISO 8601 UTC format
    with millisecond precision.
    """

    link_stop_time: Optional[datetime] = FieldInfo(alias="linkStopTime", default=None)
    """
    The end of the effective time period of the data link, in ISO 8601 UTC format
    with millisecond precision.
    """

    link_stop_time_mod: Optional[str] = FieldInfo(alias="linkStopTimeMod", default=None)
    """
    A qualifier for the end of the effective time period of this data link, such as
    AFTER, ASOF, NLT, etc. Used with field linkStopTimeMod to indicate a relative
    time.
    """


class DatalinkTupleResponseItemReference(BaseModel):
    ref_originator: Optional[str] = FieldInfo(alias="refOriginator", default=None)
    """The originator of this reference."""

    ref_serial_id: Optional[str] = FieldInfo(alias="refSerialId", default=None)
    """
    Specifies an alphabetic serial identifier a reference pertaining to the data
    link message.
    """

    ref_serial_num: Optional[str] = FieldInfo(alias="refSerialNum", default=None)
    """Serial number assigned to this reference."""

    ref_si_cs: Optional[List[str]] = FieldInfo(alias="refSICs", default=None)
    """
    Array of NATO Subject Indicator Codes (SIC) or filing numbers of the document
    being referenced.
    """

    ref_special_notation: Optional[str] = FieldInfo(alias="refSpecialNotation", default=None)
    """
    Indicates any special actions, restrictions, guidance, or information relating
    to this reference.
    """

    ref_ts: Optional[datetime] = FieldInfo(alias="refTs", default=None)
    """
    Timestamp of the referenced message, in ISO 8601 UTC format with millisecond
    precision.
    """

    ref_type: Optional[str] = FieldInfo(alias="refType", default=None)
    """Specifies the type of document referenced."""


class DatalinkTupleResponseItemRefPoint(BaseModel):
    eff_event_time: Optional[datetime] = FieldInfo(alias="effEventTime", default=None)
    """
    Indicates when a particular event or nickname becomes effective or the old event
    or nickname is deleted, in ISO 8601 UTC format with millisecond precision.
    """

    ref_des: Optional[str] = FieldInfo(alias="refDes", default=None)
    """Identifier to designate a reference point."""

    ref_lat: Optional[float] = FieldInfo(alias="refLat", default=None)
    """WGS84 latitude of the reference point for this data link message, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    ref_loc_name: Optional[str] = FieldInfo(alias="refLocName", default=None)
    """The location name of the point of reference for this data link message."""

    ref_lon: Optional[float] = FieldInfo(alias="refLon", default=None)
    """WGS84 longitude of the reference point for this data link message, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    ref_point_type: Optional[str] = FieldInfo(alias="refPointType", default=None)
    """Type of data link reference point or grid origin."""


class DatalinkTupleResponseItemRemark(BaseModel):
    text: Optional[str] = None
    """Text of the remark."""

    type: Optional[str] = None
    """Indicates the subject matter of the remark."""


class DatalinkTupleResponseItemSpecTrack(BaseModel):
    spec_track_num: Optional[str] = FieldInfo(alias="specTrackNum", default=None)
    """
    The special track number used on the data link entered as an octal reference
    number. Used to identify a particular type of platform (e.g. MPA, KRESTA) or
    platform name (e.g. TROMP, MOUNT WHITNEY) which is not included in assigned
    track blocks.
    """

    spec_track_num_desc: Optional[str] = FieldInfo(alias="specTrackNumDesc", default=None)
    """Description of the special track number."""


class DatalinkTupleResponseItemVoiceCoord(BaseModel):
    comm_pri: Optional[str] = FieldInfo(alias="commPri", default=None)
    """
    Priority of a communication circuit, channel or frequency for this data link
    message such as P (Primary), M (Monitor), etc.
    """

    freq_des: Optional[str] = FieldInfo(alias="freqDes", default=None)
    """
    Designator used in nonsecure communications to refer to a radio frequency for
    this data link message.
    """

    tele_freq_nums: Optional[List[str]] = FieldInfo(alias="teleFreqNums", default=None)
    """
    Array of telephone numbers or contact frequencies used for interface control for
    this data link message.
    """

    voice_net_des: Optional[str] = FieldInfo(alias="voiceNetDes", default=None)
    """
    Designator assigned to a voice interface control and coordination net for this
    data link message (e.g. ADCCN, DCN, VPN, etc.).
    """


class DatalinkTupleResponseItem(BaseModel):
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

    op_ex_name: str = FieldInfo(alias="opExName")
    """
    Specifies the unique operation or exercise name, nickname, or codeword assigned
    to a joint exercise or operation plan.
    """

    originator: str
    """The identifier of the originator of this message."""

    source: str
    """Source of the data."""

    start_time: datetime = FieldInfo(alias="startTime")
    """
    The start of the effective time period of this data link message, in ISO 8601
    UTC format with millisecond precision.
    """

    id: Optional[str] = None
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    ack_inst_units: Optional[List[str]] = FieldInfo(alias="ackInstUnits", default=None)
    """
    Array of instructions for acknowledging and the force or units required to
    acknowledge the data link message being sent.
    """

    ack_req: Optional[bool] = FieldInfo(alias="ackReq", default=None)
    """
    Flag Indicating if formal acknowledgement is required for the particular data
    link message being sent.
    """

    alt_diff: Optional[int] = FieldInfo(alias="altDiff", default=None)
    """Maximum altitude difference between two air tracks, in thousands of feet.

    Required if sysDefaultCode field is "MAN". Allowable entires are 5 to 50 in
    increments of 5000 feet.
    """

    canx_id: Optional[str] = FieldInfo(alias="canxId", default=None)
    """The identifier for this data link message cancellation."""

    canx_originator: Optional[str] = FieldInfo(alias="canxOriginator", default=None)
    """The originator of this data link message cancellation."""

    canx_serial_num: Optional[str] = FieldInfo(alias="canxSerialNum", default=None)
    """Serial number assigned to this data link message cancellation."""

    canx_si_cs: Optional[List[str]] = FieldInfo(alias="canxSICs", default=None)
    """
    Array of NATO Subject Indicator Codes (SIC) or filing numbers of this data link
    message or document being cancelled.
    """

    canx_special_notation: Optional[str] = FieldInfo(alias="canxSpecialNotation", default=None)
    """
    Indicates any special actions, restrictions, guidance, or information relating
    to this data link message cancellation.
    """

    canx_ts: Optional[datetime] = FieldInfo(alias="canxTs", default=None)
    """
    Timestamp of the data link message cancellation, in ISO 8601 UTC format with
    millisecond precision.
    """

    class_reasons: Optional[List[str]] = FieldInfo(alias="classReasons", default=None)
    """Array of codes that indicate the reasons material is classified."""

    class_source: Optional[str] = FieldInfo(alias="classSource", default=None)
    """
    Markings that define the source material or the original classification
    authority for this data link message.
    """

    consec_decorr: Optional[int] = FieldInfo(alias="consecDecorr", default=None)
    """
    Number of consecutive remote track reports that must meet the decorrelation
    criteria before the decorrelation is executed. Required if sysDefaultCode field
    is "MAN". Allowable entries are integers from 1 to 5.
    """

    course_diff: Optional[int] = FieldInfo(alias="courseDiff", default=None)
    """
    Maximum difference between the reported course of the remote track and the
    calculated course of the local track. Required if sysDefaultCode field is "MAN".
    Allowable entries are 15 to 90 in increments of 15 degrees.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    dec_exempt_codes: Optional[List[str]] = FieldInfo(alias="decExemptCodes", default=None)
    """
    Array of codes that provide justification for exemption from automatic
    downgrading or declassification.
    """

    dec_inst_dates: Optional[List[str]] = FieldInfo(alias="decInstDates", default=None)
    """
    Array of markings that provide the literal guidance or dates for the downgrading
    or declassification of this data link message.
    """

    decorr_win_mult: Optional[float] = FieldInfo(alias="decorrWinMult", default=None)
    """
    Distance between the common and remote track is to exceed the applicable
    correlation window for the two tracks in order to be decorrelated. Required if
    sysDefaultCode field is "MAN". Allowable entries are 1.0 to 2.0 in increments of
    0.1.
    """

    geo_datum: Optional[str] = FieldInfo(alias="geoDatum", default=None)
    """
    The code for the point of reference from which the coordinates and networks are
    computed.
    """

    jre_call_sign: Optional[str] = FieldInfo(alias="jreCallSign", default=None)
    """
    Call sign which identifies one or more communications facilities, commands,
    authorities, or activities for Joint Range Extension (JRE) units.
    """

    jre_details: Optional[str] = FieldInfo(alias="jreDetails", default=None)
    """Joint Range Extension (JRE) unit details."""

    jre_pri_add: Optional[int] = FieldInfo(alias="jrePriAdd", default=None)
    """Link-16 octal track number assigned as the primary JTIDS unit address."""

    jre_sec_add: Optional[int] = FieldInfo(alias="jreSecAdd", default=None)
    """Link-16 octal track number assigned as the secondary JTIDS unit address."""

    jre_unit_des: Optional[str] = FieldInfo(alias="jreUnitDes", default=None)
    """Designator of the unit for Joint Range Extension (JRE)."""

    max_geo_pos_qual: Optional[int] = FieldInfo(alias="maxGeoPosQual", default=None)
    """Number used for maximum geodetic position quality.

    Required if sysDefaultCode field is "MAN". Allowable entires are integers from 1
    to 15.
    """

    max_track_qual: Optional[int] = FieldInfo(alias="maxTrackQual", default=None)
    """Track quality to prevent correlation windows from being unrealistically small.

    Required if sysDefaultCode field is "MAN". Allowable entries are integers from 8
    to 15.
    """

    mgmt_code: Optional[str] = FieldInfo(alias="mgmtCode", default=None)
    """Data link management code word."""

    mgmt_code_meaning: Optional[str] = FieldInfo(alias="mgmtCodeMeaning", default=None)
    """Data link management code word meaning."""

    min_geo_pos_qual: Optional[int] = FieldInfo(alias="minGeoPosQual", default=None)
    """Number used for minimum geodetic position quality.

    Required if sysDefaultCode field is "MAN". Allowable entries are integers from 1
    to 5.
    """

    min_track_qual: Optional[int] = FieldInfo(alias="minTrackQual", default=None)
    """Track quality to prevent correlation windows from being unrealistically large.

    Required if sysDefaultCode field is "MAN". Allowable entries are integers from 3
    to 7.
    """

    month: Optional[str] = None
    """The month in which this message originated."""

    multi_duty: Optional[List[DatalinkTupleResponseItemMultiDuty]] = FieldInfo(alias="multiDuty", default=None)
    """
    Collection of contact and identification information for designated multilink
    coordinator duty assignments. There can be 0 to many DataLinkMultiDuty
    collections within the datalink service.
    """

    non_link_unit_des: Optional[List[str]] = FieldInfo(alias="nonLinkUnitDes", default=None)
    """Array of non-link specific data unit designators."""

    op_ex_info: Optional[str] = FieldInfo(alias="opExInfo", default=None)
    """
    Provides an additional caveat further identifying the exercise or modifies the
    exercise nickname.
    """

    op_ex_info_alt: Optional[str] = FieldInfo(alias="opExInfoAlt", default=None)
    """
    The secondary nickname of the option or the alternative of the operational plan
    or order.
    """

    ops: Optional[List[DatalinkTupleResponseItemOp]] = None
    """
    Collection of information describing the establishment and detailed operation of
    tactical data links. There can be 0 to many DataLinkOps collections within the
    datalink service.
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

    plan_orig_num: Optional[str] = FieldInfo(alias="planOrigNum", default=None)
    """
    The official identifier of the military establishment responsible for the
    operation plan and the identification number assigned to this plan.
    """

    poc_call_sign: Optional[str] = FieldInfo(alias="pocCallSign", default=None)
    """
    The unit identifier or call sign of the point of contact for this data link
    message.
    """

    poc_lat: Optional[float] = FieldInfo(alias="pocLat", default=None)
    """WGS84 latitude of the point of contact for this data link message, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    poc_loc_name: Optional[str] = FieldInfo(alias="pocLocName", default=None)
    """The location name of the point of contact for this data link message."""

    poc_lon: Optional[float] = FieldInfo(alias="pocLon", default=None)
    """WGS84 longitude of the point of contact for this data link message, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    poc_name: Optional[str] = FieldInfo(alias="pocName", default=None)
    """The name of the point of contact for this data link message."""

    poc_nums: Optional[List[str]] = FieldInfo(alias="pocNums", default=None)
    """
    Array of telephone numbers, radio frequency values, or email addresses of the
    point of contact for this data link message.
    """

    poc_rank: Optional[str] = FieldInfo(alias="pocRank", default=None)
    """
    The rank or position of the point of contact for this data link message in a
    military or civilian organization.
    """

    qualifier: Optional[str] = None
    """
    The qualifier which caveats the message status such as AMP (Amplification), CHG
    (Change), etc.
    """

    qual_sn: Optional[int] = FieldInfo(alias="qualSN", default=None)
    """The serial number associated with the message qualifier."""

    raw_file_uri: Optional[str] = FieldInfo(alias="rawFileURI", default=None)
    """
    Optional URI location in the document repository of the raw file parsed by the
    system to produce this record. To download the raw file, prepend
    https://udl-hostname/scs/download?id= to this value.
    """

    references: Optional[List[DatalinkTupleResponseItemReference]] = None
    """Collection of reference information.

    There can be 0 to many DataLinkReferences collections within the datalink
    service.
    """

    ref_points: Optional[List[DatalinkTupleResponseItemRefPoint]] = FieldInfo(alias="refPoints", default=None)
    """
    Collection that identifies points of reference used in the establishment of the
    data links. There can be 1 to many DataLinkRefPoints collections within the
    datalink service.
    """

    remarks: Optional[List[DatalinkTupleResponseItemRemark]] = None
    """Collection of remarks associated with this data link message."""

    res_track_qual: Optional[int] = FieldInfo(alias="resTrackQual", default=None)
    """
    Track quality to enter if too many duals involving low track quality tracks are
    occurring. Required if sysDefaultCode field is "MAN". Allowable entries are
    integers from 2 to 6.
    """

    serial_num: Optional[str] = FieldInfo(alias="serialNum", default=None)
    """The unique message identifier assigned by the originator."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    spec_tracks: Optional[List[DatalinkTupleResponseItemSpecTrack]] = FieldInfo(alias="specTracks", default=None)
    """Collection of special track numbers used on the data links.

    There can be 0 to many DataLinkSpecTracks collections within the datalink
    service.
    """

    speed_diff: Optional[int] = FieldInfo(alias="speedDiff", default=None)
    """Maximum percentage the faster track speed may differ from the slower track
    speed.

    Required if sysDefaultCode field is "MAN". Allowable entries are 10 to 100 in
    increments of 10.
    """

    stop_time: Optional[datetime] = FieldInfo(alias="stopTime", default=None)
    """
    The end of the effective time period of this data link message, in ISO 8601 UTC
    format with millisecond precision. This may be a relative stop time if used with
    stopTimeMod.
    """

    stop_time_mod: Optional[str] = FieldInfo(alias="stopTimeMod", default=None)
    """
    A qualifier for the end of the effective time period of this data link message,
    such as AFTER, ASOF, NLT, etc. Used with field stopTime to indicate a relative
    time.
    """

    sys_default_code: Optional[str] = FieldInfo(alias="sysDefaultCode", default=None)
    """
    Indicates the data terminal settings the system defaults to, either automatic
    correlation/decorrelation (AUTO) or manual (MAN).
    """

    track_num_block_l_ls: Optional[List[int]] = FieldInfo(alias="trackNumBlockLLs", default=None)
    """Array of Link-16 octal track numbers used as the lower limit of a track block."""

    track_num_blocks: Optional[List[str]] = FieldInfo(alias="trackNumBlocks", default=None)
    """
    Array of defined ranges of Link-11/11B track numbers assigned to a participating
    unit or reporting unit.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    voice_coord: Optional[List[DatalinkTupleResponseItemVoiceCoord]] = FieldInfo(alias="voiceCoord", default=None)
    """
    Collection of information regarding the function, frequency, and priority of
    interface control and coordination nets for this data link message. There can be
    1 to many DataLinkVoiceCoord collections within the datalink service.
    """

    win_size_min: Optional[float] = FieldInfo(alias="winSizeMin", default=None)
    """
    Number added to the basic window calculated from track qualities to ensure that
    windows still allow valid correlations. Required if sysDefaultCode field is
    "MAN". Allowable entries are 0.0 to 2.0 in increments of 0.25.
    """

    win_size_mult: Optional[float] = FieldInfo(alias="winSizeMult", default=None)
    """The correlation window size multiplier to stretch or reduce the window size.

    Required if sysDefaultCode field is "MAN". Allowable entries are 0.5 to 3.0 in
    increments of 0.1.
    """


DatalinkTupleResponse: TypeAlias = List[DatalinkTupleResponseItem]
