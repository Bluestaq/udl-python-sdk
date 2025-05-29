# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import attitude_data_tuple_params
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
from ..types.attitude_data_tuple_response import AttitudeDataTupleResponse
from ..types.attitude_data_query_help_response import AttitudeDataQueryHelpResponse

__all__ = ["AttitudeDataResource", "AsyncAttitudeDataResource"]


class AttitudeDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttitudeDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AttitudeDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttitudeDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AttitudeDataResourceWithStreamingResponse(self)

    def query_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudeDataQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/attitudedata/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttitudeDataQueryHelpResponse,
        )

    def tuple(
        self,
        *,
        as_id: str,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudeDataTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          as_id: Unique identifier of the parent AttitudeSet associated with this record. (uuid)

          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/attitudedata/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "as_id": as_id,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_data_tuple_params.AttitudeDataTupleParams,
                ),
            ),
            cast_to=AttitudeDataTupleResponse,
        )


class AsyncAttitudeDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttitudeDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAttitudeDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttitudeDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAttitudeDataResourceWithStreamingResponse(self)

    async def query_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudeDataQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/attitudedata/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttitudeDataQueryHelpResponse,
        )

    async def tuple(
        self,
        *,
        as_id: str,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudeDataTupleResponse:
        """
        Service operation to dynamically query data and only return specified
        columns/fields. Requested columns are specified by the 'columns' query parameter
        and should be a comma separated list of valid fields for the specified data
        type. classificationMarking is always returned. See the queryhelp operation
        (/udl/<datatype>/queryhelp) for more details on valid/required query parameter
        information. An example URI: /udl/elset/tuple?columns=satNo,period&epoch=>now-5
        hours would return the satNo and period of elsets with an epoch greater than 5
        hours ago.

        Args:
          as_id: Unique identifier of the parent AttitudeSet associated with this record. (uuid)

          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/attitudedata/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "as_id": as_id,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_data_tuple_params.AttitudeDataTupleParams,
                ),
            ),
            cast_to=AttitudeDataTupleResponse,
        )


class AttitudeDataResourceWithRawResponse:
    def __init__(self, attitude_data: AttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.query_help = to_raw_response_wrapper(
            attitude_data.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            attitude_data.tuple,
        )


class AsyncAttitudeDataResourceWithRawResponse:
    def __init__(self, attitude_data: AsyncAttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.query_help = async_to_raw_response_wrapper(
            attitude_data.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            attitude_data.tuple,
        )


class AttitudeDataResourceWithStreamingResponse:
    def __init__(self, attitude_data: AttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.query_help = to_streamed_response_wrapper(
            attitude_data.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            attitude_data.tuple,
        )


class AsyncAttitudeDataResourceWithStreamingResponse:
    def __init__(self, attitude_data: AsyncAttitudeDataResource) -> None:
        self._attitude_data = attitude_data

        self.query_help = async_to_streamed_response_wrapper(
            attitude_data.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            attitude_data.tuple,
        )
