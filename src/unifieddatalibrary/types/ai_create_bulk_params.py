# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateBulkParams", "Body"]


class AICreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


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

    ts: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp that the vessel position was recorded, in ISO 8601 UTC format."""

    id: str
    """Unique identifier of the record, auto-generated by the system."""

    antenna_ref_dimensions: Annotated[Iterable[float], PropertyInfo(alias="antennaRefDimensions")]
    """The reference dimensions of the vessel, reported as [A, B, C, D], in meters.

    Where the array values represent the distance fore (A), aft (B), to port (C),
    and to starboard (D) of the navigation antenna. Array with values A = C = 0 and
    B, D > 0 indicate the length (B) and width (D) of the vessel without antenna
    position reference.
    """

    avg_speed: Annotated[float, PropertyInfo(alias="avgSpeed")]
    """
    The average speed, in kilometers/hour, calculated for the subject vessel during
    the latest voyage (port to port).
    """

    call_sign: Annotated[str, PropertyInfo(alias="callSign")]
    """A uniquely designated identifier for the vessel's transmitter station."""

    cargo_type: Annotated[str, PropertyInfo(alias="cargoType")]
    """The reported cargo type.

    Intended as, but not constrained to, the USCG NAVCEN AIS cargo definitions.
    Users should refer to USCG Navigation Center documentation for specific
    definitions associated with ship and cargo types. USCG NAVCEN documentation may
    be found at https://www.navcen.uscg.gov.
    """

    course: float
    """The course-over-ground reported by the vessel, in degrees."""

    current_port_guid: Annotated[str, PropertyInfo(alias="currentPortGUID")]
    """The US Geographic Unique Identifier of the current port hosting the vessel."""

    current_port_locode: Annotated[str, PropertyInfo(alias="currentPortLOCODE")]
    """The UN Location Code of the current port hosting the vessel."""

    destination: str
    """The destination of the vessel according to the AIS transmission."""

    destination_eta: Annotated[Union[str, datetime], PropertyInfo(alias="destinationETA", format="iso8601")]
    """
    The Estimated Time of Arrival of the vessel at the destination, in ISO 8601 UTC
    format.
    """

    distance_to_go: Annotated[float, PropertyInfo(alias="distanceToGo")]
    """
    The remaining distance, in kilometers, for the vessel to reach the reported
    destination.
    """

    distance_travelled: Annotated[float, PropertyInfo(alias="distanceTravelled")]
    """
    The distance, in kilometers, that the vessel has travelled since departing the
    last port.
    """

    draught: float
    """
    The maximum static draught, in meters, of the vessel according to the AIS
    transmission.
    """

    engaged_in: Annotated[str, PropertyInfo(alias="engagedIn")]
    """The activity that the vessel is engaged in.

    This entry applies only when the shipType = Other.
    """

    eta_calculated: Annotated[Union[str, datetime], PropertyInfo(alias="etaCalculated", format="iso8601")]
    """
    The Estimated Time of Arrival of the vessel at the destination port, according
    to MarineTraffic calculations, in ISO 8601 UTC format.
    """

    eta_updated: Annotated[Union[str, datetime], PropertyInfo(alias="etaUpdated", format="iso8601")]
    """
    The date and time that the ETA was calculated by MarineTraffic, in ISO 8601 UTC
    format.
    """

    id_track: Annotated[str, PropertyInfo(alias="idTrack")]
    """Unique identifier of the Track."""

    id_vessel: Annotated[str, PropertyInfo(alias="idVessel")]
    """Unique identifier of the vessel."""

    imon: int
    """The International Maritime Organization Number of the vessel.

    IMON is a seven-digit number that uniquely identifies the vessel.
    """

    last_port_guid: Annotated[str, PropertyInfo(alias="lastPortGUID")]
    """The US Geographic Unique Identifier of the last port visited by the vessel."""

    last_port_locode: Annotated[str, PropertyInfo(alias="lastPortLOCODE")]
    """The UN Location Code of the last port visited by the vessel."""

    lat: float
    """WGS-84 latitude of the vessel position, in degrees.

    -90 to 90 degrees (negative values south of equator).
    """

    length: float
    """The overall length of the vessel, in meters.

    A value of 511 indicates a vessel length of 511 meters or greater.
    """

    lon: float
    """WGS-84 longitude of the vessel position, in degrees.

    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    max_speed: Annotated[float, PropertyInfo(alias="maxSpeed")]
    """
    The maximum speed, in kilometers/hour, reported by the subject vessel during the
    latest voyage (port to port).
    """

    mmsi: int
    """The Maritime Mobile Service Identity of the vessel.

    MMSI is a nine-digit number that identifies the transmitter station of the
    vessel.
    """

    nav_status: Annotated[str, PropertyInfo(alias="navStatus")]
    """The AIS Navigational Status of the vessel (e.g.

    Underway Using Engine, Moored, Aground, etc.). Intended as, but not constrained
    to, the USCG NAVCEN navigation status definitions. Users should refer to USCG
    Navigation Center documentation for specific definitions associated with
    navigation status. USCG NAVCEN documentation may be found at
    https://www.navcen.uscg.gov.
    """

    next_port_guid: Annotated[str, PropertyInfo(alias="nextPortGUID")]
    """The US Geographic Unique Identifier of the next destination port of the vessel."""

    next_port_locode: Annotated[str, PropertyInfo(alias="nextPortLOCODE")]
    """The UN Location Code of the next destination port of the vessel."""

    origin: str
    """
    Originating system or organization which produced the data, if different from
    the source. The origin may be different than the source if the source was a
    mediating system which forwarded the data on behalf of the origin system. If
    null, the source may be assumed to be the origin.
    """

    pos_device_type: Annotated[str, PropertyInfo(alias="posDeviceType")]
    """The type of electronic position fixing device (e.g.

    GPS, GLONASS, etc.). Intended as, but not constrained to, the USCG NAVCEN
    electronic position fixing device definitions. Users should refer to USCG
    Navigation Center documentation for specific device type information. USCG
    NAVCEN documentation may be found at https://www.navcen.uscg.gov.
    """

    pos_hi_accuracy: Annotated[bool, PropertyInfo(alias="posHiAccuracy")]
    """
    Flag indicating high reported position accuracy (less than or equal to 10
    meters). A value of 0/false indicates low accuracy (greater than 10 meters).
    """

    pos_hi_latency: Annotated[bool, PropertyInfo(alias="posHiLatency")]
    """Flag indicating high reported position latency (greater than 5 seconds).

    A value of 0/false indicates low latency (less than 5 seconds).
    """

    rate_of_turn: Annotated[float, PropertyInfo(alias="rateOfTurn")]
    """The Rate-of-Turn for the vessel, in degrees/minute.

    Positive value indicates that the vessel is turning right.
    """

    ship_description: Annotated[str, PropertyInfo(alias="shipDescription")]
    """Further description or explanation of the vessel or type."""

    ship_name: Annotated[str, PropertyInfo(alias="shipName")]
    """The name of the vessel.

    Vessel names that exceed the AIS 20 character are shortened (not truncated) to
    15 character-spaces, followed by an underscore and the last 4 characters-spaces
    of the vessel full name.
    """

    ship_type: Annotated[str, PropertyInfo(alias="shipType")]
    """The reported ship type (e.g.

    Passenger, Tanker, Cargo, Other, etc.). See the engagedIn and specialCraft
    entries for additional information on certain types of vessels.
    """

    special_craft: Annotated[str, PropertyInfo(alias="specialCraft")]
    """The type of special craft designation of the vessel.

    This entry applies only when the shipType = Special Craft.
    """

    special_maneuver: Annotated[bool, PropertyInfo(alias="specialManeuver")]
    """Flag indicating that the vessel is engaged in a special maneuver (e.g.

    Waterway Navigation).
    """

    speed: float
    """The speed-over-ground reported by the vessel, in kilometers/hour."""

    true_heading: Annotated[float, PropertyInfo(alias="trueHeading")]
    """The true heading reported by the vessel, in degrees."""

    vessel_flag: Annotated[str, PropertyInfo(alias="vesselFlag")]
    """The flag of the subject vessel according to AIS transmission."""

    width: float
    """The breadth of the vessel, in meters.

    A value of 63 indicates a vessel breadth of 63 meters or greater.
    """
