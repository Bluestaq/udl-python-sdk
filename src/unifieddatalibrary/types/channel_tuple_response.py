# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.channel_full import ChannelFull

__all__ = ["ChannelTupleResponse"]

ChannelTupleResponse: TypeAlias = List[ChannelFull]
