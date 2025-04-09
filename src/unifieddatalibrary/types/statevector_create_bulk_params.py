# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .state_vector_ingest_param import StateVectorIngestParam

__all__ = ["StatevectorCreateBulkParams"]


class StatevectorCreateBulkParams(TypedDict, total=False):
    body: Iterable[StateVectorIngestParam]
