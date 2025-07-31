# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.notification_full import NotificationFull

__all__ = ["NotificationTupleResponse"]

NotificationTupleResponse: TypeAlias = List[NotificationFull]
