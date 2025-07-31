# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.beamcontour_full import BeamcontourFull

__all__ = ["BeamContourTupleResponse"]

BeamContourTupleResponse: TypeAlias = List[BeamcontourFull]
