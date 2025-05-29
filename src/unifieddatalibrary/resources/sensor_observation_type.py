# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sensor_observation_type_get_params, sensor_observation_type_list_params
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
from ..types.sensor_observation_type_get_response import SensorObservationTypeGetResponse
from ..types.sensor_observation_type_list_response import SensorObservationTypeListResponse
from ..types.sensor_observation_type_queryhelp_response import SensorObservationTypeQueryhelpResponse

__all__ = ["SensorObservationTypeResource", "AsyncSensorObservationTypeResource"]


class SensorObservationTypeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SensorObservationTypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SensorObservationTypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SensorObservationTypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SensorObservationTypeResourceWithStreamingResponse(self)

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
    ) -> SyncOffsetPage[SensorObservationTypeListResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sensorobservationtype",
            page=SyncOffsetPage[SensorObservationTypeListResponse],
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
                    sensor_observation_type_list_params.SensorObservationTypeListParams,
                ),
            ),
            model=SensorObservationTypeListResponse,
        )

    def get(
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
    ) -> SensorObservationTypeGetResponse:
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sensor_observation_type_get_params.SensorObservationTypeGetParams,
                ),
            ),
            cast_to=SensorObservationTypeGetResponse,
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
    ) -> SensorObservationTypeQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/sensorobservationtype/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorObservationTypeQueryhelpResponse,
        )


class AsyncSensorObservationTypeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSensorObservationTypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSensorObservationTypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSensorObservationTypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSensorObservationTypeResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[SensorObservationTypeListResponse, AsyncOffsetPage[SensorObservationTypeListResponse]]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/sensorobservationtype",
            page=AsyncOffsetPage[SensorObservationTypeListResponse],
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
                    sensor_observation_type_list_params.SensorObservationTypeListParams,
                ),
            ),
            model=SensorObservationTypeListResponse,
        )

    async def get(
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
    ) -> SensorObservationTypeGetResponse:
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sensor_observation_type_get_params.SensorObservationTypeGetParams,
                ),
            ),
            cast_to=SensorObservationTypeGetResponse,
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
    ) -> SensorObservationTypeQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/sensorobservationtype/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorObservationTypeQueryhelpResponse,
        )


class SensorObservationTypeResourceWithRawResponse:
    def __init__(self, sensor_observation_type: SensorObservationTypeResource) -> None:
        self._sensor_observation_type = sensor_observation_type

        self.list = to_raw_response_wrapper(
            sensor_observation_type.list,
        )
        self.get = to_raw_response_wrapper(
            sensor_observation_type.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            sensor_observation_type.queryhelp,
        )


class AsyncSensorObservationTypeResourceWithRawResponse:
    def __init__(self, sensor_observation_type: AsyncSensorObservationTypeResource) -> None:
        self._sensor_observation_type = sensor_observation_type

        self.list = async_to_raw_response_wrapper(
            sensor_observation_type.list,
        )
        self.get = async_to_raw_response_wrapper(
            sensor_observation_type.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            sensor_observation_type.queryhelp,
        )


class SensorObservationTypeResourceWithStreamingResponse:
    def __init__(self, sensor_observation_type: SensorObservationTypeResource) -> None:
        self._sensor_observation_type = sensor_observation_type

        self.list = to_streamed_response_wrapper(
            sensor_observation_type.list,
        )
        self.get = to_streamed_response_wrapper(
            sensor_observation_type.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            sensor_observation_type.queryhelp,
        )


class AsyncSensorObservationTypeResourceWithStreamingResponse:
    def __init__(self, sensor_observation_type: AsyncSensorObservationTypeResource) -> None:
        self._sensor_observation_type = sensor_observation_type

        self.list = async_to_streamed_response_wrapper(
            sensor_observation_type.list,
        )
        self.get = async_to_streamed_response_wrapper(
            sensor_observation_type.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            sensor_observation_type.queryhelp,
        )
