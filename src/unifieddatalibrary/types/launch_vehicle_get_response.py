# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .engine import Engine
from .._models import BaseModel
from .organization_full import OrganizationFull

__all__ = ["LaunchVehicleGetResponse", "LaunchVehicleDetail", "Stage"]


class LaunchVehicleDetail(BaseModel):
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

    id_launch_vehicle: str = FieldInfo(alias="idLaunchVehicle")
    """Identifier of the parent launch vehicle record."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    attitude_accuracy: Optional[float] = FieldInfo(alias="attitudeAccuracy", default=None)
    """Launch vehicle attitude accuracy (degrees)."""

    category: Optional[str] = None
    """Vehicle category."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    deployment_rotation_rate: Optional[float] = FieldInfo(alias="deploymentRotationRate", default=None)
    """Launch vehicle deployment rotation rate in RPM."""

    diameter: Optional[float] = None
    """Vehicle diameter in meters."""

    est_launch_price: Optional[float] = FieldInfo(alias="estLaunchPrice", default=None)
    """Launch vehicle estimated launch price in US dollars."""

    est_launch_price_typical: Optional[float] = FieldInfo(alias="estLaunchPriceTypical", default=None)
    """Launch vehicle typical estimated launch price in US dollars."""

    fairing_external_diameter: Optional[float] = FieldInfo(alias="fairingExternalDiameter", default=None)
    """Vehicle fairing maximum external diameter in meters."""

    fairing_internal_diameter: Optional[float] = FieldInfo(alias="fairingInternalDiameter", default=None)
    """Vehicle fairing maximum internal diameter in meters."""

    fairing_length: Optional[float] = FieldInfo(alias="fairingLength", default=None)
    """Vehicle fairing length in meters."""

    fairing_mass: Optional[float] = FieldInfo(alias="fairingMass", default=None)
    """Vehicle fairing mass in kg."""

    fairing_material: Optional[str] = FieldInfo(alias="fairingMaterial", default=None)
    """Fairing material."""

    fairing_name: Optional[str] = FieldInfo(alias="fairingName", default=None)
    """Name of the fairing."""

    fairing_notes: Optional[str] = FieldInfo(alias="fairingNotes", default=None)
    """Notes/Description of the launch vehicle fairing."""

    family: Optional[str] = None
    """Vehicle family."""

    geo_payload_mass: Optional[float] = FieldInfo(alias="geoPayloadMass", default=None)
    """Maximum vehicle payload mass to GEO orbit in kg."""

    gto_inj3_sig_accuracy_apogee_margin: Optional[float] = FieldInfo(
        alias="gtoInj3SigAccuracyApogeeMargin", default=None
    )
    """Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Margin (degrees)."""

    gto_inj3_sig_accuracy_apogee_target: Optional[float] = FieldInfo(
        alias="gtoInj3SigAccuracyApogeeTarget", default=None
    )
    """Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Target (degrees)."""

    gto_inj3_sig_accuracy_inclination_margin: Optional[float] = FieldInfo(
        alias="gtoInj3SigAccuracyInclinationMargin", default=None
    )
    """Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Margin (degrees)."""

    gto_inj3_sig_accuracy_inclination_target: Optional[float] = FieldInfo(
        alias="gtoInj3SigAccuracyInclinationTarget", default=None
    )
    """Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Target (degrees)."""

    gto_inj3_sig_accuracy_perigee_margin: Optional[float] = FieldInfo(
        alias="gtoInj3SigAccuracyPerigeeMargin", default=None
    )
    """Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Margin (degrees)."""

    gto_inj3_sig_accuracy_perigee_target: Optional[float] = FieldInfo(
        alias="gtoInj3SigAccuracyPerigeeTarget", default=None
    )
    """Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Target (degrees)."""

    gto_payload_mass: Optional[float] = FieldInfo(alias="gtoPayloadMass", default=None)
    """Max vehicle payload mass to Geo-Transfer Orbit in kg."""

    launch_mass: Optional[float] = FieldInfo(alias="launchMass", default=None)
    """Vehicle total mass at launch time in kg (including all boosters)."""

    launch_prefix: Optional[str] = FieldInfo(alias="launchPrefix", default=None)
    """Vehicle launch prefix."""

    length: Optional[float] = None
    """Vehicle length in meters."""

    leo_payload_mass: Optional[float] = FieldInfo(alias="leoPayloadMass", default=None)
    """Max vehicle payload mass to LEO orbit in kg."""

    manufacturer_org: Optional[OrganizationFull] = FieldInfo(alias="manufacturerOrg", default=None)
    """An organization such as a corporation, manufacturer, consortium, government,
    etc.

    An organization may have parent and child organizations as well as link to a
    former organization if this org previously existed as another organization.
    """

    manufacturer_org_id: Optional[str] = FieldInfo(alias="manufacturerOrgId", default=None)
    """ID of the organization that manufactures the launch vehicle."""

    max_accel_load: Optional[float] = FieldInfo(alias="maxAccelLoad", default=None)
    """Vehicle maximum acceleration load in g."""

    max_acoustic_level: Optional[float] = FieldInfo(alias="maxAcousticLevel", default=None)
    """Vehicle maximum acoustic level in dB."""

    max_acoustic_level_range: Optional[float] = FieldInfo(alias="maxAcousticLevelRange", default=None)
    """Vehicle maximum acoustic level range in Hz."""

    max_fairing_pressure_change: Optional[float] = FieldInfo(alias="maxFairingPressureChange", default=None)
    """Vehicle fairing maximum pressure change in kPa/sec."""

    max_flight_shock_force: Optional[float] = FieldInfo(alias="maxFlightShockForce", default=None)
    """Vehicle maximum flight shock force in g."""

    max_flight_shock_freq: Optional[float] = FieldInfo(alias="maxFlightShockFreq", default=None)
    """Vehicle maximum flight shock frequency in Hz."""

    max_payload_freq_lat: Optional[float] = FieldInfo(alias="maxPayloadFreqLat", default=None)
    """Vehicle maximum payload lateral frequency in Hz."""

    max_payload_freq_lon: Optional[float] = FieldInfo(alias="maxPayloadFreqLon", default=None)
    """Vehicle maximum payload longitudinal frequency in Hz."""

    minor_variant: Optional[str] = FieldInfo(alias="minorVariant", default=None)
    """Vehicle minor variant."""

    notes: Optional[str] = None
    """Notes/Description of the launch vehicle."""

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

    oxidizer: Optional[str] = None
    """Oxidizer type."""

    payload_notes: Optional[str] = FieldInfo(alias="payloadNotes", default=None)
    """Notes/Description of the launch vehicle payload."""

    payload_separation_rate: Optional[float] = FieldInfo(alias="payloadSeparationRate", default=None)
    """Launch vehicle payload separation rate in m/s."""

    propellant: Optional[str] = None
    """Propellant type."""

    sound_pressure_level: Optional[float] = FieldInfo(alias="soundPressureLevel", default=None)
    """Vehicle overall sound pressure level in dB."""

    source_url: Optional[str] = FieldInfo(alias="sourceURL", default=None)
    """Optional URL for additional information on the vehicle."""

    sso_payload_mass: Optional[float] = FieldInfo(alias="ssoPayloadMass", default=None)
    """Max vehicle payload mass to Sun-Synchronous Orbit in kg."""

    tags: Optional[List[str]] = None
    """
    Optional array of provider/source specific tags for this data, where each
    element is no longer than 32 characters, used for implementing data owner
    conditional access controls to restrict access to the data. Should be left null
    by data providers unless conditional access controls are coordinated with the
    UDL team.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was last updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    variant: Optional[str] = None
    """Vehicle variant."""


class Stage(BaseModel):
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

    id_engine: str = FieldInfo(alias="idEngine")
    """Identifier of the Engine record for this stage."""

    id_launch_vehicle: str = FieldInfo(alias="idLaunchVehicle")
    """Identifier of the launch vehicle record for this stage."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    avionics_notes: Optional[str] = FieldInfo(alias="avionicsNotes", default=None)
    """Description/notes of the stage avionics."""

    burn_time: Optional[float] = FieldInfo(alias="burnTime", default=None)
    """Total burn time of the stage engines in seconds."""

    control_thruster1: Optional[str] = FieldInfo(alias="controlThruster1", default=None)
    """Control thruster 1 type."""

    control_thruster2: Optional[str] = FieldInfo(alias="controlThruster2", default=None)
    """Control thruster 2 type."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    diameter: Optional[float] = None
    """Stage maximum external diameter in meters."""

    engine: Optional[Engine] = None
    """Known launch vehicle engines and their performance characteristics and limits.

    A launch vehicle has 1 to many engines per stage.
    """

    length: Optional[float] = None
    """Stage length in meters."""

    main_engine_thrust_sea_level: Optional[float] = FieldInfo(alias="mainEngineThrustSeaLevel", default=None)
    """Thrust of the stage main engine at sea level in kN."""

    main_engine_thrust_vacuum: Optional[float] = FieldInfo(alias="mainEngineThrustVacuum", default=None)
    """Thrust of the stage main engine in a vacuum in kN."""

    manufacturer_org_id: Optional[str] = FieldInfo(alias="manufacturerOrgId", default=None)
    """ID of the organization that manufactures this launch stage."""

    mass: Optional[float] = None
    """Stage gross mass in kg."""

    notes: Optional[str] = None
    """Description/notes of the stage."""

    num_burns: Optional[int] = FieldInfo(alias="numBurns", default=None)
    """Number of burns for the stage engines."""

    num_control_thruster1: Optional[int] = FieldInfo(alias="numControlThruster1", default=None)
    """Number of type control thruster 1."""

    num_control_thruster2: Optional[int] = FieldInfo(alias="numControlThruster2", default=None)
    """Number of type control thruster 2."""

    num_engines: Optional[int] = FieldInfo(alias="numEngines", default=None)
    """The number of the specified engines on this launch stage."""

    num_stage_elements: Optional[int] = FieldInfo(alias="numStageElements", default=None)
    """Number of launch stage elements used in this stage."""

    num_vernier: Optional[int] = FieldInfo(alias="numVernier", default=None)
    """Number of vernier or additional engines."""

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

    photo_urls: Optional[List[str]] = FieldInfo(alias="photoURLs", default=None)
    """Array of URLs of photos of the stage."""

    restartable: Optional[bool] = None
    """Boolean indicating if this launch stage can be restarted."""

    reusable: Optional[bool] = None
    """Boolean indicating if this launch stage is reusable."""

    stage_number: Optional[int] = FieldInfo(alias="stageNumber", default=None)
    """The stage number of this launch stage."""

    tags: Optional[List[str]] = None
    """
    Optional array of provider/source specific tags for this data, where each
    element is no longer than 32 characters, used for implementing data owner
    conditional access controls to restrict access to the data. Should be left null
    by data providers unless conditional access controls are coordinated with the
    UDL team.
    """

    thrust_sea_level: Optional[float] = FieldInfo(alias="thrustSeaLevel", default=None)
    """Total thrust of the stage at sea level in kN."""

    thrust_vacuum: Optional[float] = FieldInfo(alias="thrustVacuum", default=None)
    """Total thrust of the stage in a vacuum in kN."""

    type: Optional[str] = None
    """Engine cycle type (e.g.

    Electrostatic Ion, Pressure Fed, Hall, Catalytic Decomposition, etc.).
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was last updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """

    vernier: Optional[str] = None
    """Engine vernier or additional engine type."""

    vernier_burn_time: Optional[float] = FieldInfo(alias="vernierBurnTime", default=None)
    """Total burn time of the vernier or additional stage engines in seconds."""

    vernier_num_burns: Optional[int] = FieldInfo(alias="vernierNumBurns", default=None)
    """Total number of burns of the vernier or additional stage engines."""

    vernier_thrust_sea_level: Optional[float] = FieldInfo(alias="vernierThrustSeaLevel", default=None)
    """Total thrust of one of the vernier or additional engines at sea level in kN."""

    vernier_thrust_vacuum: Optional[float] = FieldInfo(alias="vernierThrustVacuum", default=None)
    """Total thrust of one of the vernier or additional engines in a vacuum in kN."""


class LaunchVehicleGetResponse(BaseModel):
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
    """Launch vehicle name."""

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

    launch_vehicle_details: Optional[List[LaunchVehicleDetail]] = FieldInfo(alias="launchVehicleDetails", default=None)
    """
    Read-only collection of additional LaunchVehicleDetails by various sources for
    this launch vehicle, ignored on create/update. These details must be created
    separately via the /udl/launchvehicledetails operations.
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

    stages: Optional[List[Stage]] = None
    """
    Read-only collection of stages for this launch vehicle, ignored on
    create/update.
    """

    type: Optional[str] = None
    """Vehicle type."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Time the row was last updated in the database, auto-populated by the system."""

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
    """
    Application user who updated the row in the database, auto-populated by the
    system.
    """
