# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .air_transport_mission_abridged import AirTransportMissionAbridged

__all__ = ["AirTransportMissionListResponse"]

AirTransportMissionListResponse: TypeAlias = List[AirTransportMissionAbridged]
