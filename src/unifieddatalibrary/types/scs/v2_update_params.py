# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["V2UpdateParams", "Attachment"]


class V2UpdateParams(TypedDict, total=False):
    path: Required[str]
    """The complete path for the object to be updated."""

    send_notification: Annotated[bool, PropertyInfo(alias="sendNotification")]
    """Whether or not to send a notification that the target file/folder was updated."""

    id: str
    """Unique identifier for document."""

    attachment: Attachment
    """Additional metadata associated with this document."""

    classification_marking: Annotated[str, PropertyInfo(alias="classificationMarking")]
    """Classification marking of the folder or file in IC/CAPCO portion-marked format."""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]
    """The time at which this document was created, represented in UTC ISO format."""

    created_by: Annotated[str, PropertyInfo(alias="createdBy")]
    """The creator of this document. Can be a person or a software entity."""

    delete_on: Annotated[int, PropertyInfo(alias="deleteOn")]
    """Time at which this document should be automatically deleted.

    Represented in milliseconds since Unix epoch.
    """

    description: str
    """Optional description for the file or folder."""

    filename: str
    """The name of this document. Applicable to files and folders."""

    file_path: Annotated[str, PropertyInfo(alias="filePath")]
    """The absolute path to this document."""

    keywords: str
    """Optional.

    Any keywords associated with this document. Only applicable to files whose
    contents are indexed (e.g. text files, PDFs).
    """

    parent_path: Annotated[str, PropertyInfo(alias="parentPath")]
    """The parent folder of this document.

    If this document is a root-level folder then the parent path is "/".
    """

    path_type: Annotated[Literal["file", "folder"], PropertyInfo(alias="pathType")]
    """The type of this document."""

    read_acl: Annotated[str, PropertyInfo(alias="readAcl")]
    """For folders only.

    Comma separated list of user and group ids that should have read access on this
    folder and the items nested in it.
    """

    size: int
    """Size of this document in bytes."""

    tags: SequenceNotStr[str]
    """
    Array of provider/source specific tags for this data, used for implementing data
    owner conditional access controls to restrict access to the data.
    """

    updated_at: Annotated[str, PropertyInfo(alias="updatedAt")]
    """
    The time at which this document was most recently updated, represented in UTC
    ISO format.
    """

    updated_by: Annotated[str, PropertyInfo(alias="updatedBy")]
    """The person or software entity who updated this document most recently."""

    write_acl: Annotated[str, PropertyInfo(alias="writeAcl")]
    """For folders only.

    Comma separated list of user and group ids that should have write access on this
    folder and the items nested in it.
    """


class Attachment(TypedDict, total=False):
    author: str
    """The creator of this document. Can be a person or a software entity."""

    content_length: int
    """The length of the document, in bytes."""

    content_type: str
    """The document's MIME-type (if applicable)."""

    date: str
    """The time at which this attachment was created, represented in UTC ISO format."""

    keywords: str
    """Any keywords associated with this document.

    Only applicable to files whose contents are indexed (e.g. text files, PDFs).
    """

    language: str
    """The human language of the document, if discernible."""

    title: str
    """The title of the document."""
