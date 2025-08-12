# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .track_route_ingest_param import TrackRouteIngestParam

__all__ = ["TrackRouteCreateBulkParams"]


class TrackRouteCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[TrackRouteIngestParam]]
