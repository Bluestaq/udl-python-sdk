# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["H3GeoHexCellCountParams"]


class H3GeoHexCellCountParams(TypedDict, total=False):
    id_h3_geo: Required[Annotated[str, PropertyInfo(alias="idH3Geo")]]
    """Unique identifier of the parent H3 Geo record containing this hex cell. (uuid)"""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
