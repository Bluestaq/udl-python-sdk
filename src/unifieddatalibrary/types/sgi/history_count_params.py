# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryCountParams"]


class HistoryCountParams(TypedDict, total=False):
    effective_date: Annotated[Union[str, datetime], PropertyInfo(alias="effectiveDate", format="iso8601")]
    """
    (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
    the data was received and processed from the source. Typically a source provides
    solar data for a date window with each transmission including past, present, and
    future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    sgi_date: Annotated[Union[str, datetime], PropertyInfo(alias="sgiDate", format="iso8601")]
    """
    (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
    of the index value. This could be a past, current, or future predicted value.
    Note: sgiDate defines the start time of the time window for this data record.
    (YYYY-MM-DDTHH:MM:SS.sssZ)
    """
