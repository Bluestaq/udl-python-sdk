# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..air_operations.diplomaticclearance_full import DiplomaticclearanceFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[DiplomaticclearanceFull]
