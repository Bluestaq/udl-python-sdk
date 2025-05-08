# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.air_operations import diplomatic_clearance_unvalidated_publish_params

__all__ = ["DiplomaticClearanceResource", "AsyncDiplomaticClearanceResource"]


class DiplomaticClearanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiplomaticClearanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DiplomaticClearanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiplomaticClearanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DiplomaticClearanceResourceWithStreamingResponse(self)

    def unvalidated_publish(
        self,
        *,
        body: Iterable[diplomatic_clearance_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple Diplomatic Clearance records as a POST body
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
            "/filedrop/udl-diplomaticclearance",
            body=maybe_transform(body, Iterable[diplomatic_clearance_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDiplomaticClearanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiplomaticClearanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDiplomaticClearanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiplomaticClearanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDiplomaticClearanceResourceWithStreamingResponse(self)

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[diplomatic_clearance_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple Diplomatic Clearance records as a POST body
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
            "/filedrop/udl-diplomaticclearance",
            body=await async_maybe_transform(body, Iterable[diplomatic_clearance_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DiplomaticClearanceResourceWithRawResponse:
    def __init__(self, diplomatic_clearance: DiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.unvalidated_publish = to_raw_response_wrapper(
            diplomatic_clearance.unvalidated_publish,
        )


class AsyncDiplomaticClearanceResourceWithRawResponse:
    def __init__(self, diplomatic_clearance: AsyncDiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.unvalidated_publish = async_to_raw_response_wrapper(
            diplomatic_clearance.unvalidated_publish,
        )


class DiplomaticClearanceResourceWithStreamingResponse:
    def __init__(self, diplomatic_clearance: DiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.unvalidated_publish = to_streamed_response_wrapper(
            diplomatic_clearance.unvalidated_publish,
        )


class AsyncDiplomaticClearanceResourceWithStreamingResponse:
    def __init__(self, diplomatic_clearance: AsyncDiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.unvalidated_publish = async_to_streamed_response_wrapper(
            diplomatic_clearance.unvalidated_publish,
        )
