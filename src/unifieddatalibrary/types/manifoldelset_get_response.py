# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ManifoldelsetGetResponse"]


class ManifoldelsetGetResponse(BaseModel):
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

    epoch: datetime
    """Elset epoch time in ISO 8601 UTC format, with microsecond precision."""

    id_manifold: str = FieldInfo(alias="idManifold")
    """Identifier of the parent Manifold record."""

    source: str
    """Source of the data."""

    tmp_sat_no: int = FieldInfo(alias="tmpSatNo")
    """A placeholder satellite number and not a true NORAD catalog number."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    apogee: Optional[float] = None
    """The Orbit point furthest from the center of the earth in kilometers."""

    arg_of_perigee: Optional[float] = FieldInfo(alias="argOfPerigee", default=None)
    """
    The argument of perigee is the angle in degrees formed between the perigee and
    the ascending node. If the perigee would occur at the ascending node, the
    argument of perigee would be 0.
    """

    b_star: Optional[float] = FieldInfo(alias="bStar", default=None)
    """
    The drag term for SGP4 orbital model, used for calculating decay constants for
    altitude, eccentricity etc, measured in inverse earth radii.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    eccentricity: Optional[float] = None
    """
    The orbital eccentricity of an astronomical object is a parameter that
    determines the amount by which its orbit around another body deviates from a
    perfect circle. A value of 0 is a circular orbit, values between 0 and 1 form an
    elliptic orbit, 1 is a parabolic escape orbit, and greater than 1 is a
    hyperbolic escape orbit.
    """

    inclination: Optional[float] = None
    """
    The angle between the equator and the orbit when looking from the center of the
    Earth. If the orbit went exactly around the equator from left to right, then the
    inclination would be 0. The inclination ranges from 0 to 180 degrees.
    """

    line1: Optional[str] = None
    """
    Read only derived/generated line1 of a legacy TLE (two line element set) format,
    ignored on create/edit operations.
    """

    line2: Optional[str] = None
    """
    Read only derived/generated line2 of a legacy TLE (two line element set) format,
    ignored on create/edit operations.
    """

    mean_anomaly: Optional[float] = FieldInfo(alias="meanAnomaly", default=None)
    """Where the satellite is in its orbital path.

    The mean anomaly ranges from 0 to 360 degrees. The mean anomaly is referenced to
    the perigee. If the satellite were at the perigee, the mean anomaly would be 0.
    """

    mean_motion: Optional[float] = FieldInfo(alias="meanMotion", default=None)
    """
    The constant angular speed required for the body to complete one circular orbit
    in the same amount of time as the actual elliptical orbit with variable speed.
    Measured in revolutions per day.
    """

    mean_motion_d_dot: Optional[float] = FieldInfo(alias="meanMotionDDot", default=None)
    """2nd derivative of the mean motion with respect to time.

    Units are revolutions per day cubed.
    """

    mean_motion_dot: Optional[float] = FieldInfo(alias="meanMotionDot", default=None)
    """1st derivative of the mean motion with respect to time.

    Units are revolutions per day squared.
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

    perigee: Optional[float] = None
    """The orbit point nearest to the center of the earth in kilometers."""

    period: Optional[float] = None
    """Period of the orbit equal to inverse of mean motion."""

    raan: Optional[float] = None
    """
    Right ascension of the ascending node, or RAAN is the angle as measured in
    degrees eastwards (or, as seen from the north, counterclockwise) from the First
    Point of Aries to the ascending node, which is where the orbit crosses the
    equator when traveling north.
    """

    rev_no: Optional[int] = FieldInfo(alias="revNo", default=None)
    """The current revolution number.

    The value is incremented when a satellite crosses the equator on an ascending
    pass.
    """

    semi_major_axis: Optional[float] = FieldInfo(alias="semiMajorAxis", default=None)
    """The sum of the periapsis and apoapsis distances divided by two.

    For circular orbits, the semimajor axis is the distance between the centers of
    the bodies, not the distance of the bodies from the center of mass.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    Read-only time the row was updated in the database, set automatically by the
    system on update.
    """

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who last updated the row in the database, set by the system
    automatically and ignored on create/edit operations.
    """
