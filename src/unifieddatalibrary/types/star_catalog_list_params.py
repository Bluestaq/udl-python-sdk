# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StarCatalogListParams"]


class StarCatalogListParams(TypedDict, total=False):
    dec: float
    """
    (One or more of fields 'dec, ra' are required.) Barycentric declination of the
    source in International Celestial Reference System (ICRS) at the reference
    epoch, in degrees.
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    ra: float
    """
    (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
    the source in the International Celestial Reference System (ICRS) frame at the
    reference epoch, in degrees.
    """
