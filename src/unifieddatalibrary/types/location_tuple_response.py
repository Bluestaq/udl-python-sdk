# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .location_full import LocationFull

__all__ = ["LocationTupleResponse"]

LocationTupleResponse: TypeAlias = List[LocationFull]
