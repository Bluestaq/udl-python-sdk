# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScCopyParams"]


class ScCopyParams(TypedDict, total=False):
    id: Required[str]
    """The path of the item to copy"""

    target_path: Required[Annotated[str, PropertyInfo(alias="targetPath")]]
    """The path to copy to"""
