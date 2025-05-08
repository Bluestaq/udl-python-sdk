# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SigactListParams"]


class SigactListParams(TypedDict, total=False):
    report_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="reportDate", format="iso8601")]]
    """Date of the report or filing. (YYYY-MM-DDTHH:MM:SS.sssZ)"""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
