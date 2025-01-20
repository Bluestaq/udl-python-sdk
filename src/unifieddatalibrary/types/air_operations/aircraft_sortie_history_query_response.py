# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .aircraftsortie_full import AircraftsortieFull

__all__ = ["AircraftSortieHistoryQueryResponse"]

AircraftSortieHistoryQueryResponse: TypeAlias = List[AircraftsortieFull]
