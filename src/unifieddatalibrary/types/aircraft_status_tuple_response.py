# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.aircraftstatus_full import AircraftstatusFull

__all__ = ["AircraftStatusTupleResponse"]

AircraftStatusTupleResponse: TypeAlias = List[AircraftstatusFull]
