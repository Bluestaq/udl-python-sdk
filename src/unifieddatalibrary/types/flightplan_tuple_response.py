# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.flight_plan_full import FlightPlanFull

__all__ = ["FlightplanTupleResponse"]

FlightplanTupleResponse: TypeAlias = List[FlightPlanFull]
