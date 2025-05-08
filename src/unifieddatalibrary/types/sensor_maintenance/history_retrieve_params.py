# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryRetrieveParams"]


class HistoryRetrieveParams(TypedDict, total=False):
    columns: str
    """optional, fields for retrieval.

    When omitted, ALL fields are assumed. See the queryhelp operation
    (/udl/&lt;datatype&gt;/queryhelp) for more details on valid query fields that
    can be selected.
    """

    end_time: Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]
    """
    (One or more of fields 'endTime, startTime' are required.) The planned outage
    end time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    start_time: Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]
    """
    (One or more of fields 'endTime, startTime' are required.) The planned outage
    start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """
