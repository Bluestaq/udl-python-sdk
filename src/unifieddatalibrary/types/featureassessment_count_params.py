# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FeatureassessmentCountParams"]


class FeatureassessmentCountParams(TypedDict, total=False):
    id_analytic_imagery: Required[Annotated[str, PropertyInfo(alias="idAnalyticImagery")]]
    """
    Unique identifier of the Analytic Imagery associated with this Feature
    Assessment record.
    """
