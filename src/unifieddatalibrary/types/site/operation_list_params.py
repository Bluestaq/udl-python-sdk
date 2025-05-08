# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OperationListParams"]


class OperationListParams(TypedDict, total=False):
    id_site: Required[Annotated[str, PropertyInfo(alias="idSite")]]
    """The ID of the parent site."""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
