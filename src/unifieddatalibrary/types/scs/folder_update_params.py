# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FolderUpdateParams", "Attributes"]


class FolderUpdateParams(TypedDict, total=False):
    id: str

    attributes: Attributes

    content_action: Annotated[Literal["UPDATE", "COPY", "MOVE"], PropertyInfo(alias="contentAction")]

    target_name: Annotated[str, PropertyInfo(alias="targetName")]

    target_path: Annotated[str, PropertyInfo(alias="targetPath")]

    type: Literal["file", "folder", "summary"]


class Attributes(TypedDict, total=False):
    id: str

    classification: str

    classification_marking: Annotated[str, PropertyInfo(alias="classificationMarking")]

    created_by: Annotated[str, PropertyInfo(alias="createdBy")]

    created_date: Annotated[str, PropertyInfo(alias="createdDate")]

    delete_on: Annotated[int, PropertyInfo(alias="deleteOn")]

    description: str

    doc_title: Annotated[str, PropertyInfo(alias="docTitle")]

    doc_type: Annotated[str, PropertyInfo(alias="docType")]

    doi: List[str]

    ellipse_lat: Annotated[float, PropertyInfo(alias="ellipseLat")]

    ellipse_lon: Annotated[float, PropertyInfo(alias="ellipseLon")]

    file_name: Annotated[str, PropertyInfo(alias="fileName")]

    intrinsic_title: Annotated[str, PropertyInfo(alias="intrinsicTitle")]

    keywords: str

    media_title: Annotated[str, PropertyInfo(alias="mediaTitle")]

    meta_info: Annotated[str, PropertyInfo(alias="metaInfo")]

    milgrid: str

    milgrid_lat: Annotated[float, PropertyInfo(alias="milgridLat")]

    milgrid_lon: Annotated[float, PropertyInfo(alias="milgridLon")]

    modified_by: Annotated[str, PropertyInfo(alias="modifiedBy")]

    modified_date: Annotated[str, PropertyInfo(alias="modifiedDate")]

    name: str

    path: str

    read: str

    searchable: bool

    search_after: Annotated[str, PropertyInfo(alias="searchAfter")]

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]

    size: int

    tags: List[str]

    write: str
