# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationdetailFindBySourceParams"]


class OrganizationdetailFindBySourceParams(TypedDict, total=False):
    name: Required[str]
    """Organization details name."""

    source: Required[str]
    """The source of the OrganizationDetails records to find."""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
