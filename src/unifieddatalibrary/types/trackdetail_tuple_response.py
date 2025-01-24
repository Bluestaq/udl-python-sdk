# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .trackdetails.track_details_full import TrackDetailsFull

__all__ = ["TrackdetailTupleResponse"]

TrackdetailTupleResponse: TypeAlias = List[TrackDetailsFull]
