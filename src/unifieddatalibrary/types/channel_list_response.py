# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .channel_abridged import ChannelAbridged

__all__ = ["ChannelListResponse"]

ChannelListResponse: TypeAlias = List[ChannelAbridged]
