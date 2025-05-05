# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .state_vector_full import StateVectorFull

__all__ = ["StateVectorTupleResponse"]

StateVectorTupleResponse: TypeAlias = List[StateVectorFull]
