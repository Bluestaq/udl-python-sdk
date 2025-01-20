# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

__all__ = ["ConjunctionGetHistoryResponse"]

ConjunctionGetHistoryResponse: TypeAlias = List["ConjunctionFull"]

from .conjunction_full import ConjunctionFull
