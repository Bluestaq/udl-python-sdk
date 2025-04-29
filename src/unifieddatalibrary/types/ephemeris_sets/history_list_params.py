# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryListParams"]


class HistoryListParams(TypedDict, total=False):
    columns: str
    """optional, fields for retrieval.

    When omitted, ALL fields are assumed. See the queryhelp operation
    (/udl/&lt;datatype&gt;/queryhelp) for more details on valid query fields that
    can be selected.
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    point_end_time: Annotated[Union[str, datetime], PropertyInfo(alias="pointEndTime", format="iso8601")]
    """
    (One or more of fields 'pointEndTime, pointStartTime' are required.) End
    time/last time point of the ephemeris, in ISO 8601 UTC format.
    (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    point_start_time: Annotated[Union[str, datetime], PropertyInfo(alias="pointStartTime", format="iso8601")]
    """
    (One or more of fields 'pointEndTime, pointStartTime' are required.) Start
    time/first time point of the ephemeris, in ISO 8601 UTC format.
    (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """
