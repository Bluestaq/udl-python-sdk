# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.linkstatus.link_status_full import LinkStatusFull

__all__ = ["LinkStatusTupleResponse"]

LinkStatusTupleResponse: TypeAlias = List[LinkStatusFull]
