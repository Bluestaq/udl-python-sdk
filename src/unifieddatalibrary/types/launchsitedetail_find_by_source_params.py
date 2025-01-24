# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LaunchsitedetailFindBySourceParams"]


class LaunchsitedetailFindBySourceParams(TypedDict, total=False):
    source: Required[str]
    """The source of the LaunchSiteDetails records to find."""
