# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LogisticsSegmentsFull"]


class LogisticsSegmentsFull(BaseModel):
    arrival_icao: Optional[str] = FieldInfo(alias="arrivalICAO", default=None)
    """Airport ICAO arrival code."""

    departure_icao: Optional[str] = FieldInfo(alias="departureICAO", default=None)
    """Airport ICAO departure code."""

    ext_mission_id: Optional[str] = FieldInfo(alias="extMissionId", default=None)
    """The GDSS mission ID for this segment."""

    id_mission: Optional[str] = FieldInfo(alias="idMission", default=None)
    """
    The unique identifier of the mission to which this logistics record is assigned.
    """

    itin: Optional[int] = None
    """Start air mission itinerary point identifier."""

    mission_number: Optional[str] = FieldInfo(alias="missionNumber", default=None)
    """The user generated identifier for an air mission subgroup."""

    mission_type: Optional[str] = FieldInfo(alias="missionType", default=None)
    """The type of mission (e.g. SAAM, CHNL, etc.)."""

    mode_code: Optional[str] = FieldInfo(alias="modeCode", default=None)
    """Transportation mode.

    AMC airlift, Commercial airlift, Other, or surface transportation.
    """

    seg_act_arr_time: Optional[datetime] = FieldInfo(alias="segActArrTime", default=None)
    """
    Actual arrival time to segment destination, in ISO 8601 UTC format with
    millisecond precision.
    """

    seg_act_dep_time: Optional[datetime] = FieldInfo(alias="segActDepTime", default=None)
    """
    Actual departure time to the segment destination, in ISO 8601 UTC format with
    millisecond precision.
    """

    seg_aircraft_mds: Optional[str] = FieldInfo(alias="segAircraftMDS", default=None)
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    seg_est_arr_time: Optional[datetime] = FieldInfo(alias="segEstArrTime", default=None)
    """GC.

    LGTPS_C_DT_EST_ARR. GD2: Estimated arrival time to the segment destination. Only
    supplied when the segment is not attached to a Mission, otherwise the ETA is
    derived from the Mission segment destination point. This datetime should be in
    ISO 8601 UTC format with millisecond precision.
    """

    seg_est_dep_time: Optional[datetime] = FieldInfo(alias="segEstDepTime", default=None)
    """GC.

    LGTPS_C_DT_EST_DEP. GD2: Estimated departure time from the segment origin. Only
    supplied when the segment is not attached to a Mission, otherwise the ETD is
    derived from the Mission segment origin point. This datetime should be in ISO
    8601 UTC format with millisecond precision.
    """

    segment_number: Optional[int] = FieldInfo(alias="segmentNumber", default=None)
    """Used to sequence the segments in the transportation plan."""

    seg_tail_number: Optional[str] = FieldInfo(alias="segTailNumber", default=None)
    """The identifier that represents a specific aircraft within an aircraft type."""
