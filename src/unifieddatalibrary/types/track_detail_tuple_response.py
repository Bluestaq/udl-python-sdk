# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .track_details.track_details_full import TrackDetailsFull

__all__ = ["TrackDetailTupleResponse"]

TrackDetailTupleResponse: TypeAlias = List[TrackDetailsFull]
