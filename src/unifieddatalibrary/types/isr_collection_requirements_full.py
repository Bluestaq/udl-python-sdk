# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .isr_collection_critical_times_full import IsrCollectionCriticalTimesFull
from .isr_collection_exploitation_requirement_full import IsrCollectionExploitationRequirementFull

__all__ = ["IsrCollectionRequirementsFull"]


class IsrCollectionRequirementsFull(BaseModel):
    id: Optional[str] = None
    """Collection Requirement Unique Identifier."""

    country: Optional[str] = None
    """Country code of the collection requirement.

    A Country may represent countries, multi-national consortiums, and international
    organizations.
    """

    crid_numbers: Optional[str] = FieldInfo(alias="cridNumbers", default=None)
    """Collection Requirement Unique Identifier."""

    critical_times: Optional[IsrCollectionCriticalTimesFull] = FieldInfo(alias="criticalTimes", default=None)

    emphasized: Optional[bool] = None
    """Is this collection requirement an emphasized/critical requirement."""

    exploitation_requirement: Optional[IsrCollectionExploitationRequirementFull] = FieldInfo(
        alias="exploitationRequirement", default=None
    )

    hash: Optional[str] = None
    """Encryption hashing algorithm."""

    intel_discipline: Optional[str] = FieldInfo(alias="intelDiscipline", default=None)
    """Primary type of intelligence to be collected for this requirement."""

    is_prism_cr: Optional[bool] = FieldInfo(alias="isPrismCr", default=None)
    """Is this collection request for the Prism system?."""

    operation: Optional[str] = None
    """Human readable name for this operation."""

    priority: Optional[float] = None
    """1-n priority for this collection requirement."""

    recon_survey: Optional[str] = FieldInfo(alias="reconSurvey", default=None)
    """Reconnaissance Survey information the operator needs."""

    record_id: Optional[str] = FieldInfo(alias="recordId", default=None)
    """Record id."""

    region: Optional[str] = None
    """Region of the collection requirement."""

    secondary: Optional[bool] = None
    """Sub category of primary intelligence to be collected for this requirement."""

    special_com_guidance: Optional[str] = FieldInfo(alias="specialComGuidance", default=None)
    """
    Free text field for the user to specify special instructions needed for this
    collection.
    """

    start: Optional[datetime] = None
    """Start time for this requirement, should be within the mission time window."""

    stop: Optional[datetime] = None
    """Stop time for this requirement, should be within the mission time window."""

    subregion: Optional[str] = None
    """Subregion of the collection requirement."""

    supported_unit: Optional[str] = FieldInfo(alias="supportedUnit", default=None)
    """
    The name of the military unit that this assigned collection requirement will
    support.
    """

    target_list: Optional[List[str]] = FieldInfo(alias="targetList", default=None)
    """Array of POI Id's for the targets being tasked."""

    type: Optional[str] = None
    """Type collection this requirement applies to."""
