# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AirspaceControlOrderCreateBulkParams",
    "Body",
    "BodyAirspaceControlMeansStatus",
    "BodyAirspaceControlMeansStatusAirspaceControlMean",
    "BodyAirspaceControlMeansStatusAirspaceControlMeanAirspaceControlPoint",
    "BodyAirspaceControlMeansStatusAirspaceControlMeanAirspaceTimePeriod",
    "BodyAirspaceControlOrderReference",
]


class AirspaceControlOrderCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyAirspaceControlMeansStatusAirspaceControlMeanAirspaceControlPoint(TypedDict, total=False):
    ctrl_pt_altitude: Annotated[str, PropertyInfo(alias="ctrlPtAltitude")]
    """The altitude of the control point."""

    ctrl_pt_location: Annotated[str, PropertyInfo(alias="ctrlPtLocation")]
    """
    A geospatial point coordinate specified in DMS (Degrees, Minutes, Seconds)
    format that represents the location of the control point.
    """

    ctrl_pt_name: Annotated[str, PropertyInfo(alias="ctrlPtName")]
    """The name applied to the control point, used as a reference."""

    ctrl_pt_type: Annotated[str, PropertyInfo(alias="ctrlPtType")]
    """One of possible control point type codes, such as CP, ER, OT, etc."""


class BodyAirspaceControlMeansStatusAirspaceControlMeanAirspaceTimePeriod(TypedDict, total=False):
    int_dur: Annotated[List[str], PropertyInfo(alias="intDur")]
    """Mandatory if timeMode is INTERVAL.

    Can be a numerical multiplier on an interval frequency code, a stop time
    qualifier code such as AFTER, NET, UFN, etc, or a datetime like string.
    """

    int_freq: Annotated[List[str], PropertyInfo(alias="intFreq")]
    """Mandatory if timeMode is INTERVAL.

    Can be one of the interval frequency codes, such as BIWEEKLY, DAILY, YEARLY,
    etc.
    """

    time_end: Annotated[str, PropertyInfo(alias="timeEnd")]
    """The end time designating that the airspace control order is no longer active.

    Can contain datetime information or a stop time qualifier code, such as AFTER,
    NET, UFN, etc.
    """

    time_mode: Annotated[str, PropertyInfo(alias="timeMode")]
    """The airspace time code associated with the ACO.

    Can be DISCRETE, a fixed time block, or INTERVAL, a repeating time block.
    """

    time_start: Annotated[str, PropertyInfo(alias="timeStart")]
    """The start time designating that the airspace control order is active."""


