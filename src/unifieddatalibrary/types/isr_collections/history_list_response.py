# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..isr_collection_requirements_full import IsrCollectionRequirementsFull

__all__ = [
    "HistoryListResponse",
    "Tasking",
    "TaskingCollectionPeriods",
    "TaskingCollectionPeriodsActual",
    "TaskingCollectionPeriodsPlanned",
    "TaskingCollectionPeriodsPlannedAdditional",
    "Transit",
]


class TaskingCollectionPeriodsActual(BaseModel):
    id: Optional[str] = None
    """Unique Identifier of actual collection period for historical archive."""

    start: Optional[datetime] = None
    """Start time the collection actually occurred, in ISO 8601 UTC format."""

    stop: Optional[datetime] = None
    """Stop time the collection actually occurred, in ISO 8601 UTC format."""


class TaskingCollectionPeriodsPlannedAdditional(BaseModel):
    id: Optional[str] = None
    """Unique Identifier of additional collection period."""

    start: Optional[datetime] = None
    """Start time of collection, in ISO 8601 UTC format."""

    stop: Optional[datetime] = None
    """Stop time of collection, in ISO 8601 UTC format."""


class TaskingCollectionPeriodsPlanned(BaseModel):
    additional: Optional[List[TaskingCollectionPeriodsPlannedAdditional]] = None
    """Additional start and stop for the collection."""

    start: Optional[datetime] = None
    """Start time of collection, in ISO 8601 UTC format."""

    stop: Optional[datetime] = None
    """Stop time of collection, in ISO 8601 UTC format."""


class TaskingCollectionPeriods(BaseModel):
    actual: Optional[List[TaskingCollectionPeriodsActual]] = None
    """Actual start and stop for the collection."""

    planned: Optional[TaskingCollectionPeriodsPlanned] = None


class Tasking(BaseModel):
    id: Optional[str] = None
    """Tasking Unique Identifier."""

    collection_periods: Optional[TaskingCollectionPeriods] = FieldInfo(alias="collectionPeriods", default=None)

    collection_type: Optional[Literal["Simultaneous", "Sequential", "Operationally", "Driven", "Priority", "Order"]] = (
        FieldInfo(alias="collectionType", default=None)
    )
    """Type of collection tasked."""

    eight_line: Optional[str] = FieldInfo(alias="eightLine", default=None)
    """Eight line."""

    special_com_guidance: Optional[str] = FieldInfo(alias="specialComGuidance", default=None)
    """
    Free text field for the user to specify special instructions needed for this
    collection.
    """

    sro_track: Optional[str] = FieldInfo(alias="sroTrack", default=None)
    """Value of the Sensitive Reconnaissance Operations Track."""

    tasking_aor: Optional[str] = FieldInfo(alias="taskingAOR", default=None)
    """Human readable definition of this taskings Area Of Responsibility."""

    tasking_collection_area: Optional[str] = FieldInfo(alias="taskingCollectionArea", default=None)
    """Tasking geographical collection area."""

    tasking_collection_requirements: Optional[List[IsrCollectionRequirementsFull]] = FieldInfo(
        alias="taskingCollectionRequirements", default=None
    )
    """Tasking desired collection requirements."""

    tasking_country: Optional[str] = FieldInfo(alias="taskingCountry", default=None)
    """Country code of the tasking.

    A Country may represent countries, multi-national consortiums, and international
    organizations.
    """

    tasking_emphasis: Optional[str] = FieldInfo(alias="taskingEmphasis", default=None)
    """Tasking emphasis."""

    tasking_joa: Optional[str] = FieldInfo(alias="taskingJoa", default=None)
    """Joint Operations Area."""

    tasking_operation: Optional[str] = FieldInfo(alias="taskingOperation", default=None)
    """Tasking operation name."""

    tasking_primary_intel_discipline: Optional[str] = FieldInfo(alias="taskingPrimaryIntelDiscipline", default=None)
    """Primary type of intelligence to be collected during the mission."""

    tasking_primary_sub_category: Optional[str] = FieldInfo(alias="taskingPrimarySubCategory", default=None)
    """Sub category of primary intelligence to be collected."""

    tasking_priority: Optional[float] = FieldInfo(alias="taskingPriority", default=None)
    """Tasking Priority (1-n)."""

    tasking_region: Optional[str] = FieldInfo(alias="taskingRegion", default=None)
    """Region of the tasking."""

    tasking_retask_time: Optional[datetime] = FieldInfo(alias="taskingRetaskTime", default=None)
    """Time of retasking, in ISO 8601 UTC format."""

    tasking_role: Optional[str] = FieldInfo(alias="taskingRole", default=None)
    """What is the primary objective (role) of this task."""

    tasking_secondary_intel_discipline: Optional[str] = FieldInfo(alias="taskingSecondaryIntelDiscipline", default=None)
    """Type of tasking intelligence to be collected second."""

    tasking_secondary_sub_category: Optional[str] = FieldInfo(alias="taskingSecondarySubCategory", default=None)
    """Mission sub category for secondary intelligence discipline to be collected."""

    tasking_start_point_lat: Optional[float] = FieldInfo(alias="taskingStartPointLat", default=None)
    """WGS-84 latitude of the start position, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    tasking_start_point_long: Optional[float] = FieldInfo(alias="taskingStartPointLong", default=None)
    """WGS-84 longitude of the start position, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    tasking_sub_region: Optional[str] = FieldInfo(alias="taskingSubRegion", default=None)
    """Subregion of the tasking."""

    tasking_supported_unit: Optional[str] = FieldInfo(alias="taskingSupportedUnit", default=None)
    """Military Base to transmit the dissemination of this data."""

    tasking_sync_matrix_bin: Optional[str] = FieldInfo(alias="taskingSyncMatrixBin", default=None)
    """
    A synchronization matrix is used to organize the logistics synchronization
    process during a mission.
    """

    type: Optional[Literal["Deliberate", "Dynamic", "Training", "Transit"]] = None
    """Type of tasking."""


