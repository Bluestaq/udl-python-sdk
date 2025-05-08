# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .tai_utc.taiutc_full import TaiutcFull

__all__ = ["TaiUtcTupleResponse"]

TaiUtcTupleResponse: TypeAlias = List[TaiutcFull]
