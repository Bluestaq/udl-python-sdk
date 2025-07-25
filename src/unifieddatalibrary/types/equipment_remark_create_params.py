# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EquipmentRemarkCreateParams"]


class EquipmentRemarkCreateParams(TypedDict, total=False):
    classification_marking: Required[Annotated[str, PropertyInfo(alias="classificationMarking")]]
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    data_mode: Required[Annotated[Literal["REAL", "TEST", "SIMULATED", "EXERCISE"], PropertyInfo(alias="dataMode")]]
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

    id_equipment: Required[Annotated[str, PropertyInfo(alias="idEquipment")]]
    """The ID of the Equipment to which this remark applies."""

    source: Required[str]
    """Source of the data."""

    text: Required[str]
    """The text of the remark."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    alt_rmk_id: Annotated[str, PropertyInfo(alias="altRmkId")]
    """Unique identifier of the Equipment Remark record from the originating system."""

    code: str
    """The remark type identifier.

    For example, the Mobility Air Forces (MAF) remark code, defined in the Airfield
    Suitability and Restriction Report (ASRR).
    """

    name: str
    """The name of the remark."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    type: str
    """The remark type (e.g. Caution, Information, Misc, Restriction, etc.)."""
