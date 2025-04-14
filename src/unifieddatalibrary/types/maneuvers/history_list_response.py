# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..udl.maneuver.maneuver_full import ManeuverFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[ManeuverFull]
