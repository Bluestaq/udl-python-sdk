# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StarCatalogTupleParams"]


class StarCatalogTupleParams(TypedDict, total=False):
    columns: Required[str]
    """
    Comma-separated list of valid field names for this data type to be returned in
    the response. Only the fields specified will be returned as well as the
    classification marking of the data, if applicable. See the ‘queryhelp’ operation
    for a complete list of possible fields.
    """

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
