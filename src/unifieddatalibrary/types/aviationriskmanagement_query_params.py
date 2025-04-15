# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AviationriskmanagementQueryParams"]


class AviationriskmanagementQueryParams(TypedDict, total=False):
    id_mission: Required[Annotated[str, PropertyInfo(alias="idMission")]]
    """
    The unique identifier of the mission to which this risk management record is
    assigned.
    """
