# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .entity_full import EntityFull

__all__ = [
    "SiteTupleResponse",
    "SiteTupleResponseItem",
    "SiteTupleResponseItemSiteOperation",
    "SiteTupleResponseItemSiteOperationDailyOperation",
    "SiteTupleResponseItemSiteOperationDailyOperationOperatingHour",
    "SiteTupleResponseItemSiteOperationMaximumOnGround",
    "SiteTupleResponseItemSiteOperationOperationalDeviation",
    "SiteTupleResponseItemSiteOperationOperationalPlanning",
    "SiteTupleResponseItemSiteOperationPathway",
    "SiteTupleResponseItemSiteOperationWaiver",
    "SiteTupleResponseItemSiteRemark",
]


class SiteTupleResponseItemSiteOperationDailyOperationOperatingHour(BaseModel):
    op_start_time: Optional[str] = FieldInfo(alias="opStartTime", default=None)
    """The Zulu (UTC) operational start time, expressed in ISO 8601 format as HH:MM."""

    op_stop_time: Optional[str] = FieldInfo(alias="opStopTime", default=None)
    """The Zulu (UTC) operational stop time, expressed in ISO 8601 format as HH:MM."""


class SiteTupleResponseItemSiteOperationDailyOperation(BaseModel):
    day_of_week: Optional[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]] = (
        FieldInfo(alias="dayOfWeek", default=None)
    )
    """The day of the week to which this operational information pertains."""

    operating_hours: Optional[List[SiteTupleResponseItemSiteOperationDailyOperationOperatingHour]] = FieldInfo(
        alias="operatingHours", default=None
    )
    """
    A collection containing the operational start and stop times scheduled for the
    day of the week specified.
    """

    operation_name: Optional[str] = FieldInfo(alias="operationName", default=None)
    """The name or type of operation to which this information pertains."""

    ophrs_last_changed_by: Optional[str] = FieldInfo(alias="ophrsLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this DailyOperation
    data.
    """

    ophrs_last_changed_date: Optional[datetime] = FieldInfo(alias="ophrsLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this DailyOperation data, in ISO
    8601 UTC format with millisecond precision.
    """


class SiteTupleResponseItemSiteOperationMaximumOnGround(BaseModel):
    aircraft_mds: Optional[str] = FieldInfo(alias="aircraftMDS", default=None)
    """
    The Model Design Series (MDS) designation of the aircraft to which this maximum
    on ground (MOG) data pertains.
    """

    contingency_mog: Optional[int] = FieldInfo(alias="contingencyMOG", default=None)
    """
    Maximum on ground (MOG) number of contingent aircraft based on spacing and
    manpower, for the aircraft type specified.
    """

    mog_last_changed_by: Optional[str] = FieldInfo(alias="mogLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this maximum on ground
    data.
    """

    mog_last_changed_date: Optional[datetime] = FieldInfo(alias="mogLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this maximum on ground data, in
    ISO 8601 UTC format with millisecond precision.
    """

    wide_parking_mog: Optional[int] = FieldInfo(alias="wideParkingMOG", default=None)
    """
    Maximum on ground (MOG) number of parking wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """

    wide_working_mog: Optional[int] = FieldInfo(alias="wideWorkingMOG", default=None)
    """
    Maximum on ground (MOG) number of working wide-body aircraft based on spacing
    and manpower, for the aircraft type specified.
    """


class SiteTupleResponseItemSiteOperationOperationalDeviation(BaseModel):
    affected_aircraft_mds: Optional[str] = FieldInfo(alias="affectedAircraftMDS", default=None)
    """
    The Model Design Series (MDS) designation of the aircraft affected by this
    operational deviation.
    """

    affected_mog: Optional[int] = FieldInfo(alias="affectedMOG", default=None)
    """
    The maximum on ground (MOG) number for aircraft affected by this operational
    deviation.
    """

    aircraft_on_ground_time: Optional[str] = FieldInfo(alias="aircraftOnGroundTime", default=None)
    """On ground time for aircraft affected by this operational deviation."""

    crew_rest_time: Optional[str] = FieldInfo(alias="crewRestTime", default=None)
    """Rest time for crew affected by this operational deviation."""

    od_last_changed_by: Optional[str] = FieldInfo(alias="odLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to this
    OperationalDeviation data.
    """

    od_last_changed_date: Optional[datetime] = FieldInfo(alias="odLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this OperationalDeviation data,
    in ISO 8601 UTC format with millisecond precision.
    """

    od_remark: Optional[str] = FieldInfo(alias="odRemark", default=None)
    """Text remark regarding this operational deviation."""


class SiteTupleResponseItemSiteOperationOperationalPlanning(BaseModel):
    op_end_date: Optional[datetime] = FieldInfo(alias="opEndDate", default=None)
    """
    The end date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_last_changed_by: Optional[str] = FieldInfo(alias="opLastChangedBy", default=None)
    """
    The name of the person who made the most recent change made to this
    OperationalPlanning data.
    """

    op_last_changed_date: Optional[datetime] = FieldInfo(alias="opLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this OperationalPlanning data, in
    ISO8601 UTC format with millisecond precision.
    """

    op_remark: Optional[str] = FieldInfo(alias="opRemark", default=None)
    """Remark text regarding this operation planning."""

    op_source: Optional[str] = FieldInfo(alias="opSource", default=None)
    """The person, unit, organization, etc. responsible for this operation planning."""

    op_start_date: Optional[datetime] = FieldInfo(alias="opStartDate", default=None)
    """
    The start date of this operational planning, in ISO8601 UTC format with
    millisecond precision.
    """

    op_status: Optional[str] = FieldInfo(alias="opStatus", default=None)
    """The status of this operational planning."""


class SiteTupleResponseItemSiteOperationPathway(BaseModel):
    pw_definition: Optional[str] = FieldInfo(alias="pwDefinition", default=None)
    """Text defining this pathway from its constituent parts."""

    pw_last_changed_by: Optional[str] = FieldInfo(alias="pwLastChangedBy", default=None)
    """The name of the person who made the most recent change to this Pathway data."""

    pw_last_changed_date: Optional[datetime] = FieldInfo(alias="pwLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this Pathway data, in ISO 8601
    UTC format with millisecond precision.
    """

    pw_type: Optional[str] = FieldInfo(alias="pwType", default=None)
    """The type of paths that constitute this pathway."""

    pw_usage: Optional[str] = FieldInfo(alias="pwUsage", default=None)
    """The intended use of this pathway."""


class SiteTupleResponseItemSiteOperationWaiver(BaseModel):
    expiration_date: Optional[datetime] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date of this waiver, in ISO8601 UTC format with millisecond
    precision.
    """

    has_expired: Optional[bool] = FieldInfo(alias="hasExpired", default=None)
    """Boolean indicating whether or not this waiver has expired."""

    issue_date: Optional[datetime] = FieldInfo(alias="issueDate", default=None)
    """
    The issue date of this waiver, in ISO8601 UTC format with millisecond precision.
    """

    issuer_name: Optional[str] = FieldInfo(alias="issuerName", default=None)
    """The name of the person who issued this waiver."""

    requester_name: Optional[str] = FieldInfo(alias="requesterName", default=None)
    """The name of the person requesting this waiver."""

    requester_phone_number: Optional[str] = FieldInfo(alias="requesterPhoneNumber", default=None)
    """The phone number of the person requesting this waiver."""

    requesting_unit: Optional[str] = FieldInfo(alias="requestingUnit", default=None)
    """The unit requesting this waiver."""

    waiver_applies_to: Optional[str] = FieldInfo(alias="waiverAppliesTo", default=None)
    """Description of the entities to which this waiver applies."""

    waiver_description: Optional[str] = FieldInfo(alias="waiverDescription", default=None)
    """The description of this waiver."""

    waiver_last_changed_by: Optional[str] = FieldInfo(alias="waiverLastChangedBy", default=None)
    """The name of the person who made the most recent change to this Waiver data."""

    waiver_last_changed_date: Optional[datetime] = FieldInfo(alias="waiverLastChangedDate", default=None)
    """
    The datetime of the most recent change made to this waiver data, in ISO8601 UTC
    format with millisecond precision.
    """


class SiteTupleResponseItemSiteOperation(BaseModel):
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

    id_site: str = FieldInfo(alias="idSite")
    """The ID of the parent site."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    daily_operations: Optional[List[SiteTupleResponseItemSiteOperationDailyOperation]] = FieldInfo(
        alias="dailyOperations", default=None
    )
    """
    Collection providing hours of operation and other information specific to a day
    of the week.
    """

    dops_last_changed_by: Optional[str] = FieldInfo(alias="dopsLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to data in the
    DailyOperations collection.
    """

    dops_last_changed_date: Optional[datetime] = FieldInfo(alias="dopsLastChangedDate", default=None)
    """
    The datetime of the most recent change made to data in the DailyOperations
    collection, in ISO 8601 UTC format with millisecond precision.
    """

    dops_last_changed_reason: Optional[str] = FieldInfo(alias="dopsLastChangedReason", default=None)
    """
    The reason for the most recent change to data in the dailyOperations collection.
    """

    id_launch_site: Optional[str] = FieldInfo(alias="idLaunchSite", default=None)
    """Id of the associated launchSite entity."""

    maximum_on_grounds: Optional[List[SiteTupleResponseItemSiteOperationMaximumOnGround]] = FieldInfo(
        alias="maximumOnGrounds", default=None
    )
    """
    Collection providing maximum on ground (MOG) information for specific aircraft
    at the site associated with this SiteOperations record.
    """

    mogs_last_changed_by: Optional[str] = FieldInfo(alias="mogsLastChangedBy", default=None)
    """
    The name of the person who made the most recent change to data in the
    MaximumOnGrounds collection.
    """

    mogs_last_changed_date: Optional[datetime] = FieldInfo(alias="mogsLastChangedDate", default=None)
    """
    The datetime of the most recent change made to data in the MaximumOnGrounds
    collection, in ISO 8601 UTC format with millisecond precision.
    """

    mogs_last_changed_reason: Optional[str] = FieldInfo(alias="mogsLastChangedReason", default=None)
    """
    The reason for the most recent change to data in the MaximumOnGrounds
    collection.
    """

    operational_deviations: Optional[List[SiteTupleResponseItemSiteOperationOperationalDeviation]] = FieldInfo(
        alias="operationalDeviations", default=None
    )
    """
    Collection providing relevant information in the event of deviations/exceptions
    to normal operations.
    """

    operational_plannings: Optional[List[SiteTupleResponseItemSiteOperationOperationalPlanning]] = FieldInfo(
        alias="operationalPlannings", default=None
    )
    """Collection of planning information associated with this SiteOperations record."""

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

    pathways: Optional[List[SiteTupleResponseItemSiteOperationPathway]] = None
    """
    Collection detailing operational pathways at the Site associated with this
    SiteOperations record.
    """

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    waivers: Optional[List[SiteTupleResponseItemSiteOperationWaiver]] = None
    """
    Collection documenting operational waivers that have been issued for the Site
    associated with this record.
    """


class SiteTupleResponseItemSiteRemark(BaseModel):
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

    id_site: str = FieldInfo(alias="idSite")
    """The ID of the site to which this remark applies."""

    source: str
    """Source of the data."""

    text: str
    """The text of the remark."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    code: Optional[str] = None
    """The remark type identifier.

    For example, the Mobility Air Forces (MAF) remark code, defined in the Airfield
    Suitability and Restriction Report (ASRR).
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    name: Optional[str] = None
    """The name of the remark."""

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

    orig_rmk_id: Optional[str] = FieldInfo(alias="origRmkId", default=None)
    """Unique identifier of the Site Remark record from the originating system."""

    type: Optional[str] = None
    """The remark type (e.g. Caution, Information, Misc, Restriction, etc.)."""


class SiteTupleResponseItem(BaseModel):
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

    name: str
    """The name of this site."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    activity: Optional[str] = None
    """
    Indicates the function or mission of an entity, which that entity may or may not
    be engaged in at any particular time. Typically refers to a unit, organization,
    or installation/site performing a specific function or mission such as a
    redistribution center or naval shipyard. The specific usage and enumerations
    contained in this field may be found in the documentation provided in the
    referenceDoc field. If referenceDoc not provided, users may consult the data
    provider.
    """

    air_def_area: Optional[str] = FieldInfo(alias="airDefArea", default=None)
    """
    Air Defense District (ADD) or Air Defense Area (ADA) in which the geographic
    coordinates reside.
    """

    allegiance: Optional[str] = None
    """
    The DoD Standard Country Code designator for the country or political entity to
    which the site owes its allegiance. This field will be set to "OTHR" if the
    source value does not match a UDL Country code value (ISO-3166-ALPHA-2).
    """

    alt_allegiance: Optional[str] = FieldInfo(alias="altAllegiance", default=None)
    """
    Specifies an alternate allegiance code if the data provider code is not part of
    an official Country Code standard such as ISO-3166 or FIPS. This field will be
    set to the value provided by the source and should be used for all Queries
    specifying allegiance.
    """

    be_number: Optional[str] = FieldInfo(alias="beNumber", default=None)
    """The Basic Encyclopedia Number associated with the Site.

    Uniquely identifies the installation of a site. The beNumber is generated based
    on the value input for the COORD to determine the appropriate World Aeronautical
    Chart (WAC) location identifier, the system assigned record originator and a
    one-up-number.
    """

    cat_code: Optional[str] = FieldInfo(alias="catCode", default=None)
    """
    The category code that represents the associated site purpose within the target
    system.
    """

    cat_text: Optional[str] = FieldInfo(alias="catText", default=None)
    """Textual Description of Site catCode."""

    class_rating: Optional[str] = FieldInfo(alias="classRating", default=None)
    """Indicates the importance of the entity to the OES or MIR system.

    This data element is restricted to update by DIA (DB-4). Valid values are:

    0 - Does not meet criteria above

    1 - Primary importance to system

    2 - Secondary importance to system

    3 - Tertiary importance to system

    O - Other. Explain in Remarks.
    """

    condition: Optional[str] = None
    """The physical manner of being or state of existence of the entity.

    A physical condition that must be considered in the determining of a course of
    action. The specific usage and enumerations contained in this field may be found
    in the documentation provided in the referenceDoc field. If referenceDoc not
    provided, users may consult the data provider.
    """

    condition_avail: Optional[str] = FieldInfo(alias="conditionAvail", default=None)
    """Availability of the entity relative to its condition.

    Indicates the reason the entity is not fully operational. The specific usage and
    enumerations contained in this field may be found in the documentation provided
    in the referenceDoc field. If referenceDoc not provided, users may consult the
    data provider.
    """

    coord: Optional[str] = None
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

    Pos. 1-21. Unknown Latitude and Unknown Longitude [000000000U000000000U].
    """

    coord_datum: Optional[str] = FieldInfo(alias="coordDatum", default=None)
    """A mathematical model of the earth used to calculate coordinates on a map.

    US Forces use the World Geodetic System 1984 (WGS 84), but also use maps by
    allied countries with local datums. The datum must be specified to ensure
    accuracy of coordinates. The specific usage and enumerations contained in this
    field may be found in the documentation provided in the referenceDoc field. If
    referenceDoc not provided, users may consult the data provider.
    """

    coord_deriv_acc: Optional[float] = FieldInfo(alias="coordDerivAcc", default=None)
    """
    Indicates the plus or minus error assessed against the method used to derive the
    coordinate.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    elev_msl: Optional[float] = FieldInfo(alias="elevMsl", default=None)
    """
    Ground elevation of the geographic coordinates referenced to (above or below)
    Mean Sea Level (MSL) vertical datum, in meters.
    """

    elev_msl_conf_lvl: Optional[int] = FieldInfo(alias="elevMslConfLvl", default=None)
    """
    Indicates the confidence level expressed as a percent that a specific geometric
    spatial element, ELEVATION_MSL linear accuracy, has been vertically positioned
    to within a specified vertical accuracy.
    """

    elev_msl_deriv_acc: Optional[float] = FieldInfo(alias="elevMslDerivAcc", default=None)
    """
    Indicates the plus or minus error assessed against the method used to derive the
    elevation.
    """

    entity: Optional[EntityFull] = None
    """
    An entity is a generic representation of any object within a space/SSA system
    such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
    entity can have an operating unit, a location (if terrestrial), and statuses.
    """

    eval: Optional[int] = None
    """
    Eval represents the Intelligence Confidence Level or the Reliability/degree of
    confidence that the analyst has assigned to the data within this record. The
    numerical range is from 1 to 9 with 1 representing the highest confidence level.
    """

    faa: Optional[str] = None
    """
    The Federal Aviation Administration (FAA) Location ID of this site, if
    applicable.
    """

    fpa: Optional[str] = None
    """Functional Production Area (FPA) under the Shared Production Program (SPP).

    Producers are defined per country per FPA. The specific usage and enumerations
    contained in this field may be found in the documentation provided in the
    referenceDoc field. If referenceDoc not provided, users may consult the data
    provider.
    """

    funct_primary: Optional[str] = FieldInfo(alias="functPrimary", default=None)
    """Principal operational function being performed.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    geo_area: Optional[str] = FieldInfo(alias="geoArea", default=None)
    """
    Geographical region code used by the Requirements Management System (RMS) as
    specified by National Geospatial Agency (NGA) in Flight Information Publications
    (FIPS) 10-4, Appendix 3 - Country Code and Geographic Region Codes. The specific
    usage and enumerations contained in this field may be found in the documentation
    provided in the referenceDoc field. If referenceDoc not provided, users may
    consult the data provider.
    """

    geoidal_msl_sep: Optional[float] = FieldInfo(alias="geoidalMslSep", default=None)
    """The distance between Mean Sea Level and a referenced ellipsoid, in meters."""

    grade: Optional[int] = None
    """
    Indicates the amount or degree of deviation from the horizontal represented as a
    percent. Grade is determined by the formula: vertical distance (VD) divided by
    horizontal distance (HD) times 100. VD is the difference between the highest and
    lowest elevation within the entity. HD is the linear distance between the
    highest and lowest elevation.
    """

    iata: Optional[str] = None
    """
    The International Air Transport Association (IATA) code of this site, if
    applicable.
    """

    icao: Optional[str] = None
    """
    The International Civil Aviation Organization (ICAO) code of this site, if
    applicable.
    """

    ident: Optional[str] = None
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

    id_entity: Optional[str] = FieldInfo(alias="idEntity", default=None)
    """Unique identifier of the parent entity. idEntity is required for Put."""

    id_parent_site: Optional[str] = FieldInfo(alias="idParentSite", default=None)
    """Unique identifier of the Parent Site record associated with this Site record."""

    lz_usage: Optional[str] = FieldInfo(alias="lzUsage", default=None)
    """Indicates the normal usage of the Landing Zone (LZ).

    Intended as, but not constrained to MIDB Helocopter Landing Area usage value
    definitions:

    AF - Airfield

    FD - Field

    HC - High Crop. 1 meter and over.

    HY - Highway

    LB - Lake Bed

    LC - Low Crop. 0-1 meters

    O - Other. Explain In Remarks.

    PD - Paddy

    PK - Park

    PS - Pasture

    RB - Riverbed

    SP - Sport Field

    U - Unknown

    Z - Inconclusive Analysis.
    """

    max_runway_length: Optional[int] = FieldInfo(alias="maxRunwayLength", default=None)
    """The length of the longest runway at this site, if applicable, in meters."""

    mil_grid: Optional[str] = FieldInfo(alias="milGrid", default=None)
    """
    The Military Grid Reference System is the geocoordinate standard used by NATO
    militaries for locating points on Earth. The MGRS is derived from the Universal
    Transverse Mercator (UTM) grid system and the Universal Polar Stereographic
    (UPS) grid system, but uses a different labeling convention. The MGRS is used as
    geocode for the entire Earth. Example of an milgrid coordinate, or grid
    reference, would be 4QFJ12345678, which consists of three parts:

    4Q (grid zone designator, GZD)

    FJ (the 100,000-meter square identifier)

    12345678 (numerical location; easting is 1234 and northing is 5678, in this case
    specifying a location with 10 m resolution).
    """

    mil_grid_sys: Optional[str] = FieldInfo(alias="milGridSys", default=None)
    """Indicates the grid system used in the development of the milGrid coordinates.

    Values are:

    UPS - Universal Polar System

    UTM - Universal Transverse Mercator.
    """

    msn_primary: Optional[str] = FieldInfo(alias="msnPrimary", default=None)
    """
    Indicates the principal type of mission that an entity is organized and equipped
    to perform. The specific usage and enumerations contained in this field may be
    found in the documentation provided in the referenceDoc field. If referenceDoc
    not provided, users may consult the data provider.
    """

    msn_primary_spec: Optional[str] = FieldInfo(alias="msnPrimarySpec", default=None)
    """
    Indicates the principal specialty type of mission that an entity is organized
    and equipped to perform. The specific usage and enumerations contained in this
    field may be found in the documentation provided in the referenceDoc field. If
    referenceDoc not provided, users may consult the data provider.
    """

    notes: Optional[str] = None
    """Optional notes/comments for the site."""

    nuc_cap: Optional[str] = FieldInfo(alias="nucCap", default=None)
    """A sites ability to conduct nuclear warfare. Valid Values are:

    A - Nuclear Ammo Or Warheads Available

    N - No Nuclear Offense

    O - Other. Explain in Remarks

    U - Unknown

    W - Nuclear Weapons Available

    Y - Nuclear Warfare Offensive Capability

    Z - Inconclusive Analysis.
    """

    oper_status: Optional[str] = FieldInfo(alias="operStatus", default=None)
    """
    The Degree to which an entity is ready to perform the overall operational
    mission(s) for which it was organized and equipped. The specific usage and
    enumerations contained in this field may be found in the documentation provided
    in the referenceDoc field. If referenceDoc not provided, users may consult the
    data provider.
    """

    origin: Optional[str] = None
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    orig_lz_id: Optional[str] = FieldInfo(alias="origLzId", default=None)
    """Unique identifier of the LZ record from the originating system."""

    orig_network: Optional[str] = FieldInfo(alias="origNetwork", default=None)
    """
    The originating source network on which this record was created, auto-populated
    by the system.
    """

    orig_site_id: Optional[str] = FieldInfo(alias="origSiteID", default=None)
    """Unique identifier of the Site record from the originating system."""

    osuffix: Optional[str] = None
    """The O-suffix associated with this site.

    The O-suffix is a five-character alpha/numeric system used to identify a site,
    or demographic area, within an installation. The Installation Basic Encyclopedia
    (beNumber), in conjunction with the O-suffix, uniquely identifies the Site. The
    Installation beNumber and oSuffix are also used in conjunction with the catCode
    to classify the function or purpose of the facility.
    """

    pin: Optional[str] = None
    """Site number of a specific electronic site or its associated equipment."""

    pol_subdiv: Optional[str] = FieldInfo(alias="polSubdiv", default=None)
    """Political subdivision in which the geographic coordinates reside.

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    pop_area: Optional[bool] = FieldInfo(alias="popArea", default=None)
    """Indicates whether the facility is in or outside of a populated area.

    True, the facility is in or within 5 NM of a populated area. False, the facility
    is outside a populated area.
    """

    pop_area_prox: Optional[float] = FieldInfo(alias="popAreaProx", default=None)
    """
    Indicates the distance to nearest populated area (over 1,000 people) in nautical
    miles.
    """

    rec_status: Optional[str] = FieldInfo(alias="recStatus", default=None)
    """
    Validity and currency of the data in the record to be used in conjunction with
    the other elements in the record as defined by SOPs.

    A - Active

    I - Inactive

    K - Acknowledged

    L - Local

    Q - A nominated (NOM) or Data Change Request (DCR) record

    R - Production reduced by CMD decision

    W - Working Record.
    """

    reference_doc: Optional[str] = FieldInfo(alias="referenceDoc", default=None)
    """
    The reference documentation that specifies the usage and enumerations contained
    in this record. If referenceDoc not provided, users may consult the data
    provider.
    """

    res_prod: Optional[str] = FieldInfo(alias="resProd", default=None)
    """
    Responsible Producer - Organization that is responsible for the maintenance of
    the record.
    """

    review_date: Optional[date] = FieldInfo(alias="reviewDate", default=None)
    """
    Date on which the data in the record was last reviewed by the responsible
    analyst for accuracy and currency, in ISO8601 UTC format. This date cannot be
    greater than the current date.
    """

    runways: Optional[int] = None
    """The number of runways at the site, if applicable."""

    site_operations: Optional[List[SiteTupleResponseItemSiteOperation]] = FieldInfo(
        alias="siteOperations", default=None
    )

    site_remarks: Optional[List[SiteTupleResponseItemSiteRemark]] = FieldInfo(alias="siteRemarks", default=None)
    """Remarks contain amplifying information for a specific service.

    The information may contain context and interpretations for consumer use.
    """

    sym_code: Optional[str] = FieldInfo(alias="symCode", default=None)
    """
    A standard scheme for symbol coding enabling the transfer, display and use of
    symbols and graphics among information systems, as per MIL-STD 2525B, and
    supported by the element ident.
    """

    type: Optional[str] = None
    """The type of this site (AIRBASE, AIRFIELD, AIRPORT, NAVAL STATION, etc.)."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    usage: Optional[str] = None
    """The use authorization type of this site (e.g MILITARY, CIVIL, JOINT-USE, etc.)."""

    utm: Optional[str] = None
    """Universal Transverse Mercator (UTM) grid coordinates.

    Pos. 1-2, UTM Zone Column [01-60

    Pos. 3, UTM Zone Row [C-HJ-NP-X]

    Pos. 4, UTM False Easting [0-9]

    Pos. 5-9, UTM Meter Easting [0-9][0-9][0-9][0-9][0-9]

    Pos. 10-11, UTM False Northing [0-9][0-9]

    Pos. 12-16, UTM Meter Northing [0-9][0-9][0-9][0-9][0-9].
    """

    veg_ht: Optional[float] = FieldInfo(alias="vegHt", default=None)
    """Maximum expected height of the vegetation in the Landing Zone (LZ), in meters."""

    veg_type: Optional[str] = FieldInfo(alias="vegType", default=None)
    """The predominant vegetation found in the Landing Zone (LZ).

    The specific usage and enumerations contained in this field may be found in the
    documentation provided in the referenceDoc field. If referenceDoc not provided,
    users may consult the data provider.
    """

    wac: Optional[str] = None
    """
    World Aeronautical Chart identifier for the area in which a designated place is
    located.
    """


SiteTupleResponse: TypeAlias = List[SiteTupleResponseItem]
