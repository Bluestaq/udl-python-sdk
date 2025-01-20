# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .airspacecontrolorder_abridged import AirspacecontrolorderAbridged

__all__ = ["AirspaceControlOrderListResponse"]

AirspaceControlOrderListResponse: TypeAlias = List[AirspacecontrolorderAbridged]
