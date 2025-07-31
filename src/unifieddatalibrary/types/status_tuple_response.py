# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.status_full import StatusFull

__all__ = ["StatusTupleResponse"]

StatusTupleResponse: TypeAlias = List[StatusFull]
