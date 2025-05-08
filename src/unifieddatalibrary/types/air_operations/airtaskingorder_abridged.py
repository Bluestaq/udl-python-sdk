# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AirtaskingorderAbridged",
    "AcMsnTasking",
    "AcMsnTaskingAcMsnLocSeg",
    "AcMsnTaskingIndAcTasking",
    "GenText",
    "NavalFltOp",
]


class AcMsnTaskingAcMsnLocSeg(BaseModel):
    start_time: datetime = FieldInfo(alias="startTime")
    """
    The start time of this mission in ISO 8601 UTC format with millisecond
    precision.
    """

    air_msn_pri: Optional[str] = FieldInfo(alias="airMsnPri", default=None)
    """The code for the priority assigned to this mission."""

    alt: Optional[int] = None
    """The altitude for this mission represented as hundreds of feet above MSL."""

    area_geo_rad: Optional[int] = FieldInfo(alias="areaGeoRad", default=None)
    """The radius of the circle around the location being reported in feet."""

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)
    """The end time of this mission in ISO 8601 UTC format with millisecond precision."""

    msn_loc_name: Optional[str] = FieldInfo(alias="msnLocName", default=None)
    """The name that identifies the location at which this mission is to be performed.

    This can be the name of a general target area, orbit, cap point, station, etc.
    """

    msn_loc_pt_bar_t: Optional[str] = FieldInfo(alias="msnLocPtBarT", default=None)
    """
    The alpha-numeric specified location for this mission specified as a bearing
    angle in degrees relative to true north and a range in nautical miles (NM).
    """

    msn_loc_pt_lat: Optional[float] = FieldInfo(alias="msnLocPtLat", default=None)
    """WGS-84 latitude of the mission location, in degrees.

    -90 to 90 degrees (negative values south of equator) for this tasked air
    mission.
    """

    msn_loc_pt_lon: Optional[float] = FieldInfo(alias="msnLocPtLon", default=None)
    """WGS-84 longitude of the mission location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian) for this tasked air
    mission.
    """

    msn_loc_pt_name: Optional[str] = FieldInfo(alias="msnLocPtName", default=None)
    """The location name for this mission."""


class AcMsnTaskingIndAcTasking(BaseModel):
    acft_type: str = FieldInfo(alias="acftType")
    """The type and model number for the aircraft.

    The field may specify a value of an aircraft not yet assigned an aircraft code
    contained in the aircraft codes list.
    """

    call_sign: Optional[str] = FieldInfo(alias="callSign", default=None)
    """The call sign assigned to this mission aircraft."""

    iff_sif_mode1_code: Optional[str] = FieldInfo(alias="iffSifMode1Code", default=None)
    """
    The mode 1 and code of the Identification Friend or FOE (IFF) or Selective
    Identification Feature (SIF).
    """

    iff_sif_mode2_code: Optional[str] = FieldInfo(alias="iffSifMode2Code", default=None)
    """
    The mode 2 and code of the Identification Friend or FOE (IFF) or Selective
    Identification Feature (SIF).
    """

    iff_sif_mode3_code: Optional[str] = FieldInfo(alias="iffSifMode3Code", default=None)
    """
    The mode 3 and code of the Identification Friend or FOE (IFF) or Selective
    Identification Feature (SIF).
    """

    ju_address: Optional[List[int]] = FieldInfo(alias="juAddress", default=None)
    """
    An optional array of link 16 octal track numbers assigned as the primary JTIDS
    Unit (JU) address for the mission aircraft.
    """

    link16_call_sign: Optional[str] = FieldInfo(alias="link16CallSign", default=None)
    """The Link 16 abbreviated call sign assigned to the ACA.

    This is normally the first and last letter and the last two numbers of the call
    sign.
    """

    num_acft: Optional[int] = FieldInfo(alias="numAcft", default=None)
    """The number of aircraft participating in this mission."""

    pri_config_code: Optional[str] = FieldInfo(alias="priConfigCode", default=None)
    """The code that indicates the ordinance mix carried on this mission aircraft."""

    sec_config_code: Optional[str] = FieldInfo(alias="secConfigCode", default=None)
    """The code for the secondary ordinance mix carried on this mission aircraft."""

    tacan_chan: Optional[int] = FieldInfo(alias="tacanChan", default=None)
    """The TACAN channel assigned to this mission aircraft."""


