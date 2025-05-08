# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TrackRouteListResponse", "AltitudeBlock", "Poc", "RoutePoint"]


class AltitudeBlock(BaseModel):
    altitude_sequence_id: Optional[str] = FieldInfo(alias="altitudeSequenceId", default=None)
    """Sequencing field for the altitude block."""

    lower_altitude: Optional[float] = FieldInfo(alias="lowerAltitude", default=None)
    """Lowest altitude of the track route altitude block above mean sea level in feet."""

    upper_altitude: Optional[float] = FieldInfo(alias="upperAltitude", default=None)
    """
    Highest altitude of the track route altitude block above mean sea level in feet.
    """


class Poc(BaseModel):
    office: Optional[str] = None
    """Office name for which the contact belongs."""

    phone: Optional[str] = None
    """Phone number of the contact."""

    poc_name: Optional[str] = FieldInfo(alias="pocName", default=None)
    """The name of the contact."""

    poc_org: Optional[str] = FieldInfo(alias="pocOrg", default=None)
    """Organization name for which the contact belongs."""

    poc_sequence_id: Optional[int] = FieldInfo(alias="pocSequenceId", default=None)
    """Sequencing field for point of contact."""

    poc_type_name: Optional[str] = FieldInfo(alias="pocTypeName", default=None)
    """
    A code or name that represents the contact's role in association to the track
    route (ex. Originator, Scheduler, Maintainer, etc.).
    """

    rank: Optional[str] = None
    """The rank of contact."""

    remark: Optional[str] = None
    """Text of the remark."""

    username: Optional[str] = None
    """The username of the contact."""


class RoutePoint(BaseModel):
    alt_country_code: Optional[str] = FieldInfo(alias="altCountryCode", default=None)
    """
    Specifies an alternate country code if the data provider code is not part of an
    official NAVAID Country Code standard such as ISO-3166 or FIPS. This field will
    be set to the value provided by the source and should be used for all Queries
    specifying a Country Code.
    """

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """
    The DoD Standard Country Code designator for the country where the route point
    resides. This field should be set to "OTHR" if the source value does not match a
    UDL country code value (ISO-3166-ALPHA-2).
    """

    dafif_pt: Optional[bool] = FieldInfo(alias="dafifPt", default=None)
    """
    Flag indicating this is a Digital Aeronautical Flight Information File (DAFIF)
    point.
    """

    mag_dec: Optional[float] = FieldInfo(alias="magDec", default=None)
    """
    The magnetic declination/variation of the route point location from true north,
    in degrees. Positive values east of true north and negative values west of true
    north.
    """

    navaid: Optional[str] = None
    """Navigational Aid (NAVAID) identification code."""

    navaid_length: Optional[float] = FieldInfo(alias="navaidLength", default=None)
    """The length of the course from the Navigational Aid (NAVAID) in nautical miles."""

    navaid_type: Optional[str] = FieldInfo(alias="navaidType", default=None)
    """The NAVAID type of this route point (ex. VOR, VORTAC, TACAN, etc.)."""

    pt_lat: Optional[float] = FieldInfo(alias="ptLat", default=None)
    """WGS84 latitude of the point location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    pt_lon: Optional[float] = FieldInfo(alias="ptLon", default=None)
    """WGS84 longitude of the point location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    pt_sequence_id: Optional[int] = FieldInfo(alias="ptSequenceId", default=None)
    """Sequencing field for the track route.

    This is the identifier representing the sequence of waypoints associated to the
    track route.
    """

    pt_type_code: Optional[str] = FieldInfo(alias="ptTypeCode", default=None)
    """Code representation of the point within the track route (ex.

    EP, EX, CP, IP, etc.).
    """

    pt_type_name: Optional[str] = FieldInfo(alias="ptTypeName", default=None)
    """The name that represents the point within the track route (ex.

    ENTRY POINT, EXIT POINT, CONTROL POINT, INITIAL POINT, etc.).
    """

    waypoint_name: Optional[str] = FieldInfo(alias="waypointName", default=None)
    """Name of a waypoint which identifies the location of the point."""


