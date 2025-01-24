# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2MoveParams"]


class V2MoveParams(TypedDict, total=False):
    from_path: Required[Annotated[str, PropertyInfo(alias="fromPath")]]
    """The path of the file or folder to move or rename. Must start with '/'."""

    to_path: Required[Annotated[str, PropertyInfo(alias="toPath")]]
    """The destination path of the file or folder after moving or renaming.

    Must start with '/'.
    """
