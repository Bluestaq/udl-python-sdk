# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .logistics_remarks_full import LogisticsRemarksFull
from .logistics_segments_full import LogisticsSegmentsFull

__all__ = ["LogisticsTransportationPlansFull"]


class LogisticsTransportationPlansFull(BaseModel):
    act_dep_time: Optional[datetime] = FieldInfo(alias="actDepTime", default=None)
    """
    Actual time of departure of first segment, in ISO 8601 UTC format with
    millisecond precision.
    """

    aircraft_status: Optional[str] = FieldInfo(alias="aircraftStatus", default=None)
    """
    These are the initial maintenance values entered based on the pilot descriptions
    or the official maintenance evaluation code.
    """

    approx_arr_time: Optional[datetime] = FieldInfo(alias="approxArrTime", default=None)
    """
    Approximate time of arrival of final segement, in ISO 8601 UTC format with
    millisecond precision.
    """

    cancelled_date: Optional[datetime] = FieldInfo(alias="cancelledDate", default=None)
    """GC.

    LGTP_CANX_DT. GD2: Date when the transportation plan was cancelled, in ISO 8601
    UTC format with millisecond precision.
    """

    closed_date: Optional[datetime] = FieldInfo(alias="closedDate", default=None)
    """GC.

    LGTP_CLSD_DT. GD2: Date when the transportation plan was closed, in ISO 8601 UTC
    format with millisecond precision.
    """

    coordinator: Optional[str] = None
    """The AMS username of the operator who alters the coordination status.

    Automatically captured by the system.
    """

    coordinator_unit: Optional[str] = FieldInfo(alias="coordinatorUnit", default=None)
    """The AMS user unit_id of the operator who alters the coordination status.

    Automatically captured by the system from table AMS_USER.
    """

    destination_icao: Optional[str] = FieldInfo(alias="destinationICAO", default=None)
    """Destination location ICAO."""

    duration: Optional[str] = None
    """Transportation plan duration, expressed in the format MMM:SS."""

    est_arr_time: Optional[datetime] = FieldInfo(alias="estArrTime", default=None)
    """ETA of the final segment, in ISO 8601 UTC format with millisecond precision."""

    est_dep_time: Optional[datetime] = FieldInfo(alias="estDepTime", default=None)
    """ETD of the first segment, in ISO 8601 UTC format with millisecond precision."""

    last_changed_date: Optional[datetime] = FieldInfo(alias="lastChangedDate", default=None)
    """
    Last time transportation plan was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    logistic_master_record_id: Optional[str] = FieldInfo(alias="logisticMasterRecordId", default=None)
    """The identifier that represents a Logistics Master Record."""

    logistics_segments: Optional[List[LogisticsSegmentsFull]] = FieldInfo(alias="logisticsSegments", default=None)
    """The transportation segments associated with this transportation plan."""

    logistics_transportation_plans_remarks: Optional[List[LogisticsRemarksFull]] = FieldInfo(
        alias="logisticsTransportationPlansRemarks", default=None
    )
    """Remarks associated with this transportation plan."""

    majcom: Optional[str] = None
    """The major command for the current unit."""

    mission_change: Optional[bool] = FieldInfo(alias="missionChange", default=None)
    """
    Indicates whether there have been changes to changes to ICAOs, estArrTime, or
    estDepTime since this Transportation Plan was last edited.
    """

    num_enroute_stops: Optional[int] = FieldInfo(alias="numEnrouteStops", default=None)
    """Transportation plan enroute stops."""

    num_trans_loads: Optional[int] = FieldInfo(alias="numTransLoads", default=None)
    """The number of transloads for this Transportation Plan."""

    origin_icao: Optional[str] = FieldInfo(alias="originICAO", default=None)
    """The origin location."""

    plan_definition: Optional[str] = FieldInfo(alias="planDefinition", default=None)
    """Defines the transporation plan as either a deployment or redeployment."""

    plans_number: Optional[str] = FieldInfo(alias="plansNumber", default=None)
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """
    GDSS2 uses an 8 character serial number to uniquely identify the aircraft and
    MDS combination. This is a portion of the full manufacturer serial number.
    """

    status_code: Optional[str] = FieldInfo(alias="statusCode", default=None)
    """Transporation Coordination status code.

    Cancel, Send to APCC, working, agree, disapprove or blank.
    """

    tp_aircraft_mds: Optional[str] = FieldInfo(alias="tpAircraftMDS", default=None)
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
    """

    tp_tail_number: Optional[str] = FieldInfo(alias="tpTailNumber", default=None)
    """Contains the tail number displayed by GDSS2."""
