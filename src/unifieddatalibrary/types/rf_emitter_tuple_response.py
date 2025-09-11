# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.entity_full import EntityFull

__all__ = [
    "RfEmitterTupleResponse",
    "RfEmitterTupleResponseItem",
    "RfEmitterTupleResponseItemRfEmitterDetail",
    "RfEmitterTupleResponseItemRfEmitterDetailAmplifier",
    "RfEmitterTupleResponseItemRfEmitterDetailAntenna",
    "RfEmitterTupleResponseItemRfEmitterDetailAntennaFeed",
    "RfEmitterTupleResponseItemRfEmitterDetailAntennaReceiverChannel",
    "RfEmitterTupleResponseItemRfEmitterDetailAntennaTransmitChannel",
    "RfEmitterTupleResponseItemRfEmitterDetailPowerOffset",
    "RfEmitterTupleResponseItemRfEmitterDetailService",
    "RfEmitterTupleResponseItemRfEmitterDetailTtp",
    "RfEmitterTupleResponseItemRfEmitterDetailTtpTechniqueDefinition",
    "RfEmitterTupleResponseItemRfEmitterDetailTtpTechniqueDefinitionParamDefinition",
]


class RfEmitterTupleResponseItemRfEmitterDetailAmplifier(BaseModel):
    device_identifier: Optional[str] = FieldInfo(alias="deviceIdentifier", default=None)
    """The device identifier of the amplifier."""

    manufacturer: Optional[str] = None
    """The manufacturer of the amplifier."""

    api_model_name: Optional[str] = FieldInfo(alias="modelName", default=None)
    """The model name of the amplifier."""

    power: Optional[float] = None
    """The amplifier power level, in watts."""


class RfEmitterTupleResponseItemRfEmitterDetailAntennaFeed(BaseModel):
    freq_max: Optional[float] = FieldInfo(alias="freqMax", default=None)
    """Maximum frequency, in megahertz."""

    freq_min: Optional[float] = FieldInfo(alias="freqMin", default=None)
    """Minimum frequency, in megahertz."""

    name: Optional[str] = None
    """The feed name."""

    polarization: Optional[str] = None
    """The antenna feed linear/circular polarization (e.g.

    HORIZONTAL, VERTICAL, LEFT_HAND_CIRCULAR, RIGHT_HAND_CIRCULAR).
    """


class RfEmitterTupleResponseItemRfEmitterDetailAntennaReceiverChannel(BaseModel):
    bandwidth: Optional[float] = None
    """
    The receiver bandwidth, in megahertz, must satisfy the constraint: minBandwidth
    ≤ bandwidth ≤ maxBandwidth.
    """

    channel_num: Optional[str] = FieldInfo(alias="channelNum", default=None)
    """The receive channel number."""

    device_identifier: Optional[str] = FieldInfo(alias="deviceIdentifier", default=None)
    """The receive channel device identifier."""

    freq_max: Optional[float] = FieldInfo(alias="freqMax", default=None)
    """Maximum frequency, in megahertz."""

    freq_min: Optional[float] = FieldInfo(alias="freqMin", default=None)
    """Minimum frequency, in megahertz."""

    max_bandwidth: Optional[float] = FieldInfo(alias="maxBandwidth", default=None)
    """
    The maximum receiver bandwidth, in megahertz, must satisfy the constraint:
    minBandwidth ≤ bandwidth ≤ maxBandwidth.
    """

    min_bandwidth: Optional[float] = FieldInfo(alias="minBandwidth", default=None)
    """
    The receiver bandwidth, in megahertz, must satisfy the constraint: minBandwidth
    ≤ bandwidth ≤ maxBandwidth.
    """

    sensitivity: Optional[float] = None
    """Receiver sensitivity, in decibel-milliwatts."""


