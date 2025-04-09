# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .elset_ingest_param import ElsetIngestParam

__all__ = ["ElsetCreateBulkParams"]


class ElsetCreateBulkParams(TypedDict, total=False):
    body: Required[Iterable[ElsetIngestParam]]

    dupe_check: Annotated[bool, PropertyInfo(alias="dupeCheck")]
    """
    Boolean indicating if these elsets should be checked for duplicates, default is
    not to.
    """
