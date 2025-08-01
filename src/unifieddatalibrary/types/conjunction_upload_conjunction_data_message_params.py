# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConjunctionUploadConjunctionDataMessageParams"]


class ConjunctionUploadConjunctionDataMessageParams(TypedDict, total=False):
    classification: Required[str]
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    data_mode: Required[Annotated[Literal["REAL", "TEST", "SIMULATED", "EXERCISE"], PropertyInfo(alias="dataMode")]]
    """Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data."""

    filename: Required[str]
    """Filename of the payload."""

    source: Required[str]
    """Source of the data."""

    tags: str
    """
    Optional array of provider/source specific tags for this data, where each
    element is no longer than 32 characters, used for implementing data owner
    conditional access controls to restrict access to the data. Should be left null
    by data providers unless conditional access controls are coordinated with the
    UDL team.
    """