class BodyAirspaceControlMeansStatusAirspaceControlMean(TypedDict, total=False):
    airspace_control_point: Annotated[
        Iterable[BodyAirspaceControlMeansStatusAirspaceControlMeanAirspaceControlPoint],
        PropertyInfo(alias="airspaceControlPoint"),
    ]
    """
    The controlPoint set describes any reference/controlling/rendezvous point for a
    given airspace control means.
    """

    airspace_time_period: Annotated[
        Iterable[BodyAirspaceControlMeansStatusAirspaceControlMeanAirspaceTimePeriod],
        PropertyInfo(alias="airspaceTimePeriod"),
    ]
    """
    The timePeriods set describes the effective datetime for a given airspace
    control means.
    """

    bearing0: float
    """A bearing measured from true North, in angular degrees.

    If cmShape is set to "POLYARC" or "RADARC", this field is required and is mapped
    to the "beginning" radial bearing parameter.
    """

    bearing1: float
    """A bearing measured from true North, in angular degrees.

    If cmShape is set to "POLYARC" or "RADARC", this field is required and is mapped
    to the "ending" radial bearing parameter.
    """

    cm_id: Annotated[str, PropertyInfo(alias="cmId")]
    """Airspace control means name or designator."""

    cm_shape: Annotated[
        Literal["POLYARC", "1TRACK", "POLYGON", "CIRCLE", "CORRIDOR", "APOINT", "AORBIT", "GEOLINE"],
        PropertyInfo(alias="cmShape"),
    ]
    """Designates the geometric type that defines the airspace shape.

    One of CIRCLE, CORRIDOR, LINE, ORBIT, etc.
    """

    cm_type: Annotated[str, PropertyInfo(alias="cmType")]
    """The code for the type of airspace control means."""

    cntrl_auth: Annotated[str, PropertyInfo(alias="cntrlAuth")]
    """
    The commander responsible within a specified geographical area for the airspace
    control operation assigned to him.
    """

    cntrl_auth_freqs: Annotated[List[str], PropertyInfo(alias="cntrlAuthFreqs")]
    """The frequency for the airspace control authority.

    Can specify HZ, KHZ, MHZ, GHZ or a DESIG frequency designator code.
    """

    coord0: str
    """
    A geospatial point coordinate specified in DMS (Degrees, Minutes, Seconds)
    format. The fields coord0 and coord1 should be used in the specification of any
    airspace control shape that requires exactly one (1) or two (2) reference points
    for construction. For shapes requiring one reference point, for instance, when
    cmShape is set to "APOINT", this field is required and singularly defines the
    shape. Similarly, this field is required to define the center point of a
    "CIRCLE" shape, or the "origin of bearing" for arcs.
    """

    coord1: str
    """
    A geospatial point coordinate specified in DMS (Degrees, Minutes, Seconds)
    format. The fields coord0 and coord1 should be used in the specification of any
    airspace control shape that requires exactly one (1) or two (2) reference points
    for construction. For shapes requiring one reference point, for instance, when
    cmShape is set to "APOINT", this field is required and singularly defines the
    shape. Similarly, this field is required to define the center point of a
    "CIRCLE" shape, or the "origin of bearing" for arcs.
    """

    corr_way_points: Annotated[List[str], PropertyInfo(alias="corrWayPoints")]
    """
    An array of at least two alphanumeric symbols used to serially identify the
    corridor waypoints. If cmShape is set to "CORRIDOR", one of either corrWayPoints
    or polyCoord is required to specify the centerline of the corridor path.
    """

    eff_v_dim: Annotated[str, PropertyInfo(alias="effVDim")]
    """Description of the airspace vertical dimension."""

    free_text: Annotated[str, PropertyInfo(alias="freeText")]
    """
    General informat detailing the transit instruction for the airspace control
    means.
    """

    gen_text_ind: Annotated[str, PropertyInfo(alias="genTextInd")]
    """Used to provide transit instructions for the airspace control means."""

    geo_datum_alt: Annotated[str, PropertyInfo(alias="geoDatumAlt")]
    """
    Specifies the geodetic datum by which the spatial coordinates of the controlled
    airspace are calculated, if different from the top level ACO datum.
    """

    link16_id: Annotated[str, PropertyInfo(alias="link16Id")]
    """Unique Link 16 identifier assigned to the airspace control means."""

    orbit_alignment: Annotated[str, PropertyInfo(alias="orbitAlignment")]
    """Orbit alignment look-up code. Can be C=Center, L=Left, R=Right."""

    poly_coord: Annotated[List[str], PropertyInfo(alias="polyCoord")]
    """
    A set of geospatial coordinates specified in DMS (Degrees, Minutes, Seconds)
    format which determine the vertices of a one or two dimensional geospatial
    shape. When cmShape is set to "POLYARC" or "POLYGON", this field is required as
    applied in the construction of the area boundary. If cmShape is set to
    "CORRIDOR" or "GEOLINE", this field is required and can be interpreted as an
    ordered set of points along a path in space.
    """

    rad_mag0: Annotated[float, PropertyInfo(alias="radMag0")]
    """A distance that represents a radial magnitude.

    If cmShape is set to "CIRCLE" or "POLYARC", one of either fields radMag0 or
    radMag1 is required. If cmShape is set to "RADARC", this field is required and
    maps to the "inner" radial magnitude arc limit. If provided, the field
    radMagUnit is required.
    """

    rad_mag1: Annotated[float, PropertyInfo(alias="radMag1")]
    """A distance that represents a radial magnitude.

    If cmShape is set to "CIRCLE" or "POLYARC", one of either fields radMag0 or
    radMag1 is required. If cmShape is set to "RADARC", this field is required and
    maps to the "outer" radial magnitude arc limit. If provided, the field
    radMagUnit is required.
    """

    rad_mag_unit: Annotated[str, PropertyInfo(alias="radMagUnit")]
    """Specifies the unit of length in which radial magnitudes are given.

    Use M for meters, KM for kilometers, or NM for nautical miles.
    """

    track_leg: Annotated[int, PropertyInfo(alias="trackLeg")]
    """
    Index of a segment in an airtrack, which is defined by an ordered set of points.
    """

    trans_altitude: Annotated[str, PropertyInfo(alias="transAltitude")]
    """
    The altitude at or below which the vertical position of an aircraft is
    controlled by reference to true altitude.
    """

    usage: str
    """Designates the means by which a defined airspace control means is to be used."""

    width: float
    """Used to describe the "side to side" distance of a target, object or area.

    If cmShape is set to "CORRIDOR" or "AORBIT", this field is required and is
    mapped to the width parameter. If provided, the field widthUnit is required.
    """

    width_left: Annotated[float, PropertyInfo(alias="widthLeft")]
    """
    Given an ordered pair of spatial coordinates (p0, p1), defines a distance
    extending into the LEFT half-plane relative to the direction of the vector that
    maps p0 to p1. If cmShape is set to "1TRACK", this field is required to define
    the width of the airspace track as measured from the left of the track segment
    line. If provided, the field widthUnit is required.
    """

    width_right: Annotated[float, PropertyInfo(alias="widthRight")]
    """
    Given an ordered pair of spatial coordinates (p0, p1), defines a distance
    extending into the RIGHT half-plane relative to the direction of the vector that
    maps p0 to p1. If cmShape is set to "1TRACK", this field is required to define
    the width of the airspace track as measured from the right of the track segment
    line. If provided, the field widthUnit is required.
    """

    width_unit: Annotated[str, PropertyInfo(alias="widthUnit")]
    """Specifies the unit of length for which widths are given.

    Use M for meters, KM for kilometers, or NM for nautical miles.
    """


