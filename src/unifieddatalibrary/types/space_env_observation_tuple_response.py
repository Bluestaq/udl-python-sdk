# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .space_env_observation.space_env_observation_full import SpaceEnvObservationFull

__all__ = ["SpaceEnvObservationTupleResponse"]

SpaceEnvObservationTupleResponse: TypeAlias = List[SpaceEnvObservationFull]
