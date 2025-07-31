# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.rf_band_full import RfBandFull

__all__ = ["RfBandTupleResponse"]

RfBandTupleResponse: TypeAlias = List[RfBandFull]
