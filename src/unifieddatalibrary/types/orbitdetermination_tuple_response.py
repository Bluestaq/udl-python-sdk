# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.orbitdetermination.orbitdetermination_full import OrbitdeterminationFull

__all__ = ["OrbitdeterminationTupleResponse"]

OrbitdeterminationTupleResponse: TypeAlias = List[OrbitdeterminationFull]
