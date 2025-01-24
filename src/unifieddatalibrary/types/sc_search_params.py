# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScSearchParams"]


class ScSearchParams(TypedDict, total=False):
    path: Required[str]
    """The path to search from"""

    count: int
    """Number of items per page"""

    offset: int
    """First result to return"""

    content_criteria: Annotated[str, PropertyInfo(alias="contentCriteria")]

    meta_data_criteria: Annotated[Dict[str, List[str]], PropertyInfo(alias="metaDataCriteria")]

    non_range_criteria: Annotated[Dict[str, List[str]], PropertyInfo(alias="nonRangeCriteria")]

    range_criteria: Annotated[Dict[str, List[str]], PropertyInfo(alias="rangeCriteria")]

    search_after: Annotated[str, PropertyInfo(alias="searchAfter")]
