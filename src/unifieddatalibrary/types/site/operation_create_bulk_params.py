# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "OperationCreateBulkParams",
    "Body",
    "BodyDailyOperation",
    "BodyDailyOperationOperatingHour",
    "BodyMaximumOnGround",
    "BodyOperationalDeviation",
    "BodyOperationalPlanning",
    "BodyPathway",
    "BodyWaiver",
]


class OperationCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyDailyOperationOperatingHour(TypedDict, total=False):
    op_start_time: Annotated[str, PropertyInfo(alias="opStartTime")]
    """The Zulu (UTC) operational start time, expressed in ISO 8601 format as HH:MM."""

    op_stop_time: Annotated[str, PropertyInfo(alias="opStopTime")]
    """The Zulu (UTC) operational stop time, expressed in ISO 8601 format as HH:MM."""


class BodyDailyOperation(TypedDict, total=False):
    day_of_week: Annotated[
        Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"],
        PropertyInfo(alias="dayOfWeek"),
    ]
    """The day of the week to which this operational information pertains."""

    operating_hours: Annotated[Iterable[BodyDailyOperationOperatingHour], PropertyInfo(alias="operatingHours")]
    """
    A collection containing the operational start and stop times scheduled for the
    day of the week specified.
    """

    operation_name: Annotated[str, PropertyInfo(alias="operationName")]
    """The name or type of operation to which this information pertains."""

    ophrs_last_changed_by: Annotated[str, PropertyInfo(alias="ophrsLastChangedBy")]
    """
    The name of the person who made the most recent change to this DailyOperation
    data.
    """

    ophrs_last_changed_date: Annotated[
        Union[str, datetime], PropertyInfo(alias="ophrsLastChangedDate", format="iso8601")
    ]
    """
    The datetime of the most recent change made to this DailyOperation data, in ISO
    8601 UTC format with millisecond precision.
    """


class BodyMaximumOnGround(TypedDict, total=False):
    aircraft_mds: Annotated[str, PropertyInfo(alias="aircraftMDS")]
    """
    The Model Design Series (MDS) designation of the aircraft to which this maximum
    on ground (MOG) data pertains.
    """

    contingency_mog: Annotated[int, PropertyInfo(alias="contingencyMOG")]
    """
    Maximum on ground (MOG) number of contingent aircraft based on spacing and
    manpower, for the aircraft type specified.
    """

    mog_last_changed_by: Annotated[str, PropertyInfo(alias="mogLastChangedBy")]
    """
    The name of the person who made the most recent change to this maximum on ground
    data.
    """

    mog_last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="mogLastChangedDate", format="iso8601")]
    """
    The datetime of the most recent change made to this maximum on ground data, in
    ISO 8601 UTC format with millisecond precision.
    """

    wide_parking_mog: Annotated[int, PropertyInfo(alias="wideParkingMOG")]
    """
    Maximum on ground (MOG) number of parking wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """

    wide_working_mog: Annotated[int, PropertyInfo(alias="wideWorkingMOG")]
    """
    Maximum on ground (MOG) number of working wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """


class BodyOperationalDeviation(TypedDict, total=False):
    affected_aircraft_mds: Annotated[str, PropertyInfo(alias="affectedAircraftMDS")]
    """
    The Model Design Series (MDS) designation of the aircraft affected by this
    operational deviation.
    """

    affected_mog: Annotated[int, PropertyInfo(alias="affectedMOG")]
    """
    The maximum on ground (MOG) number for aircraft affected by this operational
    deviation.
    """

    aircraft_on_ground_time: Annotated[str, PropertyInfo(alias="aircraftOnGroundTime")]
    """On ground time for aircraft affected by this operational deviation."""

    crew_rest_time: Annotated[str, PropertyInfo(alias="crewRestTime")]
    """Rest time for crew affected by this operational deviation."""

    od_last_changed_by: Annotated[str, PropertyInfo(alias="odLastChangedBy")]
    """
    The name of the person who made the most recent change to this
    OperationalDeviation data.
    """

    od_last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="odLastChangedDate", format="iso8601")]
    """
    The datetime of the most recent change made to this OperationalDeviation data,
    in ISO 8601 UTC format with millisecond precision.
    """

    od_remark: Annotated[str, PropertyInfo(alias="odRemark")]
    """Text remark regarding this operational deviation."""


class BodyOperationalPlanning(TypedDict, total=False):
    op_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="opEndDate", format="iso8601")]
    """
    The end date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_last_changed_by: Annotated[str, PropertyInfo(alias="opLastChangedBy")]
    """
    The name of the person who made the most recent change made to this
    OperationalPlanning data.
    """

    op_last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="opLastChangedDate", format="iso8601")]
    """
    The datetime of the most recent change made to this OperationalPlanning data, in
    ISO8601 UTC format with millisecond precision.
    """

    op_remark: Annotated[str, PropertyInfo(alias="opRemark")]
    """Remark text regarding this operation planning."""

    op_source: Annotated[str, PropertyInfo(alias="opSource")]
    """The person, unit, organization, etc. responsible for this operation planning."""

    op_start_date: Annotated[Union[str, datetime], PropertyInfo(alias="opStartDate", format="iso8601")]
    """
    The start date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_status: Annotated[str, PropertyInfo(alias="opStatus")]
    """The status of this operational planning."""


class BodyPathway(TypedDict, total=False):
    pw_definition: Annotated[str, PropertyInfo(alias="pwDefinition")]
    """Text defining this pathway from its constituent parts."""

    pw_last_changed_by: Annotated[str, PropertyInfo(alias="pwLastChangedBy")]
    """The name of the person who made the most recent change to this Pathway data."""

    pw_last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="pwLastChangedDate", format="iso8601")]
    """
    The datetime of the most recent change made to this Pathway data, in ISO 8601
    UTC format with millisecond precision.
    """

    pw_type: Annotated[str, PropertyInfo(alias="pwType")]
    """The type of paths that constitute this pathway."""

    pw_usage: Annotated[str, PropertyInfo(alias="pwUsage")]
    """The intended use of this pathway."""


class BodyWaiver(TypedDict, total=False):
    expiration_date: Annotated[Union[str, datetime], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date of this waiver, in ISO8601 UTC format with millisecond
    precision.
    """

    has_expired: Annotated[bool, PropertyInfo(alias="hasExpired")]
    """Boolean indicating whether or not this waiver has expired."""

    issue_date: Annotated[Union[str, datetime], PropertyInfo(alias="issueDate", format="iso8601")]
    """
    The issue date of this waiver, in ISO8601 UTC format with millisecond precision.
    """

    issuer_name: Annotated[str, PropertyInfo(alias="issuerName")]
    """The name of the person who issued this waiver."""

    requester_name: Annotated[str, PropertyInfo(alias="requesterName")]
    """The name of the person requesting this waiver."""

    requester_phone_number: Annotated[str, PropertyInfo(alias="requesterPhoneNumber")]
    """The phone number of the person requesting this waiver."""

    requesting_unit: Annotated[str, PropertyInfo(alias="requestingUnit")]
    """The unit requesting this waiver."""

    waiver_applies_to: Annotated[str, PropertyInfo(alias="waiverAppliesTo")]
    """Description of the entities to which this waiver applies."""

    waiver_description: Annotated[str, PropertyInfo(alias="waiverDescription")]
    """The description of this waiver."""

    waiver_last_changed_by: Annotated[str, PropertyInfo(alias="waiverLastChangedBy")]
    """The name of the person who made the most recent change to this Waiver data."""

    waiver_last_changed_date: Annotated[
        Union[str, datetime], PropertyInfo(alias="waiverLastChangedDate", format="iso8601")
    ]
    """
    The datetime of the most recent change made to this waiver data, in ISO8601 UTC
    format with millisecond precision.
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

    id_site: Required[Annotated[str, PropertyInfo(alias="idSite")]]
    """The ID of the parent site."""

    source: Required[str]
    """Source of the data."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    daily_operations: Annotated[Iterable[BodyDailyOperation], PropertyInfo(alias="dailyOperations")]
    """
    Collection providing hours of operation and other information specific to a day
    of the week.
    """

    dops_last_changed_by: Annotated[str, PropertyInfo(alias="dopsLastChangedBy")]
    """
    The name of the person who made the most recent change to data in the
    DailyOperations collection.
    """

    dops_last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="dopsLastChangedDate", format="iso8601")]
    """
    The datetime of the most recent change made to data in the DailyOperations
    collection, in ISO 8601 UTC format with millisecond precision.
    """

    dops_last_changed_reason: Annotated[str, PropertyInfo(alias="dopsLastChangedReason")]
    """
    The reason for the most recent change to data in the dailyOperations collection.
    """

    id_launch_site: Annotated[str, PropertyInfo(alias="idLaunchSite")]
    """Id of the associated launchSite entity."""

    maximum_on_grounds: Annotated[Iterable[BodyMaximumOnGround], PropertyInfo(alias="maximumOnGrounds")]
    """
    Collection providing maximum on ground (MOG) information for specific aircraft
    at the site associated with this SiteOperations record.
    """

    mogs_last_changed_by: Annotated[str, PropertyInfo(alias="mogsLastChangedBy")]
    """
    The name of the person who made the most recent change to data in the
    MaximumOnGrounds collection.
    """

    mogs_last_changed_date: Annotated[Union[str, datetime], PropertyInfo(alias="mogsLastChangedDate", format="iso8601")]
    """
    The datetime of the most recent change made to data in the MaximumOnGrounds
    collection, in ISO 8601 UTC format with millisecond precision.
    """

    mogs_last_changed_reason: Annotated[str, PropertyInfo(alias="mogsLastChangedReason")]
    """
    The reason for the most recent change to data in the MaximumOnGrounds
    collection.
    """

    operational_deviations: Annotated[Iterable[BodyOperationalDeviation], PropertyInfo(alias="operationalDeviations")]
    """
    Collection providing relevant information in the event of deviations/exceptions
    to normal operations.
    """

    operational_plannings: Annotated[Iterable[BodyOperationalPlanning], PropertyInfo(alias="operationalPlannings")]
    """Collection of planning information associated with this SiteOperations record."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    pathways: Iterable[BodyPathway]
    """
    Collection detailing operational pathways at the Site associated with this
    SiteOperations record.
    """

    waivers: Iterable[BodyWaiver]
    """
    Collection documenting operational waivers that have been issued for the Site
    associated with this record.
    """
