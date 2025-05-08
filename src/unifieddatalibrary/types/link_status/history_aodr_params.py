# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryAodrParams"]


class HistoryAodrParams(TypedDict, total=False):
    columns: str
    """optional, fields for retrieval.

    When omitted, ALL fields are assumed. See the queryhelp operation
    (/udl/&lt;datatype&gt;/queryhelp) for more details on valid query fields that
    can be selected.
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

    notification: str
    """optional, notification method for the created file link.

    When omitted, EMAIL is assumed. Current valid values are: EMAIL, SMS.
    """

    output_delimiter: Annotated[str, PropertyInfo(alias="outputDelimiter")]
    """optional, field delimiter when the created file is not JSON.

    Must be a single character chosen from this set: (',', ';', ':', '|'). When
    omitted, "," is used. It is strongly encouraged that your field delimiter be a
    character unlikely to occur within the data.
    """

    output_format: Annotated[str, PropertyInfo(alias="outputFormat")]
    """optional, output format for the file.

    When omitted, JSON is assumed. Current valid values are: JSON and CSV.
    """
