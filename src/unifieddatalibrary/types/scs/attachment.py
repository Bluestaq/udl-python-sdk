# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Attachment"]


class Attachment(BaseModel):
    author: Optional[str] = None

    content: Optional[str] = None

    content_length: Optional[int] = None

    content_type: Optional[str] = None

    date: Optional[str] = None

    keywords: Optional[str] = None

    language: Optional[str] = None

    title: Optional[str] = None
