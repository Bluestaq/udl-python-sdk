# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PointOfContactIngestParam"]


class PointOfContactIngestParam(TypedDict, total=False):
    office: str
    """Office name for which the contact belongs."""

    phone: str
    """Phone number of the contact."""

    poc_name: Annotated[str, PropertyInfo(alias="pocName")]
    """The name of the contact."""

    poc_org: Annotated[str, PropertyInfo(alias="pocOrg")]
    """Organization name for which the contact belongs."""

    poc_sequence_id: Annotated[int, PropertyInfo(alias="pocSequenceId")]
    """Sequencing field for point of contact."""

    poc_type_name: Annotated[str, PropertyInfo(alias="pocTypeName")]
    """
    A code or name that represents the contact's role in association to the track
    route (ex. Originator, Scheduler, Maintainer, etc.).
    """

    rank: str
    """The rank of contact."""

    remark: str
    """Text of the remark."""

    username: str
    """The username of the contact."""
