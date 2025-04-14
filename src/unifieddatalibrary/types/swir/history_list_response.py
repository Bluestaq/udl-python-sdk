# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .swir_full import SwirFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[SwirFull]
