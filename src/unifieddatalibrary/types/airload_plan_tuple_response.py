# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.airloadplan_full import AirloadplanFull

__all__ = ["AirloadPlanTupleResponse"]

AirloadPlanTupleResponse: TypeAlias = List[AirloadplanFull]
