# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .entity_full import EntityFull

__all__ = ["AircraftFull"]


class AircraftFull(BaseModel):
    aircraft_mds: str = FieldInfo(alias="aircraftMDS")
    """The aircraft Model Design Series (MDS) designation (e.g.

    E-2C HAWKEYE, F-15 EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as,
    but not constrained to, MIL-STD-6016 environment dependent specific type
    designations.
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

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    category: Optional[str] = None
    """The category of aircraft (e.g. M = Military, C = Commercial)."""

    command: Optional[str] = None
    """The Air Force major command (MAJCOM) overseeing the aircraft."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    cruise_speed: Optional[float] = FieldInfo(alias="cruiseSpeed", default=None)
    """The cruise speed of the aircraft, in kilometers/hour."""

    dtd: Optional[str] = None
    """Military data network data transfer device ID for this aircraft."""

    entity: Optional[EntityFull] = None
    """
    An entity is a generic representation of any object within a space/SSA system
    such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
    entity can have an operating unit, a location (if terrestrial), and statuses.
    """

    id_entity: Optional[str] = FieldInfo(alias="idEntity", default=None)
    """ID of the parent entity for this aircraft."""

    max_speed: Optional[float] = FieldInfo(alias="maxSpeed", default=None)
    """The maximum air speed of the aircraft, in kilometers/hour."""

    min_req_runway_ft: Optional[int] = FieldInfo(alias="minReqRunwayFt", default=None)
    """The minimum length of runway required to land this aircraft, in feet.

    Note: The corresponding equivalent field is not converted by the UDL and may or
    may not be supplied by the provider. The provider/consumer is responsible for
    all unit conversions.
    """

    min_req_runway_m: Optional[int] = FieldInfo(alias="minReqRunwayM", default=None)
    """The minimum length of runway required to land this aircraft, in meters.

    Note: The corresponding equivalent field is not converted by the UDL and may or
    may not be supplied by the provider. The provider/consumer is responsible for
    all unit conversions.
    """

    nominal_ta_time: Optional[int] = FieldInfo(alias="nominalTATime", default=None)
    """The nominal turnaround time for this aircraft, in minutes."""

    notes: Optional[str] = None
    """Optional notes/comments for this aircraft."""

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

    owner: Optional[str] = None
    """The wing or unit that owns the aircraft."""

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """Full serial number of the aircraft."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    tail_number: Optional[str] = FieldInfo(alias="tailNumber", default=None)
    """The tail number of this aircraft."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
