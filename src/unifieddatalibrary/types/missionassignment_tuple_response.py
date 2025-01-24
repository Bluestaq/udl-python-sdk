# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .udl.missionassignment.mission_assignment_full import MissionAssignmentFull

__all__ = ["MissionassignmentTupleResponse"]

MissionassignmentTupleResponse: TypeAlias = List[MissionAssignmentFull]
