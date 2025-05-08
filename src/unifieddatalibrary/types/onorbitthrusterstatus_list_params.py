# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OnorbitthrusterstatusListParams"]


class OnorbitthrusterstatusListParams(TypedDict, total=False):
    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    id_onorbit_thruster: Annotated[str, PropertyInfo(alias="idOnorbitThruster")]
    """
    (One or more of fields 'idOnorbitThruster, statusTime' are required.) ID of the
    associated OnorbitThruster record. This ID can be used to obtain additional
    information on an onorbit thruster object using the 'get by ID' operation (e.g.
    /udl/onorbitthruster/{id}). For example, the OnorbitThruster object with
    idOnorbitThruster = abc would be queried as /udl/onorbitthruster/abc.
    """

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    status_time: Annotated[Union[str, datetime], PropertyInfo(alias="statusTime", format="iso8601")]
    """
    (One or more of fields 'idOnorbitThruster, statusTime' are required.) Datetime
    of the thruster status observation in ISO 8601 UTC datetime format with
    millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)
    """
