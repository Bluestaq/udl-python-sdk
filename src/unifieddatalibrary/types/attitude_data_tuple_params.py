# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttitudeDataTupleParams"]


class AttitudeDataTupleParams(TypedDict, total=False):
    as_id: Required[Annotated[str, PropertyInfo(alias="asId")]]
    """Unique identifier of the parent AttitudeSet associated with this record. (uuid)"""

    columns: Required[str]
    """
    Comma-separated list of valid field names for this data type to be returned in
    the response. Only the fields specified will be returned as well as the
    classification marking of the data, if applicable. See the ‘queryhelp’ operation
    for a complete list of possible fields.
    """
