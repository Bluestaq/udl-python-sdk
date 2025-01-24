# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

__all__ = ["GeostatusTupleResponse"]

GeostatusTupleResponse: TypeAlias = List["GeoStatusFull"]

from .udl.geostatus.geo_status_full import GeoStatusFull
