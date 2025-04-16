# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IsrCollectionUnvalidatedPublishParams",
    "Body",
    "BodyCollectionRequirement",
    "BodyCollectionRequirementCriticalTimes",
    "BodyCollectionRequirementExploitationRequirement",
    "BodyCollectionRequirementExploitationRequirementPoc",
    "BodyTasking",
    "BodyTaskingCollectionPeriods",
    "BodyTaskingCollectionPeriodsActual",
    "BodyTaskingCollectionPeriodsPlanned",
    "BodyTaskingCollectionPeriodsPlannedAdditional",
    "BodyTaskingTaskingCollectionRequirement",
    "BodyTaskingTaskingCollectionRequirementCriticalTimes",
    "BodyTaskingTaskingCollectionRequirementExploitationRequirement",
    "BodyTaskingTaskingCollectionRequirementExploitationRequirementPoc",
    "BodyTransit",
]


class IsrCollectionUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyCollectionRequirementCriticalTimes(TypedDict, total=False):
    earliest_imaging_time: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="earliestImagingTime", format="iso8601")]
    ]
    """Critical start time to collect an image for this requirement."""

    latest_imaging_time: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="latestImagingTime", format="iso8601")]
    ]
    """Critical stop time to collect an image for this requirement."""


class BodyCollectionRequirementExploitationRequirementPoc(TypedDict, total=False):
    id: str
    """Unique identifier of the collection requirement POC."""

    callsign: str
    """Callsign of the POC."""

    chat_name: Annotated[str, PropertyInfo(alias="chatName")]
    """Chat name of the POC."""

    chat_system: Annotated[str, PropertyInfo(alias="chatSystem")]
    """Chat system the POC is accessing."""

    email: str
    """Email address of the POC."""

    name: str
    """Name of the POC."""

    notes: str
    """Amplifying notes about the POC."""

    phone: str
    """Phone number of the POC."""

    radio_frequency: Annotated[float, PropertyInfo(alias="radioFrequency")]
    """Radio Frequency the POC is on."""

    unit: str
    """Unit the POC belongs to."""


class BodyCollectionRequirementExploitationRequirement(TypedDict, total=False):
    id: str
    """Exploitation requirement id."""

    amplification: str
    """Amplifying data for the exploitation requirement."""

    dissemination: str
    """List of e-mails to disseminate collection verification information."""

    eei: str
    """Essential Elements of Information."""

    poc: BodyCollectionRequirementExploitationRequirementPoc

    reporting_criteria: Annotated[str, PropertyInfo(alias="reportingCriteria")]
    """The reporting criteria of the collection requirement."""


class BodyCollectionRequirement(TypedDict, total=False):
    id: str
    """Collection Requirement Unique Identifier."""

    country: str
    """Country code of the collection requirement.

    A Country may represent countries, multi-national consortiums, and international
    organizations.
    """

    crid_numbers: Annotated[str, PropertyInfo(alias="cridNumbers")]
    """Collection Requirement Unique Identifier."""

    critical_times: Annotated[BodyCollectionRequirementCriticalTimes, PropertyInfo(alias="criticalTimes")]

    emphasized: bool
    """Is this collection requirement an emphasized/critical requirement."""

    exploitation_requirement: Annotated[
        BodyCollectionRequirementExploitationRequirement, PropertyInfo(alias="exploitationRequirement")
    ]

    hash: str
    """Encryption hashing algorithm."""

    intel_discipline: Annotated[str, PropertyInfo(alias="intelDiscipline")]
    """Primary type of intelligence to be collected for this requirement."""

    is_prism_cr: Annotated[bool, PropertyInfo(alias="isPrismCr")]
    """Is this collection request for the Prism system?."""

    operation: str
    """Human readable name for this operation."""

    priority: float
    """1-n priority for this collection requirement."""

    recon_survey: Annotated[str, PropertyInfo(alias="reconSurvey")]
    """Reconnaissance Survey information the operator needs."""

    record_id: Annotated[str, PropertyInfo(alias="recordId")]
    """Record id."""

    region: str
    """Region of the collection requirement."""

    secondary: bool
    """Sub category of primary intelligence to be collected for this requirement."""

    special_com_guidance: Annotated[str, PropertyInfo(alias="specialComGuidance")]
    """
    Free text field for the user to specify special instructions needed for this
    collection.
    """

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start time for this requirement, should be within the mission time window."""

    stop: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Stop time for this requirement, should be within the mission time window."""

    subregion: str
    """Subregion of the collection requirement."""

    supported_unit: Annotated[str, PropertyInfo(alias="supportedUnit")]
    """
    The name of the military unit that this assigned collection requirement will
    support.
    """

    target_list: Annotated[List[str], PropertyInfo(alias="targetList")]
    """Array of POI Id's for the targets being tasked."""

    type: str
    """Type collection this requirement applies to."""


