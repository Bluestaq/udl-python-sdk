# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List

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
from .paths import (
    PathsResource,
    AsyncPathsResource,
    PathsResourceWithRawResponse,
    AsyncPathsResourceWithRawResponse,
    PathsResourceWithStreamingResponse,
    AsyncPathsResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ...types import (
    sc_copy_params,
    sc_move_params,
    sc_delete_params,
    sc_rename_params,
    sc_search_params,
    sc_file_upload_params,
    sc_update_tags_params,
    sc_file_download_params,
)
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
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
from .file_metadata import (
    FileMetadataResource,
    AsyncFileMetadataResource,
    FileMetadataResourceWithRawResponse,
    AsyncFileMetadataResourceWithRawResponse,
    FileMetadataResourceWithStreamingResponse,
    AsyncFileMetadataResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .range_parameters import (
    RangeParametersResource,
    AsyncRangeParametersResource,
    RangeParametersResourceWithRawResponse,
    AsyncRangeParametersResourceWithRawResponse,
    RangeParametersResourceWithStreamingResponse,
    AsyncRangeParametersResourceWithStreamingResponse,
)
from .classification_markings import (
    ClassificationMarkingsResource,
    AsyncClassificationMarkingsResource,
    ClassificationMarkingsResourceWithRawResponse,
    AsyncClassificationMarkingsResourceWithRawResponse,
    ClassificationMarkingsResourceWithStreamingResponse,
    AsyncClassificationMarkingsResourceWithStreamingResponse,
)
from ...types.sc_search_response import ScSearchResponse
from ...types.sc_aggregate_doc_type_response import ScAggregateDocTypeResponse
from ...types.sc_allowable_file_mimes_response import ScAllowableFileMimesResponse
from ...types.sc_allowable_file_extensions_response import ScAllowableFileExtensionsResponse

__all__ = ["ScsResource", "AsyncScsResource"]


class ScsResource(SyncAPIResource):
    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def classification_markings(self) -> ClassificationMarkingsResource:
        return ClassificationMarkingsResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def file_metadata(self) -> FileMetadataResource:
        return FileMetadataResource(self._client)

    @cached_property
    def range_parameters(self) -> RangeParametersResource:
        return RangeParametersResource(self._client)

    @cached_property
    def paths(self) -> PathsResource:
        return PathsResource(self._client)

    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def file(self) -> FileResource:
        return FileResource(self._client)

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

    def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def aggregate_doc_type(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScAggregateDocTypeResponse:
        """Returns a map of document types and counts in root folder."""
        return self._get(
            "/scs/aggregateDocType",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAggregateDocTypeResponse,
        )

    def allowable_file_extensions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScAllowableFileExtensionsResponse:
        """Returns a list of allowable file extensions for upload."""
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScAllowableFileMimesResponse:
        """Returns a list of allowable file mime types for upload."""
        return self._get(
            "/scs/allowableFileMimes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAllowableFileMimesResponse,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            body=maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def file_download(
        self,
        *,
        id: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def file_upload(
        self,
        *,
        classification_marking: str,
        file_name: str,
        path: str,
        body: FileTypes,
        description: str | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Operation to upload a file.

        A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification (ex. U//FOUO)

          file_name: FileName (ex. dog.jpg)

          path: The base path to upload file (ex. images)

          description: Description

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scs/file",
            body=maybe_transform(body, sc_file_upload_params.ScFileUploadParams),
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
                        "description": description,
                        "overwrite": overwrite,
                        "tags": tags,
                    },
                    sc_file_upload_params.ScFileUploadParams,
                ),
            ),
            cast_to=str,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """operation to move folders or files.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def search(
        self,
        *,
        path: str,
        count: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        content_criteria: str | NotGiven = NOT_GIVEN,
        meta_data_criteria: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        non_range_criteria: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        range_criteria: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        search_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def update_tags(
        self,
        *,
        folder: str,
        tags: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates tags for given folder.

        Args:
          folder: The base path to folder

          tags: The new tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/scs/updateTagsForFilesInFolder",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "folder": folder,
                        "tags": tags,
                    },
                    sc_update_tags_params.ScUpdateTagsParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncScsResource(AsyncAPIResource):
    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def classification_markings(self) -> AsyncClassificationMarkingsResource:
        return AsyncClassificationMarkingsResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def file_metadata(self) -> AsyncFileMetadataResource:
        return AsyncFileMetadataResource(self._client)

    @cached_property
    def range_parameters(self) -> AsyncRangeParametersResource:
        return AsyncRangeParametersResource(self._client)

    @cached_property
    def paths(self) -> AsyncPathsResource:
        return AsyncPathsResource(self._client)

    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def file(self) -> AsyncFileResource:
        return AsyncFileResource(self._client)

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

    async def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def aggregate_doc_type(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScAggregateDocTypeResponse:
        """Returns a map of document types and counts in root folder."""
        return await self._get(
            "/scs/aggregateDocType",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAggregateDocTypeResponse,
        )

    async def allowable_file_extensions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScAllowableFileExtensionsResponse:
        """Returns a list of allowable file extensions for upload."""
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScAllowableFileMimesResponse:
        """Returns a list of allowable file mime types for upload."""
        return await self._get(
            "/scs/allowableFileMimes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScAllowableFileMimesResponse,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            body=await async_maybe_transform(body, List[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def file_download(
        self,
        *,
        id: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def file_upload(
        self,
        *,
        classification_marking: str,
        file_name: str,
        path: str,
        body: FileTypes,
        description: str | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Operation to upload a file.

        A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification (ex. U//FOUO)

          file_name: FileName (ex. dog.jpg)

          path: The base path to upload file (ex. images)

          description: Description

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scs/file",
            body=await async_maybe_transform(body, sc_file_upload_params.ScFileUploadParams),
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
                        "description": description,
                        "overwrite": overwrite,
                        "tags": tags,
                    },
                    sc_file_upload_params.ScFileUploadParams,
                ),
            ),
            cast_to=str,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """operation to move folders or files.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def search(
        self,
        *,
        path: str,
        count: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        content_criteria: str | NotGiven = NOT_GIVEN,
        meta_data_criteria: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        non_range_criteria: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        range_criteria: Dict[str, List[str]] | NotGiven = NOT_GIVEN,
        search_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def update_tags(
        self,
        *,
        folder: str,
        tags: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates tags for given folder.

        Args:
          folder: The base path to folder

          tags: The new tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/scs/updateTagsForFilesInFolder",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "folder": folder,
                        "tags": tags,
                    },
                    sc_update_tags_params.ScUpdateTagsParams,
                ),
            ),
            cast_to=NoneType,
        )


class ScsResourceWithRawResponse:
    def __init__(self, scs: ScsResource) -> None:
        self._scs = scs

        self.delete = to_raw_response_wrapper(
            scs.delete,
        )
        self.aggregate_doc_type = to_raw_response_wrapper(
            scs.aggregate_doc_type,
        )
        self.allowable_file_extensions = to_raw_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = to_raw_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = to_raw_response_wrapper(
            scs.copy,
        )
        self.download = to_custom_raw_response_wrapper(
            scs.download,
            BinaryAPIResponse,
        )
        self.file_download = to_custom_raw_response_wrapper(
            scs.file_download,
            BinaryAPIResponse,
        )
        self.file_upload = to_raw_response_wrapper(
            scs.file_upload,
        )
        self.move = to_raw_response_wrapper(
            scs.move,
        )
        self.rename = to_raw_response_wrapper(
            scs.rename,
        )
        self.search = to_raw_response_wrapper(
            scs.search,
        )
        self.update_tags = to_raw_response_wrapper(
            scs.update_tags,
        )

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._scs.folders)

    @cached_property
    def classification_markings(self) -> ClassificationMarkingsResourceWithRawResponse:
        return ClassificationMarkingsResourceWithRawResponse(self._scs.classification_markings)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._scs.groups)

    @cached_property
    def file_metadata(self) -> FileMetadataResourceWithRawResponse:
        return FileMetadataResourceWithRawResponse(self._scs.file_metadata)

    @cached_property
    def range_parameters(self) -> RangeParametersResourceWithRawResponse:
        return RangeParametersResourceWithRawResponse(self._scs.range_parameters)

    @cached_property
    def paths(self) -> PathsResourceWithRawResponse:
        return PathsResourceWithRawResponse(self._scs.paths)

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._scs.v2)

    @cached_property
    def file(self) -> FileResourceWithRawResponse:
        return FileResourceWithRawResponse(self._scs.file)


