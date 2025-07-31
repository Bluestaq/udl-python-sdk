# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MaximumOnGroundFull"]


class MaximumOnGroundFull(BaseModel):
    aircraft_mds: Optional[str] = FieldInfo(alias="aircraftMDS", default=None)
    """
    The Model Design Series (MDS) designation of the aircraft to which this maximum
    on ground (MOG) data pertains.
    """

    contingency_mog: Optional[int] = FieldInfo(alias="contingencyMOG", default=None)
    """
    Maximum on ground (MOG) number of contingent aircraft based on spacing and
    manpower, for the aircraft type specified.
    """

    mog_last_changed_by: Optional[str] = FieldInfo(alias="mogLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this maximum on ground
    data.
    """

    mog_last_changed_date: Optional[datetime] = FieldInfo(alias="mogLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this maximum on ground data, in
    ISO 8601 UTC format with millisecond precision.
    """

    wide_parking_mog: Optional[int] = FieldInfo(alias="wideParkingMOG", default=None)
    """
    Maximum on ground (MOG) number of parking wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """

    wide_working_mog: Optional[int] = FieldInfo(alias="wideWorkingMOG", default=None)
    """
    Maximum on ground (MOG) number of working wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """
