# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AirloadPlanUpdateParams",
    "AirLoadPlanHazmatActual",
    "AirLoadPlanHr",
    "AirLoadPlanPalletDetail",
    "AirLoadPlanPaxCargo",
    "AirLoadPlanUlnActual",
]


class AirloadPlanUpdateParams(TypedDict, total=False):
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

    est_dep_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="estDepTime", format="iso8601")]]
    """
    The current estimated time that the aircraft is planned to depart, in ISO 8601
    UTC format with millisecond precision.
    """

    source: Required[str]
    """Source of the data."""

    body_id: Annotated[str, PropertyInfo(alias="id")]
    """Unique identifier of the record, auto-generated by the system."""

    acl_onboard: Annotated[float, PropertyInfo(alias="aclOnboard")]
    """Allowable Cabin Load (ACL) onboard the aircraft.

    The maximum weight of passengers, baggage, and cargo that can be safely
    transported in the aircraft cabin, in kilograms.
    """

    acl_released: Annotated[float, PropertyInfo(alias="aclReleased")]
    """Allowable Cabin Load (ACL) released this leg.

    The weight of passengers, baggage, and cargo released from the aircraft cabin,
    in kilograms.
    """

    aircraft_mds: Annotated[str, PropertyInfo(alias="aircraftMDS")]
    """The Model Design Series designation of the aircraft supporting this load plan."""

    air_load_plan_hazmat_actuals: Annotated[
        Iterable[AirLoadPlanHazmatActual], PropertyInfo(alias="airLoadPlanHazmatActuals")
    ]
    """Collection of hazmat actuals associated with this load plan."""

    air_load_plan_hr: Annotated[Iterable[AirLoadPlanHr], PropertyInfo(alias="airLoadPlanHR")]
    """
    Collection of human remains transport information associated with this load
    plan.
    """

    air_load_plan_pallet_details: Annotated[
        Iterable[AirLoadPlanPalletDetail], PropertyInfo(alias="airLoadPlanPalletDetails")
    ]
    """
    Collection of cargo information located at the pallet positions associated with
    this load plan.
    """

    air_load_plan_pax_cargo: Annotated[Iterable[AirLoadPlanPaxCargo], PropertyInfo(alias="airLoadPlanPaxCargo")]
    """
    Collection of passenger and cargo details associated with this load plan for
    this leg of the mission.
    """

    air_load_plan_uln_actuals: Annotated[Iterable[AirLoadPlanUlnActual], PropertyInfo(alias="airLoadPlanULNActuals")]
    """Collection of unit line number actuals associated with this load plan."""

    arr_airfield: Annotated[str, PropertyInfo(alias="arrAirfield")]
    """
    Optional identifier of arrival airfield with no International Civil Organization
    (ICAO) code.
    """

    arr_icao: Annotated[str, PropertyInfo(alias="arrICAO")]
    """
    The arrival International Civil Organization (ICAO) code of the landing
    airfield.
    """

    available_time: Annotated[Union[str, datetime], PropertyInfo(alias="availableTime", format="iso8601")]
    """
    Time the loadmaster or boom operator is available for cargo loading/unloading,
    in ISO 8601 UTC format with millisecond precision.
    """

    basic_moment: Annotated[float, PropertyInfo(alias="basicMoment")]
    """
    The basic weight of the aircraft multiplied by the distance between the
    reference datum and the aircraft's center of gravity, in Newton-meters.
    """

    basic_weight: Annotated[float, PropertyInfo(alias="basicWeight")]
    """
    The weight of the aircraft without passengers, cargo, equipment, or usable fuel,
    in kilograms.
    """

    brief_time: Annotated[Union[str, datetime], PropertyInfo(alias="briefTime", format="iso8601")]
    """
    Time the cargo briefing was given to the loadmaster or boom operator, in ISO
    8601 UTC format with millisecond precision.
    """

    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """The call sign of the mission supporting this load plan."""

    cargo_bay_fs_max: Annotated[float, PropertyInfo(alias="cargoBayFSMax")]
    """Maximum fuselage station (FS) where cargo can be stored.

    FS is the distance from the reference datum, in meters.
    """

    cargo_bay_fs_min: Annotated[float, PropertyInfo(alias="cargoBayFSMin")]
    """Minimum fuselage station (FS) where cargo can be stored.

    FS is the distance from the reference datum, in meters.
    """

    cargo_bay_width: Annotated[float, PropertyInfo(alias="cargoBayWidth")]
    """Width of the cargo bay, in meters."""

    cargo_config: Annotated[str, PropertyInfo(alias="cargoConfig")]
    """The cargo configuration required for this leg (e.g.

    C-1, C-2, C-3, DV-1, DV-2, AE-1, etc.). Configuration meanings are determined by
    the data source.
    """

    cargo_moment: Annotated[float, PropertyInfo(alias="cargoMoment")]
    """The sum of cargo moments of all cargo on board the aircraft, in Newton-meters.

    Each individual cargo moment is the weight of the cargo multiplied by the
    distance between the reference datum and the cargo's center of gravity.
    """

    cargo_volume: Annotated[float, PropertyInfo(alias="cargoVolume")]
    """Volume of cargo space in the aircraft, in cubic meters."""

    cargo_weight: Annotated[float, PropertyInfo(alias="cargoWeight")]
    """The weight of the cargo on board the aircraft, in kilograms."""

    crew_size: Annotated[int, PropertyInfo(alias="crewSize")]
    """The number of crew members on the aircraft."""

    dep_airfield: Annotated[str, PropertyInfo(alias="depAirfield")]
    """
    Optional identifier of departure airfield with no International Civil
    Organization (ICAO) code.
    """

    dep_icao: Annotated[str, PropertyInfo(alias="depICAO")]
    """
    The departure International Civil Organization (ICAO) code of the departure
    airfield.
    """

    equip_config: Annotated[str, PropertyInfo(alias="equipConfig")]
    """Description of the equipment configuration (e.g.

    Standard, Ferry, JBLM, CHS, Combat, etc.). Configuration meanings are determined
    by the data source.
    """

    est_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="estArrTime", format="iso8601")]
    """
    The current estimated time that the aircraft is planned to arrive, in ISO 8601
    UTC format with millisecond precision.
    """

    est_landing_fuel_moment: Annotated[float, PropertyInfo(alias="estLandingFuelMoment")]
    """
    The estimated weight of usable fuel upon landing multiplied by the distance
    between the reference datum and the fuel's center of gravity, in Newton-meters.
    """

    est_landing_fuel_weight: Annotated[float, PropertyInfo(alias="estLandingFuelWeight")]
    """The estimated weight of usable fuel upon landing, in kilograms."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """Optional ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    fuel_moment: Annotated[float, PropertyInfo(alias="fuelMoment")]
    """
    The fuel weight on board the aircraft multiplied by the distance between the
    reference datum and the fuel's center of gravity, in Newton-meters.
    """

    fuel_weight: Annotated[float, PropertyInfo(alias="fuelWeight")]
    """The weight of usable fuel on board the aircraft, in kilograms."""

    gross_cg: Annotated[float, PropertyInfo(alias="grossCG")]
    """
    The center of gravity of the aircraft using the gross weight and gross moment,
    as a percentage of the mean aerodynamic chord (%MAC).
    """

    gross_moment: Annotated[float, PropertyInfo(alias="grossMoment")]
    """
    The sum of moments of all items making up the gross weight of the aircraft, in
    Newton-meters.
    """

    gross_weight: Annotated[float, PropertyInfo(alias="grossWeight")]
    """
    The total weight of the aircraft at takeoff including passengers, cargo,
    equipment, and usable fuel, in kilograms.
    """

    id_mission: Annotated[str, PropertyInfo(alias="idMission")]
    """The UDL ID of the mission this record is associated with."""

    id_sortie: Annotated[str, PropertyInfo(alias="idSortie")]
    """The UDL ID of the aircraft sortie this record is associated with."""

    landing_cg: Annotated[float, PropertyInfo(alias="landingCG")]
    """
    The center of gravity of the aircraft using the landing weight and landing
    moment, as a percentage of the mean aerodynamic chord (%MAC).
    """

    landing_moment: Annotated[float, PropertyInfo(alias="landingMoment")]
    """
    The sum of moments of all items making up the gross weight of the aircraft upon
    landing, in Newton-meters.
    """

    landing_weight: Annotated[float, PropertyInfo(alias="landingWeight")]
    """The gross weight of the aircraft upon landing, in kilograms."""

    leg_num: Annotated[int, PropertyInfo(alias="legNum")]
    """The leg number of the mission supporting this load plan."""

    loadmaster_name: Annotated[str, PropertyInfo(alias="loadmasterName")]
    """Name of the loadmaster or boom operator who received the cargo briefing."""

    loadmaster_rank: Annotated[str, PropertyInfo(alias="loadmasterRank")]
    """Rank of the loadmaster or boom operator overseeing cargo loading/unloading."""

    load_remarks: Annotated[str, PropertyInfo(alias="loadRemarks")]
    """Remarks concerning this load plan."""

    mission_number: Annotated[str, PropertyInfo(alias="missionNumber")]
    """The mission number of the mission supporting this load plan."""

    operating_moment: Annotated[float, PropertyInfo(alias="operatingMoment")]
    """
    The operating weight of the aircraft multiplied by the distance between the
    reference datum and the aircraft's center of gravity, in Newton-meters.
    """

    operating_weight: Annotated[float, PropertyInfo(alias="operatingWeight")]
    """
    The basic weight of the aircraft including passengers and equipment, in
    kilograms.
    """

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    pp_onboard: Annotated[int, PropertyInfo(alias="ppOnboard")]
    """Number of pallet positions on the aircraft."""

    pp_released: Annotated[int, PropertyInfo(alias="ppReleased")]
    """Number of pallet positions released this leg."""

    sched_time: Annotated[Union[str, datetime], PropertyInfo(alias="schedTime", format="iso8601")]
    """
    Time the loadmaster or boom operator is scheduled to begin overseeing cargo
    loading/unloading, in ISO 8601 UTC format with millisecond precision.
    """

    seats_onboard: Annotated[int, PropertyInfo(alias="seatsOnboard")]
    """Number of passenger seats on the aircraft."""

    seats_released: Annotated[int, PropertyInfo(alias="seatsReleased")]
    """Number of passenger seats released this leg."""

    tail_number: Annotated[str, PropertyInfo(alias="tailNumber")]
    """The tail number of the aircraft supporting this load plan."""

    tank_config: Annotated[str, PropertyInfo(alias="tankConfig")]
    """Description of the fuel tank(s) configuration (e.g.

    ER, NON-ER, etc.). Configuration meanings are determined by the data source.
    """

    util_code: Annotated[str, PropertyInfo(alias="utilCode")]
    """
    Alphanumeric code that describes general cargo-related utilization and
    characteristics for an itinerary point.
    """

    zero_fuel_cg: Annotated[float, PropertyInfo(alias="zeroFuelCG")]
    """
    The center of gravity of the aircraft using the zero fuel weight and zero fuel
    total moment, as a percentage of the mean aerodynamic chord (%MAC).
    """

    zero_fuel_moment: Annotated[float, PropertyInfo(alias="zeroFuelMoment")]
    """
    The zero fuel weight of the aircraft multiplied by the distance between the
    reference datum and the aircraft's center of gravity, in Newton-meters.
    """

    zero_fuel_weight: Annotated[float, PropertyInfo(alias="zeroFuelWeight")]
    """
    The operating weight of the aircraft including cargo, mail, baggage, and
    passengers, but without usable fuel, in kilograms.
    """


