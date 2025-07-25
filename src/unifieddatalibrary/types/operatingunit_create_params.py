# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OperatingunitCreateParams"]


class OperatingunitCreateParams(TypedDict, total=False):
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

    name: Required[str]
    """Name of the operating unit."""

    source: Required[str]
    """Source of the data."""

    air_def_area: Annotated[str, PropertyInfo(alias="airDefArea")]
    """
    Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
    coordinates reside.
    """

    allegiance: str
    """
    The DoD Standard country code designator for the country or political entity to
    which the operating unit owes its allegiance. This field will be set to "OTHR"
    if the source value does not match a UDL country code value (ISO-3166-ALPHA-2).
    """

    alt_allegiance: Annotated[str, PropertyInfo(alias="altAllegiance")]
    """
    Specifies an alternate allegiance code if the data provider code is not part of
    an official Country Code standard such as ISO-3166 or FIPS. This field will be
    set to the value provided by the source and should be used for all Queries
    specifying allegiance.
    """

    alt_country_code: Annotated[str, PropertyInfo(alias="altCountryCode")]
    """
    Specifies an alternate country code if the data provider code is not part of an
    official Country Code standard such as ISO-3166 or FIPS. This field will be set
    to the value provided by the source and should be used for all Queries
    specifying a Country Code.
    """

    alt_operating_unit_id: Annotated[str, PropertyInfo(alias="altOperatingUnitId")]
    """Unique identifier of the operating unit record from the originating system."""

    class_rating: Annotated[str, PropertyInfo(alias="classRating")]
    """Indicates the importance of the operating unit to the OES or MIR system.

    This data element is restricted to update by DIA (DB-4). Valid values are: 0 -
    Does not meet criteria above 1 - Primary importance to system 2 - Secondary
    importance to system 3 - Tertiary importance to system O - Other. Explain in
    Remarks.
    """

    condition: str
    """The physical manner of being or state of existence of the operating unit.

    A physical condition that must be considered in the determining of a course of
    action. The specific usage and enumerations contained in this field may be found
    in the documentation provided in the referenceDoc field. If referenceDoc not
    provided, users may consult the data provider.
    """

    condition_avail: Annotated[str, PropertyInfo(alias="conditionAvail")]
    """Availability of the operating unit relative to its condition.

    Indicates the reason the operating unit is not fully operational. The specific
    usage and enumerations contained in this field may be found in the documentation
    provided in the referenceDoc field. If referenceDoc not provided, users may
    consult the data provider.
    """

    coord: str
    """
    Indicates any of the magnitudes that serve to define the position of a point by
    reference to a fixed figure, system of lines, etc.

    Pos. 1-2. Latitude Degrees [00-90]

    Pos. 3-4. Latitude Minutes [00-59]

    Pos. 5-6. Latitude Seconds [00-59]

    Pos. 7-9. Latitude Thousandths Of Seconds [000-999]

    Pos. 10. Latitude Hemisphere [NS]

    Pos. 11-13. Longitude Degrees [00-180]

    Pos. 14-15. Longitude Minutes [00-59]

    Pos. 16-17. Longitude Seconds [00-59]

    Pos. 18-20. Longitude Thousandths Of Seconds [000-999]

    Pos. 21. Longitude Hemisphere [EW]

    Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U]
    """

    coord_datum: Annotated[str, PropertyInfo(alias="coordDatum")]
    """A mathematical model of the earth used to calculate coordinates on a map.

    US Forces use the World Geodetic System 1984 (WGS 84), but also use maps by
    allied countries with local datums. The datum must be specified to ensure
    accuracy of coordinates. The specific usage and enumerations contained in this
    field may be found in the documentation provided in the referenceDoc field. If
    referenceDoc not provided, users may consult the data provider.
    """

    coord_deriv_acc: Annotated[float, PropertyInfo(alias="coordDerivAcc")]
    """
    Indicates the plus or minus error assessed against the method used to derive the
    coordinate.
    """

    country_code: Annotated[str, PropertyInfo(alias="countryCode")]
    """
    The DoD Standard country code designator for the country or political entity to
    which the operating unit geographic coordinates reside . This field will be set
    to "OTHR" if the source value does not match a UDL country code value
    (ISO-3166-ALPHA-2).
    """

    deploy_status: Annotated[str, PropertyInfo(alias="deployStatus")]
    """A code describing the amount of operating unit participation in a deployment.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    description: str
    """Description of the operating unit."""

    div_cat: Annotated[str, PropertyInfo(alias="divCat")]
    """Combat status of a divisional or equivalent operating unit.

    Currently, this data element applies only to operating units of the Former
    Soviet Union. The specific usage and enumerations contained in this field may be
    found in the documentation provided in the referenceDoc field. If referenceDoc
    not provided, users may consult the data provider.
    """

    echelon: str
    """Organizational level of the operating unit.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    echelon_tier: Annotated[str, PropertyInfo(alias="echelonTier")]
    """Indicates the major group or level to which an echelon belongs.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    elev_msl: Annotated[float, PropertyInfo(alias="elevMsl")]
    """
    Ground elevation of the geographic coordinates referenced to (above or below)
    Mean Sea Level (MSL) vertical datum.
    """

    elev_msl_conf_lvl: Annotated[int, PropertyInfo(alias="elevMslConfLvl")]
    """
    Indicates the confidence level expressed as a percent that a specific geometric
    spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
    to within a specified vertical accuracy.
    """

    elev_msl_deriv_acc: Annotated[float, PropertyInfo(alias="elevMslDerivAcc")]
    """
    Indicates the plus or minus error assessed against the method used to derive the
    elevation.
    """

    eval: int
    """
    The Intelligence Confidence Level or the Reliability/degree of confidence that
    the analyst has assigned to the data within this record. The numerical range is
    from 1 to 9 with 1 representing the highest confidence level.
    """

    flag_flown: Annotated[str, PropertyInfo(alias="flagFlown")]
    """The country code of the observed flag flown."""

    fleet_id: Annotated[str, PropertyInfo(alias="fleetId")]
    """Naval fleet to which an operating unit is assigned.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    force: str
    """
    An aggregation of military units within a single service (i.e., ARMY, AIR FORCE,
    etc.) which operates under a single authority to accomplish a common mission.
    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    force_name: Annotated[str, PropertyInfo(alias="forceName")]
    """The specific name for a given force.

    For example, Force = ADF (Air Defense Force) and Force Name = Army Air Defense
    Force.
    """

    fpa: str
    """Functional Production Area (FPA) under the Shared Production Program (SPP).

    Producers are defined per country per FPA. The specific usage and enumerations
    contained in this field may be found in the documentation provided in the
    referenceDoc field. If referenceDoc not provided, users may consult the data
    provider.
    """

    funct_role: Annotated[str, PropertyInfo(alias="functRole")]
    """
    Principal combat-related role that an operating unit is organized, structured
    and equipped to perform. Or, the specialized military or paramilitary branch in
    which an individual serves, their specialization. The specific usage and
    enumerations contained in this field may be found in the documentation provided
    in the referenceDoc field. If referenceDoc not provided, users may consult the
    data provider.
    """

    geoidal_msl_sep: Annotated[float, PropertyInfo(alias="geoidalMslSep")]
    """The distance between Mean Sea Level and a referenced ellipsoid."""

    id_contact: Annotated[str, PropertyInfo(alias="idContact")]
    """Unique identifier of the contact for this operating unit."""

    ident: str
    """
    Estimated identity of the Site (ASSUMED FRIEND, FRIEND, HOSTILE, FAKER, JOKER,
    NEUTRAL, PENDING, SUSPECT, UNKNOWN):

    ASSUMED FRIEND: Track assumed to be a friend due to the object characteristics,
    behavior, and/or origin.

    FRIEND: Track object supporting friendly forces and belonging to a declared
    friendly nation or entity.

    HOSTILE: Track object belonging to an opposing nation, party, group, or entity
    deemed to contribute to a threat to friendly forces or their mission due to its
    behavior, characteristics, nationality, or origin.

    FAKER: Friendly track, object, or entity acting as an exercise hostile.

    JOKER: Friendly track, object, or entity acting as an exercise suspect.

    NEUTRAL: Track object whose characteristics, behavior, nationality, and/or
    origin indicate that it is neither supporting nor opposing friendly forces or
    their mission.

    PENDING: Track object which has not been evaluated.

    SUSPECT: Track object deemed potentially hostile due to the object
    characteristics, behavior, nationality, and/or origin.

    UNKNOWN: Track object which has been evaluated and does not meet criteria for
    any standard identity.
    """

    id_location: Annotated[str, PropertyInfo(alias="idLocation")]
    """Unique identifier of the location record for this operating unit."""

    id_operating_unit: Annotated[str, PropertyInfo(alias="idOperatingUnit")]
    """Unique identifier of the record, auto-generated by the system."""

    id_organization: Annotated[str, PropertyInfo(alias="idOrganization")]
    """Unique identifier of the organization record for this operating unit."""

    lat: float
    """WGS84 latitude of the location, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    loc_name: Annotated[str, PropertyInfo(alias="locName")]
    """Location name for the coordinates."""

    loc_reason: Annotated[str, PropertyInfo(alias="locReason")]
    """Indicates the reason that the operating unit is at that location.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    lon: float
    """WGS84 longitude of the location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    master_unit: Annotated[bool, PropertyInfo(alias="masterUnit")]
    """
    This field contains a value indicating whether the record is a master unit
    record (True) or a detail record (False). Master records contain basic
    information that does not change over time for each unit that has been selected
    to be projected.
    """

    mil_grid: Annotated[str, PropertyInfo(alias="milGrid")]
    """
    The Military Grid Reference System is the geocoordinate standard used by NATO
    militaries for locating points on Earth. The MGRS is derived from the Universal
    Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
    (UPS) grid system, but uses a different labeling convention. The MGRS is used as
    geocode for the entire Earth. Example of an milgrid coordinate, or grid
    reference, would be 4QFJ12345678, which consists of three parts: 4Q (grid zone
    designator, GZD) FJ (the 100,000-meter square identifier) 12345678 (numerical
    location; easting is 1234 and northing is 5678, in this case specifying a
    location with 10 m resolution).
    """

    mil_grid_sys: Annotated[str, PropertyInfo(alias="milGridSys")]
    """Indicates the grid system used in the development of the milGrid coordinates.

    Values are:

    UPS - Universal Polar System

    UTM - Universal Transverse Mercator
    """

    msn_primary: Annotated[str, PropertyInfo(alias="msnPrimary")]
    """
    Indicates the principal type of mission that an operating unit is organized and
    equipped to perform. The specific usage and enumerations contained in this field
    may be found in the documentation provided in the referenceDoc field. If
    referenceDoc not provided, users may consult the data provider.
    """

    msn_primary_specialty: Annotated[str, PropertyInfo(alias="msnPrimarySpecialty")]
    """
    Indicates the principal specialty type of mission that an operating unit is
    organized and equipped to perform. The specific usage and enumerations contained
    in this field may be found in the documentation provided in the referenceDoc
    field. If referenceDoc not provided, users may consult the data provider.
    """

    oper_status: Annotated[str, PropertyInfo(alias="operStatus")]
    """
    The Degree to which an operating unit is ready to perform the overall
    operational mission(s) for which it was organized and equipped. The specific
    usage and enumerations contained in this field may be found in the documentation
    provided in the referenceDoc field. If referenceDoc not provided, users may
    consult the data provider.
    """

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    pol_subdiv: Annotated[str, PropertyInfo(alias="polSubdiv")]
    """Political subdivision in which the geographic coordinates reside.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    rec_status: Annotated[str, PropertyInfo(alias="recStatus")]
    """
    Validity and currency of the data in the record to be used in conjunction with
    the other elements in the record as defined by SOPs. Values are: A - Active I -
    Inactive K - Acknowledged L - Local Q - A nominated (NOM) or Data Change Request
    (DCR) record R - Production reduced by CMD decision W - Working Record.
    """

    reference_doc: Annotated[str, PropertyInfo(alias="referenceDoc")]
    """
    The reference documentiation that specifies the usage and enumerations contained
    in this record. If referenceDoc not provided, users may consult the data
    provider.
    """

    res_prod: Annotated[str, PropertyInfo(alias="resProd")]
    """
    Responsible Producer - Organization that is responsible for the maintenance of
    the record.
    """

    review_date: Annotated[Union[str, date], PropertyInfo(alias="reviewDate", format="iso8601")]
    """
    Date on which the data in the record was last reviewed by the responsible
    analyst for accuracy and currency. This date cannot be greater than the current
    date.
    """

    stylized_unit: Annotated[bool, PropertyInfo(alias="stylizedUnit")]
    """
    This field contains a value indicating whether the record is a stylized
    operating unit record (True) or a regular operating unit record (False). A
    stylized operating unit is a type of operating unit with one set of equipment
    that can be assigned to one or more superiors. A stylized operating unit is
    generally useful for lower echelon operating units where the number of operating
    units and types of equipment are equal for multiple organizations. In lieu of
    creating unique operating unit records for each operating unit, a template is
    created for the operating unit and its equipment. This template enables the user
    to assign the operating unit to multiple organizations.
    """

    sym_code: Annotated[str, PropertyInfo(alias="symCode")]
    """
    A standard scheme for symbol coding enabling the transfer, display and use of
    symbols and graphics among information systems, as per MIL-STD 2525B, and
    supported by the element AFFILIATION.
    """

    unit_identifier: Annotated[str, PropertyInfo(alias="unitIdentifier")]
    """
    An optional identifier for this operating unit that may be composed from items
    such as the originating organization, allegiance, one-up number, etc.
    """

    utm: str
    """Universal Transverse Mercator (UTM) grid coordinates. Pos.

    1-2, UTM Zone Column [01-60 Pos. 3, UTM Zone Row [C-HJ-NP-X] Pos. 4, UTM False
    Easting [0-9] Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9] Pos. 10-11,
    UTM False Northing [0-9][0-9] Pos. 12-16, UTM Meter Northing
    [0-9][0-9][0-9][0-9][0-9].
    """

    wac: str
    """
    World Aeronautical Chart identifier for the area in which a designated operating
    unit is located.
    """
