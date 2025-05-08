# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
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

    effective_date: Annotated[Union[str, datetime], PropertyInfo(alias="effectiveDate", format="iso8601")]
    """
    (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
    the data was received and processed from the source. Typically a source provides
    solar data for a date window with each transmission including past, present, and
    future predicted values. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

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

    sgi_date: Annotated[Union[str, datetime], PropertyInfo(alias="sgiDate", format="iso8601")]
    """
    (One or more of fields 'effectiveDate, sgiDate' are required.) ISO8601 UTC Time
    of the index value. This could be a past, current, or future predicted value.
    Note: sgiDate defines the start time of the time window for this data record.
    (YYYY-MM-DDTHH:MM:SS.sssZ)
    """
