# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .track_route.track_route_full import TrackRouteFull

__all__ = ["TrackRouteTupleResponse"]

TrackRouteTupleResponse: TypeAlias = List[TrackRouteFull]
