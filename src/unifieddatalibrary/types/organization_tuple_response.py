# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .organization_full import OrganizationFull

__all__ = ["OrganizationTupleResponse"]

OrganizationTupleResponse: TypeAlias = List[OrganizationFull]
