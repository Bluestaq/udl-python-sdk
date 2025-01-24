# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["PathCreateParams"]


class PathCreateParams(TypedDict, total=False):
    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """Classification (ex. U//FOUO)"""

    body: Required[FileTypes]

    description: str
    """Description"""

    tags: str
    """Tags"""
