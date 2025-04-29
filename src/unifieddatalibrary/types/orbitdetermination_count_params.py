# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrbitdeterminationCountParams"]


class OrbitdeterminationCountParams(TypedDict, total=False):
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

    start_time: Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]
    """
    (One or more of fields 'idOnOrbit, startTime' are required.) Start time for OD
    solution in ISO 8601 UTC datetime format, with microsecond precision.
    (YYYY-MM-DDTHH:MM:SS.ssssssZ)
    """
