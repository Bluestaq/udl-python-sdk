# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .personnelrecovery.personnel_recovery_full import PersonnelRecoveryFull

__all__ = ["PersonnelrecoveryTupleResponse"]

PersonnelrecoveryTupleResponse: TypeAlias = List[PersonnelRecoveryFull]
