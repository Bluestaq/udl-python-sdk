# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.gnssrawif.gnss_raw_if_full import GnssRawIfFull

__all__ = ["GnssrawifTupleResponse"]

GnssrawifTupleResponse: TypeAlias = List[GnssRawIfFull]
