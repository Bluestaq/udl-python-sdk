# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._files import read_file_content, async_read_file_content
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileContent
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scs import path_create_with_file_params
from ..._base_client import make_request_options

__all__ = ["PathsResource", "AsyncPathsResource"]


class PathsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return PathsResourceWithStreamingResponse(self)

    def create_with_file(
        self,
        file_content: FileContent,
        *,
        id: str,
        classification_marking: str,
        delete_after: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        send_notification: bool | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Creates the path and uploads file that is passed.

        If folder exist it will only
        create folders that are missing. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The full path to create, including path and file name

          classification_marking: Classification (ex. U//FOUO)

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
            "/scs/path",
            body=read_file_content(file_content),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "classification_marking": classification_marking,
                        "delete_after": delete_after,
                        "description": description,
                        "overwrite": overwrite,
                        "send_notification": send_notification,
                        "tags": tags,
                    },
                    path_create_with_file_params.PathCreateWithFileParams,
                ),
            ),
            cast_to=str,
        )


class AsyncPathsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncPathsResourceWithStreamingResponse(self)

    async def create_with_file(
        self,
        file_content: FileContent,
        *,
        id: str,
        classification_marking: str,
        delete_after: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        send_notification: bool | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Creates the path and uploads file that is passed.

        If folder exist it will only
        create folders that are missing. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The full path to create, including path and file name

          classification_marking: Classification (ex. U//FOUO)

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
            "/scs/path",
            body=await async_read_file_content(file_content),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "classification_marking": classification_marking,
                        "delete_after": delete_after,
                        "description": description,
                        "overwrite": overwrite,
                        "send_notification": send_notification,
                        "tags": tags,
                    },
                    path_create_with_file_params.PathCreateWithFileParams,
                ),
            ),
            cast_to=str,
        )


class PathsResourceWithRawResponse:
    def __init__(self, paths: PathsResource) -> None:
        self._paths = paths

        self.create_with_file = to_raw_response_wrapper(
            paths.create_with_file,
        )


class AsyncPathsResourceWithRawResponse:
    def __init__(self, paths: AsyncPathsResource) -> None:
        self._paths = paths

        self.create_with_file = async_to_raw_response_wrapper(
            paths.create_with_file,
        )


class PathsResourceWithStreamingResponse:
    def __init__(self, paths: PathsResource) -> None:
        self._paths = paths

        self.create_with_file = to_streamed_response_wrapper(
            paths.create_with_file,
        )


class AsyncPathsResourceWithStreamingResponse:
    def __init__(self, paths: AsyncPathsResource) -> None:
        self._paths = paths

        self.create_with_file = async_to_streamed_response_wrapper(
            paths.create_with_file,
        )
