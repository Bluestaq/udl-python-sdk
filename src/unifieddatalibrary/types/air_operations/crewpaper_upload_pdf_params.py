# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["CrewpaperUploadPdfParams"]


class CrewpaperUploadPdfParams(TypedDict, total=False):
    aircraft_sortie_ids: Required[Annotated[str, PropertyInfo(alias="aircraftSortieIds")]]
    """Comma-separated list of AircraftSortie IDs the Crew Papers are being added to."""

    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """classificationMarking of the Crew Papers."""

    paper_status: Required[
        Annotated[Literal["PUBLISHED", "DELETED", "UPDATED", "READ"], PropertyInfo(alias="paperStatus")]
    ]
    """The status of the supporting document."""

    papers_version: Required[Annotated[str, PropertyInfo(alias="papersVersion")]]
    """The version number of the crew paper."""

    body: Required[FileTypes]
