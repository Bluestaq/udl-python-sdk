# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IonOobservationCreateBulkParams",
    "Body",
    "BodyAmplitude",
    "BodyAntennaElementPosition",
    "BodyAzimuth",
    "BodyCharAtt",
    "BodyDatum",
    "BodyDensityProfile",
    "BodyDensityProfileIri",
    "BodyDensityProfileParabolic",
    "BodyDensityProfileParabolicParabolicItem",
    "BodyDensityProfileQuasiParabolic",
    "BodyDensityProfileQuasiParabolicQuasiParabolicSegment",
    "BodyDensityProfileShiftedChebyshev",
    "BodyDensityProfileShiftedChebyshevShiftedChebyshev",
    "BodyDensityProfileTopsideExtensionChapmanConst",
    "BodyDensityProfileTopsideExtensionVaryChap",
    "BodyDoppler",
    "BodyElevation",
    "BodyFrequency",
    "BodyPhase",
    "BodyPolarization",
    "BodyPower",
    "BodyRange",
    "BodyScalerInfo",
    "BodyStokes",
    "BodyTime",
    "BodyTraceGeneric",
]


class IonOobservationCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyAmplitude(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of amplitude data."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers for amplitude dimensions."""

    notes: str
    """Notes for the amplitude data."""


class BodyAntennaElementPosition(TypedDict, total=False):
    data: Iterable[Iterable[float]]
    """Array of 3-element tuples (x,y,z) in km."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the antenna_element dimensions."""


class BodyAzimuth(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of incoming azimuth at the receiver."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the azimuth array dimensions."""

    notes: str
    """Notes for the azimuth data."""


class BodyCharAtt(TypedDict, total=False):
    char_name: Annotated[str, PropertyInfo(alias="charName")]
    """Characteristic name.

    This value should reflect the UDL field name for the corresponding
    characteristic.
    """

    climate_model_input_params: Annotated[List[str], PropertyInfo(alias="climateModelInputParams")]
    """Input parameters for the climate model."""

    climate_model_name: Annotated[str, PropertyInfo(alias="climateModelName")]
    """Name of the climate model."""

    climate_model_options: Annotated[List[str], PropertyInfo(alias="climateModelOptions")]
    """List of options for the climate model."""

    d: str
    """Descriptive letter (D) for the characteristic specified by URSI ID.

    Describes specific ionospheric conditions, beyond numerical values.
    """

    lower_bound: Annotated[float, PropertyInfo(alias="lowerBound")]
    """Specified characteristic's lower bound.

    Should be less than or equal to the characteristic's current value as set in
    this record.
    """

    q: str
    """Qualifying letter (Q) for the characteristic specified by URSI ID.

    Describes specific ionospheric conditions, beyond numerical values.
    """

    uncertainty_bound_type: Annotated[str, PropertyInfo(alias="uncertaintyBoundType")]
    """
    Uncertainty Bounds (lower and upper) define an interval around reported value
    that contains true value at the specified probability level. Probability levels
    are specified in terms of percentile (from 1 to 100) or the standard deviation,
    sigma (e.g. 1sigma, 2sigma, 3sigma, 5percentile, 10percentile, 25percentile).
    """

    upper_bound: Annotated[float, PropertyInfo(alias="upperBound")]
    """Specified characteristic's upper bound.

    Should be greater than or equal to the characteristic's current value as set in
    this record.
    """

    ursi_id: Annotated[str, PropertyInfo(alias="ursiID")]
    """Characteristic's URSI ID.

    See the characteristic's description for its corresponding URSI ID.
    """


class BodyDatum(TypedDict, total=False):
    data: Iterable[float]
    """Array to support sparse data collections."""

    notes: str
    """Notes for the datum with details of what the data is, units, etc."""


class BodyDensityProfileIri(TypedDict, total=False):
    b0: float
    """B0 parameter of the F2 layer shape."""

    b1: float
    """B1 parameter of the F2 layer shape."""

    chi: float
    """
    Peak Density Thickness (PDT) for description of the flat-nose shape, in
    kilometers.
    """

    d1: float
    """D1 parameter of the F1 layer shape."""

    description: str
    """Description of IRI implementation."""

    fp1: float
    """TBD."""

    fp2: float
    """TBD."""

    fp30: float
    """TBD."""

    fp3_u: Annotated[float, PropertyInfo(alias="fp3U")]
    """TBD."""

    ha: float
    """Starting height of the D layer, in kilometers."""

    hdx: float
    """Height of the intermediate region at the top of D region, in kilometers."""

    hm_d: Annotated[float, PropertyInfo(alias="hmD")]
    """Peak height of the D layer, in kilometers."""

    hm_e: Annotated[float, PropertyInfo(alias="hmE")]
    """Peak height of the F2 layer, in kilometers."""

    hm_f1: Annotated[float, PropertyInfo(alias="hmF1")]
    """Peak height of the F1 layer, in kilometers."""

    hm_f2: Annotated[float, PropertyInfo(alias="hmF2")]
    """Peak height of F2 layer, in kilometers."""

    h_val_top: Annotated[float, PropertyInfo(alias="hValTop")]
    """The valley height, in kilometers."""

    hz: float
    """Height HZ of the interim layer, in kilometers."""

    nm_d: Annotated[float, PropertyInfo(alias="nmD")]
    """Peak density of the D layer, in per cubic centimeter."""

    nm_e: Annotated[float, PropertyInfo(alias="nmE")]
    """Peak density of the E layer, in per cubic centimeter."""

    nm_f1: Annotated[float, PropertyInfo(alias="nmF1")]
    """Peak density of the F1 layer, in grams per cubic centimeter."""

    nm_f2: Annotated[float, PropertyInfo(alias="nmF2")]
    """Peak density of F2 layer, in grams per cubic centimeter."""

    n_val_b: Annotated[float, PropertyInfo(alias="nValB")]
    """The valley depth, in grams per cubic centimeter."""


class BodyDensityProfileParabolicParabolicItem(TypedDict, total=False):
    f: float
    """Plasma frequency at the layer peak, in MHz."""

    layer: str
    """Ionospheric plasma layer (E, F1, or F2)."""

    y: float
    """Half-thickness of the layer, in kilometers."""

    z: float
    """Height of the layer peak, in kilometers."""


class BodyDensityProfileParabolic(TypedDict, total=False):
    description: str
    """General description of the QP computation algorithm."""

    parabolic_items: Annotated[Iterable[BodyDensityProfileParabolicParabolicItem], PropertyInfo(alias="parabolicItems")]
    """Describes the E, F1, and F2 layers as parabolic-shape segments."""


class BodyDensityProfileQuasiParabolicQuasiParabolicSegment(TypedDict, total=False):
    a: float
    """Coefficient A."""

    b: float
    """Coefficient B."""

    c: float
    """Coefficient C."""

    error: float
    """Best-fit error."""

    index: int
    """The index of this segment in the list, from 1 to NumSegments."""

    rb: float
    """Starting range of the segment, in kilometers from the Earth's center."""

    re: float
    """Ending range of the segment, in kilometers from the Earth's center."""


class BodyDensityProfileQuasiParabolic(TypedDict, total=False):
    description: str
    """General description of the quasi-parabolic computation algorithm."""

    earth_radius: Annotated[float, PropertyInfo(alias="earthRadius")]
    """Value of the Earth's radius, in kilometers, used for computations."""

    quasi_parabolic_segments: Annotated[
        Iterable[BodyDensityProfileQuasiParabolicQuasiParabolicSegment], PropertyInfo(alias="quasiParabolicSegments")
    ]
    """Array of quasi-parabolic segments.

    Each segment is the best-fit 3-parameter quasi-parabolas defined via A, B, C
    coefficients, f^2=A/r^2+B/r+C”. Usually 3 groups for E, F1, and F2 layers, but
    additional segments may be used to improve accuracy.
    """


class BodyDensityProfileShiftedChebyshevShiftedChebyshev(TypedDict, total=False):
    coeffs: Iterable[float]
    """Array of coefficients."""

    error: float
    """Best fit error."""

    fstart: float
    """Start frequency of the layer, in MHz."""

    fstop: float
    """Stop frequency of the layer, in MHz."""

    layer: str
    """The ionospheric plasma layer."""

    n: int
    """Number of coefficients in the expansion."""

    peakheight: float
    """Peak height of the layer, in kilometers."""

    zhalf_nm: Annotated[float, PropertyInfo(alias="zhalfNm")]
    """Height at which density is half of the peak Nm, in kilometers."""


class BodyDensityProfileShiftedChebyshev(TypedDict, total=False):
    description: str
    """Description of the computation technique."""

    shifted_chebyshevs: Annotated[
        Iterable[BodyDensityProfileShiftedChebyshevShiftedChebyshev], PropertyInfo(alias="shiftedChebyshevs")
    ]
    """
    Up to 3 groups of coefficients, using “shiftedChebyshev” sub-field, to describe
    E, F1, and bottomside F2 profile shapes, or up to 6 groups of coefficients to
    describe height uncertainty boundaries (upper and lower).
    """


class BodyDensityProfileTopsideExtensionChapmanConst(TypedDict, total=False):
    chi: float
    """
    Peak Density Thickness (PDT) for description of the flat-nose shape, in
    kilometers.
    """

    description: str
    """Description of the Chapman computation technique."""

    hm_f2: Annotated[float, PropertyInfo(alias="hmF2")]
    """Peak height of F2 layer, in kilometers."""

    nm_f2: Annotated[float, PropertyInfo(alias="nmF2")]
    """Peak density of F2 layer, in grams per cubic centimeter."""

    scale_f2: Annotated[float, PropertyInfo(alias="scaleF2")]
    """Scale height if F2 layer at the peak, in kilometers."""


class BodyDensityProfileTopsideExtensionVaryChap(TypedDict, total=False):
    alpha: float
    """Alpha parameter of the profile shape."""

    beta: float
    """Beta parameter of the profile shape."""

    chi: float
    """
    Peak Density Thickness (PDT) for description of the flat-nose shape, in
    kilometers.
    """

    description: str
    """Description of the Chapman computation technique."""

    hm_f2: Annotated[float, PropertyInfo(alias="hmF2")]
    """Peak height of F2 layer, in kilometers."""

    ht: float
    """Transition height, in kilometers."""

    nm_f2: Annotated[float, PropertyInfo(alias="nmF2")]
    """Peak density of F2 layer, in grams per cubic centimeter."""

    scale_f2: Annotated[float, PropertyInfo(alias="scaleF2")]
    """Scale height if F2 layer at the peak, in kilometers."""


class BodyDensityProfile(TypedDict, total=False):
    iri: BodyDensityProfileIri
    """Full set of the IRI formalism coefficients."""

    parabolic: BodyDensityProfileParabolic
    """Coefficients to describe the E, F1, and F2 layers as parabolic-shape segments."""

    quasi_parabolic: Annotated[BodyDensityProfileQuasiParabolic, PropertyInfo(alias="quasiParabolic")]
    """Coefficients to describe profile shape as quasi-parabolic segments."""

    shifted_chebyshev: Annotated[BodyDensityProfileShiftedChebyshev, PropertyInfo(alias="shiftedChebyshev")]
    """
    Coefficients to describe either the E, F1, and bottomside F2 profile shapes or
    the height uncertainty boundaries.
    """

    topside_extension_chapman_const: Annotated[
        BodyDensityProfileTopsideExtensionChapmanConst, PropertyInfo(alias="topsideExtensionChapmanConst")
    ]
    """Parameters of the constant-scale-height Chapman layer."""

    topside_extension_vary_chap: Annotated[
        BodyDensityProfileTopsideExtensionVaryChap, PropertyInfo(alias="topsideExtensionVaryChap")
    ]
    """Varying scale height Chapman topside layer."""

    valley_model_coeffs: Annotated[Iterable[float], PropertyInfo(alias="valleyModelCoeffs")]
    """Array of valley model coefficients."""

    valley_model_description: Annotated[str, PropertyInfo(alias="valleyModelDescription")]
    """Description of the valley model and parameters."""


class BodyDoppler(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of received doppler shifts in Hz."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the doppler array dimensions."""

    notes: str
    """Notes for the doppler data."""


class BodyElevation(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of incoming elevation at the receiver."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the elevation array dimensions."""

    notes: str
    """Notes for the elevation data."""


class BodyFrequency(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of frequency data."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for frequency dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the frequency array dimensions."""

    notes: str
    """Notes for the frequency data."""


class BodyPhase(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of phase data."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for phase dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the phase array dimensions."""

    notes: str
    """Notes for the phase data.

    Orientation and position for each antenna element across the antenna_element
    dimension.
    """


class BodyPolarization(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[List[Literal["X", "O"]]]]]]]]
    """Array of polarization data."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers for polarization dimensions."""

    notes: str
    """Notes for the polarization data."""


class BodyPower(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of received power in db."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the power array dimensions."""

    notes: str
    """Notes for the power data."""


class BodyRange(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of range data."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for range dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the range array dimensions."""

    notes: str
    """Notes for the range data."""


class BodyScalerInfo(TypedDict, total=False):
    confidence_level: Annotated[int, PropertyInfo(alias="confidenceLevel")]
    """Scaler confidence level."""

    confidence_score: Annotated[int, PropertyInfo(alias="confidenceScore")]
    """Scaler confidence score."""

    name: str
    """Scaler name."""

    organization: str
    """Scaler organization."""

    type: str
    """Scaler type (MANUAL, AUTOMATIC or UNKNOWN)."""

    version: float
    """Scaler version."""


class BodyStokes(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """Array of received stokes data."""

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the stoke array dimensions."""

    notes: str
    """Notes for the stokes data."""

    s: Iterable[float]
    """S1, S2, and S3 (the normalized Stokes parameters 1, 2, and 3)."""


class BodyTime(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[Iterable[float]]]]]]]
    """
    Array of times in number of seconds passed since January 1st, 1970 with the same
    dimensions as power.
    """

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of names for dimensions."""

    dimensions: Iterable[int]
    """Array of integers of the time array dimensions."""

    notes: str
    """The notes indicate the scheme and accuracy."""


class BodyTraceGeneric(TypedDict, total=False):
    data: Iterable[Iterable[Iterable[float]]]
    """Multi-dimensional Array.

    The 1st dimension spans points along the trace while the 2nd dimension spans
    frequency-range pairs.
    """

    dimension_name: Annotated[List[str], PropertyInfo(alias="dimensionName")]
    """Array of dimension names for trace generic data."""

    notes: str
    """Notes for the trace generic data."""


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

    source: Required[str]
    """Source of the data."""

    start_time_utc: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTimeUTC", format="iso8601")]]
    """Sounding Start time in ISO8601 UTC format."""

    station_id: Required[Annotated[str, PropertyInfo(alias="stationId")]]
    """URSI code for station or stations producing the ionosonde."""

    system: Required[str]
    """
    Ionosonde hardware type or data collection type together with possible
    additional descriptors.
    """

    system_info: Required[Annotated[str, PropertyInfo(alias="systemInfo")]]
    """Names of settings."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    amplitude: BodyAmplitude

    antenna_element_position: Annotated[BodyAntennaElementPosition, PropertyInfo(alias="antennaElementPosition")]

    antenna_element_position_coordinate_system: Annotated[
        Literal[
            "J2000", "ECR/ECEF", "TEME", "GCRF", "WGS84 (GEODetic lat, long, alt)", "GEOCentric (lat, long, radii)"
        ],
        PropertyInfo(alias="antennaElementPositionCoordinateSystem"),
    ]
    """
    Enums: J2000, ECR/ECEF, TEME, GCRF, WGS84 (GEODetic lat, long, alt), GEOCentric
    (lat, long, radii).
    """

    artist_flags: Annotated[Iterable[int], PropertyInfo(alias="artistFlags")]
    """Array of Legacy Artist Flags."""

    azimuth: BodyAzimuth

    b0: float
    """IRI thickness parameter in km. URSI ID: D0."""

    b1: float
    """IRI profile shape parameter. URSI ID: D1."""

    char_atts: Annotated[Iterable[BodyCharAtt], PropertyInfo(alias="charAtts")]
    """List of attributes that are associated with the specified characteristics.

    Characteristics are defined by the CHARS: URSI IIWG format for archiving monthly
    ionospheric characteristics, INAG Bulletin No. 62 specification. Qualifying and
    Descriptive letters are defined by the URSI Handbook for Ionogram Interpretation
    and reduction, Report UAG, No. 23A specification.
    """

    d: float
    """Distance for MUF calculation in km."""

    d1: float
    """IRI profile shape parameter, F1 layer. URSI ID: D2."""

    datum: BodyDatum

    deltafo_f2: Annotated[float, PropertyInfo(alias="deltafoF2")]
    """Adjustment to the scaled foF2 during profile inversion in MHz."""

    density_profile: Annotated[BodyDensityProfile, PropertyInfo(alias="densityProfile")]
    """
    Profile of electron densities in the ionosphere associated with an
    IonoObservation.
    """

    doppler: BodyDoppler

    down_e: Annotated[float, PropertyInfo(alias="downE")]
    """Lowering of E trace to the leading edge in km."""

    down_es: Annotated[float, PropertyInfo(alias="downEs")]
    """Lowering of Es trace to the leading edge in km."""

    down_f: Annotated[float, PropertyInfo(alias="downF")]
    """Lowering of F trace to the leading edge in km."""

    electron_density: Annotated[Iterable[float], PropertyInfo(alias="electronDensity")]
    """
    Array of electron densities in cm^-3 (must match the size of the height and
    plasmaFrequency arrays).
    """

    electron_density_uncertainty: Annotated[Iterable[float], PropertyInfo(alias="electronDensityUncertainty")]
    """
    Uncertainty in specifying the electron density at each height point of the
    profile (must match the size of the electronDensity array).
    """

    elevation: BodyElevation

    fb_es: Annotated[float, PropertyInfo(alias="fbEs")]
    """The blanketing frequency of layer used to derive foEs in MHz. URSI ID: 32."""

    fe: float
    """Frequency spread beyond foE in MHz. URSI ID: 87."""

    ff: float
    """Frequency spread between fxF2 and FxI in MHz. URSI ID: 86."""

    fhprime_f: Annotated[float, PropertyInfo(alias="fhprimeF")]
    """The frequency at which hprimeF is measured in MHz. URSI ID: 61."""

    fhprime_f2: Annotated[float, PropertyInfo(alias="fhprimeF2")]
    """The frequency at which hprimeF2 is measured in MHz. URSI ID: 60."""

    fmin: float
    """Lowest frequency at which echo traces are observed on the ionogram, in MHz.

    URSI ID: 42.
    """

    fmin_e: Annotated[float, PropertyInfo(alias="fminE")]
    """Minimum frequency of E layer echoes in MHz. URSI ID: 81."""

    fmin_es: Annotated[float, PropertyInfo(alias="fminEs")]
    """Minimum frequency of Es layer in MHz."""

    fmin_f: Annotated[float, PropertyInfo(alias="fminF")]
    """Minimum frequency of F layer echoes in MHz. URSI ID: 80."""

    fmuf: float
    """MUF/OblFactor in MHz."""

    fo_e: Annotated[float, PropertyInfo(alias="foE")]
    """
    The ordinary wave critical frequency of the lowest thick layer which causes a
    discontinuity, in MHz. URSI ID: 20.
    """

    fo_ea: Annotated[float, PropertyInfo(alias="foEa")]
    """Critical frequency of night time auroral E layer in MHz. URSI ID: 23."""

    fo_ep: Annotated[float, PropertyInfo(alias="foEp")]
    """Predicted value of foE in MHz."""

    fo_es: Annotated[float, PropertyInfo(alias="foEs")]
    """
    Highest ordinary wave frequency at which a mainly continuous Es trace is
    observed, in MHz. URSI ID: 30.
    """

    fo_f1: Annotated[float, PropertyInfo(alias="foF1")]
    """The ordinary wave F1 critical frequency, in MHz. URSI ID: 10."""

    fo_f1p: Annotated[float, PropertyInfo(alias="foF1p")]
    """Predicted value of foF1 in MHz."""

    fo_f2: Annotated[float, PropertyInfo(alias="foF2")]
    """
    The ordinary wave critical frequency of the highest stratification in the F
    region, specified in MHz. URSI ID: 00.
    """

    fo_f2p: Annotated[float, PropertyInfo(alias="foF2p")]
    """Predicted value of foF2 in MHz."""

    fo_p: Annotated[float, PropertyInfo(alias="foP")]
    """Highest ordinary wave critical frequency of F region patch trace in MHz.

    URSI ID: 55.
    """

    frequency: BodyFrequency

    fx_e: Annotated[float, PropertyInfo(alias="fxE")]
    """The extraordinary wave E critical frequency, in MHz. URSI ID: 21."""

    fx_f1: Annotated[float, PropertyInfo(alias="fxF1")]
    """The extraordinary wave F1 critical frequency, in MHz. URSI ID: 11."""

    fx_f2: Annotated[float, PropertyInfo(alias="fxF2")]
    """The extraordinary wave F2 critical frequency, in MHz. URSI ID: 01."""

    fx_i: Annotated[float, PropertyInfo(alias="fxI")]
    """The highest frequency of F-trace in MHz.

    Note: fxI is with capital i. URSI ID: 51.
    """

    height: Iterable[float]
    """
    Array of altitudes above station level for plasma frequency/density arrays in km
    (must match the size of the plasmaFrequency and electronDensity Arrays).
    """

    hm_e: Annotated[float, PropertyInfo(alias="hmE")]
    """True height of the E peak in km. URSI ID: CE."""

    hm_f1: Annotated[float, PropertyInfo(alias="hmF1")]
    """True height of the F1 peak in km. URSI ID: BE."""

    hm_f2: Annotated[float, PropertyInfo(alias="hmF2")]
    """True height of the F2 peak in km. URSI ID: AE."""

    hprime_e: Annotated[float, PropertyInfo(alias="hprimeE")]
    """The minimum virtual height of the normal E layer trace in km. URSI ID: 24."""

    hprime_ea: Annotated[float, PropertyInfo(alias="hprimeEa")]
    """Minimum virtual height of night time auroral E layer trace in km. URSI ID: 27."""

    hprime_es: Annotated[float, PropertyInfo(alias="hprimeEs")]
    """The minimum height of the trace used to give foEs in km. URSI ID: 34."""

    hprime_f: Annotated[float, PropertyInfo(alias="hprimeF")]
    """The minimum virtual height of the ordinary wave trace taken as a whole, in km.

    URSI ID: 16.
    """

    hprime_f1: Annotated[float, PropertyInfo(alias="hprimeF1")]
    """
    The minimum virtual height of reflection at a point where the trace is
    horizontal in the F region in km. URSI ID: 14.
    """

    hprime_f2: Annotated[float, PropertyInfo(alias="hprimeF2")]
    """
    The minimum virtual height of ordinary wave trace for the highest stable
    stratification in the F region in km. URSI ID: 4.
    """

    hprimef_muf: Annotated[float, PropertyInfo(alias="hprimefMUF")]
    """Virtual height at MUF/OblFactor frequency in MHz."""

    hprime_p: Annotated[float, PropertyInfo(alias="hprimeP")]
    """Minimum virtual height of the trace used to determine foP in km. URSI ID: 56."""

    id_sensor: Annotated[str, PropertyInfo(alias="idSensor")]
    """Unique identifier of the reporting sensor."""

    luf: float
    """Lowest usable frequency."""

    md: float
    """MUF(D)/foF2."""

    mufd: float
    """Maximum Usable Frequency for ground distance D in MHz."""

    ne_profile_name: Annotated[str, PropertyInfo(alias="neProfileName")]
    """Name of the algorithm used for the electron density profile."""

    ne_profile_version: Annotated[float, PropertyInfo(alias="neProfileVersion")]
    """Version of the algorithm used for the electron density profile."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_sensor_id: Annotated[str, PropertyInfo(alias="origSensorId")]
    """
    Optional identifier provided by observation source to indicate the sensor
    identifier which produced this observation. This may be an internal identifier
    and not necessarily a valid sensor ID.
    """

    phase: BodyPhase

    plasma_frequency: Annotated[Iterable[float], PropertyInfo(alias="plasmaFrequency")]
    """
    Array of plasma frequencies in MHz (must match the size of the height and
    electronDensity arrays).
    """

    plasma_frequency_uncertainty: Annotated[Iterable[float], PropertyInfo(alias="plasmaFrequencyUncertainty")]
    """
    Uncertainty in specifying the electron plasma frequency at each height point of
    the profile (must match the size of the plasmaFrequency array).
    """

    platform_name: Annotated[str, PropertyInfo(alias="platformName")]
    """Equipment location."""

    polarization: BodyPolarization

    power: BodyPower

    qe: float
    """Average range spread of E layer in km. URSI ID: 85."""

    qf: float
    """Average range spread of F layer in km. URSI ID: 84."""

    range: BodyRange

    receive_coordinates: Annotated[Iterable[Iterable[float]], PropertyInfo(alias="receiveCoordinates")]
    """
    List of Geodetic Latitude, Longitude, and Altitude coordinates in km of the
    receiver. Coordinates List must always have 3 elements. Valid ranges are -90.0
    to 90.0 for Latitude and -180.0 to 180.0 for Longitude. Altitude is in km and
    its value must be 0 or greater.
    """

    receive_sensor_type: Annotated[Literal["Mobile", "Static"], PropertyInfo(alias="receiveSensorType")]
    """Enums: Mobile, Static."""

    restricted_frequency: Annotated[Iterable[float], PropertyInfo(alias="restrictedFrequency")]
    """Array of restricted frequencies."""

    restricted_frequency_notes: Annotated[str, PropertyInfo(alias="restrictedFrequencyNotes")]
    """Notes for the restrictedFrequency data."""

    scale_height_f2_peak: Annotated[float, PropertyInfo(alias="scaleHeightF2Peak")]
    """Effective scale height at hmF2 Titheridge method in km. URSI ID: 69."""

    scaler_info: Annotated[BodyScalerInfo, PropertyInfo(alias="scalerInfo")]
    """
    The ScalerInfo record describes the person or system who interpreted the
    ionogram in IonoObservation.
    """

    stokes: BodyStokes

    system_notes: Annotated[str, PropertyInfo(alias="systemNotes")]
    """Details concerning the composition/intention/interpretation/audience/etc.

    of any data recorded here. This field may contain all of the intended
    information e.g. info on signal waveforms used, antenna setup, etc. OR may
    describe the data/settings to be provided in the “data” field.
    """

    tec: float
    """Total Ionospheric Electron Content \\**10^16e/m^2.

    1 TEC Unit (TECU) = 10^16 electrons/m^2. URSI ID: 72.
    """

    tid_azimuth: Annotated[Iterable[float], PropertyInfo(alias="tidAzimuth")]
    """Array of degrees clockwise from true North of the TID."""

    tid_periods: Annotated[Iterable[float], PropertyInfo(alias="tidPeriods")]
    """Array of 1/frequency of the TID wave."""

    tid_phase_speeds: Annotated[Iterable[float], PropertyInfo(alias="tidPhaseSpeeds")]
    """Array of speed in m/s at which the disturbance travels through the ionosphere."""

    time: BodyTime

    trace_generic: Annotated[BodyTraceGeneric, PropertyInfo(alias="traceGeneric")]

    transmit_coordinates: Annotated[Iterable[Iterable[float]], PropertyInfo(alias="transmitCoordinates")]
    """
    List of Geodetic Latitude, Longitude, and Altitude coordinates in km of the
    receiver. Coordinates List must always have 3 elements. Valid ranges are -90.0
    to 90.0 for Latitude and -180.0 to 180.0 for Longitude. Altitude is in km and
    its value must be 0 or greater.
    """

    transmit_sensor_type: Annotated[Literal["Mobile", "Static"], PropertyInfo(alias="transmitSensorType")]
    """Enums: Mobile, Static."""

    type_es: Annotated[str, PropertyInfo(alias="typeEs")]
    """Characterization of the shape of Es trace. URSI ID: 36."""

    y_e: Annotated[float, PropertyInfo(alias="yE")]
    """Parabolic E layer semi-thickness in km. URSI ID: 83."""

    y_f1: Annotated[float, PropertyInfo(alias="yF1")]
    """Parabolic F1 layer semi-thickness in km. URSI ID: 95."""

    y_f2: Annotated[float, PropertyInfo(alias="yF2")]
    """Parabolic F2 layer semi-thickness in km. URSI ID: 94."""

    zhalf_nm: Annotated[float, PropertyInfo(alias="zhalfNm")]
    """True height at half peak electron density in the F2 layer in km. URSI ID: 93."""

    zm_e: Annotated[float, PropertyInfo(alias="zmE")]
    """Peak height of E-layer in km. URSI ID: 90."""
