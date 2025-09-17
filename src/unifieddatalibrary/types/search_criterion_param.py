# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Literal, TypeAlias, TypedDict, TypeAliasType

from .._compat import PYDANTIC_V1

__all__ = ["SearchCriterionParam", "ScsSearchFieldCriterion"]


class ScsSearchFieldCriterion(TypedDict, total=False):
    field: str
    """The field to search on (e.g., attachment.content, createdBy)."""

    operator: Literal["EXACT_MATCH", "WILDCARD", "FUZZY", "GTE", "LTE", "GT", "LT"]
    """Supported search operators"""

    value: str
    """The value to compare against (e.g., The Great Gatsby)"""


if TYPE_CHECKING or not PYDANTIC_V1:
    SearchCriterionParam = TypeAliasType(
        "SearchCriterionParam", Union[ScsSearchFieldCriterion, "SearchLogicalCriterionParam"]
    )
else:
    SearchCriterionParam: TypeAlias = Union[ScsSearchFieldCriterion, "SearchLogicalCriterionParam"]

from .search_logical_criterion_param import SearchLogicalCriterionParam
