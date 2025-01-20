# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .event_evolution_abridged import EventEvolutionAbridged

__all__ = ["EventEvolutionListResponse"]

EventEvolutionListResponse: TypeAlias = List[EventEvolutionAbridged]
