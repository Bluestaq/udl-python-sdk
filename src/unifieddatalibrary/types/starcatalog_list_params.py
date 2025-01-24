# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StarcatalogListParams"]


class StarcatalogListParams(TypedDict, total=False):
    dec: float
    """
    (One or more of fields 'dec, ra' are required.) Barycentric declination of the
    source in International Celestial Reference System (ICRS) at the reference
    epoch, in degrees.
    """

    ra: float
    """
    (One or more of fields 'dec, ra' are required.) Barycentric right ascension of
    the source in the International Celestial Reference System (ICRS) frame at the
    reference epoch, in degrees.
    """
