# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WeatherDataCreateBulkParams", "Body"]


class WeatherDataCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
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

    ob_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="obTime", format="iso8601")]]
    """
    Datetime of the weather observation in ISO 8601 UTC datetime format with
    microsecond precision.
    """

    source: Required[str]
    """Source of the data."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    angle_orientation: Annotated[float, PropertyInfo(alias="angleOrientation")]
    """
    Angle of orientation of the 50% positional confidence ellipse, in degrees
    clockwise from true north.
    """

    avg_ref_pwr: Annotated[float, PropertyInfo(alias="avgRefPwr")]
    """Average power of the reflected signal received by the radar, in Watts."""

    avg_tx_pwr: Annotated[float, PropertyInfo(alias="avgTxPwr")]
    """Average transmitted power of the radar, in kilowatts."""

    checksum: int
    """Checksum value for the data."""

    co_integs: Annotated[Iterable[int], PropertyInfo(alias="coIntegs")]
    """
    Array of the number(s) of measurements used in coherent integrations used for
    radar data processing. Users should consult the data provider for information on
    the coherent integrations array structure.
    """

    cons_recs: Annotated[Iterable[int], PropertyInfo(alias="consRecs")]
    """Array of the number(s) of records in consensus for a radar beam.

    Users should consult the data provider for information on the consensus records
    array structure.
    """

    dopp_vels: Annotated[Iterable[float], PropertyInfo(alias="doppVels")]
    """
    Array of full scale Nyquist Doppler velocities measured by radar, in meters per
    second. Nyquist velocity refers to the maximum velocity magnitude that the radar
    system can unambiguously detect. Doppler velocities with absolute values
    exceeding the Nyquist threshold suffer from aliasing at the time of collection.
    Users should consult the data provider for information on the doppler velocities
    array structure.
    """

    file_creation: Annotated[Union[str, datetime], PropertyInfo(alias="fileCreation", format="iso8601")]
    """Datetime the system files were created."""

    first_guess_avgs: Annotated[Iterable[int], PropertyInfo(alias="firstGuessAvgs")]
    """
    Array of average maximum number(s) of consecutive instances in which the same
    first guess velocity is used in radar data processing to estimate wind speed.
    Users should consult the data provider for information on the first guess
    averages array structure.
    """

    id_sensor: Annotated[str, PropertyInfo(alias="idSensor")]
    """Unique identifier of the sensor making the weather measurement."""

    interpulse_periods: Annotated[Iterable[float], PropertyInfo(alias="interpulsePeriods")]
    """
    Array of the elapsed time(s) from the beginning of one pulse to the beginning of
    the next pulse for a radar beam, in microseconds. Users should consult the data
    provider for information on the interpulse periods array structure.
    """

    light_det_sensors: Annotated[Iterable[int], PropertyInfo(alias="lightDetSensors")]
    """
    Array of sensor(s) that participated in the lightning event location
    determination.
    """

    light_event_num: Annotated[int, PropertyInfo(alias="lightEventNum")]
    """Number of sensors used in the lightning event location solution."""

    noise_lvls: Annotated[Iterable[float], PropertyInfo(alias="noiseLvls")]
    """Array of noise level(s) measured by radar, in decibels.

    Users should consult the data provider for information on the noise levels array
    structure.
    """

    num_elements: Annotated[int, PropertyInfo(alias="numElements")]
    """Number of antennas across all sectors within the radar coverage area."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_sensor_id: Annotated[str, PropertyInfo(alias="origSensorId")]
    """Optional identifier provided by the record source.

    This may be an internal identifier and not necessarily a valid sensor ID.
    """

    pos_confidence: Annotated[float, PropertyInfo(alias="posConfidence")]
    """
    The positional confidence of the calculated lightning event location using the
    chi-square statistical method.
    """

    qc_value: Annotated[int, PropertyInfo(alias="qcValue")]
    """Quality control flag value, as defined by the data provider."""

    sector_num: Annotated[int, PropertyInfo(alias="sectorNum")]
    """
    Number of sectors within the radar coverage area, each containing a number of
    antennas.
    """

    semi_major_axis: Annotated[float, PropertyInfo(alias="semiMajorAxis")]
    """Semi-major axis of the 50% positional confidence ellipse, in kilometers."""

    semi_minor_axis: Annotated[float, PropertyInfo(alias="semiMinorAxis")]
    """Semi-minor axis of the 50% positional confidence ellipse, in kilometers."""

    sig_pwrs: Annotated[Iterable[float], PropertyInfo(alias="sigPwrs")]
    """Array of signal power(s) measured by the sensor, in decibels.

    Users should consult the data provider for information on the signal powers
    array structure.
    """

    sig_strength: Annotated[float, PropertyInfo(alias="sigStrength")]
    """
    Signal strength of the electromagnetic energy received due to a lightning event,
    in kiloamps.
    """

    snrs: Iterable[float]
    """Array of signal to noise ratio(s) for a radar beam, in decibels.

    Users should consult the data provider for information on the signal to noise
    ratios array structure.
    """

    spec_avgs: Annotated[Iterable[int], PropertyInfo(alias="specAvgs")]
    """Array of the number(s) of spectral averages used in radar data processing.

    Users should consult the data provider for information on the spectral averages
    array structure.
    """

    spec_widths: Annotated[Iterable[float], PropertyInfo(alias="specWidths")]
    """
    Array of width(s) of the distribution in Doppler velocity measured by radar, in
    meters/second. Spectral width depends on the particle size distribution, the
    wind shear across the radar beam, and turbulence. Users should consult the data
    provider for information on the spectral widths array structure.
    """

    src_ids: Annotated[List[str], PropertyInfo(alias="srcIds")]
    """
    Array of UUID(s) of the UDL data record(s) that are related to this WeatherData
    record. See the associated 'srcTyps' array for the specific types of data,
    positionally corresponding to the UUIDs in this array. The 'srcTyps' and
    'srcIds' arrays must match in size. See the corresponding srcTyps array element
    for the data type of the UUID and use the appropriate API operation to retrieve
    that object.
    """

    src_typs: Annotated[List[str], PropertyInfo(alias="srcTyps")]
    """
    Array of UDL record types (SENSOR, WEATHERREPORT) that are related to this
    WeatherData record. See the associated 'srcIds' array for the record UUIDs,
    positionally corresponding to the record types in this array. The 'srcTyps' and
    'srcIds' arrays must match in size.
    """

    td_avg_sample_nums: Annotated[Iterable[int], PropertyInfo(alias="tdAvgSampleNums")]
    """
    Array of the number(s) of radar samples used in time domain averaging for radar
    data processing. Time domain averaging improves the quality of the measured
    signal by reducing random noise and enhancing the signal-to-noise ratio. Users
    should consult the data provider for information on the time domain sample
    numbers array structure.
    """

    term_alt: Annotated[float, PropertyInfo(alias="termAlt")]
    """Last altitude with recorded measurements in this record, in meters."""