class AcMsnTasking(BaseModel):
    country_code: str = FieldInfo(alias="countryCode")
    """
    The country code responsible for conducting this aircraft mission tasking for
    the exercise or operation.
    """

    tasked_service: str = FieldInfo(alias="taskedService")
    """
    The service tasked with conducting this aircraft mission tasking for the
    exercise or operation.
    """

    unit_designator: str = FieldInfo(alias="unitDesignator")
    """
    The designator of the unit that is tasked to perform this aircraft mission
    tasking.
    """

    ac_msn_loc_seg: Optional[List[AcMsnTaskingAcMsnLocSeg]] = FieldInfo(alias="acMsnLocSeg", default=None)
    """
    A collection of aircraft mission location information for this aircraft mission
    tasking.
    """

    alert_status: Optional[int] = FieldInfo(alias="alertStatus", default=None)
    """
    The readiness status expressed in time (minutes) for an aircraft to be airborne
    after the launch order is received or the time required for a missile unit to
    assume battle stations.
    """

    amc_msn_num: Optional[str] = FieldInfo(alias="amcMsnNum", default=None)
    """The AMC number assigned to identify one aircraft from another."""

    dep_loc_lat: Optional[float] = FieldInfo(alias="depLocLat", default=None)
    """WGS-84 latitude of the departure location, in degrees.

    -90 to 90 degrees (negative values south of equator) for this tasked air
    mission.
    """

    dep_loc_lon: Optional[float] = FieldInfo(alias="depLocLon", default=None)
    """WGS-84 longitude of the departure location, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian) for this tasked air
    mission.
    """

    dep_loc_name: Optional[str] = FieldInfo(alias="depLocName", default=None)
    """The location or name specified for the departure of the tasked air mission."""

    dep_loc_utm: Optional[str] = FieldInfo(alias="depLocUTM", default=None)
    """
    The departure location specified in UTM (100 meter) coordinates for the tasked
    air mission.
    """

    dep_time: Optional[datetime] = FieldInfo(alias="depTime", default=None)
    """
    The time of departure for the tasked air mission in ISO8601 UTC format with
    millisecond precision.
    """

    ind_ac_tasking: Optional[List[AcMsnTaskingIndAcTasking]] = FieldInfo(alias="indACTasking", default=None)
    """
    A collection of the individual aircraft assigned to this aircraft mission
    tasking.
    """

    msn_commander: Optional[str] = FieldInfo(alias="msnCommander", default=None)
    """
    The commander responsible for the planning and execution of the forces necessary
    to achieve desired objectives.
    """

    msn_num: Optional[str] = FieldInfo(alias="msnNum", default=None)
    """The mission number assigned to this mission."""

    pkg_id: Optional[str] = FieldInfo(alias="pkgId", default=None)
    """The identifier for the composite set of missions for this operation/exercise."""

    pri_msn_type: Optional[str] = FieldInfo(alias="priMsnType", default=None)
    """The code for the preferred type or designator for a tasked air mission."""

    rcvy_loc_lat: Optional[List[float]] = FieldInfo(alias="rcvyLocLat", default=None)
    """An array of WGS-84 latitude of the recovery locations, in degrees.

    -90 to 90 degrees (negative values south of equator) for this tasked air
    mission.
    """

    rcvy_loc_lon: Optional[List[float]] = FieldInfo(alias="rcvyLocLon", default=None)
    """An array of WGS-84 longitude of the recovery locations, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian) for this tasked air
    mission.
    """

    rcvy_loc_name: Optional[List[str]] = FieldInfo(alias="rcvyLocName", default=None)
    """
    An array of locations specified for the recovery of the tasked air mission
    represented by varying formats.
    """

    rcvy_loc_utm: Optional[List[str]] = FieldInfo(alias="rcvyLocUTM", default=None)
    """
    An array of recovery locations specified in UTM (100 meter) coordinates for the
    tasked air mission.
    """

    rcvy_time: Optional[List[datetime]] = FieldInfo(alias="rcvyTime", default=None)
    """
    An array of recovery times for the tasked air mission in ISO8601 UTC format with
    millisecond precision.
    """

    res_msn_ind: Optional[str] = FieldInfo(alias="resMsnInd", default=None)
    """An indicator of whether a mission is or will be a residual mission."""

    sec_msn_type: Optional[str] = FieldInfo(alias="secMsnType", default=None)
    """The code for the alternative type of a tasked air mission."""

    unit_loc_name: Optional[str] = FieldInfo(alias="unitLocName", default=None)
    """The tasked units location expressed as an ICAO or a place name."""


