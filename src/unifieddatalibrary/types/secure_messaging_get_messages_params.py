# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecureMessagingGetMessagesParams"]


class SecureMessagingGetMessagesParams(TypedDict, total=False):
    path_topic: Required[Annotated[str, PropertyInfo(alias="topic")]]

    query_offset: Required[Annotated[int, PropertyInfo(alias="offset")]]
    """The message offset."""

    query_topic: Required[Annotated[str, PropertyInfo(alias="topic")]]
    """The topic from which messages are to be retrieved."""
