# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SpaceEnvObservationListResponse", "SeoList"]


class SeoList(BaseModel):
    ob_type: str = FieldInfo(alias="obType")
    """The type of observation associated with this record."""

    ob_uo_m: str = FieldInfo(alias="obUoM")
    """The Unit of Measure associated with this observation.

    If there are no physical units associated with the measurement, a value of NONE
    should be specified.
    """

    ob_array: Optional[List[float]] = FieldInfo(alias="obArray", default=None)
    """
    An array of observation values expressed in the specified unit of measure
    (obUoM). Because of the variability of the Space Environment data types, each
    record may employ a numeric observation value (obValue), a string observation
    value (obString), a Boolean observation value (obBool), an array of numeric
    observation values (obArray), or any combination of these.
    """

    ob_bool: Optional[bool] = FieldInfo(alias="obBool", default=None)
    """A Boolean observation.

    Because of the variability of the Space Environment data types, each record may
    employ a numeric observation value (obValue), a string observation value
    (obString), a Boolean observation value (obBool), an array of numeric
    observation values (obArray), or any combination of these.
    """

    ob_description: Optional[str] = FieldInfo(alias="obDescription", default=None)
    """
    Descriptive or additional information associated with this individual
    observation.
    """

    ob_quality: Optional[str] = FieldInfo(alias="obQuality", default=None)
    """The quality of this individual observation.

    The observation quality indicator value may vary among providers and may be a
    generalized statement (BAD, GOOD, UNCERTAIN, UNKNOWN) or a numeric value. Users
    should consult the data provider to verify the usage of the observation.
    """

    ob_string: Optional[str] = FieldInfo(alias="obString", default=None)
    """A single observation string expressed in the specified unit of measure (obUoM).

    Because of the variability of the Space Environment data types, each record may
    employ a numeric observation value (obValue), a string observation value
    (obString), a Boolean observation value (obBool), an array of numeric
    observation values (obArray), or any combination of these.
    """

    ob_value: Optional[float] = FieldInfo(alias="obValue", default=None)
    """A single observation value expressed in the specified unit of measure (obUoM).

    Because of the variability of the Space Environment data types, each record may
    employ a numeric observation value (obValue), a string observation value
    (obString), a Boolean observation value (obBool), an array of numeric
    observation values (obArray), or any combination of these.
    """


