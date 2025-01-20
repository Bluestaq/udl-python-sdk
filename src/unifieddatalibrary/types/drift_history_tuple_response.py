# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.drift_history import DriftHistory

__all__ = ["DriftHistoryTupleResponse"]

DriftHistoryTupleResponse: TypeAlias = List[DriftHistory]
