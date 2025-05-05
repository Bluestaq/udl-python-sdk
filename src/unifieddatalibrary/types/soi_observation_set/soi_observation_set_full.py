# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SoiObservationSetFull", "Calibration", "OpticalSoiObservationList", "RadarSoiObservationList"]


class Calibration(BaseModel):
    cal_bg_intensity: Optional[float] = FieldInfo(alias="calBgIntensity", default=None)
    """
    Background intensity, at calibration, specified in kilowatts per steradian per
    micrometer.
    """

    cal_extinction_coeff: Optional[float] = FieldInfo(alias="calExtinctionCoeff", default=None)
    """
    Coefficient value for how much signal would be lost to atmospheric attenuation
    for a star at zenith, in magnitudes per air mass.
    """

    cal_extinction_coeff_max_unc: Optional[float] = FieldInfo(alias="calExtinctionCoeffMaxUnc", default=None)
    """Maximum extinction coefficient uncertainty in magnitudes, at calibration (e.g.

    -5.0 to 30.0).
    """

    cal_extinction_coeff_unc: Optional[float] = FieldInfo(alias="calExtinctionCoeffUnc", default=None)
    """
    Extinction coefficient uncertainty in magnitudes, at calibration, which
    represents the difference between the measured brightness and predicted
    brightness of the star with the extinction removed, making it exo-atmospheric
    (e.g. -5.0 to 30.0).
    """

    cal_num_correlated_stars: Optional[int] = FieldInfo(alias="calNumCorrelatedStars", default=None)
    """Number of correlated stars in the FOV with the target object, at calibration.

    Can be 0 for narrow FOV sensors.
    """

    cal_num_detected_stars: Optional[int] = FieldInfo(alias="calNumDetectedStars", default=None)
    """Number of detected stars in the FOV with the target object, at calibration.

    Helps identify frames with clouds.
    """

    cal_sky_bg: Optional[float] = FieldInfo(alias="calSkyBg", default=None)
    """Average Sky Background signals in magnitudes, at calibration.

    Sky Background refers to the incoming light from an apparently empty part of the
    night sky.
    """

    cal_spectral_filter_solar_mag: Optional[float] = FieldInfo(alias="calSpectralFilterSolarMag", default=None)
    """In-band solar magnitudes at 1 A.U, at calibration (e.g. -5.0 to 30.0)."""

    cal_time: Optional[datetime] = FieldInfo(alias="calTime", default=None)
    """Start time of calibration in ISO 8601 UTC time, with millisecond precision."""

    cal_type: Optional[str] = FieldInfo(alias="calType", default=None)
    """Type of calibration (e.g. PRE, MID, POST)."""

    cal_zero_point: Optional[float] = FieldInfo(alias="calZeroPoint", default=None)
    """
    Value representing the difference between the catalog magnitude and instrumental
    magnitude for a set of standard stars, at calibration (e.g. -5.0 to 30.0).
    """


