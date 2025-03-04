# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScFileDownloadParams"]


class ScFileDownloadParams(TypedDict, total=False):
    id: Required[str]
    """The complete path and filename of the file to download."""
