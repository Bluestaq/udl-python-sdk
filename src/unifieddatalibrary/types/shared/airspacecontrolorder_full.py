# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AirspacecontrolorderFull",
    "AirspaceControlMeansStatus",
    "AirspaceControlMeansStatusAirspaceControlMean",
    "AirspaceControlMeansStatusAirspaceControlMeanAirspaceControlPoint",
    "AirspaceControlMeansStatusAirspaceControlMeanAirspaceTimePeriod",
    "AirspaceControlOrderReference",
]


class AirspaceControlMeansStatusAirspaceControlMeanAirspaceControlPoint(BaseModel):
    ctrl_pt_altitude: Optional[str] = FieldInfo(alias="ctrlPtAltitude", default=None)
    """The altitude of the control point."""

    ctrl_pt_location: Optional[str] = FieldInfo(alias="ctrlPtLocation", default=None)
    """
    A geospatial point coordinate specified in DMS (Degrees, Minutes, Seconds)
    format that represents the location of the control point.
    """

    ctrl_pt_name: Optional[str] = FieldInfo(alias="ctrlPtName", default=None)
    """The name applied to the control point, used as a reference."""

    ctrl_pt_type: Optional[str] = FieldInfo(alias="ctrlPtType", default=None)
    """One of possible control point type codes, such as CP, ER, OT, etc."""


class AirspaceControlMeansStatusAirspaceControlMeanAirspaceTimePeriod(BaseModel):
    int_dur: Optional[List[str]] = FieldInfo(alias="intDur", default=None)
    """Mandatory if timeMode is INTERVAL.

    Can be a numerical multiplier on an interval frequency code, a stop time
    qualifier code such as AFTER, NET, UFN, etc, or a datetime like string.
    """

    int_freq: Optional[List[str]] = FieldInfo(alias="intFreq", default=None)
    """Mandatory if timeMode is INTERVAL.

    Can be one of the interval frequency codes, such as BIWEEKLY, DAILY, YEARLY,
    etc.
    """

    time_end: Optional[str] = FieldInfo(alias="timeEnd", default=None)
    """The end time designating that the airspace control order is no longer active.

    Can contain datetime information or a stop time qualifier code, such as AFTER,
    NET, UFN, etc.
    """

    time_mode: Optional[str] = FieldInfo(alias="timeMode", default=None)
    """The airspace time code associated with the ACO.

    Can be DISCRETE, a fixed time block, or INTERVAL, a repeating time block.
    """

    time_start: Optional[str] = FieldInfo(alias="timeStart", default=None)
    """The start time designating that the airspace control order is active."""


