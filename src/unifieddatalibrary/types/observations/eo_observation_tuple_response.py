# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .eo_observations.eo_observation_full import EoObservationFull

__all__ = ["EoObservationTupleResponse"]

EoObservationTupleResponse: TypeAlias = List[EoObservationFull]
