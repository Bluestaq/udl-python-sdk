# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.param_descriptor import ParamDescriptor

__all__ = ["SensorQueryhelpResponse"]


class SensorQueryhelpResponse(BaseModel):
    aodr_supported: Optional[bool] = FieldInfo(alias="aodrSupported", default=None)

    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)

    description: Optional[str] = None

    history_supported: Optional[bool] = FieldInfo(alias="historySupported", default=None)

    name: Optional[str] = None

    parameters: Optional[List[ParamDescriptor]] = None

    required_roles: Optional[List[str]] = FieldInfo(alias="requiredRoles", default=None)

    rest_supported: Optional[bool] = FieldInfo(alias="restSupported", default=None)

    sort_supported: Optional[bool] = FieldInfo(alias="sortSupported", default=None)

    type_name: Optional[str] = FieldInfo(alias="typeName", default=None)

    uri: Optional[str] = None
