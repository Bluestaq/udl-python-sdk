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
from ...types.supporting_data import dataowner_type_list_params
from ...types.supporting_data.dataowner_type_list_response import DataownerTypeListResponse

__all__ = ["DataownerTypesResource", "AsyncDataownerTypesResource"]


class DataownerTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataownerTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DataownerTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataownerTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DataownerTypesResourceWithStreamingResponse(self)

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
    ) -> SyncOffsetPage[DataownerTypeListResponse]:
        """
        Retrieves all distinct data owner types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/dataowner/getDataOwnerTypes",
            page=SyncOffsetPage[DataownerTypeListResponse],
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
                    dataowner_type_list_params.DataownerTypeListParams,
                ),
            ),
            model=str,
        )


class AsyncDataownerTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataownerTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDataownerTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataownerTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDataownerTypesResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[DataownerTypeListResponse, AsyncOffsetPage[DataownerTypeListResponse]]:
        """
        Retrieves all distinct data owner types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/dataowner/getDataOwnerTypes",
            page=AsyncOffsetPage[DataownerTypeListResponse],
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
                    dataowner_type_list_params.DataownerTypeListParams,
                ),
            ),
            model=str,
        )


class DataownerTypesResourceWithRawResponse:
    def __init__(self, dataowner_types: DataownerTypesResource) -> None:
        self._dataowner_types = dataowner_types

        self.list = to_raw_response_wrapper(
            dataowner_types.list,
        )


class AsyncDataownerTypesResourceWithRawResponse:
    def __init__(self, dataowner_types: AsyncDataownerTypesResource) -> None:
        self._dataowner_types = dataowner_types

        self.list = async_to_raw_response_wrapper(
            dataowner_types.list,
        )


class DataownerTypesResourceWithStreamingResponse:
    def __init__(self, dataowner_types: DataownerTypesResource) -> None:
        self._dataowner_types = dataowner_types

        self.list = to_streamed_response_wrapper(
            dataowner_types.list,
        )


class AsyncDataownerTypesResourceWithStreamingResponse:
    def __init__(self, dataowner_types: AsyncDataownerTypesResource) -> None:
        self._dataowner_types = dataowner_types

        self.list = async_to_streamed_response_wrapper(
            dataowner_types.list,
        )
