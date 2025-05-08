# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .state_vector_ingest_param import StateVectorIngestParam

__all__ = ["StateVectorCreateBulkParams"]


class StateVectorCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[StateVectorIngestParam]]
