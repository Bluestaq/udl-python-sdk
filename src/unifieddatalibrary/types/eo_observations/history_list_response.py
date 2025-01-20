# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List["EoObservationFull"]

from .eo_observation_full import EoObservationFull
