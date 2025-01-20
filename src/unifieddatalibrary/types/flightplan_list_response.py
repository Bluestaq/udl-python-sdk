# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .flight_plan_abridged import FlightPlanAbridged

__all__ = ["FlightplanListResponse"]

FlightplanListResponse: TypeAlias = List[FlightPlanAbridged]
