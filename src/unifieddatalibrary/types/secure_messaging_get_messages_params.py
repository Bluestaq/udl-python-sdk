# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecureMessagingGetMessagesParams"]


class SecureMessagingGetMessagesParams(TypedDict, total=False):
    topic_1: Required[Annotated[str, PropertyInfo(alias="topic")]]

    offset_2: Required[Annotated[int, PropertyInfo(alias="offset")]]
    """The message offset."""

    topic_2: Required[Annotated[str, PropertyInfo(alias="topic")]]
    """The topic from which messages are to be retrieved."""
