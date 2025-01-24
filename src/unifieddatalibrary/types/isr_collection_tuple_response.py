# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.isrcollection.isr_collection_full import IsrCollectionFull

__all__ = ["IsrCollectionTupleResponse"]

IsrCollectionTupleResponse: TypeAlias = List[IsrCollectionFull]
