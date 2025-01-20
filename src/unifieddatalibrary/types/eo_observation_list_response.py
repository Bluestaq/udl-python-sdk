# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .eo_observation_abridged import EoObservationAbridged

__all__ = ["EoObservationListResponse"]

EoObservationListResponse: TypeAlias = List[EoObservationAbridged]
