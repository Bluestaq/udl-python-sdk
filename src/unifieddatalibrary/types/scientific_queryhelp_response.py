# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScientificQueryhelpResponse", "Parameter"]


class Parameter(BaseModel):
    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)

    derived: Optional[bool] = None

    description: Optional[str] = None

    elem_match: Optional[bool] = FieldInfo(alias="elemMatch", default=None)

    format: Optional[str] = None

    hist_query_supported: Optional[bool] = FieldInfo(alias="histQuerySupported", default=None)

    hist_tuple_supported: Optional[bool] = FieldInfo(alias="histTupleSupported", default=None)

    name: Optional[str] = None

    required: Optional[bool] = None

    rest_query_supported: Optional[bool] = FieldInfo(alias="restQuerySupported", default=None)

    rest_tuple_supported: Optional[bool] = FieldInfo(alias="restTupleSupported", default=None)

    type: Optional[str] = None

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)

    utc_date: Optional[bool] = FieldInfo(alias="utcDate", default=None)


class ScientificQueryhelpResponse(BaseModel):
    aodr_supported: Optional[bool] = FieldInfo(alias="aodrSupported", default=None)

    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)

    description: Optional[str] = None

    history_supported: Optional[bool] = FieldInfo(alias="historySupported", default=None)

    name: Optional[str] = None

    parameters: Optional[List[Parameter]] = None

    required_roles: Optional[List[str]] = FieldInfo(alias="requiredRoles", default=None)

    rest_supported: Optional[bool] = FieldInfo(alias="restSupported", default=None)

    sort_supported: Optional[bool] = FieldInfo(alias="sortSupported", default=None)

    type_name: Optional[str] = FieldInfo(alias="typeName", default=None)

    uri: Optional[str] = None
