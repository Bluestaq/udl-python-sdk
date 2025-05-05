# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .geo_status.geo_status_full import GeoStatusFull

__all__ = ["GeoStatusTupleResponse"]

GeoStatusTupleResponse: TypeAlias = List[GeoStatusFull]
