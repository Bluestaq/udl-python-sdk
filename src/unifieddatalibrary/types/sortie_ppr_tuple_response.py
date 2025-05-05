# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .sortie_ppr.sortie_ppr_full import SortiePprFull

__all__ = ["SortiePprTupleResponse"]

SortiePprTupleResponse: TypeAlias = List[SortiePprFull]
