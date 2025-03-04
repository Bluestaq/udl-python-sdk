# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    secure_messaging_get_messages_params,
    secure_messaging_describe_topic_params,
    secure_messaging_get_latest_offset_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.topic_details import TopicDetails
from ..types.secure_messaging_list_topics_response import SecureMessagingListTopicsResponse

__all__ = ["SecureMessagingResource", "AsyncSecureMessagingResource"]


class SecureMessagingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecureMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return SecureMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecureMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return SecureMessagingResourceWithStreamingResponse(self)

    def describe_topic(
        self,
        path_topic: str,
        *,
        query_topic: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopicDetails:
        """
        Retrieve the details of the specified topic or data type.

        Args:
          query_topic: The topic to be described.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_topic:
            raise ValueError(f"Expected a non-empty value for `path_topic` but received {path_topic!r}")
        return self._get(
            f"/sm/describeTopic/{path_topic}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"query_topic": query_topic},
                    secure_messaging_describe_topic_params.SecureMessagingDescribeTopicParams,
                ),
            ),
            cast_to=TopicDetails,
        )

    def get_latest_offset(
        self,
        path_topic: str,
        *,
        query_topic: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns the current/latest offset for the passed topic name.

        Args:
          query_topic: The topic name to return the latest offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_topic:
            raise ValueError(f"Expected a non-empty value for `path_topic` but received {path_topic!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/sm/getLatestOffset/{path_topic}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"query_topic": query_topic},
                    secure_messaging_get_latest_offset_params.SecureMessagingGetLatestOffsetParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_messages(
        self,
        path_offset: str,
        *,
        path_topic: str,
        query_offset: int,
        query_topic: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retrieve a set of messages from the given topic at the given offset.

        See Help >
        Secure Messaging API on Storefront for more details on how to use getMessages.

        Args:
          query_offset: The message offset.

          query_topic: The topic from which messages are to be retrieved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_topic:
            raise ValueError(f"Expected a non-empty value for `path_topic` but received {path_topic!r}")
        if not path_offset:
            raise ValueError(f"Expected a non-empty value for `path_offset` but received {path_offset!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/sm/getMessages/{path_topic}/{path_offset}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query_offset": query_offset,
                        "query_topic": query_topic,
                    },
                    secure_messaging_get_messages_params.SecureMessagingGetMessagesParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_topics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureMessagingListTopicsResponse:
        """Retrieve the list of available secure messaging topics or data types available."""
        return self._get(
            "/sm/listTopics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureMessagingListTopicsResponse,
        )


class AsyncSecureMessagingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecureMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecureMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecureMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncSecureMessagingResourceWithStreamingResponse(self)

    async def describe_topic(
        self,
        path_topic: str,
        *,
        query_topic: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopicDetails:
        """
        Retrieve the details of the specified topic or data type.

        Args:
          query_topic: The topic to be described.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_topic:
            raise ValueError(f"Expected a non-empty value for `path_topic` but received {path_topic!r}")
        return await self._get(
            f"/sm/describeTopic/{path_topic}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_topic": query_topic},
                    secure_messaging_describe_topic_params.SecureMessagingDescribeTopicParams,
                ),
            ),
            cast_to=TopicDetails,
        )

    async def get_latest_offset(
        self,
        path_topic: str,
        *,
        query_topic: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Returns the current/latest offset for the passed topic name.

        Args:
          query_topic: The topic name to return the latest offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_topic:
            raise ValueError(f"Expected a non-empty value for `path_topic` but received {path_topic!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/sm/getLatestOffset/{path_topic}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_topic": query_topic},
                    secure_messaging_get_latest_offset_params.SecureMessagingGetLatestOffsetParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_messages(
        self,
        path_offset: str,
        *,
        path_topic: str,
        query_offset: int,
        query_topic: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retrieve a set of messages from the given topic at the given offset.

        See Help >
        Secure Messaging API on Storefront for more details on how to use getMessages.

        Args:
          query_offset: The message offset.

          query_topic: The topic from which messages are to be retrieved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_topic:
            raise ValueError(f"Expected a non-empty value for `path_topic` but received {path_topic!r}")
        if not path_offset:
            raise ValueError(f"Expected a non-empty value for `path_offset` but received {path_offset!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/sm/getMessages/{path_topic}/{path_offset}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query_offset": query_offset,
                        "query_topic": query_topic,
                    },
                    secure_messaging_get_messages_params.SecureMessagingGetMessagesParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_topics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecureMessagingListTopicsResponse:
        """Retrieve the list of available secure messaging topics or data types available."""
        return await self._get(
            "/sm/listTopics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecureMessagingListTopicsResponse,
        )


class SecureMessagingResourceWithRawResponse:
    def __init__(self, secure_messaging: SecureMessagingResource) -> None:
        self._secure_messaging = secure_messaging

        self.describe_topic = to_raw_response_wrapper(
            secure_messaging.describe_topic,
        )
        self.get_latest_offset = to_raw_response_wrapper(
            secure_messaging.get_latest_offset,
        )
        self.get_messages = to_raw_response_wrapper(
            secure_messaging.get_messages,
        )
        self.list_topics = to_raw_response_wrapper(
            secure_messaging.list_topics,
        )


class AsyncSecureMessagingResourceWithRawResponse:
    def __init__(self, secure_messaging: AsyncSecureMessagingResource) -> None:
        self._secure_messaging = secure_messaging

        self.describe_topic = async_to_raw_response_wrapper(
            secure_messaging.describe_topic,
        )
        self.get_latest_offset = async_to_raw_response_wrapper(
            secure_messaging.get_latest_offset,
        )
        self.get_messages = async_to_raw_response_wrapper(
            secure_messaging.get_messages,
        )
        self.list_topics = async_to_raw_response_wrapper(
            secure_messaging.list_topics,
        )


class SecureMessagingResourceWithStreamingResponse:
    def __init__(self, secure_messaging: SecureMessagingResource) -> None:
        self._secure_messaging = secure_messaging

        self.describe_topic = to_streamed_response_wrapper(
            secure_messaging.describe_topic,
        )
        self.get_latest_offset = to_streamed_response_wrapper(
            secure_messaging.get_latest_offset,
        )
        self.get_messages = to_streamed_response_wrapper(
            secure_messaging.get_messages,
        )
        self.list_topics = to_streamed_response_wrapper(
            secure_messaging.list_topics,
        )


class AsyncSecureMessagingResourceWithStreamingResponse:
    def __init__(self, secure_messaging: AsyncSecureMessagingResource) -> None:
        self._secure_messaging = secure_messaging

        self.describe_topic = async_to_streamed_response_wrapper(
            secure_messaging.describe_topic,
        )
        self.get_latest_offset = async_to_streamed_response_wrapper(
            secure_messaging.get_latest_offset,
        )
        self.get_messages = async_to_streamed_response_wrapper(
            secure_messaging.get_messages,
        )
        self.list_topics = async_to_streamed_response_wrapper(
            secure_messaging.list_topics,
        )
