# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...udl.rfobservation.rfobservationdetails_full import RfobservationdetailsFull

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[RfobservationdetailsFull]
