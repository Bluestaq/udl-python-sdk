# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DiplomaticclearanceAbridged", "DiplomaticClearanceDetail", "DiplomaticClearanceRemark"]


class DiplomaticClearanceDetail(BaseModel):
    action: Optional[str] = None
    """The type of action the aircraft can take with this diplomatic clearance (e.g.

    O for Overfly, L for Land, etc.).
    """

    alt_country_code: Optional[str] = FieldInfo(alias="altCountryCode", default=None)
    """
    Specifies an alternate country code if the data provider code is not part of an
    official Country Code standard such as ISO-3166 or FIPS. This field will be set
    to the value provided by the source and should be used for all Queries
    specifying a Country Code.
    """

    clearance_id: Optional[str] = FieldInfo(alias="clearanceId", default=None)
    """Identifier of this diplomatic clearance issued by the host country."""

    clearance_remark: Optional[str] = FieldInfo(alias="clearanceRemark", default=None)
    """Remarks concerning this diplomatic clearance."""

    cleared_call_sign: Optional[str] = FieldInfo(alias="clearedCallSign", default=None)
    """The call sign of the sortie cleared with this diplomatic clearance."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """
    The DoD Standard Country Code designator for the country issuing the diplomatic
    clearance. This field will be set to "OTHR" if the source value does not match a
    UDL Country code value (ISO-3166-ALPHA-2).
    """

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)
    """Name of the country issuing this diplomatic clearance."""

    entry_net: Optional[datetime] = FieldInfo(alias="entryNET", default=None)
    """
    Earliest time the aircraft may enter the country, in ISO 8601 UTC format with
    millisecond precision.
    """

    entry_point: Optional[str] = FieldInfo(alias="entryPoint", default=None)
    """The navigation point name where the aircraft must enter the country."""

    exit_nlt: Optional[datetime] = FieldInfo(alias="exitNLT", default=None)
    """
    Latest time the aircraft may exit the country, in ISO 8601 UTC format with
    millisecond precision.
    """

    exit_point: Optional[str] = FieldInfo(alias="exitPoint", default=None)
    """The navigation point name where the aircraft must exit the country."""

    external_clearance_id: Optional[str] = FieldInfo(alias="externalClearanceId", default=None)
    """Optional clearance ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    id_sortie: Optional[str] = FieldInfo(alias="idSortie", default=None)
    """
    Unique identifier of the Aircraft Sortie associated with this diplomatic
    clearance record.
    """

    leg_num: Optional[int] = FieldInfo(alias="legNum", default=None)
    """Identifies the Itinerary point of a sortie where an air event occurs."""

    profile: Optional[str] = None
    """The diplomatic clearance profile name used within clearance management systems."""

    req_icao: Optional[bool] = FieldInfo(alias="reqICAO", default=None)
    """
    Flag indicating whether the clearance request requires ICAO specific
    information.
    """

    req_point: Optional[bool] = FieldInfo(alias="reqPoint", default=None)
    """Flag indicating whether entry/exit points are required for clearances."""

    route_string: Optional[str] = FieldInfo(alias="routeString", default=None)
    """
    The 1801 fileable route of flight string associated with this diplomatic
    clearance. The route of flight string contains route designators, significant
    points, change of speed/altitude, change of flight rules, and cruise climbs.
    """

    sequence_num: Optional[int] = FieldInfo(alias="sequenceNum", default=None)
    """
    The placement of this diplomatic clearance within a sequence of clearances used
    on a sortie. For example, a sequence value of 3 means that it is the third
    diplomatic clearance the aircraft will use.
    """

    status: Optional[str] = None
    """Indicates the current status of the diplomatic clearance request."""

    valid_desc: Optional[str] = FieldInfo(alias="validDesc", default=None)
    """Description of when this diplomatic clearance is valid."""

    valid_end_time: Optional[datetime] = FieldInfo(alias="validEndTime", default=None)
    """
    The end time of the validity of this diplomatic clearance, in ISO 8601 UTC
    format with millisecond precision.
    """

    valid_start_time: Optional[datetime] = FieldInfo(alias="validStartTime", default=None)
    """
    The start time of the validity of this diplomatic clearance, in ISO 8601 UTC
    format with millisecond precision.
    """

    window_remark: Optional[str] = FieldInfo(alias="windowRemark", default=None)
    """Remarks concerning the valid diplomatic clearance window."""


class DiplomaticClearanceRemark(BaseModel):
    date: Optional[datetime] = None
    """
    Date the remark was published, in ISO 8601 UTC format, with millisecond
    precision.
    """

    gdss_remark_id: Optional[str] = FieldInfo(alias="gdssRemarkId", default=None)
    """Global Decision Support System (GDSS) remark identifier."""

    text: Optional[str] = None
    """Text of the remark."""

    user: Optional[str] = None
    """User who published the remark."""


class DiplomaticclearanceAbridged(BaseModel):
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

    first_dep_date: datetime = FieldInfo(alias="firstDepDate")
    """
    The First Departure Date (FDD) the mission is scheduled for departure, in ISO
    8601 UTC format with millisecond precision.
    """

    id_mission: str = FieldInfo(alias="idMission")
    """
    Unique identifier of the Mission associated with this diplomatic clearance
    record.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    apacs_id: Optional[str] = FieldInfo(alias="apacsId", default=None)
    """
    The Aircraft and Personnel Automated Clearance System (APACS) system identifier
    used to process and approve this clearance request.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    diplomatic_clearance_details: Optional[List[DiplomaticClearanceDetail]] = FieldInfo(
        alias="diplomaticClearanceDetails", default=None
    )
    """Collection of diplomatic clearance details."""

    diplomatic_clearance_remarks: Optional[List[DiplomaticClearanceRemark]] = FieldInfo(
        alias="diplomaticClearanceRemarks", default=None
    )
    """Collection of diplomatic clearance remarks."""

    dip_worksheet_name: Optional[str] = FieldInfo(alias="dipWorksheetName", default=None)
    """
    Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
    clearance requests.
    """

    doc_deadline: Optional[datetime] = FieldInfo(alias="docDeadline", default=None)
    """
    Suspense date for the diplomatic clearance worksheet to be worked, in ISO 8601
    UTC format with millisecond precision.
    """

    external_worksheet_id: Optional[str] = FieldInfo(alias="externalWorksheetId", default=None)
    """Optional diplomatic clearance worksheet ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
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

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
