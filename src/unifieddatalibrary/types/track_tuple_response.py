# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .track.track_full import TrackFull

__all__ = ["TrackTupleResponse"]

TrackTupleResponse: TypeAlias = List[TrackFull]
