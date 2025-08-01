# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.entity_full import EntityFull

__all__ = ["EntityTupleResponse"]

EntityTupleResponse: TypeAlias = List[EntityFull]
