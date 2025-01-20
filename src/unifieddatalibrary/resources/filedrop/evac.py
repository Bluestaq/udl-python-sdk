# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.filedrop import evac_create_params

__all__ = ["EvacResource", "AsyncEvacResource"]


class EvacResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvacResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return EvacResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvacResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return EvacResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: Iterable[evac_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Evac events as a POST body and ingest into
        the database. Requires a specific role, please contact the UDL team to gain
        access. This operation is intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-evac",
            body=maybe_transform(body, Iterable[evac_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvacResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvacResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvacResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvacResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncEvacResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: Iterable[evac_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Evac events as a POST body and ingest into
        the database. Requires a specific role, please contact the UDL team to gain
        access. This operation is intended to be used for automated feeds into UDL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-evac",
            body=await async_maybe_transform(body, Iterable[evac_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvacResourceWithRawResponse:
    def __init__(self, evac: EvacResource) -> None:
        self._evac = evac

        self.create = to_raw_response_wrapper(
            evac.create,
        )


class AsyncEvacResourceWithRawResponse:
    def __init__(self, evac: AsyncEvacResource) -> None:
        self._evac = evac

        self.create = async_to_raw_response_wrapper(
            evac.create,
        )


class EvacResourceWithStreamingResponse:
    def __init__(self, evac: EvacResource) -> None:
        self._evac = evac

        self.create = to_streamed_response_wrapper(
            evac.create,
        )


class AsyncEvacResourceWithStreamingResponse:
    def __init__(self, evac: AsyncEvacResource) -> None:
        self._evac = evac

        self.create = async_to_streamed_response_wrapper(
            evac.create,
        )
