# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IsrCollectionCriticalTimesFull"]


class IsrCollectionCriticalTimesFull(BaseModel):
    earliest_imaging_time: datetime = FieldInfo(alias="earliestImagingTime")
    """Critical start time to collect an image for this requirement."""

    latest_imaging_time: datetime = FieldInfo(alias="latestImagingTime")
    """Critical stop time to collect an image for this requirement."""
