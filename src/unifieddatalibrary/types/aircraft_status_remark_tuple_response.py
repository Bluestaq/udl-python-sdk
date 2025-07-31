# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.aircraftstatusremark_full import AircraftstatusremarkFull

__all__ = ["AircraftStatusRemarkTupleResponse"]

AircraftStatusRemarkTupleResponse: TypeAlias = List[AircraftstatusremarkFull]
