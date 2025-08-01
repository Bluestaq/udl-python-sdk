# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.solar_array_full import SolarArrayFull

__all__ = ["SolarArrayTupleResponse"]

SolarArrayTupleResponse: TypeAlias = List[SolarArrayFull]
