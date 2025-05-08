# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .soi_observation_set.soi_observation_set_full import SoiObservationSetFull

__all__ = ["SoiObservationSetTupleResponse"]

SoiObservationSetTupleResponse: TypeAlias = List[SoiObservationSetFull]