class BodyAirspaceControlMeansStatus(TypedDict, total=False):
    airspace_control_means: Annotated[
        Iterable[BodyAirspaceControlMeansStatusAirspaceControlMean], PropertyInfo(alias="airspaceControlMeans")
    ]
    """
    A conditional nested segment to report multiple airspace control means within a
    particular airspace control means status.
    """

    cm_stat: Annotated[str, PropertyInfo(alias="cmStat")]
    """Status of Airspace Control Means. Must be ADD, CHANGE, or DELETE."""

    cm_stat_id: Annotated[List[str], PropertyInfo(alias="cmStatId")]
    """Airspace control means name or designator.

    Mandatory if acmStat equals "DELETE," otherwise this field is prohibited.
    """


class BodyAirspaceControlOrderReference(TypedDict, total=False):
    ref_originator: Annotated[str, PropertyInfo(alias="refOriginator")]
    """The originator of this reference."""

    ref_serial_num: Annotated[str, PropertyInfo(alias="refSerialNum")]
    """The reference serial number."""

    ref_si_cs: Annotated[List[str], PropertyInfo(alias="refSICs")]
    """
    Array of NATO Subject Indicator Codes (SIC) or filing numbers of the document
    being referenced.
    """

    ref_s_id: Annotated[str, PropertyInfo(alias="refSId")]
    """
    Specifies an alphabetic serial number identifying a reference pertaining to this
    message.
    """

    ref_special_notation: Annotated[str, PropertyInfo(alias="refSpecialNotation")]
    """
    Indicates any special actions, restrictions, guidance, or information relating
    to this reference.
    """

    ref_ts: Annotated[Union[str, datetime], PropertyInfo(alias="refTs", format="iso8601")]
    """
    Timestamp of the referenced message, in ISO 8601 UTC format with millisecond
    precision.
    """

    ref_type: Annotated[str, PropertyInfo(alias="refType")]
    """Specifies the type for this reference."""


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

    op_ex_name: Required[Annotated[str, PropertyInfo(alias="opExName")]]
    """
    Specifies the unique operation or exercise name, nickname, or codeword assigned
    to a joint exercise or operation plan.
    """

    originator: Required[str]
    """The identifier of the originator of this message."""

    source: Required[str]
    """Source of the data."""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]
    """
    The start of the effective time period of this airspace control order, in ISO
    8601 UTC format with millisecond precision.
    """

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    aco_comments: Annotated[str, PropertyInfo(alias="acoComments")]
    """Free text information expressed in natural language."""

    aco_serial_num: Annotated[str, PropertyInfo(alias="acoSerialNum")]
    """The serial number of this airspace control order."""

    airspace_control_means_status: Annotated[
        Iterable[BodyAirspaceControlMeansStatus], PropertyInfo(alias="airspaceControlMeansStatus")
    ]
    """
    Mandatory nested segment to report multiple airspace control means statuses
    within an ACOID.
    """

    airspace_control_order_references: Annotated[
        Iterable[BodyAirspaceControlOrderReference], PropertyInfo(alias="airspaceControlOrderReferences")
    ]
    """
    The airspaceControlReferences set provides both USMTF and non-USMTF references
    for this airspace control order.
    """

    area_of_validity: Annotated[str, PropertyInfo(alias="areaOfValidity")]
    """Name of the area of the command for which the ACO is valid."""

    class_reasons: Annotated[List[str], PropertyInfo(alias="classReasons")]
    """Mandatory if classSource uses the "IORIG" designator.

    Must be a REASON FOR CLASSIFICATION code.
    """

    class_source: Annotated[str, PropertyInfo(alias="classSource")]
    """
    Markings defining the source material or the original classification authority
    for the ACO message.
    """

    declass_exemption_codes: Annotated[List[str], PropertyInfo(alias="declassExemptionCodes")]
    """
    Coded entries that provide justification for exemption from automatic
    downgrading or declassification of the airspace control order.
    """

    downgrade_ins_dates: Annotated[List[str], PropertyInfo(alias="downgradeInsDates")]
    """
    Markings providing the literal guidance or date for downgrading or declassifying
    the airspace control order.
    """

    geo_datum: Annotated[str, PropertyInfo(alias="geoDatum")]
    """
    Specifies the geodetic datum by which the spatial coordinates of the controlled
    airspace are calculated.
    """

    month: str
    """The month in which the message originated."""

    op_ex_info: Annotated[str, PropertyInfo(alias="opExInfo")]
    """
    Supplementary name that can be used to further identify exercise nicknames, or
    to provide the primary nickname of the option or the alternative of an
    operational plan.
    """

    op_ex_info_alt: Annotated[str, PropertyInfo(alias="opExInfoAlt")]
    """
    The secondary supplementary nickname of the option or the alternative of the
    operational plan or order.
    """

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    plan_orig_num: Annotated[str, PropertyInfo(alias="planOrigNum")]
    """
    The official identifier of the military establishment responsible for the
    operation plan and the identification number assigned to this plan.
    """

    qualifier: str
    """The qualifier which caveats the message status."""

    qual_sn: Annotated[int, PropertyInfo(alias="qualSN")]
    """The serial number associated with the message qualifier."""

    serial_num: Annotated[str, PropertyInfo(alias="serialNum")]
    """The unique message identifier sequentially assigned by the originator."""

    stop_qualifier: Annotated[str, PropertyInfo(alias="stopQualifier")]
    """
    A qualifier for the end of the effective time period of this airspace control
    order, such as AFTER, ASOF, NLT, etc. Used with field stopTime to indicate a
    relative time.
    """

    stop_time: Annotated[Union[str, datetime], PropertyInfo(alias="stopTime", format="iso8601")]
    """
    The end of the effective time period of this airspace control order, in ISO 8601
    UTC format with millisecond precision.
    """

    und_lnk_trks: Annotated[List[str], PropertyInfo(alias="undLnkTrks")]
    """
    Array of unique link 16 identifiers that will be assigned to a future airspace
    control means.
    """
