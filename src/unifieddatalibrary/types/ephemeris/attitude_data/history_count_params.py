# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HistoryCountParams"]


class HistoryCountParams(TypedDict, total=False):
    as_id: Required[Annotated[str, PropertyInfo(alias="asId")]]
    """Unique identifier of the parent AttitudeSet associated with this record. (uuid)"""
