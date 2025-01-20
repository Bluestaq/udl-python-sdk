# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .aircraftstatus_abridged import AircraftstatusAbridged

__all__ = ["AircraftStatusListResponse"]

AircraftStatusListResponse: TypeAlias = List[AircraftstatusAbridged]
