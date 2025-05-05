# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .weather_data.weather_data_full import WeatherDataFull

__all__ = ["WeatherDataTupleResponse"]

WeatherDataTupleResponse: TypeAlias = List[WeatherDataFull]
