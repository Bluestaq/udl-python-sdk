# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventEvolutionListParams"]


class EventEvolutionListParams(TypedDict, total=False):
    event_id: Annotated[str, PropertyInfo(alias="eventId")]
    """
    (One or more of fields 'eventId, startTime' are required.) User-provided unique
    identifier of this activity or event. This ID should remain the same on
    subsequent updates in order to associate all records pertaining to the activity
    or event.
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    start_time: Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]
    """
    (One or more of fields 'eventId, startTime' are required.) The actual or
    estimated start time of the activity or event, in ISO 8601 UTC format.
    (YYYY-MM-DDTHH:MM:SS.sssZ)
    """
