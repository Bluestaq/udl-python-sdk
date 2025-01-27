# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AirEventCreateBulkParams", "Body", "BodyReceiver", "BodyRemark", "BodyTanker"]


class AirEventCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyReceiver(TypedDict, total=False):
    alt_receiver_mission_id: Annotated[str, PropertyInfo(alias="altReceiverMissionId")]
    """Alternate mission identifier of this receiver provided by source."""

    amc_receiver_mission_id: Annotated[str, PropertyInfo(alias="amcReceiverMissionId")]
    """The Air Mobility Command (AMC) mission identifier of this receiver."""

    external_receiver_id: Annotated[str, PropertyInfo(alias="externalReceiverId")]
    """Optional receiver identifier from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    fuel_on: Annotated[float, PropertyInfo(alias="fuelOn")]
    """
    Total weight of the fuel transferred to this receiver during an air refueling
    event, in pounds.
    """

    id_receiver_airfield: Annotated[str, PropertyInfo(alias="idReceiverAirfield")]
    """The UDL ID of the airfield this receiver is associated with for this event."""

    id_receiver_mission: Annotated[str, PropertyInfo(alias="idReceiverMission")]
    """The UDL ID of the mission this receiver is associated with for this event."""

    id_receiver_sortie: Annotated[str, PropertyInfo(alias="idReceiverSortie")]
    """
    The UDL ID of the aircraft sortie this receiver is associated with for this
    event.
    """

    num_rec_aircraft: Annotated[int, PropertyInfo(alias="numRecAircraft")]
    """
    Number of aircraft contained within one receiver coordination record for an air
    refueling event.
    """

    package_id: Annotated[str, PropertyInfo(alias="packageId")]
    """The package identifier for the receiver in an air refueling event."""

    receiver_call_sign: Annotated[str, PropertyInfo(alias="receiverCallSign")]
    """The call sign assigned to this receiver."""

    receiver_cell_position: Annotated[int, PropertyInfo(alias="receiverCellPosition")]
    """
    Position of this receiver within a group of receivers in an air refueling event.
    """

    receiver_coord: Annotated[str, PropertyInfo(alias="receiverCoord")]
    """Coordination record identifier of this receiver."""

    receiver_delivery_method: Annotated[str, PropertyInfo(alias="receiverDeliveryMethod")]
    """
    Type of fuel delivery method used by the receiver during an air refueling event
    (BOOM, DROGUE, BOTH).
    """

    receiver_deployed_icao: Annotated[str, PropertyInfo(alias="receiverDeployedICAO")]
    """Location the receiver is deployed to for an air refueling event."""

    receiver_exercise: Annotated[str, PropertyInfo(alias="receiverExercise")]
    """Name of the receiver exercise associated with an air refueling event."""

    receiver_fuel_type: Annotated[str, PropertyInfo(alias="receiverFuelType")]
    """Type of fuel being transferred to the receiver in an air refueling event."""

    receiver_leg_num: Annotated[int, PropertyInfo(alias="receiverLegNum")]
    """Identifies the itinerary point of a mission that this receiver is linked to."""

    receiver_mds: Annotated[str, PropertyInfo(alias="receiverMDS")]
    """The Model Design Series designation of this receiver."""

    receiver_owner: Annotated[str, PropertyInfo(alias="receiverOwner")]
    """The wing or unit that owns this receiver."""

    receiver_poc: Annotated[str, PropertyInfo(alias="receiverPOC")]
    """The name and/or number of the point of contact for this receiver."""

    rec_org: Annotated[str, PropertyInfo(alias="recOrg")]
    """
    The major command level (MAJCOM) or foreign military sales (FMS) name of the
    receiver's organization. The tanker flying hours used for an air refueling event
    are logged against the receiver MAJCOM or foreign government being supported.
    """

    sequence_num: Annotated[str, PropertyInfo(alias="sequenceNum")]
    """
    Indicates the unique number by Unit ID, which identifies an air refueling event.
    """


class BodyRemark(TypedDict, total=False):
    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Date the remark was published, in ISO 8601 UTC format, with millisecond
    precision.
    """

    external_remark_id: Annotated[str, PropertyInfo(alias="externalRemarkId")]
    """Optional remark ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    text: str
    """Text of the remark."""

    user: str
    """User who published the remark."""


class BodyTanker(TypedDict, total=False):
    alt_tanker_mission_id: Annotated[str, PropertyInfo(alias="altTankerMissionId")]
    """Alternate mission identifier of this tanker provided by source."""

    amc_tanker_mission_id: Annotated[str, PropertyInfo(alias="amcTankerMissionId")]
    """The Air Mobility Command (AMC) mission identifier of this tanker."""

    dual_role: Annotated[bool, PropertyInfo(alias="dualRole")]
    """
    Flag indicating that this tanker is flying a dual role mission in an air
    refueling event.
    """

    external_tanker_id: Annotated[str, PropertyInfo(alias="externalTankerId")]
    """Optional tanker identifier from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    fuel_off: Annotated[float, PropertyInfo(alias="fuelOff")]
    """
    Total weight of the fuel transferred from this tanker during an air refueling
    event, in pounds.
    """

    id_tanker_airfield: Annotated[str, PropertyInfo(alias="idTankerAirfield")]
    """The UDL ID of the airfield this tanker is associated with for this event."""

    id_tanker_mission: Annotated[str, PropertyInfo(alias="idTankerMission")]
    """The UDL ID of the mission this tanker is associated with for this event."""

    id_tanker_sortie: Annotated[str, PropertyInfo(alias="idTankerSortie")]
    """
    The UDL ID of the aircraft sortie this tanker is associated with for this event.
    """

    tanker_call_sign: Annotated[str, PropertyInfo(alias="tankerCallSign")]
    """The call sign assigned to this tanker."""

    tanker_cell_position: Annotated[int, PropertyInfo(alias="tankerCellPosition")]
    """Position of this tanker within a group of tankers in an air refueling event."""

    tanker_coord: Annotated[str, PropertyInfo(alias="tankerCoord")]
    """Coordination record identifier of this tanker."""

    tanker_delivery_method: Annotated[str, PropertyInfo(alias="tankerDeliveryMethod")]
    """
    Type of fuel delivery method used by the tanker during an air refueling event
    (BOOM, DROGUE, BOTH).
    """

    tanker_deployed_icao: Annotated[str, PropertyInfo(alias="tankerDeployedICAO")]
    """
    Location the tanker has been deployed to in preparation for an air refueling
    event.
    """

    tanker_fuel_type: Annotated[str, PropertyInfo(alias="tankerFuelType")]
    """Type of fuel being transferred from the tanker in an air refueling event."""

    tanker_leg_num: Annotated[int, PropertyInfo(alias="tankerLegNum")]
    """Identifies the itinerary point of a mission that this tanker is linked to."""

    tanker_mds: Annotated[str, PropertyInfo(alias="tankerMDS")]
    """The Model Design Series designation of this tanker."""

    tanker_owner: Annotated[str, PropertyInfo(alias="tankerOwner")]
    """The wing or unit that owns this tanker."""

    tanker_poc: Annotated[str, PropertyInfo(alias="tankerPOC")]
    """The name and/or number of the point of contact for this tanker."""


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

    type: Required[str]
    """Type of air event (e.g. FUEL TRANSFER, AIR DROP, etc)."""

    id: str
    """
    Unique identifier of the record, auto-generated by the system if not provided on
    create operations.
    """

    actual_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="actualArrTime", format="iso8601")]
    """
    The actual arrival time of the aircraft at the air event, in ISO 8601 UTC format
    with millisecond precision.
    """

    actual_dep_time: Annotated[Union[str, datetime], PropertyInfo(alias="actualDepTime", format="iso8601")]
    """
    The actual departure time of the aircraft from the air event, in ISO 8601 UTC
    format with millisecond precision.
    """

    arct: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The Air Refueling Control Time is the planned time the tanker aircraft will
    transfer fuel to the receiver aircraft, in ISO 8601 UTC format, with millisecond
    precision.
    """

    ar_event_type: Annotated[str, PropertyInfo(alias="arEventType")]
    """Type of process used by AMC to schedule this air refueling event.

    Possible values are A (Matched Long Range), F (Matched AMC Short Notice), N
    (Unmatched Theater Operation Short Notice (Theater Assets)), R, Unmatched Long
    Range, S (Soft Air Refueling), T (Matched Theater Operation Short Notice
    (Theater Assets)), V (Unmatched AMC Short Notice), X (Unmatched Theater
    Operation Short Notice (AMC Assets)), Y (Matched Theater Operation Short Notice
    (AMC Assets)), Z (Other Air Refueling).
    """

    arr_purpose: Annotated[str, PropertyInfo(alias="arrPurpose")]
    """The purpose of the air event at the arrival location.

    Can be either descriptive text such as 'fuel onload' or a purpose code specified
    by the provider, such as 'A'.
    """

    ar_track_id: Annotated[str, PropertyInfo(alias="arTrackId")]
    """Identifier of the air refueling track, if applicable."""

    ar_track_name: Annotated[str, PropertyInfo(alias="arTrackName")]
    """Name of the air refueling track, if applicable."""

    base_alt: Annotated[float, PropertyInfo(alias="baseAlt")]
    """Altitude of this air event, in feet."""

    cancelled: bool
    """Flag indicating that this air refueling event has been cancelled."""

    dep_purpose: Annotated[str, PropertyInfo(alias="depPurpose")]
    """The purpose of the air event at the departure location.

    Can be either descriptive text such as 'fuel onload' or a purpose code specified
    by the provider, such as 'A'.
    """

    est_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="estArrTime", format="iso8601")]
    """
    The current estimated arrival time of the aircraft at the air event, in ISO 8601
    UTC format with millisecond precision.
    """

    est_dep_time: Annotated[Union[str, datetime], PropertyInfo(alias="estDepTime", format="iso8601")]
    """
    The current estimated departure time of the aircraft from the air event, in ISO
    8601 UTC format with millisecond precision.
    """

    external_air_event_id: Annotated[str, PropertyInfo(alias="externalAirEventId")]
    """Optional air event ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    external_ar_track_id: Annotated[str, PropertyInfo(alias="externalARTrackId")]
    """Optional air refueling track ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    id_mission: Annotated[str, PropertyInfo(alias="idMission")]
    """The UDL unique identifier of the mission associated with this air event."""

    id_sortie: Annotated[str, PropertyInfo(alias="idSortie")]
    """The UDL unique identifier of the sortie associated with this air event."""

    leg_num: Annotated[int, PropertyInfo(alias="legNum")]
    """Identifies the Itinerary point of a sortie where an air event occurs."""

    location: str
    """The location representing this air event specified as a feature Id.

    Locations specified include air refueling track Ids and air drop event
    locations.
    """

    num_tankers: Annotated[int, PropertyInfo(alias="numTankers")]
    """The number of tankers requested for an air refueling event."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    planned_arr_time: Annotated[Union[str, datetime], PropertyInfo(alias="plannedArrTime", format="iso8601")]
    """
    The scheduled arrival time of the aircraft at the air event, in ISO 8601 UTC
    format with millisecond precision.
    """

    planned_dep_time: Annotated[Union[str, datetime], PropertyInfo(alias="plannedDepTime", format="iso8601")]
    """
    The scheduled departure time of the aircraft from the air event, in ISO 8601 UTC
    format with millisecond precision.
    """

    priority: str
    """Priority of this air event."""

    receivers: Iterable[BodyReceiver]
    """Collection of receiver aircraft associated with this Air Event."""

    remarks: Iterable[BodyRemark]
    """Collection of remarks associated with this Air Event."""

    rev_track: Annotated[bool, PropertyInfo(alias="revTrack")]
    """
    Flag indicating if the receiver unit has requested flying an air refueling track
    in both directions.
    """

    rzct: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The Rendezvous Control Time is the planned time the tanker and receiver aircraft
    will rendezvous for an en route type air refueling event, in ISO 8601 UTC
    format, with millisecond precision.
    """

    rz_point: Annotated[str, PropertyInfo(alias="rzPoint")]
    """Rendezvous point for the tanker and receiver during this air refueling event.

    Possible values are AN (Anchor Nav Point), AP (Anchor Pattern), CP (Control
    Point), ET (Entry Point), EX (Exit Point), IP (Initial Point), NC (Nav Check
    Point).
    """

    rz_type: Annotated[str, PropertyInfo(alias="rzType")]
    """Type of rendezvous used for this air refueling event.

    Possible values are BUD (Buddy), EN (Enroute), GCI (Ground Control), PP (Point
    Parallel).
    """

    short_track: Annotated[bool, PropertyInfo(alias="shortTrack")]
    """
    Flag indicating that the receiver unit has requested flying a short portion of
    an air refueling track.
    """

    status_code: Annotated[str, PropertyInfo(alias="statusCode")]
    """Status of this air refueling event track reservation.

    Receivers are responsible for scheduling or reserving air refueling tracks.
    Possible values are A (Altitude Reservation), R (Reserved), or Q (Questionable).
    """

    tankers: Iterable[BodyTanker]
    """Collection of tanker aircraft associated with this Air Event."""

    track_time: Annotated[float, PropertyInfo(alias="trackTime")]
    """Length of time the receiver unit has requested for an air event, in hours."""
