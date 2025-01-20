# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BeamContourCountParams"]


class BeamContourCountParams(TypedDict, total=False):
    id_beam: Required[Annotated[str, PropertyInfo(alias="idBeam")]]
    """ID of the beam."""
