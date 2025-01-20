# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .antenna_details_abridged import AntennaDetailsAbridged

__all__ = ["AntennaDetailListResponse"]

AntennaDetailListResponse: TypeAlias = List[AntennaDetailsAbridged]