class AsyncScsResourceWithRawResponse:
    def __init__(self, scs: AsyncScsResource) -> None:
        self._scs = scs

        self.delete = async_to_raw_response_wrapper(
            scs.delete,
        )
        self.aggregate_doc_type = async_to_raw_response_wrapper(
            scs.aggregate_doc_type,
        )
        self.allowable_file_extensions = async_to_raw_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = async_to_raw_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = async_to_raw_response_wrapper(
            scs.copy,
        )
        self.download = async_to_custom_raw_response_wrapper(
            scs.download,
            AsyncBinaryAPIResponse,
        )
        self.file_download = async_to_custom_raw_response_wrapper(
            scs.file_download,
            AsyncBinaryAPIResponse,
        )
        self.file_upload = async_to_raw_response_wrapper(
            scs.file_upload,
        )
        self.move = async_to_raw_response_wrapper(
            scs.move,
        )
        self.rename = async_to_raw_response_wrapper(
            scs.rename,
        )
        self.search = async_to_raw_response_wrapper(
            scs.search,
        )
        self.update_tags = async_to_raw_response_wrapper(
            scs.update_tags,
        )

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._scs.folders)

    @cached_property
    def classification_markings(self) -> AsyncClassificationMarkingsResourceWithRawResponse:
        return AsyncClassificationMarkingsResourceWithRawResponse(self._scs.classification_markings)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._scs.groups)

    @cached_property
    def file_metadata(self) -> AsyncFileMetadataResourceWithRawResponse:
        return AsyncFileMetadataResourceWithRawResponse(self._scs.file_metadata)

    @cached_property
    def range_parameters(self) -> AsyncRangeParametersResourceWithRawResponse:
        return AsyncRangeParametersResourceWithRawResponse(self._scs.range_parameters)

    @cached_property
    def paths(self) -> AsyncPathsResourceWithRawResponse:
        return AsyncPathsResourceWithRawResponse(self._scs.paths)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._scs.v2)

    @cached_property
    def file(self) -> AsyncFileResourceWithRawResponse:
        return AsyncFileResourceWithRawResponse(self._scs.file)


class ScsResourceWithStreamingResponse:
    def __init__(self, scs: ScsResource) -> None:
        self._scs = scs

        self.delete = to_streamed_response_wrapper(
            scs.delete,
        )
        self.aggregate_doc_type = to_streamed_response_wrapper(
            scs.aggregate_doc_type,
        )
        self.allowable_file_extensions = to_streamed_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = to_streamed_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = to_streamed_response_wrapper(
            scs.copy,
        )
        self.download = to_custom_streamed_response_wrapper(
            scs.download,
            StreamedBinaryAPIResponse,
        )
        self.file_download = to_custom_streamed_response_wrapper(
            scs.file_download,
            StreamedBinaryAPIResponse,
        )
        self.file_upload = to_streamed_response_wrapper(
            scs.file_upload,
        )
        self.move = to_streamed_response_wrapper(
            scs.move,
        )
        self.rename = to_streamed_response_wrapper(
            scs.rename,
        )
        self.search = to_streamed_response_wrapper(
            scs.search,
        )
        self.update_tags = to_streamed_response_wrapper(
            scs.update_tags,
        )

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._scs.folders)

    @cached_property
    def classification_markings(self) -> ClassificationMarkingsResourceWithStreamingResponse:
        return ClassificationMarkingsResourceWithStreamingResponse(self._scs.classification_markings)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._scs.groups)

    @cached_property
    def file_metadata(self) -> FileMetadataResourceWithStreamingResponse:
        return FileMetadataResourceWithStreamingResponse(self._scs.file_metadata)

    @cached_property
    def range_parameters(self) -> RangeParametersResourceWithStreamingResponse:
        return RangeParametersResourceWithStreamingResponse(self._scs.range_parameters)

    @cached_property
    def paths(self) -> PathsResourceWithStreamingResponse:
        return PathsResourceWithStreamingResponse(self._scs.paths)

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._scs.v2)

    @cached_property
    def file(self) -> FileResourceWithStreamingResponse:
        return FileResourceWithStreamingResponse(self._scs.file)


class AsyncScsResourceWithStreamingResponse:
    def __init__(self, scs: AsyncScsResource) -> None:
        self._scs = scs

        self.delete = async_to_streamed_response_wrapper(
            scs.delete,
        )
        self.aggregate_doc_type = async_to_streamed_response_wrapper(
            scs.aggregate_doc_type,
        )
        self.allowable_file_extensions = async_to_streamed_response_wrapper(
            scs.allowable_file_extensions,
        )
        self.allowable_file_mimes = async_to_streamed_response_wrapper(
            scs.allowable_file_mimes,
        )
        self.copy = async_to_streamed_response_wrapper(
            scs.copy,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            scs.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.file_download = async_to_custom_streamed_response_wrapper(
            scs.file_download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.file_upload = async_to_streamed_response_wrapper(
            scs.file_upload,
        )
        self.move = async_to_streamed_response_wrapper(
            scs.move,
        )
        self.rename = async_to_streamed_response_wrapper(
            scs.rename,
        )
        self.search = async_to_streamed_response_wrapper(
            scs.search,
        )
        self.update_tags = async_to_streamed_response_wrapper(
            scs.update_tags,
        )

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._scs.folders)

    @cached_property
    def classification_markings(self) -> AsyncClassificationMarkingsResourceWithStreamingResponse:
        return AsyncClassificationMarkingsResourceWithStreamingResponse(self._scs.classification_markings)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._scs.groups)

    @cached_property
    def file_metadata(self) -> AsyncFileMetadataResourceWithStreamingResponse:
        return AsyncFileMetadataResourceWithStreamingResponse(self._scs.file_metadata)

    @cached_property
    def range_parameters(self) -> AsyncRangeParametersResourceWithStreamingResponse:
        return AsyncRangeParametersResourceWithStreamingResponse(self._scs.range_parameters)

    @cached_property
    def paths(self) -> AsyncPathsResourceWithStreamingResponse:
        return AsyncPathsResourceWithStreamingResponse(self._scs.paths)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._scs.v2)

    @cached_property
    def file(self) -> AsyncFileResourceWithStreamingResponse:
        return AsyncFileResourceWithStreamingResponse(self._scs.file)
