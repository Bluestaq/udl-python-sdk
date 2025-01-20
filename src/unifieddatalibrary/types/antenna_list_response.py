# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .antenna_abridged import AntennaAbridged

__all__ = ["AntennaListResponse"]

AntennaListResponse: TypeAlias = List[AntennaAbridged]
