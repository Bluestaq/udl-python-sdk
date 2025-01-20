# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .battery_abridged import BatteryAbridged

__all__ = ["BatteryListResponse"]

BatteryListResponse: TypeAlias = List[BatteryAbridged]
