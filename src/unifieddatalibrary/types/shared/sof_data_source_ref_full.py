# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SofDataSourceRefFull"]


class SofDataSourceRefFull(BaseModel):
    data_source_id: Optional[str] = FieldInfo(alias="dataSourceId", default=None)
    """Data source id."""

    end_position: Optional[str] = FieldInfo(alias="endPosition", default=None)
    """end position."""

    paragraph_number: Optional[str] = FieldInfo(alias="paragraphNumber", default=None)
    """paragraph number."""

    sentence_number: Optional[str] = FieldInfo(alias="sentenceNumber", default=None)
    """sentence number."""

    start_position: Optional[str] = FieldInfo(alias="startPosition", default=None)
    """start position."""
