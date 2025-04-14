# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.sarobservation.sarobservation_full import SarobservationFull

__all__ = ["SarobservationTupleResponse"]

SarobservationTupleResponse: TypeAlias = List[SarobservationFull]
