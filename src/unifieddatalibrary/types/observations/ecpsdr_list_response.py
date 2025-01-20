# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .ecpsdr_abridged import EcpsdrAbridged

__all__ = ["EcpsdrListResponse"]

EcpsdrListResponse: TypeAlias = List[EcpsdrAbridged]
