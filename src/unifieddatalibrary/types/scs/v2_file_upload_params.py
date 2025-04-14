# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["V2FileUploadParams"]


class V2FileUploadParams(TypedDict, total=False):
    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """Classification marking of uploaded document.

    If folders are created, they will also have this classification marking.
    """

    path: Required[str]
    """The complete path for the upload including filename.

    Will attempt to create folders in path if necessary. Must start with '/'.
    """

    body: Required[FileTypes]

    description: str
    """Optional description of uploaded document."""

    overwrite: bool
    """Whether or not to overwrite a file with the same name and path, if one exists."""

    tags: str
    """
    Optional array of provider/source specific tags for this data, used for
    implementing data owner conditional access controls to restrict access to the
    data.
    """
