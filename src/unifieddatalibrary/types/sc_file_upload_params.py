# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ScFileUploadParams"]


class ScFileUploadParams(TypedDict, total=False):
    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """Classification (ex. U//FOUO)"""

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]
    """FileName (ex. dog.jpg)"""

    path: Required[str]
    """The base path to upload file (ex. images)"""

    body: Required[FileTypes]

    description: str
    """Description"""

    overwrite: bool
    """Whether or not to overwrite a file with the same name and path, if one exists."""

    tags: str
    """Tags"""
