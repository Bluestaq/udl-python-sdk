# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .space_env_observation_full import SpaceEnvObservationFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[SpaceEnvObservationFull]
