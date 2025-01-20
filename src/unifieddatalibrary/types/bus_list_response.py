# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .bus_abridged import BusAbridged

__all__ = ["BusListResponse"]

BusListResponse: TypeAlias = List[BusAbridged]
