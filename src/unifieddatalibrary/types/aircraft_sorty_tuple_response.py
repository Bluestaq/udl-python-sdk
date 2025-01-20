# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .air_operations.aircraftsortie_full import AircraftsortieFull

__all__ = ["AircraftSortyTupleResponse"]

AircraftSortyTupleResponse: TypeAlias = List[AircraftsortieFull]
