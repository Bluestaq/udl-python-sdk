# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.scs.notifications.offset_get_response import OffsetGetResponse

__all__ = ["OffsetResource", "AsyncOffsetResource"]


class OffsetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OffsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OffsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OffsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OffsetResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetGetResponse:
        """Retrieve the min and max offsets of the SCS Event Notification Kafka topic."""
        return self._get(
            "/scs/notifications/offsets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetGetResponse,
        )

    def get_latest(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns the current/latest offset for the SCS Event Notification Kafka topic."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/scs/notifications/getLatestOffset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOffsetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOffsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOffsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOffsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOffsetResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetGetResponse:
        """Retrieve the min and max offsets of the SCS Event Notification Kafka topic."""
        return await self._get(
            "/scs/notifications/offsets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetGetResponse,
        )

    async def get_latest(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns the current/latest offset for the SCS Event Notification Kafka topic."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/scs/notifications/getLatestOffset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OffsetResourceWithRawResponse:
    def __init__(self, offset: OffsetResource) -> None:
        self._offset = offset

        self.get = to_raw_response_wrapper(
            offset.get,
        )
        self.get_latest = to_raw_response_wrapper(
            offset.get_latest,
        )


class AsyncOffsetResourceWithRawResponse:
    def __init__(self, offset: AsyncOffsetResource) -> None:
        self._offset = offset

        self.get = async_to_raw_response_wrapper(
            offset.get,
        )
        self.get_latest = async_to_raw_response_wrapper(
            offset.get_latest,
        )


class OffsetResourceWithStreamingResponse:
    def __init__(self, offset: OffsetResource) -> None:
        self._offset = offset

        self.get = to_streamed_response_wrapper(
            offset.get,
        )
        self.get_latest = to_streamed_response_wrapper(
            offset.get_latest,
        )


class AsyncOffsetResourceWithStreamingResponse:
    def __init__(self, offset: AsyncOffsetResource) -> None:
        self._offset = offset

        self.get = async_to_streamed_response_wrapper(
            offset.get,
        )
        self.get_latest = async_to_streamed_response_wrapper(
            offset.get_latest,
        )
