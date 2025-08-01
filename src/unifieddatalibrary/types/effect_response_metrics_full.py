# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EffectResponseMetricsFull"]


class EffectResponseMetricsFull(BaseModel):
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
