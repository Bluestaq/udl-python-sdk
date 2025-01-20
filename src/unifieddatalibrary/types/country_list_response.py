# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .country_abridged import CountryAbridged

__all__ = ["CountryListResponse"]

CountryListResponse: TypeAlias = List[CountryAbridged]
