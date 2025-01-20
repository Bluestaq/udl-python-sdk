# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .ephemeris_abridged import EphemerisAbridged

__all__ = ["EphemerisListResponse"]

EphemerisListResponse: TypeAlias = List[EphemerisAbridged]
