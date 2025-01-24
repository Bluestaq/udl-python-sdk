# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .weather_data_full import WeatherDataFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[WeatherDataFull]