class BodyTaskingCollectionPeriodsActual(TypedDict, total=False):
    id: str
    """Unique Identifier of actual collection period for historical archive."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start time the collection actually occurred, in ISO 8601 UTC format."""

    stop: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Stop time the collection actually occurred, in ISO 8601 UTC format."""


class BodyTaskingCollectionPeriodsPlannedAdditional(TypedDict, total=False):
    id: str
    """Unique Identifier of additional collection period."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start time of collection, in ISO 8601 UTC format."""

    stop: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Stop time of collection, in ISO 8601 UTC format."""


class BodyTaskingCollectionPeriodsPlanned(TypedDict, total=False):
    additional: Iterable[BodyTaskingCollectionPeriodsPlannedAdditional]
    """Additional start and stop for the collection."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start time of collection, in ISO 8601 UTC format."""

    stop: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Stop time of collection, in ISO 8601 UTC format."""


class BodyTaskingCollectionPeriods(TypedDict, total=False):
    actual: Iterable[BodyTaskingCollectionPeriodsActual]
    """Actual start and stop for the collection."""

    planned: BodyTaskingCollectionPeriodsPlanned


class BodyTaskingTaskingCollectionRequirementCriticalTimes(TypedDict, total=False):
    earliest_imaging_time: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="earliestImagingTime", format="iso8601")]
    ]
    """Critical start time to collect an image for this requirement."""

    latest_imaging_time: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="latestImagingTime", format="iso8601")]
    ]
    """Critical stop time to collect an image for this requirement."""


class BodyTaskingTaskingCollectionRequirementExploitationRequirementPoc(TypedDict, total=False):
    id: str
    """Unique identifier of the collection requirement POC."""

    callsign: str
    """Callsign of the POC."""

    chat_name: Annotated[str, PropertyInfo(alias="chatName")]
    """Chat name of the POC."""

    chat_system: Annotated[str, PropertyInfo(alias="chatSystem")]
    """Chat system the POC is accessing."""

    email: str
    """Email address of the POC."""

    name: str
    """Name of the POC."""

    notes: str
    """Amplifying notes about the POC."""

    phone: str
    """Phone number of the POC."""

    radio_frequency: Annotated[float, PropertyInfo(alias="radioFrequency")]
    """Radio Frequency the POC is on."""

    unit: str
    """Unit the POC belongs to."""


class BodyTaskingTaskingCollectionRequirementExploitationRequirement(TypedDict, total=False):
    id: str
    """Exploitation requirement id."""

    amplification: str
    """Amplifying data for the exploitation requirement."""

    dissemination: str
    """List of e-mails to disseminate collection verification information."""

    eei: str
    """Essential Elements of Information."""

    poc: BodyTaskingTaskingCollectionRequirementExploitationRequirementPoc

    reporting_criteria: Annotated[str, PropertyInfo(alias="reportingCriteria")]
    """The reporting criteria of the collection requirement."""


class BodyTaskingTaskingCollectionRequirement(TypedDict, total=False):
    id: str
    """Collection Requirement Unique Identifier."""

    country: str
    """Country code of the collection requirement.

    A Country may represent countries, multi-national consortiums, and international
    organizations.
    """

    crid_numbers: Annotated[str, PropertyInfo(alias="cridNumbers")]
    """Collection Requirement Unique Identifier."""

    critical_times: Annotated[BodyTaskingTaskingCollectionRequirementCriticalTimes, PropertyInfo(alias="criticalTimes")]

    emphasized: bool
    """Is this collection requirement an emphasized/critical requirement."""

    exploitation_requirement: Annotated[
        BodyTaskingTaskingCollectionRequirementExploitationRequirement, PropertyInfo(alias="exploitationRequirement")
    ]

    hash: str
    """Encryption hashing algorithm."""

    intel_discipline: Annotated[str, PropertyInfo(alias="intelDiscipline")]
    """Primary type of intelligence to be collected for this requirement."""

    is_prism_cr: Annotated[bool, PropertyInfo(alias="isPrismCr")]
    """Is this collection request for the Prism system?."""

    operation: str
    """Human readable name for this operation."""

    priority: float
    """1-n priority for this collection requirement."""

    recon_survey: Annotated[str, PropertyInfo(alias="reconSurvey")]
    """Reconnaissance Survey information the operator needs."""

    record_id: Annotated[str, PropertyInfo(alias="recordId")]
    """Record id."""

    region: str
    """Region of the collection requirement."""

    secondary: bool
    """Sub category of primary intelligence to be collected for this requirement."""

    special_com_guidance: Annotated[str, PropertyInfo(alias="specialComGuidance")]
    """
    Free text field for the user to specify special instructions needed for this
    collection.
    """

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start time for this requirement, should be within the mission time window."""

    stop: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Stop time for this requirement, should be within the mission time window."""

    subregion: str
    """Subregion of the collection requirement."""

    supported_unit: Annotated[str, PropertyInfo(alias="supportedUnit")]
    """
    The name of the military unit that this assigned collection requirement will
    support.
    """

    target_list: Annotated[List[str], PropertyInfo(alias="targetList")]
    """Array of POI Id's for the targets being tasked."""

    type: str
    """Type collection this requirement applies to."""