class AirLoadPlanHazmatActual(TypedDict, total=False):
    ashc: str
    """
    The Air Special Handling Code (ASHC) indicates the type of special handling
    required for hazardous cargo.
    """

    cgc: str
    """
    Compatibility group code used to specify the controls for the transportation and
    storage of hazardous materials according to the Hazardous Materials Regulations
    issued by the U.S. Department of Transportation.
    """

    class_div: Annotated[str, PropertyInfo(alias="classDiv")]
    """
    Class and division of the hazardous material according to the Hazardous
    Materials Regulations issued by the U.S. Department of Transportation.
    """

    haz_description: Annotated[str, PropertyInfo(alias="hazDescription")]
    """Description of the hazardous item."""

    hazmat_remarks: Annotated[str, PropertyInfo(alias="hazmatRemarks")]
    """Remarks concerning this hazardous material."""

    haz_num: Annotated[str, PropertyInfo(alias="hazNum")]
    """
    United Nations number or North American number that identifies hazardous
    materials according to the Hazardous Materials Regulations issued by the U.S.
    Department of Transportation.
    """

    haz_num_type: Annotated[str, PropertyInfo(alias="hazNumType")]
    """
    Designates the type of hazmat number for the item (UN for United Nations or NA
    for North American).
    """

    haz_off_icao: Annotated[str, PropertyInfo(alias="hazOffICAO")]
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    hazardous material is unloaded.
    """

    haz_off_itin: Annotated[int, PropertyInfo(alias="hazOffItin")]
    """Itinerary number that identifies where the hazardous material is unloaded."""

    haz_on_icao: Annotated[str, PropertyInfo(alias="hazOnICAO")]
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    hazardous material is loaded.
    """

    haz_on_itin: Annotated[int, PropertyInfo(alias="hazOnItin")]
    """Itinerary number that identifies where the hazardous material is loaded."""

    haz_pieces: Annotated[int, PropertyInfo(alias="hazPieces")]
    """Number of pieces of hazardous cargo."""

    haz_tcn: Annotated[str, PropertyInfo(alias="hazTcn")]
    """Transportation Control Number (TCN) of the hazardous item."""

    haz_weight: Annotated[float, PropertyInfo(alias="hazWeight")]
    """Total weight of hazardous cargo, including non-explosive parts, in kilograms."""

    item_name: Annotated[str, PropertyInfo(alias="itemName")]
    """
    United Nations proper shipping name of the hazardous material according to the
    Hazardous Materials Regulations issued by the U.S. Department of Transportation.
    """

    lot_num: Annotated[str, PropertyInfo(alias="lotNum")]
    """Manufacturer's lot number for identification of the hazardous material."""

    net_exp_wt: Annotated[float, PropertyInfo(alias="netExpWt")]
    """Net explosive weight of the hazardous material, in kilograms."""


