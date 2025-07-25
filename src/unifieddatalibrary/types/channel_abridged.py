# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ChannelAbridged"]


class ChannelAbridged(BaseModel):
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

    id_transponder: str = FieldInfo(alias="idTransponder")
    """ID of the parent transponder object for this Channel."""

    name: str
    """Channel name."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    apid: Optional[str] = None
    """Channel aPid."""

    beam_name: Optional[str] = FieldInfo(alias="beamName", default=None)
    """The antenna beam ID of the particular beam for this channel.

    beamName is not unique across payloads.
    """

    compression: Optional[str] = None
    """Channel compression."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    encryption: Optional[str] = None
    """Channel encryption."""

    id_beam: Optional[str] = FieldInfo(alias="idBeam", default=None)
    """Identifier of the particular beam for this channel."""

    id_rf_band: Optional[str] = FieldInfo(alias="idRFBand", default=None)
    """ID of the RF Band object for this channel."""

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

    owner: Optional[str] = None
    """Owner."""

    pkg: Optional[str] = None
    """Pkg."""

    res: Optional[str] = None
    """Res."""

    sid: Optional[str] = None
    """SID."""

    type: Optional[str] = None
    """Channel type."""

    vpid: Optional[str] = None
    """Channel vPid."""
