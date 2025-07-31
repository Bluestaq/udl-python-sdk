# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.diplomaticclearance_full import DiplomaticclearanceFull

__all__ = ["DiplomaticClearanceTupleResponse"]

DiplomaticClearanceTupleResponse: TypeAlias = List[DiplomaticclearanceFull]
