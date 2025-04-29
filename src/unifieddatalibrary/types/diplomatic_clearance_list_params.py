# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DiplomaticClearanceListParams"]


class DiplomaticClearanceListParams(TypedDict, total=False):
    first_dep_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="firstDepDate", format="iso8601")]]
    """
    The First Departure Date (FDD) the mission is scheduled for departure, in ISO
    8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
