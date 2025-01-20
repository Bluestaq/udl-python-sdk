# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..mission_ops.effect_request import EffectRequest

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[EffectRequest]
