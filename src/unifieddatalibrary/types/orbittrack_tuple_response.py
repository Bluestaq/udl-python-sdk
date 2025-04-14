# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.orbittrack.orbittrack_full import OrbittrackFull

__all__ = ["OrbittrackTupleResponse"]

OrbittrackTupleResponse: TypeAlias = List[OrbittrackFull]
