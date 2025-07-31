# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IsrCollectionPocFull"]


class IsrCollectionPocFull(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the collection requirement POC."""

    callsign: Optional[str] = None
    """Callsign of the POC."""

    chat_name: Optional[str] = FieldInfo(alias="chatName", default=None)
    """Chat name of the POC."""

    chat_system: Optional[str] = FieldInfo(alias="chatSystem", default=None)
    """Chat system the POC is accessing."""

    email: Optional[str] = None
    """Email address of the POC."""

    name: Optional[str] = None
    """Name of the POC."""

    notes: Optional[str] = None
    """Amplifying notes about the POC."""

    phone: Optional[str] = None
    """Phone number of the POC."""

    radio_frequency: Optional[float] = FieldInfo(alias="radioFrequency", default=None)
    """Radio Frequency the POC is on."""

    unit: Optional[str] = None
    """Unit the POC belongs to."""
