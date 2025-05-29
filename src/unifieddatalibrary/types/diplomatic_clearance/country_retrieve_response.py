# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CountryRetrieveResponse",
    "DiplomaticClearanceCountryContact",
    "DiplomaticClearanceCountryEntryExitPoint",
    "DiplomaticClearanceCountryProfile",
]


class DiplomaticClearanceCountryContact(BaseModel):
    ah_num: Optional[str] = FieldInfo(alias="ahNum", default=None)
    """Phone number for this contact after regular business hours."""

    ah_spd_dial_code: Optional[str] = FieldInfo(alias="ahSpdDialCode", default=None)
    """Speed dial code for this contact after regular business hours."""

    comm_num: Optional[str] = FieldInfo(alias="commNum", default=None)
    """Commercial phone number for this contact."""

    comm_spd_dial_code: Optional[str] = FieldInfo(alias="commSpdDialCode", default=None)
    """Commercial speed dial code for this contact."""

    contact_id: Optional[str] = FieldInfo(alias="contactId", default=None)
    """Identifier of the contact for this country."""

    contact_name: Optional[str] = FieldInfo(alias="contactName", default=None)
    """Name of the contact for this country."""

    contact_remark: Optional[str] = FieldInfo(alias="contactRemark", default=None)
    """Remarks about this contact."""

    dsn_num: Optional[str] = FieldInfo(alias="dsnNum", default=None)
    """Defense Switched Network (DSN) phone number for this contact."""

    dsn_spd_dial_code: Optional[str] = FieldInfo(alias="dsnSpdDialCode", default=None)
    """Defense Switched Network (DSN) speed dial code for this contact."""

    fax_num: Optional[str] = FieldInfo(alias="faxNum", default=None)
    """Fax number for this contact."""

    nipr_num: Optional[str] = FieldInfo(alias="niprNum", default=None)
    """
    Phone number to contact the Diplomatic Attache Office (DAO) for this country
    over a secure NIPR line.
    """

    sipr_num: Optional[str] = FieldInfo(alias="siprNum", default=None)
    """
    Phone number to contact the Diplomatic Attache Office (DAO) for this country
    over a secure SIPR line.
    """


class DiplomaticClearanceCountryEntryExitPoint(BaseModel):
    is_entry: Optional[bool] = FieldInfo(alias="isEntry", default=None)
    """Flag indicating whether this is a point of entry for this country."""

    is_exit: Optional[bool] = FieldInfo(alias="isExit", default=None)
    """Flag indicating whether this is a point of exit for this country."""

    point_name: Optional[str] = FieldInfo(alias="pointName", default=None)
    """Name of this entry/exit point."""