class OpticalSoiObservationList(BaseModel):
    ob_start_time: datetime = FieldInfo(alias="obStartTime")
    """Observation detection start time in ISO 8601 UTC with microsecond precision."""

    current_spectral_filter_num: Optional[int] = FieldInfo(alias="currentSpectralFilterNum", default=None)
    """
    The reference number, x, where x ranges from 1 to n, where n is the number
    specified in spectralFilters that corresponds to the spectral filter used.
    """

    declinations: Optional[List[float]] = None
    """
    Array of declination values, in degrees, of the Target object from the frame of
    reference of the sensor. A value is provided for each element in the intensities
    field, at the middle of the frame’s exposure time.
    """

    exp_duration: Optional[float] = FieldInfo(alias="expDuration", default=None)
    """Image exposure duration in seconds."""

    extinction_coeffs: Optional[List[float]] = FieldInfo(alias="extinctionCoeffs", default=None)
    """
    Array of coefficients for how much signal would be lost to atmospheric
    attenuation for a star at zenith for each element in intensities, in magnitudes
    per air mass.
    """

    extinction_coeffs_unc: Optional[List[float]] = FieldInfo(alias="extinctionCoeffsUnc", default=None)
    """Array of extinction coefficient uncertainties for each element in intensities.

    Each value represents the difference between the measured brightness and
    predicted brightness of the star with the extinction removed, making it
    exo-atmospheric (e.g. -5.0 to 30.0).
    """

    intensities: Optional[List[float]] = None
    """
    Array of intensities of the Space Object for observations, in kilowatts per
    steradian per micrometer.
    """

    intensity_times: Optional[List[datetime]] = FieldInfo(alias="intensityTimes", default=None)
    """Array of start times for each intensity measurement.

    The 1st value in the array will match obStartTime.
    """

    local_sky_bgs: Optional[List[float]] = FieldInfo(alias="localSkyBgs", default=None)
    """
    Array of local average Sky Background signals, in magnitudes, with a value
    corresponding to the time of each intensity measurement. Sky Background refers
    to the incoming light from an apparently empty part of the night sky.
    """

    local_sky_bgs_unc: Optional[List[float]] = FieldInfo(alias="localSkyBgsUnc", default=None)
    """
    Array of uncertainty of the local average Sky Background signal, in magnitudes,
    with a value corresponding to the time of each intensity measurement.
    """

    num_correlated_stars: Optional[List[int]] = FieldInfo(alias="numCorrelatedStars", default=None)
    """
    Array of the number of correlated stars in the FOV with a value for each element
    in the intensities field.
    """

    num_detected_stars: Optional[List[int]] = FieldInfo(alias="numDetectedStars", default=None)
    """
    Array of the number of detected stars in the FOV with a value for each element
    in the intensities field.
    """

    percent_sats: Optional[List[float]] = FieldInfo(alias="percentSats", default=None)
    """
    Array of values giving the percent of pixels that make up the object signal that
    are beyond the saturation point for the sensor, with a value for each element in
    the intensities field.
    """

    ra_rates: Optional[List[float]] = FieldInfo(alias="raRates", default=None)
    """
    Array of right ascension rate values, in degrees per second, measuring the rate
    the telescope is moving to track the Target object from the frame of reference
    of the sensor, for each element in the intensities field, at the middle of the
    frame’s exposure time.
    """

    ras: Optional[List[float]] = None
    """
    Array of right ascension values, in degrees, of the Target object from the frame
    of reference of the sensor. A value is provided for each element in the
    intensities field.
    """

    sky_bgs: Optional[List[float]] = FieldInfo(alias="skyBgs", default=None)
    """
    Array of average Sky Background signals, in magnitudes, with a value
    corresponding to the time of each intensity measurement. Sky Background refers
    to the incoming light from an apparently empty part of the night sky.
    """

    zero_points: Optional[List[float]] = FieldInfo(alias="zeroPoints", default=None)
    """
    Array of values for the zero-point in magnitudes, calculated at the time of each
    intensity measurement. It is the difference between the catalog mag and
    instrumental mag for a set of standard stars (e.g. -5.0 to 30.0).
    """


