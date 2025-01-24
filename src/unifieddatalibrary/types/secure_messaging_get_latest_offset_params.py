# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecureMessagingGetLatestOffsetParams"]


class SecureMessagingGetLatestOffsetParams(TypedDict, total=False):
    topic_2: Required[Annotated[str, PropertyInfo(alias="topic")]]
    """The topic name to return the latest offset."""
