# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EphemerisFileUploadParams"]


class EphemerisFileUploadParams(TypedDict, total=False):
    category: Required[str]
    """Ephemeris category."""

    classification: Required[str]
    """Classification marking of the data in IC/CAPCO Portion-marked format."""

    data_mode: Required[Annotated[Literal["REAL", "TEST", "SIMULATED", "EXERCISE"], PropertyInfo(alias="dataMode")]]
    """Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data."""

    ephem_format_type: Required[
        Annotated[Literal["ModITC", "GOO", "NASA", "OEM", "OASYS"], PropertyInfo(alias="ephemFormatType")]
    ]
    """Ephemeris format as documented in Flight Safety Handbook."""

    has_mnvr: Required[Annotated[bool, PropertyInfo(alias="hasMnvr")]]
    """Boolean indicating whether maneuver(s) are incorporated into the ephemeris."""

    sat_no: Required[Annotated[int, PropertyInfo(alias="satNo")]]
    """Satellite/Catalog number of the target on-orbit object."""

    source: Required[str]
    """Source of the Ephemeris data."""

    type: Required[str]
    """Ephemeris type."""

    body: Required[str]

    origin: str
    """Optional origin of the Ephemeris."""

    tags: str
    """
    Optional array of provider/source specific tags for this data, where each
    element is no longer than 32 characters, used for implementing data owner
    conditional access controls to restrict access to the data. Should be left null
    by data providers unless conditional access controls are coordinated with the
    UDL team.
    """
