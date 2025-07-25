# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SoiObservationSetListResponse", "Calibration"]


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


class SoiObservationSetListResponse(BaseModel):
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
