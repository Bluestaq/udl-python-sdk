# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GnssObservationsetCountParams"]


class GnssObservationsetCountParams(TypedDict, total=False):
    ts: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Observation Time, in ISO8601 UTC format with microsecond precision.

    This timestamp applies to all observations within the set.
    (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
