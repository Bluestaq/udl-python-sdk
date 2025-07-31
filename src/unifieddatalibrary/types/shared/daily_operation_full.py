# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .operating_hours_full import OperatingHoursFull

__all__ = ["DailyOperationFull"]


class DailyOperationFull(BaseModel):
    day_of_week: Optional[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]] = (
        FieldInfo(alias="dayOfWeek", default=None)
    )
    """The day of the week to which this operational information pertains."""

    operating_hours: Optional[List[OperatingHoursFull]] = FieldInfo(alias="operatingHours", default=None)
    """
    A collection containing the operational start and stop times scheduled for the
    day of the week specified.
    """

    operation_name: Optional[str] = FieldInfo(alias="operationName", default=None)
    """The name or type of operation to which this information pertains."""

    ophrs_last_changed_by: Optional[str] = FieldInfo(alias="ophrsLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this DailyOperation
    data.
    """

    ophrs_last_changed_date: Optional[datetime] = FieldInfo(alias="ophrsLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this DailyOperation data, in ISO
    8601 UTC format with millisecond precision.
    """
