# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LogisticsSpecialtiesFull"]


class LogisticsSpecialtiesFull(BaseModel):
    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the specialist."""

    last4_ssn: Optional[str] = FieldInfo(alias="last4Ssn", default=None)
    """The last four digits of the specialist's social security number."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the specialist."""

    rank_code: Optional[str] = FieldInfo(alias="rankCode", default=None)
    """Military service rank designation."""

    role_type_code: Optional[str] = FieldInfo(alias="roleTypeCode", default=None)
    """Type code that determines role of the mission response team member.

    TC - Team Chief, TM - Team Member.
    """

    skill_level: Optional[int] = FieldInfo(alias="skillLevel", default=None)
    """Skill level of the mission response team member."""

    specialty: Optional[str] = None
    """
    Indicates where the repairs will be performed, or which shop specialty has been
    assigned responsibility for correcting the discrepancy. Shop specialties are
    normally listed in abbreviated format.
    """
