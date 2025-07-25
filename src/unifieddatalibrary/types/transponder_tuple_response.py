# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .channel_full import ChannelFull

__all__ = ["TransponderTupleResponse", "TransponderTupleResponseItem"]


class TransponderTupleResponseItem(BaseModel):
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

    id_comm: str = FieldInfo(alias="idComm")
    """ID of the parent Comm object for this transponder."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    channels: Optional[List[ChannelFull]] = None
    """Collection of Channels for this Transponder."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    fec: Optional[int] = None
    """Forward error correction, e.g.

    0=Auto, 1 = 1/2, 2 = 2/3, 3 = 3/4, 4 = 5/6, 5 = 7/8, 6 = 8/9, 7 = 3/5, 8 = 4/5,
    9 = 9/10, 15 = None.
    """

    format: Optional[str] = None
    """Format."""

    modulation: Optional[str] = None
    """Transponder modulation, e.g. Auto, QPSK, 8PSK."""

    name: Optional[str] = None
    """Optional name of the transponder."""

    nid: Optional[str] = None
    """Optional external network id as provided data source."""

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

    symbol_rate: Optional[float] = FieldInfo(alias="symbolRate", default=None)
    """
    Symbol rate is the number of symbol changes, waveform changes, or signaling
    events, across the transmission medium per time unit using a digitally modulated
    signal or a line code. Also measured in Hz.
    """

    system: Optional[str] = None
    """Transponder system, e.g. DVB-S, DVB-S2."""

    tid: Optional[str] = None
    """Optional external transponder id as provided data source."""

    ttf: Optional[float] = None
    """Transponder Translation Factor.

    This is the frequency difference between the uplink received by a satellite, and
    the downlink transmitted back. It varies satellite to satellite dependent on the
    mission.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was last updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """


TransponderTupleResponse: TypeAlias = List[TransponderTupleResponseItem]
