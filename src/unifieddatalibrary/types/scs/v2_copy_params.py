# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2CopyParams"]


class V2CopyParams(TypedDict, total=False):
    from_path: Required[Annotated[str, PropertyInfo(alias="fromPath")]]
    """The path of the file or folder to copy. Must start with '/'."""

    to_path: Required[Annotated[str, PropertyInfo(alias="toPath")]]
    """The destination path to copy to. Must start with '/'."""
