# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryCountParams"]


class HistoryCountParams(TypedDict, total=False):
    id_sortie: Required[Annotated[str, PropertyInfo(alias="idSortie")]]
    """
    Unique identifier of the Aircraft Sortie associated with this prior permission
    required (PPR) record.
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
