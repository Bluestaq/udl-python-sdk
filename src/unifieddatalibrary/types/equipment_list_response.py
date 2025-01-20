# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .equipment_abridged import EquipmentAbridged

__all__ = ["EquipmentListResponse"]

EquipmentListResponse: TypeAlias = List[EquipmentAbridged]
