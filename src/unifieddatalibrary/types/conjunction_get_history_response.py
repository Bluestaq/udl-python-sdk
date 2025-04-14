# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .conjunction_full import ConjunctionFull

__all__ = ["ConjunctionGetHistoryResponse"]

ConjunctionGetHistoryResponse: TypeAlias = List[ConjunctionFull]
