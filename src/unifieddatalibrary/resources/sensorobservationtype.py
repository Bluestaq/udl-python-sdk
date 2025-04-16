# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sensorobservationtype_get_response import SensorobservationtypeGetResponse
from ..types.sensorobservationtype_list_response import SensorobservationtypeListResponse

__all__ = ["SensorobservationtypeResource", "AsyncSensorobservationtypeResource"]


class SensorobservationtypeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SensorobservationtypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SensorobservationtypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SensorobservationtypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return SensorobservationtypeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SensorobservationtypeListResponse:
        return self._get(
            "/udl/sensorobservationtype",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorobservationtypeListResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SensorobservationtypeGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/sensorobservationtype/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorobservationtypeGetResponse,
        )

    def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/sensorobservationtype/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSensorobservationtypeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSensorobservationtypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSensorobservationtypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSensorobservationtypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSensorobservationtypeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SensorobservationtypeListResponse:
        return await self._get(
            "/udl/sensorobservationtype",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorobservationtypeListResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SensorobservationtypeGetResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/sensorobservationtype/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorobservationtypeGetResponse,
        )

    async def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/sensorobservationtype/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SensorobservationtypeResourceWithRawResponse:
    def __init__(self, sensorobservationtype: SensorobservationtypeResource) -> None:
        self._sensorobservationtype = sensorobservationtype

        self.list = to_raw_response_wrapper(
            sensorobservationtype.list,
        )
        self.get = to_raw_response_wrapper(
            sensorobservationtype.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            sensorobservationtype.queryhelp,
        )


class AsyncSensorobservationtypeResourceWithRawResponse:
    def __init__(self, sensorobservationtype: AsyncSensorobservationtypeResource) -> None:
        self._sensorobservationtype = sensorobservationtype

        self.list = async_to_raw_response_wrapper(
            sensorobservationtype.list,
        )
        self.get = async_to_raw_response_wrapper(
            sensorobservationtype.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            sensorobservationtype.queryhelp,
        )


class SensorobservationtypeResourceWithStreamingResponse:
    def __init__(self, sensorobservationtype: SensorobservationtypeResource) -> None:
        self._sensorobservationtype = sensorobservationtype

        self.list = to_streamed_response_wrapper(
            sensorobservationtype.list,
        )
        self.get = to_streamed_response_wrapper(
            sensorobservationtype.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            sensorobservationtype.queryhelp,
        )


class AsyncSensorobservationtypeResourceWithStreamingResponse:
    def __init__(self, sensorobservationtype: AsyncSensorobservationtypeResource) -> None:
        self._sensorobservationtype = sensorobservationtype

        self.list = async_to_streamed_response_wrapper(
            sensorobservationtype.list,
        )
        self.get = async_to_streamed_response_wrapper(
            sensorobservationtype.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            sensorobservationtype.queryhelp,
        )
