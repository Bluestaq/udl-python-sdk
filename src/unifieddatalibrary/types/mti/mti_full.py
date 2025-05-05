# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "MtiFull",
    "Dwell",
    "DwellD32",
    "FreeText",
    "Hrr",
    "HrrH32",
    "JobDef",
    "JobRequest",
    "Mission",
    "PlatformLoc",
]


class DwellD32(BaseModel):
    d32_1: Optional[int] = None
    """Sequential count of this MTI report within the dwell."""

    d32_10: Optional[str] = None
    """The classification of the target (i.e. vehicle, aircraft, …)."""

    d32_11: Optional[int] = None
    """
    Estimated probability that the target classification field is correctly
    classified.
    """

    d32_12: Optional[int] = None
    """
    Standard deviation of the estimated slant range of the reported detection, in
    centimeters.
    """

    d32_13: Optional[int] = None
    """
    Standard deviation of the position estimate, in the cross-range direction, of
    the reported detection, in decimeters.
    """

    d32_14: Optional[int] = None
    """Standard deviation of the estimated geodetic height, in meters."""

    d32_15: Optional[int] = None
    """
    Standard deviation of the measured line-of-sight velocity component, in
    centimeters per second.
    """

    d32_16: Optional[int] = None
    """
    The Truth Tag- Application is the Application Field truncated to 8 bits, from
    the Entity State Protocol Data Unit (PDU) used to generate the MTI Target.
    """

    d32_17: Optional[int] = None
    """
    The Truth Tag - Entity is the Entity Field from the Entity State PDU used to
    generate the MTI Target.
    """

    d32_18: Optional[int] = None
    """Estimated radar cross section of the target return, in half-decibels."""

    d32_2: Optional[float] = None
    """
    The North-South position of the reported detection, expressed as degrees North
    (positive) or South (negative) of the Equator.
    """

    d32_3: Optional[float] = None
    """
    The East-West position of the reported detection, expressed as degrees East
    (positive) from the Prime Meridian.
    """

    d32_4: Optional[int] = None
    """
    The North-South position of the reported detection, expressed as degrees North
    (positive) or South (negative) from the Dwell Area Center Latitude.
    """

    d32_5: Optional[int] = None
    """
    The East-West position of the reported detection, expressed as degrees East
    (positive, 0 to 180) or West (negative, 0 to -180) of the Prime Meridian from
    the Dwell Area Center Longitude.
    """

    d32_6: Optional[int] = None
    """
    Height of the reported detection, referenced to its position above the WGS 84
    ellipsoid, in meters.
    """

    d32_7: Optional[int] = None
    """
    The component of velocity for the reported detection, expressed in centimeters
    per second, corrected for platform motion, along the line of sight between the
    sensor and the reported detection, where the positive direction is away from the
    sensor.
    """

    d32_8: Optional[int] = None
    """
    The target wrap velocity permits trackers to un-wrap velocities for targets with
    line-of-sight components large enough to exceed the first velocity period.
    Expressed in centimeters/sec.
    """

    d32_9: Optional[int] = None
    """Estimated signal-to-noise ratio (SNR) of the target return, in decibels."""


class Dwell(BaseModel):
    d10: Optional[float] = None
    """
    Factor which modifies the value of the reported target latitude (Delta Latitude,
    field D32.4).
    """

    d11: Optional[float] = None
    """
    Factor which modifies the value of the reported target longitude (Delta
    Longitude, field D32.5).
    """

    d12: Optional[int] = None
    """
    Standard deviation in the estimated horizontal sensor location at the time of
    the dwell, measured along the sensor track direction (field D15), in
    centimeters.
    """

    d13: Optional[int] = None
    """
    Standard deviation in the estimated horizontal sensor location at the time of
    the dwell, measured orthogonal to the sensor track direction (field D15), in
    centimeters.
    """

    d14: Optional[int] = None
    """Standard deviation of the sensor altitude estimate (field D9), in centimeters."""

    d15: Optional[float] = None
    """
    Ground track of the sensor at the time of the dwell, as the angle in degrees
    (clockwise) from True North.
    """

    d16: Optional[int] = None
    """Ground speed of the sensor at the time of the dwell, in millimeters per second."""

    d17: Optional[int] = None
    """Velocity of the sensor in the vertical direction, in decimeters per second."""

    d18: Optional[int] = None
    """Standard deviation of the estimate of the sensor track, in degrees."""

    d19: Optional[int] = None
    """Standard deviation of estimate of the sensor speed, in millimeters per second."""

    d2: Optional[int] = None
    """
    Sequential count of a revisit of the bounding area in the last sent Job
    Definition Segment, where a Revisit Index of '0' indicates the first revisit.
    """

    d20: Optional[int] = None
    """
    Standard deviation of estimate of the sensor vertical velocity, expressed in
    centimeters per second.
    """

    d21: Optional[float] = None
    """
    Heading of the platform at the time of the dwell, as the angle in degrees
    (clockwise) from True North to the roll axis of the platform.
    """

    d22: Optional[float] = None
    """Pitch angle of the platform at the time of the dwell, in degrees."""

    d23: Optional[float] = None
    """Roll angle of the platform at the time of the dwell, in degrees."""

    d24: Optional[float] = None
    """
    The North-South position of the center of the dwell area, expressed as degrees
    North (positive) or South (negative) of the Equator.
    """

    d25: Optional[float] = None
    """
    The East-West position of the center of the dwell area, expressed as degrees
    East (positive, 0 to 180) or West (negative, 0 to -180) of the Prime Meridian.
    """

    d26: Optional[float] = None
    """
    Distance on the earth surface, expressed in kilometers, from the near edge to
    the center of the dwell area.
    """

    d27: Optional[float] = None
    """For dwell based radars, one-half of the 3-dB beamwidth.

    For non-dwell based radars, the angle between the beginning of the dwell to the
    center of the dwell. Measured in degrees.
    """

    d28: Optional[float] = None
    """
    Rotation of the sensor broadside face about the local vertical axis of the
    platform, in degrees.
    """

    d29: Optional[float] = None
    """
    Rotation angle of the sensor about the transverse axis of the sensor broadside,
    in degrees.
    """

    d3: Optional[int] = None
    """
    Temporally sequential count of a dwell within the revisit of a particular
    bounding area for a given job ID.
    """

    d30: Optional[float] = None
    """
    Rotation angle of the sensor about the transverse axis of the sensor broadside,
    in degrees.
    """

    d31: Optional[int] = None
    """
    Minimum velocity component, along the line of sight, which can be detected by
    the sensor, in decimeters per second.
    """

    d32: Optional[List[DwellD32]] = None
    """
    Minimum velocity component, along the line of sight, which can be detected by
    the sensor, in decimeters per second.
    """

    d4: Optional[bool] = None
    """Flag indicating the last dwell of the revisit."""

    d5: Optional[int] = None
    """
    Count of the total number of targets reported during this dwell and sent in this
    Dwell Segment.
    """

    d6: Optional[int] = None
    """
    Elapsed time, expressed in milliseconds, from midnight at the beginning of the
    day specified in the Reference Time fields (missionRefTime) of the Mission
    Segment.
    """

    d7: Optional[float] = None
    """
    North-South position of the sensor at the temporal center of the dwell, in
    degrees.
    """

    d8: Optional[float] = None
    """
    The East-West position of the sensor at the temporal center of the dwell, in
    degrees East (positive, 0 to 180) or West (negative, 0 to -180) of the Prime
    Meridian.
    """

    d9: Optional[int] = None
    """
    The altitude of the sensor at temporal center of the dwell, above the WGS 84
    ellipsoid, expressed in centimeters.
    """

    dwellts: Optional[datetime] = None
    """Dwell timestamp in ISO8601 UTC format."""


class FreeText(BaseModel):
    f1: Optional[str] = None
    """The originator of the Free Text message."""

    f2: Optional[str] = None
    """The recipient for which the Free Text message is intended."""

    f3: Optional[str] = None
    """Free text data message."""


class HrrH32(BaseModel):
    h32_1: Optional[int] = None
    """Scatterer’s power magnitude."""

    h32_2: Optional[int] = None
    """Scatterer’s complex phase, in degrees."""

    h32_3: Optional[int] = None
    """
    Scatterer’s Range index relative to Range-Doppler chip, where increasing index
    equates to increasing range.
    """

    h32_4: Optional[int] = None
    """
    Scatterer’s Doppler index relative to Range-Doppler chip, where increasing index
    equates to increasing Doppler.
    """


class Hrr(BaseModel):
    h10: Optional[int] = None
    """
    Detection threshold used to isolate significant target scatterer pixels,
    expressed as power relative to clutter mean in negative quarter-decibels.
    """

    h11: Optional[float] = None
    """3dB range impulse response of the radar, expressed in centimeters."""

    h12: Optional[float] = None
    """Slant Range pixel spacing after over sampling, expressed in centimeters."""

    h13: Optional[float] = None
    """3dB Doppler resolution of the radar, expressed in Hertz."""

    h14: Optional[float] = None
    """Doppler pixel spacing after over sampling, expressed in Hertz."""

    h15: Optional[float] = None
    """Center Frequency of the radar in GHz."""

    h16: Optional[str] = None
    """Enumeration table denoting the compression technique used."""

    h17: Optional[str] = None
    """
    Enumeration table indicating the spectral weighting used in the range
    compression process.
    """

    h18: Optional[str] = None
    """
    Enumeration table indicating the spectral weighting used in the cross-range or
    Doppler compression process.
    """

    h19: Optional[float] = None
    """Initial power of the peak scatterer, expressed in dB."""

    h2: Optional[int] = None
    """Sequential count of a revisit of the bounding area for a given job ID."""

    h20: Optional[int] = None
    """RCS of the peak scatterer, expressed in half-decibels (dB/2)."""

    h21: Optional[int] = None
    """
    When the RDM does not correlate to a single MTI report index or when the center
    range bin does not correlate to the center of the dwell; provide the range
    sample offset in meters from Dwell Center (positive is away from the sensor) of
    the first scatterer record.
    """

    h22: Optional[int] = None
    """
    When the RDM does not correlate to a single MTI report index or the center
    doppler bin does not correlate to the doppler centroid of the dwell; Doppler
    sample value in Hz of the first scatterer record.
    """

    h23: Optional[str] = None
    """Enumeration field which designates the type of data being delivered."""

    h24: Optional[str] = None
    """
    Flag field to indicate the additional signal processing techniques applied to
    the data.
    """

    h27: Optional[int] = None
    """Number of pixels in the range dimension of the chip."""

    h28: Optional[int] = None
    """
    Distance from Range Bin to closest edge in the entire chip, expressed in
    centimeters.
    """

    h29: Optional[int] = None
    """Relative velocity to skin line."""

    h3: Optional[int] = None
    """
    Sequential count of a dwell within the revisit of a particular bounding area for
    a given job ID.
    """

    h30: Optional[int] = None
    """Computed object length based upon HRR profile, in meters."""

    h31: Optional[int] = None
    """Standard deviation of estimate of the object length, expressed in meters."""

    h32: Optional[List[HrrH32]] = None
    """Standard deviation of estimate of the object length, expressed in meters."""

    h4: Optional[bool] = None
    """Flag to indicate the last dwell of the revisit."""

    h5: Optional[int] = None
    """Sequential index of the associated MTI Report."""

    h6: Optional[int] = None
    """
    Number of Range Doppler pixels that exceed target scatterer threshold and are
    reported in this segment.
    """

    h7: Optional[int] = None
    """Number of Range Bins/Samples in a Range Doppler Chip."""

    h8: Optional[int] = None
    """Number of Doppler bins in a Range-Doppler chip."""

    h9: Optional[int] = None
    """The Peak Scatter returns the maximum power level (e.g.

    in milliwatts, or dBm) registered by the sensor.
    """


