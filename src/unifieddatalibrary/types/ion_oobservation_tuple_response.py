# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "IonOobservationTupleResponse",
    "IonOobservationTupleResponseItem",
    "IonOobservationTupleResponseItemAmplitude",
    "IonOobservationTupleResponseItemAntennaElementPosition",
    "IonOobservationTupleResponseItemAzimuth",
    "IonOobservationTupleResponseItemCharAtt",
    "IonOobservationTupleResponseItemDatum",
    "IonOobservationTupleResponseItemDensityProfile",
    "IonOobservationTupleResponseItemDensityProfileIri",
    "IonOobservationTupleResponseItemDensityProfileParabolic",
    "IonOobservationTupleResponseItemDensityProfileParabolicParabolicItem",
    "IonOobservationTupleResponseItemDensityProfileQuasiParabolic",
    "IonOobservationTupleResponseItemDensityProfileQuasiParabolicQuasiParabolicSegment",
    "IonOobservationTupleResponseItemDensityProfileShiftedChebyshev",
    "IonOobservationTupleResponseItemDensityProfileShiftedChebyshevShiftedChebyshev",
    "IonOobservationTupleResponseItemDensityProfileTopsideExtensionChapmanConst",
    "IonOobservationTupleResponseItemDensityProfileTopsideExtensionVaryChap",
    "IonOobservationTupleResponseItemDoppler",
    "IonOobservationTupleResponseItemElevation",
    "IonOobservationTupleResponseItemFrequency",
    "IonOobservationTupleResponseItemPhase",
    "IonOobservationTupleResponseItemPolarization",
    "IonOobservationTupleResponseItemPower",
    "IonOobservationTupleResponseItemRange",
    "IonOobservationTupleResponseItemScalerInfo",
    "IonOobservationTupleResponseItemStokes",
    "IonOobservationTupleResponseItemTime",
    "IonOobservationTupleResponseItemTraceGeneric",
]


