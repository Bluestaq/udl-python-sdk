# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AttachmentParam"]


class AttachmentParam(TypedDict, total=False):
    author: str

    content: str

    content_length: int

    content_type: str

    date: str

    keywords: str

    language: str

    title: str
