# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScDeleteParams"]


class ScDeleteParams(TypedDict, total=False):
    id: Required[str]
    """The id of the item to delete"""
