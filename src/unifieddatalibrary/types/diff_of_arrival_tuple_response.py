# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .tdoa_fdoa.diffofarrival_full import DiffofarrivalFull

__all__ = ["DiffOfArrivalTupleResponse"]

DiffOfArrivalTupleResponse: TypeAlias = List[DiffofarrivalFull]
