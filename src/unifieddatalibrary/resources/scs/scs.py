# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict

import httpx

from .v2 import (
    V2Resource,
    AsyncV2Resource,
    V2ResourceWithRawResponse,
    AsyncV2ResourceWithRawResponse,
    V2ResourceWithStreamingResponse,
    AsyncV2ResourceWithStreamingResponse,
)
from .file import (
    FileResource,
    AsyncFileResource,
    FileResourceWithRawResponse,
    AsyncFileResourceWithRawResponse,
    FileResourceWithStreamingResponse,
    AsyncFileResourceWithStreamingResponse,
)
from .view import (
    ViewResource,
    AsyncViewResource,
    ViewResourceWithRawResponse,
    AsyncViewResourceWithRawResponse,
    ViewResourceWithStreamingResponse,
    AsyncViewResourceWithStreamingResponse,
)
from .paths import (
    PathsResource,
    AsyncPathsResource,
    PathsResourceWithRawResponse,
    AsyncPathsResourceWithRawResponse,
    PathsResourceWithStreamingResponse,
    AsyncPathsResourceWithStreamingResponse,
)
from ...types import (
    sc_copy_params,
    sc_move_params,
    sc_delete_params,
    sc_rename_params,
    sc_search_params,
    sc_file_upload_params,
    sc_file_download_params,
    sc_has_write_access_params,
)
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
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
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sc_search_response import ScSearchResponse
from .notifications.notifications import (
    NotificationsResource,
    AsyncNotificationsResource,
    NotificationsResourceWithRawResponse,
    AsyncNotificationsResourceWithRawResponse,
    NotificationsResourceWithStreamingResponse,
    AsyncNotificationsResourceWithStreamingResponse,
)
from ...types.sc_has_write_access_response import ScHasWriteAccessResponse
from ...types.sc_allowable_file_mimes_response import ScAllowableFileMimesResponse
from ...types.sc_allowable_file_extensions_response import ScAllowableFileExtensionsResponse

__all__ = ["ScsResource", "AsyncScsResource"]


