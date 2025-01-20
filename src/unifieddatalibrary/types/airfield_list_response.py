# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .airfield_abridged import AirfieldAbridged

__all__ = ["AirfieldListResponse"]

AirfieldListResponse: TypeAlias = List[AirfieldAbridged]
