# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .attachment import Attachment

__all__ = ["ScsEntity"]


class ScsEntity(BaseModel):
    id: Optional[str] = None
    """Unique identifier for document."""

    attachment: Optional[Attachment] = None
    """Additional metadata associated with this document."""

    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)
    """Classification marking of the folder or file in IC/CAPCO portion-marked format."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """The time at which this document was created, represented in UTC ISO format."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """The creator of this document. Can be a person or a software entity."""

    delete_on: Optional[int] = FieldInfo(alias="deleteOn", default=None)
    """Time at which this document should be automatically deleted.

    Represented in milliseconds since Unix epoch.
    """

    description: Optional[str] = None
    """Optional description for the file or folder."""

    filename: Optional[str] = None
    """The name of this document. Applicable to files and folders."""

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)
    """The absolute path to this document."""

    keywords: Optional[str] = None
    """Optional.

    Any keywords associated with this document. Only applicable to files whose
    contents are indexed (e.g. text files, PDFs).
    """

    parent_path: Optional[str] = FieldInfo(alias="parentPath", default=None)
    """The parent folder of this document.

    If this document is a root-level folder then the parent path is "/".
    """

    path_type: Optional[Literal["file", "folder"]] = FieldInfo(alias="pathType", default=None)
    """The type of this document."""

    read_acl: Optional[str] = FieldInfo(alias="readAcl", default=None)
    """For folders only.

    Comma separated list of user and group ids that should have read access on this
    folder and the items nested in it.
    """

    size: Optional[int] = None
    """Size of this document in bytes."""

    tags: Optional[List[str]] = None
    """
    Array of provider/source specific tags for this data, used for implementing data
    owner conditional access controls to restrict access to the data.
    """

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """
    The time at which this document was most recently updated, represented in UTC
    ISO format.
    """

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """The person or software entity who updated this document most recently."""

    write_acl: Optional[str] = FieldInfo(alias="writeAcl", default=None)
    """For folders only.

    Comma separated list of user and group ids that should have write access on this
    folder and the items nested in it.
    """
