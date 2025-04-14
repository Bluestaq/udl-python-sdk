# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..ephemeris_set import EphemerisSet

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[EphemerisSet]
