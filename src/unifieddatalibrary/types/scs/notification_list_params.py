# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    path: str
    """Path of the folder to retrieve notification for.

    Must start and end with /. If no path is specified, all notifications will be
    returned.
    """
