# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .swir.swir_full import SwirFull

__all__ = ["SwirTupleResponse"]

SwirTupleResponse: TypeAlias = List[SwirFull]
