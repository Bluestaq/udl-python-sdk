# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scs import folder_create_params, folder_update_params, folder_retrieve_params
from ..._base_client import make_request_options
from ...types.shared.file_data import FileData

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        id: str,
        classification_marking: str,
        description: str | Omit = omit,
        read: str | Omit = omit,
        send_notification: bool | Omit = omit,
        tags: str | Omit = omit,
        write: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Creates a new folder that is passed as part of the path.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          id: Path to create folder.

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          description: Optional description to include on folder.

          read: Comma separated list of user ids who can read contents of the folder.

          send_notification: Whether or not to send a notification that this folder was created.

          tags: Comma separated list of tags to add to the folder.

          write: Comma separated list of user ids who can write to the folder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scs/folder",
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
                        "read": read,
                        "send_notification": send_notification,
                        "tags": tags,
                        "write": write,
                    },
                    folder_create_params.FolderCreateParams,
                ),
            ),
            cast_to=str,
        )

    @typing_extensions.deprecated("deprecated")
    def retrieve(
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
    ) -> FileData:
        """
        Returns a FileData object representing the folder ID that is visible to the
        calling user.

        Args:
          id: The folder ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/scs/folder",
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
                    folder_retrieve_params.FolderRetrieveParams,
                ),
            ),
            cast_to=FileData,
        )

    @typing_extensions.deprecated("deprecated")
    def update(
        self,
        *,
        id: str | Omit = omit,
        attributes: folder_update_params.Attributes | Omit = omit,
        target_name: str | Omit = omit,
        target_path: str | Omit = omit,
        type: Literal["file", "folder", "summary"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """operation to update folders metadata.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/scs/folder",
            body=maybe_transform(
                {
                    "id": id,
                    "attributes": attributes,
                    "target_name": target_name,
                    "target_path": target_path,
                    "type": type,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        id: str,
        classification_marking: str,
        description: str | Omit = omit,
        read: str | Omit = omit,
        send_notification: bool | Omit = omit,
        tags: str | Omit = omit,
        write: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Creates a new folder that is passed as part of the path.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          id: Path to create folder.

          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          description: Optional description to include on folder.

          read: Comma separated list of user ids who can read contents of the folder.

          send_notification: Whether or not to send a notification that this folder was created.

          tags: Comma separated list of tags to add to the folder.

          write: Comma separated list of user ids who can write to the folder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scs/folder",
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
                        "read": read,
                        "send_notification": send_notification,
                        "tags": tags,
                        "write": write,
                    },
                    folder_create_params.FolderCreateParams,
                ),
            ),
            cast_to=str,
        )

    @typing_extensions.deprecated("deprecated")
    async def retrieve(
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
    ) -> FileData:
        """
        Returns a FileData object representing the folder ID that is visible to the
        calling user.

        Args:
          id: The folder ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/scs/folder",
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
                    folder_retrieve_params.FolderRetrieveParams,
                ),
            ),
            cast_to=FileData,
        )

    @typing_extensions.deprecated("deprecated")
    async def update(
        self,
        *,
        id: str | Omit = omit,
        attributes: folder_update_params.Attributes | Omit = omit,
        target_name: str | Omit = omit,
        target_path: str | Omit = omit,
        type: Literal["file", "folder", "summary"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """operation to update folders metadata.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/scs/folder",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "attributes": attributes,
                    "target_name": target_name,
                    "target_path": target_path,
                    "type": type,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                folders.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                folders.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                folders.update,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                folders.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                folders.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                folders.update,  # pyright: ignore[reportDeprecated],
            )
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                folders.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                folders.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                folders.update,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                folders.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                folders.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                folders.update,  # pyright: ignore[reportDeprecated],
            )
        )
