# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SensormaintenanceListParams"]


class SensormaintenanceListParams(TypedDict, total=False):
    end_time: Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]
    """
    (One or more of fields 'endTime, startTime' are required.) The planned outage
    end time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """

    start_time: Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]
    """
    (One or more of fields 'endTime, startTime' are required.) The planned outage
    start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """
