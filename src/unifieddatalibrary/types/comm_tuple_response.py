# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.comm_full import CommFull

__all__ = ["CommTupleResponse"]

CommTupleResponse: TypeAlias = List[CommFull]
