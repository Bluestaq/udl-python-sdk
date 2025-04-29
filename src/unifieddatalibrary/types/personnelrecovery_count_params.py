# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonnelrecoveryCountParams"]


class PersonnelrecoveryCountParams(TypedDict, total=False):
    msg_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="msgTime", format="iso8601")]]
    """Time stamp of the original personnel recovery message, in ISO 8601 UTC format.

    (YYYY-MM-DDTHH:MM:SS.sssZ)
    """

    first_result: Annotated[int, PropertyInfo(alias="firstResult")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