class SpaceEnvObservationListResponse(BaseModel):
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

    ob_time: datetime = FieldInfo(alias="obTime")
    """Time of the observation, in ISO 8601 UTC format with millisecond precision."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    alt: Optional[float] = None
    """
    Spacecraft/sensor altitude at observation time, expressed in kilometers above
    WGS-84 ellipsoid.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    data_type: Optional[str] = FieldInfo(alias="dataType", default=None)
    """The data type (e.g.

    AP, AURORAL FLUX, ECP, KINDEX, PROPAGATED SOLAR WIND, XRAY FLUX, etc.) of
    observations in this record.
    """

    derived: Optional[bool] = None
    """Flag indicating that this record contains derived data."""

    description: Optional[str] = None
    """Descriptive or additional information associated with this observation record."""

    descriptor: Optional[str] = None
    """Optional source-provided and searchable metadata or descriptor of the data."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Optional ID from external systems.

    This field has no meaning within UDL and is provided as a convenience for
    systems that require tracking of an internal system generated ID.
    """

    forecast: Optional[bool] = None
    """Flag indicating that this record contains forecast data."""

    gen_system: Optional[str] = FieldInfo(alias="genSystem", default=None)
    """The external system which generated the message, if applicable."""

    gen_time: Optional[datetime] = FieldInfo(alias="genTime", default=None)
    """
    The time at which the associated data message was generated, in ISO 8601 UTC
    format with millisecond precision.
    """

    id_on_orbit: Optional[str] = FieldInfo(alias="idOnOrbit", default=None)
    """
    Unique identifier of the on-orbit satellite hosting the sensor which produced
    this data.
    """

    id_sensor: Optional[str] = FieldInfo(alias="idSensor", default=None)
    """Unique identifier of the reporting sensor."""

    instrument_type: Optional[str] = FieldInfo(alias="instrumentType", default=None)
    """The type of instrument from which this data was collected (e.g.

    ANTENNA, CHANNELTRON, INTERFEROMETER, MAGNETOMETER, RADIOMETER, etc.).
    """

    lat: Optional[float] = None
    """
    WGS-84 spacecraft/sensor latitude sub-point at observation time, represented as
    -90 to 90 degrees (negative values south of equator).
    """

    lon: Optional[float] = None
    """
    WGS-84 spacecraft/sensor longitude sub-point at observation time, represented as
    -180 to 180 degrees (negative values west of Prime Meridian).
    """

    meas_type: Optional[str] = FieldInfo(alias="measType", default=None)
    """The sensor measurement type of the observation data contained in this record."""

    msg_type: Optional[str] = FieldInfo(alias="msgType", default=None)
    """The type of message associated with this record."""

    observatory_name: Optional[str] = FieldInfo(alias="observatoryName", default=None)
    """The name of the observatory from which this data was collected."""

    observatory_notes: Optional[str] = FieldInfo(alias="observatoryNotes", default=None)
    """Additional notes concerning the observatory."""

    observatory_type: Optional[str] = FieldInfo(alias="observatoryType", default=None)
    """The type of observatory from which this data was collected (e.g.

    FACILITY, ONORBIT, NETWORK, etc.).
    """

    ob_set_id: Optional[str] = FieldInfo(alias="obSetId", default=None)
    """A user-defined name or ID of a set of observations, if applicable.

    Used for identifying multiple observation records as part of one observation
    set.
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

    orig_object_id: Optional[str] = FieldInfo(alias="origObjectId", default=None)
    """
    Optional identifier provided by the record source to indicate the satellite
    hosting the sensor which produced this data. This may be an internal identifier
    and not necessarily map to a valid satellite number.
    """

    orig_sensor_id: Optional[str] = FieldInfo(alias="origSensorId", default=None)
    """
    Optional identifier provided by the observation source to indicate the sensor
    which produced this observation. This may be an internal identifier and not
    necessarily a valid sensor ID.
    """

    particle_type: Optional[str] = FieldInfo(alias="particleType", default=None)
    """
    The particle type (AEROSOL, ALPHA PARTICLE, ATOM, DUST, ELECTRON, ION, MOLECULE,
    NEUTRON, POSITRON, PROTON) associated with this measurement.
    """

    quality: Optional[str] = None
    """The quality of the overall data contained in this record.

    The quality indicator value may vary among providers and may be a generalized
    statement (BAD, GOOD, UNCERTAIN, UNKNOWN) or a numeric value. Users should
    consult the data provider to verify the usage of the quality indicator.
    """

    sat_no: Optional[int] = FieldInfo(alias="satNo", default=None)
    """
    Satellite/catalog number of the on-orbit satellite hosting the sensor which
    produced this data.
    """

    sen_energy_level: Optional[str] = FieldInfo(alias="senEnergyLevel", default=None)
    """The energy level bin of the sensor associated with this measurement."""

    sen_pos: Optional[List[float]] = FieldInfo(alias="senPos", default=None)
    """
    Three element array, expressing the observing spacecraft/sensor position vector
    components at observation time, in kilometers, in the specified
    senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.
    The array element order is [xpos, ypos, zpos].
    """

    sen_reference_frame: Optional[Literal["J2000", "EFG/TDR", "ECR/ECEF", "TEME", "ITRF", "GCRF"]] = FieldInfo(
        alias="senReferenceFrame", default=None
    )
    """The reference frame of the observing spacecraft/sensor state.

    If the senReferenceFrame is null it is assumed to be J2000.
    """

    sen_vel: Optional[List[float]] = FieldInfo(alias="senVel", default=None)
    """
    Three element array, expressing the observing spacecraft/sensor velocity vector
    components at observation time, in kilometers/second, in the specified
    senReferenceFrame. If senReferenceFrame is null then J2000 should be assumed.
    The array element order is [xvel, yvel, zvel].
    """

    seo_list: Optional[List[SeoList]] = FieldInfo(alias="seoList", default=None)
    """A collection of individual space environment observations."""

    src_ids: Optional[List[str]] = FieldInfo(alias="srcIds", default=None)
    """
    Array of UUIDs of the UDL data records that are related to this observation
    record. See the associated 'srcTyps' array for specific types of data,
    positionally corresponding to the UUIDs in this array. The 'srcTyps' and
    'srcIds' arrays must match in size. See the corresponding srcTyps array element
    of the data type of the UUID and use the appropriate API operation to retrieve
    that object.
    """

    src_typs: Optional[List[str]] = FieldInfo(alias="srcTyps", default=None)
    """
    Array of UDL record types (AIS, CONJUNCTION, DOA, ELSET, EO, ESID, GROUNDIMAGE,
    POI, MANEUVER, MTI, NOTIFICATION, RADAR, RF, SGI, SIGACT, SKYIMAGE, SPACEENVOB,
    SV, TRACK) that are related to this observation record. See the associated
    'srcIds' array for the record UUIDs, positionally corresponding to the record
    types in this array. The 'srcTyps' and 'srcIds' arrays must match in size.
    """
