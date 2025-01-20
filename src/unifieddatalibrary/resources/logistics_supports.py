# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import logistics_support_create_params
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

__all__ = ["LogisticsSupportsResource", "AsyncLogisticsSupportsResource"]


class LogisticsSupportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogisticsSupportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return LogisticsSupportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogisticsSupportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return LogisticsSupportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: Iterable[logistics_support_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple logisticssupport records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-logisticssupport",
            body=maybe_transform(body, Iterable[logistics_support_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLogisticsSupportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogisticsSupportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogisticsSupportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogisticsSupportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncLogisticsSupportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: Iterable[logistics_support_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple logisticssupport records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-logisticssupport",
            body=await async_maybe_transform(body, Iterable[logistics_support_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LogisticsSupportsResourceWithRawResponse:
    def __init__(self, logistics_supports: LogisticsSupportsResource) -> None:
        self._logistics_supports = logistics_supports

        self.create = to_raw_response_wrapper(
            logistics_supports.create,
        )


class AsyncLogisticsSupportsResourceWithRawResponse:
    def __init__(self, logistics_supports: AsyncLogisticsSupportsResource) -> None:
        self._logistics_supports = logistics_supports

        self.create = async_to_raw_response_wrapper(
            logistics_supports.create,
        )


class LogisticsSupportsResourceWithStreamingResponse:
    def __init__(self, logistics_supports: LogisticsSupportsResource) -> None:
        self._logistics_supports = logistics_supports

        self.create = to_streamed_response_wrapper(
            logistics_supports.create,
        )


class AsyncLogisticsSupportsResourceWithStreamingResponse:
    def __init__(self, logistics_supports: AsyncLogisticsSupportsResource) -> None:
        self._logistics_supports = logistics_supports

        self.create = async_to_streamed_response_wrapper(
            logistics_supports.create,
        )
