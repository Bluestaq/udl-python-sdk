# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryCountParams"]


class HistoryCountParams(TypedDict, total=False):
    event_start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="eventStartTime", format="iso8601")]]
    """Maneuver event start time in ISO 8601 UTC with microsecond precision.

    For maneuvers without start and end times, the start time is considered to be
    the maneuver event time. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