class JobDef(BaseModel):
    j1: Optional[int] = None
    """
    A platform assigned number identifying the specific request or task to which the
    specific dwell pertains.
    """

    j10: Optional[float] = None
    """
    North-South position of the third corner (Point C) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j11: Optional[float] = None
    """
    East-West position of the third corner (Point C) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    j12: Optional[float] = None
    """
    North-South position of the fourth corner (Point D) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j13: Optional[float] = None
    """
    East-West position of the fourth corner (Point D) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    j14: Optional[str] = None
    """Mode in which the radar will operate for the given job ID."""

    j15: Optional[int] = None
    """The nominal revisit interval for the job ID, expressed in deciseconds.

    Value of zero, indicates that the sensor is not revisiting the previous area.
    """

    j16: Optional[int] = None
    """
    Nominal estimate of the standard deviation in the estimated horizontal (along
    track) sensor location, expressed in decimeters. measured along the sensor track
    direction defined in the Dwell segment.
    """

    j17: Optional[int] = None
    """
    Nominal estimate of the standard deviation in the estimated horizontal sensor
    location, measured orthogonal to the track direction, expressed in decimeters.
    """

    j18: Optional[int] = None
    """
    Nominal estimate of the standard deviation of the measured sensor altitude,
    expressed in decimeters.
    """

    j19: Optional[int] = None
    """
    Standard deviation of the estimate of sensor track heading, expressed in
    degrees.
    """

    j2: Optional[str] = None
    """The type of sensor or the platform."""

    j20: Optional[int] = None
    """
    Nominal standard deviation of the estimate of sensor speed, expressed in
    millimeters per second.
    """

    j21: Optional[int] = None
    """
    Nominal standard deviation of the slant range of the reported detection,
    expressed in centimeters.
    """

    j22: Optional[float] = None
    """
    Nominal standard deviation of the measured cross angle to the reported
    detection, expressed in degrees.
    """

    j23: Optional[int] = None
    """
    Nominal standard deviation of the velocity line-of-sight component, expressed in
    centimeters per second.
    """

    j24: Optional[int] = None
    """
    Nominal minimum velocity component along the line of sight, which can be
    detected by the sensor, expressed in decimeters per second.
    """

    j25: Optional[int] = None
    """
    Nominal probability that an unobscured ten square-meter target will be detected
    within the given area of surveillance.
    """

    j26: Optional[int] = None
    """
    The expected density of False Alarms (FA), expressed as the negative of the
    decibel value.
    """

    j27: Optional[str] = None
    """The terrain elevation model used for developing the target reports."""

    j28: Optional[str] = None
    """The geoid model used for developing the target reports."""

    j3: Optional[str] = None
    """Identifier of the particular variant of the sensor type."""

    j4: Optional[int] = None
    """
    Flag field indicating whether filtering has been applied to the targets detected
    within the dwell area.
    """

    j5: Optional[int] = None
    """
    Priority of this tasking request relative to all other active tasking requests
    scheduled for execution on the specified platform.
    """

    j6: Optional[float] = None
    """
    North-South position of the first corner (Point A) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j7: Optional[float] = None
    """
    East-West position of the first corner (Point A) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    j8: Optional[float] = None
    """
    North-South position of the second corner (Point B) defining the area for sensor
    service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    j9: Optional[float] = None
    """
    East-West position of the second corner (Point B) defining the area for sensor
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """


class JobRequest(BaseModel):
    job_req_est: Optional[datetime] = FieldInfo(alias="jobReqEst", default=None)
    """Specifies the Earliest Start Time for which the service is requested.

    Composite of fields R15-R20.
    """

    r1: Optional[str] = None
    """The requestor of the sensor service."""

    r10: Optional[float] = None
    """
    North-South position of the fourth corner (Point D) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r11: Optional[float] = None
    """
    East-West position of the fourth corner (Point D) defining the requested area
    for service, expressed as degrees East (positive, 0 to 180) or West (negative, 0
    to -180) of the Prime Meridian.
    """

    r12: Optional[str] = None
    """Identifies the radar mode requested by the requestor."""

    r13: Optional[int] = None
    """
    Specifies the radar range resolution requested by the requestor, expressed in
    centimeters.
    """

    r14: Optional[int] = None
    """
    Specifies the radar cross-range resolution requested by the requestor, expressed
    in decimeters.
    """

    r2: Optional[str] = None
    """Identifier for the tasking message sent by the requesting station."""

    r21: Optional[int] = None
    """
    Specifies the maximum time from the requested start time after which the request
    is to be abandoned, expressed in seconds.
    """

    r22: Optional[int] = None
    """
    Specifies the time duration for the radar job, measured from the actual start of
    the job, expressed in seconds.
    """

    r23: Optional[int] = None
    """Specifies the revisit interval for the radar job, expressed in deciseconds."""

    r24: Optional[str] = None
    """the type of sensor or the platform."""

    r25: Optional[str] = None
    """The particular variant of the sensor type."""

    r26: Optional[bool] = None
    """
    Flag field indicating that it is an initial request (flag = 0) or the desire of
    the requestor to cancel (flag = 1) the requested job.
    """

    r3: Optional[int] = None
    """
    The priority of the request relative to other requests originated by the
    requesting station.
    """

    r4: Optional[float] = None
    """
    North-South position of the first corner (Point A) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r5: Optional[float] = None
    """
    East-West position of the first corner (Point A) defining the requested area for
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """

    r6: Optional[float] = None
    """
    North-South position of the second corner (Point B) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r7: Optional[float] = None
    """
    East-West position of the second corner (Point B) defining the requested area
    for service, expressed as degrees East (positive, 0 to 180) or West (negative, 0
    to -180) of the Prime Meridian.
    """

    r8: Optional[float] = None
    """
    North-South position of the third corner (Point C) defining the requested area
    for service, expressed as degrees North (positive) or South (negative) of the
    Equator.
    """

    r9: Optional[float] = None
    """
    East-West position of the third corner (Point C) defining the requested area for
    service, expressed as degrees East (positive, 0 to 180) or West (negative, 0 to
    -180) of the Prime Meridian.
    """


class Mission(BaseModel):
    m1: Optional[str] = None
    """The mission plan id."""

    m2: Optional[str] = None
    """Unique identification of the flight plan."""

    m3: Optional[str] = None
    """Platform type that originated the data."""

    m4: Optional[str] = None
    """Identification of the platform variant, modifications, etc."""

    msn_ref_ts: Optional[date] = FieldInfo(alias="msnRefTs", default=None)
    """Mission origination date."""


class PlatformLoc(BaseModel):
    l1: Optional[int] = None
    """
    Elapsed time, expressed in milliseconds, from midnight at the beginning of the
    day specified in the Reference Time fields of the Mission Segment to the time
    the report is prepared.
    """

    l2: Optional[float] = None
    """
    North-South position of the platform at the time the report is prepared,
    expressed as degrees North (positive) or South (negative) of the Equator.
    """

    l3: Optional[float] = None
    """
    East-West position of the platform at the time the report is prepared, expressed
    as degrees East (positive) from the Prime Meridian.
    """

    l4: Optional[int] = None
    """
    Altitude of the platform at the time the report is prepared, referenced to its
    position above the WGS-84 ellipsoid, in centimeters.
    """

    l5: Optional[float] = None
    """
    Ground track of the platform at the time the report is prepared, expressed as
    the angle in degrees (clockwise) from True North.
    """

    l6: Optional[int] = None
    """
    Ground speed of the platform at the time the report is prepared, expressed as
    millimeters per second.
    """

    l7: Optional[int] = None
    """
    Velocity of the platform in the vertical direction, expressed as decimeters per
    second.
    """

    platlocts: Optional[datetime] = None
    """Platform location timestamp in ISO8601 UTC format."""


class MtiFull(BaseModel):
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

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    dwells: Optional[List[Dwell]] = None
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    free_texts: Optional[List[FreeText]] = FieldInfo(alias="freeTexts", default=None)
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    hrrs: Optional[List[Hrr]] = None
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    job_defs: Optional[List[JobDef]] = FieldInfo(alias="jobDefs", default=None)
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    job_requests: Optional[List[JobRequest]] = FieldInfo(alias="jobRequests", default=None)
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    missions: Optional[List[Mission]] = None
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
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

    p10: Optional[int] = None
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """

    p3: Optional[str] = None
    """Nationality of the platform providing the data."""

    p6: Optional[str] = None
    """Control / handling marking."""

    p7: Optional[str] = None
    """Data record exercise indicator."""

    p8: Optional[str] = None
    """
    ID of the platform providing the data (tail number for air platform, name and
    numerical designator for space-based platforms).
    """

    p9: Optional[int] = None
    """
    Integer field, assigned by the platform, that uniquely identifies the mission
    for the platform.
    """

    platform_locs: Optional[List[PlatformLoc]] = FieldInfo(alias="platformLocs", default=None)
    """
    A platform-assigned number identifying the specific request or task that
    pertains to all Dwell, HRR, and Range-Doppler segments in the packet. Job ID is
    unique within a mission.
    """
