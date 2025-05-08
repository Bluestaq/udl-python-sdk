# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HistoryCountParams"]


class HistoryCountParams(TypedDict, total=False):
    ob_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="obTime", format="iso8601")]]
    """Ob detection time in ISO 8601 UTC, up to microsecond precision.

    Consumers should contact the provider for details on their obTime
    specifications. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
