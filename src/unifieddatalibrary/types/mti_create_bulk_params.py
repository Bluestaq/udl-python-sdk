# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MtiCreateBulkParams",
    "Body",
    "BodyDwell",
    "BodyDwellD32",
    "BodyFreeText",
    "BodyHrr",
    "BodyHrrH32",
    "BodyJobDef",
    "BodyJobRequest",
    "BodyMission",
    "BodyPlatformLoc",
]


class MtiCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyDwellD32(TypedDict, total=False):
    d32_1: int
    """Sequential count of this MTI report within the dwell."""

    d32_10: str
    """The classification of the target (i.e. vehicle, aircraft, …)."""

    d32_11: int
    """
    Estimated probability that the target classification field is correctly
    classified.
    """

    d32_12: int
    """
    Standard deviation of the estimated slant range of the reported detection, in
    centimeters.
    """

    d32_13: int
    """
    Standard deviation of the position estimate, in the cross-range direction, of
    the reported detection, in decimeters.
    """

    d32_14: int
    """Standard deviation of the estimated geodetic height, in meters."""

    d32_15: int
    """
    Standard deviation of the measured line-of-sight velocity component, in
    centimeters per second.
    """

    d32_16: int
    """
    The Truth Tag- Application is the Application Field truncated to 8 bits, from
    the Entity State Protocol Data Unit (PDU) used to generate the MTI Target.
    """

    d32_17: int
    """
    The Truth Tag - Entity is the Entity Field from the Entity State PDU used to
    generate the MTI Target.
    """

    d32_18: int
    """Estimated radar cross section of the target return, in half-decibels."""

    d32_2: float
    """
    The North-South position of the reported detection, expressed as degrees North
    (positive) or South (negative) of the Equator.
    """

    d32_3: float
    """
    The East-West position of the reported detection, expressed as degrees East
    (positive) from the Prime Meridian.
    """

    d32_4: int
    """
    The North-South position of the reported detection, expressed as degrees North
    (positive) or South (negative) from the Dwell Area Center Latitude.
    """

    d32_5: int
    """
    The East-West position of the reported detection, expressed as degrees East
    (positive, 0 to 180) or West (negative, 0 to -180) of the Prime Meridian from
    the Dwell Area Center Longitude.
    """

    d32_6: int
    """
    Height of the reported detection, referenced to its position above the WGS 84
    ellipsoid, in meters.
    """

    d32_7: int
    """
    The component of velocity for the reported detection, expressed in centimeters
    per second, corrected for platform motion, along the line of sight between the
    sensor and the reported detection, where the positive direction is away from the
    sensor.
    """

    d32_8: int
    """
    The target wrap velocity permits trackers to un-wrap velocities for targets with
    line-of-sight components large enough to exceed the first velocity period.
    Expressed in centimeters/sec.
    """

    d32_9: int
    """Estimated signal-to-noise ratio (SNR) of the target return, in decibels."""


