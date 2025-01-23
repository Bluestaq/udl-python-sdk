# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.collect_request_full import CollectRequestFull

__all__ = ["CollectRequestTupleResponse"]

CollectRequestTupleResponse: TypeAlias = List[CollectRequestFull]
