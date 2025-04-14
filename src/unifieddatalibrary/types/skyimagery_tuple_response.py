# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.skyimagery.skyimagery_full import SkyimageryFull

__all__ = ["SkyimageryTupleResponse"]

SkyimageryTupleResponse: TypeAlias = List[SkyimageryFull]
