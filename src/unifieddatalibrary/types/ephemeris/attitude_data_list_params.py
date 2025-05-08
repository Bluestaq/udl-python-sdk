# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AttitudeDataListParams"]


class AttitudeDataListParams(TypedDict, total=False):
    as_id: Required[Annotated[str, PropertyInfo(alias="asId")]]
    """Unique identifier of the parent AttitudeSet associated with this record. (uuid)"""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
