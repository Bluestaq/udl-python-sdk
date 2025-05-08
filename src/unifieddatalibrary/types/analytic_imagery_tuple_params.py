# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AnalyticImageryTupleParams"]


class AnalyticImageryTupleParams(TypedDict, total=False):
    columns: Required[str]
    """
    Comma-separated list of valid field names for this data type to be returned in
    the response. Only the fields specified will be returned as well as the
    classification marking of the data, if applicable. See the ‘queryhelp’ operation
    for a complete list of possible fields.
    """

    msg_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="msgTime", format="iso8601")]]
    """
    The message time of this image record, in ISO8601 UTC format with millisecond
    precision. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
