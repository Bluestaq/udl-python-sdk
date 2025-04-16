# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .datalink_ingest_param import DatalinkIngestParam

__all__ = ["DatalinkUnvalidatedPublishParams"]


class DatalinkUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[DatalinkIngestParam]]