class AirLoadPlanHr(TypedDict, total=False):
    container: str
    """Type of transfer case used."""

    escort: str
    """Name of the escort for the remains."""

    hr_est_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="hrEstArrTime", format="iso8601")]
    """
    The current estimated time of arrival for the remains in ISO 8601 UTC format
    with millisecond precision.
    """

    hr_off_icao: Annotated[str, PropertyInfo(alias="hrOffICAO")]
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    remains are unloaded.
    """

    hr_off_itin: Annotated[int, PropertyInfo(alias="hrOffItin")]
    """Itinerary number that identifies where the remains are unloaded."""

    hr_on_icao: Annotated[str, PropertyInfo(alias="hrOnICAO")]
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    remains are loaded.
    """

    hr_on_itin: Annotated[int, PropertyInfo(alias="hrOnItin")]
    """Itinerary number that identifies where the remains are loaded."""

    hr_remarks: Annotated[str, PropertyInfo(alias="hrRemarks")]
    """Remarks concerning the remains."""

    name: str
    """Name of the deceased."""

    rank: str
    """Rank of the deceased."""

    rec_agency: Annotated[str, PropertyInfo(alias="recAgency")]
    """
    Name of the receiving agency or funeral home to which the remains are being
    delivered.
    """

    service: str
    """Branch of service of the deceased."""

    viewable: bool
    """Flag indicating if the remains are viewable."""


