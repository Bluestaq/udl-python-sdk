# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .air_tasking_order_full import AirTaskingOrderFull

__all__ = ["AirTaskingOrderTupleResponse"]

AirTaskingOrderTupleResponse: TypeAlias = List[AirTaskingOrderFull]
