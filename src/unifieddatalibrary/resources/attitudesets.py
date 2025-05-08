# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import attitudeset_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.attitudeset_full import AttitudesetFull

__all__ = ["AttitudesetsResource", "AsyncAttitudesetsResource"]


class AttitudesetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttitudesetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AttitudesetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttitudesetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AttitudesetsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudesetFull:
        """
        Service operation to get a single AttitudeSet record by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/attitudeset/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitudeset_retrieve_params.AttitudesetRetrieveParams,
                ),
            ),
            cast_to=AttitudesetFull,
        )


class AsyncAttitudesetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttitudesetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAttitudesetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttitudesetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAttitudesetsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudesetFull:
        """
        Service operation to get a single AttitudeSet record by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/attitudeset/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitudeset_retrieve_params.AttitudesetRetrieveParams,
                ),
            ),
            cast_to=AttitudesetFull,
        )


class AttitudesetsResourceWithRawResponse:
    def __init__(self, attitudesets: AttitudesetsResource) -> None:
        self._attitudesets = attitudesets

        self.retrieve = to_raw_response_wrapper(
            attitudesets.retrieve,
        )


class AsyncAttitudesetsResourceWithRawResponse:
    def __init__(self, attitudesets: AsyncAttitudesetsResource) -> None:
        self._attitudesets = attitudesets

        self.retrieve = async_to_raw_response_wrapper(
            attitudesets.retrieve,
        )


class AttitudesetsResourceWithStreamingResponse:
    def __init__(self, attitudesets: AttitudesetsResource) -> None:
        self._attitudesets = attitudesets

        self.retrieve = to_streamed_response_wrapper(
            attitudesets.retrieve,
        )


class AsyncAttitudesetsResourceWithStreamingResponse:
    def __init__(self, attitudesets: AsyncAttitudesetsResource) -> None:
        self._attitudesets = attitudesets

        self.retrieve = async_to_streamed_response_wrapper(
            attitudesets.retrieve,
        )
