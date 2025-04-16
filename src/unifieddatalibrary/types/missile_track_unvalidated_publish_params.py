# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MissileTrackUnvalidatedPublishParams", "Body", "BodyVector"]


class MissileTrackUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyVector(TypedDict, total=False):
    epoch: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Vector timestamp in ISO8601 UTC format, with microsecond precision."""

    accel: Iterable[float]
    """
    Three element array, expressing the cartesian acceleration vector of the target
    object, in kilometers/second^2, in the specified referenceFrame. If
    referenceFrame is null then ECEF should be assumed. The array element order is
    [x'', y'', z''].
    """

    confidence: int
    """Confidence of the vector, 0-100."""

    course: float
    """Track object course, in degrees clockwise from true north."""

    cov: Iterable[float]
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

    cov_reference_frame: Annotated[str, PropertyInfo(alias="covReferenceFrame")]
    """The reference frame of the covariance elements (ECEF, J2000, UVW).

    If the referenceFrame is null it is assumed to be UVW.
    """

    flight_az: Annotated[float, PropertyInfo(alias="flightAz")]
    """The flight azimuth associated with the current state vector (0-360 degrees)."""

    id_sensor: Annotated[str, PropertyInfo(alias="idSensor")]
    """Unique identifier of the reporting sensor of the object."""

    object: str
    """Object to which this vector applies."""

    orig_sensor_id: Annotated[str, PropertyInfo(alias="origSensorId")]
    """
    Optional identifier provided by the source to indicate the reporting sensor of
    the object. This may be an internal identifier and not necessarily a valid
    sensor ID.
    """

    pos: Iterable[float]
    """
    Three element array, expressing the cartesian position vector of the target
    object, in kilometers, in the specified referenceFrame. If referenceFrame is
    null then ECEF should be assumed. The array element order is [x, y, z].
    """

    quat: Iterable[float]
    """
    The quaternion describing the attitude of the spacecraft with respect to the
    reference frame listed in the 'referenceFrame' field. The array element order
    convention is the three vector components, followed by the scalar component.
    """

    reference_frame: Annotated[str, PropertyInfo(alias="referenceFrame")]
    """The reference frame of the cartesian vector (ECEF, J2000).

    If the referenceFrame is null it is assumed to be ECEF.
    """

    spd: float
    """Track object speed, in kilometers/sec."""

    status: str
    """Status of the vector (e.g. INITIAL, UPDATE)."""

    time_source: Annotated[str, PropertyInfo(alias="timeSource")]
    """Source of the time value."""

    type: str
    """Type of vector represented (e.g. LOS, PREDICTED, STATE)."""

    vector_alt: Annotated[float, PropertyInfo(alias="vectorAlt")]
    """Object altitude at epoch, expressed in kilometers above WGS-84 ellipsoid."""

    vector_lat: Annotated[float, PropertyInfo(alias="vectorLat")]
    """
    WGS-84 object latitude subpoint at epoch, represented as -90 to 90 degrees
    (negative values south of equator).
    """

    vector_lon: Annotated[float, PropertyInfo(alias="vectorLon")]
    """
    WGS-84 object longitude subpoint at epoch, represented as -180 to 180 degrees
    (negative values west of Prime Meridian).
    """

    vel: Iterable[float]
    """
    Three element array, expressing the cartesian velocity vector of the target
    object, in kilometers/second, in the specified referenceFrame. If referenceFrame
    is null then ECEF should be assumed. The array element order is [x', y', z'].
    """


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

    ts: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The receipt time of the data by the processing system, in ISO8601 UTC format
    with microsecond precision.
    """

    id: str
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    acft_sub_type: Annotated[str, PropertyInfo(alias="acftSubType")]
    """Subtype is a finer grain categorization of missile types.

    Examples include but are not limited to SRBM, MRBM, IRBM, LRBM, ICBM, SLBM.

    &nbsp;SRBM - Short-Range Ballistic Missile

    &nbsp;MRBM - Medium-Range Ballistic Missile

    &nbsp;IRBM - Intermediate-Range Ballistic Missile

    &nbsp;LRBM - Long-Range Ballistic Missile

    &nbsp;ICBM - Intercontinental Ballistic Missile

    &nbsp;SLBM - Submarine-Launched Ballistic Missile.
    """

    alert: str
    """A track may be designated as a non-alert track or an alert track.

    Examples include but are not limited to:

    &nbsp;Non-alert tracks – choose None (Blank).

    &nbsp;Alert tracks – enter the proper alert classification:

    &nbsp;HIT - High Interest Track

    &nbsp;TGT - Target

    &nbsp;SUS - Suspect Carrier

    &nbsp;NSP - Cleared Suspect.
    """

    ang_elev: Annotated[float, PropertyInfo(alias="angElev")]
    """Angle of elevation/depression between observer and missile in degrees."""

    aou_rpt_data: Annotated[Iterable[float], PropertyInfo(alias="aouRptData")]
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

    aou_rpt_type: Annotated[str, PropertyInfo(alias="aouRptType")]
    """The Area of Uncertainty (AoU) type (BEARING, ELLIPSE, OTHER) definition.

    This type defines the elements of the aouEllp array and is required if aouEllp
    is not null. See the aouEllp field definition for specific information.
    """

    az_corr: Annotated[float, PropertyInfo(alias="azCorr")]
    """Missile azimuth corridor data."""

    boosting: bool
    """Indicates whether or not the missile is currently in a state of boosting."""

    burnout_alt: Annotated[float, PropertyInfo(alias="burnoutAlt")]
    """Track point burnout altitude relative to WGS-84 ellipsoid, in kilometers."""

    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """The call sign currently assigned to the track object."""

    containment: float
    """
    The percentage of time that the estimated AoU will "cover" the true position of
    the track.
    """

    drop_pt_ind: Annotated[bool, PropertyInfo(alias="dropPtInd")]
    """The drop-point indicator setting."""

    emg_ind: Annotated[bool, PropertyInfo(alias="emgInd")]
    """Indicates whether or not a track has an emergency."""

    env: Literal["AIR", "LAND", "SPACE", "SURFACE", "SUBSURFACE", "UNKNOWN"]
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

    impact_aou_data: Annotated[Iterable[float], PropertyInfo(alias="impactAouData")]
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

    impact_aou_type: Annotated[str, PropertyInfo(alias="impactAouType")]
    """The Area of Uncertainty (AoU) type (BEARING, ELLIPSE, OTHER) definition.

    This type defines the elements of the aouEllp array and is required if aouEllp
    is not null. See the aouEllp field definition for specific information.
    """

    impact_lat: Annotated[float, PropertyInfo(alias="impactLat")]
    """WGS-84 latitude of the missile object impact point, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    impact_lon: Annotated[float, PropertyInfo(alias="impactLon")]
    """WGS-84 longitude of the missile object impact point, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    impact_time: Annotated[Union[str, datetime], PropertyInfo(alias="impactTime", format="iso8601")]
    """
    Estimated time of impact timestamp in ISO8601 UTC format with microsecond
    precision.
    """

    info_source: Annotated[str, PropertyInfo(alias="infoSource")]
    """Source code for source of information used to detect track."""

    launch_aou_data: Annotated[Iterable[float], PropertyInfo(alias="launchAouData")]
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

    launch_aou_type: Annotated[str, PropertyInfo(alias="launchAouType")]
    """The Area of Uncertainty (AoU) type (BEARING, ELLIPSE, OTHER) definition.

    This type defines the elements of the aouEllp array and is required if aouEllp
    is not null. See the aouEllp field definition for specific information.
    """

    launch_lat: Annotated[float, PropertyInfo(alias="launchLat")]
    """WGS-84 latitude of the missile launch point, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    launch_lon: Annotated[float, PropertyInfo(alias="launchLon")]
    """WGS-84 longitude of the missile launch point, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    launch_time: Annotated[Union[str, datetime], PropertyInfo(alias="launchTime", format="iso8601")]
    """Missile launch timestamp in ISO8601 UTC format with microsecond precision."""

    lost_trk_ind: Annotated[bool, PropertyInfo(alias="lostTrkInd")]
    """Indicates whether or not the missile is considered lost."""

    msg_create_date: Annotated[Union[str, datetime], PropertyInfo(alias="msgCreateDate", format="iso8601")]
    """
    The timestamp of the external message from which this request originated, if
    applicable, in ISO8601 UTC format with millisecond precision.
    """

    msg_sub_type: Annotated[str, PropertyInfo(alias="msgSubType")]
    """
    The message subtype is a finer grain categorization of message types as many
    messages can contain a variety of data content within the same structure.
    Examples include but are not limited to Initial, Final, Launch, Update, etc.
    Users should consult the appropriate documentation, based on the message type,
    for the definitions of the subtypes that apply to that message.
    """

    msg_type: Annotated[str, PropertyInfo(alias="msgType")]
    """The type of external message from which this request originated."""

    msl_status: Annotated[str, PropertyInfo(alias="mslStatus")]
    """Missile status enumeration examples include but are not limited to:

    &nbsp;AT LAUNCH

    &nbsp;AT OBSERVATION

    &nbsp;FLYING

    &nbsp;IMPACTED

    &nbsp;LOST

    &nbsp;STALE

    &nbsp;DEBRIS.
    """

    muid_src: Annotated[str, PropertyInfo(alias="muidSrc")]
    """Source of the missile-unique identifier (MUID)."""

    muid_src_trk: Annotated[str, PropertyInfo(alias="muidSrcTrk")]
    """Track ID for the source of the missile-unique identifier."""

    name: str
    """Track name."""

    obj_act: Annotated[str, PropertyInfo(alias="objAct")]
    """Space activity (examples: RECONNAISSANCE, ANTISPACE WARFARE, TELEVISION).

    The activity in which the track object is engaged. Intended as, but not
    constrained to, MIL-STD-6016 environment dependent activity designations. The
    activity can be reported as either a combination of the code and environment
    (e.g. 65/AIR) or as the descriptive enumeration (e.g. DIVERTING), which are
    equivalent.
    """

    obj_ident: Annotated[
        Literal["ASSUMED FRIEND", "FRIEND", "HOSTILE", "NEUTRAL", "PENDING", "SUSPECT", "UNKNOWN"],
        PropertyInfo(alias="objIdent"),
    ]
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

    obj_plat: Annotated[str, PropertyInfo(alias="objPlat")]
    """
    Space Platform field along with the Space Activity field further defines the
    identity of a Space track (examples: SATELLITE, WEAPON, PATROL). The object
    platform type. Intended as, but not constrained to, MIL-STD-6016 environment
    dependent platform type designations. The platform type can be reported as
    either a combination of the code and environment (e.g. 14/LAND) or as the
    descriptive representations (e.g. COMBAT VEHICLE), which are equivalent.
    """

    obj_type: Annotated[str, PropertyInfo(alias="objType")]
    """The type of object to which this record refers.

    The object type may be updated in later records based on assessment of
    additional data.
    """

    obj_type_conf: Annotated[int, PropertyInfo(alias="objTypeConf")]
    """Confidence of the object type, 0-100."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    parent_track_id: Annotated[str, PropertyInfo(alias="parentTrackId")]
    """
    Track ID of the parent track, within the originating system, from which the
    track was developed.
    """

    polar_sing_loc_lat: Annotated[float, PropertyInfo(alias="polarSingLocLat")]
    """Azimuth corridor reference point latitude."""

    polar_sing_loc_lon: Annotated[float, PropertyInfo(alias="polarSingLocLon")]
    """Azimuth corridor reference point longitude."""

    sen_mode: Annotated[str, PropertyInfo(alias="senMode")]
    """
    Last report type received from the sensor (for example, OBSBO = observation
    burnout).
    """

    space_amp: Annotated[str, PropertyInfo(alias="spaceAmp")]
    """
    Space amplification indicates additional information on the space environment
    being reported (examples: NUCLEAR WARHEAD, FUEL-AIR EXPLOSIVE WARHEAD, DEBRIS).
    """

    space_amp_conf: Annotated[int, PropertyInfo(alias="spaceAmpConf")]
    """Confidence level of the amplifying characteristics. Values range from 0 to 6."""

    space_spec_type: Annotated[str, PropertyInfo(alias="spaceSpecType")]
    """Specific type of point or track with an environment of space."""

    track_id: Annotated[str, PropertyInfo(alias="trackId")]
    """Track ID within the originating system."""

    trk_conf: Annotated[float, PropertyInfo(alias="trkConf")]
    """
    Overall track confidence estimate (not standardized, but typically a value
    between 0 and 1, with 0 indicating lowest confidence).
    """

    trk_qual: Annotated[int, PropertyInfo(alias="trkQual")]
    """Track Quality is reported as an integer from 0-15.

    Track Quality specifies the reliability of the positional information of a
    reported track, with higher values indicating higher track quality; i.e., lower
    errors in reported position.
    """

    vectors: Iterable[BodyVector]
    """Array of MissileTrackVector objects.

    Missile track vectors are cartesian vectors of position, velocity, and
    acceleration that, together with their time, 'epoch', uniquely determine the
    trajectory of the missile. ECEF is the preferred coordinate frame but in some
    cases data may be in another frame as specified by 'referenceFrame', depending
    on the provider.
    """
