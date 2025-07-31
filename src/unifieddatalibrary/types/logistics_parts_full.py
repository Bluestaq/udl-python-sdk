# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .logistics_stocks_full import LogisticsStocksFull

__all__ = ["LogisticsPartsFull"]


class LogisticsPartsFull(BaseModel):
    figure_number: Optional[str] = FieldInfo(alias="figureNumber", default=None)
    """Technical order manual figure number for the requested / supplied part."""

    index_number: Optional[str] = FieldInfo(alias="indexNumber", default=None)
    """Technical order manual index number for the requested part."""

    location_verifier: Optional[str] = FieldInfo(alias="locationVerifier", default=None)
    """
    The person who validated that the sourced location has, and can supply, the
    requested parts.
    """

    logistics_stocks: Optional[List[LogisticsStocksFull]] = FieldInfo(alias="logisticsStocks", default=None)
    """The supply stocks for this support item."""

    measurement_unit_code: Optional[str] = FieldInfo(alias="measurementUnitCode", default=None)
    """Code for a unit of measurement."""

    national_stock_number: Optional[str] = FieldInfo(alias="nationalStockNumber", default=None)
    """The National Stock Number of the part being requested or supplied."""

    part_number: Optional[str] = FieldInfo(alias="partNumber", default=None)
    """Requested or supplied part number."""

    request_verifier: Optional[str] = FieldInfo(alias="requestVerifier", default=None)
    """The person who validated the request for parts."""

    supply_document_number: Optional[str] = FieldInfo(alias="supplyDocumentNumber", default=None)
    """The supply document number."""

    technical_order_text: Optional[str] = FieldInfo(alias="technicalOrderText", default=None)
    """
    Indicates the specified Technical Order manual holding the aircraft information
    for use in diagnosing a problem or condition.
    """

    work_unit_code: Optional[str] = FieldInfo(alias="workUnitCode", default=None)
    """Work Unit Code (WUC), or for some aircraft types, the Reference Designator."""
