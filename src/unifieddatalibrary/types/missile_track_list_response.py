# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MissileTrackListResponse", "Vector"]


class Vector(BaseModel):
    epoch: datetime
    """Vector timestamp in ISO8601 UTC format, with microsecond precision."""

    accel: Optional[List[float]] = None
    """
    Three element array, expressing the cartesian acceleration vector of the target
    object, in kilometers/second^2, in the specified referenceFrame. If
    referenceFrame is null then ECEF should be assumed. The array element order is
    [x'', y'', z''].
    """

    confidence: Optional[int] = None
    """Confidence of the vector, 0-100."""

    course: Optional[float] = None
    """Track object course, in degrees clockwise from true north."""

    cov: Optional[List[float]] = None
    """
    Covariance matrix, in kilometer and second based units, in the specified
    covReferenceFrame.

    If the covReferenceFrame is null it is assumed to be UVW. The array values
    (1-45) represent the upper triangular half of the position-velocity-acceleration
    covariance matrix.

    The covariance elements are position dependent within the array with values
    ordered as follows:

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;y&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y'&nbsp;&nbsp;&nbsp;&nbsp;z'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x"&nbsp;&nbsp;&nbsp;&nbsp;y"&nbsp;&nbsp;&nbsp;&nbsp;z"

    x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9

    y&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;11&nbsp;&nbsp;&nbsp;12&nbsp;&nbsp;&nbsp;13&nbsp;&nbsp;&nbsp;14&nbsp;&nbsp;&nbsp;15&nbsp;&nbsp;&nbsp;16&nbsp;&nbsp;&nbsp;17

    z&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18&nbsp;&nbsp;&nbsp;19&nbsp;&nbsp;&nbsp;20&nbsp;&nbsp;&nbsp;21&nbsp;&nbsp;&nbsp;22&nbsp;&nbsp;&nbsp;23&nbsp;&nbsp;&nbsp;24

    x'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25&nbsp;&nbsp;&nbsp;26&nbsp;&nbsp;&nbsp;27&nbsp;&nbsp;&nbsp;28&nbsp;&nbsp;&nbsp;29&nbsp;&nbsp;&nbsp;30

    y'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31&nbsp;&nbsp;&nbsp;32&nbsp;&nbsp;&nbsp;33&nbsp;&nbsp;&nbsp;34&nbsp;&nbsp;&nbsp;35

    z'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36&nbsp;&nbsp;&nbsp;37&nbsp;&nbsp;&nbsp;38&nbsp;&nbsp;&nbsp;39

    x"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;40&nbsp;&nbsp;&nbsp;41&nbsp;&nbsp;&nbsp;42

    y"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;43&nbsp;&nbsp;&nbsp;44

    z"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;45

    The cov array should contain only the upper right triangle values from top left
    down to bottom right, in order.
    """

    cov_reference_frame: Optional[str] = FieldInfo(alias="covReferenceFrame", default=None)
    """The reference frame of the covariance elements (ECEF, J2000, UVW).

    If the referenceFrame is null it is assumed to be UVW.
    """

    flight_az: Optional[float] = FieldInfo(alias="flightAz", default=None)
    """The flight azimuth associated with the current state vector (0-360 degrees)."""

    id_sensor: Optional[str] = FieldInfo(alias="idSensor", default=None)
    """Unique identifier of the reporting sensor of the object."""

    object: Optional[str] = None
    """Object to which this vector applies."""

    orig_sensor_id: Optional[str] = FieldInfo(alias="origSensorId", default=None)
    """
    Optional identifier provided by the source to indicate the reporting sensor of
    the object. This may be an internal identifier and not necessarily a valid
    sensor ID.
    """

    pos: Optional[List[float]] = None
    """
    Three element array, expressing the cartesian position vector of the target
    object, in kilometers, in the specified referenceFrame. If referenceFrame is
    null then ECEF should be assumed. The array element order is [x, y, z].
    """

    quat: Optional[List[float]] = None
    """
    The quaternion describing the attitude of the spacecraft with respect to the
    reference frame listed in the 'referenceFrame' field. The array element order
    convention is the three vector components, followed by the scalar component.
    """

    reference_frame: Optional[str] = FieldInfo(alias="referenceFrame", default=None)
    """The reference frame of the cartesian vector (ECEF, J2000).

    If the referenceFrame is null it is assumed to be ECEF.
    """

    spd: Optional[float] = None
    """Track object speed, in kilometers/sec."""

    status: Optional[str] = None
    """Status of the vector (e.g. INITIAL, UPDATE)."""

    time_source: Optional[str] = FieldInfo(alias="timeSource", default=None)
    """Source of the time value."""

    type: Optional[str] = None
    """Type of vector represented (e.g. LOS, PREDICTED, STATE)."""

    vector_alt: Optional[float] = FieldInfo(alias="vectorAlt", default=None)
    """Object altitude at epoch, expressed in kilometers above WGS-84 ellipsoid."""

    vector_lat: Optional[float] = FieldInfo(alias="vectorLat", default=None)
    """
    WGS-84 object latitude subpoint at epoch, represented as -90 to 90 degrees
    (negative values south of equator).
    """

    vector_lon: Optional[float] = FieldInfo(alias="vectorLon", default=None)
    """
    WGS-84 object longitude subpoint at epoch, represented as -180 to 180 degrees
    (negative values west of Prime Meridian).
    """

    vel: Optional[List[float]] = None
    """
    Three element array, expressing the cartesian velocity vector of the target
    object, in kilometers/second, in the specified referenceFrame. If referenceFrame
    is null then ECEF should be assumed. The array element order is [x', y', z'].
    """


class MissileTrackListResponse(BaseModel):
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

    ts: datetime
    """
    The receipt time of the data by the processing system, in ISO8601 UTC format
    with microsecond precision.
    """

    id: Optional[str] = None
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    acft_sub_type: Optional[str] = FieldInfo(alias="acftSubType", default=None)
    """Subtype is a finer grain categorization of missile types.

    Examples include but are not limited to SRBM, MRBM, IRBM, LRBM, ICBM, SLBM.

    &nbsp;SRBM - Short-Range Ballistic Missile

    &nbsp;MRBM - Medium-Range Ballistic Missile

    &nbsp;IRBM - Intermediate-Range Ballistic Missile

    &nbsp;LRBM - Long-Range Ballistic Missile

    &nbsp;ICBM - Intercontinental Ballistic Missile

    &nbsp;SLBM - Submarine-Launched Ballistic Missile.
    """

    alert: Optional[str] = None
    """A track may be designated as a non-alert track or an alert track.

    Examples include but are not limited to:

    &nbsp;Non-alert tracks – choose None (Blank).

    &nbsp;Alert tracks – enter the proper alert classification:

    &nbsp;HIT - High Interest Track

    &nbsp;TGT - Target

    &nbsp;SUS - Suspect Carrier

    &nbsp;NSP - Cleared Suspect.
    """

    ang_elev: Optional[float] = FieldInfo(alias="angElev", default=None)
    """Angle of elevation/depression between observer and missile in degrees."""

    aou_rpt_data: Optional[List[float]] = FieldInfo(alias="aouRptData", default=None)
    """Three element array representing an Area of Uncertainty (AoU).

    The array element definitions and units are type specific depending on the
    aouType specified in this record:

    &nbsp;ELLIPSE:

    &nbsp;&nbsp;brg - orientation in degrees of the ellipse

    &nbsp;&nbsp;a1 - semi-major axis in kilometers

    &nbsp;&nbsp;a2 - semi-minor axis in kilometers

    &nbsp;BEARING (BEARING BOX or MTST BEARING BOX):

    &nbsp;&nbsp;brg - orientation in degrees of the bearing box

    &nbsp;&nbsp;a1 - length of bearing box in kilometers

    &nbsp;&nbsp;a2 - half-width of bearing box in kilometers

    &nbsp;OTHER (All other type values):

    &nbsp;&nbsp;brg - line of bearing in degrees true

    &nbsp;&nbsp;a1 - bearing error in degrees

    &nbsp;&nbsp;a2 - estimated range in kilometers.
    """

    aou_rpt_type: Optional[str] = FieldInfo(alias="aouRptType", default=None)
    """The Area of Uncertainty (AoU) type (BEARING, ELLIPSE, OTHER) definition.

    This type defines the elements of the aouEllp array and is required if aouEllp
    is not null. See the aouEllp field definition for specific information.
    """

    az_corr: Optional[float] = FieldInfo(alias="azCorr", default=None)
    """Missile azimuth corridor data."""

    boosting: Optional[bool] = None
    """Indicates whether or not the missile is currently in a state of boosting."""

    burnout_alt: Optional[float] = FieldInfo(alias="burnoutAlt", default=None)
    """Track point burnout altitude relative to WGS-84 ellipsoid, in kilometers."""

    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign currently assigned to the track object."""

    containment: Optional[float] = None
    """
    The percentage of time that the estimated AoU will "cover" the true position of
    the track.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """Application user who created the row in the database."""

    drop_pt_ind: Optional[bool] = FieldInfo(alias="dropPtInd", default=None)
    """The drop-point indicator setting."""

    emg_ind: Optional[bool] = FieldInfo(alias="emgInd", default=None)
    """Indicates whether or not a track has an emergency."""

    env: Optional[Literal["AIR", "LAND", "SPACE", "SURFACE", "SUBSURFACE", "UNKNOWN"]] = None
    """The track environment type (AIR, LAND, SPACE, SUBSURFACE, SURFACE, UNKNOWN):

    AIR: Between sea level and the Kármán line, which has an altitude of 100
    kilometers (62 miles).

    LAND: On the surface of dry land.

    SPACE: Above the Kármán line, which has an altitude of 100 kilometers (62
    miles).

    SURFACE: On the surface of a body of water.

    SUBSURFACE: Below the surface of a body of water.

    UNKNOWN: Environment is not known.
    """

    impact_aou_data: Optional[List[float]] = FieldInfo(alias="impactAouData", default=None)
    """Three element array representing an Area of Uncertainty (AoU).

    The array element definitions and units are type specific depending on the
    aouType specified in this record:

    &nbsp;ELLIPSE:

    &nbsp;&nbsp;brg - orientation in degrees of the ellipse

    &nbsp;&nbsp;a1 - semi-major axis in kilometers

    &nbsp;&nbsp;a2 - semi-minor axis in kilometers

    &nbsp;BEARING (BEARING BOX or MTST BEARING BOX):

    &nbsp;&nbsp;brg - orientation in degrees of the bearing box

    &nbsp;&nbsp;a1 - length of bearing box in kilometers

    &nbsp;&nbsp;a2 - half-width of bearing box in kilometers

    &nbsp;OTHER (All other type values):

    &nbsp;&nbsp;brg - line of bearing in degrees true

    &nbsp;&nbsp;a1 - bearing error in degrees

    &nbsp;&nbsp;a2 - estimated range in kilometers.
    """

    impact_aou_type: Optional[str] = FieldInfo(alias="impactAouType", default=None)
    """The Area of Uncertainty (AoU) type (BEARING, ELLIPSE, OTHER) definition.

    This type defines the elements of the aouEllp array and is required if aouEllp
    is not null. See the aouEllp field definition for specific information.
    """

    impact_lat: Optional[float] = FieldInfo(alias="impactLat", default=None)
    """WGS-84 latitude of the missile object impact point, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    impact_lon: Optional[float] = FieldInfo(alias="impactLon", default=None)
    """WGS-84 longitude of the missile object impact point, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    impact_time: Optional[datetime] = FieldInfo(alias="impactTime", default=None)
    """
    Estimated time of impact timestamp in ISO8601 UTC format with microsecond
    precision.
    """

    info_source: Optional[str] = FieldInfo(alias="infoSource", default=None)
    """Source code for source of information used to detect track."""

    launch_aou_data: Optional[List[float]] = FieldInfo(alias="launchAouData", default=None)
    """Three element array representing an Area of Uncertainty (AoU).

    The array element definitions and units are type specific depending on the
    aouType specified in this record:

    &nbsp;ELLIPSE:

    &nbsp;&nbsp;brg - orientation in degrees of the ellipse

    &nbsp;&nbsp;a1 - semi-major axis in kilometers

    &nbsp;&nbsp;a2 - semi-minor axis in kilometers

    &nbsp;BEARING (BEARING BOX or MTST BEARING BOX):

    &nbsp;&nbsp;brg - orientation in degrees of the bearing box

    &nbsp;&nbsp;a1 - length of bearing box in kilometers

    &nbsp;&nbsp;a2 - half-width of bearing box in kilometers

    &nbsp;OTHER (All other type values):

    &nbsp;&nbsp;brg - line of bearing in degrees true

    &nbsp;&nbsp;a1 - bearing error in degrees

    &nbsp;&nbsp;a2 - estimated range in kilometers.
    """

    launch_aou_type: Optional[str] = FieldInfo(alias="launchAouType", default=None)
    """The Area of Uncertainty (AoU) type (BEARING, ELLIPSE, OTHER) definition.

    This type defines the elements of the aouEllp array and is required if aouEllp
    is not null. See the aouEllp field definition for specific information.
    """

    launch_lat: Optional[float] = FieldInfo(alias="launchLat", default=None)
    """WGS-84 latitude of the missile launch point, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    launch_lon: Optional[float] = FieldInfo(alias="launchLon", default=None)
    """WGS-84 longitude of the missile launch point, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    launch_time: Optional[datetime] = FieldInfo(alias="launchTime", default=None)
    """Missile launch timestamp in ISO8601 UTC format with microsecond precision."""

    lost_trk_ind: Optional[bool] = FieldInfo(alias="lostTrkInd", default=None)
    """Indicates whether or not the missile is considered lost."""

    msg_create_date: Optional[datetime] = FieldInfo(alias="msgCreateDate", default=None)
    """
    The timestamp of the external message from which this request originated, if
    applicable, in ISO8601 UTC format with millisecond precision.
    """

    msg_sub_type: Optional[str] = FieldInfo(alias="msgSubType", default=None)
    """
    The message subtype is a finer grain categorization of message types as many
    messages can contain a variety of data content within the same structure.
    Examples include but are not limited to Initial, Final, Launch, Update, etc.
    Users should consult the appropriate documentation, based on the message type,
    for the definitions of the subtypes that apply to that message.
    """

    msg_type: Optional[str] = FieldInfo(alias="msgType", default=None)
    """The type of external message from which this request originated."""

    msl_status: Optional[str] = FieldInfo(alias="mslStatus", default=None)
    """Missile status enumeration examples include but are not limited to:

    &nbsp;AT LAUNCH

    &nbsp;AT OBSERVATION

    &nbsp;FLYING

    &nbsp;IMPACTED

    &nbsp;LOST

    &nbsp;STALE

    &nbsp;DEBRIS.
    """

    muid_src: Optional[str] = FieldInfo(alias="muidSrc", default=None)
    """Source of the missile-unique identifier (MUID)."""

    muid_src_trk: Optional[str] = FieldInfo(alias="muidSrcTrk", default=None)
    """Track ID for the source of the missile-unique identifier."""

    name: Optional[str] = None
    """Track name."""

    obj_act: Optional[str] = FieldInfo(alias="objAct", default=None)
    """Space activity (examples: RECONNAISSANCE, ANTISPACE WARFARE, TELEVISION).

    The activity in which the track object is engaged. Intended as, but not
    constrained to, MIL-STD-6016 environment dependent activity designations. The
    activity can be reported as either a combination of the code and environment
    (e.g. 65/AIR) or as the descriptive enumeration (e.g. DIVERTING), which are
    equivalent.
    """

    obj_ident: Optional[Literal["ASSUMED FRIEND", "FRIEND", "HOSTILE", "NEUTRAL", "PENDING", "SUSPECT", "UNKNOWN"]] = (
        FieldInfo(alias="objIdent", default=None)
    )
    """
    The estimated identity of the track object (ASSUMED FRIEND, FRIEND, HOSTILE,
    NEUTRAL, PENDING, SUSPECT, UNKNOWN):

    ASSUMED FRIEND: Track assumed to be a friend due to the object characteristics,
    behavior, and/or origin.

    FRIEND: Track object supporting friendly forces and belonging to a declared
    friendly nation or entity.

    HOSTILE: Track object belonging to an opposing nation, party, group, or entity
    deemed to contribute to a threat to friendly forces or their mission due to its
    behavior, characteristics, nationality, or origin.

    NEUTRAL: Track object whose characteristics, behavior, nationality, and/or
    origin indicate that it is neither supporting nor opposing friendly forces or
    their mission.

    PENDING: Track object which has not been evaluated.

    SUSPECT: Track object deemed potentially hostile due to the object
    characteristics, behavior, nationality, and/or origin.

    UNKNOWN: Track object which has been evaluated and does not meet criteria for
    any standard identity.
    """

    obj_plat: Optional[str] = FieldInfo(alias="objPlat", default=None)
    """
    Space Platform field along with the Space Activity field further defines the
    identity of a Space track (examples: SATELLITE, WEAPON, PATROL). The object
    platform type. Intended as, but not constrained to, MIL-STD-6016 environment
    dependent platform type designations. The platform type can be reported as
    either a combination of the code and environment (e.g. 14/LAND) or as the
    descriptive representations (e.g. COMBAT VEHICLE), which are equivalent.
    """

    obj_type: Optional[str] = FieldInfo(alias="objType", default=None)
    """The type of object to which this record refers.

    The object type may be updated in later records based on assessment of
    additional data.
    """

    obj_type_conf: Optional[int] = FieldInfo(alias="objTypeConf", default=None)
    """Confidence of the object type, 0-100."""

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

    parent_track_id: Optional[str] = FieldInfo(alias="parentTrackId", default=None)
    """
    Track ID of the parent track, within the originating system, from which the
    track was developed.
    """

    polar_sing_loc_lat: Optional[float] = FieldInfo(alias="polarSingLocLat", default=None)
    """Azimuth corridor reference point latitude."""

    polar_sing_loc_lon: Optional[float] = FieldInfo(alias="polarSingLocLon", default=None)
    """Azimuth corridor reference point longitude."""

    sen_mode: Optional[str] = FieldInfo(alias="senMode", default=None)
    """
    Last report type received from the sensor (for example, OBSBO = observation
    burnout).
    """

    space_amp: Optional[str] = FieldInfo(alias="spaceAmp", default=None)
    """
    Space amplification indicates additional information on the space environment
    being reported (examples: NUCLEAR WARHEAD, FUEL-AIR EXPLOSIVE WARHEAD, DEBRIS).
    """

    space_amp_conf: Optional[int] = FieldInfo(alias="spaceAmpConf", default=None)
    """Confidence level of the amplifying characteristics. Values range from 0 to 6."""

    space_spec_type: Optional[str] = FieldInfo(alias="spaceSpecType", default=None)
    """Specific type of point or track with an environment of space."""

    track_id: Optional[str] = FieldInfo(alias="trackId", default=None)
    """Track ID within the originating system."""

    trk_conf: Optional[float] = FieldInfo(alias="trkConf", default=None)
    """
    Overall track confidence estimate (not standardized, but typically a value
    between 0 and 1, with 0 indicating lowest confidence).
    """

    trk_qual: Optional[int] = FieldInfo(alias="trkQual", default=None)
    """Track Quality is reported as an integer from 0-15.

    Track Quality specifies the reliability of the positional information of a
    reported track, with higher values indicating higher track quality; i.e., lower
    errors in reported position.
    """

    vectors: Optional[List[Vector]] = None
    """Array of MissileTrackVector objects.

    Missile track vectors are cartesian vectors of position, velocity, and
    acceleration that, together with their time, 'epoch', uniquely determine the
    trajectory of the missile. ECEF is the preferred coordinate frame but in some
    cases data may be in another frame as specified by 'referenceFrame', depending
    on the provider.
    """
