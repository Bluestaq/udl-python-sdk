# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DataownerAbridged"]


class DataownerAbridged(BaseModel):
    classification_marking: str = FieldInfo(alias="classificationMarking")
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    description: str
    """Description of this data owner."""

    do_name: str = FieldInfo(alias="doName")
    """The name of the data owner."""

    id_contact: str = FieldInfo(alias="idContact")
    """Unique identifier of the contact for this data owner."""

    source: str
    """Source of the data."""

    coming_soon: Optional[bool] = FieldInfo(alias="comingSoon", default=None)
    """Boolean indicating if the data owner is coming soon or not yet available."""

    control: Optional[str] = None
    """Optional control required to access this data type from this owner."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """The country code.

    This value is typically the ISO 3166 Alpha-2 two-character country code, however
    it can also represent various consortiums that do not appear in the ISO
    document. The code must correspond to an existing country in the UDL’s country
    API. Call udl/country/{code} to get any associated FIPS code, ISO Alpha-3 code,
    or alternate code values that exist for the specified country code.
    """

    data_type: Optional[str] = FieldInfo(alias="dataType", default=None)
    """Type of data this data owner owns (e.g. EPHEMERIS, IMAGERY, MANEUVER, etc.)."""

    enabled: Optional[bool] = None
    """
    Boolean indicating if the data owner is enabled (if not enabled, they should not
    appear on the data products screen on the storefront).
    """

    owner_type: Optional[str] = FieldInfo(alias="ownerType", default=None)
    """Type of organization which this data owner belongs to (e.g.

    Commercial, Government, Academic, Consortium, etc.).
    """

    provider: Optional[str] = None
    """Organization name for the data provider."""
