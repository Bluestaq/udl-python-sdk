# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V2DeleteParams"]


class V2DeleteParams(TypedDict, total=False):
    path: Required[str]
    """The complete path for the object to be deleted. Must start with '/'."""
