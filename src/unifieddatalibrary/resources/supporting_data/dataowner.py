# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.supporting_data import (
    dataowner_count_params,
    dataowner_retrieve_params,
    dataowner_retrieve_data_owner_types_params,
    dataowner_retrieve_provider_metadata_params,
)
from ...types.supporting_data.dataowner_retrieve_response import DataownerRetrieveResponse
from ...types.supporting_data.dataowner_query_help_response import DataownerQueryHelpResponse
from ...types.supporting_data.dataowner_retrieve_data_owner_types_response import (
    DataownerRetrieveDataOwnerTypesResponse,
)
from ...types.supporting_data.dataowner_retrieve_provider_metadata_response import (
    DataownerRetrieveProviderMetadataResponse,
)

__all__ = ["DataownerResource", "AsyncDataownerResource"]


class DataownerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataownerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DataownerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataownerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DataownerResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> DataownerRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/dataowner",
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
                    dataowner_retrieve_params.DataownerRetrieveParams,
                ),
            ),
            cast_to=DataownerRetrieveResponse,
        )

    def count(
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
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/dataowner/count",
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
                    dataowner_count_params.DataownerCountParams,
                ),
            ),
            cast_to=str,
        )

    def query_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataownerQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/dataowner/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataownerQueryHelpResponse,
        )

    def retrieve_data_owner_types(
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
    ) -> DataownerRetrieveDataOwnerTypesResponse:
        """
        Retrieves all distinct data owner types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/dataowner/getDataOwnerTypes",
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
                    dataowner_retrieve_data_owner_types_params.DataownerRetrieveDataOwnerTypesParams,
                ),
            ),
            cast_to=DataownerRetrieveDataOwnerTypesResponse,
        )

    def retrieve_provider_metadata(
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
    ) -> DataownerRetrieveProviderMetadataResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/dataowner/providerMetadata",
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
                    dataowner_retrieve_provider_metadata_params.DataownerRetrieveProviderMetadataParams,
                ),
            ),
            cast_to=DataownerRetrieveProviderMetadataResponse,
        )


class AsyncDataownerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataownerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDataownerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataownerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDataownerResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> DataownerRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/dataowner",
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
                    dataowner_retrieve_params.DataownerRetrieveParams,
                ),
            ),
            cast_to=DataownerRetrieveResponse,
        )

    async def count(
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
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/dataowner/count",
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
                    dataowner_count_params.DataownerCountParams,
                ),
            ),
            cast_to=str,
        )

    async def query_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataownerQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/dataowner/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataownerQueryHelpResponse,
        )

    async def retrieve_data_owner_types(
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
    ) -> DataownerRetrieveDataOwnerTypesResponse:
        """
        Retrieves all distinct data owner types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/dataowner/getDataOwnerTypes",
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
                    dataowner_retrieve_data_owner_types_params.DataownerRetrieveDataOwnerTypesParams,
                ),
            ),
            cast_to=DataownerRetrieveDataOwnerTypesResponse,
        )

    async def retrieve_provider_metadata(
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
    ) -> DataownerRetrieveProviderMetadataResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/dataowner/providerMetadata",
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
                    dataowner_retrieve_provider_metadata_params.DataownerRetrieveProviderMetadataParams,
                ),
            ),
            cast_to=DataownerRetrieveProviderMetadataResponse,
        )


class DataownerResourceWithRawResponse:
    def __init__(self, dataowner: DataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = to_raw_response_wrapper(
            dataowner.retrieve,
        )
        self.count = to_raw_response_wrapper(
            dataowner.count,
        )
        self.query_help = to_raw_response_wrapper(
            dataowner.query_help,
        )
        self.retrieve_data_owner_types = to_raw_response_wrapper(
            dataowner.retrieve_data_owner_types,
        )
        self.retrieve_provider_metadata = to_raw_response_wrapper(
            dataowner.retrieve_provider_metadata,
        )


class AsyncDataownerResourceWithRawResponse:
    def __init__(self, dataowner: AsyncDataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = async_to_raw_response_wrapper(
            dataowner.retrieve,
        )
        self.count = async_to_raw_response_wrapper(
            dataowner.count,
        )
        self.query_help = async_to_raw_response_wrapper(
            dataowner.query_help,
        )
        self.retrieve_data_owner_types = async_to_raw_response_wrapper(
            dataowner.retrieve_data_owner_types,
        )
        self.retrieve_provider_metadata = async_to_raw_response_wrapper(
            dataowner.retrieve_provider_metadata,
        )


class DataownerResourceWithStreamingResponse:
    def __init__(self, dataowner: DataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = to_streamed_response_wrapper(
            dataowner.retrieve,
        )
        self.count = to_streamed_response_wrapper(
            dataowner.count,
        )
        self.query_help = to_streamed_response_wrapper(
            dataowner.query_help,
        )
        self.retrieve_data_owner_types = to_streamed_response_wrapper(
            dataowner.retrieve_data_owner_types,
        )
        self.retrieve_provider_metadata = to_streamed_response_wrapper(
            dataowner.retrieve_provider_metadata,
        )


class AsyncDataownerResourceWithStreamingResponse:
    def __init__(self, dataowner: AsyncDataownerResource) -> None:
        self._dataowner = dataowner

        self.retrieve = async_to_streamed_response_wrapper(
            dataowner.retrieve,
        )
        self.count = async_to_streamed_response_wrapper(
            dataowner.count,
        )
        self.query_help = async_to_streamed_response_wrapper(
            dataowner.query_help,
        )
        self.retrieve_data_owner_types = async_to_streamed_response_wrapper(
            dataowner.retrieve_data_owner_types,
        )
        self.retrieve_provider_metadata = async_to_streamed_response_wrapper(
            dataowner.retrieve_provider_metadata,
        )
