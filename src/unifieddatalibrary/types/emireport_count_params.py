# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmireportCountParams"]


class EmireportCountParams(TypedDict, total=False):
    report_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="reportTime", format="iso8601")]]
    """
    The reporting time of this EMI Report record, in ISO 8601 UTC format, with
    millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
