# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StatusGetByEntityTypeParams"]


class StatusGetByEntityTypeParams(TypedDict, total=False):
    query_entity_type: Required[Annotated[str, PropertyInfo(alias="entityType")]]
    """The entity type of the Status to find."""
