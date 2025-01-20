# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .mission_ops.effect_request import EffectRequest

__all__ = ["EffectRequestTupleResponse"]

EffectRequestTupleResponse: TypeAlias = List[EffectRequest]
