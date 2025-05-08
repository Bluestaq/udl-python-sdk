# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryAodrParams"]


class HistoryAodrParams(TypedDict, total=False):
    columns: str
    """optional, fields for retrieval.

    When omitted, ALL fields are assumed. See the queryhelp operation
    (/udl/&lt;datatype&gt;/queryhelp) for more details on valid query fields that
    can be selected.
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    id_on_orbit: Annotated[str, PropertyInfo(alias="idOnOrbit")]
    """
    (One or more of fields 'idOnOrbit, startTime' are required.) Unique identifier
    of the target satellite on-orbit object. This ID can be used to obtain
    additional information on an OnOrbit object using the 'get by ID' operation
    (e.g. /udl/onorbit/{id}). For example, the OnOrbit with idOnOrbit = 25544 would
    be queried as /udl/onorbit/25544.
    """

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    notification: str
    """optional, notification method for the created file link.

    When omitted, EMAIL is assumed. Current valid values are: EMAIL, SMS.
    """

    output_delimiter: Annotated[str, PropertyInfo(alias="outputDelimiter")]
    """optional, field delimiter when the created file is not JSON.

    Must be a single character chosen from this set: (',', ';', ':', '|'). When
    omitted, "," is used. It is strongly encouraged that your field delimiter be a
    character unlikely to occur within the data.
    """

    output_format: Annotated[str, PropertyInfo(alias="outputFormat")]
    """optional, output format for the file.

    When omitted, JSON is assumed. Current valid values are: JSON and CSV.
    """

    start_time: Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]
    """
    (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
    solution in ISO 8601 UTC datetime format, with microsecond precision.
    (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """
