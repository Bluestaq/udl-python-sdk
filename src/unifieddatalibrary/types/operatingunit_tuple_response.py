# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.operatingunit_full import OperatingunitFull

__all__ = ["OperatingunitTupleResponse"]

OperatingunitTupleResponse: TypeAlias = List[OperatingunitFull]
