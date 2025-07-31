# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LogisticsDiscrepancyInfosFull"]


class LogisticsDiscrepancyInfosFull(BaseModel):
    closure_time: Optional[datetime] = FieldInfo(alias="closureTime", default=None)
    """
    The discrepancy closure time, in ISO 8601 UTC format with millisecond precision.
    """

    discrepancy_info: Optional[str] = FieldInfo(alias="discrepancyInfo", default=None)
    """The aircraft discrepancy description."""

    jcn: Optional[str] = None
    """Job Control Number of the discrepancy."""

    job_st_time: Optional[datetime] = FieldInfo(alias="jobStTime", default=None)
    """The job start time, in ISO 8601 UTC format with millisecond precision."""
