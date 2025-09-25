# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_auth_response import UserAuthResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def auth(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAuthResponse:
        """Retrieve authentication details for the current user"""
        return self._get(
            "/basicAuth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAuthResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def auth(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAuthResponse:
        """Retrieve authentication details for the current user"""
        return await self._get(
            "/basicAuth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAuthResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.auth = to_raw_response_wrapper(
            user.auth,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.auth = async_to_raw_response_wrapper(
            user.auth,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.auth = to_streamed_response_wrapper(
            user.auth,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.auth = async_to_streamed_response_wrapper(
            user.auth,
        )
