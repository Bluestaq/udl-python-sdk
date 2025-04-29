# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LinkStatusTupleParams"]


class LinkStatusTupleParams(TypedDict, total=False):
    columns: Required[str]
    """
    Comma-separated list of valid field names for this data type to be returned in
    the response. Only the fields specified will be returned as well as the
    classification marking of the data, if applicable. See the ‘queryhelp’ operation
    for a complete list of possible fields.
    """

    created_at: Annotated[Union[str, date], PropertyInfo(alias="createdAt", format="iso8601")]
    """
    (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
    Time the row was created in the database, auto-populated by the system.
    (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    link_start_time: Annotated[Union[str, datetime], PropertyInfo(alias="linkStartTime", format="iso8601")]
    """
    (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
    The link establishment time, or the time that the link becomes available for
    use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    link_stop_time: Annotated[Union[str, datetime], PropertyInfo(alias="linkStopTime", format="iso8601")]
    """
    (One or more of fields 'createdAt, linkStartTime, linkStopTime' are required.)
    The link termination time, or the time that the link becomes unavailable for
    use, in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
