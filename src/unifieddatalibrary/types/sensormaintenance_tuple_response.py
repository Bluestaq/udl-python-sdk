# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.sensormaintenance.sensormaintenance_full import SensormaintenanceFull

__all__ = ["SensormaintenanceTupleResponse"]

SensormaintenanceTupleResponse: TypeAlias = List[SensormaintenanceFull]
