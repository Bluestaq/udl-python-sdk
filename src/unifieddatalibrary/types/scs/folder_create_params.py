# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FolderCreateParams"]


class FolderCreateParams(TypedDict, total=False):
    id: Required[str]
    """Path to create folder."""

    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    description: str
    """Optional description to include on folder."""

    read: str
    """Comma separated list of user ids who can read contents of the folder."""

    send_notification: Annotated[bool, PropertyInfo(alias="sendNotification")]
    """Whether or not to send a notification that this folder was created."""

    tags: str
    """Comma separated list of tags to add to the folder."""

    write: str
    """Comma separated list of user ids who can write to the folder."""