class RadarSoiObservationList(BaseModel):
    ob_start_time: datetime = FieldInfo(alias="obStartTime")
    """
    Observation detection start time in ISO 8601 UTC format with microsecond
    precision.
    """

    aspect_angles: Optional[List[float]] = FieldInfo(alias="aspectAngles", default=None)
    """Array of the aspect angle at the center of the image in degrees.

    The 'tovs' and 'aspectAngles' arrays must match in size, if 'aspectAngles' is
    provided.
    """

    azimuth_biases: Optional[List[float]] = FieldInfo(alias="azimuthBiases", default=None)
    """Array of sensor azimuth angle biases in degrees.

    The 'tovs' and 'azimuthBiases' arrays must match in size, if 'azimuthBiases' is
    provided.
    """

    azimuth_rates: Optional[List[float]] = FieldInfo(alias="azimuthRates", default=None)
    """Array of the azimuth rate of target at image center in degrees per second.

    The 'tovs' and 'azimuthRates' arrays must match in size, if 'azimuthRates' is
    provided. If there is an associated image the azimuth rate is assumed to be at
    image center.
    """

    azimuths: Optional[List[float]] = None
    """Array of the azimuth angle to target at image center in degrees.

    The 'tovs' and 'azimuths' arrays must match in size, if 'azimuths' is provided.
    If there is an associated image the azimuth angle is assumed to be at image
    center.
    """

    beta: Optional[float] = None
    """Beta angle (between target and radar-image frame z axis) in degrees."""

    center_frequency: Optional[float] = FieldInfo(alias="centerFrequency", default=None)
    """Radar center frequency of the radar in hertz."""

    cross_range_res: Optional[List[float]] = FieldInfo(alias="crossRangeRes", default=None)
    """
    Array of cross-range resolutions (accounting for weighting function) in
    kilometers. The 'tovs' and 'crossRangeRes' arrays must match in size, if
    'crossRangeRes' is provided.
    """

    delta_times: Optional[List[float]] = FieldInfo(alias="deltaTimes", default=None)
    """Array of average Interpulse spacing in seconds.

    The 'tovs' and 'deltaTimes' arrays must match in size, if 'deltaTimes' is
    provided.
    """

    doppler2_x_rs: Optional[List[float]] = FieldInfo(alias="doppler2XRs", default=None)
    """Array of conversion factors between Doppler in hertz and cross-range in meters.

    The 'tovs' and 'doppler2XRs' arrays must match in size, if 'doppler2XRs' is
    provided.
    """

    elevation_biases: Optional[List[float]] = FieldInfo(alias="elevationBiases", default=None)
    """Array of sensor elevation biases in degrees.

    The 'tovs' and 'elevationBiases' arrays must match in size, if 'elevationBiases'
    is provided.
    """

    elevation_rates: Optional[List[float]] = FieldInfo(alias="elevationRates", default=None)
    """Array of the elevation rate of target at image center in degrees per second.

    The 'tovs' and 'elevationRates' arrays must match in size, if 'elevationRates'
    is provided. If there is an associated image the elevation rate is assumed to be
    at image center.
    """

    elevations: Optional[List[float]] = None
    """Array of the elevation angle to target at image center in degrees.

    The 'tovs' and 'elevations' arrays must match in size, if 'elevations' is
    provided. If there is an associated image the elevation angle is assumed to be
    at image center.
    """

    id_attitude_set: Optional[str] = FieldInfo(alias="idAttitudeSet", default=None)
    """Optional id of assumed AttitudeSet of object being observed."""

    id_state_vector: Optional[str] = FieldInfo(alias="idStateVector", default=None)
    """Optional id of assumed StateVector of object being observed."""

    integration_angles: Optional[List[float]] = FieldInfo(alias="integrationAngles", default=None)
    """Array of Integration angles in degrees.

    The 'tovs' and 'integrationAngles' arrays must match in size, if
    'integrationAngles' is provided.
    """

    kappa: Optional[float] = None
    """Kappa angle (between radar-line-of-sight and target-frame x axis) in degrees."""

    peak_amplitudes: Optional[List[float]] = FieldInfo(alias="peakAmplitudes", default=None)
    """Array of the peak pixel amplitude for each image in decibels.

    The 'tovs' and 'peakAmplitudes' arrays must match in size, if 'peakAmplitudes'
    is provided.
    """

    polarizations: Optional[List[str]] = None
    """Array of sensor polarizations when collecting the data.

    Polarization is a property of electromagnetic waves that describes the
    orientation of their oscillations. Possible values are H - (Horizontally
    Polarized) Perpendicular to Earth's surface, V - (Vertically Polarized) Parallel
    to Earth's surface, L - (Left Hand Circularly Polarized) Rotating left relative
    to the Earth's surface, R - (Right Hand Circularly Polarized) Rotating right
    relative to the Earth's surface.
    """

    proj_ang_vels: Optional[List[float]] = FieldInfo(alias="projAngVels", default=None)
    """
    Array of the component of target angular velocity observable by radar in radians
    per second. The 'tovs' and 'projAngVels' arrays must match in size, if
    'projAngVels' is provided.
    """

    pulse_bandwidth: Optional[float] = FieldInfo(alias="pulseBandwidth", default=None)
    """Bandwidth of radar pulse in hertz."""

    range_accels: Optional[List[float]] = FieldInfo(alias="rangeAccels", default=None)
    """Array of the range acceleratons of target in kilometers per second squared.

    The 'tovs' and 'rangeAccels' arrays must match in size, if 'rangeAccels' is
    provided. If there is an associated image the range acceleration is assumed to
    be at image center.
    """

    range_biases: Optional[List[float]] = FieldInfo(alias="rangeBiases", default=None)
    """Array of sensor range biases in kilometers.

    The 'tovs' and 'rangeBiases' arrays must match in size, if 'rangeBiases' is
    provided.
    """

    range_rates: Optional[List[float]] = FieldInfo(alias="rangeRates", default=None)
    """Array of the range rate of target at image center in kilometers per second.

    The 'tovs' and 'rangeRates' arrays must match in size, if 'rangeRates' is
    provided. If there is an associated image the range rate is assumed to be at
    image center.
    """

    ranges: Optional[List[float]] = None
    """Array of the range to target at image center in kilometers.

    The 'tovs' and 'ranges' arrays must match in size, if 'ranges' is provided. If
    there is an associated image the range is assumed to be at image center.
    """

    rcs_error_ests: Optional[List[float]] = FieldInfo(alias="rcsErrorEsts", default=None)
    """Array of error estimates of RCS values, in square meters."""

    rcs_values: Optional[List[float]] = FieldInfo(alias="rcsValues", default=None)
    """Array of observed radar cross section (RCS) values, in square meters."""

    rspaces: Optional[List[float]] = None
    """Array of range sample spacing in meters.

    The 'tovs' and 'rspaces' arrays must match in size, if 'rspaces' is provided.
    """

    spectral_widths: Optional[List[float]] = FieldInfo(alias="spectralWidths", default=None)
    """Array of spectral widths, in hertz.

    The spectral width of a satellite can help determine if an object is stable or
    tumbling which is often useful to distinguish a rocket body from an active
    stabilized payload or to deduce a rotational period of slowly tumbling objects
    at GEO.
    """

    tovs: Optional[List[datetime]] = None
    """
    Array of the times of validity in ISO 8601 UTC format with microsecond
    precision.
    """

    xaccel: Optional[List[float]] = None
    """
    Array of the cartesian X accelerations, in kilometers per second squared, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'xaccel' arrays must match in size, if 'xaccel' is provided.
    """

    xpos: Optional[List[float]] = None
    """
    Array of the cartesian X positions of the target, in kilometers, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'xpos' arrays must match in size, if 'xpos' is provided.
    """

    xspaces: Optional[List[float]] = None
    """Array of cross-range sample spacing in meters.

    The 'tovs' and 'xspaces' arrays must match in size, if 'xspaces' is provided.
    """

    xvel: Optional[List[float]] = None
    """
    Array of the cartesian X velocities of target, in kilometers per second, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'xvel' arrays must match in size, if 'xvel' is provided.
    """

    yaccel: Optional[List[float]] = None
    """
    Array of the cartesian Y accelerations, in kilometers per second squared, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'yaccel' arrays must match in size, if 'yaccel' is provided.
    """

    ypos: Optional[List[float]] = None
    """
    Array of the cartesian Y positions of the target, in kilometers, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'ypos' arrays must match in size, if 'ypos' is provided.
    """

    yvel: Optional[List[float]] = None
    """
    Array of the cartesian Y velocities of target, in kilometers per second, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'yvel' arrays must match in size, if 'yvel' is provided.
    """

    zaccel: Optional[List[float]] = None
    """
    Array of the cartesian Z accelerations, in kilometers per second squared, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'zaccel' arrays must match in size, if 'zaccel' is provided.
    """

    zpos: Optional[List[float]] = None
    """
    Array of the cartesian Z positions of the target, in kilometers, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'zpos' arrays must match in size, if 'zpos' is provided.
    """

    zvel: Optional[List[float]] = None
    """
    Array of the cartesian Z velocities of target, in kilometers per second, in the
    specified referenceFrame. If referenceFrame is null then J2K should be assumed.
    The 'tovs' and 'zvel' arrays must match in size, if 'zvel' is provided.
    """