class IonOobservationTupleResponseItemAmplitude(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of amplitude data."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers for amplitude dimensions."""

    notes: Optional[str] = None
    """Notes for the amplitude data."""


class IonOobservationTupleResponseItemAntennaElementPosition(BaseModel):
    data: Optional[List[List[float]]] = None
    """Array of 3-element tuples (x,y,z) in km."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the antenna_element dimensions."""


class IonOobservationTupleResponseItemAzimuth(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of incoming azimuth at the receiver."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the azimuth array dimensions."""

    notes: Optional[str] = None
    """Notes for the azimuth data."""


class IonOobservationTupleResponseItemCharAtt(BaseModel):
    char_name: Optional[str] = FieldInfo(alias="charName", default=None)
    """Characteristic name.

    This value should reflect the UDL field name for the corresponding
    characteristic.
    """

    climate_model_input_params: Optional[List[str]] = FieldInfo(alias="climateModelInputParams", default=None)
    """Input parameters for the climate model."""

    climate_model_name: Optional[str] = FieldInfo(alias="climateModelName", default=None)
    """Name of the climate model."""

    climate_model_options: Optional[List[str]] = FieldInfo(alias="climateModelOptions", default=None)
    """List of options for the climate model."""

    d: Optional[str] = None
    """Descriptive letter (D) for the characteristic specified by URSI ID.

    Describes specific ionospheric conditions, beyond numerical values.
    """

    lower_bound: Optional[float] = FieldInfo(alias="lowerBound", default=None)
    """Specified characteristic's lower bound.

    Should be less than or equal to the characteristic's current value as set in
    this record.
    """

    q: Optional[str] = None
    """Qualifying letter (Q) for the characteristic specified by URSI ID.

    Describes specific ionospheric conditions, beyond numerical values.
    """

    uncertainty_bound_type: Optional[str] = FieldInfo(alias="uncertaintyBoundType", default=None)
    """
    Uncertainty Bounds (lower and upper) define an interval around reported value
    that contains true value at the specified probability level. Probability levels
    are specified in terms of percentile (from 1 to 100) or the standard deviation,
    sigma (e.g. 1sigma, 2sigma, 3sigma, 5percentile, 10percentile, 25percentile).
    """

    upper_bound: Optional[float] = FieldInfo(alias="upperBound", default=None)
    """Specified characteristic's upper bound.

    Should be greater than or equal to the characteristic's current value as set in
    this record.
    """

    ursi_id: Optional[str] = FieldInfo(alias="ursiID", default=None)
    """Characteristic's URSI ID.

    See the characteristic's description for its corresponding URSI ID.
    """


class IonOobservationTupleResponseItemDatum(BaseModel):
    data: Optional[List[float]] = None
    """Array to support sparse data collections."""

    notes: Optional[str] = None
    """Notes for the datum with details of what the data is, units, etc."""


class IonOobservationTupleResponseItemDensityProfileIri(BaseModel):
    b0: Optional[float] = None
    """B0 parameter of the F2 layer shape."""

    b1: Optional[float] = None
    """B1 parameter of the F2 layer shape."""

    chi: Optional[float] = None
    """
    Peak Density Thickness (PDT) for description of the flat-nose shape, in
    kilometers.
    """

    d1: Optional[float] = None
    """D1 parameter of the F1 layer shape."""

    description: Optional[str] = None
    """Description of IRI implementation."""

    fp1: Optional[float] = None
    """TBD."""

    fp2: Optional[float] = None
    """TBD."""

    fp30: Optional[float] = None
    """TBD."""

    fp3_u: Optional[float] = FieldInfo(alias="fp3U", default=None)
    """TBD."""

    ha: Optional[float] = None
    """Starting height of the D layer, in kilometers."""

    hdx: Optional[float] = None
    """Height of the intermediate region at the top of D region, in kilometers."""

    hm_d: Optional[float] = FieldInfo(alias="hmD", default=None)
    """Peak height of the D layer, in kilometers."""

    hm_e: Optional[float] = FieldInfo(alias="hmE", default=None)
    """Peak height of the F2 layer, in kilometers."""

    hm_f1: Optional[float] = FieldInfo(alias="hmF1", default=None)
    """Peak height of the F1 layer, in kilometers."""

    hm_f2: Optional[float] = FieldInfo(alias="hmF2", default=None)
    """Peak height of F2 layer, in kilometers."""

    h_val_top: Optional[float] = FieldInfo(alias="hValTop", default=None)
    """The valley height, in kilometers."""

    hz: Optional[float] = None
    """Height HZ of the interim layer, in kilometers."""

    nm_d: Optional[float] = FieldInfo(alias="nmD", default=None)
    """Peak density of the D layer, in per cubic centimeter."""

    nm_e: Optional[float] = FieldInfo(alias="nmE", default=None)
    """Peak density of the E layer, in per cubic centimeter."""

    nm_f1: Optional[float] = FieldInfo(alias="nmF1", default=None)
    """Peak density of the F1 layer, in grams per cubic centimeter."""

    nm_f2: Optional[float] = FieldInfo(alias="nmF2", default=None)
    """Peak density of F2 layer, in grams per cubic centimeter."""

    n_val_b: Optional[float] = FieldInfo(alias="nValB", default=None)
    """The valley depth, in grams per cubic centimeter."""


class IonOobservationTupleResponseItemDensityProfileParabolicParabolicItem(BaseModel):
    f: Optional[float] = None
    """Plasma frequency at the layer peak, in MHz."""

    layer: Optional[str] = None
    """Ionospheric plasma layer (E, F1, or F2)."""

    y: Optional[float] = None
    """Half-thickness of the layer, in kilometers."""

    z: Optional[float] = None
    """Height of the layer peak, in kilometers."""


class IonOobservationTupleResponseItemDensityProfileParabolic(BaseModel):
    description: Optional[str] = None
    """General description of the QP computation algorithm."""

    parabolic_items: Optional[List[IonOobservationTupleResponseItemDensityProfileParabolicParabolicItem]] = FieldInfo(
        alias="parabolicItems", default=None
    )
    """Describes the E, F1, and F2 layers as parabolic-shape segments."""


class IonOobservationTupleResponseItemDensityProfileQuasiParabolicQuasiParabolicSegment(BaseModel):
    a: Optional[float] = None
    """Coefficient A."""

    b: Optional[float] = None
    """Coefficient B."""

    c: Optional[float] = None
    """Coefficient C."""

    error: Optional[float] = None
    """Best-fit error."""

    index: Optional[int] = None
    """The index of this segment in the list, from 1 to NumSegments."""

    rb: Optional[float] = None
    """Starting range of the segment, in kilometers from the Earth's center."""

    re: Optional[float] = None
    """Ending range of the segment, in kilometers from the Earth's center."""


class IonOobservationTupleResponseItemDensityProfileQuasiParabolic(BaseModel):
    description: Optional[str] = None
    """General description of the quasi-parabolic computation algorithm."""

    earth_radius: Optional[float] = FieldInfo(alias="earthRadius", default=None)
    """Value of the Earth's radius, in kilometers, used for computations."""

    quasi_parabolic_segments: Optional[
        List[IonOobservationTupleResponseItemDensityProfileQuasiParabolicQuasiParabolicSegment]
    ] = FieldInfo(alias="quasiParabolicSegments", default=None)
    """Array of quasi-parabolic segments.

    Each segment is the best-fit 3-parameter quasi-parabolas defined via A, B, C
    coefficients, f^2=A/r^2+B/r+C”. Usually 3 groups for E, F1, and F2 layers, but
    additional segments may be used to improve accuracy.
    """


class IonOobservationTupleResponseItemDensityProfileShiftedChebyshevShiftedChebyshev(BaseModel):
    coeffs: Optional[List[float]] = None
    """Array of coefficients."""

    error: Optional[float] = None
    """Best fit error."""

    fstart: Optional[float] = None
    """Start frequency of the layer, in MHz."""

    fstop: Optional[float] = None
    """Stop frequency of the layer, in MHz."""

    layer: Optional[str] = None
    """The ionospheric plasma layer."""

    n: Optional[int] = None
    """Number of coefficients in the expansion."""

    peakheight: Optional[float] = None
    """Peak height of the layer, in kilometers."""

    zhalf_nm: Optional[float] = FieldInfo(alias="zhalfNm", default=None)
    """Height at which density is half of the peak Nm, in kilometers."""


class IonOobservationTupleResponseItemDensityProfileShiftedChebyshev(BaseModel):
    description: Optional[str] = None
    """Description of the computation technique."""

    shifted_chebyshevs: Optional[
        List[IonOobservationTupleResponseItemDensityProfileShiftedChebyshevShiftedChebyshev]
    ] = FieldInfo(alias="shiftedChebyshevs", default=None)
    """
    Up to 3 groups of coefficients, using “shiftedChebyshev” sub-field, to describe
    E, F1, and bottomside F2 profile shapes, or up to 6 groups of coefficients to
    describe height uncertainty boundaries (upper and lower).
    """


class IonOobservationTupleResponseItemDensityProfileTopsideExtensionChapmanConst(BaseModel):
    chi: Optional[float] = None
    """
    Peak Density Thickness (PDT) for description of the flat-nose shape, in
    kilometers.
    """

    description: Optional[str] = None
    """Description of the Chapman computation technique."""

    hm_f2: Optional[float] = FieldInfo(alias="hmF2", default=None)
    """Peak height of F2 layer, in kilometers."""

    nm_f2: Optional[float] = FieldInfo(alias="nmF2", default=None)
    """Peak density of F2 layer, in grams per cubic centimeter."""

    scale_f2: Optional[float] = FieldInfo(alias="scaleF2", default=None)
    """Scale height if F2 layer at the peak, in kilometers."""


class IonOobservationTupleResponseItemDensityProfileTopsideExtensionVaryChap(BaseModel):
    alpha: Optional[float] = None
    """Alpha parameter of the profile shape."""

    beta: Optional[float] = None
    """Beta parameter of the profile shape."""

    chi: Optional[float] = None
    """
    Peak Density Thickness (PDT) for description of the flat-nose shape, in
    kilometers.
    """

    description: Optional[str] = None
    """Description of the Chapman computation technique."""

    hm_f2: Optional[float] = FieldInfo(alias="hmF2", default=None)
    """Peak height of F2 layer, in kilometers."""

    ht: Optional[float] = None
    """Transition height, in kilometers."""

    nm_f2: Optional[float] = FieldInfo(alias="nmF2", default=None)
    """Peak density of F2 layer, in grams per cubic centimeter."""

    scale_f2: Optional[float] = FieldInfo(alias="scaleF2", default=None)
    """Scale height if F2 layer at the peak, in kilometers."""


class IonOobservationTupleResponseItemDensityProfile(BaseModel):
    iri: Optional[IonOobservationTupleResponseItemDensityProfileIri] = None
    """Full set of the IRI formalism coefficients."""

    parabolic: Optional[IonOobservationTupleResponseItemDensityProfileParabolic] = None
    """Coefficients to describe the E, F1, and F2 layers as parabolic-shape segments."""

    quasi_parabolic: Optional[IonOobservationTupleResponseItemDensityProfileQuasiParabolic] = FieldInfo(
        alias="quasiParabolic", default=None
    )
    """Coefficients to describe profile shape as quasi-parabolic segments."""

    shifted_chebyshev: Optional[IonOobservationTupleResponseItemDensityProfileShiftedChebyshev] = FieldInfo(
        alias="shiftedChebyshev", default=None
    )
    """
    Coefficients to describe either the E, F1, and bottomside F2 profile shapes or
    the height uncertainty boundaries.
    """

    topside_extension_chapman_const: Optional[
        IonOobservationTupleResponseItemDensityProfileTopsideExtensionChapmanConst
    ] = FieldInfo(alias="topsideExtensionChapmanConst", default=None)
    """Parameters of the constant-scale-height Chapman layer."""

    topside_extension_vary_chap: Optional[IonOobservationTupleResponseItemDensityProfileTopsideExtensionVaryChap] = (
        FieldInfo(alias="topsideExtensionVaryChap", default=None)
    )
    """Varying scale height Chapman topside layer."""

    valley_model_coeffs: Optional[List[float]] = FieldInfo(alias="valleyModelCoeffs", default=None)
    """Array of valley model coefficients."""

    valley_model_description: Optional[str] = FieldInfo(alias="valleyModelDescription", default=None)
    """Description of the valley model and parameters."""


class IonOobservationTupleResponseItemDoppler(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of received doppler shifts in Hz."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the doppler array dimensions."""

    notes: Optional[str] = None
    """Notes for the doppler data."""


class IonOobservationTupleResponseItemElevation(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of incoming elevation at the receiver."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the elevation array dimensions."""

    notes: Optional[str] = None
    """Notes for the elevation data."""


class IonOobservationTupleResponseItemFrequency(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of frequency data."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for frequency dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the frequency array dimensions."""

    notes: Optional[str] = None
    """Notes for the frequency data."""


class IonOobservationTupleResponseItemPhase(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of phase data."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for phase dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the phase array dimensions."""

    notes: Optional[str] = None
    """Notes for the phase data.

    Orientation and position for each antenna element across the antenna_element
    dimension.
    """


class IonOobservationTupleResponseItemPolarization(BaseModel):
    data: Optional[List[List[List[List[List[List[List[Literal["X", "O"]]]]]]]]] = None
    """Array of polarization data."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers for polarization dimensions."""

    notes: Optional[str] = None
    """Notes for the polarization data."""


class IonOobservationTupleResponseItemPower(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of received power in db."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the power array dimensions."""

    notes: Optional[str] = None
    """Notes for the power data."""


class IonOobservationTupleResponseItemRange(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of range data."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for range dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the range array dimensions."""

    notes: Optional[str] = None
    """Notes for the range data."""


class IonOobservationTupleResponseItemScalerInfo(BaseModel):
    confidence_level: Optional[int] = FieldInfo(alias="confidenceLevel", default=None)
    """Scaler confidence level."""

    confidence_score: Optional[int] = FieldInfo(alias="confidenceScore", default=None)
    """Scaler confidence score."""

    name: Optional[str] = None
    """Scaler name."""

    organization: Optional[str] = None
    """Scaler organization."""

    type: Optional[str] = None
    """Scaler type (MANUAL, AUTOMATIC or UNKNOWN)."""

    version: Optional[float] = None
    """Scaler version."""


class IonOobservationTupleResponseItemStokes(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """Array of received stokes data."""

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the stoke array dimensions."""

    notes: Optional[str] = None
    """Notes for the stokes data."""

    s: Optional[List[float]] = None
    """S1, S2, and S3 (the normalized Stokes parameters 1, 2, and 3)."""


class IonOobservationTupleResponseItemTime(BaseModel):
    data: Optional[List[List[List[List[List[List[List[float]]]]]]]] = None
    """
    Array of times in number of seconds passed since January 1st, 1970 with the same
    dimensions as power.
    """

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of names for dimensions."""

    dimensions: Optional[List[int]] = None
    """Array of integers of the time array dimensions."""

    notes: Optional[str] = None
    """The notes indicate the scheme and accuracy."""


class IonOobservationTupleResponseItemTraceGeneric(BaseModel):
    data: Optional[List[List[List[float]]]] = None
    """Multi-dimensional Array.

    The 1st dimension spans points along the trace while the 2nd dimension spans
    frequency-range pairs.
    """

    dimension_name: Optional[List[str]] = FieldInfo(alias="dimensionName", default=None)
    """Array of dimension names for trace generic data."""

    notes: Optional[str] = None
    """Notes for the trace generic data."""


class IonOobservationTupleResponseItem(BaseModel):
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

    source: str
    """Source of the data."""

    start_time_utc: datetime = FieldInfo(alias="startTimeUTC")
    """Sounding Start time in ISO8601 UTC format."""

    station_id: str = FieldInfo(alias="stationId")
    """URSI code for station or stations producing the ionosonde."""

    system: str
    """
    Ionosonde hardware type or data collection type together with possible
    additional descriptors.
    """

    system_info: str = FieldInfo(alias="systemInfo")
    """Names of settings."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    amplitude: Optional[IonOobservationTupleResponseItemAmplitude] = None

    antenna_element_position: Optional[IonOobservationTupleResponseItemAntennaElementPosition] = FieldInfo(
        alias="antennaElementPosition", default=None
    )

    antenna_element_position_coordinate_system: Optional[
        Literal["J2000", "ECR/ECEF", "TEME", "GCRF", "WGS84 (GEODetic lat, long, alt)", "GEOCentric (lat, long, radii)"]
    ] = FieldInfo(alias="antennaElementPositionCoordinateSystem", default=None)
    """
    Enums: J2000, ECR/ECEF, TEME, GCRF, WGS84 (GEODetic lat, long, alt), GEOCentric
    (lat, long, radii).
    """

    artist_flags: Optional[List[int]] = FieldInfo(alias="artistFlags", default=None)
    """Array of Legacy Artist Flags."""

    azimuth: Optional[IonOobservationTupleResponseItemAzimuth] = None

    b0: Optional[float] = None
    """IRI thickness parameter in km. URSI ID: D0."""

    b1: Optional[float] = None
    """IRI profile shape parameter. URSI ID: D1."""

    char_atts: Optional[List[IonOobservationTupleResponseItemCharAtt]] = FieldInfo(alias="charAtts", default=None)
    """List of attributes that are associated with the specified characteristics.

    Characteristics are defined by the CHARS: URSI IIWG format for archiving monthly
    ionospheric characteristics, INAG Bulletin No. 62 specification. Qualifying and
    Descriptive letters are defined by the URSI Handbook for Ionogram Interpretation
    and reduction, Report UAG, No. 23A specification.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    d: Optional[float] = None
    """Distance for MUF calculation in km."""

    d1: Optional[float] = None
    """IRI profile shape parameter, F1 layer. URSI ID: D2."""

    datum: Optional[IonOobservationTupleResponseItemDatum] = None

    deltafo_f2: Optional[float] = FieldInfo(alias="deltafoF2", default=None)
    """Adjustment to the scaled foF2 during profile inversion in MHz."""

    density_profile: Optional[IonOobservationTupleResponseItemDensityProfile] = FieldInfo(
        alias="densityProfile", default=None
    )
    """
    Profile of electron densities in the ionosphere associated with an
    IonoObservation.
    """

    doppler: Optional[IonOobservationTupleResponseItemDoppler] = None

    down_e: Optional[float] = FieldInfo(alias="downE", default=None)
    """Lowering of E trace to the leading edge in km."""

    down_es: Optional[float] = FieldInfo(alias="downEs", default=None)
    """Lowering of Es trace to the leading edge in km."""

    down_f: Optional[float] = FieldInfo(alias="downF", default=None)
    """Lowering of F trace to the leading edge in km."""

    electron_density: Optional[List[float]] = FieldInfo(alias="electronDensity", default=None)
    """
    Array of electron densities in cm^-3 (must match the size of the height and
    plasmaFrequency arrays).
    """

    electron_density_uncertainty: Optional[List[float]] = FieldInfo(alias="electronDensityUncertainty", default=None)
    """
    Uncertainty in specifying the electron density at each height point of the
    profile (must match the size of the electronDensity array).
    """

    elevation: Optional[IonOobservationTupleResponseItemElevation] = None

    fb_es: Optional[float] = FieldInfo(alias="fbEs", default=None)
    """The blanketing frequency of layer used to derive foEs in MHz. URSI ID: 32."""

    fe: Optional[float] = None
    """Frequency spread beyond foE in MHz. URSI ID: 87."""

    ff: Optional[float] = None
    """Frequency spread between fxF2 and FxI in MHz. URSI ID: 86."""

    fhprime_f: Optional[float] = FieldInfo(alias="fhprimeF", default=None)
    """The frequency at which hprimeF is measured in MHz. URSI ID: 61."""

    fhprime_f2: Optional[float] = FieldInfo(alias="fhprimeF2", default=None)
    """The frequency at which hprimeF2 is measured in MHz. URSI ID: 60."""

    fmin: Optional[float] = None
    """Lowest frequency at which echo traces are observed on the ionogram, in MHz.

    URSI ID: 42.
    """

    fmin_e: Optional[float] = FieldInfo(alias="fminE", default=None)
    """Minimum frequency of E layer echoes in MHz. URSI ID: 81."""

    fmin_es: Optional[float] = FieldInfo(alias="fminEs", default=None)
    """Minimum frequency of Es layer in MHz."""

    fmin_f: Optional[float] = FieldInfo(alias="fminF", default=None)
    """Minimum frequency of F layer echoes in MHz. URSI ID: 80."""

    fmuf: Optional[float] = None
    """MUF/OblFactor in MHz."""

    fo_e: Optional[float] = FieldInfo(alias="foE", default=None)
    """
    The ordinary wave critical frequency of the lowest thick layer which causes a
    discontinuity, in MHz. URSI ID: 20.
    """

    fo_ea: Optional[float] = FieldInfo(alias="foEa", default=None)
    """Critical frequency of night time auroral E layer in MHz. URSI ID: 23."""

    fo_ep: Optional[float] = FieldInfo(alias="foEp", default=None)
    """Predicted value of foE in MHz."""

    fo_es: Optional[float] = FieldInfo(alias="foEs", default=None)
    """
    Highest ordinary wave frequency at which a mainly continuous Es trace is
    observed, in MHz. URSI ID: 30.
    """

    fo_f1: Optional[float] = FieldInfo(alias="foF1", default=None)
    """The ordinary wave F1 critical frequency, in MHz. URSI ID: 10."""

    fo_f1p: Optional[float] = FieldInfo(alias="foF1p", default=None)
    """Predicted value of foF1 in MHz."""

    fo_f2: Optional[float] = FieldInfo(alias="foF2", default=None)
    """
    The ordinary wave critical frequency of the highest stratification in the F
    region, specified in MHz. URSI ID: 00.
    """

    fo_f2p: Optional[float] = FieldInfo(alias="foF2p", default=None)
    """Predicted value of foF2 in MHz."""

    fo_p: Optional[float] = FieldInfo(alias="foP", default=None)
    """Highest ordinary wave critical frequency of F region patch trace in MHz.

    URSI ID: 55.
    """

    frequency: Optional[IonOobservationTupleResponseItemFrequency] = None

    fx_e: Optional[float] = FieldInfo(alias="fxE", default=None)
    """The extraordinary wave E critical frequency, in MHz. URSI ID: 21."""

    fx_f1: Optional[float] = FieldInfo(alias="fxF1", default=None)
    """The extraordinary wave F1 critical frequency, in MHz. URSI ID: 11."""

    fx_f2: Optional[float] = FieldInfo(alias="fxF2", default=None)
    """The extraordinary wave F2 critical frequency, in MHz. URSI ID: 01."""

    fx_i: Optional[float] = FieldInfo(alias="fxI", default=None)
    """The highest frequency of F-trace in MHz.

    Note: fxI is with capital i. URSI ID: 51.
    """

    height: Optional[List[float]] = None
    """
    Array of altitudes above station level for plasma frequency/density arrays in km
    (must match the size of the plasmaFrequency and electronDensity Arrays).
    """

    hm_e: Optional[float] = FieldInfo(alias="hmE", default=None)
    """True height of the E peak in km. URSI ID: CE."""

    hm_f1: Optional[float] = FieldInfo(alias="hmF1", default=None)
    """True height of the F1 peak in km. URSI ID: BE."""

    hm_f2: Optional[float] = FieldInfo(alias="hmF2", default=None)
    """True height of the F2 peak in km. URSI ID: AE."""

    hprime_e: Optional[float] = FieldInfo(alias="hprimeE", default=None)
    """The minimum virtual height of the normal E layer trace in km. URSI ID: 24."""

    hprime_ea: Optional[float] = FieldInfo(alias="hprimeEa", default=None)
    """Minimum virtual height of night time auroral E layer trace in km. URSI ID: 27."""

    hprime_es: Optional[float] = FieldInfo(alias="hprimeEs", default=None)
    """The minimum height of the trace used to give foEs in km. URSI ID: 34."""

    hprime_f: Optional[float] = FieldInfo(alias="hprimeF", default=None)
    """The minimum virtual height of the ordinary wave trace taken as a whole, in km.

    URSI ID: 16.
    """

    hprime_f1: Optional[float] = FieldInfo(alias="hprimeF1", default=None)
    """
    The minimum virtual height of reflection at a point where the trace is
    horizontal in the F region in km. URSI ID: 14.
    """

    hprime_f2: Optional[float] = FieldInfo(alias="hprimeF2", default=None)
    """
    The minimum virtual height of ordinary wave trace for the highest stable
    stratification in the F region in km. URSI ID: 4.
    """

    hprimef_muf: Optional[float] = FieldInfo(alias="hprimefMUF", default=None)
    """Virtual height at MUF/OblFactor frequency in MHz."""

    hprime_p: Optional[float] = FieldInfo(alias="hprimeP", default=None)
    """Minimum virtual height of the trace used to determine foP in km. URSI ID: 56."""

    id_sensor: Optional[str] = FieldInfo(alias="idSensor", default=None)
    """Unique identifier of the reporting sensor."""

    luf: Optional[float] = None
    """Lowest usable frequency."""

    md: Optional[float] = None
    """MUF(D)/foF2."""

    mufd: Optional[float] = None
    """Maximum Usable Frequency for ground distance D in MHz."""

    ne_profile_name: Optional[str] = FieldInfo(alias="neProfileName", default=None)
    """Name of the algorithm used for the electron density profile."""

    ne_profile_version: Optional[float] = FieldInfo(alias="neProfileVersion", default=None)
    """Version of the algorithm used for the electron density profile."""

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
    """
    Optional identifier provided by observation source to indicate the sensor
    identifier which produced this observation. This may be an internal identifier
    and not necessarily a valid sensor ID.
    """

    phase: Optional[IonOobservationTupleResponseItemPhase] = None

    plasma_frequency: Optional[List[float]] = FieldInfo(alias="plasmaFrequency", default=None)
    """
    Array of plasma frequencies in MHz (must match the size of the height and
    electronDensity arrays).
    """

    plasma_frequency_uncertainty: Optional[List[float]] = FieldInfo(alias="plasmaFrequencyUncertainty", default=None)
    """
    Uncertainty in specifying the electron plasma frequency at each height point of
    the profile (must match the size of the plasmaFrequency array).
    """

    platform_name: Optional[str] = FieldInfo(alias="platformName", default=None)
    """Equipment location."""

    polarization: Optional[IonOobservationTupleResponseItemPolarization] = None

    power: Optional[IonOobservationTupleResponseItemPower] = None

    qe: Optional[float] = None
    """Average range spread of E layer in km. URSI ID: 85."""

    qf: Optional[float] = None
    """Average range spread of F layer in km. URSI ID: 84."""

    range: Optional[IonOobservationTupleResponseItemRange] = None

    receive_coordinates: Optional[List[List[float]]] = FieldInfo(alias="receiveCoordinates", default=None)
    """
    List of Geodetic Latitude, Longitude, and Altitude coordinates in km of the
    receiver. Coordinates List must always have 3 elements. Valid ranges are -90.0
    to 90.0 for Latitude and -180.0 to 180.0 for Longitude. Altitude is in km and
    its value must be 0 or greater.
    """

    receive_sensor_type: Optional[Literal["Mobile", "Static"]] = FieldInfo(alias="receiveSensorType", default=None)
    """Enums: Mobile, Static."""

    restricted_frequency: Optional[List[float]] = FieldInfo(alias="restrictedFrequency", default=None)
    """Array of restricted frequencies."""

    restricted_frequency_notes: Optional[str] = FieldInfo(alias="restrictedFrequencyNotes", default=None)
    """Notes for the restrictedFrequency data."""

    scale_height_f2_peak: Optional[float] = FieldInfo(alias="scaleHeightF2Peak", default=None)
    """Effective scale height at hmF2 Titheridge method in km. URSI ID: 69."""

    scaler_info: Optional[IonOobservationTupleResponseItemScalerInfo] = FieldInfo(alias="scalerInfo", default=None)
    """
    The ScalerInfo record describes the person or system who interpreted the
    ionogram in IonoObservation.
    """

    stokes: Optional[IonOobservationTupleResponseItemStokes] = None

    system_notes: Optional[str] = FieldInfo(alias="systemNotes", default=None)
    """Details concerning the composition/intention/interpretation/audience/etc.

    of any data recorded here. This field may contain all of the intended
    information e.g. info on signal waveforms used, antenna setup, etc. OR may
    describe the data/settings to be provided in the “data” field.
    """

    tec: Optional[float] = None
    """Total Ionospheric Electron Content \\**10^16e/m^2.

    1 TEC Unit (TECU) = 10^16 electrons/m^2. URSI ID: 72.
    """

    tid_azimuth: Optional[List[float]] = FieldInfo(alias="tidAzimuth", default=None)
    """Array of degrees clockwise from true North of the TID."""

    tid_periods: Optional[List[float]] = FieldInfo(alias="tidPeriods", default=None)
    """Array of 1/frequency of the TID wave."""

    tid_phase_speeds: Optional[List[float]] = FieldInfo(alias="tidPhaseSpeeds", default=None)
    """Array of speed in m/s at which the disturbance travels through the ionosphere."""

    time: Optional[IonOobservationTupleResponseItemTime] = None

    trace_generic: Optional[IonOobservationTupleResponseItemTraceGeneric] = FieldInfo(
        alias="traceGeneric", default=None
    )

    transmit_coordinates: Optional[List[List[float]]] = FieldInfo(alias="transmitCoordinates", default=None)
    """
    List of Geodetic Latitude, Longitude, and Altitude coordinates in km of the
    receiver. Coordinates List must always have 3 elements. Valid ranges are -90.0
    to 90.0 for Latitude and -180.0 to 180.0 for Longitude. Altitude is in km and
    its value must be 0 or greater.
    """

    transmit_sensor_type: Optional[Literal["Mobile", "Static"]] = FieldInfo(alias="transmitSensorType", default=None)
    """Enums: Mobile, Static."""

    type_es: Optional[str] = FieldInfo(alias="typeEs", default=None)
    """Characterization of the shape of Es trace. URSI ID: 36."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    Time the row was updated in the database, auto-populated by the system, example
    = 2018-01-01T16:00:00.123Z.
    """

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    y_e: Optional[float] = FieldInfo(alias="yE", default=None)
    """Parabolic E layer semi-thickness in km. URSI ID: 83."""

    y_f1: Optional[float] = FieldInfo(alias="yF1", default=None)
    """Parabolic F1 layer semi-thickness in km. URSI ID: 95."""

    y_f2: Optional[float] = FieldInfo(alias="yF2", default=None)
    """Parabolic F2 layer semi-thickness in km. URSI ID: 94."""

    zhalf_nm: Optional[float] = FieldInfo(alias="zhalfNm", default=None)
    """True height at half peak electron density in the F2 layer in km. URSI ID: 93."""

    zm_e: Optional[float] = FieldInfo(alias="zmE", default=None)
    """Peak height of E-layer in km. URSI ID: 90."""


IonOobservationTupleResponse: TypeAlias = List[IonOobservationTupleResponseItem]
