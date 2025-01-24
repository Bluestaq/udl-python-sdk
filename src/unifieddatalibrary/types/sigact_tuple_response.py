# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.sigact.sigact_full import SigactFull

__all__ = ["SigactTupleResponse"]

SigactTupleResponse: TypeAlias = List[SigactFull]
