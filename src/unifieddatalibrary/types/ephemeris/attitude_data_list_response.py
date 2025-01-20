# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .attitude_data_abridged import AttitudeDataAbridged

__all__ = ["AttitudeDataListResponse"]

AttitudeDataListResponse: TypeAlias = List[AttitudeDataAbridged]
