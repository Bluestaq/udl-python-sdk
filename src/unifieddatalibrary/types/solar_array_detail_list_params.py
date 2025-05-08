# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SolarArrayDetailListParams"]


class SolarArrayDetailListParams(TypedDict, total=False):
    classification_marking: Annotated[str, PropertyInfo(alias="classificationMarking")]
    """
    (One or more of fields 'classificationMarking, dataMode, source' are required.)
    Classification marking of the data in IC/CAPCO Portion-marked format.
    """

    data_mode: Annotated[str, PropertyInfo(alias="dataMode")]
    """
    (One or more of fields 'classificationMarking, dataMode, source' are required.)
    Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data. (REAL,
    TEST, SIMULATED, or EXERCISE)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    source: str
    """
    (One or more of fields 'classificationMarking, dataMode, source' are required.)
    Source of the data.
    """
