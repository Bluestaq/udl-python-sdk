# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CalibrationUnvalidatedPublishParams", "Body"]


class CalibrationUnvalidatedPublishParams(TypedDict, total=False):
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

    id_sensor: Required[Annotated[str, PropertyInfo(alias="idSensor")]]
    """Unique identifier of the sensor to which this calibration data applies.

    This ID can be used to obtain additional information on a sensor using the 'get
    by ID' operation (e.g. /udl/sensor/{id}). For example, the sensor with idSensor
    = abc would be queried as /udl/sensor/abc.
    """

    source: Required[str]
    """Source of the data."""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]
    """
    Calibration data span start time in ISO 8601 UTC format with millisecond
    precision.
    """

    id: str
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    az_ra_accel_bias: Annotated[float, PropertyInfo(alias="azRaAccelBias")]
    """
    Sensor azimuth/right-ascension acceleration bias, in degrees per second squared.
    """

    az_ra_accel_sigma: Annotated[float, PropertyInfo(alias="azRaAccelSigma")]
    """
    The standard deviation of the azimuth/right ascension acceleration residuals, in
    degrees, used to determine the sensor azimuth/right-ascension acceleration bias.
    """

    az_ra_bias: Annotated[float, PropertyInfo(alias="azRaBias")]
    """Sensor azimuth/right-ascension bias, in degrees."""

    az_ra_rate_bias: Annotated[float, PropertyInfo(alias="azRaRateBias")]
    """Sensor azimuth/right-ascension rate bias, in degrees per second."""

    az_ra_rate_sigma: Annotated[float, PropertyInfo(alias="azRaRateSigma")]
    """
    The standard deviation of the azimuth/right ascension rate residuals, in
    degrees, used to determine the sensor azimuth/right-ascension rate bias.
    """

    az_ra_rms: Annotated[float, PropertyInfo(alias="azRaRms")]
    """
    The root mean square of the azimuth/right-ascension residuals, in degrees, used
    to determine the sensor azimuth/right-ascension bias.
    """

    az_ra_sigma: Annotated[float, PropertyInfo(alias="azRaSigma")]
    """
    The standard deviation of the azimuth/right ascension residuals, in degrees,
    used to determine the sensor azimuth/right-ascension bias.
    """

    cal_angle_ref: Annotated[str, PropertyInfo(alias="calAngleRef")]
    """Specifies the calibration reference angle set for this calibration data set.

    Azimuth and Elevation (AZEL) or Right Ascension and Declination (RADEC).
    """

    cal_track_mode: Annotated[str, PropertyInfo(alias="calTrackMode")]
    """
    Specifies that the calibration data are from INTRA_TRACK or INTER_TRACK
    residuals.
    """

    cal_type: Annotated[str, PropertyInfo(alias="calType")]
    """
    The basis of calibration values contained in this record (COMPUTED,
    OPERATIONAL).
    """

    confidence_noise_bias: Annotated[float, PropertyInfo(alias="confidenceNoiseBias")]
    """The confidence noise bias of the duration span."""

    duration: float
    """
    Duration of the sensor calibration data which produced these values, measured in
    days.
    """

    ecr: Iterable[float]
    """
    Three element array, expressing the sensor location in Earth Centered Rotating
    (ECR) coordinates, in kilometers. The array element order is [x, y, z].
    """

    el_dec_accel_bias: Annotated[float, PropertyInfo(alias="elDecAccelBias")]
    """Sensor elevation/declination acceleration bias, in degrees per second squared."""

    el_dec_accel_sigma: Annotated[float, PropertyInfo(alias="elDecAccelSigma")]
    """
    The standard deviation of the elevation/declination acceleration residuals, in
    degrees, used to determine the sensor elevation/declination acceleration bias.
    """

    el_dec_bias: Annotated[float, PropertyInfo(alias="elDecBias")]
    """Sensor elevation/declination bias, in degrees."""

    el_dec_rate_bias: Annotated[float, PropertyInfo(alias="elDecRateBias")]
    """Sensor elevation/declination rate bias, in degrees per second."""

    el_dec_rate_sigma: Annotated[float, PropertyInfo(alias="elDecRateSigma")]
    """
    The standard deviation of the elevation/declination rate residuals, in degrees,
    used to determine the sensor elevation/declination rate bias.
    """

    el_dec_rms: Annotated[float, PropertyInfo(alias="elDecRms")]
    """
    The root mean square of the elevation/declination residuals, in degrees, used to
    determine the sensor elevation/declination bias.
    """

    el_dec_sigma: Annotated[float, PropertyInfo(alias="elDecSigma")]
    """
    The standard deviation of the elevation/declination residuals, in degrees, used
    to determine the sensor elevation/declination bias.
    """

    end_time: Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]
    """Calibration data span end time in ISO 8601 UTC format with millisecond
    precision.

    If provided, the endTime must be greater than or equal to the startTime in the
    SensorCalibration record.
    """

    num_az_ra_obs: Annotated[int, PropertyInfo(alias="numAzRaObs")]
    """
    The number of observables used in determining the azimuth or right-ascension
    calibration values.
    """

    num_el_dec_obs: Annotated[int, PropertyInfo(alias="numElDecObs")]
    """
    The number of observables used in determining the elevation or declination
    calibration values.
    """

    num_obs: Annotated[int, PropertyInfo(alias="numObs")]
    """The total number of observables available over the calibration span."""

    num_photo_obs: Annotated[int, PropertyInfo(alias="numPhotoObs")]
    """
    The number of observables used in determining the photometric calibration
    values.
    """

    num_range_obs: Annotated[int, PropertyInfo(alias="numRangeObs")]
    """The number of observables used in determining the range calibration values."""

    num_range_rate_obs: Annotated[int, PropertyInfo(alias="numRangeRateObs")]
    """
    The number of observables used in determining the range rate calibration values.
    """

    num_rcs_obs: Annotated[int, PropertyInfo(alias="numRcsObs")]
    """
    The number of observables used in determining the radar cross section (RCS)
    calibration values.
    """

    num_time_obs: Annotated[int, PropertyInfo(alias="numTimeObs")]
    """The number of observables used in determining the time calibration values."""

    num_tracks: Annotated[int, PropertyInfo(alias="numTracks")]
    """The total number of tracks available over the calibration span."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    photo_bias: Annotated[float, PropertyInfo(alias="photoBias")]
    """The sensor photometric observation magnitude bias, in visual magnitude."""

    photo_sigma: Annotated[float, PropertyInfo(alias="photoSigma")]
    """
    The standard deviation of the magnitude residuals, in visual magnitude, used to
    determine the photometric bias.
    """

    range_accel_bias: Annotated[float, PropertyInfo(alias="rangeAccelBias")]
    """Sensor range rate acceleration bias, in kilometers per second squared."""

    range_accel_sigma: Annotated[float, PropertyInfo(alias="rangeAccelSigma")]
    """
    The standard deviation of the range acceleration residuals, in kilometers per
    second squared, used to determine the sensor range acceleration bias.
    """

    range_bias: Annotated[float, PropertyInfo(alias="rangeBias")]
    """Sensor range bias, in kilometers."""

    range_rate_bias: Annotated[float, PropertyInfo(alias="rangeRateBias")]
    """Sensor range rate bias, in kilometers per second."""

    range_rate_rms: Annotated[float, PropertyInfo(alias="rangeRateRms")]
    """
    The root mean square of the range rate residuals, in kilometers per second, used
    to determine the sensor range rate bias.
    """

    range_rate_sigma: Annotated[float, PropertyInfo(alias="rangeRateSigma")]
    """
    The standard deviation of the range rate residuals, in kilometers per second,
    used to determine the sensor range rate bias.
    """

    range_rms: Annotated[float, PropertyInfo(alias="rangeRms")]
    """
    The root mean square of the range residuals, in kilometers, used to determine
    the sensor range bias.
    """

    range_sigma: Annotated[float, PropertyInfo(alias="rangeSigma")]
    """
    The standard deviation of the range residuals, in kilometers, used to determine
    the sensor range bias.
    """

    rcs_bias: Annotated[float, PropertyInfo(alias="rcsBias")]
    """The sensor radar cross section (RCS) observation bias, in square meters."""

    rcs_sigma: Annotated[float, PropertyInfo(alias="rcsSigma")]
    """
    The standard deviation of the radar cross section residuals, in square meters,
    used to determine the radar cross section bias.
    """

    ref_targets: Annotated[List[str], PropertyInfo(alias="refTargets")]
    """Array of the catalog IDs of the reference targets used in the calibration."""

    ref_type: Annotated[str, PropertyInfo(alias="refType")]
    """The reference type used in the calibration."""

    sen_type: Annotated[str, PropertyInfo(alias="senType")]
    """The sensor type (MECHANICAL, OPTICAL, PHASED ARRAY, RF)."""

    time_bias: Annotated[float, PropertyInfo(alias="timeBias")]
    """Sensor time bias, in seconds."""

    time_bias_sigma: Annotated[float, PropertyInfo(alias="timeBiasSigma")]
    """
    The standard deviation of the time residuals, in seconds, used to determine the
    sensor time bias.
    """
