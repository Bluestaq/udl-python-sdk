# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AviationRiskManagementQueryParams"]


class AviationRiskManagementQueryParams(TypedDict, total=False):
    id_mission: Required[Annotated[str, PropertyInfo(alias="idMission")]]
    """
    The unique identifier of the mission to which this risk management record is
    assigned.
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
