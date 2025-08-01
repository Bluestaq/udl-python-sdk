# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WaiverFull"]


class WaiverFull(BaseModel):
    expiration_date: Optional[datetime] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date of this waiver, in ISO8601 UTC format with millisecond
    precision.
    """

    has_expired: Optional[bool] = FieldInfo(alias="hasExpired", default=None)
    """Boolean indicating whether or not this waiver has expired."""

    issue_date: Optional[datetime] = FieldInfo(alias="issueDate", default=None)
    """
    The issue date of this waiver, in ISO8601 UTC format with millisecond precision.
    """

    issuer_name: Optional[str] = FieldInfo(alias="issuerName", default=None)
    """The name of the person who issued this waiver."""

    requester_name: Optional[str] = FieldInfo(alias="requesterName", default=None)
    """The name of the person requesting this waiver."""

    requester_phone_number: Optional[str] = FieldInfo(alias="requesterPhoneNumber", default=None)
    """The phone number of the person requesting this waiver."""

    requesting_unit: Optional[str] = FieldInfo(alias="requestingUnit", default=None)
    """The unit requesting this waiver."""

    waiver_applies_to: Optional[str] = FieldInfo(alias="waiverAppliesTo", default=None)
    """Description of the entities to which this waiver applies."""

    waiver_description: Optional[str] = FieldInfo(alias="waiverDescription", default=None)
    """The description of this waiver."""

    waiver_last_changed_by: Optional[str] = FieldInfo(alias="waiverLastChangedBy", default=None)
    """The name of the person who made the most recent change to this Waiver data."""

    waiver_last_changed_date: Optional[datetime] = FieldInfo(alias="waiverLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this waiver data, in ISO8601 UTC
    format with millisecond precision.
    """
