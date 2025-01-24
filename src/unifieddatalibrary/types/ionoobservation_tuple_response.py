# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.ionoobservation.iono_observation_full import IonoObservationFull

__all__ = ["IonoobservationTupleResponse"]

IonoobservationTupleResponse: TypeAlias = List[IonoObservationFull]