class SoiObservationSetFull(BaseModel):
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

    num_obs: int = FieldInfo(alias="numObs")
    """The number of observation records in the set."""

    source: str
    """Source of the data."""

    start_time: datetime = FieldInfo(alias="startTime")
    """
    Observation set detection start time in ISO 8601 UTC with microsecond precision.
    """

    type: Literal["OPTICAL", "RADAR"]
    """Observation type (OPTICAL, RADAR)."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    binning_horiz: Optional[int] = FieldInfo(alias="binningHoriz", default=None)
    """The number of pixels binned horizontally."""

    binning_vert: Optional[int] = FieldInfo(alias="binningVert", default=None)
    """The number of pixels binned vertically."""

    brightness_variance_change_detected: Optional[bool] = FieldInfo(
        alias="brightnessVarianceChangeDetected", default=None
    )
    """
    Boolean indicating if a brightness variance change event was detected, based on
    historical collection data for the object.
    """

    calibrations: Optional[List[Calibration]] = None
    """Array of SOI Calibrations associated with this SOIObservationSet."""

    calibration_type: Optional[str] = FieldInfo(alias="calibrationType", default=None)
    """Type of calibration used by the Sensor (e.g.

    ALL SKY, DIFFERENTIAL, DEFAULT, NONE).
    """

    change_conf: Optional[str] = FieldInfo(alias="changeConf", default=None)
    """Overall qualitative confidence assessment of change detection results (e.g.

    HIGH, MEDIUM, LOW).
    """

    change_detected: Optional[bool] = FieldInfo(alias="changeDetected", default=None)
    """
    Boolean indicating if any change event was detected, based on historical
    collection data for the object.
    """

    collection_density_conf: Optional[str] = FieldInfo(alias="collectionDensityConf", default=None)
    """
    Qualitative Collection Density assessment, with respect to confidence of
    detecting a change event (e.g. HIGH, MEDIUM, LOW).
    """

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """Universally Unique collection ID.

    Mechanism to correlate Single Point Photometry (SPP) JSON files to images.
    """

    collection_mode: Optional[str] = FieldInfo(alias="collectionMode", default=None)
    """
    Mode indicating telescope movement during collection (AUTOTRACK, MANUAL
    AUTOTRACK, MANUAL RATE TRACK, MANUAL SIDEREAL, SIDEREAL, RATE TRACK).
    """

    corr_quality: Optional[float] = FieldInfo(alias="corrQuality", default=None)
    """Object Correlation Quality value.

    Measures how close the observed object's orbit is to matching an object in the
    catalog. The scale of this field may vary depending on provider. Users should
    consult the data provider to verify the meaning of the value (e.g. A value of
    0.0 indicates a high/strong correlation, while a value closer to 1.0 indicates
    low/weak correlation).
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)
    """Observation set detection end time in ISO 8601 UTC with microsecond precision."""

    gain: Optional[float] = None
    """
    The gain used during the collection, in units of photoelectrons per
    analog-to-digital unit (e-/ADU). If no gain is used, the value = 1.
    """

    id_elset: Optional[str] = FieldInfo(alias="idElset", default=None)
    """ID of the UDL Elset of the Space Object under observation."""

    id_on_orbit: Optional[str] = FieldInfo(alias="idOnOrbit", default=None)
    """Unique identifier of the target on-orbit object, if correlated."""

    id_sensor: Optional[str] = FieldInfo(alias="idSensor", default=None)
    """ID of the observing sensor."""

    los_declination_end: Optional[float] = FieldInfo(alias="losDeclinationEnd", default=None)
    """Line of sight declination at observation set detection end time.

    Specified in degrees, in the specified referenceFrame. If referenceFrame is null
    then J2K should be assumed (e.g -30 to 130.0).
    """

    los_declination_start: Optional[float] = FieldInfo(alias="losDeclinationStart", default=None)
    """Line of sight declination at observation set detection start time.

    Specified in degrees, in the specified referenceFrame. If referenceFrame is null
    then J2K should be assumed (e.g -30 to 130.0).
    """

    msg_create_date: Optional[datetime] = FieldInfo(alias="msgCreateDate", default=None)
    """SOI msgCreateDate time in ISO 8601 UTC time, with millisecond precision."""

    num_spectral_filters: Optional[int] = FieldInfo(alias="numSpectralFilters", default=None)
    """The value is the number of spectral filters used."""

    optical_soi_observation_list: Optional[List[OpticalSoiObservationList]] = FieldInfo(
        alias="opticalSOIObservationList", default=None
    )
    """OpticalSOIObservations associated with this SOIObservationSet."""

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

    orig_object_id: Optional[str] = FieldInfo(alias="origObjectId", default=None)
    """
    Optional identifier provided by observation source to indicate the target
    onorbit object of this observation. This may be an internal identifier and not
    necessarily a valid satellite number.
    """

    orig_sensor_id: Optional[str] = FieldInfo(alias="origSensorId", default=None)
    """
    Optional identifier provided by the record source to indicate the sensor
    identifier to which this attitude set applies if this set is reporting a single
    sensor orientation. This may be an internal identifier and not necessarily a
    valid sensor ID.
    """

    percent_sat_threshold: Optional[float] = FieldInfo(alias="percentSatThreshold", default=None)
    """
    A threshold for percent of pixels that make up object signal that are beyond the
    saturation point for the sensor that are removed in the EOSSA file, in range of
    0 to 1.
    """

    periodicity_change_detected: Optional[bool] = FieldInfo(alias="periodicityChangeDetected", default=None)
    """
    Boolean indicating if a periodicity change event was detected, based on
    historical collection data for the object.
    """

    periodicity_detection_conf: Optional[str] = FieldInfo(alias="periodicityDetectionConf", default=None)
    """
    Qualitative assessment of the periodicity detection results from the Attitude
    and Shape Retrieval (ASR) Periodicity Assessment (PA) Tool (e.g. HIGH, MEDIUM,
    LOW).
    """

    periodicity_sampling_conf: Optional[str] = FieldInfo(alias="periodicitySamplingConf", default=None)
    """
    Qualitative Periodicity Sampling assessment, with respect to confidence of
    detecting a change event (e.g. HIGH, MEDIUM, LOW).
    """

    pixel_array_height: Optional[int] = FieldInfo(alias="pixelArrayHeight", default=None)
    """Pixel array size (height) in pixels."""

    pixel_array_width: Optional[int] = FieldInfo(alias="pixelArrayWidth", default=None)
    """Pixel array size (width) in pixels."""

    pixel_max: Optional[int] = FieldInfo(alias="pixelMax", default=None)
    """The maximum valid pixel value."""

    pixel_min: Optional[int] = FieldInfo(alias="pixelMin", default=None)
    """The minimum valid pixel value."""

    pointing_angle_az_end: Optional[float] = FieldInfo(alias="pointingAngleAzEnd", default=None)
    """Pointing angle of the Azimuth gimbal/mount at observation set detection end
    time.

    Specified in degrees.
    """

    pointing_angle_az_start: Optional[float] = FieldInfo(alias="pointingAngleAzStart", default=None)
    """
    Pointing angle of the Azimuth gimbal/mount at observation set detection start
    time. Specified in degrees.
    """

    pointing_angle_el_end: Optional[float] = FieldInfo(alias="pointingAngleElEnd", default=None)
    """
    Pointing angle of the Elevation gimbal/mount at observation set detection end
    time. Specified in degrees.
    """

    pointing_angle_el_start: Optional[float] = FieldInfo(alias="pointingAngleElStart", default=None)
    """
    Pointing angle of the Elevation gimbal/mount at observation set detection start
    time. Specified in degrees.
    """

    polar_angle_end: Optional[float] = FieldInfo(alias="polarAngleEnd", default=None)
    """
    Polar angle of the gimbal/mount at observation set detection end time in
    degrees.
    """

    polar_angle_start: Optional[float] = FieldInfo(alias="polarAngleStart", default=None)
    """
    Polar angle of the gimbal/mount at observation set detection start time in
    degrees.
    """

    radar_soi_observation_list: Optional[List[RadarSoiObservationList]] = FieldInfo(
        alias="radarSOIObservationList", default=None
    )
    """RadarSOIObservations associated with this RadarSOIObservationSet."""

    reference_frame: Optional[Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"]] = FieldInfo(
        alias="referenceFrame", default=None
    )
    """The reference frame of the observation measurements.

    If the referenceFrame is null it is assumed to be J2000.
    """

    satellite_name: Optional[str] = FieldInfo(alias="satelliteName", default=None)
    """Name of the target satellite."""

    sat_no: Optional[int] = FieldInfo(alias="satNo", default=None)
    """Satellite/catalog number of the target on-orbit object."""

    senalt: Optional[float] = None
    """Sensor altitude at startTime (if mobile/onorbit) in kilometers."""

    senlat: Optional[float] = None
    """Sensor WGS84 latitude at startTime (if mobile/onorbit) in degrees.

    If null, can be obtained from sensor info. -90 to 90 degrees (negative values
    south of equator).
    """

    senlon: Optional[float] = None
    """Sensor WGS84 longitude at startTime (if mobile/onorbit) in degrees.

    If null, can be obtained from sensor info. -180 to 180 degrees (negative values
    south of equator).
    """

    sen_reference_frame: Optional[Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"]] = FieldInfo(
        alias="senReferenceFrame", default=None
    )
    """The reference frame of the observing sensor state.

    If the senReferenceFrame is null it is assumed to be J2000.
    """

    sensor_as_id: Optional[str] = FieldInfo(alias="sensorAsId", default=None)
    """ID of the AttitudeSet record for the observing sensor."""

    senvelx: Optional[float] = None
    """
    Cartesian X velocity of the observing mobile/onorbit sensor at startTime, in
    kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
    is null then J2K should be assumed.
    """

    senvely: Optional[float] = None
    """
    Cartesian Y velocity of the observing mobile/onorbit sensor at startTime, in
    kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
    is null then J2K should be assumed.
    """

    senvelz: Optional[float] = None
    """
    Cartesian Z velocity of the observing mobile/onorbit sensor at startTime, in
    kilometers per second, in the specified senReferenceFrame. If senReferenceFrame
    is null then J2K should be assumed.
    """

    senx: Optional[float] = None
    """
    Cartesian X position of the observing mobile/onorbit sensor at startTime, in
    kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
    then J2K should be assumed.
    """

    seny: Optional[float] = None
    """
    Cartesian Y position of the observing mobile/onorbit sensor at startTime, in
    kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
    then J2K should be assumed.
    """

    senz: Optional[float] = None
    """
    Cartesian Z position of the observing mobile/onorbit sensor at startTime, in
    kilometers, in the specified senReferenceFrame. If senReferenceFrame is null
    then J2K should be assumed.
    """

    software_version: Optional[str] = FieldInfo(alias="softwareVersion", default=None)
    """Software Version used to Capture, Process, and Deliver the data."""

    solar_mag: Optional[float] = FieldInfo(alias="solarMag", default=None)
    """The in-band solar magnitude at 1 A.U."""

    solar_phase_angle_brightness_change_detected: Optional[bool] = FieldInfo(
        alias="solarPhaseAngleBrightnessChangeDetected", default=None
    )
    """
    Boolean indicating if a solar phase angle brightness change event was detected,
    based on historical collection data for the object.
    """

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    spectral_filters: Optional[List[str]] = FieldInfo(alias="spectralFilters", default=None)
    """
    Array of the SpectralFilters keywords, must be present for all values n=1 to
    numSpectralFilters, in incrementing order of n, and for no other values of n.
    """

    star_cat_name: Optional[str] = FieldInfo(alias="starCatName", default=None)
    """Name of the Star Catalog used for photometry and astrometry."""

    tags: Optional[List[str]] = None
    """
    Optional array of provider/source specific tags for this data, where each
    element is no longer than 32 characters, used for implementing data owner
    conditional access controls to restrict access to the data. Should be left null
    by data providers unless conditional access controls are coordinated with the
    UDL team.
    """

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """
    Optional identifier to track a commercial or marketplace transaction executed to
    produce this data.
    """

    uct: Optional[bool] = None
    """
    Boolean indicating whether the target object was unable to be correlated to a
    known object. This flag should only be set to true by data providers after an
    attempt to correlate to an OnOrbit object was made and failed. If unable to
    correlate, the 'origObjectId' field may be populated with an internal data
    provider specific identifier.
    """

    valid_calibrations: Optional[str] = FieldInfo(alias="validCalibrations", default=None)
    """
    Key to indicate which, if any of, the pre/post photometer calibrations are valid
    for use when generating data for the EOSSA file. If the field is not populated,
    then the provided calibration data will be used when generating the EOSSA file
    (e.g. PRE, POST, BOTH, NONE).
    """
