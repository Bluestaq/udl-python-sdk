# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .attachment import Attachment

__all__ = ["ScsEntity"]


class ScsEntity(BaseModel):
    id: Optional[str] = None

    attachment: Optional[Attachment] = None

    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)
    """Classification marking of the folder or file in IC/CAPCO portion-marked format."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    data: Optional[str] = None

    delete_on: Optional[int] = FieldInfo(alias="deleteOn", default=None)

    description: Optional[str] = None
    """Optional description for the file or folder."""

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)

    keywords: Optional[str] = None

    parent_path: Optional[str] = FieldInfo(alias="parentPath", default=None)

    path_type: Optional[str] = FieldInfo(alias="pathType", default=None)

    read_acl: Optional[str] = FieldInfo(alias="readAcl", default=None)
    """For folders only.

    Comma separated list of user and group ids that should have read access on this
    folder and the items nested in it.
    """

    size: Optional[int] = None

    tags: Optional[List[str]] = None
    """
    Array of provider/source specific tags for this data, used for implementing data
    owner conditional access controls to restrict access to the data.
    """

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)

    write_acl: Optional[str] = FieldInfo(alias="writeAcl", default=None)
    """For folders only.

    Comma separated list of user and group ids that should have write access on this
    folder and the items nested in it.
    """
