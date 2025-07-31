# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LogisticsStocksFull"]


class LogisticsStocksFull(BaseModel):
    quantity: Optional[int] = None
    """The quantity of available parts needed from sourceICAO."""

    source_icao: Optional[str] = FieldInfo(alias="sourceICAO", default=None)
    """The ICAO code for the primary location with available parts."""

    stock_check_time: Optional[datetime] = FieldInfo(alias="stockCheckTime", default=None)
    """
    The datetime when the parts were sourced, in ISO 8601 UTC format with
    millisecond precision.
    """

    stock_poc: Optional[str] = FieldInfo(alias="stockPOC", default=None)
    """The point of contact at the sourced location."""
