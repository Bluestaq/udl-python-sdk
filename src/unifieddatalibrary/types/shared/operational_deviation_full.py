# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OperationalDeviationFull"]


class OperationalDeviationFull(BaseModel):
    affected_aircraft_mds: Optional[str] = FieldInfo(alias="affectedAircraftMDS", default=None)
    """
    The Model Design Series (MDS) designation of the aircraft affected by this
    operational deviation.
    """

    affected_mog: Optional[int] = FieldInfo(alias="affectedMOG", default=None)
    """
    The maximum on ground (MOG) number for aircraft affected by this operational
    deviation.
    """

    aircraft_on_ground_time: Optional[str] = FieldInfo(alias="aircraftOnGroundTime", default=None)
    """On ground time for aircraft affected by this operational deviation."""

    crew_rest_time: Optional[str] = FieldInfo(alias="crewRestTime", default=None)
    """Rest time for crew affected by this operational deviation."""

    od_last_changed_by: Optional[str] = FieldInfo(alias="odLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this
    OperationalDeviation data.
    """

    od_last_changed_date: Optional[datetime] = FieldInfo(alias="odLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this OperationalDeviation data,
    in ISO 8601 UTC format with millisecond precision.
    """

    od_remark: Optional[str] = FieldInfo(alias="odRemark", default=None)
    """Text remark regarding this operational deviation."""