class TrackRouteListResponse(BaseModel):
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

    last_update_date: datetime = FieldInfo(alias="lastUpdateDate")
    """
    The last updated date of the track route in ISO 8601 UTC format with millisecond
    precision.
    """

    source: str
    """Source of the data."""

    type: str
    """The track route type represented by this record (ex. AIR REFUELING)."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    altitude_blocks: Optional[List[AltitudeBlock]] = FieldInfo(alias="altitudeBlocks", default=None)
    """Minimum and maximum altitude bounds for the track."""

    apn_setting: Optional[str] = FieldInfo(alias="apnSetting", default=None)
    """The APN radar code sent and received by the aircraft for identification."""

    apx_beacon_code: Optional[str] = FieldInfo(alias="apxBeaconCode", default=None)
    """The APX radar code sent and received by the aircraft for identification."""

    artcc_message: Optional[str] = FieldInfo(alias="artccMessage", default=None)
    """Air Refueling Track Control Center message."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    creating_org: Optional[str] = FieldInfo(alias="creatingOrg", default=None)
    """The name of the creating organization of the track route."""

    direction: Optional[str] = None
    """The principal compass direction (cardinal or ordinal) of the track route."""

    effective_date: Optional[datetime] = FieldInfo(alias="effectiveDate", default=None)
    """
    The date which the DAFIF track was last updated/validated in ISO 8601 UTC format
    with millisecond precision.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Optional air refueling track ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    last_used_date: Optional[datetime] = FieldInfo(alias="lastUsedDate", default=None)
    """
    Used to show last time the track route was added to an itinerary in ISO 8601 UTC
    format with millisecond precision.
    """

    location_track_id: Optional[str] = FieldInfo(alias="locationTrackId", default=None)
    """Track location ID."""

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

    poc: Optional[List[Poc]] = None
    """Point of contacts for scheduling or modifying the route."""

    pri_freq: Optional[float] = FieldInfo(alias="priFreq", default=None)
    """The primary UHF radio frequency used for the track route in megahertz."""

    receiver_tanker_ch_code: Optional[str] = FieldInfo(alias="receiverTankerCHCode", default=None)
    """The receiver tanker channel identifer for air refueling tracks."""

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)
    """
    Region code indicating where the track resides as determined by the data source.
    """

    region_name: Optional[str] = FieldInfo(alias="regionName", default=None)
    """Region where the track resides."""

    review_date: Optional[datetime] = FieldInfo(alias="reviewDate", default=None)
    """
    Date the track needs to be reviewed for accuracy or deletion in ISO 8601 UTC
    format with millisecond precision.
    """

    route_points: Optional[List[RoutePoint]] = FieldInfo(alias="routePoints", default=None)
    """Points identified within the route."""

    scheduler_org_name: Optional[str] = FieldInfo(alias="schedulerOrgName", default=None)
    """Point of contact for the air refueling track route scheduler."""

    scheduler_org_unit: Optional[str] = FieldInfo(alias="schedulerOrgUnit", default=None)
    """The unit responsible for scheduling the track route."""

    sec_freq: Optional[float] = FieldInfo(alias="secFreq", default=None)
    """The secondary UHF radio frequency used for the track route in megahertz."""

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)
    """Abbreviated name of the track."""

    sic: Optional[str] = None
    """Standard Indicator Code of the air refueling track."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    track_id: Optional[str] = FieldInfo(alias="trackId", default=None)
    """Identifier of the track."""

    track_name: Optional[str] = FieldInfo(alias="trackName", default=None)
    """Name of the track."""

    type_code: Optional[str] = FieldInfo(alias="typeCode", default=None)
    """Type of process used by AMC to schedule an air refueling event.

    Possible values are A (Matched Long Range), F (Matched AMC Short Notice), N
    (Unmatched Theater Operation Short Notice (Theater Assets)), R, Unmatched Long
    Range, S (Soft Air Refueling), T (Matched Theater Operation Short Notice
    (Theater Assets)), V (Unmatched AMC Short Notice), X (Unmatched Theater
    Operation Short Notice (AMC Assets)), Y (Matched Theater Operation Short Notice
    (AMC Assets)), Z (Other Air Refueling).
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
