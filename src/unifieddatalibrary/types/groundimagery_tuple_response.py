# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.groundimagery.ground_imagery_full import GroundImageryFull

__all__ = ["GroundimageryTupleResponse"]

GroundimageryTupleResponse: TypeAlias = List[GroundImageryFull]