class RfEmitterTupleResponseItemRfEmitterDetailAntennaTransmitChannel(BaseModel):
    power: float
    """Transmit power, in watts."""

    bandwidth: Optional[float] = None
    """
    The transmitter bandwidth, in megahertz, must satisfy the constraint:
    minBandwidth ≤ bandwidth ≤ maxBandwidth.
    """

    channel_num: Optional[str] = FieldInfo(alias="channelNum", default=None)
    """The transmit channel number."""

    device_identifier: Optional[str] = FieldInfo(alias="deviceIdentifier", default=None)
    """The transmit channel device identifier."""

    freq: Optional[float] = None
    """
    The transmitter frequency, in megahertz, must satisfy the constraint: freqMin <=
    freq <= freqMax.
    """

    freq_max: Optional[float] = FieldInfo(alias="freqMax", default=None)
    """
    The maximum transmitter frequency, in megahertz, must satisfy the constraint:
    freqMin ≤ freq ≤ freqMax.
    """

    freq_min: Optional[float] = FieldInfo(alias="freqMin", default=None)
    """
    The minimum transmitter frequency, in megahertz, must satisfy the constraint:
    freqMin ≤ freq ≤ freqMax.
    """

    hardware_sample_rate: Optional[int] = FieldInfo(alias="hardwareSampleRate", default=None)
    """The hardware sample rate, in bits per second for this transmit channel."""

    max_bandwidth: Optional[float] = FieldInfo(alias="maxBandwidth", default=None)
    """
    The maximum transmitter bandwidth, in megahertz, must satisfy the constraint:
    minBandwidth ≤ bandwidth ≤ maxBandwidth.
    """

    max_gain: Optional[float] = FieldInfo(alias="maxGain", default=None)
    """Maximum gain, in decibels."""

    min_bandwidth: Optional[float] = FieldInfo(alias="minBandwidth", default=None)
    """
    The minimum transmitter bandwidth, in megahertz, must satisfy the constraint:
    minBandwidth ≤ bandwidth ≤ maxBandwidth.
    """

    min_gain: Optional[float] = FieldInfo(alias="minGain", default=None)
    """Minimum gain, in decibels."""

    sample_rates: Optional[List[float]] = FieldInfo(alias="sampleRates", default=None)
    """The set of sample rates supported by this transmit channel, in bits per second."""


class RfEmitterTupleResponseItemRfEmitterDetailAntenna(BaseModel):
    antenna_diameter: Optional[float] = FieldInfo(alias="antennaDiameter", default=None)
    """For parabolic/dish antennas, the diameter of the antenna in meters."""

    antenna_size: Optional[List[float]] = FieldInfo(alias="antennaSize", default=None)
    """
    Array with 1-2 values specifying the length and width (for rectangular) and just
    length for dipole antennas in meters.
    """

    az_el_fixed: Optional[bool] = FieldInfo(alias="azElFixed", default=None)
    """A flag to indicate whether the antenna points at a fixed azimuth/elevation."""

    feeds: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailAntennaFeed]] = None
    """The set of antenna feeds for this antenna."""

    fixed_azimuth: Optional[float] = FieldInfo(alias="fixedAzimuth", default=None)
    """Antenna azimuth, in degrees clockwise from true North, for a fixed antenna."""

    fixed_elevation: Optional[float] = FieldInfo(alias="fixedElevation", default=None)
    """Antenna elevation, in degrees, for a fixed antenna."""

    max_azimuths: Optional[List[float]] = FieldInfo(alias="maxAzimuths", default=None)
    """Array of maximum azimuths, in degrees."""

    max_elevation: Optional[float] = FieldInfo(alias="maxElevation", default=None)
    """Maximum elevation, in degrees."""

    min_azimuths: Optional[List[float]] = FieldInfo(alias="minAzimuths", default=None)
    """Array of minimum azimuths, in degrees."""

    min_elevation: Optional[float] = FieldInfo(alias="minElevation", default=None)
    """Minimum elevation, in degrees."""

    name: Optional[str] = None
    """The name of the antenna."""

    receiver_channels: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailAntennaReceiverChannel]] = FieldInfo(
        alias="receiverChannels", default=None
    )
    """The set of receiver channels for this antenna."""

    transmit_channels: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailAntennaTransmitChannel]] = FieldInfo(
        alias="transmitChannels", default=None
    )
    """The set of transmit channels for this antenna."""


class RfEmitterTupleResponseItemRfEmitterDetailPowerOffset(BaseModel):
    frequency_band: Optional[str] = FieldInfo(alias="frequencyBand", default=None)
    """The RF frequency band (e.g. HF, VHF, P, UHF, L, S, C, X, KU, K, KA, V, W, MM)."""

    power_offset: Optional[float] = FieldInfo(alias="powerOffset", default=None)
    """Power offset, in decibels."""


