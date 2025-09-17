# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NotificationListResponse"]


class NotificationListResponse(BaseModel):
    actions: Optional[
        List[
            Literal[
                "ROOT_WRITE",
                "UPLOAD_FILE",
                "CREATE_FOLDER",
                "DOWNLOAD_FILE",
                "DOWNLOAD_FOLDER",
                "MOVE_RENAME_FILE",
                "MOVE_RENAME_FOLDER",
                "COPY_FILE",
                "COPY_FOLDER",
                "UPDATE_FILE",
                "UPDATE_FOLDER",
                "DELETE_FILE",
                "DELETE_FOLDER",
                "DELETE_EMPTY_FOLDER",
                "CROSS_DOMAIN",
                "SEND_NOTIFICATION",
                "DELETE_READ_ACL",
                "DELETE_WRITE_ACL",
                "DELETE_FILE_TAGS",
                "DELETE_FOLDER_TAGS",
            ]
        ]
    ] = None

    classification_marking: Optional[str] = FieldInfo(alias="classificationMarking", default=None)

    cross_domain_to: Optional[str] = FieldInfo(alias="crossDomainTo", default=None)

    expires: Optional[str] = None

    overwrite: Optional[bool] = None

    path: Optional[str] = None

    timestamp: Optional[str] = None

    user: Optional[str] = None
