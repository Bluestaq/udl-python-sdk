# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.antenna_full import AntennaFull

__all__ = ["AntennaTupleResponse"]

AntennaTupleResponse: TypeAlias = List[AntennaFull]