class AirspaceControlMeansStatusAirspaceControlMean(BaseModel):
    airspace_control_point: Optional[List[AirspaceControlMeansStatusAirspaceControlMeanAirspaceControlPoint]] = (
        FieldInfo(alias="airspaceControlPoint", default=None)
    )
    """
    The controlPoint set describes any reference/controlling/rendezvous point for a
    given airspace control means.
    """

    airspace_time_period: Optional[List[AirspaceControlMeansStatusAirspaceControlMeanAirspaceTimePeriod]] = FieldInfo(
        alias="airspaceTimePeriod", default=None
    )
    """
    The timePeriods set describes the effective datetime for a given airspace
    control means.
    """

    bearing0: Optional[float] = None
    """A bearing measured from true North, in angular degrees.

    If cmShape is set to "POLYARC" or "RADARC", this field is required and is mapped
    to the "beginning" radial bearing parameter.
    """

    bearing1: Optional[float] = None
    """A bearing measured from true North, in angular degrees.

    If cmShape is set to "POLYARC" or "RADARC", this field is required and is mapped
    to the "ending" radial bearing parameter.
    """

    cm_id: Optional[str] = FieldInfo(alias="cmId", default=None)
    """Airspace control means name or designator."""

    cm_shape: Optional[Literal["POLYARC", "1TRACK", "POLYGON", "CIRCLE", "CORRIDOR", "APOINT", "AORBIT", "GEOLINE"]] = (
        FieldInfo(alias="cmShape", default=None)
    )
    """Designates the geometric type that defines the airspace shape.

    One of CIRCLE, CORRIDOR, LINE, ORBIT, etc.
    """

    cm_type: Optional[str] = FieldInfo(alias="cmType", default=None)
    """The code for the type of airspace control means."""

    cntrl_auth: Optional[str] = FieldInfo(alias="cntrlAuth", default=None)
    """
    The commander responsible within a specified geographical area for the airspace
    control operation assigned to him.
    """

    cntrl_auth_freqs: Optional[List[str]] = FieldInfo(alias="cntrlAuthFreqs", default=None)
    """The frequency for the airspace control authority.

    Can specify HZ, KHZ, MHZ, GHZ or a DESIG frequency designator code.
    """

    coord0: Optional[str] = None
    """
    A geospatial point coordinate specified in DMS (Degrees, Minutes, Seconds)
    format. The fields coord0 and coord1 should be used in the specification of any
    airspace control shape that requires exactly one (1) or two (2) reference points
    for construction. For shapes requiring one reference point, for instance, when
    cmShape is set to "APOINT", this field is required and singularly defines the
    shape. Similarly, this field is required to define the center point of a
    "CIRCLE" shape, or the "origin of bearing" for arcs.
    """

    coord1: Optional[str] = None
    """
    A geospatial point coordinate specified in DMS (Degrees, Minutes, Seconds)
    format. The fields coord0 and coord1 should be used in the specification of any
    airspace control shape that requires exactly one (1) or two (2) reference points
    for construction. For shapes requiring one reference point, for instance, when
    cmShape is set to "APOINT", this field is required and singularly defines the
    shape. Similarly, this field is required to define the center point of a
    "CIRCLE" shape, or the "origin of bearing" for arcs.
    """

    corr_way_points: Optional[List[str]] = FieldInfo(alias="corrWayPoints", default=None)
    """
    An array of at least two alphanumeric symbols used to serially identify the
    corridor waypoints. If cmShape is set to "CORRIDOR", one of either corrWayPoints
    or polyCoord is required to specify the centerline of the corridor path.
    """

    eff_v_dim: Optional[str] = FieldInfo(alias="effVDim", default=None)
    """Description of the airspace vertical dimension."""

    free_text: Optional[str] = FieldInfo(alias="freeText", default=None)
    """
    General informat detailing the transit instruction for the airspace control
    means.
    """

    gen_text_ind: Optional[str] = FieldInfo(alias="genTextInd", default=None)
    """Used to provide transit instructions for the airspace control means."""

    geo_datum_alt: Optional[str] = FieldInfo(alias="geoDatumAlt", default=None)
    """
    Specifies the geodetic datum by which the spatial coordinates of the controlled
    airspace are calculated, if different from the top level ACO datum.
    """

    link16_id: Optional[str] = FieldInfo(alias="link16Id", default=None)
    """Unique Link 16 identifier assigned to the airspace control means."""

    orbit_alignment: Optional[str] = FieldInfo(alias="orbitAlignment", default=None)
    """Orbit alignment look-up code. Can be C=Center, L=Left, R=Right."""

    poly_coord: Optional[List[str]] = FieldInfo(alias="polyCoord", default=None)
    """
    A set of geospatial coordinates specified in DMS (Degrees, Minutes, Seconds)
    format which determine the vertices of a one or two dimensional geospatial
    shape. When cmShape is set to "POLYARC" or "POLYGON", this field is required as
    applied in the construction of the area boundary. If cmShape is set to
    "CORRIDOR" or "GEOLINE", this field is required and can be interpreted as an
    ordered set of points along a path in space.
    """

    rad_mag0: Optional[float] = FieldInfo(alias="radMag0", default=None)
    """A distance that represents a radial magnitude.

    If cmShape is set to "CIRCLE" or "POLYARC", one of either fields radMag0 or
    radMag1 is required. If cmShape is set to "RADARC", this field is required and
    maps to the "inner" radial magnitude arc limit. If provided, the field
    radMagUnit is required.
    """

    rad_mag1: Optional[float] = FieldInfo(alias="radMag1", default=None)
    """A distance that represents a radial magnitude.

    If cmShape is set to "CIRCLE" or "POLYARC", one of either fields radMag0 or
    radMag1 is required. If cmShape is set to "RADARC", this field is required and
    maps to the "outer" radial magnitude arc limit. If provided, the field
    radMagUnit is required.
    """

    rad_mag_unit: Optional[str] = FieldInfo(alias="radMagUnit", default=None)
    """Specifies the unit of length in which radial magnitudes are given.

    Use M for meters, KM for kilometers, or NM for nautical miles.
    """

    track_leg: Optional[int] = FieldInfo(alias="trackLeg", default=None)
    """
    Index of a segment in an airtrack, which is defined by an ordered set of points.
    """

    trans_altitude: Optional[str] = FieldInfo(alias="transAltitude", default=None)
    """
    The altitude at or below which the vertical position of an aircraft is
    controlled by reference to true altitude.
    """

    usage: Optional[str] = None
    """Designates the means by which a defined airspace control means is to be used."""

    width: Optional[float] = None
    """Used to describe the "side to side" distance of a target, object or area.

    If cmShape is set to "CORRIDOR" or "AORBIT", this field is required and is
    mapped to the width parameter. If provided, the field widthUnit is required.
    """

    width_left: Optional[float] = FieldInfo(alias="widthLeft", default=None)
    """
    Given an ordered pair of spatial coordinates (p0, p1), defines a distance
    extending into the LEFT half-plane relative to the direction of the vector that
    maps p0 to p1. If cmShape is set to "1TRACK", this field is required to define
    the width of the airspace track as measured from the left of the track segment
    line. If provided, the field widthUnit is required.
    """

    width_right: Optional[float] = FieldInfo(alias="widthRight", default=None)
    """
    Given an ordered pair of spatial coordinates (p0, p1), defines a distance
    extending into the RIGHT half-plane relative to the direction of the vector that
    maps p0 to p1. If cmShape is set to "1TRACK", this field is required to define
    the width of the airspace track as measured from the right of the track segment
    line. If provided, the field widthUnit is required.
    """

    width_unit: Optional[str] = FieldInfo(alias="widthUnit", default=None)
    """Specifies the unit of length for which widths are given.

    Use M for meters, KM for kilometers, or NM for nautical miles.
    """


