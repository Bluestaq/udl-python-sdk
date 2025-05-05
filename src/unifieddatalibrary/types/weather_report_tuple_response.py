# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .weather_report.weather_report_full import WeatherReportFull

__all__ = ["WeatherReportTupleResponse"]

WeatherReportTupleResponse: TypeAlias = List[WeatherReportFull]
