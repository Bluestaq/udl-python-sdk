# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .video_streams_full import VideoStreamsFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[VideoStreamsFull]