class BodyDwell(TypedDict, total=False):
    d10: float
    """
    Factor which modifies the value of the reported target latitude (Delta Latitude,
    field D32.4).
    """

    d11: float
    """
    Factor which modifies the value of the reported target longitude (Delta
    Longitude, field D32.5).
    """

    d12: int
    """
    Standard deviation in the estimated horizontal sensor location at the time of
    the dwell, measured along the sensor track direction (field D15), in
    centimeters.
    """

    d13: int
    """
    Standard deviation in the estimated horizontal sensor location at the time of
    the dwell, measured orthogonal to the sensor track direction (field D15), in
    centimeters.
    """

    d14: int
    """Standard deviation of the sensor altitude estimate (field D9), in centimeters."""

    d15: float
    """
    Ground track of the sensor at the time of the dwell, as the angle in degrees
    (clockwise) from True North.
    """

    d16: int
    """Ground speed of the sensor at the time of the dwell, in millimeters per second."""

    d17: int
    """Velocity of the sensor in the vertical direction, in decimeters per second."""

    d18: int
    """Standard deviation of the estimate of the sensor track, in degrees."""

    d19: int
    """Standard deviation of estimate of the sensor speed, in millimeters per second."""

    d2: int
    """
    Sequential count of a revisit of the bounding area in the last sent Job
    Definition Segment, where a Revisit Index of '0' indicates the first revisit.
    """

    d20: int
    """
    Standard deviation of estimate of the sensor vertical velocity, expressed in
    centimeters per second.
    """

    d21: float
    """
    Heading of the platform at the time of the dwell, as the angle in degrees
    (clockwise) from True North to the roll axis of the platform.
    """

    d22: float
    """Pitch angle of the platform at the time of the dwell, in degrees."""

    d23: float
    """Roll angle of the platform at the time of the dwell, in degrees."""

    d24: float
    """
    The North-South position of the center of the dwell area, expressed as degrees
    North (positive) or South (negative) of the Equator.
    """

    d25: float
    """
    The East-West position of the center of the dwell area, expressed as degrees
    East (positive, 0 to 180) or West (negative, 0 to -180) of the Prime Meridian.
    """

    d26: float
    """
    Distance on the earth surface, expressed in kilometers, from the near edge to
    the center of the dwell area.
    """

    d27: float
    """For dwell based radars, one-half of the 3-dB beamwidth.

    For non-dwell based radars, the angle between the beginning of the dwell to the
    center of the dwell. Measured in degrees.
    """

    d28: float
    """
    Rotation of the sensor broadside face about the local vertical axis of the
    platform, in degrees.
    """

    d29: float
    """
    Rotation angle of the sensor about the transverse axis of the sensor broadside,
    in degrees.
    """

    d3: int
    """
    Temporally sequential count of a dwell within the revisit of a particular
    bounding area for a given job ID.
    """

    d30: float
    """
    Rotation angle of the sensor about the transverse axis of the sensor broadside,
    in degrees.
    """

    d31: int
    """
    Minimum velocity component, along the line of sight, which can be detected by
    the sensor, in decimeters per second.
    """

    d32: Iterable[BodyDwellD32]
    """
    Minimum velocity component, along the line of sight, which can be detected by
    the sensor, in decimeters per second.
    """

    d4: bool
    """Flag indicating the last dwell of the revisit."""

    d5: int
    """
    Count of the total number of targets reported during this dwell and sent in this
    Dwell Segment.
    """

    d6: int
    """
    Elapsed time, expressed in milliseconds, from midnight at the beginning of the
    day specified in the Reference Time fields (missionRefTime) of the Mission
    Segment.
    """

    d7: float
    """
    North-South position of the sensor at the temporal center of the dwell, in
    degrees.
    """

    d8: float
    """
    The East-West position of the sensor at the temporal center of the dwell, in
    degrees East (positive, 0 to 180) or West (negative, 0 to -180) of the Prime
    Meridian.
    """

    d9: int
    """
    The altitude of the sensor at temporal center of the dwell, above the WGS 84
    ellipsoid, expressed in centimeters.
    """

    dwellts: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Dwell timestamp in ISO8601 UTC format."""


class BodyFreeText(TypedDict, total=False):
    f1: str
    """The originator of the Free Text message."""

    f2: str
    """The recipient for which the Free Text message is intended."""

    f3: str
    """Free text data message."""


class BodyHrrH32(TypedDict, total=False):
    h32_1: int
    """Scatterer’s power magnitude."""

    h32_2: int
    """Scatterer’s complex phase, in degrees."""

    h32_3: int
    """
    Scatterer’s Range index relative to Range-Doppler chip, where increasing index
    equates to increasing range.
    """

    h32_4: int
    """
    Scatterer’s Doppler index relative to Range-Doppler chip, where increasing index
    equates to increasing Doppler.
    """


class BodyHrr(TypedDict, total=False):
    h10: int
    """
    Detection threshold used to isolate significant target scatterer pixels,
    expressed as power relative to clutter mean in negative quarter-decibels.
    """

    h11: float
    """3dB range impulse response of the radar, expressed in centimeters."""

    h12: float
    """Slant Range pixel spacing after over sampling, expressed in centimeters."""

    h13: float
    """3dB Doppler resolution of the radar, expressed in Hertz."""

    h14: float
    """Doppler pixel spacing after over sampling, expressed in Hertz."""

    h15: float
    """Center Frequency of the radar in GHz."""

    h16: str
    """Enumeration table denoting the compression technique used."""

    h17: str
    """
    Enumeration table indicating the spectral weighting used in the range
    compression process.
    """

    h18: str
    """
    Enumeration table indicating the spectral weighting used in the cross-range or
    Doppler compression process.
    """

    h19: float
    """Initial power of the peak scatterer, expressed in dB."""

    h2: int
    """Sequential count of a revisit of the bounding area for a given job ID."""

    h20: int
    """RCS of the peak scatterer, expressed in half-decibels (dB/2)."""

    h21: int
    """
    When the RDM does not correlate to a single MTI report index or when the center
    range bin does not correlate to the center of the dwell; provide the range
    sample offset in meters from Dwell Center (positive is away from the sensor) of
    the first scatterer record.
    """

    h22: int
    """
    When the RDM does not correlate to a single MTI report index or the center
    doppler bin does not correlate to the doppler centroid of the dwell; Doppler
    sample value in Hz of the first scatterer record.
    """

    h23: str
    """Enumeration field which designates the type of data being delivered."""

    h24: str
    """
    Flag field to indicate the additional signal processing techniques applied to
    the data.
    """

    h27: int
    """Number of pixels in the range dimension of the chip."""

    h28: int
    """
    Distance from Range Bin to closest edge in the entire chip, expressed in
    centimeters.
    """

    h29: int
    """Relative velocity to skin line."""

    h3: int
    """
    Sequential count of a dwell within the revisit of a particular bounding area for
    a given job ID.
    """

    h30: int
    """Computed object length based upon HRR profile, in meters."""

    h31: int
    """Standard deviation of estimate of the object length, expressed in meters."""

    h32: Iterable[BodyHrrH32]
    """Standard deviation of estimate of the object length, expressed in meters."""

    h4: bool
    """Flag to indicate the last dwell of the revisit."""

    h5: int
    """Sequential index of the associated MTI Report."""

    h6: int
    """
    Number of Range Doppler pixels that exceed target scatterer threshold and are
    reported in this segment.
    """

    h7: int
    """Number of Range Bins/Samples in a Range Doppler Chip."""

    h8: int
    """Number of Doppler bins in a Range-Doppler chip."""

    h9: int
    """The Peak Scatter returns the maximum power level (e.g.

    in milliwatts, or dBm) registered by the sensor.
    """


class BodyJobDef(TypedDict, total=False):
    j1: int
    """
    A platform assigned number identifying the specific request or task to which the
    specific dwell pertains.
    """

    j10: float
    """
    North-South position of the third corner (Point C) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j11: float
    """
    East-West position of the third corner (Point C) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    j12: float
    """
    North-South position of the fourth corner (Point D) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j13: float
    """
    East-West position of the fourth corner (Point D) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    j14: str
    """Mode in which the radar will operate for the given job ID."""

    j15: int
    """The nominal revisit interval for the job ID, expressed in deciseconds.

    Value of zero, indicates that the sensor is not revisiting the previous area.
    """

    j16: int
    """
    Nominal estimate of the standard deviation in the estimated horizontal (along
    track) sensor location, expressed in decimeters. measured along the sensor track
    direction defined in the Dwell segment.
    """

    j17: int
    """
    Nominal estimate of the standard deviation in the estimated horizontal sensor
    location, measured orthogonal to the track direction, expressed in decimeters.
    """

    j18: int
    """
    Nominal estimate of the standard deviation of the measured sensor altitude,
    expressed in decimeters.
    """

    j19: int
    """
    Standard deviation of the estimate of sensor track heading, expressed in
    degrees.
    """

    j2: str
    """The type of sensor or the platform."""

    j20: int
    """
    Nominal standard deviation of the estimate of sensor speed, expressed in
    millimeters per second.
    """

    j21: int
    """
    Nominal standard deviation of the slant range of the reported detection,
    expressed in centimeters.
    """

    j22: float
    """
    Nominal standard deviation of the measured cross angle to the reported
    detection, expressed in degrees.
    """

    j23: int
    """
    Nominal standard deviation of the velocity line-of-sight component, expressed in
    centimeters per second.
    """

    j24: int
    """
    Nominal minimum velocity component along the line of sight, which can be
    detected by the sensor, expressed in decimeters per second.
    """

    j25: int
    """
    Nominal probability that an unobscured ten square-meter target will be detected
    within the given area of surveillance.
    """

    j26: int
    """
    The expected density of False Alarms (FA), expressed as the negative of the
    decibel value.
    """

    j27: str
    """The terrain elevation model used for developing the target reports."""

    j28: str
    """The geoid model used for developing the target reports."""

    j3: str
    """Identifier of the particular variant of the sensor type."""

    j4: int
    """
    Flag field indicating whether filtering has been applied to the targets detected
    within the dwell area.
    """

    j5: int
    """
    Priority of this tasking request relative to all other active tasking requests
    scheduled for execution on the specified platform.
    """

    j6: float
    """
    North-South position of the first corner (Point A) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j7: float
    """
    East-West position of the first corner (Point A) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    j8: float
    """
    North-South position of the second corner (Point B) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j9: float
    """
    East-West position of the second corner (Point B) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """


