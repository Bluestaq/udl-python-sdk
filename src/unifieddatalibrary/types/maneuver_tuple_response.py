# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

__all__ = ["ManeuverTupleResponse"]

ManeuverTupleResponse: TypeAlias = List["ManeuverFull"]

from .udl.maneuver.maneuver_full import ManeuverFull
