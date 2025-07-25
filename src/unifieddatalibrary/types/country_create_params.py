# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CountryCreateParams"]


class CountryCreateParams(TypedDict, total=False):
    code: Required[str]
    """The country code.

    Optimally, this value is the ISO 3166 Alpha-2-two-character country code,
    however it can represent various consortiums that do not appear in the ISO
    document.
    """

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

    code_alt: Annotated[str, PropertyInfo(alias="codeAlt")]
    """3 Digit or other alternate country code."""

    fips_code: Annotated[str, PropertyInfo(alias="fipsCode")]
    """Federal Information Processing Standard (FIPS) two-character country code.

    This field is used when the country code for FIPS differs from the country code
    for ISO-3166 value. For example, the ISO-3166 Alpha-2-country code for Vanuatu
    is VU, whereas Vanuatu's FIPS equivalent country code is NH.
    """

    iso3_code: Annotated[str, PropertyInfo(alias="iso3Code")]
    """ISO 3166 Alpha-3 country code.

    This is a three-character code that represents a country name, which may be more
    closely related to the country name than its corresponding Alpha-2 code.
    """

    name: str
    """Country name."""