class RfEmitterTupleResponseItemRfEmitterDetailService(BaseModel):
    name: Optional[str] = None
    """The name for this software service."""

    version: Optional[str] = None
    """The version for this software service."""


class RfEmitterTupleResponseItemRfEmitterDetailTtpTechniqueDefinitionParamDefinition(BaseModel):
    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
    """Default parameter value used if not overridden in a SEW task definition."""

    max: Optional[float] = None
    """Maximum allowable value for a numeric parameter."""

    min: Optional[float] = None
    """Minimum allowable value for a numeric parameter."""

    name: Optional[str] = None
    """The name of the parameter."""

    optional: Optional[bool] = None
    """A flag to specify that a parameter is optional."""

    type: Optional[str] = None
    """The type of parameter (e.g. STRING, DOUBLE, INT, LIST)."""

    units: Optional[str] = None
    """Units (degrees, seconds, decibels, etc.) for a numeric parameter."""

    valid_values: Optional[List[str]] = FieldInfo(alias="validValues", default=None)
    """Valid values for strictly defined parameters."""


class RfEmitterTupleResponseItemRfEmitterDetailTtpTechniqueDefinition(BaseModel):
    name: Optional[str] = None
    """The EW Emitter system technique name."""

    param_definitions: Optional[
        List[RfEmitterTupleResponseItemRfEmitterDetailTtpTechniqueDefinitionParamDefinition]
    ] = FieldInfo(alias="paramDefinitions", default=None)
    """The set of required/optional parameters for this technique."""


class RfEmitterTupleResponseItemRfEmitterDetailTtp(BaseModel):
    output_signal_name: Optional[str] = FieldInfo(alias="outputSignalName", default=None)
    """The name of the output signal."""

    technique_definitions: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailTtpTechniqueDefinition]] = FieldInfo(
        alias="techniqueDefinitions", default=None
    )
    """The set of TTPs affected by this signal."""


class RfEmitterTupleResponseItemRfEmitterDetail(BaseModel):
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

    id_rf_emitter: str = FieldInfo(alias="idRFEmitter")
    """Unique identifier of the parent RF Emitter."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    alternate_facility_name: Optional[str] = FieldInfo(alias="alternateFacilityName", default=None)
    """Alternate facility name for this RF Emitter."""

    alt_name: Optional[str] = FieldInfo(alias="altName", default=None)
    """Optional alternate name or alias for this RF Emitter."""

    amplifier: Optional[RfEmitterTupleResponseItemRfEmitterDetailAmplifier] = None
    """An RF Amplifier associated with an RF Emitter Details."""

    antennas: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailAntenna]] = None
    """The set of antennas hosted on this EW Emitter system."""

    barrage_noise_bandwidth: Optional[float] = FieldInfo(alias="barrageNoiseBandwidth", default=None)
    """Barrage noise bandwidth, in megahertz."""

    bit_run_time: Optional[float] = FieldInfo(alias="bitRunTime", default=None)
    """
    The length of time, in seconds, for the RF Emitter built-in test to run to
    completion.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    description: Optional[str] = None
    """Detailed description of the RF Emitter."""

    designator: Optional[str] = None
    """Designator of this RF Emitter."""

    doppler_noise: Optional[float] = FieldInfo(alias="dopplerNoise", default=None)
    """Doppler noise value, in megahertz."""

    drfm_instantaneous_bandwidth: Optional[float] = FieldInfo(alias="drfmInstantaneousBandwidth", default=None)
    """Digital Form Radio Memory instantaneous bandwidth in megahertz."""

    family: Optional[str] = None
    """Family of this RF Emitter type."""

    fixed_attenuation: Optional[float] = FieldInfo(alias="fixedAttenuation", default=None)
    """
    A fixed attenuation value to be set on the SRF Emitter HPA when commanding an
    Electronic Attack/Techniques Tactics and Procedures task, in decibels.
    """

    id_manufacturer_org: Optional[str] = FieldInfo(alias="idManufacturerOrg", default=None)
    """Unique identifier of the organization which manufactured this RF Emitter."""

    id_production_facility_location: Optional[str] = FieldInfo(alias="idProductionFacilityLocation", default=None)
    """
    Unique identifier of the location of the production facility for this RF
    Emitter.
    """

    loaned_to_cocom: Optional[str] = FieldInfo(alias="loanedToCocom", default=None)
    """
    COCOM that has temporary responsibility for scheduling and management of the RF
    Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
    SPACEFOR-STRATNORTH, SPACESOC, NONE).
    """

    notes: Optional[str] = None
    """Notes on the RF Emitter."""

    num_bits: Optional[int] = FieldInfo(alias="numBits", default=None)
    """Number of bits."""

    num_channels: Optional[int] = FieldInfo(alias="numChannels", default=None)
    """Number of channels."""

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

    power_offsets: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailPowerOffset]] = FieldInfo(
        alias="powerOffsets", default=None
    )
    """
    A set of system/frequency band adjustments to the power offset commanded in an
    EA/TTP task.
    """

    prep_time: Optional[float] = FieldInfo(alias="prepTime", default=None)
    """
    The length of time, in seconds, for the RF Emitter to prepare for a task,
    including sufficient time to slew the antenna and configure the equipment.
    """

    primary_cocom: Optional[str] = FieldInfo(alias="primaryCocom", default=None)
    """
    Primary COCOM that is responsible for scheduling and management of the RF
    Emitter (e.g. SPACEFOR-CENT, SPACEFOR-EURAF, SPACEFOR-INDOPAC, SPACEFOR-KOR,
    SPACEFOR-STRATNORTH, SPACESOC, NONE).
    """

    production_facility_name: Optional[str] = FieldInfo(alias="productionFacilityName", default=None)
    """Name of the production facility for this RF Emitter."""

    receiver_type: Optional[str] = FieldInfo(alias="receiverType", default=None)
    """Type or name of receiver."""

    secondary_notes: Optional[str] = FieldInfo(alias="secondaryNotes", default=None)
    """Secondary notes on the RF Emitter."""

    services: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailService]] = None
    """The set of software services running on this EW Emitter system."""

    system_sensitivity_end: Optional[float] = FieldInfo(alias="systemSensitivityEnd", default=None)
    """
    Receiver sensitivity is the lowest power level at which the receiver can detect
    an RF signal and demodulate data. Sensitivity is purely a receiver specification
    and is independent of the transmitter. End sensitivity range, in
    decibel-milliwatts.
    """

    system_sensitivity_start: Optional[float] = FieldInfo(alias="systemSensitivityStart", default=None)
    """
    Receiver sensitivity is the lowest power level at which the receiver can detect
    an RF signal and demodulate data. Sensitivity is purely a receiver specification
    and is independent of the transmitter. Start sensitivity range, in
    decibel-milliwatts.
    """

    ttps: Optional[List[RfEmitterTupleResponseItemRfEmitterDetailTtp]] = None
    """The set of EA/TTP techniques that are supported by this EW Emitter system."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was last updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    urls: Optional[List[str]] = None
    """Array of URLs containing additional information on this RF Emitter."""


class RfEmitterTupleResponseItem(BaseModel):
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

    name: str
    """Unique name of this RF Emitter."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    entity: Optional[EntityFull] = None
    """
    An entity is a generic representation of any object within a space/SSA system
    such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
    entity can have an operating unit, a location (if terrestrial), and statuses.
    """

    ext_sys_id: Optional[str] = FieldInfo(alias="extSysId", default=None)
    """The originating system ID for the RF Emitter."""

    id_entity: Optional[str] = FieldInfo(alias="idEntity", default=None)
    """ID by reference of the parent entity for this RFEmitter."""

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

    rf_emitter_details: Optional[List[RfEmitterTupleResponseItemRfEmitterDetail]] = FieldInfo(
        alias="rfEmitterDetails", default=None
    )
    """Details about this RF Emitter."""

    subtype: Optional[str] = None
    """The RF Emitter subtype, which can distinguish specialized deployments (e.g.

    BLOCK_0_AVL, BLOCK_0_DS1, BLOCK_0_TEST, BLOCK_1, BLOCK_1_TEST, NONE).
    """

    type: Optional[str] = None
    """Type of this RF Emitter."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was last updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """


RfEmitterTupleResponse: TypeAlias = List[RfEmitterTupleResponseItem]
