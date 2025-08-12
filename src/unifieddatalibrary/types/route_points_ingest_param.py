# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoutePointsIngestParam"]


class RoutePointsIngestParam(TypedDict, total=False):
    alt_country_code: Annotated[str, PropertyInfo(alias="altCountryCode")]
    """
    Specifies an alternate country code if the data provider code is not part of an
    official NAVAID Country Code standard such as ISO-3166 or FIPS. This field will
    be set to the value provided by the source and should be used for all Queries
    specifying a Country Code.
    """

    country_code: Annotated[str, PropertyInfo(alias="countryCode")]
    """
    The DoD Standard Country Code designator for the country where the route point
    resides. This field should be set to "OTHR" if the source value does not match a
    UDL country code value (ISO-3166-ALPHA-2).
    """

    dafif_pt: Annotated[bool, PropertyInfo(alias="dafifPt")]
    """
    Flag indicating this is a Digital Aeronautical Flight Information File (DAFIF)
    point.
    """

    mag_dec: Annotated[float, PropertyInfo(alias="magDec")]
    """
    The magnetic declination/variation of the route point location from true north,
    in degrees. Positive values east of true north and negative values west of true
    north.
    """

    navaid: str
    """Navigational Aid (NAVAID) identification code."""

    navaid_length: Annotated[float, PropertyInfo(alias="navaidLength")]
    """The length of the course from the Navigational Aid (NAVAID) in nautical miles."""

    navaid_type: Annotated[str, PropertyInfo(alias="navaidType")]
    """The NAVAID type of this route point (ex. VOR, VORTAC, TACAN, etc.)."""

    pt_lat: Annotated[float, PropertyInfo(alias="ptLat")]
    """WGS84 latitude of the point location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    pt_lon: Annotated[float, PropertyInfo(alias="ptLon")]
    """WGS84 longitude of the point location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    pt_sequence_id: Annotated[int, PropertyInfo(alias="ptSequenceId")]
    """Sequencing field for the track route.

    This is the identifier representing the sequence of waypoints associated to the
    track route.
    """

    pt_type_code: Annotated[str, PropertyInfo(alias="ptTypeCode")]
    """Code representation of the point within the track route (ex.

    EP, EX, CP, IP, etc.).
    """

    pt_type_name: Annotated[str, PropertyInfo(alias="ptTypeName")]
    """The name that represents the point within the track route (ex.

    ENTRY POINT, EXIT POINT, CONTROL POINT, INITIAL POINT, etc.).
    """

    waypoint_name: Annotated[str, PropertyInfo(alias="waypointName")]
    """Name of a waypoint which identifies the location of the point."""
