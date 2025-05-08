# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OnorbitGetSignatureParams"]


class OnorbitGetSignatureParams(TypedDict, total=False):
    id_on_orbit: Required[Annotated[str, PropertyInfo(alias="idOnOrbit")]]
    """ID of the Onorbit object."""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
