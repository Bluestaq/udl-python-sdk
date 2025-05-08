# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.scs.range_parameter_list_response import RangeParameterListResponse

__all__ = ["RangeParametersResource", "AsyncRangeParametersResource"]


class RangeParametersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RangeParametersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RangeParametersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RangeParametersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return RangeParametersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RangeParameterListResponse:
        """Returns a set of File Metadata that can be used for search endpoint."""
        return self._get(
            "/scs/listRangeParameters",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RangeParameterListResponse,
        )


class AsyncRangeParametersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRangeParametersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRangeParametersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRangeParametersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncRangeParametersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RangeParameterListResponse:
        """Returns a set of File Metadata that can be used for search endpoint."""
        return await self._get(
            "/scs/listRangeParameters",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RangeParameterListResponse,
        )


class RangeParametersResourceWithRawResponse:
    def __init__(self, range_parameters: RangeParametersResource) -> None:
        self._range_parameters = range_parameters

        self.list = to_raw_response_wrapper(
            range_parameters.list,
        )


class AsyncRangeParametersResourceWithRawResponse:
    def __init__(self, range_parameters: AsyncRangeParametersResource) -> None:
        self._range_parameters = range_parameters

        self.list = async_to_raw_response_wrapper(
            range_parameters.list,
        )


class RangeParametersResourceWithStreamingResponse:
    def __init__(self, range_parameters: RangeParametersResource) -> None:
        self._range_parameters = range_parameters

        self.list = to_streamed_response_wrapper(
            range_parameters.list,
        )


class AsyncRangeParametersResourceWithStreamingResponse:
    def __init__(self, range_parameters: AsyncRangeParametersResource) -> None:
        self._range_parameters = range_parameters

        self.list = async_to_streamed_response_wrapper(
            range_parameters.list,
        )
