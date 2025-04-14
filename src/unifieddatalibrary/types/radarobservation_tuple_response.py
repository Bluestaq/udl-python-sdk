# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.radarobservation.radarobservation_full import RadarobservationFull

__all__ = ["RadarobservationTupleResponse"]

RadarobservationTupleResponse: TypeAlias = List[RadarobservationFull]
