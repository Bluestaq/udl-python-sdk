# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AviationRiskManagementUnvalidatedPublishParams",
    "Body",
    "BodyAviationRiskManagementWorksheetRecord",
    "BodyAviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScore",
    "BodyAviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScoreAviationRiskManagementSortie",
]


class AviationRiskManagementUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyAviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScoreAviationRiskManagementSortie(
    TypedDict, total=False
):
    ext_sortie_id: Annotated[str, PropertyInfo(alias="extSortieId")]
    """Optional aircraft sortie ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    id_sortie: Annotated[str, PropertyInfo(alias="idSortie")]
    """
    Unique identifier of an associated Aircraft Sortie that is assigned to this risk
    management record.
    """

    leg_num: Annotated[int, PropertyInfo(alias="legNum")]
    """The leg number of the sortie."""

    sortie_score: Annotated[int, PropertyInfo(alias="sortieScore")]
    """The score of the associated aircraft sortie as defined by the data source.

    Value ranges from 0 to 3, where a value of 0 indicates a low and a value of 3
    indicates severe. A value of -1 indicates no score.
    """


class BodyAviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScore(TypedDict, total=False):
    approval_date: Annotated[Union[str, datetime], PropertyInfo(alias="approvalDate", format="iso8601")]
    """
    Timestamp the worksheet record score was approval or disapproval, in ISO 8601
    UTC format with millisecond precision.
    """

    approved_by: Annotated[str, PropertyInfo(alias="approvedBy")]
    """Name of the individual who approved or disapproved of the score."""

    approved_code: Annotated[int, PropertyInfo(alias="approvedCode")]
    """Numeric assignment used to determine score approval.

    0 - APPROVAL PENDING (used when score value is 2 or 3); 1 - APPROVED (used when
    score value is 2 or 3); 2 - DISAPPROVED.
    """

    aviation_risk_management_sortie: Annotated[
        Iterable[
            BodyAviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScoreAviationRiskManagementSortie
        ],
        PropertyInfo(alias="aviationRiskManagementSortie"),
    ]
    """Collection of aviation risk management worksheet record score aircraft sorties."""

    ext_score_id: Annotated[str, PropertyInfo(alias="extScoreId")]
    """Optional identifier of the worksheet record score provided by the data source.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    risk_category: Annotated[str, PropertyInfo(alias="riskCategory")]
    """The category of the risk factor."""

    risk_description: Annotated[str, PropertyInfo(alias="riskDescription")]
    """Description of the risk factor."""

    risk_key: Annotated[str, PropertyInfo(alias="riskKey")]
    """Code or identifier of the risk factor category as defined by the data source."""

    risk_name: Annotated[str, PropertyInfo(alias="riskName")]
    """Name of the risk factor."""

    score: int
    """Score of the worksheet record risk factor.

    Value ranges from 0 to 3, where a value of 0 indicates a low and a value of 3
    indicates severe. A value of -1 indicates no score.
    """

    score_remark: Annotated[str, PropertyInfo(alias="scoreRemark")]
    """Remarks and/or comments regarding the worksheet score."""


class BodyAviationRiskManagementWorksheetRecord(TypedDict, total=False):
    mission_date: Required[Annotated[Union[str, date], PropertyInfo(alias="missionDate", format="iso8601")]]
    """Date of the mission in ISO 8601 date-only format (YYYY-MM-DD)."""

    aircraft_mds: Annotated[str, PropertyInfo(alias="aircraftMDS")]
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of the aircraft associated with
    this risk management worksheet record. Intended as, but not constrained to,
    MIL-STD-6016 environment dependent specific type designations.
    """

    approval_pending: Annotated[bool, PropertyInfo(alias="approvalPending")]
    """Flag indicating the worksheet record is pending approval."""

    approved: bool
    """Flag indicating the worksheet record is approved."""

    aviation_risk_management_worksheet_score: Annotated[
        Iterable[BodyAviationRiskManagementWorksheetRecordAviationRiskManagementWorksheetScore],
        PropertyInfo(alias="aviationRiskManagementWorksheetScore"),
    ]
    """Collection of Aviation Risk Management worksheet record scores."""

    disposition_comments: Annotated[str, PropertyInfo(alias="dispositionComments")]
    """
    Comment(s) explaining why the worksheet record has been approved or disapproved.
    """

    ext_record_id: Annotated[str, PropertyInfo(alias="extRecordId")]
    """Optional identifier of the worksheet record provided by the data source.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    itinerary: str
    """Sequential order of itinerary locations associated for the mission."""

    last_updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="lastUpdatedAt", format="iso8601")]
    """
    Timestamp the worksheet record was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    remarks: str
    """Remarks and/or comments regarding the worksheet record."""

    severity_level: Annotated[int, PropertyInfo(alias="severityLevel")]
    """Numeric assignment for the worksheet record severity.

    0 - LOW; 1 - MODERATE; 2 - HIGH; 3 - SEVERE.
    """

    submission_date: Annotated[Union[str, datetime], PropertyInfo(alias="submissionDate", format="iso8601")]
    """
    Timestamp the worksheet record was submitted, in ISO 8601 UTC format with
    millisecond precision.
    """

    tier_number: Annotated[int, PropertyInfo(alias="tierNumber")]
    """Tier number which the mission is being scored as determined by the data source.

    For example, Tier 1 may indicate mission planners, Tier 2 may indicate
    operations personnel, Tier 3 may indicate squadron leadership, and Tier 4 may
    indicate the aircrew.
    """

    total_score: Annotated[int, PropertyInfo(alias="totalScore")]
    """Total score for the worksheet record as defined by the data source.

    Larger values indicate a higher risk level. For example, values between 0-10 may
    indicate a low risk level, where values greater then 40 indicate a severe risk
    level.
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """User identifier associated to the worksheet record."""


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

    id_mission: Required[Annotated[str, PropertyInfo(alias="idMission")]]
    """
    The unique identifier of the mission to which this risk management record is
    assigned.
    """

    source: Required[str]
    """Source of the data."""

    id: str
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    aviation_risk_management_worksheet_record: Annotated[
        Iterable[BodyAviationRiskManagementWorksheetRecord], PropertyInfo(alias="aviationRiskManagementWorksheetRecord")
    ]
    """Collection of Aviation Risk Management Worksheet Records."""

    ext_mission_id: Annotated[str, PropertyInfo(alias="extMissionId")]
    """Optional mission ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    mission_number: Annotated[str, PropertyInfo(alias="missionNumber")]
    """The mission number of the mission associated with this record."""

    org_id: Annotated[str, PropertyInfo(alias="orgId")]
    """Identifier for the organization which this risk management record is evaluated."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    unit_id: Annotated[str, PropertyInfo(alias="unitId")]
    """Identifier for the unit which this risk management record is evaluated."""
