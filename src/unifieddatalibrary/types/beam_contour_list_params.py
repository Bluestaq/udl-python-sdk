# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BeamContourListParams"]


class BeamContourListParams(TypedDict, total=False):
    id_beam: Required[Annotated[str, PropertyInfo(alias="idBeam")]]
    """ID of the beam."""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
