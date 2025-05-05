# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NavigationalObstructionTupleParams"]


class NavigationalObstructionTupleParams(TypedDict, total=False):
    columns: Required[str]
    """
    Comma-separated list of valid field names for this data type to be returned in
    the response. Only the fields specified will be returned as well as the
    classification marking of the data, if applicable. See the ‘queryhelp’ operation
    for a complete list of possible fields.
    """

    cycle_date: Annotated[Union[str, date], PropertyInfo(alias="cycleDate", format="iso8601")]
    """
    (One or more of fields 'cycleDate, obstacleId' are required.) Start date of this
    obstruction data set's currency, in ISO 8601 date-only format. (YYYY-MM-DD)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    obstacle_id: Annotated[str, PropertyInfo(alias="obstacleId")]
    """
    (One or more of fields 'cycleDate, obstacleId' are required.) The ID of this
    obstacle.
    """
