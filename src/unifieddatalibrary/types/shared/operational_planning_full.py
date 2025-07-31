# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OperationalPlanningFull"]


class OperationalPlanningFull(BaseModel):
    op_end_date: Optional[datetime] = FieldInfo(alias="opEndDate", default=None)
    """
    The end date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_last_changed_by: Optional[str] = FieldInfo(alias="opLastChangedBy", default=None)
    """
    The name of the person who made the most recent change made to this
    OperationalPlanning data.
    """

    op_last_changed_date: Optional[datetime] = FieldInfo(alias="opLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this OperationalPlanning data, in
    ISO8601 UTC format with millisecond precision.
    """

    op_remark: Optional[str] = FieldInfo(alias="opRemark", default=None)
    """Remark text regarding this operation planning."""

    op_source: Optional[str] = FieldInfo(alias="opSource", default=None)
    """The person, unit, organization, etc. responsible for this operation planning."""

    op_start_date: Optional[datetime] = FieldInfo(alias="opStartDate", default=None)
    """
    The start date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_status: Optional[str] = FieldInfo(alias="opStatus", default=None)
    """The status of this operational planning."""
