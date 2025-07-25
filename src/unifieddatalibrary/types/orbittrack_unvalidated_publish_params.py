# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrbittrackUnvalidatedPublishParams", "Body", "BodyTrackSensor"]


class OrbittrackUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyTrackSensor(TypedDict, total=False):
    az: Required[float]
    """The observing sensor azimuth angle, in degrees and topocentric frame."""

    range: Required[float]
    """The track object range from the observing sensor, in kilometers."""

    min_range_limit: Annotated[float, PropertyInfo(alias="minRangeLimit")]
    """Minimum range measurement capability of the sensor, in kilometers."""

    mission_number: Annotated[str, PropertyInfo(alias="missionNumber")]
    """The mission number which produced this track observation."""

    sensor_fov_type: Annotated[
        Literal["BUTTERFLY", "CONE ANGULAR", "CONE DISTANCE", "HORIZON TO HORIZON", "UNKNOWN"],
        PropertyInfo(alias="sensorFOVType"),
    ]
    """
    The field of view (FOV) type (Butterfly, Cone Angular, Cone Distance, Horizon to
    Horizon, Unknown) employed by the sensor observing this object.
    """

    sensor_name: Annotated[str, PropertyInfo(alias="sensorName")]
    """Unique name of this sensor."""

    sensor_number: Annotated[int, PropertyInfo(alias="sensorNumber")]
    """Number assigned to this sensor.

    Since there is no authoritative numbering scheme, these numbers sometimes
    collide across sensors (especially commercial sensors). It is therefore not a
    unique identifier.
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

    lat: Required[float]
    """WGS-84 latitude of the track object subpoint, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    lon: Required[float]
    """WGS-84 longitude of the track object subpoint, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    source: Required[str]
    """Source of the data."""

    ts: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Track timestamp in ISO8601 UTC format, with microsecond precision."""

    id: str
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    alt: float
    """Track point altitude relative to WGS-84 ellipsoid, in meters."""

    amplification: str
    """Free-form remarks entered for the satellite."""

    ang_elev: Annotated[float, PropertyInfo(alias="angElev")]
    """
    The angle formed between the line of sight of the observer and the horizon at
    track timestamp, in degrees. The angular range is -90 to 90, with negative
    values representing angle of depression.
    """

    aou_data: Annotated[Iterable[float], PropertyInfo(alias="aouData")]
    """Three element array representing an Area of Uncertainty (AoU).

    The array element definitions and units are type specific depending on the
    aouType specified in this record:

    ELLIPSE:

    brg - orientation in degrees of the ellipse

    a1 - semi-major axis in meters

    a2 - semi-minor axis in meters

    BEARING (BEARING BOX or MTST BEARING BOX):

    brg - orientation in degrees of the bearing box

    a1 - length of bearing box in meters

    a2 - half-width of bearing box in meters

    OTHER (All other type values):

    brg - line of bearing in degrees true

    a1 - bearing error in degrees

    a2 - estimated range in meters.
    """

    aou_type: Annotated[str, PropertyInfo(alias="aouType")]
    """The Area of Uncertainty (AoU) type (BEARING, ELLIPSE, OTHER) definition.

    This type defines the elements of the aouData array and is required if aouData
    is not null. See the aouData field definition for specific information.
    """

    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """International radio call sign assigned to the track.

    This is an 8-character alphanumeric code.
    """

    charlie_line: Annotated[str, PropertyInfo(alias="charlieLine")]
    """One-line Charlie elements set."""

    ch_x_ref: Annotated[str, PropertyInfo(alias="chXRef")]
    """
    The cross-reference code of the channel on which this track report was received,
    if the report came over a comms channel.
    """

    cntnmnt: float
    """The Area Of Uncertainty (AOU) percentage (0 - 100) containment value.

    The percentage of time (90%) that the estimated area of uncertainty will cover
    the true position of the track object.
    """

    country_code: Annotated[str, PropertyInfo(alias="countryCode")]
    """The country code.

    This value is typically the ISO 3166 Alpha-2 two-character country code, however
    it can also represent various consortiums that do not appear in the ISO
    document. The code must correspond to an existing country in the UDL’s country
    API. Call udl/country/{code} to get any associated FIPS code, ISO Alpha-3 code,
    or alternate code values that exist for the specified country code.
    """

    decay: float
    """Predicted change in Mean Motion (velocity) in radians/herg^2.

    herg is a unit of time measure equal to 806.8120769 seconds, and is the orbital
    period of an imaginary satellite rotating about the Earth at zero altitude.
    """

    dummy: bool
    """Flag indicating that this track represents a dummy object or group.

    Identifies offensive or defensive units, equipment and/or installations intended
    to draw the enemy's attention away from the area of the main attack. Based on
    MIL-STD-2525 symbology definitions.
    """

    feint: bool
    """Flag indicating that this track represents a feint object or group.

    Identifies offensive or defensive units, equipment and/or installations intended
    to draw the enemy's attention away from the area of the main attack. Based on
    MIL-STD-2525 symbology definitions.
    """

    hq: bool
    """Flag indicating that this track represents a headquarters object.

    Based on MIL-STD-2525 symbology definitions.
    """

    id_elset: Annotated[str, PropertyInfo(alias="idElset")]
    """Unique identifier of the Elset associated with this object."""

    ident_amp: Annotated[str, PropertyInfo(alias="identAmp")]
    """
    Additional track object identity/status information, typically used for EXERCISE
    identity amplification (FAKER, JOKER, KILO, TRAVELLER, ZOMBIE):

    FAKER: Friendly track, object, or entity acting as an exercise hostile.

    JOKER: Friendly track, object, or entity acting as an exercise suspect.

    KILO: Friendly high-value object.

    TRAVELLER: Suspect land or surface track following a recognized traffic route.

    ZOMBIE: Suspect track, object, or entity of special interest.
    """

    id_on_orbit: Annotated[str, PropertyInfo(alias="idOnOrbit")]
    """Unique identifier of the target on-orbit object, if correlated."""

    iff: str
    """A text amplifier displaying IFF/SIF/AIS Identification modes and codes."""

    installation: bool
    """Flag indicating that this track represents an installation.

    Based on MIL-STD-2525 symbology definitions.
    """

    object_type: Annotated[
        Literal["DEBRIS", "MANNED", "PAYLOAD", "PLATFORM", "ROCKET BODY", "UNKNOWN"], PropertyInfo(alias="objectType")
    ]
    """
    The on-orbit category assigned to this track object (DEBRIS, MANNED, PAYLOAD,
    PLATFORM, ROCKET BODY, UNKNOWN).
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

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_object_id: Annotated[str, PropertyInfo(alias="origObjectId")]
    """
    Optional identifier provided by observation source to indicate the target
    on-orbit object of this track. This may be an internal identifier and not
    necessarily a valid satellite number.
    """

    rdf_rf: Annotated[float, PropertyInfo(alias="rdfRF")]
    """Radio frequency of the track, measured in megahertz (MHz)."""

    reduced: bool
    """Flag indicating that this track represents a reduced object or group.

    Based on MIL-STD-2525 symbology definitions.
    """

    reinforced: bool
    """Flag indicating that this track represents a reinforced object or group.

    Based on MIL-STD-2525 symbology definitions.
    """

    rpt_num: Annotated[str, PropertyInfo(alias="rptNum")]
    """Report number received from the reporting source for this track."""

    sat_no: Annotated[int, PropertyInfo(alias="satNo")]
    """Satellite/catalog number of the target on-orbit object."""

    sat_status: Annotated[str, PropertyInfo(alias="satStatus")]
    """Status of the satellite."""

    spd: float
    """Track object speed, in km/sec."""

    task_force: Annotated[bool, PropertyInfo(alias="taskForce")]
    """Flag indicating that this track represents a task force.

    Based on MIL-STD-2525 symbology definitions.
    """

    track_sensors: Annotated[Iterable[BodyTrackSensor], PropertyInfo(alias="trackSensors")]
    """TrackSensor Collection."""

    trk_id: Annotated[str, PropertyInfo(alias="trkId")]
    """
    UUID identifying the track, which should remain the same on subsequent tracks of
    the same object.
    """

    veh_type: Annotated[str, PropertyInfo(alias="vehType")]
    """The type of vehicle with which the device is associated.

    Based on MIL-STD-2525 symbology definitions.
    """

    xref: str
    """Source cross-reference code for the command that originated the track report."""