class ScsResource(SyncAPIResource):
    @cached_property
    def notifications(self) -> NotificationsResource:
        return NotificationsResource(self._client)

    @cached_property
    def file(self) -> FileResource:
        return FileResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def paths(self) -> PathsResource:
        return PathsResource(self._client)

    @cached_property
    def view(self) -> ViewResource:
        return ViewResource(self._client)

    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> ScsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ScsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the requested file or folder in the passed path directory that is
        visible to the calling user. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          id: The id of the item to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/scs/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, sc_delete_params.ScDeleteParams),
            ),
            cast_to=NoneType,
        )

    def allowable_file_extensions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScAllowableFileExtensionsResponse:
        """Returns a list of the allowed filename extensions."""
        return self._get(
            "/scs/allowableFileExtensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAllowableFileExtensionsResponse,
        )

    def allowable_file_mimes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScAllowableFileMimesResponse:
        """Returns a list of the allowed file upload mime types."""
        return self._get(
            "/scs/allowableFileMimes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAllowableFileMimesResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def copy(
        self,
        *,
        id: str,
        target_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """operation to copy folders or files.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The path of the item to copy

          target_path: The path to copy to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scs/copy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "target_path": target_path,
                    },
                    sc_copy_params.ScCopyParams,
                ),
            ),
            cast_to=str,
        )

    def download(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Downloads a zip of one or more files and/or folders.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/scs/download",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def file_download(
        self,
        *,
        id: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download a single file from SCS.

        Args:
          id: The complete path and filename of the file to download.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            "/scs/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sc_file_download_params.ScFileDownloadParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def file_upload(
        self,
        file_content: FileContent,
        *,
        classification_marking: str,
        file_name: str,
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
    ) -> str:
        """Operation to upload a file.

        A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the file being uploaded.

          file_name: Name of the file to upload.

          path: The base path to upload file

          delete_after: Length of time after which to automatically delete the file.

          description: Description

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          send_notification: Whether or not to send a notification that this file was uploaded.

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/scs/file",
            body=read_file_content(file_content),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "classification_marking": classification_marking,
                        "file_name": file_name,
                        "path": path,
                        "delete_after": delete_after,
                        "description": description,
                        "overwrite": overwrite,
                        "send_notification": send_notification,
                        "tags": tags,
                    },
                    sc_file_upload_params.ScFileUploadParams,
                ),
            ),
            cast_to=str,
        )

    def has_write_access(
        self,
        *,
        path: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScHasWriteAccessResponse:
        """
        Returns true if a user has write access to the specified folder.

        Args:
          path: Folder path for which to check user write access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/scs/userHasWriteAccess",
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
                    },
                    sc_has_write_access_params.ScHasWriteAccessParams,
                ),
            ),
            cast_to=ScHasWriteAccessResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def move(
        self,
        *,
        id: str,
        target_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """operation to move folders or files.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The path of the item to move

          target_path: The path to copy to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/scs/move",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "target_path": target_path,
                    },
                    sc_move_params.ScMoveParams,
                ),
            ),
            cast_to=str,
        )

    @typing_extensions.deprecated("deprecated")
    def rename(
        self,
        *,
        id: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to rename folders or files.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          id: The path of the item to rename.

          new_name: The new name for the file or folder. Do not include the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/scs/rename",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "new_name": new_name,
                    },
                    sc_rename_params.ScRenameParams,
                ),
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def search(
        self,
        *,
        path: str,
        count: int | Omit = omit,
        offset: int | Omit = omit,
        content_criteria: str | Omit = omit,
        meta_data_criteria: Dict[str, SequenceNotStr[str]] | Omit = omit,
        non_range_criteria: Dict[str, SequenceNotStr[str]] | Omit = omit,
        range_criteria: Dict[str, SequenceNotStr[str]] | Omit = omit,
        search_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScSearchResponse:
        """
        Search for files by metadata and/or text in file content.

        Args:
          path: The path to search from

          count: Number of items per page

          offset: First result to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scs/search",
            body=maybe_transform(
                {
                    "content_criteria": content_criteria,
                    "meta_data_criteria": meta_data_criteria,
                    "non_range_criteria": non_range_criteria,
                    "range_criteria": range_criteria,
                    "search_after": search_after,
                },
                sc_search_params.ScSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "count": count,
                        "offset": offset,
                    },
                    sc_search_params.ScSearchParams,
                ),
            ),
            cast_to=ScSearchResponse,
        )


class AsyncScsResource(AsyncAPIResource):
    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        return AsyncNotificationsResource(self._client)

    @cached_property
    def file(self) -> AsyncFileResource:
        return AsyncFileResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def paths(self) -> AsyncPathsResource:
        return AsyncPathsResource(self._client)

    @cached_property
    def view(self) -> AsyncViewResource:
        return AsyncViewResource(self._client)

    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncScsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the requested file or folder in the passed path directory that is
        visible to the calling user. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          id: The id of the item to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/scs/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, sc_delete_params.ScDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def allowable_file_extensions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScAllowableFileExtensionsResponse:
        """Returns a list of the allowed filename extensions."""
        return await self._get(
            "/scs/allowableFileExtensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAllowableFileExtensionsResponse,
        )

    async def allowable_file_mimes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScAllowableFileMimesResponse:
        """Returns a list of the allowed file upload mime types."""
        return await self._get(
            "/scs/allowableFileMimes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAllowableFileMimesResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def copy(
        self,
        *,
        id: str,
        target_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """operation to copy folders or files.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The path of the item to copy

          target_path: The path to copy to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scs/copy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "target_path": target_path,
                    },
                    sc_copy_params.ScCopyParams,
                ),
            ),
            cast_to=str,
        )

    async def download(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Downloads a zip of one or more files and/or folders.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/scs/download",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def file_download(
        self,
        *,
        id: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download a single file from SCS.

        Args:
          id: The complete path and filename of the file to download.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            "/scs/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sc_file_download_params.ScFileDownloadParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def file_upload(
        self,
        file_content: FileContent,
        *,
        classification_marking: str,
        file_name: str,
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
    ) -> str:
        """Operation to upload a file.

        A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the file being uploaded.

          file_name: Name of the file to upload.

          path: The base path to upload file

          delete_after: Length of time after which to automatically delete the file.

          description: Description

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          send_notification: Whether or not to send a notification that this file was uploaded.

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/scs/file",
            body=await async_read_file_content(file_content),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "classification_marking": classification_marking,
                        "file_name": file_name,
                        "path": path,
                        "delete_after": delete_after,
                        "description": description,
                        "overwrite": overwrite,
                        "send_notification": send_notification,
                        "tags": tags,
                    },
                    sc_file_upload_params.ScFileUploadParams,
                ),
            ),
            cast_to=str,
        )

    async def has_write_access(
        self,
        *,
        path: str,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScHasWriteAccessResponse:
        """
        Returns true if a user has write access to the specified folder.

        Args:
          path: Folder path for which to check user write access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/scs/userHasWriteAccess",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sc_has_write_access_params.ScHasWriteAccessParams,
                ),
            ),
            cast_to=ScHasWriteAccessResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def move(
        self,
        *,
        id: str,
        target_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """operation to move folders or files.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The path of the item to move

          target_path: The path to copy to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/scs/move",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "target_path": target_path,
                    },
                    sc_move_params.ScMoveParams,
                ),
            ),
            cast_to=str,
        )

    @typing_extensions.deprecated("deprecated")
    async def rename(
        self,
        *,
        id: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Operation to rename folders or files.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          id: The path of the item to rename.

          new_name: The new name for the file or folder. Do not include the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/scs/rename",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "new_name": new_name,
                    },
                    sc_rename_params.ScRenameParams,
                ),
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def search(
        self,
        *,
        path: str,
        count: int | Omit = omit,
        offset: int | Omit = omit,
        content_criteria: str | Omit = omit,
        meta_data_criteria: Dict[str, SequenceNotStr[str]] | Omit = omit,
        non_range_criteria: Dict[str, SequenceNotStr[str]] | Omit = omit,
        range_criteria: Dict[str, SequenceNotStr[str]] | Omit = omit,
        search_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScSearchResponse:
        """
        Search for files by metadata and/or text in file content.

        Args:
          path: The path to search from

          count: Number of items per page

          offset: First result to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scs/search",
            body=await async_maybe_transform(
                {
                    "content_criteria": content_criteria,
                    "meta_data_criteria": meta_data_criteria,
                    "non_range_criteria": non_range_criteria,
                    "range_criteria": range_criteria,
                    "search_after": search_after,
                },
                sc_search_params.ScSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "count": count,
                        "offset": offset,
                    },
                    sc_search_params.ScSearchParams,
                ),
            ),
            cast_to=ScSearchResponse,
        )


