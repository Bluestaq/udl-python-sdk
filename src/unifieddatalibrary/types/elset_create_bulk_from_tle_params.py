# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ElsetCreateBulkFromTleParams"]


class ElsetCreateBulkFromTleParams(TypedDict, total=False):
    data_mode: Required[Annotated[str, PropertyInfo(alias="dataMode")]]
    """Data mode of the passed elsets (REAL, TEST, etc)."""

    make_current: Required[Annotated[bool, PropertyInfo(alias="makeCurrent")]]
    """
    Boolean indicating if these elsets should be set as the 'current' for their
    corresponding on-orbit/satellite numbers.
    """

    source: Required[str]
    """Source of the elset data."""

    body: Required[str]

    auto_create_sats: Annotated[bool, PropertyInfo(alias="autoCreateSats")]
    """
    Boolean indicating if a shell Onorbit/satellite should be created if the passed
    satellite number doesn't exist.
    """

    control: str
    """Dissemination control of the passed elsets (e.g.

    to support tagging with proprietary markings).
    """

    origin: str
    """Origin of the elset data."""

    tags: str
    """
    Optional comma-delineated list of provider/source specific tags for this data,
    where each element is no longer than 32 characters, used for implementing data
    owner conditional access controls to restrict access to the data. Should be left
    null by data providers unless conditional access controls are coordinated with
    the UDL team.
    """
