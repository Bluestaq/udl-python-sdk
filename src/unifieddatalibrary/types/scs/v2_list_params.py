# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2ListParams"]


class V2ListParams(TypedDict, total=False):
    path: Required[str]
    """The base path to list."""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

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
