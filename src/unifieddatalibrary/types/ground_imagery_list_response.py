# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GroundImageryListResponse"]


class GroundImageryListResponse(BaseModel):
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

    filename: str
    """Name of the image file."""

    image_time: datetime = FieldInfo(alias="imageTime")
    """Timestamp the image was captured/produced."""

    source: str
    """Source of the data."""

    id: Optional[str] = None
    """Unique identifier of the record, auto-generated by the system."""

    checksum_value: Optional[str] = FieldInfo(alias="checksumValue", default=None)
    """MD5 value of the file.

    The ingest/create operation will automatically generate the value.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time the row was created in the database, auto-populated by the system."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """
    Application user who created the row in the database, auto-populated by the
    system.
    """

    filesize: Optional[int] = None
    """Size of the image file.

    Units in bytes. If filesize is provided without an associated file, it defaults
    to 0.
    """

    format: Optional[str] = None
    """Optional, field indicating type of image, NITF, PNG, etc."""

    id_sensor: Optional[str] = FieldInfo(alias="idSensor", default=None)
    """Optional ID of the sensor that produced this ground image."""

    name: Optional[str] = None
    """Optional name/description associated with this image."""

    notes: Optional[str] = None
    """Description and notes of the image."""

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

    orig_sensor_id: Optional[str] = FieldInfo(alias="origSensorId", default=None)
    """
    Optional identifier provided by source to indicate the sensor identifier used to
    detect this event. This may be an internal identifier and not necessarily a
    valid sensor ID.
    """

    region_geo_json: Optional[str] = FieldInfo(alias="regionGeoJSON", default=None)
    """
    Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
    representation of the geometry/geography, of the image as projected on the
    ground. Reference: https://geojson.org/. Ignored if included with a create
    operation that also specifies a valid region or regionText.
    """

    region_n_dims: Optional[int] = FieldInfo(alias="regionNDims", default=None)
    """Number of dimensions of the geometry depicted by region."""

    region_s_rid: Optional[int] = FieldInfo(alias="regionSRid", default=None)
    """Geographical spatial_ref_sys for region."""

    region_text: Optional[str] = FieldInfo(alias="regionText", default=None)
    """
    Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
    Text representation of the geometry/geography, of the image as projected on the
    ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
    if included with a create operation that also specifies a valid region.
    """

    region_type: Optional[str] = FieldInfo(alias="regionType", default=None)
    """Type of region as projected on the ground."""

    source_dl: Optional[str] = FieldInfo(alias="sourceDL", default=None)
    """The source data library from which this record was received.

    This could be a remote or tactical UDL or another data library. If null, the
    record should be assumed to have originated from the primary Enterprise UDL.
    """

    subject_id: Optional[str] = FieldInfo(alias="subjectId", default=None)
    """
    Optional identifier of the subject/target of the image, useful for correlating
    multiple images of the same subject.
    """

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """
    Optional identifier to track a commercial or marketplace transaction executed to
    produce this data.
    """
