# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["OffsetGetResponse"]


class OffsetGetResponse(BaseModel):
    max_offset: Optional[int] = FieldInfo(alias="maxOffset", default=None)
    """The maximum (latest) Kafka offset for this topic."""

    min_offset: Optional[int] = FieldInfo(alias="minOffset", default=None)
    """The minimum (oldest) Kafka offset for this topic."""
