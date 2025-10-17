# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2SearchParams"]


class V2SearchParams(TypedDict, total=False):
    order: str
    """The order in which entries should be sorted."""

    search_after: Annotated[str, PropertyInfo(alias="searchAfter")]
    """
    The starting point for pagination results, usually set to the value of the
    SEARCH_AFTER header returned in the previous request.
    """

    size: int
    """The number of results to retrieve."""

    sort: str
    """The field on which to sort entries."""

    query: "SearchCriterionParam"
    """
    A search criterion, which can be a simple field comparison or a logical
    combination of other criteria.
    """


from ..search_criterion_param import SearchCriterionParam
