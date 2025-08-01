# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .onorbit_full import OnorbitFull

__all__ = ["EoObservationFull", "EoobservationDetails"]


class EoobservationDetails(BaseModel):
    acal_cr_pix_x: Optional[float] = FieldInfo(alias="acalCrPixX", default=None)
    """World Coordinate System (WCS) X pixel origin in astrometric fit."""

    acal_cr_pix_y: Optional[float] = FieldInfo(alias="acalCrPixY", default=None)
    """World Coordinate System (WCS) Y pixel origin in astrometric fit."""

    acal_cr_val_x: Optional[float] = FieldInfo(alias="acalCrValX", default=None)
    """
    World Coordinate System (WCS) equatorial coordinate X origin corresponding to
    CRPIX in astrometric fit in degrees.
    """

    acal_cr_val_y: Optional[float] = FieldInfo(alias="acalCrValY", default=None)
    """
    World Coordinate System (WCS) equatorial coordinate Y origin corresponding to
    CRPIX in astrometric fit in degrees.
    """

    acal_num_stars: Optional[int] = FieldInfo(alias="acalNumStars", default=None)
    """Number of stars used in astrometric fit."""

    background_signal: Optional[float] = FieldInfo(alias="backgroundSignal", default=None)
    """
    This is the background signal at or in the vicinity of the radiometric source
    position. Specifically, this is the average background count level (DN/pixel)
    divided by the exposure time in seconds of the background pixels used in the
    photometric extraction. DN/pixel/sec.
    """

    background_signal_unc: Optional[float] = FieldInfo(alias="backgroundSignalUnc", default=None)
    """
    Estimated 1-sigma uncertainty in the background signal at or in the vicinity of
    the radiometric source position. DN/pixel/sec.
    """

    binning_horiz: Optional[int] = FieldInfo(alias="binningHoriz", default=None)
    """The number of pixels binned horizontally."""

    binning_vert: Optional[int] = FieldInfo(alias="binningVert", default=None)
    """The number of pixels binned vertically."""

    ccd_obj_pos_x: Optional[float] = FieldInfo(alias="ccdObjPosX", default=None)
    """The x centroid position on the CCD of the target object in pixels."""

    ccd_obj_pos_y: Optional[float] = FieldInfo(alias="ccdObjPosY", default=None)
    """The y centroid position on the CCD of the target object in pixels."""

    ccd_obj_width: Optional[float] = FieldInfo(alias="ccdObjWidth", default=None)
    """This is the pixel width of the target.

    This is either a frame-by-frame measurement or a constant point spread function
    or synthetic aperture used in the extraction.
    """

    ccd_temp: Optional[float] = FieldInfo(alias="ccdTemp", default=None)
    """
    Operating temperature of CCD recorded during exposure or measured during
    calibrations in K.
    """

    centroid_column: Optional[float] = FieldInfo(alias="centroidColumn", default=None)
    """
    Observed centroid column number on the focal plane in pixels (0 is left edge,
    0.5 is center of pixels along left of image).
    """

    centroid_row: Optional[float] = FieldInfo(alias="centroidRow", default=None)
    """
    Observed centroid row number on the focal plane in pixels (0 is top edge, 0.5 is
    center of pixels along top of image).
    """

    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)
    """
    Classification marking of the data in IC/CAPCO Portion-marked format, will be
    set to EOObservation classificationMarking if blank.
    """

    color_coeffs: Optional[List[float]] = FieldInfo(alias="colorCoeffs", default=None)
    """
    Color coefficient for filter n for a space-based sensor where there is no
    atmospheric extinction. Must be present for all values n=1 to
    numSpectralFilters, in incrementing order of n, and for no other values of n.
    """

    column_variance: Optional[float] = FieldInfo(alias="columnVariance", default=None)
    """
    Spatial variance of image distribution in horizontal direction measured in
    pixels squared.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    current_neutral_density_filter_num: Optional[int] = FieldInfo(alias="currentNeutralDensityFilterNum", default=None)
    """
    The reference number n, in neutralDensityFilters for the currently used neutral
    density filter.
    """

    current_spectral_filter_num: Optional[int] = FieldInfo(alias="currentSpectralFilterNum", default=None)
    """
    The reference number, x, where x ranges from 1 to n, where n is the number
    specified in spectralFilters that corresponds to the spectral filter given in
    the corresponding spectralFilterNames.
    """

    data_mode: Optional[Literal["REAL", "TEST", "SIMULATED", "EXERCISE"]] = FieldInfo(alias="dataMode", default=None)
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

    , will be set to EOObservation dataMode if blank.
    """

    declination_cov: Optional[float] = FieldInfo(alias="declinationCov", default=None)
    """Covariance (Y^2) in measured declination (Y) in deg^2."""

    dist_from_streak_center: Optional[List[float]] = FieldInfo(alias="distFromStreakCenter", default=None)
    """
    An array of measurements that correspond to the distance from the streak center
    measured from the optical image in pixels that show change over an interval of
    time. The array length is dependent on the length of the streak. The
    distFromStreakCenter, surfBrightness, and surfBrightnessUnc arrays will match in
    size.
    """

    does: Optional[float] = None
    """Angle off element set reported in degrees."""

    extinction_coeffs: Optional[List[float]] = FieldInfo(alias="extinctionCoeffs", default=None)
    """The extinction coefficient computed for the nth filter.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. Units = mag/airmass.
    """

    extinction_coeffs_unc: Optional[List[float]] = FieldInfo(alias="extinctionCoeffsUnc", default=None)
    """This is the uncertainty in the extinction coefficient for the nth filter.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. -9999 for space-based sensors. Units =
    mag/airmass.
    """

    gain: Optional[float] = None
    """Some sensors have gain settings.

    This value is the gain used during the observation in units e-/ADU. If no gain
    is used, the value = 1.
    """

    id_eo_observation: Optional[str] = FieldInfo(alias="idEOObservation", default=None)
    """Unique identifier of the parent EOObservation."""

    ifov: Optional[float] = None
    """Sensor instantaneous field of view (ratio of pixel pitch to focal length)."""

    mag_instrumental: Optional[float] = FieldInfo(alias="magInstrumental", default=None)
    """
    Instrumental magnitude of a sensor before corrections are applied for atmosphere
    or to transform to standard magnitude scale.
    """

    mag_instrumental_unc: Optional[float] = FieldInfo(alias="magInstrumentalUnc", default=None)
    """Uncertainty in the instrumental magnitude."""

    neutral_density_filter_names: Optional[List[str]] = FieldInfo(alias="neutralDensityFilterNames", default=None)
    """
    Must be present for all values n=1 to numNeutralDensityFilters, in incrementing
    order of n, and for no other values of n.
    """

    neutral_density_filter_transmissions: Optional[List[float]] = FieldInfo(
        alias="neutralDensityFilterTransmissions", default=None
    )
    """The transmission of the nth neutral density filter.

    Must be present for all values n=1 to numNeutralDensityFilters, in incrementing
    order of n, and for no other values of n.
    """

    neutral_density_filter_transmissions_unc: Optional[List[float]] = FieldInfo(
        alias="neutralDensityFilterTransmissionsUnc", default=None
    )
    """This is the uncertainty in the transmission for the nth filter.

    Must be present for all values n=1 to numNeutralDensityFilters, in incrementing
    order of n, and for no other values of n.
    """

    num_catalog_stars: Optional[int] = FieldInfo(alias="numCatalogStars", default=None)
    """
    Number of catalog stars in the detector field of view (FOV) with the target
    object. Can be 0 for narrow FOV sensors.
    """

    num_correlated_stars: Optional[int] = FieldInfo(alias="numCorrelatedStars", default=None)
    """Number of correlated stars in the FOV with the target object.

    Can be 0 for narrow FOV sensors.
    """

    num_detected_stars: Optional[int] = FieldInfo(alias="numDetectedStars", default=None)
    """Number of detected stars in the FOV with the target object.

    Helps identify frames with clouds.
    """

    num_neutral_density_filters: Optional[int] = FieldInfo(alias="numNeutralDensityFilters", default=None)
    """The value is the number of neutral density filters used."""

    num_spectral_filters: Optional[int] = FieldInfo(alias="numSpectralFilters", default=None)
    """The value is the number of spectral filters used."""

    obj_sun_range: Optional[float] = FieldInfo(alias="objSunRange", default=None)
    """Distance from the target object to the sun during the observation in meters."""

    ob_time: Optional[datetime] = FieldInfo(alias="obTime", default=None)
    """
    Ob detection time in ISO 8601 UTC with microsecond precision, will be set to
    EOObservation obTime if blank.
    """

    optical_cross_section: Optional[float] = FieldInfo(alias="opticalCrossSection", default=None)
    """Optical Cross Section computed in units m(2)/ster."""

    optical_cross_section_unc: Optional[float] = FieldInfo(alias="opticalCrossSectionUnc", default=None)
    """Uncertainty in Optical Cross Section computed in units m(2)/ster."""

    pcal_num_stars: Optional[int] = FieldInfo(alias="pcalNumStars", default=None)
    """Number of stars used in photometric fit count."""

    peak_aperture_count: Optional[float] = FieldInfo(alias="peakApertureCount", default=None)
    """
    Peak Aperture Raw Counts is the value of the peak pixel in the real or synthetic
    aperture containing the target signal.
    """

    peak_background_count: Optional[int] = FieldInfo(alias="peakBackgroundCount", default=None)
    """
    Peak Background Raw Counts is the largest pixel value used in background signal.
    """

    phase_ang_bisect: Optional[float] = FieldInfo(alias="phaseAngBisect", default=None)
    """Solar phase angle bisector vector.

    The vector that bisects the solar phase angle. The phase angle bisector is the
    angle that is << of the value in #48. Then calculate the point on the RA/DEC
    (ECI J2000.0) sphere that a vector at this angle would intersect.
    """

    pixel_array_height: Optional[int] = FieldInfo(alias="pixelArrayHeight", default=None)
    """Pixel array size (height) in pixels."""

    pixel_array_width: Optional[int] = FieldInfo(alias="pixelArrayWidth", default=None)
    """Pixel array size (width) in pixels."""

    pixel_max: Optional[int] = FieldInfo(alias="pixelMax", default=None)
    """Maximum valid pixel value, this is defined as 2^(number of bits per pixel).

    For example, a CCD with 8-bitpixels, would have a maximum valid pixel value of
    2^8 = 256. This can represent the saturation value of the detector, but some
    sensors will saturate at a value significantly lower than full well depth. This
    is the analog-to-digital conversion (ADC) saturation value.
    """

    pixel_min: Optional[int] = FieldInfo(alias="pixelMin", default=None)
    """Minimum valid pixel value, this is typically 0."""

    predicted_azimuth: Optional[float] = FieldInfo(alias="predictedAzimuth", default=None)
    """
    Predicted Azimuth angle of the target object from a ground -based sensor (no
    atmospheric refraction correction required) in degrees. AZ_EL implies apparent
    topocentric place in true of date reference frame as seen from the observer with
    aberration due to the observer velocity and light travel time applied.
    """

    predicted_declination: Optional[float] = FieldInfo(alias="predictedDeclination", default=None)
    """
    Predicted Declination of the Target object from the frame of reference of the
    sensor (J2000, geocentric velocity aberration). SGP4 and VCMs produce geocentric
    origin and velocity aberration and subtracting the sensor geocentric position of
    the sensor places in its reference frame.
    """

    predicted_declination_unc: Optional[float] = FieldInfo(alias="predictedDeclinationUnc", default=None)
    """
    Uncertainty of Predicted Declination of the Target object from the frame of
    reference of the sensor (J2000, geocentric velocity aberration). SGP4 and VCMs
    produce geocentric origin and velocity aberration and subtracting the sensor
    geocentric position of the sensor places in its reference frame.
    """

    predicted_elevation: Optional[float] = FieldInfo(alias="predictedElevation", default=None)
    """
    Predicted elevation angle of the target object from a ground -based sensor (no
    atmospheric refraction correction required) in degrees. AZ_EL implies apparent
    topocentric place in true of date reference frame as seen from the observer with
    aberration due to the observer velocity and light travel time applied.
    """

    predicted_ra: Optional[float] = FieldInfo(alias="predictedRa", default=None)
    """
    Predicted Right Ascension of the Target object from the frame of reference of
    the sensor (J2000, geocentric velocity aberration). SGP4 and VCMs produce
    geocentric origin and velocity aberration and subtracting the sensor geocentric
    position of the sensor places in its reference frame.
    """

    predicted_ra_unc: Optional[float] = FieldInfo(alias="predictedRaUnc", default=None)
    """
    Uncertainty of predicted Right Ascension of the Target object from the frame of
    reference of the sensor (J2000, geocentric velocity aberration). SGP4 and VCMs
    produce geocentric origin and velocity aberration and subtracting the sensor
    geocentric position of the sensor places in its reference frame.
    """

    ra_cov: Optional[float] = FieldInfo(alias="raCov", default=None)
    """Covariance (x^2) in measured Right Ascension (X) in deg^2."""

    ra_declination_cov: Optional[float] = FieldInfo(alias="raDeclinationCov", default=None)
    """Covariance (XY) in measured ra/declination (XY) in deg^2."""

    row_col_cov: Optional[float] = FieldInfo(alias="rowColCov", default=None)
    """
    Spatial covariance of image distribution across horizontal and vertical
    directions measured in pixels squared.
    """

    row_variance: Optional[float] = FieldInfo(alias="rowVariance", default=None)
    """
    Spatial variance of image distribution in vertical direction measured in pixels
    squared.
    """

    snr_est: Optional[float] = FieldInfo(alias="snrEst", default=None)
    """Estimated signal-to-noise ratio (SNR) for the total radiometric signal.

    Under some algorithms, this can be a constant per target (not per observation).
    Note: this SNR applies to the total signal of the radiometric source (i.e.,
    Net_Obj_Sig with units DN/sec), not to be confused with the SNR of the signal in
    the peak pixel (i.e., DN/pixel/sec).
    """

    solar_disk_frac: Optional[float] = FieldInfo(alias="solarDiskFrac", default=None)
    """Fraction of the sun that is illuminating the target object.

    This indicates if the target is in the Earth’s penumbra or umbra. (It is 0 when
    object is in umbra and 1 when object is fully illuminated.).
    """

    source: Optional[str] = None
    """Source of the data, will be set to EOObservation source if blank."""

    spectral_filters: Optional[List[str]] = FieldInfo(alias="spectralFilters", default=None)
    """
    Array of the SpectralFilters keywords, must be present for all values n=1 to
    numSpectralFilters, in incrementing order of n, and for no other values of n.
    """

    spectral_filter_solar_mag: Optional[List[float]] = FieldInfo(alias="spectralFilterSolarMag", default=None)
    """This is the in-band solar magnitude at 1 A.U.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. Units = mag.
    """

    spectral_zmfl: Optional[List[float]] = FieldInfo(alias="spectralZMFL", default=None)
    """This is the in-band average irradiance of a 0th mag source.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. Units = W/m2/nm.
    """

    sun_azimuth: Optional[float] = FieldInfo(alias="sunAzimuth", default=None)
    """
    Azimuth angle of the sun from a ground-based telescope (no atmospheric
    refraction correction required) the observer with aberration due to the observer
    velocity and light travel time applied in degrees.
    """

    sun_elevation: Optional[float] = FieldInfo(alias="sunElevation", default=None)
    """
    Elevation angle of the sun from a ground-based telescope (no atmospheric
    refraction correction required) in degrees.
    """

    sun_state_pos_x: Optional[float] = FieldInfo(alias="sunStatePosX", default=None)
    """Sun state vector in ECI J2000 coordinate frame in km."""

    sun_state_pos_y: Optional[float] = FieldInfo(alias="sunStatePosY", default=None)
    """Sun state vector in ECI J2000 coordinate frame in km."""

    sun_state_pos_z: Optional[float] = FieldInfo(alias="sunStatePosZ", default=None)
    """Sun state vector in ECI J2000 coordinate frame in km."""

    sun_state_vel_x: Optional[float] = FieldInfo(alias="sunStateVelX", default=None)
    """Sun state vector in ECI J2000 coordinate frame in km/sec."""

    sun_state_vel_y: Optional[float] = FieldInfo(alias="sunStateVelY", default=None)
    """Sun state vector in ECI J2000 coordinate frame in km/sec."""

    sun_state_vel_z: Optional[float] = FieldInfo(alias="sunStateVelZ", default=None)
    """Sun state vector in ECI J2000 coordinate frame in km/sec."""

    surf_brightness: Optional[List[float]] = FieldInfo(alias="surfBrightness", default=None)
    """
    An array of surface brightness measurements in magnitudes per square arcsecond
    from the optical image that show change over an interval of time. The array
    length is dependent on the length of the streak. The distFromStreakCenter,
    surfBrightness, and surfBrightnessUnc arrays will match in size.
    """

    surf_brightness_unc: Optional[List[float]] = FieldInfo(alias="surfBrightnessUnc", default=None)
    """
    An array of surface brightness uncertainty measurements in magnitudes per square
    arcsecond from the optical image that show change over an interval of time. The
    array length is dependent on the length of the streak. The distFromStreakCenter,
    surfBrightness, and surfBrightnessUnc arrays will match in size.
    """

    times_unc: Optional[float] = FieldInfo(alias="timesUnc", default=None)
    """Uncertainty in the times reported in UTC in seconds."""

    toes: Optional[float] = None
    """Time off element set reported in seconds."""

    zero_points: Optional[List[float]] = FieldInfo(alias="zeroPoints", default=None)
    """
    This is the value for the zero-point calculated for each filter denoted in
    spectralFilters. It is the difference between the catalog mag and instrumental
    mag for a set of standard stars. For use with All Sky photometry. Must be
    present for all values n=1 to numSpectralFilters, in incrementing order of n,
    and for no other values of n.
    """

    zero_points_unc: Optional[List[float]] = FieldInfo(alias="zeroPointsUnc", default=None)
    """
    This is the uncertainty in the zero point for the filter denoted in
    spectralFilters. For use with All Sky photometry. Must be present for all values
    n=1 to numSpectralFilters, in incrementing order of n, and for no other values
    of n.
    """


class EoObservationFull(BaseModel):
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
    """Ob detection time in ISO 8601 UTC, up to microsecond precision.

    Consumers should contact the provider for details on their obTime
    specifications.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    azimuth: Optional[float] = None
    """Line of sight azimuth angle in degrees and topocentric frame.

    Reported value should include all applicable corrections as specified on the
    source provider data card. If uncertain, consumers should contact the provider
    for details on the applied corrections.
    """

    azimuth_bias: Optional[float] = FieldInfo(alias="azimuthBias", default=None)
    """Sensor line of sight azimuth angle bias in degrees."""

    azimuth_measured: Optional[bool] = FieldInfo(alias="azimuthMeasured", default=None)
    """
    Optional flag indicating whether the azimuth value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    azimuth_rate: Optional[float] = FieldInfo(alias="azimuthRate", default=None)
    """Rate of change of the line of sight azimuth in degrees per second."""

    azimuth_unc: Optional[float] = FieldInfo(alias="azimuthUnc", default=None)
    """One sigma uncertainty in the line of sight azimuth angle, in degrees."""

    bg_intensity: Optional[float] = FieldInfo(alias="bgIntensity", default=None)
    """Background intensity for IR observations, in kw/sr/um."""

    collect_method: Optional[str] = FieldInfo(alias="collectMethod", default=None)
    """
    Method indicating telescope movement during collection (AUTOTRACK, MANUAL
    AUTOTRACK, MANUAL RATE TRACK, MANUAL SIDEREAL, SIDEREAL, RATE TRACK).
    """

    corr_quality: Optional[float] = FieldInfo(alias="corrQuality", default=None)
    """
    Object Correlation Quality score of the observation when compared to a known
    orbit state, (non-standardized). Users should consult data providers regarding
    the expected range of values.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    declination: Optional[float] = None
    """Line of sight declination, in degrees, in the specified referenceFrame.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    declination_bias: Optional[float] = FieldInfo(alias="declinationBias", default=None)
    """Sensor line of sight declination angle bias in degrees."""

    declination_measured: Optional[bool] = FieldInfo(alias="declinationMeasured", default=None)
    """
    Optional flag indicating whether the declination value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    declination_rate: Optional[float] = FieldInfo(alias="declinationRate", default=None)
    """
    Line of sight declination rate of change, in degrees/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    declination_unc: Optional[float] = FieldInfo(alias="declinationUnc", default=None)
    """One sigma uncertainty in the line of sight declination angle, in degrees."""

    descriptor: Optional[str] = None
    """Optional source-provided and searchable metadata or descriptor of the data."""

    elevation: Optional[float] = None
    """Line of sight elevation in degrees and topocentric frame.

    Reported value should include all applicable corrections as specified on the
    source provider data card. If uncertain, consumers should contact the provider
    for details on the applied corrections.
    """

    elevation_bias: Optional[float] = FieldInfo(alias="elevationBias", default=None)
    """Sensor line of sight elevation bias in degrees."""

    elevation_measured: Optional[bool] = FieldInfo(alias="elevationMeasured", default=None)
    """
    Optional flag indicating whether the elevation value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    elevation_rate: Optional[float] = FieldInfo(alias="elevationRate", default=None)
    """Rate of change of the line of sight elevation in degrees per second."""

    elevation_unc: Optional[float] = FieldInfo(alias="elevationUnc", default=None)
    """One sigma uncertainty in the line of sight elevation angle, in degrees."""

    eoobservation_details: Optional[EoobservationDetails] = FieldInfo(alias="eoobservationDetails", default=None)
    """
    Model representation of additional detailed observation data for electro-optical
    based sensor phenomenologies.
    """

    exp_duration: Optional[float] = FieldInfo(alias="expDuration", default=None)
    """Image exposure duration in seconds.

    For observations performed using frame stacking or synthetic tracking methods,
    the exposure duration should be the total integration time. This field is highly
    recommended / required if the observations are going to be used for photometric
    processing.
    """

    fov_count: Optional[int] = FieldInfo(alias="fovCount", default=None)
    """The number of RSOs detected in the sensor field of view."""

    fov_count_uct: Optional[int] = FieldInfo(alias="fovCountUCT", default=None)
    """The number of uncorrelated tracks in the field of view."""

    geoalt: Optional[float] = None
    """For GEO detections, the altitude in km."""

    geolat: Optional[float] = None
    """For GEO detections, the latitude in degrees north."""

    geolon: Optional[float] = None
    """For GEO detections, the longitude in degrees east."""

    georange: Optional[float] = None
    """For GEO detections, the range in km."""

    id_on_orbit: Optional[str] = FieldInfo(alias="idOnOrbit", default=None)
    """Unique identifier of the target on-orbit object, if correlated."""

    id_sensor: Optional[str] = FieldInfo(alias="idSensor", default=None)
    """Unique identifier of the reporting sensor."""

    id_sky_imagery: Optional[str] = FieldInfo(alias="idSkyImagery", default=None)
    """Unique identifier of the Sky Imagery."""

    intensity: Optional[float] = None
    """Intensity of the target for IR observations, in kw/sr/um."""

    los_unc: Optional[float] = FieldInfo(alias="losUnc", default=None)
    """One sigma uncertainty in the line of sight pointing in micro-radians."""

    losx: Optional[float] = None
    """
    Line-of-sight cartesian X position of the target, in km, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losxvel: Optional[float] = None
    """
    Line-of-sight cartesian X velocity of target, in km/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losy: Optional[float] = None
    """
    Line-of-sight cartesian Y position of the target, in km, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losyvel: Optional[float] = None
    """
    Line-of-sight cartesian Y velocity of target, in km/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losz: Optional[float] = None
    """
    Line-of-sight cartesian Z position of the target, in km, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    loszvel: Optional[float] = None
    """
    Line-of-sight cartesian Z velocity of target, in km/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    mag: Optional[float] = None
    """
    Measure of observed brightness calibrated against the Gaia G-band in units of
    magnitudes.
    """

    mag_norm_range: Optional[float] = FieldInfo(alias="magNormRange", default=None)
    """Formula: mag - 5.0 \\** log_10(geo_range / 1000000.0)."""

    mag_unc: Optional[float] = FieldInfo(alias="magUnc", default=None)
    """Uncertainty of the observed brightness in units of magnitudes."""

    net_obj_sig: Optional[float] = FieldInfo(alias="netObjSig", default=None)
    """Net object signature = counts / expDuration."""

    net_obj_sig_unc: Optional[float] = FieldInfo(alias="netObjSigUnc", default=None)
    """Net object signature uncertainty = counts uncertainty / expDuration."""

    ob_position: Optional[str] = FieldInfo(alias="obPosition", default=None)
    """The position of this observation within a track (FENCE, FIRST, IN, LAST,
    SINGLE).

    This identifier is optional and, if null, no assumption should be made regarding
    whether other observations may or may not exist to compose a track.
    """

    on_orbit: Optional[OnorbitFull] = FieldInfo(alias="onOrbit", default=None)
    """Model object representing on-orbit objects or satellites in the system."""

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
    Optional identifier provided by observation source to indicate the sensor
    identifier which produced this observation. This may be an internal identifier
    and not necessarily a valid sensor ID.
    """

    penumbra: Optional[bool] = None
    """
    Boolean indicating that the target object was in a penumbral eclipse at the time
    of this observation.
    """

    primary_extinction: Optional[float] = FieldInfo(alias="primaryExtinction", default=None)
    """Primary Extinction Coefficient, in Magnitudes.

    Primary Extinction is the coefficient applied to the airmass to determine how
    much the observed visual magnitude has been attenuated by the atmosphere.
    Extinction, in general, describes the absorption and scattering of
    electromagnetic radiation by dust and gas between an emitting astronomical
    object and the observer. See the EOObservationDetails API for specification of
    extinction coefficients for multiple spectral filters.
    """

    primary_extinction_unc: Optional[float] = FieldInfo(alias="primaryExtinctionUnc", default=None)
    """Primary Extinction Coefficient Uncertainty, in Magnitudes."""

    ra: Optional[float] = None
    """Line of sight right ascension, in degrees, in the specified referenceFrame.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    ra_bias: Optional[float] = FieldInfo(alias="raBias", default=None)
    """Sensor line of sight right ascension bias in degrees."""

    ra_measured: Optional[bool] = FieldInfo(alias="raMeasured", default=None)
    """
    Optional flag indicating whether the ra value is measured (true) or computed
    (false). If null, consumers may consult the data provider for information
    regarding whether the corresponding value is computed or measured.
    """

    range: Optional[float] = None
    """Line of sight range in km.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    range_bias: Optional[float] = FieldInfo(alias="rangeBias", default=None)
    """Sensor line of sight range bias in km."""

    range_measured: Optional[bool] = FieldInfo(alias="rangeMeasured", default=None)
    """
    Optional flag indicating whether the range value is measured (true) or computed
    (false). If null, consumers may consult the data provider for information
    regarding whether the corresponding value is computed or measured.
    """

    range_rate: Optional[float] = FieldInfo(alias="rangeRate", default=None)
    """Range rate in km/s.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    range_rate_measured: Optional[bool] = FieldInfo(alias="rangeRateMeasured", default=None)
    """
    Optional flag indicating whether the rangeRate value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    range_rate_unc: Optional[float] = FieldInfo(alias="rangeRateUnc", default=None)
    """One sigma uncertainty in the line of sight range rate, in kilometers/second."""

    range_unc: Optional[float] = FieldInfo(alias="rangeUnc", default=None)
    """One sigma uncertainty in the line of sight range, in kilometers."""

    ra_rate: Optional[float] = FieldInfo(alias="raRate", default=None)
    """
    Line of sight right ascension rate of change, in degrees/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    ra_unc: Optional[float] = FieldInfo(alias="raUnc", default=None)
    """One sigma uncertainty in the line of sight right ascension angle, in degrees."""

    raw_file_uri: Optional[str] = FieldInfo(alias="rawFileURI", default=None)
    """
    Optional URI location in the document repository of the raw file parsed by the
    system to produce this record. To download the raw file, prepend
    https://udl-hostname/scs/download?id= to this value.
    """

    reference_frame: Optional[Literal["J2000", "GCRF", "ITRF", "TEME"]] = FieldInfo(
        alias="referenceFrame", default=None
    )
    """The reference frame of the EOObservation measurements.

    If the referenceFrame is null it is assumed to be J2000.
    """

    sat_no: Optional[int] = FieldInfo(alias="satNo", default=None)
    """Satellite/Catalog number of the target on-orbit object."""

    senalt: Optional[float] = None
    """Sensor altitude at obTime (if mobile/onorbit) in km."""

    senlat: Optional[float] = None
    """Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees.

    If null, can be obtained from sensor info. -90 to 90 degrees (negative values
    south of equator).
    """

    senlon: Optional[float] = None
    """Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees.

    If null, can be obtained from sensor info. -180 to 180 degrees (negative values
    west of Prime Meridian).
    """

    sen_quat: Optional[List[float]] = FieldInfo(alias="senQuat", default=None)
    """
    The quaternion describing the rotation of the sensor in relation to the
    body-fixed frame used for this system into the local geodetic frame, at
    observation time (obTime). The array element order convention is scalar
    component first, followed by the three vector components (qc, q1, q2, q3).
    """

    sen_reference_frame: Optional[Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"]] = FieldInfo(
        alias="senReferenceFrame", default=None
    )
    """The reference frame of the observing sensor state.

    If the senReferenceFrame is null it is assumed to be J2000.
    """

    senvelx: Optional[float] = None
    """
    Cartesian X velocity of the observing mobile/onorbit sensor at obTime, in
    km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
    J2K should be assumed.
    """

    senvely: Optional[float] = None
    """
    Cartesian Y velocity of the observing mobile/onorbit sensor at obTime, in
    km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
    J2K should be assumed.
    """

    senvelz: Optional[float] = None
    """
    Cartesian Z velocity of the observing mobile/onorbit sensor at obTime, in
    km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
    J2K should be assumed.
    """

    senx: Optional[float] = None
    """
    Cartesian X position of the observing mobile/onorbit sensor at obTime, in km, in
    the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
    assumed.
    """

    seny: Optional[float] = None
    """
    Cartesian Y position of the observing mobile/onorbit sensor at obTime, in km, in
    the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
    assumed.
    """

    senz: Optional[float] = None
    """
    Cartesian Z position of the observing mobile/onorbit sensor at obTime, in km, in
    the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
    assumed.
    """

    shutter_delay: Optional[float] = FieldInfo(alias="shutterDelay", default=None)
    """Shutter delay in seconds."""

    sky_bkgrnd: Optional[float] = FieldInfo(alias="skyBkgrnd", default=None)
    """Average Sky Background signal, in Magnitudes.

    Sky Background refers to the incoming light from an apparently empty part of the
    night sky.
    """

    solar_dec_angle: Optional[float] = FieldInfo(alias="solarDecAngle", default=None)
    """Angle from the sun to the equatorial plane."""

    solar_eq_phase_angle: Optional[float] = FieldInfo(alias="solarEqPhaseAngle", default=None)
    """
    The angle, in degrees, between the projections of the target-to-observer vector
    and the target-to-sun vector onto the equatorial plane. The angle is represented
    as negative when closing (i.e. before the opposition) and positive when opening
    (after the opposition).
    """

    solar_phase_angle: Optional[float] = FieldInfo(alias="solarPhaseAngle", default=None)
    """
    The angle, in degrees, between the target-to-observer vector and the
    target-to-sun vector.
    """

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    tags: Optional[List[str]] = None
    """
    Optional array of provider/source specific tags for this data, where each
    element is no longer than 32 characters, used for implementing data owner
    conditional access controls to restrict access to the data. Should be left null
    by data providers unless conditional access controls are coordinated with the
    UDL team.
    """

    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)
    """
    Optional identifier to indicate the specific tasking which produced this
    observation.
    """

    timing_bias: Optional[float] = FieldInfo(alias="timingBias", default=None)
    """Sensor timing bias in seconds."""

    track_id: Optional[str] = FieldInfo(alias="trackId", default=None)
    """Optional identifier of the track to which this observation belongs."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """
    Optional identifier to track a commercial or marketplace transaction executed to
    produce this data.
    """

    type: Optional[str] = None
    """Read only field specifying the type of observation (e.g.

    OPTICAL, OPTICAL_IR, LASER_RANGING, etc).
    """

    uct: Optional[bool] = None
    """
    Boolean indicating this observation is part of an uncorrelated track or was
    unable to be correlated to a known object. This flag should only be set to true
    by data providers after an attempt to correlate to an on-orbit object was made
    and failed. If unable to correlate, the 'origObjectId' field may be populated
    with an internal data provider specific identifier.
    """

    umbra: Optional[bool] = None
    """
    Boolean indicating that the target object was in umbral eclipse at the time of
    this observation.
    """

    zeroptd: Optional[float] = None
    """Formula: 2.5 \\** log_10 (zero_mag_counts / expDuration)."""

    zero_ptd_unc: Optional[float] = FieldInfo(alias="zeroPtdUnc", default=None)
    """
    This is the uncertainty in the zero point for the filter used for this
    observation/row in units of mag. For use with differential photometry.
    """
