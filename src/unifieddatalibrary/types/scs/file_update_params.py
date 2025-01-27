# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.file_data import FileData

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    file_data_list: Annotated[Iterable[FileData], PropertyInfo(alias="fileDataList")]
