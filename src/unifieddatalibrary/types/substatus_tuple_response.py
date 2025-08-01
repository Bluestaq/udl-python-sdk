# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.sub_status_full import SubStatusFull

__all__ = ["SubstatusTupleResponse"]

SubstatusTupleResponse: TypeAlias = List[SubStatusFull]