class AirLoadPlanPalletDetail(TypedDict, total=False):
    category: str
    """Category of special interest cargo."""

    pp: str
    """Pallet position of the cargo."""

    pp_description: Annotated[str, PropertyInfo(alias="ppDescription")]
    """Description of the cargo."""

    pp_off_icao: Annotated[str, PropertyInfo(alias="ppOffICAO")]
    """
    The International Civil Aviation Organization (ICAO) code of the site where the
    cargo is unloaded.
    """

    pp_pieces: Annotated[int, PropertyInfo(alias="ppPieces")]
    """Number of pieces included in the Transportation Control Number (TCN)."""

    pp_remarks: Annotated[str, PropertyInfo(alias="ppRemarks")]
    """Remarks concerning the cargo at this pallet position."""

    pp_tcn: Annotated[str, PropertyInfo(alias="ppTcn")]
    """Transportation Control Number (TCN) of the cargo."""

    pp_weight: Annotated[float, PropertyInfo(alias="ppWeight")]
    """Total weight of the cargo at this pallet position in kilograms."""

    special_interest: Annotated[bool, PropertyInfo(alias="specialInterest")]
    """Flag indicating if this cargo is considered special interest."""


class AirLoadPlanPaxCargo(TypedDict, total=False):
    amb_pax: Annotated[int, PropertyInfo(alias="ambPax")]
    """Number of ambulatory medical passengers in this group."""

    att_pax: Annotated[int, PropertyInfo(alias="attPax")]
    """Number of patient attendant passengers in this group."""

    available_pax: Annotated[int, PropertyInfo(alias="availablePax")]
    """Number of space available passengers in this group."""

    bag_weight: Annotated[float, PropertyInfo(alias="bagWeight")]
    """Weight of baggage in this group in kilograms."""

    civ_pax: Annotated[int, PropertyInfo(alias="civPax")]
    """Number of civilian passengers in this group."""

    dv_pax: Annotated[int, PropertyInfo(alias="dvPax")]
    """Number of distinguished visitor passengers in this group."""

    fn_pax: Annotated[int, PropertyInfo(alias="fnPax")]
    """Number of foreign national passengers in this group."""

    group_cargo_weight: Annotated[float, PropertyInfo(alias="groupCargoWeight")]
    """Weight of cargo in this group in kilograms."""

    group_type: Annotated[str, PropertyInfo(alias="groupType")]
    """
    Describes the status or action needed for this group of passenger and cargo data
    (e.g. ARRONBD, OFFTHIS, THROUGH, ONTHIS, DEPONBD, OFFNEXT).
    """

    lit_pax: Annotated[int, PropertyInfo(alias="litPax")]
    """Number of litter-bound passengers in this group."""

    mail_weight: Annotated[float, PropertyInfo(alias="mailWeight")]
    """Weight of mail in this group in kilograms."""

    num_pallet: Annotated[int, PropertyInfo(alias="numPallet")]
    """Number of cargo pallets in this group."""

    pallet_weight: Annotated[float, PropertyInfo(alias="palletWeight")]
    """Weight of pallets, chains, and devices in this group in kilograms."""

    pax_weight: Annotated[float, PropertyInfo(alias="paxWeight")]
    """Weight of passengers in this group in kilograms."""

    required_pax: Annotated[int, PropertyInfo(alias="requiredPax")]
    """Number of space required passengers in this group."""


