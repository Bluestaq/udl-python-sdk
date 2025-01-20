# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.filedrop.observation import onboardnavigation_create_params

__all__ = ["OnboardnavigationResource", "AsyncOnboardnavigationResource"]


class OnboardnavigationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnboardnavigationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return OnboardnavigationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnboardnavigationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return OnboardnavigationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: Iterable[onboardnavigation_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of onboard navigation records as a POST body
        and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-onboardnavigation",
            body=maybe_transform(body, Iterable[onboardnavigation_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOnboardnavigationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnboardnavigationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnboardnavigationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnboardnavigationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncOnboardnavigationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: Iterable[onboardnavigation_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of onboard navigation records as a POST body
        and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-onboardnavigation",
            body=await async_maybe_transform(body, Iterable[onboardnavigation_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OnboardnavigationResourceWithRawResponse:
    def __init__(self, onboardnavigation: OnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

        self.create = to_raw_response_wrapper(
            onboardnavigation.create,
        )


class AsyncOnboardnavigationResourceWithRawResponse:
    def __init__(self, onboardnavigation: AsyncOnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

        self.create = async_to_raw_response_wrapper(
            onboardnavigation.create,
        )


class OnboardnavigationResourceWithStreamingResponse:
    def __init__(self, onboardnavigation: OnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

        self.create = to_streamed_response_wrapper(
            onboardnavigation.create,
        )


class AsyncOnboardnavigationResourceWithStreamingResponse:
    def __init__(self, onboardnavigation: AsyncOnboardnavigationResource) -> None:
        self._onboardnavigation = onboardnavigation

        self.create = async_to_streamed_response_wrapper(
            onboardnavigation.create,
        )
