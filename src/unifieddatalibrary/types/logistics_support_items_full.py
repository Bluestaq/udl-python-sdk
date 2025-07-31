# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .logistics_parts_full import LogisticsPartsFull
from .logistics_remarks_full import LogisticsRemarksFull
from .logistics_specialties_full import LogisticsSpecialtiesFull

__all__ = ["LogisticsSupportItemsFull"]


class LogisticsSupportItemsFull(BaseModel):
    cannibalized: Optional[bool] = None
    """
    This element indicates whether or not the supplied item is contained within
    another item.
    """

    deploy_plan_number: Optional[str] = FieldInfo(alias="deployPlanNumber", default=None)
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    description: Optional[str] = None
    """The technical order name of the part ordered."""

    item_last_changed_date: Optional[datetime] = FieldInfo(alias="itemLastChangedDate", default=None)
    """
    The last time this supported item was updated, in ISO 8601 UTC format with
    millisecond precision.
    """

    job_control_number: Optional[str] = FieldInfo(alias="jobControlNumber", default=None)
    """
    A number assigned by Job Control to monitor and record maintenance actions
    required to correct the associated aircraft maintenance discrepancy. It is
    seven, nine or twelve characters, depending on the base-specific numbering
    scheme. If seven characters: characters 1-3 are Julian date, 4-7 are sequence
    numbers. If nine characters: characters 1-2 are last two digits of the year,
    characters 3-5 are Julian date, 6-9 are sequence numbers. If twelve characters:
    characters 1-2 are last two digits of the year, 3-5 are Julian date, 6-9 are
    sequence numbers, and 10-12 are a three-digit supplemental number.
    """

    logistics_parts: Optional[List[LogisticsPartsFull]] = FieldInfo(alias="logisticsParts", default=None)
    """The parts associated with this support item."""

    logistics_remarks: Optional[List[LogisticsRemarksFull]] = FieldInfo(alias="logisticsRemarks", default=None)
    """Remarks associated with this support item."""

    logistics_specialties: Optional[List[LogisticsSpecialtiesFull]] = FieldInfo(
        alias="logisticsSpecialties", default=None
    )
    """The specialties required to implement this support item."""

    quantity: Optional[int] = None
    """Military aircraft discrepancy logistics requisition ordered quantity.

    The quantity of equipment ordered that is required to fix the aircraft.
    """

    ready_time: Optional[datetime] = FieldInfo(alias="readyTime", default=None)
    """The time the item is ready, in ISO 8601 UTC format with millisecond precision."""

    received_time: Optional[datetime] = FieldInfo(alias="receivedTime", default=None)
    """
    The time the item is received, in ISO 8601 UTC format with millisecond
    precision.
    """

    recovery_request_type_code: Optional[str] = FieldInfo(alias="recoveryRequestTypeCode", default=None)
    """The type of recovery request needed. Contact the source provider for details."""

    redeploy_plan_number: Optional[str] = FieldInfo(alias="redeployPlanNumber", default=None)
    """System generated reference id for the transportation plan.

    Format: TXXXXXNNNN T - Transportation, Sequence Number, Node Id.
    """

    redeploy_shipment_unit_id: Optional[str] = FieldInfo(alias="redeployShipmentUnitId", default=None)
    """
    This is the Redeploy (return) Transportation Control Number/Tracking Reference
    Number for the selected item.
    """

    request_number: Optional[str] = FieldInfo(alias="requestNumber", default=None)
    """The request or record number for this item type (Equipent, Part, or MRT)."""

    resupport_flag: Optional[bool] = FieldInfo(alias="resupportFlag", default=None)
    """
    This element indicates if the supplied item is characterized as additional
    support.
    """

    shipment_unit_id: Optional[str] = FieldInfo(alias="shipmentUnitId", default=None)
    """
    Shipment Unit Identifier is the Transportation Control Number (TCN) for shipping
    that piece of equipment being requested.
    """

    si_poc: Optional[str] = FieldInfo(alias="siPOC", default=None)
    """
    The point of contact is a free text field to add information about the
    individual(s) with knowledge of the referenced requested or supplied item(s).
    The default value for this field is the last name, first name, and middle
    initial of the operator who created the records and/or generated the
    transaction.
    """

    source_icao: Optional[str] = FieldInfo(alias="sourceICAO", default=None)
    """
    The code that represents the International Civil Aviation Organization (ICAO)
    designations of an airport.
    """
