# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2FolderCreateParams"]


class V2FolderCreateParams(TypedDict, total=False):
    path: Required[str]
    """Path to create.

    Will attempt to create all folders in the path that do not exist. Must start and
    end with '/'.
    """

    send_notification: Annotated[bool, PropertyInfo(alias="sendNotification")]
    """Whether or not to send a notification that this folder was created."""

    classification_marking: Annotated[str, PropertyInfo(alias="classificationMarking")]
    """Classification marking of the folder or file in IC/CAPCO portion-marked format."""

    delete_on: Annotated[int, PropertyInfo(alias="deleteOn")]

    description: str
    """Optional description for the file or folder."""

    read_acl: Annotated[str, PropertyInfo(alias="readAcl")]
    """For folders only.

    Comma separated list of user and group ids that should have read access on this
    folder and the items nested in it.
    """

    tags: List[str]
    """
    Array of provider/source specific tags for this data, used for implementing data
    owner conditional access controls to restrict access to the data.
    """

    write_acl: Annotated[str, PropertyInfo(alias="writeAcl")]
    """For folders only.

    Comma separated list of user and group ids that should have write access on this
    folder and the items nested in it.
    """
