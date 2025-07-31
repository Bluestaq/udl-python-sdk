# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PathwayFull"]


class PathwayFull(BaseModel):
    pw_definition: Optional[str] = FieldInfo(alias="pwDefinition", default=None)
    """Text defining this pathway from its constituent parts."""

    pw_last_changed_by: Optional[str] = FieldInfo(alias="pwLastChangedBy", default=None)
    """The name of the person who made the most recent change to this Pathway data."""

    pw_last_changed_date: Optional[datetime] = FieldInfo(alias="pwLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this Pathway data, in ISO 8601
    UTC format with millisecond precision.
    """

    pw_type: Optional[str] = FieldInfo(alias="pwType", default=None)
    """The type of paths that constitute this pathway."""

    pw_usage: Optional[str] = FieldInfo(alias="pwUsage", default=None)
    """The intended use of this pathway."""
