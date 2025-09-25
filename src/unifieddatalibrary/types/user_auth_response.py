# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["UserAuthResponse"]


class UserAuthResponse(BaseModel):
    auth: bool
    """Authentication status"""

    roles: List[str]
    """List of user roles"""

    sub: str
    """Subject identifier"""
