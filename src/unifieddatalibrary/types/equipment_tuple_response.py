# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .equipment_full import EquipmentFull

__all__ = ["EquipmentTupleResponse"]

EquipmentTupleResponse: TypeAlias = List[EquipmentFull]