class ScsResourceWithRawResponse:
    def __init__(self, scs: ScsResource) -> None:
        self._scs = scs

        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                scs.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.allowable_file_extensions = to_raw_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = to_raw_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                scs.copy,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download = to_custom_raw_response_wrapper(
            scs.download,
            BinaryAPIResponse,
        )
        self.file_download = to_custom_raw_response_wrapper(
            scs.file_download,
            BinaryAPIResponse,
        )
        self.file_upload = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                scs.file_upload,  # pyright: ignore[reportDeprecated],
            )
        )
        self.has_write_access = to_raw_response_wrapper(
            scs.has_write_access,
        )
        self.move = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                scs.move,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rename = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                scs.rename,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                scs.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def notifications(self) -> NotificationsResourceWithRawResponse:
        return NotificationsResourceWithRawResponse(self._scs.notifications)

    @cached_property
    def file(self) -> FileResourceWithRawResponse:
        return FileResourceWithRawResponse(self._scs.file)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._scs.folders)

    @cached_property
    def paths(self) -> PathsResourceWithRawResponse:
        return PathsResourceWithRawResponse(self._scs.paths)

    @cached_property
    def view(self) -> ViewResourceWithRawResponse:
        return ViewResourceWithRawResponse(self._scs.view)

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._scs.v2)


class AsyncScsResourceWithRawResponse:
    def __init__(self, scs: AsyncScsResource) -> None:
        self._scs = scs

        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                scs.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.allowable_file_extensions = async_to_raw_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = async_to_raw_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                scs.copy,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download = async_to_custom_raw_response_wrapper(
            scs.download,
            AsyncBinaryAPIResponse,
        )
        self.file_download = async_to_custom_raw_response_wrapper(
            scs.file_download,
            AsyncBinaryAPIResponse,
        )
        self.file_upload = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                scs.file_upload,  # pyright: ignore[reportDeprecated],
            )
        )
        self.has_write_access = async_to_raw_response_wrapper(
            scs.has_write_access,
        )
        self.move = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                scs.move,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rename = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                scs.rename,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                scs.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithRawResponse:
        return AsyncNotificationsResourceWithRawResponse(self._scs.notifications)

    @cached_property
    def file(self) -> AsyncFileResourceWithRawResponse:
        return AsyncFileResourceWithRawResponse(self._scs.file)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._scs.folders)

    @cached_property
    def paths(self) -> AsyncPathsResourceWithRawResponse:
        return AsyncPathsResourceWithRawResponse(self._scs.paths)

    @cached_property
    def view(self) -> AsyncViewResourceWithRawResponse:
        return AsyncViewResourceWithRawResponse(self._scs.view)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._scs.v2)


class ScsResourceWithStreamingResponse:
    def __init__(self, scs: ScsResource) -> None:
        self._scs = scs

        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                scs.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.allowable_file_extensions = to_streamed_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = to_streamed_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                scs.copy,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download = to_custom_streamed_response_wrapper(
            scs.download,
            StreamedBinaryAPIResponse,
        )
        self.file_download = to_custom_streamed_response_wrapper(
            scs.file_download,
            StreamedBinaryAPIResponse,
        )
        self.file_upload = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                scs.file_upload,  # pyright: ignore[reportDeprecated],
            )
        )
        self.has_write_access = to_streamed_response_wrapper(
            scs.has_write_access,
        )
        self.move = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                scs.move,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rename = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                scs.rename,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                scs.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def notifications(self) -> NotificationsResourceWithStreamingResponse:
        return NotificationsResourceWithStreamingResponse(self._scs.notifications)

    @cached_property
    def file(self) -> FileResourceWithStreamingResponse:
        return FileResourceWithStreamingResponse(self._scs.file)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._scs.folders)

    @cached_property
    def paths(self) -> PathsResourceWithStreamingResponse:
        return PathsResourceWithStreamingResponse(self._scs.paths)

    @cached_property
    def view(self) -> ViewResourceWithStreamingResponse:
        return ViewResourceWithStreamingResponse(self._scs.view)

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._scs.v2)


class AsyncScsResourceWithStreamingResponse:
    def __init__(self, scs: AsyncScsResource) -> None:
        self._scs = scs

        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                scs.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.allowable_file_extensions = async_to_streamed_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = async_to_streamed_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                scs.copy,  # pyright: ignore[reportDeprecated],
            )
        )
        self.download = async_to_custom_streamed_response_wrapper(
            scs.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.file_download = async_to_custom_streamed_response_wrapper(
            scs.file_download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.file_upload = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                scs.file_upload,  # pyright: ignore[reportDeprecated],
            )
        )
        self.has_write_access = async_to_streamed_response_wrapper(
            scs.has_write_access,
        )
        self.move = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                scs.move,  # pyright: ignore[reportDeprecated],
            )
        )
        self.rename = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                scs.rename,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                scs.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithStreamingResponse:
        return AsyncNotificationsResourceWithStreamingResponse(self._scs.notifications)

    @cached_property
    def file(self) -> AsyncFileResourceWithStreamingResponse:
        return AsyncFileResourceWithStreamingResponse(self._scs.file)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._scs.folders)

    @cached_property
    def paths(self) -> AsyncPathsResourceWithStreamingResponse:
        return AsyncPathsResourceWithStreamingResponse(self._scs.paths)

    @cached_property
    def view(self) -> AsyncViewResourceWithStreamingResponse:
        return AsyncViewResourceWithStreamingResponse(self._scs.view)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._scs.v2)