class AirLoadPlanUlnActual(TypedDict, total=False):
    num_ambulatory: Annotated[int, PropertyInfo(alias="numAmbulatory")]
    """Number of ambulatory patients associated with this load plan."""

    num_attendant: Annotated[int, PropertyInfo(alias="numAttendant")]
    """Number of attendants associated with this load plan."""

    num_litter: Annotated[int, PropertyInfo(alias="numLitter")]
    """Number of litter patients associated with this load plan."""

    num_pax: Annotated[int, PropertyInfo(alias="numPax")]
    """Number of passengers associated with this load plan."""

    offload_id: Annotated[int, PropertyInfo(alias="offloadId")]
    """Identifier of the offload itinerary location."""

    offload_lo_code: Annotated[str, PropertyInfo(alias="offloadLOCode")]
    """Offload location code."""

    onload_id: Annotated[int, PropertyInfo(alias="onloadId")]
    """Identifier of the onload itinerary location."""

    onload_lo_code: Annotated[str, PropertyInfo(alias="onloadLOCode")]
    """Onload location code."""

    oplan: str
    """
    Identification number of the Operation Plan (OPLAN) associated with this load
    plan.
    """

    proj_name: Annotated[str, PropertyInfo(alias="projName")]
    """Project name."""

    uln: str
    """Unit line number."""

    uln_cargo_weight: Annotated[float, PropertyInfo(alias="ulnCargoWeight")]
    """Total weight of all cargo items for this unit line number in kilograms."""

    uln_remarks: Annotated[str, PropertyInfo(alias="ulnRemarks")]
    """Remarks concerning these unit line number actuals."""
