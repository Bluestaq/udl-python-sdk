# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .battery_full import BatteryFull

__all__ = ["BatteryTupleResponse"]

BatteryTupleResponse: TypeAlias = List[BatteryFull]
