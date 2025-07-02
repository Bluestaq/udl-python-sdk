# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sensor_type_get_params, sensor_type_list_params
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
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.sensor_type_get_response import SensorTypeGetResponse
from ..types.sensor_type_list_response import SensorTypeListResponse
from ..types.sensor_type_queryhelp_response import SensorTypeQueryhelpResponse

__all__ = ["SensorTypeResource", "AsyncSensorTypeResource"]


class SensorTypeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SensorTypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SensorTypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SensorTypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SensorTypeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SensorTypeListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sensortype",
            page=SyncOffsetPage[SensorTypeListResponse],
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
                    sensor_type_list_params.SensorTypeListParams,
                ),
            ),
            model=SensorTypeListResponse,
        )

    def get(
        self,
        id: int,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SensorTypeGetResponse:
        """
        Service operation to get a single Sensortype record by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/udl/sensortype/{id}",
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
                    sensor_type_get_params.SensorTypeGetParams,
                ),
            ),
            cast_to=SensorTypeGetResponse,
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
    ) -> SensorTypeQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/sensortype/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorTypeQueryhelpResponse,
        )


class AsyncSensorTypeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSensorTypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSensorTypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSensorTypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSensorTypeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SensorTypeListResponse, AsyncOffsetPage[SensorTypeListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sensortype",
            page=AsyncOffsetPage[SensorTypeListResponse],
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
                    sensor_type_list_params.SensorTypeListParams,
                ),
            ),
            model=SensorTypeListResponse,
        )

    async def get(
        self,
        id: int,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SensorTypeGetResponse:
        """
        Service operation to get a single Sensortype record by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/udl/sensortype/{id}",
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
                    sensor_type_get_params.SensorTypeGetParams,
                ),
            ),
            cast_to=SensorTypeGetResponse,
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
    ) -> SensorTypeQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/sensortype/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorTypeQueryhelpResponse,
        )


class SensorTypeResourceWithRawResponse:
    def __init__(self, sensor_type: SensorTypeResource) -> None:
        self._sensor_type = sensor_type

        self.list = to_raw_response_wrapper(
            sensor_type.list,
        )
        self.get = to_raw_response_wrapper(
            sensor_type.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            sensor_type.queryhelp,
        )


class AsyncSensorTypeResourceWithRawResponse:
    def __init__(self, sensor_type: AsyncSensorTypeResource) -> None:
        self._sensor_type = sensor_type

        self.list = async_to_raw_response_wrapper(
            sensor_type.list,
        )
        self.get = async_to_raw_response_wrapper(
            sensor_type.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            sensor_type.queryhelp,
        )


class SensorTypeResourceWithStreamingResponse:
    def __init__(self, sensor_type: SensorTypeResource) -> None:
        self._sensor_type = sensor_type

        self.list = to_streamed_response_wrapper(
            sensor_type.list,
        )
        self.get = to_streamed_response_wrapper(
            sensor_type.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            sensor_type.queryhelp,
        )


class AsyncSensorTypeResourceWithStreamingResponse:
    def __init__(self, sensor_type: AsyncSensorTypeResource) -> None:
        self._sensor_type = sensor_type

        self.list = async_to_streamed_response_wrapper(
            sensor_type.list,
        )
        self.get = async_to_streamed_response_wrapper(
            sensor_type.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            sensor_type.queryhelp,
        )
