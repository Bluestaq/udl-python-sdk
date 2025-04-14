# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AirloadplanAbridged",
    "AirLoadPlanHazmatActual",
    "AirLoadPlanHr",
    "AirLoadPlanPalletDetail",
    "AirLoadPlanPaxCargo",
    "AirLoadPlanUlnActual",
]


class AirLoadPlanHazmatActual(BaseModel):
    ashc: Optional[str] = None
    """
    The Air Special Handling Code (ASHC) indicates the type of special handling
    required for hazardous cargo.
    """

    cgc: Optional[str] = None
    """
    Compatibility group code used to specify the controls for the transportation and
    storage of hazardous materials according to the Hazardous Materials Regulations
    issued by the U.S. Department of Transportation.
    """

    class_div: Optional[str] = FieldInfo(alias="classDiv", default=None)
    """
    Class and division of the hazardous material according to the Hazardous
    Materials Regulations issued by the U.S. Department of Transportation.
    """

    haz_description: Optional[str] = FieldInfo(alias="hazDescription", default=None)
    """Description of the hazardous item."""

    hazmat_remarks: Optional[str] = FieldInfo(alias="hazmatRemarks", default=None)
    """Remarks concerning this hazardous material."""

    haz_num: Optional[str] = FieldInfo(alias="hazNum", default=None)
    """
    United Nations number or North American number that identifies hazardous
    materials according to the Hazardous Materials Regulations issued by the U.S.
    Department of Transportation.
    """

    haz_num_type: Optional[str] = FieldInfo(alias="hazNumType", default=None)
    """
    Designates the type of hazmat number for the item (UN for United Nations or NA
    for North American).
    """

    haz_off_icao: Optional[str] = FieldInfo(alias="hazOffICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    hazardous material is unloaded.
    """

    haz_off_itin: Optional[int] = FieldInfo(alias="hazOffItin", default=None)
    """Itinerary number that identifies where the hazardous material is unloaded."""

    haz_on_icao: Optional[str] = FieldInfo(alias="hazOnICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    hazardous material is loaded.
    """

    haz_on_itin: Optional[int] = FieldInfo(alias="hazOnItin", default=None)
    """Itinerary number that identifies where the hazardous material is loaded."""

    haz_pieces: Optional[int] = FieldInfo(alias="hazPieces", default=None)
    """Number of pieces of hazardous cargo."""

    haz_tcn: Optional[str] = FieldInfo(alias="hazTcn", default=None)
    """Transportation Control Number (TCN) of the hazardous item."""

    haz_weight: Optional[float] = FieldInfo(alias="hazWeight", default=None)
    """Total weight of hazardous cargo, including non-explosive parts, in kilograms."""

    item_name: Optional[str] = FieldInfo(alias="itemName", default=None)
    """
    United Nations proper shipping name of the hazardous material according to the
    Hazardous Materials Regulations issued by the U.S. Department of Transportation.
    """

    lot_num: Optional[str] = FieldInfo(alias="lotNum", default=None)
    """Manufacturer's lot number for identification of the hazardous material."""

    net_exp_wt: Optional[float] = FieldInfo(alias="netExpWt", default=None)
    """Net explosive weight of the hazardous material, in kilograms."""


class AirLoadPlanHr(BaseModel):
    container: Optional[str] = None
    """Type of transfer case used."""

    escort: Optional[str] = None
    """Name of the escort for the remains."""

    hr_est_arr_time: Optional[datetime] = FieldInfo(alias="hrEstArrTime", default=None)
    """
    The current estimated time of arrival for the remains in ISO 8601 UTC format
    with millisecond precision.
    """

    hr_off_icao: Optional[str] = FieldInfo(alias="hrOffICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    remains are unloaded.
    """

    hr_off_itin: Optional[int] = FieldInfo(alias="hrOffItin", default=None)
    """Itinerary number that identifies where the remains are unloaded."""

    hr_on_icao: Optional[str] = FieldInfo(alias="hrOnICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    remains are loaded.
    """

    hr_on_itin: Optional[int] = FieldInfo(alias="hrOnItin", default=None)
    """Itinerary number that identifies where the remains are loaded."""

    hr_remarks: Optional[str] = FieldInfo(alias="hrRemarks", default=None)
    """Remarks concerning the remains."""

    name: Optional[str] = None
    """Name of the deceased."""

    rank: Optional[str] = None
    """Rank of the deceased."""

    rec_agency: Optional[str] = FieldInfo(alias="recAgency", default=None)
    """
    Name of the receiving agency or funeral home to which the remains are being
    delivered.
    """

    service: Optional[str] = None
    """Branch of service of the deceased."""

    viewable: Optional[bool] = None
    """Flag indicating if the remains are viewable."""


class AirLoadPlanPalletDetail(BaseModel):
    category: Optional[str] = None
    """Category of special interest cargo."""

    pp: Optional[str] = None
    """Pallet position of the cargo."""

    pp_description: Optional[str] = FieldInfo(alias="ppDescription", default=None)
    """Description of the cargo."""

    pp_off_icao: Optional[str] = FieldInfo(alias="ppOffICAO", default=None)
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    cargo is unloaded.
    """

    pp_pieces: Optional[int] = FieldInfo(alias="ppPieces", default=None)
    """Number of pieces included in the Transportation Control Number (TCN)."""

    pp_remarks: Optional[str] = FieldInfo(alias="ppRemarks", default=None)
    """Remarks concerning the cargo at this pallet position."""

    pp_tcn: Optional[str] = FieldInfo(alias="ppTcn", default=None)
    """Transportation Control Number (TCN) of the cargo."""

    pp_weight: Optional[float] = FieldInfo(alias="ppWeight", default=None)
    """Total weight of the cargo at this pallet position in kilograms."""

    special_interest: Optional[bool] = FieldInfo(alias="specialInterest", default=None)
    """Flag indicating if this cargo is considered special interest."""


class AirLoadPlanPaxCargo(BaseModel):
    amb_pax: Optional[int] = FieldInfo(alias="ambPax", default=None)
    """Number of ambulatory medical passengers in this group."""

    att_pax: Optional[int] = FieldInfo(alias="attPax", default=None)
    """Number of patient attendant passengers in this group."""

    available_pax: Optional[int] = FieldInfo(alias="availablePax", default=None)
    """Number of space available passengers in this group."""

    bag_weight: Optional[float] = FieldInfo(alias="bagWeight", default=None)
    """Weight of baggage in this group in kilograms."""

    civ_pax: Optional[int] = FieldInfo(alias="civPax", default=None)
    """Number of civilian passengers in this group."""

    dv_pax: Optional[int] = FieldInfo(alias="dvPax", default=None)
    """Number of distinguished visitor passengers in this group."""

    fn_pax: Optional[int] = FieldInfo(alias="fnPax", default=None)
    """Number of foreign national passengers in this group."""

    group_cargo_weight: Optional[float] = FieldInfo(alias="groupCargoWeight", default=None)
    """Weight of cargo in this group in kilograms."""

    group_type: Optional[str] = FieldInfo(alias="groupType", default=None)
    """
    Describes the status or action needed for this group of passenger and cargo data
    (e.g. ARRONBD, OFFTHIS, THROUGH, ONTHIS, DEPONBD, OFFNEXT).
    """

    lit_pax: Optional[int] = FieldInfo(alias="litPax", default=None)
    """Number of litter-bound passengers in this group."""

    mail_weight: Optional[float] = FieldInfo(alias="mailWeight", default=None)
    """Weight of mail in this group in kilograms."""

    num_pallet: Optional[int] = FieldInfo(alias="numPallet", default=None)
    """Number of cargo pallets in this group."""

    pallet_weight: Optional[float] = FieldInfo(alias="palletWeight", default=None)
    """Weight of pallets, chains, and devices in this group in kilograms."""

    pax_weight: Optional[float] = FieldInfo(alias="paxWeight", default=None)
    """Weight of passengers in this group in kilograms."""

    required_pax: Optional[int] = FieldInfo(alias="requiredPax", default=None)
    """Number of space required passengers in this group."""


class AirLoadPlanUlnActual(BaseModel):
    num_ambulatory: Optional[int] = FieldInfo(alias="numAmbulatory", default=None)
    """Number of ambulatory patients associated with this load plan."""

    num_attendant: Optional[int] = FieldInfo(alias="numAttendant", default=None)
    """Number of attendants associated with this load plan."""

    num_litter: Optional[int] = FieldInfo(alias="numLitter", default=None)
    """Number of litter patients associated with this load plan."""

    num_pax: Optional[int] = FieldInfo(alias="numPax", default=None)
    """Number of passengers associated with this load plan."""

    offload_id: Optional[int] = FieldInfo(alias="offloadId", default=None)
    """Identifier of the offload itinerary location."""

    offload_lo_code: Optional[str] = FieldInfo(alias="offloadLOCode", default=None)
    """Offload location code."""

    onload_id: Optional[int] = FieldInfo(alias="onloadId", default=None)
    """Identifier of the onload itinerary location."""

    onload_lo_code: Optional[str] = FieldInfo(alias="onloadLOCode", default=None)
    """Onload location code."""

    oplan: Optional[str] = None
    """
    Identification number of the Operation Plan (OPLAN) associated with this load
    plan.
    """

    proj_name: Optional[str] = FieldInfo(alias="projName", default=None)
    """Project name."""

    uln: Optional[str] = None
    """Unit line number."""

    uln_cargo_weight: Optional[float] = FieldInfo(alias="ulnCargoWeight", default=None)
    """Total weight of all cargo items for this unit line number in kilograms."""

    uln_remarks: Optional[str] = FieldInfo(alias="ulnRemarks", default=None)
    """Remarks concerning these unit line number actuals."""


class AirloadplanAbridged(BaseModel):
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

    est_dep_time: datetime = FieldInfo(alias="estDepTime")
    """
    The current estimated time that the aircraft is planned to depart, in ISO 8601
    UTC format with millisecond precision.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    acl_onboard: Optional[float] = FieldInfo(alias="aclOnboard", default=None)
    """Allowable Cabin Load (ACL) onboard the aircraft.

    The maximum weight of passengers, baggage, and cargo that can be safely
    transported in the aircraft cabin, in kilograms.
    """

    acl_released: Optional[float] = FieldInfo(alias="aclReleased", default=None)
    """Allowable Cabin Load (ACL) released this leg.

    The weight of passengers, baggage, and cargo released from the aircraft cabin,
    in kilograms.
    """

    aircraft_mds: Optional[str] = FieldInfo(alias="aircraftMDS", default=None)
    """The Model Design Series designation of the aircraft supporting this load plan."""

    air_load_plan_hazmat_actuals: Optional[List[AirLoadPlanHazmatActual]] = FieldInfo(
        alias="airLoadPlanHazmatActuals", default=None
    )
    """Collection of hazmat actuals associated with this load plan."""

    air_load_plan_hr: Optional[List[AirLoadPlanHr]] = FieldInfo(alias="airLoadPlanHR", default=None)
    """
    Collection of human remains transport information associated with this load
    plan.
    """

    air_load_plan_pallet_details: Optional[List[AirLoadPlanPalletDetail]] = FieldInfo(
        alias="airLoadPlanPalletDetails", default=None
    )
    """
    Collection of cargo information located at the pallet positions associated with
    this load plan.
    """

    air_load_plan_pax_cargo: Optional[List[AirLoadPlanPaxCargo]] = FieldInfo(alias="airLoadPlanPaxCargo", default=None)
    """
    Collection of passenger and cargo details associated with this load plan for
    this leg of the mission.
    """

    air_load_plan_uln_actuals: Optional[List[AirLoadPlanUlnActual]] = FieldInfo(
        alias="airLoadPlanULNActuals", default=None
    )
    """Collection of unit line number actuals associated with this load plan."""

    arr_airfield: Optional[str] = FieldInfo(alias="arrAirfield", default=None)
    """
    Optional identifier of arrival airfield with no International Civil Organization
    (ICAO) code.
    """

    arr_icao: Optional[str] = FieldInfo(alias="arrICAO", default=None)
    """
    The arrival International Civil Organization (ICAO) code of the landing
    airfield.
    """

    available_time: Optional[datetime] = FieldInfo(alias="availableTime", default=None)
    """
    Time the loadmaster or boom operator is available for cargo loading/unloading,
    in ISO 8601 UTC format with millisecond precision.
    """

    basic_moment: Optional[float] = FieldInfo(alias="basicMoment", default=None)
    """
    The basic weight of the aircraft multiplied by the distance between the
    reference datum and the aircraft's center of gravity, in Newton-meters.
    """

    basic_weight: Optional[float] = FieldInfo(alias="basicWeight", default=None)
    """
    The weight of the aircraft without passengers, cargo, equipment, or usable fuel,
    in kilograms.
    """

    brief_time: Optional[datetime] = FieldInfo(alias="briefTime", default=None)
    """
    Time the cargo briefing was given to the loadmaster or boom operator, in ISO
    8601 UTC format with millisecond precision.
    """

    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign of the mission supporting this load plan."""

    cargo_bay_fs_max: Optional[float] = FieldInfo(alias="cargoBayFSMax", default=None)
    """Maximum fuselage station (FS) where cargo can be stored.

    FS is the distance from the reference datum, in meters.
    """

    cargo_bay_fs_min: Optional[float] = FieldInfo(alias="cargoBayFSMin", default=None)
    """Minimum fuselage station (FS) where cargo can be stored.

    FS is the distance from the reference datum, in meters.
    """

    cargo_bay_width: Optional[float] = FieldInfo(alias="cargoBayWidth", default=None)
    """Width of the cargo bay, in meters."""

    cargo_config: Optional[str] = FieldInfo(alias="cargoConfig", default=None)
    """The cargo configuration required for this leg (e.g.

    C-1, C-2, C-3, DV-1, DV-2, AE-1, etc.). Configuration meanings are determined by
    the data source.
    """

    cargo_moment: Optional[float] = FieldInfo(alias="cargoMoment", default=None)
    """The sum of cargo moments of all cargo on board the aircraft, in Newton-meters.

    Each individual cargo moment is the weight of the cargo multiplied by the
    distance between the reference datum and the cargo's center of gravity.
    """

    cargo_volume: Optional[float] = FieldInfo(alias="cargoVolume", default=None)
    """Volume of cargo space in the aircraft, in cubic meters."""

    cargo_weight: Optional[float] = FieldInfo(alias="cargoWeight", default=None)
    """The weight of the cargo on board the aircraft, in kilograms."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    crew_size: Optional[int] = FieldInfo(alias="crewSize", default=None)
    """The number of crew members on the aircraft."""

    dep_airfield: Optional[str] = FieldInfo(alias="depAirfield", default=None)
    """
    Optional identifier of departure airfield with no International Civil
    Organization (ICAO) code.
    """

    dep_icao: Optional[str] = FieldInfo(alias="depICAO", default=None)
    """
    The departure International Civil Organization (ICAO) code of the departure
    airfield.
    """

    equip_config: Optional[str] = FieldInfo(alias="equipConfig", default=None)
    """Description of the equipment configuration (e.g.

    Standard, Ferry, JBLM, CHS, Combat, etc.). Configuration meanings are determined
    by the data source.
    """

    est_arr_time: Optional[datetime] = FieldInfo(alias="estArrTime", default=None)
    """
    The current estimated time that the aircraft is planned to arrive, in ISO 8601
    UTC format with millisecond precision.
    """

    est_landing_fuel_moment: Optional[float] = FieldInfo(alias="estLandingFuelMoment", default=None)
    """
    The estimated weight of usable fuel upon landing multiplied by the distance
    between the reference datum and the fuel's center of gravity, in Newton-meters.
    """

    est_landing_fuel_weight: Optional[float] = FieldInfo(alias="estLandingFuelWeight", default=None)
    """The estimated weight of usable fuel upon landing, in kilograms."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Optional ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    fuel_moment: Optional[float] = FieldInfo(alias="fuelMoment", default=None)
    """
    The fuel weight on board the aircraft multiplied by the distance between the
    reference datum and the fuel's center of gravity, in Newton-meters.
    """

    fuel_weight: Optional[float] = FieldInfo(alias="fuelWeight", default=None)
    """The weight of usable fuel on board the aircraft, in kilograms."""

    gross_cg: Optional[float] = FieldInfo(alias="grossCG", default=None)
    """
    The center of gravity of the aircraft using the gross weight and gross moment,
    as a percentage of the mean aerodynamic chord (%MAC).
    """

    gross_moment: Optional[float] = FieldInfo(alias="grossMoment", default=None)
    """
    The sum of moments of all items making up the gross weight of the aircraft, in
    Newton-meters.
    """

    gross_weight: Optional[float] = FieldInfo(alias="grossWeight", default=None)
    """
    The total weight of the aircraft at takeoff including passengers, cargo,
    equipment, and usable fuel, in kilograms.
    """

    id_mission: Optional[str] = FieldInfo(alias="idMission", default=None)
    """The UDL ID of the mission this record is associated with."""

    id_sortie: Optional[str] = FieldInfo(alias="idSortie", default=None)
    """The UDL ID of the aircraft sortie this record is associated with."""

    landing_cg: Optional[float] = FieldInfo(alias="landingCG", default=None)
    """
    The center of gravity of the aircraft using the landing weight and landing
    moment, as a percentage of the mean aerodynamic chord (%MAC).
    """

    landing_moment: Optional[float] = FieldInfo(alias="landingMoment", default=None)
    """
    The sum of moments of all items making up the gross weight of the aircraft upon
    landing, in Newton-meters.
    """

    landing_weight: Optional[float] = FieldInfo(alias="landingWeight", default=None)
    """The gross weight of the aircraft upon landing, in kilograms."""

    leg_num: Optional[int] = FieldInfo(alias="legNum", default=None)
    """The leg number of the mission supporting this load plan."""

    loadmaster_name: Optional[str] = FieldInfo(alias="loadmasterName", default=None)
    """Name of the loadmaster or boom operator who received the cargo briefing."""

    loadmaster_rank: Optional[str] = FieldInfo(alias="loadmasterRank", default=None)
    """Rank of the loadmaster or boom operator overseeing cargo loading/unloading."""

    load_remarks: Optional[str] = FieldInfo(alias="loadRemarks", default=None)
    """Remarks concerning this load plan."""

    mission_number: Optional[str] = FieldInfo(alias="missionNumber", default=None)
    """The mission number of the mission supporting this load plan."""

    operating_moment: Optional[float] = FieldInfo(alias="operatingMoment", default=None)
    """
    The operating weight of the aircraft multiplied by the distance between the
    reference datum and the aircraft's center of gravity, in Newton-meters.
    """

    operating_weight: Optional[float] = FieldInfo(alias="operatingWeight", default=None)
    """
    The basic weight of the aircraft including passengers and equipment, in
    kilograms.
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

    pp_onboard: Optional[int] = FieldInfo(alias="ppOnboard", default=None)
    """Number of pallet positions on the aircraft."""

    pp_released: Optional[int] = FieldInfo(alias="ppReleased", default=None)
    """Number of pallet positions released this leg."""

    sched_time: Optional[datetime] = FieldInfo(alias="schedTime", default=None)
    """
    Time the loadmaster or boom operator is scheduled to begin overseeing cargo
    loading/unloading, in ISO 8601 UTC format with millisecond precision.
    """

    seats_onboard: Optional[int] = FieldInfo(alias="seatsOnboard", default=None)
    """Number of passenger seats on the aircraft."""

    seats_released: Optional[int] = FieldInfo(alias="seatsReleased", default=None)
    """Number of passenger seats released this leg."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    tail_number: Optional[str] = FieldInfo(alias="tailNumber", default=None)
    """The tail number of the aircraft supporting this load plan."""

    tank_config: Optional[str] = FieldInfo(alias="tankConfig", default=None)
    """Description of the fuel tank(s) configuration (e.g.

    ER, NON-ER, etc.). Configuration meanings are determined by the data source.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    util_code: Optional[str] = FieldInfo(alias="utilCode", default=None)
    """
    Alphanumeric code that describes general cargo-related utilization and
    characteristics for an itinerary point.
    """

    zero_fuel_cg: Optional[float] = FieldInfo(alias="zeroFuelCG", default=None)
    """
    The center of gravity of the aircraft using the zero fuel weight and zero fuel
    total moment, as a percentage of the mean aerodynamic chord (%MAC).
    """

    zero_fuel_moment: Optional[float] = FieldInfo(alias="zeroFuelMoment", default=None)
    """
    The zero fuel weight of the aircraft multiplied by the distance between the
    reference datum and the aircraft's center of gravity, in Newton-meters.
    """

    zero_fuel_weight: Optional[float] = FieldInfo(alias="zeroFuelWeight", default=None)
    """
    The operating weight of the aircraft including cargo, mail, baggage, and
    passengers, but without usable fuel, in kilograms.
    """
