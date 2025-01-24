# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TopicDetails"]


class TopicDetails(BaseModel):
    description: Optional[str] = None
    """A description of the data content of this topic."""

    max_pos: Optional[int] = FieldInfo(alias="maxPos", default=None)
    """The maximum (latest) kafka offset for this topic."""

    min_pos: Optional[int] = FieldInfo(alias="minPos", default=None)
    """The minimum (oldest) kafka offset for this topic."""

    topic: Optional[str] = None
    """The name of the topic in kafka."""

    udl_openapi_schema: Optional[str] = FieldInfo(alias="udlOpenAPISchema", default=None)
    """The UDL schema that the objects in this topic apply to."""
