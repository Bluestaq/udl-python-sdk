# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .sof_data_source_ref_full import SofDataSourceRefFull

__all__ = ["RelatedDocumentFull"]


class RelatedDocumentFull(BaseModel):
    data_source_refs: Optional[List[SofDataSourceRefFull]] = FieldInfo(alias="dataSourceRefs", default=None)
    """List of data sources related to this document."""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """The document id of the related document."""
