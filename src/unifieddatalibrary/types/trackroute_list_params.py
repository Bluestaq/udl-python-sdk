# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrackrouteListParams"]


class TrackrouteListParams(TypedDict, total=False):
    last_update_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="lastUpdateDate", format="iso8601")]]
    """
    The last updated date of the track route in ISO 8601 UTC format with millisecond
    precision. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """
