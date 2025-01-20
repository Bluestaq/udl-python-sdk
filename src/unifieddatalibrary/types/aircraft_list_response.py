# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .aircraft_abridged import AircraftAbridged

__all__ = ["AircraftListResponse"]

AircraftListResponse: TypeAlias = List[AircraftAbridged]
