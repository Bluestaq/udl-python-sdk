# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CotCreateParams", "CotChatData", "CotPositionData"]


class CotCreateParams(TypedDict, total=False):
    lat: Required[float]
    """WGS-84 latitude of the POI, in degrees (+N, -S), -90 to 90."""

    lon: Required[float]
    """WGS-84 longitude of the POI, in degrees (+E, -W), -180 to 180."""

    alt: float
    """Point height above ellipsoid (WGS-84), in meters."""

    call_signs: Annotated[List[str], PropertyInfo(alias="callSigns")]
    """Optional list of call signs to send message to directly."""

    ce: float
    """
    Radius of circular area about lat/lon point, in meters (1-sigma, if representing
    error).
    """

    cot_chat_data: Annotated[CotChatData, PropertyInfo(alias="cotChatData")]
    """Schema for the CotChatData to post."""

    cot_position_data: Annotated[CotPositionData, PropertyInfo(alias="cotPositionData")]
    """Schema for the CotPositionData to post."""

    groups: List[str]
    """Optional set of groups to send message to specifically.

    If not specified, the message will be sent to the default _ANON_ group.
    """

    how: str
    """
    How the event point was generated, in CoT object heirarchy notation (optional,
    CoT).
    """

    le: float
    """Height above lat/lon point, in meters (1-sigma, if representing linear error)."""

    sender_uid: Annotated[str, PropertyInfo(alias="senderUid")]
    """
    Identifier of the sender of the cot message which should remain the same on
    subsequent POI records of the same point of interest.
    """

    stale: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Stale timestamp (optional), in ISO8601 UTC format."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start time of event validity (optional), in ISO8601 UTC format."""

    type: str
    """Event type, in CoT object heirarchy notation (optional, CoT)."""

    uids: List[str]
    """Optional list of TAK user ids to send message to directly."""


class CotChatData(TypedDict, total=False):
    chat_msg: Annotated[str, PropertyInfo(alias="chatMsg")]
    """Contents of a chat message."""

    chat_room: Annotated[str, PropertyInfo(alias="chatRoom")]
    """Chat room name to send chat message to."""

    chat_sender_call_sign: Annotated[str, PropertyInfo(alias="chatSenderCallSign")]
    """Callsign of chat sender."""


class CotPositionData(TypedDict, total=False):
    call_sign: Required[Annotated[str, PropertyInfo(alias="callSign")]]
    """Name of the POI target Object."""

    team: Required[str]
    """Description of the POI target Object."""

    team_role: Required[Annotated[str, PropertyInfo(alias="teamRole")]]
    """
    Team role (Team Member| Team Lead | HQ | Sniper | Medic | Forward Observer | RTO
    | K9).
    """
