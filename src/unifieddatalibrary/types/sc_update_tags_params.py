# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScUpdateTagsParams"]


class ScUpdateTagsParams(TypedDict, total=False):
    folder: Required[str]
    """The base path to folder"""

    tags: Required[str]
    """The new tag"""