class Transit(BaseModel):
    id: Optional[str] = None
    """Transit Unique Identifier."""

    base: Optional[str] = None
    """Military Base to transmit the dissemination of this data."""

    duration: Optional[float] = None
    """Length of mission in milliseconds."""


class HistoryListResponse(BaseModel):
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

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    collection_requirements: Optional[List[IsrCollectionRequirementsFull]] = FieldInfo(
        alias="collectionRequirements", default=None
    )
    """Mission desired collection requirements."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    idex_version: Optional[int] = FieldInfo(alias="idexVersion", default=None)
    """Version of the IDEX software the request came from for compatibility."""

    mission_aor: Optional[str] = FieldInfo(alias="missionAOR", default=None)
    """Designation of mission Area Of Responsibility."""

    mission_collection_area: Optional[str] = FieldInfo(alias="missionCollectionArea", default=None)
    """Mission geographical collection area."""

    mission_country: Optional[str] = FieldInfo(alias="missionCountry", default=None)
    """Country code of the mission.

    A Country may represent countries, multi-national consortiums, and international
    organizations.
    """

    mission_emphasis: Optional[str] = FieldInfo(alias="missionEmphasis", default=None)
    """Text version of what we are emphasizing in this mission."""

    mission_id: Optional[str] = FieldInfo(alias="missionId", default=None)
    """Mission Identifier."""

    mission_joa: Optional[str] = FieldInfo(alias="missionJoa", default=None)
    """Joint Operations Area."""

    mission_operation: Optional[str] = FieldInfo(alias="missionOperation", default=None)
    """Mission operation name."""

    mission_primary_intel_discipline: Optional[str] = FieldInfo(alias="missionPrimaryIntelDiscipline", default=None)
    """Primary type of intelligence to be collected during the mission."""

    mission_primary_sub_category: Optional[str] = FieldInfo(alias="missionPrimarySubCategory", default=None)
    """Sub category of primary intelligence to be collected."""

    mission_priority: Optional[int] = FieldInfo(alias="missionPriority", default=None)
    """Mission Priority (1-n)."""

    mission_region: Optional[str] = FieldInfo(alias="missionRegion", default=None)
    """Region of the mission."""

    mission_role: Optional[str] = FieldInfo(alias="missionRole", default=None)
    """What is the primary objective(Role) of this mission."""

    mission_secondary_intel_discipline: Optional[str] = FieldInfo(alias="missionSecondaryIntelDiscipline", default=None)
    """Type of intelligence to be collected second."""

    mission_secondary_sub_category: Optional[str] = FieldInfo(alias="missionSecondarySubCategory", default=None)
    """Mission sub category for secondary intelligence discipline to be collected."""

    mission_start_point_lat: Optional[float] = FieldInfo(alias="missionStartPointLat", default=None)
    """WGS-84 latitude of the start position, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    mission_start_point_long: Optional[float] = FieldInfo(alias="missionStartPointLong", default=None)
    """WGS-84 longitude of the start position, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    mission_sub_region: Optional[str] = FieldInfo(alias="missionSubRegion", default=None)
    """Subregion of the mission."""

    mission_supported_unit: Optional[str] = FieldInfo(alias="missionSupportedUnit", default=None)
    """Name of the Supporting unit/Location that is performing this mission."""

    mission_sync_matrix_bin: Optional[str] = FieldInfo(alias="missionSyncMatrixBin", default=None)
    """
    A synchronization matrix is used to organize the logistics synchronization
    process during a mission.
    """

    name: Optional[str] = None
    """Human readable Mission Name."""

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

    taskings: Optional[List[Tasking]] = None
    """Individual taskings to complete the mission."""

    transit: Optional[List[Transit]] = None
    """Object for data dissemination."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    Time the row was updated in the database, auto-populated by the system, example
    = 2018-01-01T16:00:00.123Z.
    """

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
