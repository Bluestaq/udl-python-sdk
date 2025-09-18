# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .offset import (
    OffsetResource,
    AsyncOffsetResource,
    OffsetResourceWithRawResponse,
    AsyncOffsetResourceWithRawResponse,
    OffsetResourceWithStreamingResponse,
    AsyncOffsetResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.scs import notification_list_params
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.scs.notification_list_response import NotificationListResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def offset(self) -> OffsetResource:
        return OffsetResource(self._client)

    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def list(
        self,
        offset: str,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[NotificationListResponse]:
        """
        Returns a list of notifications for items in a specific folder.

        Args:
          path: Path of the folder to retrieve notification for. Must start and end with /. If
              no path is specified, all notifications will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return self._get_api_list(
            f"/scs/notifications/{offset}",
            page=SyncOffsetPage[NotificationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                        "path": path,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            model=NotificationListResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def offset(self) -> AsyncOffsetResource:
        return AsyncOffsetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    def list(
        self,
        offset: str,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NotificationListResponse, AsyncOffsetPage[NotificationListResponse]]:
        """
        Returns a list of notifications for items in a specific folder.

        Args:
          path: Path of the folder to retrieve notification for. Must start and end with /. If
              no path is specified, all notifications will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offset:
            raise ValueError(f"Expected a non-empty value for `offset` but received {offset!r}")
        return self._get_api_list(
            f"/scs/notifications/{offset}",
            page=AsyncOffsetPage[NotificationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                        "path": path,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            model=NotificationListResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_raw_response_wrapper(
            notifications.list,
        )

    @cached_property
    def offset(self) -> OffsetResourceWithRawResponse:
        return OffsetResourceWithRawResponse(self._notifications.offset)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )

    @cached_property
    def offset(self) -> AsyncOffsetResourceWithRawResponse:
        return AsyncOffsetResourceWithRawResponse(self._notifications.offset)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_streamed_response_wrapper(
            notifications.list,
        )

    @cached_property
    def offset(self) -> OffsetResourceWithStreamingResponse:
        return OffsetResourceWithStreamingResponse(self._notifications.offset)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )

    @cached_property
    def offset(self) -> AsyncOffsetResourceWithStreamingResponse:
        return AsyncOffsetResourceWithStreamingResponse(self._notifications.offset)
