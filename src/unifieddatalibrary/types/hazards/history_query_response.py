# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..udl.hazard.hazard_full import HazardFull

__all__ = ["HistoryQueryResponse"]

HistoryQueryResponse: TypeAlias = List[HazardFull]
