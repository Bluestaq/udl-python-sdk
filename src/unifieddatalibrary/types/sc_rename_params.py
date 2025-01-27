# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScRenameParams"]


class ScRenameParams(TypedDict, total=False):
    id: Required[str]
    """The path of the item to rename."""

    new_name: Required[Annotated[str, PropertyInfo(alias="newName")]]
    """The new name for the file or folder. Do not include the path."""
