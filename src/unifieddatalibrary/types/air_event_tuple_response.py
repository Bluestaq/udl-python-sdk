# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AirEventTupleResponse",
    "AirEventTupleResponseItem",
    "AirEventTupleResponseItemReceiver",
    "AirEventTupleResponseItemRemark",
    "AirEventTupleResponseItemTanker",
]


class AirEventTupleResponseItemReceiver(BaseModel):
    alt_receiver_mission_id: Optional[str] = FieldInfo(alias="altReceiverMissionId", default=None)
    """Alternate mission identifier of this receiver provided by source."""

    amc_receiver_mission_id: Optional[str] = FieldInfo(alias="amcReceiverMissionId", default=None)
    """The Air Mobility Command (AMC) mission identifier of this receiver."""

    external_receiver_id: Optional[str] = FieldInfo(alias="externalReceiverId", default=None)
    """Optional receiver identifier from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    fuel_on: Optional[float] = FieldInfo(alias="fuelOn", default=None)
    """
    Total weight of the fuel transferred to this receiver during an air refueling
    event, in pounds.
    """

    id_receiver_airfield: Optional[str] = FieldInfo(alias="idReceiverAirfield", default=None)
    """The UDL ID of the airfield this receiver is associated with for this event."""

    id_receiver_mission: Optional[str] = FieldInfo(alias="idReceiverMission", default=None)
    """The UDL ID of the mission this receiver is associated with for this event."""

    id_receiver_sortie: Optional[str] = FieldInfo(alias="idReceiverSortie", default=None)
    """
    The UDL ID of the aircraft sortie this receiver is associated with for this
    event.
    """

    num_rec_aircraft: Optional[int] = FieldInfo(alias="numRecAircraft", default=None)
    """
    Number of aircraft contained within one receiver coordination record for an air
    refueling event.
    """

    package_id: Optional[str] = FieldInfo(alias="packageId", default=None)
    """The package identifier for the receiver in an air refueling event."""

    receiver_call_sign: Optional[str] = FieldInfo(alias="receiverCallSign", default=None)
    """The call sign assigned to this receiver."""

    receiver_cell_position: Optional[int] = FieldInfo(alias="receiverCellPosition", default=None)
    """
    Position of this receiver within a group of receivers in an air refueling event.
    """

    receiver_coord: Optional[str] = FieldInfo(alias="receiverCoord", default=None)
    """Coordination record identifier of this receiver."""

    receiver_delivery_method: Optional[str] = FieldInfo(alias="receiverDeliveryMethod", default=None)
    """
    Type of fuel delivery method used by the receiver during an air refueling event
    (BOOM, DROGUE, BOTH).
    """

    receiver_deployed_icao: Optional[str] = FieldInfo(alias="receiverDeployedICAO", default=None)
    """Location the receiver is deployed to for an air refueling event."""

    receiver_exercise: Optional[str] = FieldInfo(alias="receiverExercise", default=None)
    """Name of the receiver exercise associated with an air refueling event."""

    receiver_fuel_type: Optional[str] = FieldInfo(alias="receiverFuelType", default=None)
    """Type of fuel being transferred to the receiver in an air refueling event."""

    receiver_leg_num: Optional[int] = FieldInfo(alias="receiverLegNum", default=None)
    """Identifies the itinerary point of a mission that this receiver is linked to."""

    receiver_mds: Optional[str] = FieldInfo(alias="receiverMDS", default=None)
    """The Model Design Series designation of this receiver."""

    receiver_owner: Optional[str] = FieldInfo(alias="receiverOwner", default=None)
    """The wing or unit that owns this receiver."""

    receiver_poc: Optional[str] = FieldInfo(alias="receiverPOC", default=None)
    """The name and/or number of the point of contact for this receiver."""

    rec_org: Optional[str] = FieldInfo(alias="recOrg", default=None)
    """
    The major command level (MAJCOM) or foreign military sales (FMS) name of the
    receiver's organization. The tanker flying hours used for an air refueling event
    are logged against the receiver MAJCOM or foreign government being supported.
    """

    sequence_num: Optional[str] = FieldInfo(alias="sequenceNum", default=None)
    """
    Indicates the unique number by Unit ID, which identifies an air refueling event.
    """


class AirEventTupleResponseItemRemark(BaseModel):
    date: Optional[datetime] = None
    """
    Date the remark was published, in ISO 8601 UTC format, with millisecond
    precision.
    """

    external_remark_id: Optional[str] = FieldInfo(alias="externalRemarkId", default=None)
    """Optional remark ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    text: Optional[str] = None
    """Text of the remark."""

    user: Optional[str] = None
    """User who published the remark."""


