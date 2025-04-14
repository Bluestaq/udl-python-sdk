# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .aircraft_full import AircraftFull

__all__ = ["AircraftTupleQueryResponse"]

AircraftTupleQueryResponse: TypeAlias = List[AircraftFull]
