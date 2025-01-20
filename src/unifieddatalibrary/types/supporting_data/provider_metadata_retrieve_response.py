# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .dataowner_abridged import DataownerAbridged

__all__ = ["ProviderMetadataRetrieveResponse"]

ProviderMetadataRetrieveResponse: TypeAlias = List[DataownerAbridged]
