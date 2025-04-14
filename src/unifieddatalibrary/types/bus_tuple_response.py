# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .bus_full import BusFull

__all__ = ["BusTupleResponse"]

BusTupleResponse: TypeAlias = List[BusFull]