class DiplomaticClearanceCountryProfile(BaseModel):
    cargo_pax_remark: Optional[str] = FieldInfo(alias="cargoPaxRemark", default=None)
    """
    Remarks concerning aircraft cargo and passenger information for this country
    profile.
    """

    clearance_id: Optional[str] = FieldInfo(alias="clearanceId", default=None)
    """Identifier of the associated diplomatic clearance issued by the host country."""

    crew_info_remark: Optional[str] = FieldInfo(alias="crewInfoRemark", default=None)
    """Remarks concerning crew information for this country profile."""

    def_clearance_status: Optional[str] = FieldInfo(alias="defClearanceStatus", default=None)
    """
    Code denoting the status of the default diplomatic clearance (e.g., A for
    Approved via APACS, E for Requested via email, etc.).
    """

    def_entry_remark: Optional[str] = FieldInfo(alias="defEntryRemark", default=None)
    """Remarks concerning the default entry point for this country."""

    def_entry_time: Optional[str] = FieldInfo(alias="defEntryTime", default=None)
    """Zulu default entry time for this country expressed in HH:MM format."""

    def_exit_remark: Optional[str] = FieldInfo(alias="defExitRemark", default=None)
    """Remarks concerning the default exit point for this country."""

    def_exit_time: Optional[str] = FieldInfo(alias="defExitTime", default=None)
    """Zulu default exit time for this country expressed in HH:MM format."""

    flt_info_remark: Optional[str] = FieldInfo(alias="fltInfoRemark", default=None)
    """Remarks concerning flight information for this country profile."""

    haz_info_remark: Optional[str] = FieldInfo(alias="hazInfoRemark", default=None)
    """Remarks concerning hazardous material information for this country profile."""

    land_def_prof: Optional[bool] = FieldInfo(alias="landDefProf", default=None)
    """Flag indicating whether this is the default landing profile for this country."""

    land_lead_time: Optional[int] = FieldInfo(alias="landLeadTime", default=None)
    """Amount of lead time required for an aircraft to land in this country.

    Units need to be specified in the landLeadTimeUnit field.
    """

    land_lead_time_remark: Optional[str] = FieldInfo(alias="landLeadTimeRemark", default=None)
    """Remarks concerning the landing lead time required for this country."""

    land_lead_time_unit: Optional[str] = FieldInfo(alias="landLeadTimeUnit", default=None)
    """
    Unit of time specified for the landLeadTime field to indicate the landing lead
    time required for this country.
    """

    land_valid_period_minus: Optional[int] = FieldInfo(alias="landValidPeriodMinus", default=None)
    """
    Amount of time before the landing valid period that an aircraft is allowed to
    land in this country for this profile. The unit of time should be specified in
    the landValidPeriodUnit field.
    """

    land_valid_period_plus: Optional[int] = FieldInfo(alias="landValidPeriodPlus", default=None)
    """
    Amount of time after the landing valid period that an aircraft is allowed to
    land in this country for this profile. The unit of time should be specified in
    the landValidPeriodUnit field.
    """

    land_valid_period_remark: Optional[str] = FieldInfo(alias="landValidPeriodRemark", default=None)
    """Remarks concerning the valid landing time period for this country."""

    land_valid_period_unit: Optional[str] = FieldInfo(alias="landValidPeriodUnit", default=None)
    """
    Unit of time specified for the landValidPeriodPlus and landValidPeriodMinus
    fields to indicate the valid landing period for this country.
    """

    overfly_def_prof: Optional[bool] = FieldInfo(alias="overflyDefProf", default=None)
    """Flag indicating whether this is the default overfly profile for this country."""

    overfly_lead_time: Optional[int] = FieldInfo(alias="overflyLeadTime", default=None)
    """
    Amount of lead time required for an aircraft to enter and fly over the airspace
    of this country. Units need to be specified in the overflyLeadTimeUnit field.
    """

    overfly_lead_time_remark: Optional[str] = FieldInfo(alias="overflyLeadTimeRemark", default=None)
    """Remarks concerning the overfly lead time required for this country."""

    overfly_lead_time_unit: Optional[str] = FieldInfo(alias="overflyLeadTimeUnit", default=None)
    """
    Unit of time specified for the overflyLeadTime field to indicate the overfly
    lead time required for this country.
    """

    overfly_valid_period_minus: Optional[int] = FieldInfo(alias="overflyValidPeriodMinus", default=None)
    """
    Amount of time before the overfly valid period that an aircraft is allowed to
    fly over this country for this profile. The unit of time should be specified in
    the overflyValidPeriodUnit field.
    """

    overfly_valid_period_plus: Optional[int] = FieldInfo(alias="overflyValidPeriodPlus", default=None)
    """
    Amount of time after the overfly valid period that an aircraft is allowed to fly
    over this country for this profile. The unit of time should be specified in the
    overflyValidPeriodUnit field.
    """

    overfly_valid_period_remark: Optional[str] = FieldInfo(alias="overflyValidPeriodRemark", default=None)
    """Remarks concerning the valid overfly time period for this country."""

    overfly_valid_period_unit: Optional[str] = FieldInfo(alias="overflyValidPeriodUnit", default=None)
    """
    Unit of time specified for the overflyValidPeriodPlus and
    overflyValidPeriodMinus fields to indicate the valid overfly period for this
    country.
    """

    profile: Optional[str] = None
    """The diplomatic clearance profile name used within clearance management systems."""

    profile_agency: Optional[str] = FieldInfo(alias="profileAgency", default=None)
    """The agency to which this profile applies."""

    profile_id: Optional[str] = FieldInfo(alias="profileId", default=None)
    """Identifier of the diplomatic clearance country profile."""

    profile_remark: Optional[str] = FieldInfo(alias="profileRemark", default=None)
    """Remarks concerning this country profile."""

    req_ac_alt_name: Optional[bool] = FieldInfo(alias="reqACAltName", default=None)
    """
    Flag indicating whether alternate aircraft names are required to be reported to
    the country using this diplomatic clearance profile.
    """

    req_all_haz_info: Optional[bool] = FieldInfo(alias="reqAllHazInfo", default=None)
    """
    Flag indicating whether all hazardous material information is required to be
    reported to the country using this diplomatic clearance profile.
    """

    req_amc_std_info: Optional[bool] = FieldInfo(alias="reqAMCStdInfo", default=None)
    """
    Flag indicating whether standard AMC information is required to be reported to
    the country using this diplomatic clearance profile.
    """

    req_cargo_list: Optional[bool] = FieldInfo(alias="reqCargoList", default=None)
    """
    Flag indicating whether a cargo list is required to be reported to the country
    using this diplomatic clearance profile.
    """

    req_cargo_pax: Optional[bool] = FieldInfo(alias="reqCargoPax", default=None)
    """
    Flag indicating whether aircraft cargo and passenger information is required to
    be reported to the country using this diplomatic clearance profile.
    """

    req_class1_info: Optional[bool] = FieldInfo(alias="reqClass1Info", default=None)
    """
    Flag indicating whether Class 1 hazardous material information is required to be
    reported to the country using this diplomatic clearance profile.
    """

    req_class9_info: Optional[bool] = FieldInfo(alias="reqClass9Info", default=None)
    """
    Flag indicating whether Class 9 hazardous material information is required to be
    reported to the country using this diplomatic clearance profile.
    """

    req_crew_comp: Optional[bool] = FieldInfo(alias="reqCrewComp", default=None)
    """
    Flag indicating whether the number of crew members on a flight is required to be
    reported to the country using this diplomatic clearance profile.
    """

    req_crew_detail: Optional[bool] = FieldInfo(alias="reqCrewDetail", default=None)
    """
    Flag indicating whether the names, ranks, and positions of crew members are
    required to be reported to the country using this diplomatic clearance profile.
    """

    req_crew_info: Optional[bool] = FieldInfo(alias="reqCrewInfo", default=None)
    """
    Flag indicating whether crew information is required to be reported to the
    country using this diplomatic clearance profile.
    """

    req_div1_info: Optional[bool] = FieldInfo(alias="reqDiv1Info", default=None)
    """
    Flag indicating whether Division 1.1 hazardous material information is required
    to be reported to the country using this diplomatic clearance profile.
    """

    req_dv: Optional[bool] = FieldInfo(alias="reqDV", default=None)
    """
    Flag indicating whether distinguished visitors are required to be reported to
    the country using this diplomatic clearance profile.
    """

    req_entry_exit_coord: Optional[bool] = FieldInfo(alias="reqEntryExitCoord", default=None)
    """
    Flag indicating whether entry/exit coordinates need to be specified for this
    diplomatic clearance profile.
    """

    req_flt_info: Optional[bool] = FieldInfo(alias="reqFltInfo", default=None)
    """
    Flag indicating whether flight information is required to be reported to the
    country using this diplomatic clearance profile.
    """

    req_flt_plan_route: Optional[bool] = FieldInfo(alias="reqFltPlanRoute", default=None)
    """
    Flag indicating whether a flight plan route is required to be reported to the
    country using this diplomatic clearance profile.
    """

    req_fund_source: Optional[bool] = FieldInfo(alias="reqFundSource", default=None)
    """
    Flag indicating whether aviation funding sources are required to be reported to
    the country using this diplomatic clearance profile.
    """

    req_haz_info: Optional[bool] = FieldInfo(alias="reqHazInfo", default=None)
    """
    Flag indicating whether hazardous material information is required to be
    reported to the country using this diplomatic clearance profile.
    """

    req_icao: Optional[bool] = FieldInfo(alias="reqICAO", default=None)
    """
    Flag indicating whether this diplomatic clearance profile applies to specific
    ICAO(s). These specific ICAO(s) should be clarified in the fltInfoRemark field.
    """

    req_passport_info: Optional[bool] = FieldInfo(alias="reqPassportInfo", default=None)
    """
    Flag indicating whether passport information is required to be reported to the
    country using this diplomatic clearance profile.
    """

    req_raven: Optional[bool] = FieldInfo(alias="reqRaven", default=None)
    """
    Flag indicating whether ravens are required to be reported to the country using
    this diplomatic clearance profile.
    """

    req_rep_change: Optional[bool] = FieldInfo(alias="reqRepChange", default=None)
    """
    Flag indicating whether changes are required to be reported to the country using
    this diplomatic clearance profile.
    """

    req_tail_num: Optional[bool] = FieldInfo(alias="reqTailNum", default=None)
    """
    Flag indicating whether an aircraft tail number is required to be reported to
    the country using this diplomatic clearance profile.
    """

    req_weapons_info: Optional[bool] = FieldInfo(alias="reqWeaponsInfo", default=None)
    """
    Flag indicating whether weapons information is required to be reported to the
    country using this diplomatic clearance profile.
    """

    undefined_crew_reporting: Optional[bool] = FieldInfo(alias="undefinedCrewReporting", default=None)
    """
    Flag indicating whether crew reporting is undefined for the country using this
    diplomatic clearance profile.
    """


