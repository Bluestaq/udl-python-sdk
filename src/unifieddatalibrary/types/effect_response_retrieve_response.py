# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EffectResponseRetrieveResponse", "ActionsList", "ActionsListActionMetric", "CoaMetric"]


class ActionsListActionMetric(BaseModel):
    domain_value: Optional[float] = FieldInfo(alias="domainValue", default=None)
    """The metric score specific to its domain."""

    metric_type: Optional[str] = FieldInfo(alias="metricType", default=None)
    """The type of the metric (e.g.

    CollateralDamage, GoalAchievement, OpportunityCost, Timeliness, Unavailable,
    etc.).
    """

    provenance: Optional[str] = None
    """The metric that was used to score this task."""

    relative_value: Optional[float] = FieldInfo(alias="relativeValue", default=None)
    """The metric score adjusted to be relative and comparable to other domains."""


class ActionsList(BaseModel):
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

    action_metrics: Optional[List[ActionsListActionMetric]] = FieldInfo(alias="actionMetrics", default=None)
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


class CoaMetric(BaseModel):
    domain_value: Optional[float] = FieldInfo(alias="domainValue", default=None)
    """The metric score specific to its domain."""

    metric_type: Optional[str] = FieldInfo(alias="metricType", default=None)
    """The type of the metric (e.g.

    CollateralDamage, GoalAchievement, OpportunityCost, Timeliness, Unavailable,
    etc.).
    """

    provenance: Optional[str] = None
    """The metric that was used to score this task."""

    relative_value: Optional[float] = FieldInfo(alias="relativeValue", default=None)
    """The metric score adjusted to be relative and comparable to other domains."""


class EffectResponseRetrieveResponse(BaseModel):
    classification_marking: str = FieldInfo(alias="classificationMarking")
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"] = FieldInfo(alias="dataMode")
    """Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

    EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
    may include both real and simulated data.

    REAL:&nbsp;Data collected or produced that pertains to real-world objects,
    events, and analysis.

    SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
    datasets.

    TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
    requirements, and for validating technical, functional, and performance
    characteristics.
    """

    source: str
    """Source of the data."""

    type: str
    """The type of response in this record (e.g. COA, SCORECARD, etc.)."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    actions_list: Optional[List[ActionsList]] = FieldInfo(alias="actionsList", default=None)
    """List of actions associated with this effect response."""

    actor_src_id: Optional[str] = FieldInfo(alias="actorSrcId", default=None)
    """
    The record ID, depending on the type identified in actorSrcType, of the
    requested asset.
    """

    actor_src_type: Optional[str] = FieldInfo(alias="actorSrcType", default=None)
    """
    The source type of the asset/actor identifier (AIRCRAFT, LANDCRAFT, SEACRAFT,
    TRACK).
    """

    coa_metrics: Optional[List[CoaMetric]] = FieldInfo(alias="coaMetrics", default=None)
    """List of COA metrics associated with this effect response."""

    collateral_damage_est: Optional[float] = FieldInfo(alias="collateralDamageEst", default=None)
    """The collateral damage estimate (CDE) of the munition being fired."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    decision_deadline: Optional[datetime] = FieldInfo(alias="decisionDeadline", default=None)
    """
    The deadline time to accept this COA before it's no longer valid, in ISO8601 UTC
    format.
    """

    external_actions: Optional[List[str]] = FieldInfo(alias="externalActions", default=None)
    """List of external actions to be executed as part of this task."""

    external_request_id: Optional[str] = FieldInfo(alias="externalRequestId", default=None)
    """The external system identifier of the associated effect request.

    A human readable unique id.
    """

    id_effect_request: Optional[str] = FieldInfo(alias="idEffectRequest", default=None)
    """Unique identifier of the EffectRequest associated with this response."""

    munition_id: Optional[str] = FieldInfo(alias="munitionId", default=None)
    """Unique identifier of the munition."""

    munition_type: Optional[str] = FieldInfo(alias="munitionType", default=None)
    """The type of munition being fired."""

    origin: Optional[str] = None
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_network: Optional[str] = FieldInfo(alias="origNetwork", default=None)
    """
    The originating source network on which this record was created, auto-populated
    by the system.
    """

    probability_of_kill: Optional[float] = FieldInfo(alias="probabilityOfKill", default=None)
    """The probability of kill (0-1) of the target being destroyed."""

    red_target_src_id: Optional[str] = FieldInfo(alias="redTargetSrcId", default=None)
    """
    The record ID, depending on the type identified in redTargetSrcType, of the red
    force target. If the redTargetSrcType is POI or TRACK, then this identifier
    corresponds to either poi.poiid or track.trkId from their respective schemas.
    """

    red_target_src_type: Optional[str] = FieldInfo(alias="redTargetSrcType", default=None)
    """The source type of the targetId identifier (POI, SITE, TRACK)."""

    red_time_to_overhead: Optional[datetime] = FieldInfo(alias="redTimeToOverhead", default=None)
    """
    The time to overhead for the red force to be over their target, in ISO8601 UTC
    format.
    """

    shots_required: Optional[int] = FieldInfo(alias="shotsRequired", default=None)
    """The number of shots required to destroy target."""
