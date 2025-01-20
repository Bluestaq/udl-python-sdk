# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .batterydetails_abridged import BatterydetailsAbridged

__all__ = ["BatterydetailListResponse"]

BatterydetailListResponse: TypeAlias = List[BatterydetailsAbridged]
