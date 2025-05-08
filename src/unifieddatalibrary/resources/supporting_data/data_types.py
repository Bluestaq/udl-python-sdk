# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.supporting_data import data_type_list_params
from ...types.supporting_data.data_type_list_response import DataTypeListResponse

__all__ = ["DataTypesResource", "AsyncDataTypesResource"]


class DataTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DataTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DataTypesResourceWithStreamingResponse(self)

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
    ) -> SyncOffsetPage[DataTypeListResponse]:
        """
        Retrieves all distinct data owner types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/dataowner/getDataTypes",
            page=SyncOffsetPage[DataTypeListResponse],
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
                    data_type_list_params.DataTypeListParams,
                ),
            ),
            model=str,
        )


class AsyncDataTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDataTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDataTypesResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[DataTypeListResponse, AsyncOffsetPage[DataTypeListResponse]]:
        """
        Retrieves all distinct data owner types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/dataowner/getDataTypes",
            page=AsyncOffsetPage[DataTypeListResponse],
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
                    data_type_list_params.DataTypeListParams,
                ),
            ),
            model=str,
        )


class DataTypesResourceWithRawResponse:
    def __init__(self, data_types: DataTypesResource) -> None:
        self._data_types = data_types

        self.list = to_raw_response_wrapper(
            data_types.list,
        )


class AsyncDataTypesResourceWithRawResponse:
    def __init__(self, data_types: AsyncDataTypesResource) -> None:
        self._data_types = data_types

        self.list = async_to_raw_response_wrapper(
            data_types.list,
        )


class DataTypesResourceWithStreamingResponse:
    def __init__(self, data_types: DataTypesResource) -> None:
        self._data_types = data_types

        self.list = to_streamed_response_wrapper(
            data_types.list,
        )


class AsyncDataTypesResourceWithStreamingResponse:
    def __init__(self, data_types: AsyncDataTypesResource) -> None:
        self._data_types = data_types

        self.list = async_to_streamed_response_wrapper(
            data_types.list,
        )
