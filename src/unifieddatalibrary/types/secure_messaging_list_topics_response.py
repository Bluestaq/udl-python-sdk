# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .topic_details import TopicDetails

__all__ = ["SecureMessagingListTopicsResponse"]

SecureMessagingListTopicsResponse: TypeAlias = List[TopicDetails]
