# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..udl.sensorplan.sensorplan_full import SensorplanFull

__all__ = ["HistoryRetrieveResponse"]

HistoryRetrieveResponse: TypeAlias = List[SensorplanFull]
