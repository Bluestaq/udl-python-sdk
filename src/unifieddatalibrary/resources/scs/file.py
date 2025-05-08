# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scs import file_list_params, file_update_params, file_retrieve_params
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.file_data import FileData as SharedFileData
from ...types.shared_params.file_data import FileData as SharedParamsFileData

__all__ = ["FileResource", "AsyncFileResource"]


class FileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return FileResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> SharedFileData:
        """
        Returns a FileData object representing the file with the given ID that is
        visible to the calling user.

        Args:
          id: The file ID to view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/scs/file",
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
                    file_retrieve_params.FileRetrieveParams,
                ),
            ),
            cast_to=SharedFileData,
        )

    def update(
        self,
        *,
        file_data_list: Iterable[SharedParamsFileData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """operation to update files metadata.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/scs/file",
            body=maybe_transform({"file_data_list": file_data_list}, file_update_params.FileUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        path: str,
        count: int | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SharedFileData]:
        """
        Returns a non-recursive list of FileData objects representing the files and
        subdirectories in the passed-in path directory that are visible to the calling
        user.

        Args:
          path: The base path to list

          count: Number of items per page

          offset: First result to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/scs/list",
            page=SyncOffsetPage[SharedFileData],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "count": count,
                        "first_result": first_result,
                        "max_results": max_results,
                        "offset": offset,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=SharedFileData,
        )


class AsyncFileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncFileResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> SharedFileData:
        """
        Returns a FileData object representing the file with the given ID that is
        visible to the calling user.

        Args:
          id: The file ID to view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/scs/file",
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
                    file_retrieve_params.FileRetrieveParams,
                ),
            ),
            cast_to=SharedFileData,
        )

    async def update(
        self,
        *,
        file_data_list: Iterable[SharedParamsFileData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """operation to update files metadata.

        A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/scs/file",
            body=await async_maybe_transform({"file_data_list": file_data_list}, file_update_params.FileUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        path: str,
        count: int | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SharedFileData, AsyncOffsetPage[SharedFileData]]:
        """
        Returns a non-recursive list of FileData objects representing the files and
        subdirectories in the passed-in path directory that are visible to the calling
        user.

        Args:
          path: The base path to list

          count: Number of items per page

          offset: First result to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/scs/list",
            page=AsyncOffsetPage[SharedFileData],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "count": count,
                        "first_result": first_result,
                        "max_results": max_results,
                        "offset": offset,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=SharedFileData,
        )


class FileResourceWithRawResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.retrieve = to_raw_response_wrapper(
            file.retrieve,
        )
        self.update = to_raw_response_wrapper(
            file.update,
        )
        self.list = to_raw_response_wrapper(
            file.list,
        )


class AsyncFileResourceWithRawResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.retrieve = async_to_raw_response_wrapper(
            file.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            file.update,
        )
        self.list = async_to_raw_response_wrapper(
            file.list,
        )


class FileResourceWithStreamingResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.retrieve = to_streamed_response_wrapper(
            file.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            file.update,
        )
        self.list = to_streamed_response_wrapper(
            file.list,
        )


class AsyncFileResourceWithStreamingResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.retrieve = async_to_streamed_response_wrapper(
            file.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            file.update,
        )
        self.list = async_to_streamed_response_wrapper(
            file.list,
        )
