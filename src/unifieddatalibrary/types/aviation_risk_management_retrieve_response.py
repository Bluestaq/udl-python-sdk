# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AviationRiskManagementRetrieveResponse",
    "AviationRiskManagementWorksheetRecord",
    "AviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScore",
    "AviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScoreAviationRiskManagementSortie",
]


class AviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScoreAviationRiskManagementSortie(BaseModel):
    ext_sortie_id: Optional[str] = FieldInfo(alias="extSortieId", default=None)
    """Optional aircraft sortie ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    id_sortie: Optional[str] = FieldInfo(alias="idSortie", default=None)
    """
    Unique identifier of an associated Aircraft Sortie that is assigned to this risk
    management record.
    """

    leg_num: Optional[int] = FieldInfo(alias="legNum", default=None)
    """The leg number of the sortie."""

    sortie_score: Optional[int] = FieldInfo(alias="sortieScore", default=None)
    """The score of the associated aircraft sortie as defined by the data source.

    Value ranges from 0 to 3, where a value of 0 indicates a low and a value of 3
    indicates severe. A value of -1 indicates no score.
    """


class AviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScore(BaseModel):
    approval_date: Optional[datetime] = FieldInfo(alias="approvalDate", default=None)
    """
    Timestamp the worksheet record score was approval or disapproval, in ISO 8601
    UTC format with millisecond precision.
    """

    approved_by: Optional[str] = FieldInfo(alias="approvedBy", default=None)
    """Name of the individual who approved or disapproved of the score."""

    approved_code: Optional[int] = FieldInfo(alias="approvedCode", default=None)
    """Numeric assignment used to determine score approval.

    0 - APPROVAL PENDING (used when score value is 2 or 3); 1 - APPROVED (used when
    score value is 2 or 3); 2 - DISAPPROVED.
    """

    aviation_risk_management_sortie: Optional[
        List[AviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScoreAviationRiskManagementSortie]
    ] = FieldInfo(alias="aviationRiskManagementSortie", default=None)
    """Collection of aviation risk management worksheet record score aircraft sorties."""

    ext_score_id: Optional[str] = FieldInfo(alias="extScoreId", default=None)
    """Optional identifier of the worksheet record score provided by the data source.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    risk_category: Optional[str] = FieldInfo(alias="riskCategory", default=None)
    """The category of the risk factor."""

    risk_description: Optional[str] = FieldInfo(alias="riskDescription", default=None)
    """Description of the risk factor."""

    risk_key: Optional[str] = FieldInfo(alias="riskKey", default=None)
    """Code or identifier of the risk factor category as defined by the data source."""

    risk_name: Optional[str] = FieldInfo(alias="riskName", default=None)
    """Name of the risk factor."""

    score: Optional[int] = None
    """Score of the worksheet record risk factor.

    Value ranges from 0 to 3, where a value of 0 indicates a low and a value of 3
    indicates severe. A value of -1 indicates no score.
    """

    score_remark: Optional[str] = FieldInfo(alias="scoreRemark", default=None)
    """Remarks and/or comments regarding the worksheet score."""


class AviationRiskManagementWorksheetRecord(BaseModel):
    mission_date: date = FieldInfo(alias="missionDate")
    """Date of the mission in ISO 8601 date-only format (YYYY-MM-DD)."""

    aircraft_mds: Optional[str] = FieldInfo(alias="aircraftMDS", default=None)
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of the aircraft associated with
    this risk management worksheet record. Intended as, but not constrained to,
    MIL-STD-6016 environment dependent specific type designations.
    """

    approval_pending: Optional[bool] = FieldInfo(alias="approvalPending", default=None)
    """Flag indicating the worksheet record is pending approval."""

    approved: Optional[bool] = None
    """Flag indicating the worksheet record is approved."""

    aviation_risk_management_worksheet_score: Optional[
        List[AviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScore]
    ] = FieldInfo(alias="aviationRiskManagementWorksheetScore", default=None)
    """Collection of Aviation Risk Management worksheet record scores."""

    disposition_comments: Optional[str] = FieldInfo(alias="dispositionComments", default=None)
    """
    Comment(s) explaining why the worksheet record has been approved or disapproved.
    """

    ext_record_id: Optional[str] = FieldInfo(alias="extRecordId", default=None)
    """Optional identifier of the worksheet record provided by the data source.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    itinerary: Optional[str] = None
    """Sequential order of itinerary locations associated for the mission."""

    last_updated_at: Optional[datetime] = FieldInfo(alias="lastUpdatedAt", default=None)
    """
    Timestamp the worksheet record was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    remarks: Optional[str] = None
    """Remarks and/or comments regarding the worksheet record."""

    severity_level: Optional[int] = FieldInfo(alias="severityLevel", default=None)
    """Numeric assignment for the worksheet record severity.

    0 - LOW; 1 - MODERATE; 2 - HIGH; 3 - SEVERE.
    """

    submission_date: Optional[datetime] = FieldInfo(alias="submissionDate", default=None)
    """
    Timestamp the worksheet record was submitted, in ISO 8601 UTC format with
    millisecond precision.
    """

    tier_number: Optional[int] = FieldInfo(alias="tierNumber", default=None)
    """Tier number which the mission is being scored as determined by the data source.

    For example, Tier 1 may indicate mission planners, Tier 2 may indicate
    operations personnel, Tier 3 may indicate squadron leadership, and Tier 4 may
    indicate the aircrew.
    """

    total_score: Optional[int] = FieldInfo(alias="totalScore", default=None)
    """Total score for the worksheet record as defined by the data source.

    Larger values indicate a higher risk level. For example, values between 0-10 may
    indicate a low risk level, where values greater then 40 indicate a severe risk
    level.
    """

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """User identifier associated to the worksheet record."""


class AviationRiskManagementRetrieveResponse(BaseModel):
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

    id_mission: str = FieldInfo(alias="idMission")
    """
    The unique identifier of the mission to which this risk management record is
    assigned.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    aviation_risk_management_worksheet_record: Optional[List[AviationRiskManagementWorksheetRecord]] = FieldInfo(
        alias="aviationRiskManagementWorksheetRecord", default=None
    )
    """Collection of Aviation Risk Management Worksheet Records."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    ext_mission_id: Optional[str] = FieldInfo(alias="extMissionId", default=None)
    """Optional mission ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    mission_number: Optional[str] = FieldInfo(alias="missionNumber", default=None)
    """The mission number of the mission associated with this record."""

    org_id: Optional[str] = FieldInfo(alias="orgId", default=None)
    """Identifier for the organization which this risk management record is evaluated."""

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

    unit_id: Optional[str] = FieldInfo(alias="unitId", default=None)
    """Identifier for the unit which this risk management record is evaluated."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
