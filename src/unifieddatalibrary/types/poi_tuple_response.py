# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.poi.poi_full import PoiFull

__all__ = ["PoiTupleResponse"]

PoiTupleResponse: TypeAlias = List[PoiFull]
