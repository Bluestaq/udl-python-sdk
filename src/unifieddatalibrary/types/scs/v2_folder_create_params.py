# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2FolderCreateParams", "Attachment"]


class V2FolderCreateParams(TypedDict, total=False):
    path: Required[str]
    """Path to create.

    Will attempt to create all folders in the path that do not exist. Must start and
    end with '/'.
    """

    id: str

    attachment: Attachment

    classification_marking: Annotated[str, PropertyInfo(alias="classificationMarking")]
    """Classification marking of the folder or file in IC/CAPCO portion-marked format."""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]

    created_by: Annotated[str, PropertyInfo(alias="createdBy")]

    data: str

    description: str
    """Optional description for the file or folder."""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]

    file_path: Annotated[str, PropertyInfo(alias="filePath")]

    keywords: str

    parent_path: Annotated[str, PropertyInfo(alias="parentPath")]

    path_type: Annotated[str, PropertyInfo(alias="pathType")]

    read_acl: Annotated[str, PropertyInfo(alias="readAcl")]
    """For folders only.

    Comma separated list of user and group ids that should have read access on this
    folder and the items nested in it.
    """

    size: int

    tags: List[str]
    """
    Array of provider/source specific tags for this data, used for implementing data
    owner conditional access controls to restrict access to the data.
    """

    updated_at: Annotated[str, PropertyInfo(alias="updatedAt")]

    updated_by: Annotated[str, PropertyInfo(alias="updatedBy")]

    write_acl: Annotated[str, PropertyInfo(alias="writeAcl")]
    """For folders only.

    Comma separated list of user and group ids that should have write access on this
    folder and the items nested in it.
    """


class Attachment(TypedDict, total=False):
    author: str

    content: str

    content_length: int

    content_type: str

    date: str

    keywords: str

    language: str

    title: str
