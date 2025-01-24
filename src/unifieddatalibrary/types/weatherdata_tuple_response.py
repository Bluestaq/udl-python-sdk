# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .weatherdata.weather_data_full import WeatherDataFull

__all__ = ["WeatherdataTupleResponse"]

WeatherdataTupleResponse: TypeAlias = List[WeatherDataFull]
