# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.airfieldstatus_full import AirfieldstatusFull

__all__ = ["AirfieldStatusTupleResponse"]

AirfieldStatusTupleResponse: TypeAlias = List[AirfieldstatusFull]
