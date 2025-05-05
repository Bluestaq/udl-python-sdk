# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaiUtcTupleParams"]


class TaiUtcTupleParams(TypedDict, total=False):
    adjustment_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="adjustmentDate", format="iso8601")]]
    """Effective date/time for the leap second adjustment.

    Must be a unique value across all TAIUTC datasets. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    columns: Required[str]
    """
    Comma-separated list of valid field names for this data type to be returned in
    the response. Only the fields specified will be returned as well as the
    classification marking of the data, if applicable. See the ‘queryhelp’ operation
    for a complete list of possible fields.
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
