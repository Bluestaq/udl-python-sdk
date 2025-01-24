# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.personnelrecovery.personnelrecovery_full import PersonnelrecoveryFull

__all__ = ["PersonnelrecoveryTupleResponse"]

PersonnelrecoveryTupleResponse: TypeAlias = List[PersonnelrecoveryFull]
