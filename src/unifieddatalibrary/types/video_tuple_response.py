# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .video.video_streams_full import VideoStreamsFull

__all__ = ["VideoTupleResponse"]

VideoTupleResponse: TypeAlias = List[VideoStreamsFull]
