# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .effect_response_metrics_full import EffectResponseMetricsFull

__all__ = ["EffectResponseActionsListFull"]


class EffectResponseActionsListFull(BaseModel):
    action_actor_src_id: Optional[str] = FieldInfo(alias="actionActorSrcId", default=None)
    """
    The record ID, depending on the type identified in actorSrcType, of the
    requested asset/actor.
    """

    action_actor_src_type: Optional[str] = FieldInfo(alias="actionActorSrcType", default=None)
    """
    The source type of the asset/actor identifier (AIRCRAFT, LANDCRAFT, SEACRAFT,
    TRACK).
    """

    action_end_time: Optional[datetime] = FieldInfo(alias="actionEndTime", default=None)
    """The desired end time of this task, in ISO8601 UTC format."""

    action_id: Optional[str] = FieldInfo(alias="actionId", default=None)
    """Identifier of this action."""

    action_metrics: Optional[List[EffectResponseMetricsFull]] = FieldInfo(alias="actionMetrics", default=None)
    """List of metrics associated with this action."""

    action_start_time: Optional[datetime] = FieldInfo(alias="actionStartTime", default=None)
    """The desired start time of this task, in ISO8601 UTC format."""

    actor_intercept_alt: Optional[float] = FieldInfo(alias="actorInterceptAlt", default=None)
    """The WGS-84 altitude of the asset/actor location at weapon launch, in meters."""

    actor_intercept_lat: Optional[float] = FieldInfo(alias="actorInterceptLat", default=None)
    """The WGS-84 latitude of the asset/actor location at weapon launch, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    actor_intercept_lon: Optional[float] = FieldInfo(alias="actorInterceptLon", default=None)
    """The WGS-84 longitude of the asset/actor location at weapon launch, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    effector: Optional[str] = None
    """The type of munition or sensor used by this asset/actor."""

    summary: Optional[str] = None
    """A summary string describing different aspects of the action."""

    target_src_id: Optional[str] = FieldInfo(alias="targetSrcId", default=None)
    """
    The POI or TRACK ID, depending on the type identified in targetSrcType, of the
    requested target. This identifier corresponds to either poi.poiid or track.trkId
    from their respective schemas.
    """

    target_src_type: Optional[str] = FieldInfo(alias="targetSrcType", default=None)
    """The source type of the targetId identifier (POI, TRACK)."""

    tot_end_time: Optional[datetime] = FieldInfo(alias="totEndTime", default=None)
    """The end time of the asset TOT (time over target), in ISO8601 UTC format."""

    tot_start_time: Optional[datetime] = FieldInfo(alias="totStartTime", default=None)
    """The start time of the asset TOT (time over target), in ISO8601 UTC format."""

    weapon_intercept_alt: Optional[float] = FieldInfo(alias="weaponInterceptAlt", default=None)
    """The WGS-84 altitude of the weapon destination location, in meters."""

    weapon_intercept_lat: Optional[float] = FieldInfo(alias="weaponInterceptLat", default=None)
    """The WGS-84 latitude of the weapon destination location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    weapon_intercept_lon: Optional[float] = FieldInfo(alias="weaponInterceptLon", default=None)
    """The WGS-84 longitude of the weapon destination location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """
