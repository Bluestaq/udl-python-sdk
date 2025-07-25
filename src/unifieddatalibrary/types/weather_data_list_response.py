# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WeatherDataListResponse"]


class WeatherDataListResponse(BaseModel):
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

    ob_time: datetime = FieldInfo(alias="obTime")
    """
    Datetime of the weather observation in ISO 8601 UTC datetime format with
    microsecond precision.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    angle_orientation: Optional[float] = FieldInfo(alias="angleOrientation", default=None)
    """
    Angle of orientation of the 50% positional confidence ellipse, in degrees
    clockwise from true north.
    """

    avg_ref_pwr: Optional[float] = FieldInfo(alias="avgRefPwr", default=None)
    """Average power of the reflected signal received by the radar, in Watts."""

    avg_tx_pwr: Optional[float] = FieldInfo(alias="avgTxPwr", default=None)
    """Average transmitted power of the radar, in kilowatts."""

    checksum: Optional[int] = None
    """Checksum value for the data."""

    co_integs: Optional[List[int]] = FieldInfo(alias="coIntegs", default=None)
    """
    Array of the number(s) of measurements used in coherent integrations used for
    radar data processing. Users should consult the data provider for information on
    the coherent integrations array structure.
    """

    cons_recs: Optional[List[int]] = FieldInfo(alias="consRecs", default=None)
    """Array of the number(s) of records in consensus for a radar beam.

    Users should consult the data provider for information on the consensus records
    array structure.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """Application user who created the row in the database."""

    dopp_vels: Optional[List[float]] = FieldInfo(alias="doppVels", default=None)
    """
    Array of full scale Nyquist Doppler velocities measured by radar, in meters per
    second. Nyquist velocity refers to the maximum velocity magnitude that the radar
    system can unambiguously detect. Doppler velocities with absolute values
    exceeding the Nyquist threshold suffer from aliasing at the time of collection.
    Users should consult the data provider for information on the doppler velocities
    array structure.
    """

    file_creation: Optional[datetime] = FieldInfo(alias="fileCreation", default=None)
    """Datetime the system files were created."""

    first_guess_avgs: Optional[List[int]] = FieldInfo(alias="firstGuessAvgs", default=None)
    """
    Array of average maximum number(s) of consecutive instances in which the same
    first guess velocity is used in radar data processing to estimate wind speed.
    Users should consult the data provider for information on the first guess
    averages array structure.
    """

    id_sensor: Optional[str] = FieldInfo(alias="idSensor", default=None)
    """Unique identifier of the sensor making the weather measurement."""

    interpulse_periods: Optional[List[float]] = FieldInfo(alias="interpulsePeriods", default=None)
    """
    Array of the elapsed time(s) from the beginning of one pulse to the beginning of
    the next pulse for a radar beam, in microseconds. Users should consult the data
    provider for information on the interpulse periods array structure.
    """

    light_det_sensors: Optional[List[int]] = FieldInfo(alias="lightDetSensors", default=None)
    """
    Array of sensor(s) that participated in the lightning event location
    determination.
    """

    light_event_num: Optional[int] = FieldInfo(alias="lightEventNum", default=None)
    """Number of sensors used in the lightning event location solution."""

    noise_lvls: Optional[List[float]] = FieldInfo(alias="noiseLvls", default=None)
    """Array of noise level(s) measured by radar, in decibels.

    Users should consult the data provider for information on the noise levels array
    structure.
    """

    num_elements: Optional[int] = FieldInfo(alias="numElements", default=None)
    """Number of antennas across all sectors within the radar coverage area."""

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

    orig_sensor_id: Optional[str] = FieldInfo(alias="origSensorId", default=None)
    """Optional identifier provided by the record source.

    This may be an internal identifier and not necessarily a valid sensor ID.
    """

    pos_confidence: Optional[float] = FieldInfo(alias="posConfidence", default=None)
    """
    The positional confidence of the calculated lightning event location using the
    chi-square statistical method.
    """

    qc_value: Optional[int] = FieldInfo(alias="qcValue", default=None)
    """Quality control flag value, as defined by the data provider."""

    sector_num: Optional[int] = FieldInfo(alias="sectorNum", default=None)
    """
    Number of sectors within the radar coverage area, each containing a number of
    antennas.
    """

    semi_major_axis: Optional[float] = FieldInfo(alias="semiMajorAxis", default=None)
    """Semi-major axis of the 50% positional confidence ellipse, in kilometers."""

    semi_minor_axis: Optional[float] = FieldInfo(alias="semiMinorAxis", default=None)
    """Semi-minor axis of the 50% positional confidence ellipse, in kilometers."""

    sig_pwrs: Optional[List[float]] = FieldInfo(alias="sigPwrs", default=None)
    """Array of signal power(s) measured by the sensor, in decibels.

    Users should consult the data provider for information on the signal powers
    array structure.
    """

    sig_strength: Optional[float] = FieldInfo(alias="sigStrength", default=None)
    """
    Signal strength of the electromagnetic energy received due to a lightning event,
    in kiloamps.
    """

    snrs: Optional[List[float]] = None
    """Array of signal to noise ratio(s) for a radar beam, in decibels.

    Users should consult the data provider for information on the signal to noise
    ratios array structure.
    """

    spec_avgs: Optional[List[int]] = FieldInfo(alias="specAvgs", default=None)
    """Array of the number(s) of spectral averages used in radar data processing.

    Users should consult the data provider for information on the spectral averages
    array structure.
    """

    spec_widths: Optional[List[float]] = FieldInfo(alias="specWidths", default=None)
    """
    Array of width(s) of the distribution in Doppler velocity measured by radar, in
    meters/second. Spectral width depends on the particle size distribution, the
    wind shear across the radar beam, and turbulence. Users should consult the data
    provider for information on the spectral widths array structure.
    """

    src_ids: Optional[List[str]] = FieldInfo(alias="srcIds", default=None)
    """
    Array of UUID(s) of the UDL data record(s) that are related to this WeatherData
    record. See the associated 'srcTyps' array for the specific types of data,
    positionally corresponding to the UUIDs in this array. The 'srcTyps' and
    'srcIds' arrays must match in size. See the corresponding srcTyps array element
    for the data type of the UUID and use the appropriate API operation to retrieve
    that object.
    """

    src_typs: Optional[List[str]] = FieldInfo(alias="srcTyps", default=None)
    """
    Array of UDL record types (SENSOR, WEATHERREPORT) that are related to this
    WeatherData record. See the associated 'srcIds' array for the record UUIDs,
    positionally corresponding to the record types in this array. The 'srcTyps' and
    'srcIds' arrays must match in size.
    """

    td_avg_sample_nums: Optional[List[int]] = FieldInfo(alias="tdAvgSampleNums", default=None)
    """
    Array of the number(s) of radar samples used in time domain averaging for radar
    data processing. Time domain averaging improves the quality of the measured
    signal by reducing random noise and enhancing the signal-to-noise ratio. Users
    should consult the data provider for information on the time domain sample
    numbers array structure.
    """

    term_alt: Optional[float] = FieldInfo(alias="termAlt", default=None)
    """Last altitude with recorded measurements in this record, in meters."""