class CountryRetrieveResponse(BaseModel):
    classification_marking: str = FieldInfo(alias="classificationMarking")
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    country_code: str = FieldInfo(alias="countryCode")
    """
    The DoD Standard Country Code designator for the country for which the
    diplomatic clearance will be issued. This field should be set to "OTHR" if the
    source value does not match a UDL country code value (ISO-3166-ALPHA-2).
    """

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

    last_changed_date: datetime = FieldInfo(alias="lastChangedDate")
    """
    Last time this country's diplomatic clearance profile information was updated,
    in ISO 8601 UTC format with millisecond precision.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    accepts_dms: Optional[bool] = FieldInfo(alias="acceptsDMS", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office can receive
    messages using the Defense Message System (DMS).
    """

    accepts_email: Optional[bool] = FieldInfo(alias="acceptsEmail", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office can receive
    messages via email.
    """

    accepts_fax: Optional[bool] = FieldInfo(alias="acceptsFax", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office can receive
    messages via fax.
    """

    accepts_sipr_net: Optional[bool] = FieldInfo(alias="acceptsSIPRNet", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office can receive
    messages via SIPRNet.
    """

    agency: Optional[str] = None
    """The source agency of the diplomatic clearance country data."""

    alt_country_code: Optional[str] = FieldInfo(alias="altCountryCode", default=None)
    """
    Specifies an alternate country code if the data provider code does not match a
    UDL Country code value (ISO-3166-ALPHA-2). This field will be set to the value
    provided by the source and should be used for all Queries specifying a Country
    Code.
    """

    close_time: Optional[str] = FieldInfo(alias="closeTime", default=None)
    """
    Zulu closing time of this country's diplomatic clearance office expressed in
    HH:MM format.
    """

    country_id: Optional[str] = FieldInfo(alias="countryId", default=None)
    """System generated code used to identify a country."""

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)
    """Name of the country for which the diplomatic clearance will be issued."""

    country_remark: Optional[str] = FieldInfo(alias="countryRemark", default=None)
    """
    Remarks concerning the country for which the diplomatic clearance will be
    issued.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    diplomatic_clearance_country_contacts: Optional[List[DiplomaticClearanceCountryContact]] = FieldInfo(
        alias="diplomaticClearanceCountryContacts", default=None
    )
    """Collection of diplomatic clearance profile information for this country."""

    diplomatic_clearance_country_entry_exit_points: Optional[List[DiplomaticClearanceCountryEntryExitPoint]] = (
        FieldInfo(alias="diplomaticClearanceCountryEntryExitPoints", default=None)
    )
    """Collection of diplomatic clearance profile information for this country."""

    diplomatic_clearance_country_profiles: Optional[List[DiplomaticClearanceCountryProfile]] = FieldInfo(
        alias="diplomaticClearanceCountryProfiles", default=None
    )
    """Collection of diplomatic clearance profile information for this country."""

    existing_profile: Optional[bool] = FieldInfo(alias="existingProfile", default=None)
    """Flag indicating whether a diplomatic clearance profile exists for this country."""

    gmt_offset: Optional[str] = FieldInfo(alias="gmtOffset", default=None)
    """
    Time difference between the location of the country for which the diplomatic
    clearance will be issued and the Greenwich Mean Time (GMT), expressed as
    +/-HH:MM. Time zones east of Greenwich have positive offsets and time zones west
    of Greenwich are negative.
    """

    office_name: Optional[str] = FieldInfo(alias="officeName", default=None)
    """Name of this country's diplomatic clearance office."""

    office_poc: Optional[str] = FieldInfo(alias="officePOC", default=None)
    """Name of the point of contact for this country's diplomatic clearance office."""

    office_remark: Optional[str] = FieldInfo(alias="officeRemark", default=None)
    """Remarks concerning this country's diplomatic clearance office."""

    open_fri: Optional[bool] = FieldInfo(alias="openFri", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office is open on
    Friday.
    """

    open_mon: Optional[bool] = FieldInfo(alias="openMon", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office is open on
    Monday.
    """

    open_sat: Optional[bool] = FieldInfo(alias="openSat", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office is open on
    Saturday.
    """

    open_sun: Optional[bool] = FieldInfo(alias="openSun", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office is open on
    Sunday.
    """

    open_thu: Optional[bool] = FieldInfo(alias="openThu", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office is open on
    Thursday.
    """

    open_time: Optional[str] = FieldInfo(alias="openTime", default=None)
    """
    Zulu opening time of this country's diplomatic clearance office expressed in
    HH:MM format.
    """

    open_tue: Optional[bool] = FieldInfo(alias="openTue", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office is open on
    Tuesday.
    """

    open_wed: Optional[bool] = FieldInfo(alias="openWed", default=None)
    """
    Flag indicating whether this country's diplomatic clearance office is open on
    Wednesday.
    """

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
