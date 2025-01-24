# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.mti.mti_full import MtiFull

__all__ = ["MtiTupleResponse"]

MtiTupleResponse: TypeAlias = List[MtiFull]
