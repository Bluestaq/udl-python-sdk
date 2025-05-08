# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VideoGetPublisherStreamingInfoParams"]


class VideoGetPublisherStreamingInfoParams(TypedDict, total=False):
    source_name: Required[Annotated[str, PropertyInfo(alias="sourceName")]]
    """The video source name."""

    stream_name: Required[Annotated[str, PropertyInfo(alias="streamName")]]
    """The video stream name."""

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