class BodyTasking(TypedDict, total=False):
    id: str
    """Tasking Unique Identifier."""

    collection_periods: Annotated[BodyTaskingCollectionPeriods, PropertyInfo(alias="collectionPeriods")]

    collection_type: Annotated[
        Literal["Simultaneous", "Sequential", "Operationally", "Driven", "Priority", "Order"],
        PropertyInfo(alias="collectionType"),
    ]
    """Type of collection tasked."""

    eight_line: Annotated[str, PropertyInfo(alias="eightLine")]
    """Eight line."""

    special_com_guidance: Annotated[str, PropertyInfo(alias="specialComGuidance")]
    """
    Free text field for the user to specify special instructions needed for this
    collection.
    """

    sro_track: Annotated[str, PropertyInfo(alias="sroTrack")]
    """Value of the Sensitive Reconnaissance Operations Track."""

    tasking_aor: Annotated[str, PropertyInfo(alias="taskingAOR")]
    """Human readable definition of this taskings Area Of Responsibility."""

    tasking_collection_area: Annotated[str, PropertyInfo(alias="taskingCollectionArea")]
    """Tasking geographical collection area."""

    tasking_collection_requirements: Annotated[
        Iterable[BodyTaskingTaskingCollectionRequirement], PropertyInfo(alias="taskingCollectionRequirements")
    ]
    """Tasking desired collection requirements."""

    tasking_country: Annotated[str, PropertyInfo(alias="taskingCountry")]
    """Country code of the tasking.

    A Country may represent countries, multi-national consortiums, and international
    organizations.
    """

    tasking_emphasis: Annotated[str, PropertyInfo(alias="taskingEmphasis")]
    """Tasking emphasis."""

    tasking_joa: Annotated[str, PropertyInfo(alias="taskingJoa")]
    """Joint Operations Area."""

    tasking_operation: Annotated[str, PropertyInfo(alias="taskingOperation")]
    """Tasking operation name."""

    tasking_primary_intel_discipline: Annotated[str, PropertyInfo(alias="taskingPrimaryIntelDiscipline")]
    """Primary type of intelligence to be collected during the mission."""

    tasking_primary_sub_category: Annotated[str, PropertyInfo(alias="taskingPrimarySubCategory")]
    """Sub category of primary intelligence to be collected."""

    tasking_priority: Annotated[float, PropertyInfo(alias="taskingPriority")]
    """Tasking Priority (1-n)."""

    tasking_region: Annotated[str, PropertyInfo(alias="taskingRegion")]
    """Region of the tasking."""

    tasking_retask_time: Annotated[Union[str, datetime], PropertyInfo(alias="taskingRetaskTime", format="iso8601")]
    """Time of retasking, in ISO 8601 UTC format."""

    tasking_role: Annotated[str, PropertyInfo(alias="taskingRole")]
    """What is the primary objective (role) of this task."""

    tasking_secondary_intel_discipline: Annotated[str, PropertyInfo(alias="taskingSecondaryIntelDiscipline")]
    """Type of tasking intelligence to be collected second."""

    tasking_secondary_sub_category: Annotated[str, PropertyInfo(alias="taskingSecondarySubCategory")]
    """Mission sub category for secondary intelligence discipline to be collected."""

    tasking_start_point_lat: Annotated[float, PropertyInfo(alias="taskingStartPointLat")]
    """WGS-84 latitude of the start position, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    tasking_start_point_long: Annotated[float, PropertyInfo(alias="taskingStartPointLong")]
    """WGS-84 longitude of the start position, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    tasking_sub_region: Annotated[str, PropertyInfo(alias="taskingSubRegion")]
    """Subregion of the tasking."""

    tasking_supported_unit: Annotated[str, PropertyInfo(alias="taskingSupportedUnit")]
    """Military Base to transmit the dissemination of this data."""

    tasking_sync_matrix_bin: Annotated[str, PropertyInfo(alias="taskingSyncMatrixBin")]
    """
    A synchronization matrix is used to organize the logistics synchronization
    process during a mission.
    """

    type: Literal["Deliberate", "Dynamic", "Training", "Transit"]
    """Type of tasking."""


