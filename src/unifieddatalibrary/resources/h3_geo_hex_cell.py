# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import h3_geo_hex_cell_list_params, h3_geo_hex_cell_count_params, h3_geo_hex_cell_tuple_params
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
from ..types.h3_geo_hex_cell_list_response import H3GeoHexCellListResponse
from ..types.h3_geo_hex_cell_tuple_response import H3GeoHexCellTupleResponse
from ..types.h3_geo_hex_cell_queryhelp_response import H3GeoHexCellQueryhelpResponse

__all__ = ["H3GeoHexCellResource", "AsyncH3GeoHexCellResource"]


class H3GeoHexCellResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> H3GeoHexCellResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return H3GeoHexCellResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> H3GeoHexCellResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return H3GeoHexCellResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id_h3_geo: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[H3GeoHexCellListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_h3_geo: Unique identifier of the parent H3 Geo record containing this hex cell. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/h3geohexcell",
            page=SyncOffsetPage[H3GeoHexCellListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id_h3_geo": id_h3_geo,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    h3_geo_hex_cell_list_params.H3GeoHexCellListParams,
                ),
            ),
            model=H3GeoHexCellListResponse,
        )

    def count(
        self,
        *,
        id_h3_geo: str,
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
          id_h3_geo: Unique identifier of the parent H3 Geo record containing this hex cell. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/h3geohexcell/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id_h3_geo": id_h3_geo,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    h3_geo_hex_cell_count_params.H3GeoHexCellCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> H3GeoHexCellQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/h3geohexcell/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=H3GeoHexCellQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        id_h3_geo: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> H3GeoHexCellTupleResponse:
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
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          id_h3_geo: Unique identifier of the parent H3 Geo record containing this hex cell. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/h3geohexcell/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "id_h3_geo": id_h3_geo,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    h3_geo_hex_cell_tuple_params.H3GeoHexCellTupleParams,
                ),
            ),
            cast_to=H3GeoHexCellTupleResponse,
        )


class AsyncH3GeoHexCellResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncH3GeoHexCellResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncH3GeoHexCellResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncH3GeoHexCellResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncH3GeoHexCellResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id_h3_geo: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[H3GeoHexCellListResponse, AsyncOffsetPage[H3GeoHexCellListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          id_h3_geo: Unique identifier of the parent H3 Geo record containing this hex cell. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/h3geohexcell",
            page=AsyncOffsetPage[H3GeoHexCellListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id_h3_geo": id_h3_geo,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    h3_geo_hex_cell_list_params.H3GeoHexCellListParams,
                ),
            ),
            model=H3GeoHexCellListResponse,
        )

    async def count(
        self,
        *,
        id_h3_geo: str,
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
          id_h3_geo: Unique identifier of the parent H3 Geo record containing this hex cell. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/h3geohexcell/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id_h3_geo": id_h3_geo,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    h3_geo_hex_cell_count_params.H3GeoHexCellCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> H3GeoHexCellQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/h3geohexcell/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=H3GeoHexCellQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        id_h3_geo: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> H3GeoHexCellTupleResponse:
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
          columns: Comma-separated list of valid field names for this data type to be returned in
              the response. Only the fields specified will be returned as well as the
              classification marking of the data, if applicable. See the ‘queryhelp’ operation
              for a complete list of possible fields.

          id_h3_geo: Unique identifier of the parent H3 Geo record containing this hex cell. (uuid)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/h3geohexcell/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "id_h3_geo": id_h3_geo,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    h3_geo_hex_cell_tuple_params.H3GeoHexCellTupleParams,
                ),
            ),
            cast_to=H3GeoHexCellTupleResponse,
        )


class H3GeoHexCellResourceWithRawResponse:
    def __init__(self, h3_geo_hex_cell: H3GeoHexCellResource) -> None:
        self._h3_geo_hex_cell = h3_geo_hex_cell

        self.list = to_raw_response_wrapper(
            h3_geo_hex_cell.list,
        )
        self.count = to_raw_response_wrapper(
            h3_geo_hex_cell.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            h3_geo_hex_cell.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            h3_geo_hex_cell.tuple,
        )


class AsyncH3GeoHexCellResourceWithRawResponse:
    def __init__(self, h3_geo_hex_cell: AsyncH3GeoHexCellResource) -> None:
        self._h3_geo_hex_cell = h3_geo_hex_cell

        self.list = async_to_raw_response_wrapper(
            h3_geo_hex_cell.list,
        )
        self.count = async_to_raw_response_wrapper(
            h3_geo_hex_cell.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            h3_geo_hex_cell.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            h3_geo_hex_cell.tuple,
        )


class H3GeoHexCellResourceWithStreamingResponse:
    def __init__(self, h3_geo_hex_cell: H3GeoHexCellResource) -> None:
        self._h3_geo_hex_cell = h3_geo_hex_cell

        self.list = to_streamed_response_wrapper(
            h3_geo_hex_cell.list,
        )
        self.count = to_streamed_response_wrapper(
            h3_geo_hex_cell.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            h3_geo_hex_cell.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            h3_geo_hex_cell.tuple,
        )


class AsyncH3GeoHexCellResourceWithStreamingResponse:
    def __init__(self, h3_geo_hex_cell: AsyncH3GeoHexCellResource) -> None:
        self._h3_geo_hex_cell = h3_geo_hex_cell

        self.list = async_to_streamed_response_wrapper(
            h3_geo_hex_cell.list,
        )
        self.count = async_to_streamed_response_wrapper(
            h3_geo_hex_cell.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            h3_geo_hex_cell.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            h3_geo_hex_cell.tuple,
        )
