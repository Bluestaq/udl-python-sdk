# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EoObservationUnvalidatedPublishParams", "Body", "BodyEoobservationDetails"]


class EoObservationUnvalidatedPublishParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyEoobservationDetails(TypedDict, total=False):
    acal_cr_pix_x: Annotated[float, PropertyInfo(alias="acalCrPixX")]
    """World Coordinate System (WCS) X pixel origin in astrometric fit."""

    acal_cr_pix_y: Annotated[float, PropertyInfo(alias="acalCrPixY")]
    """World Coordinate System (WCS) Y pixel origin in astrometric fit."""

    acal_cr_val_x: Annotated[float, PropertyInfo(alias="acalCrValX")]
    """
    World Coordinate System (WCS) equatorial coordinate X origin corresponding to
    CRPIX in astrometric fit in degrees.
    """

    acal_cr_val_y: Annotated[float, PropertyInfo(alias="acalCrValY")]
    """
    World Coordinate System (WCS) equatorial coordinate Y origin corresponding to
    CRPIX in astrometric fit in degrees.
    """

    acal_num_stars: Annotated[int, PropertyInfo(alias="acalNumStars")]
    """Number of stars used in astrometric fit."""

    background_signal: Annotated[float, PropertyInfo(alias="backgroundSignal")]
    """
    This is the background signal at or in the vicinity of the radiometric source
    position. Specifically, this is the average background count level (DN/pixel)
    divided by the exposure time in seconds of the background pixels used in the
    photometric extraction. DN/pixel/sec.
    """

    background_signal_unc: Annotated[float, PropertyInfo(alias="backgroundSignalUnc")]
    """
    Estimated 1-sigma uncertainty in the background signal at or in the vicinity of
    the radiometric source position. DN/pixel/sec.
    """

    binning_horiz: Annotated[int, PropertyInfo(alias="binningHoriz")]
    """The number of pixels binned horizontally."""

    binning_vert: Annotated[int, PropertyInfo(alias="binningVert")]
    """The number of pixels binned vertically."""

    ccd_obj_pos_x: Annotated[float, PropertyInfo(alias="ccdObjPosX")]
    """The x centroid position on the CCD of the target object in pixels."""

    ccd_obj_pos_y: Annotated[float, PropertyInfo(alias="ccdObjPosY")]
    """The y centroid position on the CCD of the target object in pixels."""

    ccd_obj_width: Annotated[float, PropertyInfo(alias="ccdObjWidth")]
    """This is the pixel width of the target.

    This is either a frame-by-frame measurement or a constant point spread function
    or synthetic aperture used in the extraction.
    """

    ccd_temp: Annotated[float, PropertyInfo(alias="ccdTemp")]
    """
    Operating temperature of CCD recorded during exposure or measured during
    calibrations in K.
    """

    centroid_column: Annotated[float, PropertyInfo(alias="centroidColumn")]
    """
    Observed centroid column number on the focal plane in pixels (0 is left edge,
    0.5 is center of pixels along left of image).
    """

    centroid_row: Annotated[float, PropertyInfo(alias="centroidRow")]
    """
    Observed centroid row number on the focal plane in pixels (0 is top edge, 0.5 is
    center of pixels along top of image).
    """

    classification_marking: Annotated[str, PropertyInfo(alias="classificationMarking")]
    """
    Classification marking of the data in IC/CAPCO Portion-marked format, will be
    set to EOObservation classificationMarking if blank.
    """

    color_coeffs: Annotated[Iterable[float], PropertyInfo(alias="colorCoeffs")]
    """
    Color coefficient for filter n for a space-based sensor where there is no
    atmospheric extinction. Must be present for all values n=1 to
    numSpectralFilters, in incrementing order of n, and for no other values of n.
    """

    column_variance: Annotated[float, PropertyInfo(alias="columnVariance")]
    """
    Spatial variance of image distribution in horizontal direction measured in
    pixels squared.
    """

    current_neutral_density_filter_num: Annotated[int, PropertyInfo(alias="currentNeutralDensityFilterNum")]
    """
    The reference number n, in neutralDensityFilters for the currently used neutral
    density filter.
    """

    current_spectral_filter_num: Annotated[int, PropertyInfo(alias="currentSpectralFilterNum")]
    """
    The reference number, x, where x ranges from 1 to n, where n is the number
    specified in spectralFilters that corresponds to the spectral filter given in
    the corresponding spectralFilterNames.
    """

    data_mode: Annotated[Literal["REAL", "TEST", "SIMULATED", "EXERCISE"], PropertyInfo(alias="dataMode")]
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

    declination_cov: Annotated[float, PropertyInfo(alias="declinationCov")]
    """Covariance (Y^2) in measured declination (Y) in deg^2."""

    dist_from_streak_center: Annotated[Iterable[float], PropertyInfo(alias="distFromStreakCenter")]
    """
    An array of measurements that correspond to the distance from the streak center
    measured from the optical image in pixels that show change over an interval of
    time. The array length is dependent on the length of the streak. The
    distFromStreakCenter, surfBrightness, and surfBrightnessUnc arrays will match in
    size.
    """

    does: float
    """Angle off element set reported in degrees."""

    extinction_coeffs: Annotated[Iterable[float], PropertyInfo(alias="extinctionCoeffs")]
    """The extinction coefficient computed for the nth filter.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. Units = mag/airmass.
    """

    extinction_coeffs_unc: Annotated[Iterable[float], PropertyInfo(alias="extinctionCoeffsUnc")]
    """This is the uncertainty in the extinction coefficient for the nth filter.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. -9999 for space-based sensors. Units =
    mag/airmass.
    """

    gain: float
    """Some sensors have gain settings.

    This value is the gain used during the observation in units e-/ADU. If no gain
    is used, the value = 1.
    """

    id_eo_observation: Annotated[str, PropertyInfo(alias="idEOObservation")]
    """Unique identifier of the parent EOObservation."""

    ifov: float
    """Sensor instantaneous field of view (ratio of pixel pitch to focal length)."""

    mag_instrumental: Annotated[float, PropertyInfo(alias="magInstrumental")]
    """
    Instrumental magnitude of a sensor before corrections are applied for atmosphere
    or to transform to standard magnitude scale.
    """

    mag_instrumental_unc: Annotated[float, PropertyInfo(alias="magInstrumentalUnc")]
    """Uncertainty in the instrumental magnitude."""

    neutral_density_filter_names: Annotated[List[str], PropertyInfo(alias="neutralDensityFilterNames")]
    """
    Must be present for all values n=1 to numNeutralDensityFilters, in incrementing
    order of n, and for no other values of n.
    """

    neutral_density_filter_transmissions: Annotated[
        Iterable[float], PropertyInfo(alias="neutralDensityFilterTransmissions")
    ]
    """The transmission of the nth neutral density filter.

    Must be present for all values n=1 to numNeutralDensityFilters, in incrementing
    order of n, and for no other values of n.
    """

    neutral_density_filter_transmissions_unc: Annotated[
        Iterable[float], PropertyInfo(alias="neutralDensityFilterTransmissionsUnc")
    ]
    """This is the uncertainty in the transmission for the nth filter.

    Must be present for all values n=1 to numNeutralDensityFilters, in incrementing
    order of n, and for no other values of n.
    """

    num_catalog_stars: Annotated[int, PropertyInfo(alias="numCatalogStars")]
    """
    Number of catalog stars in the detector field of view (FOV) with the target
    object. Can be 0 for narrow FOV sensors.
    """

    num_correlated_stars: Annotated[int, PropertyInfo(alias="numCorrelatedStars")]
    """Number of correlated stars in the FOV with the target object.

    Can be 0 for narrow FOV sensors.
    """

    num_detected_stars: Annotated[int, PropertyInfo(alias="numDetectedStars")]
    """Number of detected stars in the FOV with the target object.

    Helps identify frames with clouds.
    """

    num_neutral_density_filters: Annotated[int, PropertyInfo(alias="numNeutralDensityFilters")]
    """The value is the number of neutral density filters used."""

    num_spectral_filters: Annotated[int, PropertyInfo(alias="numSpectralFilters")]
    """The value is the number of spectral filters used."""

    obj_sun_range: Annotated[float, PropertyInfo(alias="objSunRange")]
    """Distance from the target object to the sun during the observation in meters."""

    ob_time: Annotated[Union[str, datetime], PropertyInfo(alias="obTime", format="iso8601")]
    """
    Ob detection time in ISO 8601 UTC with microsecond precision, will be set to
    EOObservation obTime if blank.
    """

    optical_cross_section: Annotated[float, PropertyInfo(alias="opticalCrossSection")]
    """Optical Cross Section computed in units m(2)/ster."""

    optical_cross_section_unc: Annotated[float, PropertyInfo(alias="opticalCrossSectionUnc")]
    """Uncertainty in Optical Cross Section computed in units m(2)/ster."""

    pcal_num_stars: Annotated[int, PropertyInfo(alias="pcalNumStars")]
    """Number of stars used in photometric fit count."""

    peak_aperture_count: Annotated[float, PropertyInfo(alias="peakApertureCount")]
    """
    Peak Aperture Raw Counts is the value of the peak pixel in the real or synthetic
    aperture containing the target signal.
    """

    peak_background_count: Annotated[int, PropertyInfo(alias="peakBackgroundCount")]
    """
    Peak Background Raw Counts is the largest pixel value used in background signal.
    """

    phase_ang_bisect: Annotated[float, PropertyInfo(alias="phaseAngBisect")]
    """Solar phase angle bisector vector.

    The vector that bisects the solar phase angle. The phase angle bisector is the
    angle that is << of the value in #48. Then calculate the point on the RA/DEC
    (ECI J2000.0) sphere that a vector at this angle would intersect.
    """

    pixel_array_height: Annotated[int, PropertyInfo(alias="pixelArrayHeight")]
    """Pixel array size (height) in pixels."""

    pixel_array_width: Annotated[int, PropertyInfo(alias="pixelArrayWidth")]
    """Pixel array size (width) in pixels."""

    pixel_max: Annotated[int, PropertyInfo(alias="pixelMax")]
    """Maximum valid pixel value, this is defined as 2^(number of bits per pixel).

    For example, a CCD with 8-bitpixels, would have a maximum valid pixel value of
    2^8 = 256. This can represent the saturation value of the detector, but some
    sensors will saturate at a value significantly lower than full well depth. This
    is the analog-to-digital conversion (ADC) saturation value.
    """

    pixel_min: Annotated[int, PropertyInfo(alias="pixelMin")]
    """Minimum valid pixel value, this is typically 0."""

    predicted_azimuth: Annotated[float, PropertyInfo(alias="predictedAzimuth")]
    """
    Predicted Azimuth angle of the target object from a ground -based sensor (no
    atmospheric refraction correction required) in degrees. AZ_EL implies apparent
    topocentric place in true of date reference frame as seen from the observer with
    aberration due to the observer velocity and light travel time applied.
    """

    predicted_declination: Annotated[float, PropertyInfo(alias="predictedDeclination")]
    """
    Predicted Declination of the Target object from the frame of reference of the
    sensor (J2000, geocentric velocity aberration). SGP4 and VCMs produce geocentric
    origin and velocity aberration and subtracting the sensor geocentric position of
    the sensor places in its reference frame.
    """

    predicted_declination_unc: Annotated[float, PropertyInfo(alias="predictedDeclinationUnc")]
    """
    Uncertainty of Predicted Declination of the Target object from the frame of
    reference of the sensor (J2000, geocentric velocity aberration). SGP4 and VCMs
    produce geocentric origin and velocity aberration and subtracting the sensor
    geocentric position of the sensor places in its reference frame.
    """

    predicted_elevation: Annotated[float, PropertyInfo(alias="predictedElevation")]
    """
    Predicted elevation angle of the target object from a ground -based sensor (no
    atmospheric refraction correction required) in degrees. AZ_EL implies apparent
    topocentric place in true of date reference frame as seen from the observer with
    aberration due to the observer velocity and light travel time applied.
    """

    predicted_ra: Annotated[float, PropertyInfo(alias="predictedRa")]
    """
    Predicted Right Ascension of the Target object from the frame of reference of
    the sensor (J2000, geocentric velocity aberration). SGP4 and VCMs produce
    geocentric origin and velocity aberration and subtracting the sensor geocentric
    position of the sensor places in its reference frame.
    """

    predicted_ra_unc: Annotated[float, PropertyInfo(alias="predictedRaUnc")]
    """
    Uncertainty of predicted Right Ascension of the Target object from the frame of
    reference of the sensor (J2000, geocentric velocity aberration). SGP4 and VCMs
    produce geocentric origin and velocity aberration and subtracting the sensor
    geocentric position of the sensor places in its reference frame.
    """

    ra_cov: Annotated[float, PropertyInfo(alias="raCov")]
    """Covariance (x^2) in measured Right Ascension (X) in deg^2."""

    ra_declination_cov: Annotated[float, PropertyInfo(alias="raDeclinationCov")]
    """Covariance (XY) in measured ra/declination (XY) in deg^2."""

    row_col_cov: Annotated[float, PropertyInfo(alias="rowColCov")]
    """
    Spatial covariance of image distribution across horizontal and vertical
    directions measured in pixels squared.
    """

    row_variance: Annotated[float, PropertyInfo(alias="rowVariance")]
    """
    Spatial variance of image distribution in vertical direction measured in pixels
    squared.
    """

    snr_est: Annotated[float, PropertyInfo(alias="snrEst")]
    """Estimated signal-to-noise ratio (SNR) for the total radiometric signal.

    Under some algorithms, this can be a constant per target (not per observation).
    Note: this SNR applies to the total signal of the radiometric source (i.e.,
    Net_Obj_Sig with units DN/sec), not to be confused with the SNR of the signal in
    the peak pixel (i.e., DN/pixel/sec).
    """

    solar_disk_frac: Annotated[float, PropertyInfo(alias="solarDiskFrac")]
    """Fraction of the sun that is illuminating the target object.

    This indicates if the target is in the Earth’s penumbra or umbra. (It is 0 when
    object is in umbra and 1 when object is fully illuminated.).
    """

    source: str
    """Source of the data, will be set to EOObservation source if blank."""

    spectral_filters: Annotated[List[str], PropertyInfo(alias="spectralFilters")]
    """
    Array of the SpectralFilters keywords, must be present for all values n=1 to
    numSpectralFilters, in incrementing order of n, and for no other values of n.
    """

    spectral_filter_solar_mag: Annotated[Iterable[float], PropertyInfo(alias="spectralFilterSolarMag")]
    """This is the in-band solar magnitude at 1 A.U.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. Units = mag.
    """

    spectral_zmfl: Annotated[Iterable[float], PropertyInfo(alias="spectralZMFL")]
    """This is the in-band average irradiance of a 0th mag source.

    Must be present for all values n=1 to numSpectralFilters, in incrementing order
    of n, and for no other values of n. Units = W/m2/nm.
    """

    sun_azimuth: Annotated[float, PropertyInfo(alias="sunAzimuth")]
    """
    Azimuth angle of the sun from a ground-based telescope (no atmospheric
    refraction correction required) the observer with aberration due to the observer
    velocity and light travel time applied in degrees.
    """

    sun_elevation: Annotated[float, PropertyInfo(alias="sunElevation")]
    """
    Elevation angle of the sun from a ground-based telescope (no atmospheric
    refraction correction required) in degrees.
    """

    sun_state_pos_x: Annotated[float, PropertyInfo(alias="sunStatePosX")]
    """Sun state vector in ECI J2000 coordinate frame in km."""

    sun_state_pos_y: Annotated[float, PropertyInfo(alias="sunStatePosY")]
    """Sun state vector in ECI J2000 coordinate frame in km."""

    sun_state_pos_z: Annotated[float, PropertyInfo(alias="sunStatePosZ")]
    """Sun state vector in ECI J2000 coordinate frame in km."""

    sun_state_vel_x: Annotated[float, PropertyInfo(alias="sunStateVelX")]
    """Sun state vector in ECI J2000 coordinate frame in km/sec."""

    sun_state_vel_y: Annotated[float, PropertyInfo(alias="sunStateVelY")]
    """Sun state vector in ECI J2000 coordinate frame in km/sec."""

    sun_state_vel_z: Annotated[float, PropertyInfo(alias="sunStateVelZ")]
    """Sun state vector in ECI J2000 coordinate frame in km/sec."""

    surf_brightness: Annotated[Iterable[float], PropertyInfo(alias="surfBrightness")]
    """
    An array of surface brightness measurements in magnitudes per square arcsecond
    from the optical image that show change over an interval of time. The array
    length is dependent on the length of the streak. The distFromStreakCenter,
    surfBrightness, and surfBrightnessUnc arrays will match in size.
    """

    surf_brightness_unc: Annotated[Iterable[float], PropertyInfo(alias="surfBrightnessUnc")]
    """
    An array of surface brightness uncertainty measurements in magnitudes per square
    arcsecond from the optical image that show change over an interval of time. The
    array length is dependent on the length of the streak. The distFromStreakCenter,
    surfBrightness, and surfBrightnessUnc arrays will match in size.
    """

    times_unc: Annotated[float, PropertyInfo(alias="timesUnc")]
    """Uncertainty in the times reported in UTC in seconds."""

    toes: float
    """Time off element set reported in seconds."""

    zero_points: Annotated[Iterable[float], PropertyInfo(alias="zeroPoints")]
    """
    This is the value for the zero-point calculated for each filter denoted in
    spectralFilters. It is the difference between the catalog mag and instrumental
    mag for a set of standard stars. For use with All Sky photometry. Must be
    present for all values n=1 to numSpectralFilters, in incrementing order of n,
    and for no other values of n.
    """

    zero_points_unc: Annotated[Iterable[float], PropertyInfo(alias="zeroPointsUnc")]
    """
    This is the uncertainty in the zero point for the filter denoted in
    spectralFilters. For use with All Sky photometry. Must be present for all values
    n=1 to numSpectralFilters, in incrementing order of n, and for no other values
    of n.
    """


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
    """Ob detection time in ISO 8601 UTC, up to microsecond precision.

    Consumers should contact the provider for details on their obTime
    specifications.
    """

    source: Required[str]
    """Source of the data."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    azimuth: float
    """Line of sight azimuth angle in degrees and topocentric frame.

    Reported value should include all applicable corrections as specified on the
    source provider data card. If uncertain, consumers should contact the provider
    for details on the applied corrections.
    """

    azimuth_bias: Annotated[float, PropertyInfo(alias="azimuthBias")]
    """Sensor line of sight azimuth angle bias in degrees."""

    azimuth_measured: Annotated[bool, PropertyInfo(alias="azimuthMeasured")]
    """
    Optional flag indicating whether the azimuth value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    azimuth_rate: Annotated[float, PropertyInfo(alias="azimuthRate")]
    """Rate of change of the line of sight azimuth in degrees per second."""

    azimuth_unc: Annotated[float, PropertyInfo(alias="azimuthUnc")]
    """One sigma uncertainty in the line of sight azimuth angle, in degrees."""

    bg_intensity: Annotated[float, PropertyInfo(alias="bgIntensity")]
    """Background intensity for IR observations, in kw/sr/um."""

    collect_method: Annotated[str, PropertyInfo(alias="collectMethod")]
    """
    Method indicating telescope movement during collection (AUTOTRACK, MANUAL
    AUTOTRACK, MANUAL RATE TRACK, MANUAL SIDEREAL, SIDEREAL, RATE TRACK).
    """

    corr_quality: Annotated[float, PropertyInfo(alias="corrQuality")]
    """
    Object Correlation Quality score of the observation when compared to a known
    orbit state, (non-standardized). Users should consult data providers regarding
    the expected range of values.
    """

    declination: float
    """Line of sight declination, in degrees, in the specified referenceFrame.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    declination_bias: Annotated[float, PropertyInfo(alias="declinationBias")]
    """Sensor line of sight declination angle bias in degrees."""

    declination_measured: Annotated[bool, PropertyInfo(alias="declinationMeasured")]
    """
    Optional flag indicating whether the declination value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    declination_rate: Annotated[float, PropertyInfo(alias="declinationRate")]
    """
    Line of sight declination rate of change, in degrees/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    declination_unc: Annotated[float, PropertyInfo(alias="declinationUnc")]
    """One sigma uncertainty in the line of sight declination angle, in degrees."""

    descriptor: str
    """Optional source-provided and searchable metadata or descriptor of the data."""

    elevation: float
    """Line of sight elevation in degrees and topocentric frame.

    Reported value should include all applicable corrections as specified on the
    source provider data card. If uncertain, consumers should contact the provider
    for details on the applied corrections.
    """

    elevation_bias: Annotated[float, PropertyInfo(alias="elevationBias")]
    """Sensor line of sight elevation bias in degrees."""

    elevation_measured: Annotated[bool, PropertyInfo(alias="elevationMeasured")]
    """
    Optional flag indicating whether the elevation value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    elevation_rate: Annotated[float, PropertyInfo(alias="elevationRate")]
    """Rate of change of the line of sight elevation in degrees per second."""

    elevation_unc: Annotated[float, PropertyInfo(alias="elevationUnc")]
    """One sigma uncertainty in the line of sight elevation angle, in degrees."""

    eoobservation_details: Annotated[BodyEoobservationDetails, PropertyInfo(alias="eoobservationDetails")]
    """
    Model representation of additional detailed observation data for electro-optical
    based sensor phenomenologies.
    """

    exp_duration: Annotated[float, PropertyInfo(alias="expDuration")]
    """Image exposure duration in seconds.

    For observations performed using frame stacking or synthetic tracking methods,
    the exposure duration should be the total integration time. This field is highly
    recommended / required if the observations are going to be used for photometric
    processing.
    """

    fov_count: Annotated[int, PropertyInfo(alias="fovCount")]
    """The number of RSOs detected in the sensor field of view."""

    fov_count_uct: Annotated[int, PropertyInfo(alias="fovCountUCT")]
    """The number of uncorrelated tracks in the field of view."""

    geoalt: float
    """For GEO detections, the altitude in km."""

    geolat: float
    """For GEO detections, the latitude in degrees north."""

    geolon: float
    """For GEO detections, the longitude in degrees east."""

    georange: float
    """For GEO detections, the range in km."""

    id_sensor: Annotated[str, PropertyInfo(alias="idSensor")]
    """Unique identifier of the reporting sensor."""

    id_sky_imagery: Annotated[str, PropertyInfo(alias="idSkyImagery")]
    """Unique identifier of the Sky Imagery."""

    intensity: float
    """Intensity of the target for IR observations, in kw/sr/um."""

    los_unc: Annotated[float, PropertyInfo(alias="losUnc")]
    """One sigma uncertainty in the line of sight pointing in micro-radians."""

    losx: float
    """
    Line-of-sight cartesian X position of the target, in km, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losxvel: float
    """
    Line-of-sight cartesian X velocity of target, in km/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losy: float
    """
    Line-of-sight cartesian Y position of the target, in km, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losyvel: float
    """
    Line-of-sight cartesian Y velocity of target, in km/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    losz: float
    """
    Line-of-sight cartesian Z position of the target, in km, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    loszvel: float
    """
    Line-of-sight cartesian Z velocity of target, in km/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    mag: float
    """
    Measure of observed brightness calibrated against the Gaia G-band in units of
    magnitudes.
    """

    mag_norm_range: Annotated[float, PropertyInfo(alias="magNormRange")]
    """Formula: mag - 5.0 \\** log_10(geo_range / 1000000.0)."""

    mag_unc: Annotated[float, PropertyInfo(alias="magUnc")]
    """Uncertainty of the observed brightness in units of magnitudes."""

    net_obj_sig: Annotated[float, PropertyInfo(alias="netObjSig")]
    """Net object signature = counts / expDuration."""

    net_obj_sig_unc: Annotated[float, PropertyInfo(alias="netObjSigUnc")]
    """Net object signature uncertainty = counts uncertainty / expDuration."""

    ob_position: Annotated[str, PropertyInfo(alias="obPosition")]
    """The position of this observation within a track (FENCE, FIRST, IN, LAST,
    SINGLE).

    This identifier is optional and, if null, no assumption should be made regarding
    whether other observations may or may not exist to compose a track.
    """

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_object_id: Annotated[str, PropertyInfo(alias="origObjectId")]
    """
    Optional identifier provided by observation source to indicate the target
    onorbit object of this observation. This may be an internal identifier and not
    necessarily a valid satellite number.
    """

    orig_sensor_id: Annotated[str, PropertyInfo(alias="origSensorId")]
    """
    Optional identifier provided by observation source to indicate the sensor
    identifier which produced this observation. This may be an internal identifier
    and not necessarily a valid sensor ID.
    """

    penumbra: bool
    """
    Boolean indicating that the target object was in a penumbral eclipse at the time
    of this observation.
    """

    primary_extinction: Annotated[float, PropertyInfo(alias="primaryExtinction")]
    """Primary Extinction Coefficient, in Magnitudes.

    Primary Extinction is the coefficient applied to the airmass to determine how
    much the observed visual magnitude has been attenuated by the atmosphere.
    Extinction, in general, describes the absorption and scattering of
    electromagnetic radiation by dust and gas between an emitting astronomical
    object and the observer. See the EOObservationDetails API for specification of
    extinction coefficients for multiple spectral filters.
    """

    primary_extinction_unc: Annotated[float, PropertyInfo(alias="primaryExtinctionUnc")]
    """Primary Extinction Coefficient Uncertainty, in Magnitudes."""

    ra: float
    """Line of sight right ascension, in degrees, in the specified referenceFrame.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    ra_bias: Annotated[float, PropertyInfo(alias="raBias")]
    """Sensor line of sight right ascension bias in degrees."""

    ra_measured: Annotated[bool, PropertyInfo(alias="raMeasured")]
    """
    Optional flag indicating whether the ra value is measured (true) or computed
    (false). If null, consumers may consult the data provider for information
    regarding whether the corresponding value is computed or measured.
    """

    range: float
    """Line of sight range in km.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    range_bias: Annotated[float, PropertyInfo(alias="rangeBias")]
    """Sensor line of sight range bias in km."""

    range_measured: Annotated[bool, PropertyInfo(alias="rangeMeasured")]
    """
    Optional flag indicating whether the range value is measured (true) or computed
    (false). If null, consumers may consult the data provider for information
    regarding whether the corresponding value is computed or measured.
    """

    range_rate: Annotated[float, PropertyInfo(alias="rangeRate")]
    """Range rate in km/s.

    If referenceFrame is null then J2K should be assumed. Reported value should
    include all applicable corrections as specified on the source provider data
    card. If uncertain, consumers should contact the provider for details on the
    applied corrections.
    """

    range_rate_measured: Annotated[bool, PropertyInfo(alias="rangeRateMeasured")]
    """
    Optional flag indicating whether the rangeRate value is measured (true) or
    computed (false). If null, consumers may consult the data provider for
    information regarding whether the corresponding value is computed or measured.
    """

    range_rate_unc: Annotated[float, PropertyInfo(alias="rangeRateUnc")]
    """One sigma uncertainty in the line of sight range rate, in kilometers/second."""

    range_unc: Annotated[float, PropertyInfo(alias="rangeUnc")]
    """One sigma uncertainty in the line of sight range, in kilometers."""

    ra_rate: Annotated[float, PropertyInfo(alias="raRate")]
    """
    Line of sight right ascension rate of change, in degrees/sec, in the specified
    referenceFrame. If referenceFrame is null then J2K should be assumed.
    """

    ra_unc: Annotated[float, PropertyInfo(alias="raUnc")]
    """One sigma uncertainty in the line of sight right ascension angle, in degrees."""

    raw_file_uri: Annotated[str, PropertyInfo(alias="rawFileURI")]
    """
    Optional URI location in the document repository of the raw file parsed by the
    system to produce this record. To download the raw file, prepend
    https://udl-hostname/scs/download?id= to this value.
    """

    reference_frame: Annotated[Literal["J2000", "GCRF", "ITRF", "TEME"], PropertyInfo(alias="referenceFrame")]
    """The reference frame of the EOObservation measurements.

    If the referenceFrame is null it is assumed to be J2000.
    """

    sat_no: Annotated[int, PropertyInfo(alias="satNo")]
    """Satellite/Catalog number of the target on-orbit object."""

    senalt: float
    """Sensor altitude at obTime (if mobile/onorbit) in km."""

    senlat: float
    """Sensor WGS84 latitude at obTime (if mobile/onorbit) in degrees.

    If null, can be obtained from sensor info. -90 to 90 degrees (negative values
    south of equator).
    """

    senlon: float
    """Sensor WGS84 longitude at obTime (if mobile/onorbit) in degrees.

    If null, can be obtained from sensor info. -180 to 180 degrees (negative values
    west of Prime Meridian).
    """

    sen_quat: Annotated[Iterable[float], PropertyInfo(alias="senQuat")]
    """
    The quaternion describing the rotation of the sensor in relation to the
    body-fixed frame used for this system into the local geodetic frame, at
    observation time (obTime). The array element order convention is scalar
    component first, followed by the three vector components (qc, q1, q2, q3).
    """

    sen_reference_frame: Annotated[
        Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"], PropertyInfo(alias="senReferenceFrame")
    ]
    """The reference frame of the observing sensor state.

    If the senReferenceFrame is null it is assumed to be J2000.
    """

    senvelx: float
    """
    Cartesian X velocity of the observing mobile/onorbit sensor at obTime, in
    km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
    J2K should be assumed.
    """

    senvely: float
    """
    Cartesian Y velocity of the observing mobile/onorbit sensor at obTime, in
    km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
    J2K should be assumed.
    """

    senvelz: float
    """
    Cartesian Z velocity of the observing mobile/onorbit sensor at obTime, in
    km/sec, in the specified senReferenceFrame. If senReferenceFrame is null then
    J2K should be assumed.
    """

    senx: float
    """
    Cartesian X position of the observing mobile/onorbit sensor at obTime, in km, in
    the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
    assumed.
    """

    seny: float
    """
    Cartesian Y position of the observing mobile/onorbit sensor at obTime, in km, in
    the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
    assumed.
    """

    senz: float
    """
    Cartesian Z position of the observing mobile/onorbit sensor at obTime, in km, in
    the specified senReferenceFrame. If senReferenceFrame is null then J2K should be
    assumed.
    """

    shutter_delay: Annotated[float, PropertyInfo(alias="shutterDelay")]
    """Shutter delay in seconds."""

    sky_bkgrnd: Annotated[float, PropertyInfo(alias="skyBkgrnd")]
    """Average Sky Background signal, in Magnitudes.

    Sky Background refers to the incoming light from an apparently empty part of the
    night sky.
    """

    solar_dec_angle: Annotated[float, PropertyInfo(alias="solarDecAngle")]
    """Angle from the sun to the equatorial plane."""

    solar_eq_phase_angle: Annotated[float, PropertyInfo(alias="solarEqPhaseAngle")]
    """
    The angle, in degrees, between the projections of the target-to-observer vector
    and the target-to-sun vector onto the equatorial plane. The angle is represented
    as negative when closing (i.e. before the opposition) and positive when opening
    (after the opposition).
    """

    solar_phase_angle: Annotated[float, PropertyInfo(alias="solarPhaseAngle")]
    """
    The angle, in degrees, between the target-to-observer vector and the
    target-to-sun vector.
    """

    tags: List[str]
    """
    Optional array of provider/source specific tags for this data, where each
    element is no longer than 32 characters, used for implementing data owner
    conditional access controls to restrict access to the data. Should be left null
    by data providers unless conditional access controls are coordinated with the
    UDL team.
    """

    task_id: Annotated[str, PropertyInfo(alias="taskId")]
    """
    Optional identifier to indicate the specific tasking which produced this
    observation.
    """

    timing_bias: Annotated[float, PropertyInfo(alias="timingBias")]
    """Sensor timing bias in seconds."""

    track_id: Annotated[str, PropertyInfo(alias="trackId")]
    """Optional identifier of the track to which this observation belongs."""

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
    """
    Optional identifier to track a commercial or marketplace transaction executed to
    produce this data.
    """

    uct: bool
    """
    Boolean indicating this observation is part of an uncorrelated track or was
    unable to be correlated to a known object. This flag should only be set to true
    by data providers after an attempt to correlate to an on-orbit object was made
    and failed. If unable to correlate, the 'origObjectId' field may be populated
    with an internal data provider specific identifier.
    """

    umbra: bool
    """
    Boolean indicating that the target object was in umbral eclipse at the time of
    this observation.
    """

    zeroptd: float
    """Formula: 2.5 \\** log_10 (zero_mag_counts / expDuration)."""

    zero_ptd_unc: Annotated[float, PropertyInfo(alias="zeroPtdUnc")]
    """
    This is the uncertainty in the zero point for the filter used for this
    observation/row in units of mag. For use with differential photometry.
    """
