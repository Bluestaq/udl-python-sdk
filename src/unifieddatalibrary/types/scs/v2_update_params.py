# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .attachment_param import AttachmentParam

__all__ = ["V2UpdateParams"]


class V2UpdateParams(TypedDict, total=False):
    path: Required[str]
    """The complete path for the object to be updated."""

    id: str

    attachment: AttachmentParam

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