class AirspaceControlMeansStatus(BaseModel):
    airspace_control_means: Optional[List[AirspaceControlMeansStatusAirspaceControlMean]] = FieldInfo(
        alias="airspaceControlMeans", default=None
    )
    """
    A conditional nested segment to report multiple airspace control means within a
    particular airspace control means status.
    """

    cm_stat: Optional[str] = FieldInfo(alias="cmStat", default=None)
    """Status of Airspace Control Means. Must be ADD, CHANGE, or DELETE."""

    cm_stat_id: Optional[List[str]] = FieldInfo(alias="cmStatId", default=None)
    """Airspace control means name or designator.

    Mandatory if acmStat equals "DELETE," otherwise this field is prohibited.
    """


class AirspaceControlOrderReference(BaseModel):
    ref_originator: Optional[str] = FieldInfo(alias="refOriginator", default=None)
    """The originator of this reference."""

    ref_serial_num: Optional[str] = FieldInfo(alias="refSerialNum", default=None)
    """The reference serial number."""

    ref_si_cs: Optional[List[str]] = FieldInfo(alias="refSICs", default=None)
    """
    Array of NATO Subject Indicator Codes (SIC) or filing numbers of the document
    being referenced.
    """

    ref_s_id: Optional[str] = FieldInfo(alias="refSId", default=None)
    """
    Specifies an alphabetic serial number identifying a reference pertaining to this
    message.
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
    """Specifies the type for this reference."""


class AirspacecontrolorderFull(BaseModel):
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
    The start of the effective time period of this airspace control order, in ISO
    8601 UTC format with millisecond precision.
    """

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    aco_comments: Optional[str] = FieldInfo(alias="acoComments", default=None)
    """Free text information expressed in natural language."""

    aco_serial_num: Optional[str] = FieldInfo(alias="acoSerialNum", default=None)
    """The serial number of this airspace control order."""

    airspace_control_means_status: Optional[List[AirspaceControlMeansStatus]] = FieldInfo(
        alias="airspaceControlMeansStatus", default=None
    )
    """
    Mandatory nested segment to report multiple airspace control means statuses
    within an ACOID.
    """

    airspace_control_order_references: Optional[List[AirspaceControlOrderReference]] = FieldInfo(
        alias="airspaceControlOrderReferences", default=None
    )
    """
    The airspaceControlReferences set provides both USMTF and non-USMTF references
    for this airspace control order.
    """

    area_of_validity: Optional[str] = FieldInfo(alias="areaOfValidity", default=None)
    """Name of the area of the command for which the ACO is valid."""

    class_reasons: Optional[List[str]] = FieldInfo(alias="classReasons", default=None)
    """Mandatory if classSource uses the "IORIG" designator.

    Must be a REASON FOR CLASSIFICATION code.
    """

    class_source: Optional[str] = FieldInfo(alias="classSource", default=None)
    """
    Markings defining the source material or the original classification authority
    for the ACO message.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    declass_exemption_codes: Optional[List[str]] = FieldInfo(alias="declassExemptionCodes", default=None)
    """
    Coded entries that provide justification for exemption from automatic
    downgrading or declassification of the airspace control order.
    """

    downgrade_ins_dates: Optional[List[str]] = FieldInfo(alias="downgradeInsDates", default=None)
    """
    Markings providing the literal guidance or date for downgrading or declassifying
    the airspace control order.
    """

    geo_datum: Optional[str] = FieldInfo(alias="geoDatum", default=None)
    """
    Specifies the geodetic datum by which the spatial coordinates of the controlled
    airspace are calculated.
    """

    month: Optional[str] = None
    """The month in which the message originated."""

    op_ex_info: Optional[str] = FieldInfo(alias="opExInfo", default=None)
    """
    Supplementary name that can be used to further identify exercise nicknames, or
    to provide the primary nickname of the option or the alternative of an
    operational plan.
    """

    op_ex_info_alt: Optional[str] = FieldInfo(alias="opExInfoAlt", default=None)
    """
    The secondary supplementary nickname of the option or the alternative of the
    operational plan or order.
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

    qualifier: Optional[str] = None
    """The qualifier which caveats the message status."""

    qual_sn: Optional[int] = FieldInfo(alias="qualSN", default=None)
    """The serial number associated with the message qualifier."""

    raw_file_uri: Optional[str] = FieldInfo(alias="rawFileURI", default=None)
    """
    Optional URI location in the document repository of the raw file parsed by the
    system to produce this record. To download the raw file, prepend
    https://udl-hostname/scs/download?id= to this value.
    """

    serial_num: Optional[str] = FieldInfo(alias="serialNum", default=None)
    """The unique message identifier sequentially assigned by the originator."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    stop_qualifier: Optional[str] = FieldInfo(alias="stopQualifier", default=None)
    """
    A qualifier for the end of the effective time period of this airspace control
    order, such as AFTER, ASOF, NLT, etc. Used with field stopTime to indicate a
    relative time.
    """

    stop_time: Optional[datetime] = FieldInfo(alias="stopTime", default=None)
    """
    The end of the effective time period of this airspace control order, in ISO 8601
    UTC format with millisecond precision.
    """

    und_lnk_trks: Optional[List[str]] = FieldInfo(alias="undLnkTrks", default=None)
    """
    Array of unique link 16 identifiers that will be assigned to a future airspace
    control means.
    """
