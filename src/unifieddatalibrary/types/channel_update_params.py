# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChannelUpdateParams"]


class ChannelUpdateParams(TypedDict, total=False):
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

    id_transponder: Required[Annotated[str, PropertyInfo(alias="idTransponder")]]
    """ID of the parent transponder object for this Channel."""

    name: Required[str]
    """Channel name."""

    source: Required[str]
    """Source of the data."""

    body_id: Annotated[str, PropertyInfo(alias="id")]
    """Unique identifier of the record, auto-generated by the system."""

    apid: str
    """Channel aPid."""

    beam_name: Annotated[str, PropertyInfo(alias="beamName")]
    """The antenna beam ID of the particular beam for this channel.

    beamName is not unique across payloads.
    """

    compression: str
    """Channel compression."""

    encryption: str
    """Channel encryption."""

    id_beam: Annotated[str, PropertyInfo(alias="idBeam")]
    """Identifier of the particular beam for this channel."""

    id_rf_band: Annotated[str, PropertyInfo(alias="idRFBand")]
    """ID of the RF Band object for this channel."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    owner: str
    """Owner."""

    pkg: str
    """Pkg."""

    res: str
    """Res."""

    sid: str
    """SID."""

    type: str
    """Channel type."""

    vpid: str
    """Channel vPid."""
