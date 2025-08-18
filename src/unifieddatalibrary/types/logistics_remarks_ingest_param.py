# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LogisticsRemarksIngestParam"]


class LogisticsRemarksIngestParam(TypedDict, total=False):
    last_changed: Annotated[Union[str, datetime], PropertyInfo(alias="lastChanged", format="iso8601")]
    """
    Date the remark was published or updated, in ISO 8601 UTC format, with
    millisecond precision.
    """

    remark: str
    """Text of the remark."""

    username: str
    """User who published the remark."""