class GenText(BaseModel):
    text: Optional[str] = None
    """The free text that describes the information specific to the text indicator."""

    text_ind: Optional[str] = FieldInfo(alias="textInd", default=None)
    """The indicator for the general text block.

    Examples include "OPENING REMARKS" and "GENERAL SPINS INFORMATION".
    """


class NavalFltOp(BaseModel):
    ship_name: str = FieldInfo(alias="shipName")
    """The name of a ship or maritime vessel. Specify UNKNOWN if name is not known."""

    flt_op_start: Optional[datetime] = FieldInfo(alias="fltOpStart", default=None)
    """
    The time when flight operations begin in ISO8601 UTC format with millisecond
    precision.
    """

    flt_op_stop: Optional[datetime] = FieldInfo(alias="fltOpStop", default=None)
    """
    The time when flight operations end in ISO8601 UTC format with millisecond
    precision.
    """

    schd_launch_rcvy_time: Optional[List[datetime]] = FieldInfo(alias="schdLaunchRcvyTime", default=None)
    """
    An array of times at which an aircraft will be launched and/or recovered in
    ISO8601 UTC format with millisecond precision.
    """


class AirtaskingorderAbridged(BaseModel):
    begin_ts: datetime = FieldInfo(alias="beginTs")
    """
    The effective begin time for this ATO in ISO 8601 UTC format with millisecond
    precision.
    """

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

    op_exer_name: str = FieldInfo(alias="opExerName")
    """
    Specifies the unique operation or exercise name, nickname, or codeword assigned
    to a joint exercise or operation plan.
    """

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    ack_req_ind: Optional[str] = FieldInfo(alias="ackReqInd", default=None)
    """
    The indicator specifying an affirmative or a negatice condition for this
    message.
    """

    ack_unit_instructions: Optional[str] = FieldInfo(alias="ackUnitInstructions", default=None)
    """
    Specifies textual data amplifying the data contained in the acknowledgement
    requirement indicator (ackRedInd) field or the unit required to acknowledge.
    """

    ac_msn_tasking: Optional[List[AcMsnTasking]] = FieldInfo(alias="acMsnTasking", default=None)
    """
    A collection that specifies the tasked country, tasked service, unit and mission
    level tasking for this ATO.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """Application user who created the row in the database."""

    end_ts: Optional[datetime] = FieldInfo(alias="endTs", default=None)
    """
    The effective end time for this ATO in ISO 8601 UTC format with millisecond
    precision.
    """

    gen_text: Optional[List[GenText]] = FieldInfo(alias="genText", default=None)
    """
    A collection that details special instructions, important information, guidance,
    and amplifying information regarding this ATO.
    """

    msg_month: Optional[str] = FieldInfo(alias="msgMonth", default=None)
    """The month in which the message originated."""

    msg_originator: Optional[str] = FieldInfo(alias="msgOriginator", default=None)
    """The identifier of the originator of the message."""

    msg_qualifier: Optional[str] = FieldInfo(alias="msgQualifier", default=None)
    """The qualifier which caveats the message status."""

    msg_sn: Optional[str] = FieldInfo(alias="msgSN", default=None)
    """The unique message identifier sequentially assigned by the originator."""

    naval_flt_ops: Optional[List[NavalFltOp]] = FieldInfo(alias="navalFltOps", default=None)
    """A collection that specifies the naval flight operations for this ATO."""

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

    raw_file_uri: Optional[str] = FieldInfo(alias="rawFileURI", default=None)
    """
    Optional URI location in the document repository of the raw file parsed by the
    system to produce this record. To download the raw file, prepend
    https://udl-hostname/scs/download?id= to this value.
    """

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """
