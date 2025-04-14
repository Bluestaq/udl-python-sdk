# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.geostatus.geo_status_full import GeoStatusFull

__all__ = ["GeostatusTupleResponse"]

GeostatusTupleResponse: TypeAlias = List[GeoStatusFull]
