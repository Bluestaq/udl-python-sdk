# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V2ListParams"]


class V2ListParams(TypedDict, total=False):
    path: Required[str]
    """The base path to list"""
