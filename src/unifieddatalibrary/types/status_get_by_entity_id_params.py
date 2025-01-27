# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StatusGetByEntityIDParams"]


class StatusGetByEntityIDParams(TypedDict, total=False):
    id_entity_2: Required[Annotated[str, PropertyInfo(alias="idEntity")]]
    """The entity id to find the list of statuses for."""
