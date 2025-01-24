# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.sitestatus.sitestatus_full import SitestatusFull

__all__ = ["SitestatusTupleResponse"]

SitestatusTupleResponse: TypeAlias = List[SitestatusFull]
