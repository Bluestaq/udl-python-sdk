# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.event_evolution_full import EventEvolutionFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[EventEvolutionFull]
