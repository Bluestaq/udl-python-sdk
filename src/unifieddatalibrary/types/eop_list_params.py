# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EopListParams"]


class EopListParams(TypedDict, total=False):
    eop_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="eopDate", format="iso8601")]]
    """Effective date/time for the EOP values in ISO8601 UTC format.

    The values could be current or predicted. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
