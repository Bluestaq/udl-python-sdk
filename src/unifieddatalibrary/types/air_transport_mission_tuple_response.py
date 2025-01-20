# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.air_transport_mission_full import AirTransportMissionFull

__all__ = ["AirTransportMissionTupleResponse"]

AirTransportMissionTupleResponse: TypeAlias = List[AirTransportMissionFull]
