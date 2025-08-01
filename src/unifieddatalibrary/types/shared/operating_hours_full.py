# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OperatingHoursFull"]


class OperatingHoursFull(BaseModel):
    op_start_time: Optional[str] = FieldInfo(alias="opStartTime", default=None)
    """The Zulu (UTC) operational start time, expressed in ISO 8601 format as HH:MM."""

    op_stop_time: Optional[str] = FieldInfo(alias="opStopTime", default=None)
    """The Zulu (UTC) operational stop time, expressed in ISO 8601 format as HH:MM."""
