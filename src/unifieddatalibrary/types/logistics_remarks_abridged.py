# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LogisticsRemarksAbridged"]


class LogisticsRemarksAbridged(BaseModel):
    last_changed: Optional[datetime] = FieldInfo(alias="lastChanged", default=None)
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: Optional[str] = None
    """Text of the remark."""

    username: Optional[str] = None
    """User who published the remark."""
