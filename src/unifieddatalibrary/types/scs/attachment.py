# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Attachment"]


class Attachment(BaseModel):
    author: Optional[str] = None
    """The creator of this document. Can be a person or a software entity."""

    content_length: Optional[int] = None
    """The length of the document, in bytes."""

    content_type: Optional[str] = None
    """The document's MIME-type (if applicable)."""

    date: Optional[str] = None
    """The time at which this attachment was created, represented in UTC ISO format."""

    keywords: Optional[str] = None
    """Any keywords associated with this document.

    Only applicable to files whose contents are indexed (e.g. text files, PDFs).
    """

    language: Optional[str] = None
    """The human language of the document, if discernible."""

    title: Optional[str] = None
    """The title of the document."""
