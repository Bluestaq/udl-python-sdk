# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FixedPointFull"]


class FixedPointFull(BaseModel):
    latitude: float
    """WGS84 latitude of a point, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    longitude: float
    """WGS84 longitude of a point, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    height: Optional[float] = None
    """Point height as measured from sea level, ranging from -300 to 1000 kilometers."""
