# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PathCreateWithFileParams"]


class PathCreateWithFileParams(TypedDict, total=False):
    id: Required[str]
    """The full path to create, including path and file name"""

    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """Classification (ex. U//FOUO)"""

    delete_after: Annotated[str, PropertyInfo(alias="deleteAfter")]
    """Length of time after which to automatically delete the file."""

    description: str
    """Description"""

    overwrite: bool
    """Whether or not to overwrite a file with the same name and path, if one exists."""

    send_notification: Annotated[bool, PropertyInfo(alias="sendNotification")]
    """Whether or not to send a notification that this file was uploaded."""

    tags: str
    """Tags"""
