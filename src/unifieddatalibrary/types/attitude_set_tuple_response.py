# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.attitudeset_full import AttitudesetFull

__all__ = ["AttitudeSetTupleResponse"]

AttitudeSetTupleResponse: TypeAlias = List[AttitudesetFull]
