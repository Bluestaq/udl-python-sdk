# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.drifthistory_abridged import DrifthistoryAbridged

__all__ = ["DriftHistoryListResponse"]

DriftHistoryListResponse: TypeAlias = List[DrifthistoryAbridged]