class BodyTransit(TypedDict, total=False):
    id: str
    """Transit Unique Identifier."""

    base: str
    """Military Base to transmit the dissemination of this data."""

    duration: float
    """Length of mission in milliseconds."""


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

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    collection_requirements: Annotated[
        Iterable[BodyCollectionRequirement], PropertyInfo(alias="collectionRequirements")
    ]
    """Mission desired collection requirements."""

    idex_version: Annotated[int, PropertyInfo(alias="idexVersion")]
    """Version of the IDEX software the request came from for compatibility."""

    mission_aor: Annotated[str, PropertyInfo(alias="missionAOR")]
    """Designation of mission Area Of Responsibility."""

    mission_collection_area: Annotated[str, PropertyInfo(alias="missionCollectionArea")]
    """Mission geographical collection area."""

    mission_country: Annotated[str, PropertyInfo(alias="missionCountry")]
    """Country code of the mission.

    A Country may represent countries, multi-national consortiums, and international
    organizations.
    """

    mission_emphasis: Annotated[str, PropertyInfo(alias="missionEmphasis")]
    """Text version of what we are emphasizing in this mission."""

    mission_id: Annotated[str, PropertyInfo(alias="missionId")]
    """Mission Identifier."""

    mission_joa: Annotated[str, PropertyInfo(alias="missionJoa")]
    """Joint Operations Area."""

    mission_operation: Annotated[str, PropertyInfo(alias="missionOperation")]
    """Mission operation name."""

    mission_primary_intel_discipline: Annotated[str, PropertyInfo(alias="missionPrimaryIntelDiscipline")]
    """Primary type of intelligence to be collected during the mission."""

    mission_primary_sub_category: Annotated[str, PropertyInfo(alias="missionPrimarySubCategory")]
    """Sub category of primary intelligence to be collected."""

    mission_priority: Annotated[int, PropertyInfo(alias="missionPriority")]
    """Mission Priority (1-n)."""

    mission_region: Annotated[str, PropertyInfo(alias="missionRegion")]
    """Region of the mission."""

    mission_role: Annotated[str, PropertyInfo(alias="missionRole")]
    """What is the primary objective(Role) of this mission."""

    mission_secondary_intel_discipline: Annotated[str, PropertyInfo(alias="missionSecondaryIntelDiscipline")]
    """Type of intelligence to be collected second."""

    mission_secondary_sub_category: Annotated[str, PropertyInfo(alias="missionSecondarySubCategory")]
    """Mission sub category for secondary intelligence discipline to be collected."""

    mission_start_point_lat: Annotated[float, PropertyInfo(alias="missionStartPointLat")]
    """WGS-84 latitude of the start position, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    mission_start_point_long: Annotated[float, PropertyInfo(alias="missionStartPointLong")]
    """WGS-84 longitude of the start position, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    mission_sub_region: Annotated[str, PropertyInfo(alias="missionSubRegion")]
    """Subregion of the mission."""

    mission_supported_unit: Annotated[str, PropertyInfo(alias="missionSupportedUnit")]
    """Name of the Supporting unit/Location that is performing this mission."""

    mission_sync_matrix_bin: Annotated[str, PropertyInfo(alias="missionSyncMatrixBin")]
    """
    A synchronization matrix is used to organize the logistics synchronization
    process during a mission.
    """

    name: str
    """Human readable Mission Name."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    taskings: Iterable[BodyTasking]
    """Individual taskings to complete the mission."""

    transit: Iterable[BodyTransit]
    """Object for data dissemination."""
