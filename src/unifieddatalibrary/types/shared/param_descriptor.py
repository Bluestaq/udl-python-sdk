# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParamDescriptor"]


class ParamDescriptor(BaseModel):
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
