# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .attitudeset_abridged import AttitudesetAbridged

__all__ = ["AttitudeSetListResponse"]

AttitudeSetListResponse: TypeAlias = List[AttitudesetAbridged]
