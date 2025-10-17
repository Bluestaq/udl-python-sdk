# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._files import read_file_content, async_read_file_content
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileContent,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scs import (
    v2_copy_params,
    v2_list_params,
    v2_move_params,
    v2_delete_params,
    v2_search_params,
    v2_update_params,
    v2_file_upload_params,
    v2_folder_create_params,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.scs.scs_entity import ScsEntity
from ...types.scs.v2_search_response import V2SearchResponse
from ...types.search_criterion_param import SearchCriterionParam

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        path: str,
        send_notification: bool | Omit = omit,
        id: str | Omit = omit,
        attachment: v2_update_params.Attachment | Omit = omit,
        classification_marking: str | Omit = omit,
        created_at: str | Omit = omit,
        created_by: str | Omit = omit,
        delete_on: int | Omit = omit,
        description: str | Omit = omit,
        filename: str | Omit = omit,
        file_path: str | Omit = omit,
        keywords: str | Omit = omit,
        parent_path: str | Omit = omit,
        path_type: Literal["file", "folder"] | Omit = omit,
        read_acl: str | Omit = omit,
        size: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        updated_at: str | Omit = omit,
        updated_by: str | Omit = omit,
        write_acl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update folders and files.

        For a folder, you may update description, writeAcl,
        readAcl, classificationMarking, and tags. For a file, you may update
        description, classificationMarking, and tags. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          path: The complete path for the object to be updated.

          send_notification: Whether or not to send a notification that the target file/folder was updated.

          id: Unique identifier for document.

          attachment: Additional metadata associated with this document.

          classification_marking: Classification marking of the folder or file in IC/CAPCO portion-marked format.

          created_at: The time at which this document was created, represented in UTC ISO format.

          created_by: The creator of this document. Can be a person or a software entity.

          delete_on: Time at which this document should be automatically deleted. Represented in
              milliseconds since Unix epoch.

          description: Optional description for the file or folder.

          filename: The name of this document. Applicable to files and folders.

          file_path: The absolute path to this document.

          keywords: Optional. Any keywords associated with this document. Only applicable to files
              whose contents are indexed (e.g. text files, PDFs).

          parent_path: The parent folder of this document. If this document is a root-level folder then
              the parent path is "/".

          path_type: The type of this document.

          read_acl: For folders only. Comma separated list of user and group ids that should have
              read access on this folder and the items nested in it.

          size: Size of this document in bytes.

          tags: Array of provider/source specific tags for this data, used for implementing data
              owner conditional access controls to restrict access to the data.

          updated_at: The time at which this document was most recently updated, represented in UTC
              ISO format.

          updated_by: The person or software entity who updated this document most recently.

          write_acl: For folders only. Comma separated list of user and group ids that should have
              write access on this folder and the items nested in it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/scs/v2/update",
            body=maybe_transform(
                {
                    "id": id,
                    "attachment": attachment,
                    "classification_marking": classification_marking,
                    "created_at": created_at,
                    "created_by": created_by,
                    "delete_on": delete_on,
                    "description": description,
                    "filename": filename,
                    "file_path": file_path,
                    "keywords": keywords,
                    "parent_path": parent_path,
                    "path_type": path_type,
                    "read_acl": read_acl,
                    "size": size,
                    "tags": tags,
                    "updated_at": updated_at,
                    "updated_by": updated_by,
                    "write_acl": write_acl,
                },
                v2_update_params.V2UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "send_notification": send_notification,
                    },
                    v2_update_params.V2UpdateParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        path: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        order: str | Omit = omit,
        search_after: str | Omit = omit,
        size: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[ScsEntity]:
        """
        Returns a list of ScsEntity objects, each directly nested under the provided
        path.

        Args:
          path: The base path to list.

          order: The order in which entries should be sorted.

          search_after: The starting point for pagination results, usually set to the value of the
              SEARCH_AFTER header returned in the previous request.

          size: The number of results to retrieve.

          sort: The field on which to sort entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/scs/v2/list",
            page=SyncOffsetPage[ScsEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "first_result": first_result,
                        "max_results": max_results,
                        "order": order,
                        "search_after": search_after,
                        "size": size,
                        "sort": sort,
                    },
                    v2_list_params.V2ListParams,
                ),
            ),
            model=ScsEntity,
        )

    def delete(
        self,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to delete a folder or file.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          path: The complete path for the object to be deleted. Must start with '/'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/scs/v2/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"path": path}, v2_delete_params.V2DeleteParams),
            ),
            cast_to=NoneType,
        )

    def copy(
        self,
        *,
        from_path: str,
        to_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to copy a folder or file.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          from_path: The path of the file or folder to copy. Must start with '/'.

          to_path: The destination path to copy to. Must start with '/'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/scs/v2/copy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_path": from_path,
                        "to_path": to_path,
                    },
                    v2_copy_params.V2CopyParams,
                ),
            ),
            cast_to=NoneType,
        )

    def file_upload(
        self,
        file_content: FileContent,
        *,
        classification_marking: str,
        path: str,
        delete_after: str | Omit = omit,
        description: str | Omit = omit,
        overwrite: bool | Omit = omit,
        send_notification: bool | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to upload a file.

        A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of uploaded document. If folders are created, they will
              also have this classification marking.

          path: The complete path for the upload including filename. Will attempt to create
              folders in path if necessary. Must start with '/'.

          delete_after: Length of time after which to automatically delete the file.

          description: Optional description of uploaded document.

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          send_notification: Whether or not to send a notification that this file was uploaded.

          tags: Optional array of provider/source specific tags for this data, used for
              implementing data owner conditional access controls to restrict access to the
              data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return self._post(
            "/scs/v2/file",
            body=read_file_content(file_content),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "classification_marking": classification_marking,
                        "path": path,
                        "delete_after": delete_after,
                        "description": description,
                        "overwrite": overwrite,
                        "send_notification": send_notification,
                        "tags": tags,
                    },
                    v2_file_upload_params.V2FileUploadParams,
                ),
            ),
            cast_to=NoneType,
        )

    def folder_create(
        self,
        *,
        path: str,
        send_notification: bool | Omit = omit,
        id: str | Omit = omit,
        attachment: v2_folder_create_params.Attachment | Omit = omit,
        classification_marking: str | Omit = omit,
        created_at: str | Omit = omit,
        created_by: str | Omit = omit,
        delete_on: int | Omit = omit,
        description: str | Omit = omit,
        filename: str | Omit = omit,
        file_path: str | Omit = omit,
        keywords: str | Omit = omit,
        parent_path: str | Omit = omit,
        path_type: Literal["file", "folder"] | Omit = omit,
        read_acl: str | Omit = omit,
        size: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        updated_at: str | Omit = omit,
        updated_by: str | Omit = omit,
        write_acl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates all folders in provided path that don't exist.

        Can be used to create a
        single folder or a new folder structure. Provided classificationMarking,
        description, writeAcl, readAcl, and tags are applied to the deepest folder in
        the provided path. If parent folders are created by this request, each parent
        folder will be created with the same classificationMarking and tags. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          path: Path to create. Will attempt to create all folders in the path that do not
              exist. Must start and end with '/'.

          send_notification: Whether or not to send a notification that this folder was created.

          id: Unique identifier for document.

          attachment: Additional metadata associated with this document.

          classification_marking: Classification marking of the folder or file in IC/CAPCO portion-marked format.

          created_at: The time at which this document was created, represented in UTC ISO format.

          created_by: The creator of this document. Can be a person or a software entity.

          delete_on: Time at which this document should be automatically deleted. Represented in
              milliseconds since Unix epoch.

          description: Optional description for the file or folder.

          filename: The name of this document. Applicable to files and folders.

          file_path: The absolute path to this document.

          keywords: Optional. Any keywords associated with this document. Only applicable to files
              whose contents are indexed (e.g. text files, PDFs).

          parent_path: The parent folder of this document. If this document is a root-level folder then
              the parent path is "/".

          path_type: The type of this document.

          read_acl: For folders only. Comma separated list of user and group ids that should have
              read access on this folder and the items nested in it.

          size: Size of this document in bytes.

          tags: Array of provider/source specific tags for this data, used for implementing data
              owner conditional access controls to restrict access to the data.

          updated_at: The time at which this document was most recently updated, represented in UTC
              ISO format.

          updated_by: The person or software entity who updated this document most recently.

          write_acl: For folders only. Comma separated list of user and group ids that should have
              write access on this folder and the items nested in it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/scs/v2/folder",
            body=maybe_transform(
                {
                    "id": id,
                    "attachment": attachment,
                    "classification_marking": classification_marking,
                    "created_at": created_at,
                    "created_by": created_by,
                    "delete_on": delete_on,
                    "description": description,
                    "filename": filename,
                    "file_path": file_path,
                    "keywords": keywords,
                    "parent_path": parent_path,
                    "path_type": path_type,
                    "read_acl": read_acl,
                    "size": size,
                    "tags": tags,
                    "updated_at": updated_at,
                    "updated_by": updated_by,
                    "write_acl": write_acl,
                },
                v2_folder_create_params.V2FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "send_notification": send_notification,
                    },
                    v2_folder_create_params.V2FolderCreateParams,
                ),
            ),
            cast_to=NoneType,
        )

    def move(
        self,
        *,
        from_path: str,
        to_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to move or rename a folder or file.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          from_path: The path of the file or folder to move or rename. Must start with '/'.

          to_path: The destination path of the file or folder after moving or renaming. Must start
              with '/'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/scs/v2/move",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_path": from_path,
                        "to_path": to_path,
                    },
                    v2_move_params.V2MoveParams,
                ),
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        *,
        order: str | Omit = omit,
        search_after: str | Omit = omit,
        size: int | Omit = omit,
        sort: str | Omit = omit,
        query: SearchCriterionParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2SearchResponse:
        """
        Operation to search for files in the Secure Content Store.

        Args:
          order: The order in which entries should be sorted.

          search_after: The starting point for pagination results, usually set to the value of the
              SEARCH_AFTER header returned in the previous request.

          size: The number of results to retrieve.

          sort: The field on which to sort entries.

          query: A search criterion, which can be a simple field comparison or a logical
              combination of other criteria.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scs/v2/search",
            body=maybe_transform({"query": query}, v2_search_params.V2SearchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "search_after": search_after,
                        "size": size,
                        "sort": sort,
                    },
                    v2_search_params.V2SearchParams,
                ),
            ),
            cast_to=V2SearchResponse,
        )


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        path: str,
        send_notification: bool | Omit = omit,
        id: str | Omit = omit,
        attachment: v2_update_params.Attachment | Omit = omit,
        classification_marking: str | Omit = omit,
        created_at: str | Omit = omit,
        created_by: str | Omit = omit,
        delete_on: int | Omit = omit,
        description: str | Omit = omit,
        filename: str | Omit = omit,
        file_path: str | Omit = omit,
        keywords: str | Omit = omit,
        parent_path: str | Omit = omit,
        path_type: Literal["file", "folder"] | Omit = omit,
        read_acl: str | Omit = omit,
        size: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        updated_at: str | Omit = omit,
        updated_by: str | Omit = omit,
        write_acl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update folders and files.

        For a folder, you may update description, writeAcl,
        readAcl, classificationMarking, and tags. For a file, you may update
        description, classificationMarking, and tags. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          path: The complete path for the object to be updated.

          send_notification: Whether or not to send a notification that the target file/folder was updated.

          id: Unique identifier for document.

          attachment: Additional metadata associated with this document.

          classification_marking: Classification marking of the folder or file in IC/CAPCO portion-marked format.

          created_at: The time at which this document was created, represented in UTC ISO format.

          created_by: The creator of this document. Can be a person or a software entity.

          delete_on: Time at which this document should be automatically deleted. Represented in
              milliseconds since Unix epoch.

          description: Optional description for the file or folder.

          filename: The name of this document. Applicable to files and folders.

          file_path: The absolute path to this document.

          keywords: Optional. Any keywords associated with this document. Only applicable to files
              whose contents are indexed (e.g. text files, PDFs).

          parent_path: The parent folder of this document. If this document is a root-level folder then
              the parent path is "/".

          path_type: The type of this document.

          read_acl: For folders only. Comma separated list of user and group ids that should have
              read access on this folder and the items nested in it.

          size: Size of this document in bytes.

          tags: Array of provider/source specific tags for this data, used for implementing data
              owner conditional access controls to restrict access to the data.

          updated_at: The time at which this document was most recently updated, represented in UTC
              ISO format.

          updated_by: The person or software entity who updated this document most recently.

          write_acl: For folders only. Comma separated list of user and group ids that should have
              write access on this folder and the items nested in it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/scs/v2/update",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "attachment": attachment,
                    "classification_marking": classification_marking,
                    "created_at": created_at,
                    "created_by": created_by,
                    "delete_on": delete_on,
                    "description": description,
                    "filename": filename,
                    "file_path": file_path,
                    "keywords": keywords,
                    "parent_path": parent_path,
                    "path_type": path_type,
                    "read_acl": read_acl,
                    "size": size,
                    "tags": tags,
                    "updated_at": updated_at,
                    "updated_by": updated_by,
                    "write_acl": write_acl,
                },
                v2_update_params.V2UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "send_notification": send_notification,
                    },
                    v2_update_params.V2UpdateParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        path: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        order: str | Omit = omit,
        search_after: str | Omit = omit,
        size: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ScsEntity, AsyncOffsetPage[ScsEntity]]:
        """
        Returns a list of ScsEntity objects, each directly nested under the provided
        path.

        Args:
          path: The base path to list.

          order: The order in which entries should be sorted.

          search_after: The starting point for pagination results, usually set to the value of the
              SEARCH_AFTER header returned in the previous request.

          size: The number of results to retrieve.

          sort: The field on which to sort entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/scs/v2/list",
            page=AsyncOffsetPage[ScsEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "first_result": first_result,
                        "max_results": max_results,
                        "order": order,
                        "search_after": search_after,
                        "size": size,
                        "sort": sort,
                    },
                    v2_list_params.V2ListParams,
                ),
            ),
            model=ScsEntity,
        )

    async def delete(
        self,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to delete a folder or file.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          path: The complete path for the object to be deleted. Must start with '/'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/scs/v2/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"path": path}, v2_delete_params.V2DeleteParams),
            ),
            cast_to=NoneType,
        )

    async def copy(
        self,
        *,
        from_path: str,
        to_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to copy a folder or file.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          from_path: The path of the file or folder to copy. Must start with '/'.

          to_path: The destination path to copy to. Must start with '/'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/scs/v2/copy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_path": from_path,
                        "to_path": to_path,
                    },
                    v2_copy_params.V2CopyParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def file_upload(
        self,
        file_content: FileContent,
        *,
        classification_marking: str,
        path: str,
        delete_after: str | Omit = omit,
        description: str | Omit = omit,
        overwrite: bool | Omit = omit,
        send_notification: bool | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to upload a file.

        A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of uploaded document. If folders are created, they will
              also have this classification marking.

          path: The complete path for the upload including filename. Will attempt to create
              folders in path if necessary. Must start with '/'.

          delete_after: Length of time after which to automatically delete the file.

          description: Optional description of uploaded document.

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          send_notification: Whether or not to send a notification that this file was uploaded.

          tags: Optional array of provider/source specific tags for this data, used for
              implementing data owner conditional access controls to restrict access to the
              data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return await self._post(
            "/scs/v2/file",
            body=await async_read_file_content(file_content),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "classification_marking": classification_marking,
                        "path": path,
                        "delete_after": delete_after,
                        "description": description,
                        "overwrite": overwrite,
                        "send_notification": send_notification,
                        "tags": tags,
                    },
                    v2_file_upload_params.V2FileUploadParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def folder_create(
        self,
        *,
        path: str,
        send_notification: bool | Omit = omit,
        id: str | Omit = omit,
        attachment: v2_folder_create_params.Attachment | Omit = omit,
        classification_marking: str | Omit = omit,
        created_at: str | Omit = omit,
        created_by: str | Omit = omit,
        delete_on: int | Omit = omit,
        description: str | Omit = omit,
        filename: str | Omit = omit,
        file_path: str | Omit = omit,
        keywords: str | Omit = omit,
        parent_path: str | Omit = omit,
        path_type: Literal["file", "folder"] | Omit = omit,
        read_acl: str | Omit = omit,
        size: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        updated_at: str | Omit = omit,
        updated_by: str | Omit = omit,
        write_acl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates all folders in provided path that don't exist.

        Can be used to create a
        single folder or a new folder structure. Provided classificationMarking,
        description, writeAcl, readAcl, and tags are applied to the deepest folder in
        the provided path. If parent folders are created by this request, each parent
        folder will be created with the same classificationMarking and tags. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          path: Path to create. Will attempt to create all folders in the path that do not
              exist. Must start and end with '/'.

          send_notification: Whether or not to send a notification that this folder was created.

          id: Unique identifier for document.

          attachment: Additional metadata associated with this document.

          classification_marking: Classification marking of the folder or file in IC/CAPCO portion-marked format.

          created_at: The time at which this document was created, represented in UTC ISO format.

          created_by: The creator of this document. Can be a person or a software entity.

          delete_on: Time at which this document should be automatically deleted. Represented in
              milliseconds since Unix epoch.

          description: Optional description for the file or folder.

          filename: The name of this document. Applicable to files and folders.

          file_path: The absolute path to this document.

          keywords: Optional. Any keywords associated with this document. Only applicable to files
              whose contents are indexed (e.g. text files, PDFs).

          parent_path: The parent folder of this document. If this document is a root-level folder then
              the parent path is "/".

          path_type: The type of this document.

          read_acl: For folders only. Comma separated list of user and group ids that should have
              read access on this folder and the items nested in it.

          size: Size of this document in bytes.

          tags: Array of provider/source specific tags for this data, used for implementing data
              owner conditional access controls to restrict access to the data.

          updated_at: The time at which this document was most recently updated, represented in UTC
              ISO format.

          updated_by: The person or software entity who updated this document most recently.

          write_acl: For folders only. Comma separated list of user and group ids that should have
              write access on this folder and the items nested in it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/scs/v2/folder",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "attachment": attachment,
                    "classification_marking": classification_marking,
                    "created_at": created_at,
                    "created_by": created_by,
                    "delete_on": delete_on,
                    "description": description,
                    "filename": filename,
                    "file_path": file_path,
                    "keywords": keywords,
                    "parent_path": parent_path,
                    "path_type": path_type,
                    "read_acl": read_acl,
                    "size": size,
                    "tags": tags,
                    "updated_at": updated_at,
                    "updated_by": updated_by,
                    "write_acl": write_acl,
                },
                v2_folder_create_params.V2FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "send_notification": send_notification,
                    },
                    v2_folder_create_params.V2FolderCreateParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def move(
        self,
        *,
        from_path: str,
        to_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to move or rename a folder or file.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

        Args:
          from_path: The path of the file or folder to move or rename. Must start with '/'.

          to_path: The destination path of the file or folder after moving or renaming. Must start
              with '/'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/scs/v2/move",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_path": from_path,
                        "to_path": to_path,
                    },
                    v2_move_params.V2MoveParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def search(
        self,
        *,
        order: str | Omit = omit,
        search_after: str | Omit = omit,
        size: int | Omit = omit,
        sort: str | Omit = omit,
        query: SearchCriterionParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2SearchResponse:
        """
        Operation to search for files in the Secure Content Store.

        Args:
          order: The order in which entries should be sorted.

          search_after: The starting point for pagination results, usually set to the value of the
              SEARCH_AFTER header returned in the previous request.

          size: The number of results to retrieve.

          sort: The field on which to sort entries.

          query: A search criterion, which can be a simple field comparison or a logical
              combination of other criteria.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scs/v2/search",
            body=await async_maybe_transform({"query": query}, v2_search_params.V2SearchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order": order,
                        "search_after": search_after,
                        "size": size,
                        "sort": sort,
                    },
                    v2_search_params.V2SearchParams,
                ),
            ),
            cast_to=V2SearchResponse,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.update = to_raw_response_wrapper(
            v2.update,
        )
        self.list = to_raw_response_wrapper(
            v2.list,
        )
        self.delete = to_raw_response_wrapper(
            v2.delete,
        )
        self.copy = to_raw_response_wrapper(
            v2.copy,
        )
        self.file_upload = to_raw_response_wrapper(
            v2.file_upload,
        )
        self.folder_create = to_raw_response_wrapper(
            v2.folder_create,
        )
        self.move = to_raw_response_wrapper(
            v2.move,
        )
        self.search = to_raw_response_wrapper(
            v2.search,
        )


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.update = async_to_raw_response_wrapper(
            v2.update,
        )
        self.list = async_to_raw_response_wrapper(
            v2.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v2.delete,
        )
        self.copy = async_to_raw_response_wrapper(
            v2.copy,
        )
        self.file_upload = async_to_raw_response_wrapper(
            v2.file_upload,
        )
        self.folder_create = async_to_raw_response_wrapper(
            v2.folder_create,
        )
        self.move = async_to_raw_response_wrapper(
            v2.move,
        )
        self.search = async_to_raw_response_wrapper(
            v2.search,
        )


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.update = to_streamed_response_wrapper(
            v2.update,
        )
        self.list = to_streamed_response_wrapper(
            v2.list,
        )
        self.delete = to_streamed_response_wrapper(
            v2.delete,
        )
        self.copy = to_streamed_response_wrapper(
            v2.copy,
        )
        self.file_upload = to_streamed_response_wrapper(
            v2.file_upload,
        )
        self.folder_create = to_streamed_response_wrapper(
            v2.folder_create,
        )
        self.move = to_streamed_response_wrapper(
            v2.move,
        )
        self.search = to_streamed_response_wrapper(
            v2.search,
        )


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.update = async_to_streamed_response_wrapper(
            v2.update,
        )
        self.list = async_to_streamed_response_wrapper(
            v2.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v2.delete,
        )
        self.copy = async_to_streamed_response_wrapper(
            v2.copy,
        )
        self.file_upload = async_to_streamed_response_wrapper(
            v2.file_upload,
        )
        self.folder_create = async_to_streamed_response_wrapper(
            v2.folder_create,
        )
        self.move = async_to_streamed_response_wrapper(
            v2.move,
        )
        self.search = async_to_streamed_response_wrapper(
            v2.search,
        )