class BodyJobRequest(TypedDict, total=False):
    job_req_est: Annotated[Union[str, datetime], PropertyInfo(alias="jobReqEst", format="iso8601")]
    """Specifies the Earliest Start Time for which the service is requested.

    Composite of fields R15-R20.
    """

    r1: str
    """The requestor of the sensor service."""

    r10: float
    """
    North-South position of the fourth corner (Point D) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r11: float
    """
    East-West position of the fourth corner (Point D) defining the requested area
    for service, expressed as degrees East (positive, 0 to 180) or West (negative, 0
    to -180) of the Prime Meridian.
    """

    r12: str
    """Identifies the radar mode requested by the requestor."""

    r13: int
    """
    Specifies the radar range resolution requested by the requestor, expressed in
    centimeters.
    """

    r14: int
    """
    Specifies the radar cross-range resolution requested by the requestor, expressed
    in decimeters.
    """

    r2: str
    """Identifier for the tasking message sent by the requesting station."""

    r21: int
    """
    Specifies the maximum time from the requested start time after which the request
    is to be abandoned, expressed in seconds.
    """

    r22: int
    """
    Specifies the time duration for the radar job, measured from the actual start of
    the job, expressed in seconds.
    """

    r23: int
    """Specifies the revisit interval for the radar job, expressed in deciseconds."""

    r24: str
    """the type of sensor or the platform."""

    r25: str
    """The particular variant of the sensor type."""

    r26: bool
    """
    Flag field indicating that it is an initial request (flag = 0) or the desire of
    the requestor to cancel (flag = 1) the requested job.
    """

    r3: int
    """
    The priority of the request relative to other requests originated by the
    requesting station.
    """

    r4: float
    """
    North-South position of the first corner (Point A) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r5: float
    """
    East-West position of the first corner (Point A) defining the requested area for
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    r6: float
    """
    North-South position of the second corner (Point B) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r7: float
    """
    East-West position of the second corner (Point B) defining the requested area
    for service, expressed as degrees East (positive, 0 to 180) or West (negative, 0
    to -180) of the Prime Meridian.
    """

    r8: float
    """
    North-South position of the third corner (Point C) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r9: float
    """
    East-West position of the third corner (Point C) defining the requested area for
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """


class BodyMission(TypedDict, total=False):
    m1: str
    """The mission plan id."""

    m2: str
    """Unique identification of the flight plan."""

    m3: str
    """Platform type that originated the data."""

    m4: str
    """Identification of the platform variant, modifications, etc."""

    msn_ref_ts: Annotated[Union[str, date], PropertyInfo(alias="msnRefTs", format="iso8601")]
    """Mission origination date."""


class BodyPlatformLoc(TypedDict, total=False):
    l1: int
    """
    Elapsed time, expressed in milliseconds, from midnight at the beginning of the
    day specified in the Reference Time fields of the Mission Segment to the time
    the report is prepared.
    """

    l2: float
    """
    North-South position of the platform at the time the report is prepared,
    expressed as degrees North (positive) or South (negative) of the Equator.
    """

    l3: float
    """
    East-West position of the platform at the time the report is prepared, expressed
    as degrees East (positive) from the Prime Meridian.
    """

    l4: int
    """
    Altitude of the platform at the time the report is prepared, referenced to its
    position above the WGS-84 ellipsoid, in centimeters.
    """

    l5: float
    """
    Ground track of the platform at the time the report is prepared, expressed as
    the angle in degrees (clockwise) from True North.
    """

    l6: int
    """
    Ground speed of the platform at the time the report is prepared, expressed as
    millimeters per second.
    """

    l7: int
    """
    Velocity of the platform in the vertical direction, expressed as decimeters per
    second.
    """

    platlocts: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Platform location timestamp in ISO8601 UTC format."""


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

    source: Required[str]
    """Source of the data."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    dwells: Iterable[BodyDwell]
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    free_texts: Annotated[Iterable[BodyFreeText], PropertyInfo(alias="freeTexts")]
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    hrrs: Iterable[BodyHrr]
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    job_defs: Annotated[Iterable[BodyJobDef], PropertyInfo(alias="jobDefs")]
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    job_requests: Annotated[Iterable[BodyJobRequest], PropertyInfo(alias="jobRequests")]
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    missions: Iterable[BodyMission]
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    p10: int
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    p3: str
    """Nationality of the platform providing the data."""

    p6: str
    """Control / handling marking."""

    p7: str
    """Data record exercise indicator."""

    p8: str
    """
    ID of the platform providing the data (tail number for air platform, name and
    numerical designator for space-based platforms).
    """

    p9: int
    """
    Integer field, assigned by the platform, that uniquely identifies the mission
    for the platform.
    """

    platform_locs: Annotated[Iterable[BodyPlatformLoc], PropertyInfo(alias="platformLocs")]
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """
