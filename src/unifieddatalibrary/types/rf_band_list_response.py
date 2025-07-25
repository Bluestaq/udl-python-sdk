# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RfBandListResponse"]


class RfBandListResponse(BaseModel):
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

    id_entity: str = FieldInfo(alias="idEntity")
    """Unique identifier of the parent Entity which uses this band."""

    name: str
    """RF Band name."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    band: Optional[str] = None
    """Name of the band of this RF range (e.g.

    X,K,Ku,Ka,L,S,C,UHF,VHF,EHF,SHF,UNK,VLF,HF,E,Q,V,W). See RFBandType for more
    details and descriptions of each band name.
    """

    bandwidth: Optional[float] = None
    """RF Band frequency range bandwidth in Mhz."""

    beamwidth: Optional[float] = None
    """
    Angle between the half-power (-3 dB) points of the main lobe of the antenna, in
    degrees.
    """

    center_freq: Optional[float] = FieldInfo(alias="centerFreq", default=None)
    """Center frequency of RF frequency range, if applicable, in Mhz."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    edge_gain: Optional[float] = FieldInfo(alias="edgeGain", default=None)
    """RF Range edge gain, in dBi."""

    eirp: Optional[float] = None
    """
    EIRP is defined as the RMS power input in decibel watts required to a lossless
    half-wave dipole antenna to give the same maximum power density far from the
    antenna as the actual transmitter. It is equal to the power input to the
    transmitter's antenna multiplied by the antenna gain relative to a half-wave
    dipole. Effective radiated power and effective isotropic radiated power both
    measure the amount of power a radio transmitter and antenna (or other source of
    electromagnetic waves) radiates in a specific direction: in the direction of
    maximum signal strength (the "main lobe") of its radiation pattern.
    """

    erp: Optional[float] = None
    """
    Effective Radiated Power (ERP) is the total power in decibel watts radiated by
    an actual antenna relative to a half-wave dipole rather than a theoretical
    isotropic antenna. A half-wave dipole has a gain of 2.15 dB compared to an
    isotropic antenna. EIRP(dB) = ERP (dB)+2.15 dB or EIRP (W) = 1.64\\**ERP(W).
    Effective radiated power and effective isotropic radiated power both measure the
    amount of power a radio transmitter and antenna (or other source of
    electromagnetic waves) radiates in a specific direction: in the direction of
    maximum signal strength (the "main lobe") of its radiation pattern.
    """

    freq_max: Optional[float] = FieldInfo(alias="freqMax", default=None)
    """End/maximum of transmit RF frequency range, if applicable, in Mhz."""

    freq_min: Optional[float] = FieldInfo(alias="freqMin", default=None)
    """Start/minimum of transmit RF frequency range, if applicable, in Mhz."""

    mode: Optional[Literal["TX", "RX"]] = None
    """RF Band mode (e.g. TX, RX)."""

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

    peak_gain: Optional[float] = FieldInfo(alias="peakGain", default=None)
    """RF Range maximum gain, in dBi."""

    polarization: Optional[Literal["H", "V", "R", "L"]] = None
    """Transponder polarization e.g.

    H - (Horizontally Polarized) Perpendicular to Earth's surface, V - (Vertically
    Polarized) Parallel to Earth's surface, L - (Left Hand Circularly Polarized)
    Rotating left relative to the Earth's surface, R - (Right Hand Circularly
    Polarized) Rotating right relative to the Earth's surface.
    """

    purpose: Optional[Literal["COMM", "TTC", "OPS", "OTHER"]] = None
    """
    Purpose or use of the RF Band -- COMM = communications, TTC =
    Telemetry/Tracking/Control, OPS = Operations, OTHER = Other).
    """