class AirEventTupleResponseItemTanker(BaseModel):
    alt_tanker_mission_id: Optional[str] = FieldInfo(alias="altTankerMissionId", default=None)
    """Alternate mission identifier of this tanker provided by source."""

    amc_tanker_mission_id: Optional[str] = FieldInfo(alias="amcTankerMissionId", default=None)
    """The Air Mobility Command (AMC) mission identifier of this tanker."""

    dual_role: Optional[bool] = FieldInfo(alias="dualRole", default=None)
    """
    Flag indicating that this tanker is flying a dual role mission in an air
    refueling event.
    """

    external_tanker_id: Optional[str] = FieldInfo(alias="externalTankerId", default=None)
    """Optional tanker identifier from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    fuel_off: Optional[float] = FieldInfo(alias="fuelOff", default=None)
    """
    Total weight of the fuel transferred from this tanker during an air refueling
    event, in pounds.
    """

    id_tanker_airfield: Optional[str] = FieldInfo(alias="idTankerAirfield", default=None)
    """The UDL ID of the airfield this tanker is associated with for this event."""

    id_tanker_mission: Optional[str] = FieldInfo(alias="idTankerMission", default=None)
    """The UDL ID of the mission this tanker is associated with for this event."""

    id_tanker_sortie: Optional[str] = FieldInfo(alias="idTankerSortie", default=None)
    """
    The UDL ID of the aircraft sortie this tanker is associated with for this event.
    """

    tanker_call_sign: Optional[str] = FieldInfo(alias="tankerCallSign", default=None)
    """The call sign assigned to this tanker."""

    tanker_cell_position: Optional[int] = FieldInfo(alias="tankerCellPosition", default=None)
    """Position of this tanker within a group of tankers in an air refueling event."""

    tanker_coord: Optional[str] = FieldInfo(alias="tankerCoord", default=None)
    """Coordination record identifier of this tanker."""

    tanker_delivery_method: Optional[str] = FieldInfo(alias="tankerDeliveryMethod", default=None)
    """
    Type of fuel delivery method used by the tanker during an air refueling event
    (BOOM, DROGUE, BOTH).
    """

    tanker_deployed_icao: Optional[str] = FieldInfo(alias="tankerDeployedICAO", default=None)
    """
    Location the tanker has been deployed to in preparation for an air refueling
    event.
    """

    tanker_fuel_type: Optional[str] = FieldInfo(alias="tankerFuelType", default=None)
    """Type of fuel being transferred from the tanker in an air refueling event."""

    tanker_leg_num: Optional[int] = FieldInfo(alias="tankerLegNum", default=None)
    """Identifies the itinerary point of a mission that this tanker is linked to."""

    tanker_mds: Optional[str] = FieldInfo(alias="tankerMDS", default=None)
    """The Model Design Series designation of this tanker."""

    tanker_owner: Optional[str] = FieldInfo(alias="tankerOwner", default=None)
    """The wing or unit that owns this tanker."""

    tanker_poc: Optional[str] = FieldInfo(alias="tankerPOC", default=None)
    """The name and/or number of the point of contact for this tanker."""


class AirEventTupleResponseItem(BaseModel):
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

    type: str
    """Type of air event (e.g. FUEL TRANSFER, AIR DROP, etc)."""

    id: Optional[str] = None
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    actual_arr_time: Optional[datetime] = FieldInfo(alias="actualArrTime", default=None)
    """
    The actual arrival time of the aircraft at the air event, in ISO 8601 UTC format
    with millisecond precision.
    """

    actual_dep_time: Optional[datetime] = FieldInfo(alias="actualDepTime", default=None)
    """
    The actual departure time of the aircraft from the air event, in ISO 8601 UTC
    format with millisecond precision.
    """

    arct: Optional[datetime] = None
    """
    The Air Refueling Control Time is the planned time the tanker aircraft will
    transfer fuel to the receiver aircraft, in ISO 8601 UTC format, with millisecond
    precision.
    """

    ar_event_type: Optional[str] = FieldInfo(alias="arEventType", default=None)
    """Type of process used by AMC to schedule this air refueling event.

    Possible values are A (Matched Long Range), F (Matched AMC Short Notice), N
    (Unmatched Theater Operation Short Notice (Theater Assets)), R, Unmatched Long
    Range, S (Soft Air Refueling), T (Matched Theater Operation Short Notice
    (Theater Assets)), V (Unmatched AMC Short Notice), X (Unmatched Theater
    Operation Short Notice (AMC Assets)), Y (Matched Theater Operation Short Notice
    (AMC Assets)), Z (Other Air Refueling).
    """

    arr_purpose: Optional[str] = FieldInfo(alias="arrPurpose", default=None)
    """The purpose of the air event at the arrival location.

    Can be either descriptive text such as 'fuel onload' or a purpose code specified
    by the provider, such as 'A'.
    """

    ar_track_id: Optional[str] = FieldInfo(alias="arTrackId", default=None)
    """Identifier of the air refueling track, if applicable."""

    ar_track_name: Optional[str] = FieldInfo(alias="arTrackName", default=None)
    """Name of the air refueling track, if applicable."""

    base_alt: Optional[float] = FieldInfo(alias="baseAlt", default=None)
    """Altitude of this air event, in feet."""

    cancelled: Optional[bool] = None
    """Flag indicating that this air refueling event has been cancelled."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    dep_purpose: Optional[str] = FieldInfo(alias="depPurpose", default=None)
    """The purpose of the air event at the departure location.

    Can be either descriptive text such as 'fuel onload' or a purpose code specified
    by the provider, such as 'A'.
    """

    est_arr_time: Optional[datetime] = FieldInfo(alias="estArrTime", default=None)
    """
    The current estimated arrival time of the aircraft at the air event, in ISO 8601
    UTC format with millisecond precision.
    """

    est_dep_time: Optional[datetime] = FieldInfo(alias="estDepTime", default=None)
    """
    The current estimated departure time of the aircraft from the air event, in ISO
    8601 UTC format with millisecond precision.
    """

    external_air_event_id: Optional[str] = FieldInfo(alias="externalAirEventId", default=None)
    """Optional air event ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    external_ar_track_id: Optional[str] = FieldInfo(alias="externalARTrackId", default=None)
    """Optional air refueling track ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    id_mission: Optional[str] = FieldInfo(alias="idMission", default=None)
    """The UDL unique identifier of the mission associated with this air event."""

    id_sortie: Optional[str] = FieldInfo(alias="idSortie", default=None)
    """The UDL unique identifier of the sortie associated with this air event."""

    leg_num: Optional[int] = FieldInfo(alias="legNum", default=None)
    """Identifies the Itinerary point of a sortie where an air event occurs."""

    location: Optional[str] = None
    """The location representing this air event specified as a feature Id.

    Locations specified include air refueling track Ids and air drop event
    locations.
    """

    num_tankers: Optional[int] = FieldInfo(alias="numTankers", default=None)
    """The number of tankers requested for an air refueling event."""

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

    planned_arr_time: Optional[datetime] = FieldInfo(alias="plannedArrTime", default=None)
    """
    The scheduled arrival time of the aircraft at the air event, in ISO 8601 UTC
    format with millisecond precision.
    """

    planned_dep_time: Optional[datetime] = FieldInfo(alias="plannedDepTime", default=None)
    """
    The scheduled departure time of the aircraft from the air event, in ISO 8601 UTC
    format with millisecond precision.
    """

    priority: Optional[str] = None
    """Priority of this air event."""

    receivers: Optional[List[AirEventTupleResponseItemReceiver]] = None
    """Collection of receiver aircraft associated with this Air Event."""

    remarks: Optional[List[AirEventTupleResponseItemRemark]] = None
    """Collection of remarks associated with this Air Event."""

    rev_track: Optional[bool] = FieldInfo(alias="revTrack", default=None)
    """
    Flag indicating if the receiver unit has requested flying an air refueling track
    in both directions.
    """

    rzct: Optional[datetime] = None
    """
    The Rendezvous Control Time is the planned time the tanker and receiver aircraft
    will rendezvous for an en route type air refueling event, in ISO 8601 UTC
    format, with millisecond precision.
    """

    rz_point: Optional[str] = FieldInfo(alias="rzPoint", default=None)
    """Rendezvous point for the tanker and receiver during this air refueling event.

    Possible values are AN (Anchor Nav Point), AP (Anchor Pattern), CP (Control
    Point), ET (Entry Point), EX (Exit Point), IP (Initial Point), NC (Nav Check
    Point).
    """

    rz_type: Optional[str] = FieldInfo(alias="rzType", default=None)
    """Type of rendezvous used for this air refueling event.

    Possible values are BUD (Buddy), EN (Enroute), GCI (Ground Control), PP (Point
    Parallel).
    """

    short_track: Optional[bool] = FieldInfo(alias="shortTrack", default=None)
    """
    Flag indicating that the receiver unit has requested flying a short portion of
    an air refueling track.
    """

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    status_code: Optional[str] = FieldInfo(alias="statusCode", default=None)
    """Status of this air refueling event track reservation.

    Receivers are responsible for scheduling or reserving air refueling tracks.
    Possible values are A (Altitude Reservation), R (Reserved), or Q (Questionable).
    """

    tankers: Optional[List[AirEventTupleResponseItemTanker]] = None
    """Collection of tanker aircraft associated with this Air Event."""

    track_time: Optional[float] = FieldInfo(alias="trackTime", default=None)
    """Length of time the receiver unit has requested for an air event, in hours."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """


AirEventTupleResponse: TypeAlias = List[AirEventTupleResponseItem]
