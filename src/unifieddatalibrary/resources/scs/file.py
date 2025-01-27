# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scs import file_update_params
from ..._base_client import make_request_options
from ...types.shared.file_data import FileData as SharedFileData
from ...types.shared_params.file_data import FileData as SharedParamsFileData

__all__ = ["FileResource", "AsyncFileResource"]


class FileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return FileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return FileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
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
        """
        return self._get(
            "/scs/file",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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


class AsyncFileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncFileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
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
        """
        return await self._get(
            "/scs/file",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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


class FileResourceWithRawResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.retrieve = to_raw_response_wrapper(
            file.retrieve,
        )
        self.update = to_raw_response_wrapper(
            file.update,
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


class FileResourceWithStreamingResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.retrieve = to_streamed_response_wrapper(
            file.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            file.update,
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
