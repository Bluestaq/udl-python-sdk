# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.ephemeris_full import EphemerisFull

__all__ = ["EphemerisTupleResponse"]

EphemerisTupleResponse: TypeAlias = List[EphemerisFull]
