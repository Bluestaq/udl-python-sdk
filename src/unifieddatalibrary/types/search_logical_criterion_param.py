# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["SearchLogicalCriterionParam"]


class SearchLogicalCriterionParam(TypedDict, total=False):
    criteria: Iterable["SearchCriterionParam"]
    """List of search criteria to combine"""

    operator: Literal["AND", "OR", "NOT"]
    """Supported search operators"""


from .search_criterion_param import SearchCriterionParam
