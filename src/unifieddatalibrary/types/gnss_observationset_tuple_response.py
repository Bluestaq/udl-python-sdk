# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .gnss_observationset.gnss_observation_set_full import GnssObservationSetFull

__all__ = ["GnssObservationsetTupleResponse"]

GnssObservationsetTupleResponse: TypeAlias = List[GnssObservationSetFull]
