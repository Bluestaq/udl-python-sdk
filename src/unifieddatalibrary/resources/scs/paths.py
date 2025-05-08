# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scs import path_create_params
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

    def create(
        self,
        *,
        id: str,
        classification_marking: str,
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
        """Creates the path and uploads file that is passed.

        If folder exist it will only
        create folders that are missing. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The full path to create, including path and file name

          classification_marking: Classification (ex. U//FOUO)

          description: Description

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scs/path",
            body=maybe_transform(body, path_create_params.PathCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "classification_marking": classification_marking,
                        "description": description,
                        "overwrite": overwrite,
                        "tags": tags,
                    },
                    path_create_params.PathCreateParams,
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

    async def create(
        self,
        *,
        id: str,
        classification_marking: str,
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
        """Creates the path and uploads file that is passed.

        If folder exist it will only
        create folders that are missing. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

        Args:
          id: The full path to create, including path and file name

          classification_marking: Classification (ex. U//FOUO)

          description: Description

          overwrite: Whether or not to overwrite a file with the same name and path, if one exists.

          tags: Tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scs/path",
            body=await async_maybe_transform(body, path_create_params.PathCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "classification_marking": classification_marking,
                        "description": description,
                        "overwrite": overwrite,
                        "tags": tags,
                    },
                    path_create_params.PathCreateParams,
                ),
            ),
            cast_to=str,
        )


class PathsResourceWithRawResponse:
    def __init__(self, paths: PathsResource) -> None:
        self._paths = paths

        self.create = to_raw_response_wrapper(
            paths.create,
        )


class AsyncPathsResourceWithRawResponse:
    def __init__(self, paths: AsyncPathsResource) -> None:
        self._paths = paths

        self.create = async_to_raw_response_wrapper(
            paths.create,
        )


class PathsResourceWithStreamingResponse:
    def __init__(self, paths: PathsResource) -> None:
        self._paths = paths

        self.create = to_streamed_response_wrapper(
            paths.create,
        )


class AsyncPathsResourceWithStreamingResponse:
    def __init__(self, paths: AsyncPathsResource) -> None:
        self._paths = paths

        self.create = async_to_streamed_response_wrapper(
            paths.create,
        )
