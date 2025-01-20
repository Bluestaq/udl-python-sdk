# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CrewpaperUnpublishParams"]


class CrewpaperUnpublishParams(TypedDict, total=False):
    ids: Required[str]
    """Comma-separated list of AircraftSortie IDs where Crew Papers are unpublished."""
