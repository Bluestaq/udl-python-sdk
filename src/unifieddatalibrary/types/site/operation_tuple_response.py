# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "OperationTupleResponse",
    "OperationTupleResponseItem",
    "OperationTupleResponseItemDailyOperation",
    "OperationTupleResponseItemDailyOperationOperatingHour",
    "OperationTupleResponseItemMaximumOnGround",
    "OperationTupleResponseItemOperationalDeviation",
    "OperationTupleResponseItemOperationalPlanning",
    "OperationTupleResponseItemPathway",
    "OperationTupleResponseItemWaiver",
]


class OperationTupleResponseItemDailyOperationOperatingHour(BaseModel):
    op_start_time: Optional[str] = FieldInfo(alias="opStartTime", default=None)
    """The Zulu (UTC) operational start time, expressed in ISO 8601 format as HH:MM."""

    op_stop_time: Optional[str] = FieldInfo(alias="opStopTime", default=None)
    """The Zulu (UTC) operational stop time, expressed in ISO 8601 format as HH:MM."""


class OperationTupleResponseItemDailyOperation(BaseModel):
    day_of_week: Optional[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]] = (
        FieldInfo(alias="dayOfWeek", default=None)
    )
    """The day of the week to which this operational information pertains."""

    operating_hours: Optional[List[OperationTupleResponseItemDailyOperationOperatingHour]] = FieldInfo(
        alias="operatingHours", default=None
    )
    """
    A collection containing the operational start and stop times scheduled for the
    day of the week specified.
    """

    operation_name: Optional[str] = FieldInfo(alias="operationName", default=None)
    """The name or type of operation to which this information pertains."""

    ophrs_last_changed_by: Optional[str] = FieldInfo(alias="ophrsLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this DailyOperation
    data.
    """

    ophrs_last_changed_date: Optional[datetime] = FieldInfo(alias="ophrsLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this DailyOperation data, in ISO
    8601 UTC format with millisecond precision.
    """


class OperationTupleResponseItemMaximumOnGround(BaseModel):
    aircraft_mds: Optional[str] = FieldInfo(alias="aircraftMDS", default=None)
    """
    The Model Design Series (MDS) designation of the aircraft to which this maximum
    on ground (MOG) data pertains.
    """

    contingency_mog: Optional[int] = FieldInfo(alias="contingencyMOG", default=None)
    """
    Maximum on ground (MOG) number of contingent aircraft based on spacing and
    manpower, for the aircraft type specified.
    """

    mog_last_changed_by: Optional[str] = FieldInfo(alias="mogLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this maximum on ground
    data.
    """

    mog_last_changed_date: Optional[datetime] = FieldInfo(alias="mogLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this maximum on ground data, in
    ISO 8601 UTC format with millisecond precision.
    """

    wide_parking_mog: Optional[int] = FieldInfo(alias="wideParkingMOG", default=None)
    """
    Maximum on ground (MOG) number of parking wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """

    wide_working_mog: Optional[int] = FieldInfo(alias="wideWorkingMOG", default=None)
    """
    Maximum on ground (MOG) number of working wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """


class OperationTupleResponseItemOperationalDeviation(BaseModel):
    affected_aircraft_mds: Optional[str] = FieldInfo(alias="affectedAircraftMDS", default=None)
    """
    The Model Design Series (MDS) designation of the aircraft affected by this
    operational deviation.
    """

    affected_mog: Optional[int] = FieldInfo(alias="affectedMOG", default=None)
    """
    The maximum on ground (MOG) number for aircraft affected by this operational
    deviation.
    """

    aircraft_on_ground_time: Optional[str] = FieldInfo(alias="aircraftOnGroundTime", default=None)
    """On ground time for aircraft affected by this operational deviation."""

    crew_rest_time: Optional[str] = FieldInfo(alias="crewRestTime", default=None)
    """Rest time for crew affected by this operational deviation."""

    od_last_changed_by: Optional[str] = FieldInfo(alias="odLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this
    OperationalDeviation data.
    """

    od_last_changed_date: Optional[datetime] = FieldInfo(alias="odLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this OperationalDeviation data,
    in ISO 8601 UTC format with millisecond precision.
    """

    od_remark: Optional[str] = FieldInfo(alias="odRemark", default=None)
    """Text remark regarding this operational deviation."""


class OperationTupleResponseItemOperationalPlanning(BaseModel):
    op_end_date: Optional[datetime] = FieldInfo(alias="opEndDate", default=None)
    """
    The end date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_last_changed_by: Optional[str] = FieldInfo(alias="opLastChangedBy", default=None)
    """
    The name of the person who made the most recent change made to this
    OperationalPlanning data.
    """

    op_last_changed_date: Optional[datetime] = FieldInfo(alias="opLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this OperationalPlanning data, in
    ISO8601 UTC format with millisecond precision.
    """

    op_remark: Optional[str] = FieldInfo(alias="opRemark", default=None)
    """Remark text regarding this operation planning."""

    op_source: Optional[str] = FieldInfo(alias="opSource", default=None)
    """The person, unit, organization, etc. responsible for this operation planning."""

    op_start_date: Optional[datetime] = FieldInfo(alias="opStartDate", default=None)
    """
    The start date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_status: Optional[str] = FieldInfo(alias="opStatus", default=None)
    """The status of this operational planning."""


class OperationTupleResponseItemPathway(BaseModel):
    pw_definition: Optional[str] = FieldInfo(alias="pwDefinition", default=None)
    """Text defining this pathway from its constituent parts."""

    pw_last_changed_by: Optional[str] = FieldInfo(alias="pwLastChangedBy", default=None)
    """The name of the person who made the most recent change to this Pathway data."""

    pw_last_changed_date: Optional[datetime] = FieldInfo(alias="pwLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this Pathway data, in ISO 8601
    UTC format with millisecond precision.
    """

    pw_type: Optional[str] = FieldInfo(alias="pwType", default=None)
    """The type of paths that constitute this pathway."""

    pw_usage: Optional[str] = FieldInfo(alias="pwUsage", default=None)
    """The intended use of this pathway."""


class OperationTupleResponseItemWaiver(BaseModel):
    expiration_date: Optional[datetime] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date of this waiver, in ISO8601 UTC format with millisecond
    precision.
    """

    has_expired: Optional[bool] = FieldInfo(alias="hasExpired", default=None)
    """Boolean indicating whether or not this waiver has expired."""

    issue_date: Optional[datetime] = FieldInfo(alias="issueDate", default=None)
    """
    The issue date of this waiver, in ISO8601 UTC format with millisecond precision.
    """

    issuer_name: Optional[str] = FieldInfo(alias="issuerName", default=None)
    """The name of the person who issued this waiver."""

    requester_name: Optional[str] = FieldInfo(alias="requesterName", default=None)
    """The name of the person requesting this waiver."""

    requester_phone_number: Optional[str] = FieldInfo(alias="requesterPhoneNumber", default=None)
    """The phone number of the person requesting this waiver."""

    requesting_unit: Optional[str] = FieldInfo(alias="requestingUnit", default=None)
    """The unit requesting this waiver."""

    waiver_applies_to: Optional[str] = FieldInfo(alias="waiverAppliesTo", default=None)
    """Description of the entities to which this waiver applies."""

    waiver_description: Optional[str] = FieldInfo(alias="waiverDescription", default=None)
    """The description of this waiver."""

    waiver_last_changed_by: Optional[str] = FieldInfo(alias="waiverLastChangedBy", default=None)
    """The name of the person who made the most recent change to this Waiver data."""

    waiver_last_changed_date: Optional[datetime] = FieldInfo(alias="waiverLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this waiver data, in ISO8601 UTC
    format with millisecond precision.
    """


class OperationTupleResponseItem(BaseModel):
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

    id_site: str = FieldInfo(alias="idSite")
    """The ID of the parent site."""

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

    daily_operations: Optional[List[OperationTupleResponseItemDailyOperation]] = FieldInfo(
        alias="dailyOperations", default=None
    )
    """
    Collection providing hours of operation and other information specific to a day
    of the week.
    """

    dops_last_changed_by: Optional[str] = FieldInfo(alias="dopsLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to data in the
    DailyOperations collection.
    """

    dops_last_changed_date: Optional[datetime] = FieldInfo(alias="dopsLastChangedDate", default=None)
    """
    The datetime of the most recent change made to data in the DailyOperations
    collection, in ISO 8601 UTC format with millisecond precision.
    """

    dops_last_changed_reason: Optional[str] = FieldInfo(alias="dopsLastChangedReason", default=None)
    """
    The reason for the most recent change to data in the dailyOperations collection.
    """

    id_launch_site: Optional[str] = FieldInfo(alias="idLaunchSite", default=None)
    """Id of the associated launchSite entity."""

    maximum_on_grounds: Optional[List[OperationTupleResponseItemMaximumOnGround]] = FieldInfo(
        alias="maximumOnGrounds", default=None
    )
    """
    Collection providing maximum on ground (MOG) information for specific aircraft
    at the site associated with this SiteOperations record.
    """

    mogs_last_changed_by: Optional[str] = FieldInfo(alias="mogsLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to data in the
    MaximumOnGrounds collection.
    """

    mogs_last_changed_date: Optional[datetime] = FieldInfo(alias="mogsLastChangedDate", default=None)
    """
    The datetime of the most recent change made to data in the MaximumOnGrounds
    collection, in ISO 8601 UTC format with millisecond precision.
    """

    mogs_last_changed_reason: Optional[str] = FieldInfo(alias="mogsLastChangedReason", default=None)
    """
    The reason for the most recent change to data in the MaximumOnGrounds
    collection.
    """

    operational_deviations: Optional[List[OperationTupleResponseItemOperationalDeviation]] = FieldInfo(
        alias="operationalDeviations", default=None
    )
    """
    Collection providing relevant information in the event of deviations/exceptions
    to normal operations.
    """

    operational_plannings: Optional[List[OperationTupleResponseItemOperationalPlanning]] = FieldInfo(
        alias="operationalPlannings", default=None
    )
    """Collection of planning information associated with this SiteOperations record."""

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

    pathways: Optional[List[OperationTupleResponseItemPathway]] = None
    """
    Collection detailing operational pathways at the Site associated with this
    SiteOperations record.
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

    waivers: Optional[List[OperationTupleResponseItemWaiver]] = None
    """
    Collection documenting operational waivers that have been issued for the Site
    associated with this record.
    """


OperationTupleResponse: TypeAlias = List[OperationTupleResponseItem]
