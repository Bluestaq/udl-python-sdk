# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .country_full import CountryFull

__all__ = ["CountryTupleResponse"]

CountryTupleResponse: TypeAlias = List[CountryFull]
