# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FileData", "Attributes"]


class Attributes(BaseModel):
    id: Optional[str] = None

    classification: Optional[str] = None

    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    created_date: Optional[str] = FieldInfo(alias="createdDate", default=None)

    description: Optional[str] = None

    doc_title: Optional[str] = FieldInfo(alias="docTitle", default=None)

    doc_type: Optional[str] = FieldInfo(alias="docType", default=None)

    doi: Optional[List[str]] = None

    ellipse_lat: Optional[float] = FieldInfo(alias="ellipseLat", default=None)

    ellipse_lon: Optional[float] = FieldInfo(alias="ellipseLon", default=None)

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    intrinsic_title: Optional[str] = FieldInfo(alias="intrinsicTitle", default=None)

    keywords: Optional[str] = None

    media_title: Optional[str] = FieldInfo(alias="mediaTitle", default=None)

    meta_info: Optional[str] = FieldInfo(alias="metaInfo", default=None)

    milgrid: Optional[str] = None

    milgrid_lat: Optional[float] = FieldInfo(alias="milgridLat", default=None)

    milgrid_lon: Optional[float] = FieldInfo(alias="milgridLon", default=None)

    modified_by: Optional[str] = FieldInfo(alias="modifiedBy", default=None)

    modified_date: Optional[str] = FieldInfo(alias="modifiedDate", default=None)

    name: Optional[str] = None

    path: Optional[str] = None

    read: Optional[str] = None

    searchable: Optional[bool] = None

    search_after: Optional[str] = FieldInfo(alias="searchAfter", default=None)

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)

    size: Optional[int] = None

    tags: Optional[List[str]] = None

    write: Optional[str] = None


class FileData(BaseModel):
    id: Optional[str] = None

    attributes: Optional[Attributes] = None

    content_action: Optional[Literal["UPDATE", "COPY", "MOVE"]] = FieldInfo(alias="contentAction", default=None)

    target_name: Optional[str] = FieldInfo(alias="targetName", default=None)

    target_path: Optional[str] = FieldInfo(alias="targetPath", default=None)

    type: Optional[Literal["file", "folder", "summary"]] = None
