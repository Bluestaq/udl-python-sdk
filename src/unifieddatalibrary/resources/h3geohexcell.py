# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import h3geohexcell_list_params, h3geohexcell_count_params, h3geohexcell_tuple_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.h3geohexcell_list_response import H3geohexcellListResponse
from ..types.h3geohexcell_tuple_response import H3geohexcellTupleResponse

__all__ = ["H3geohexcellResource", "AsyncH3geohexcellResource"]


class H3geohexcellResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> H3geohexcellResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return H3geohexcellResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> H3geohexcellResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return H3geohexcellResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id_h3_geo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> H3geohexcellListResponse:
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
        return self._get(
            "/udl/h3geohexcell",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id_h3_geo": id_h3_geo}, h3geohexcell_list_params.H3geohexcellListParams),
            ),
            cast_to=H3geohexcellListResponse,
        )

    def count(
        self,
        *,
        id_h3_geo: str,
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
                query=maybe_transform({"id_h3_geo": id_h3_geo}, h3geohexcell_count_params.H3geohexcellCountParams),
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/h3geohexcell/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        id_h3_geo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> H3geohexcellTupleResponse:
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
                    },
                    h3geohexcell_tuple_params.H3geohexcellTupleParams,
                ),
            ),
            cast_to=H3geohexcellTupleResponse,
        )


class AsyncH3geohexcellResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncH3geohexcellResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncH3geohexcellResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncH3geohexcellResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncH3geohexcellResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        id_h3_geo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> H3geohexcellListResponse:
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
        return await self._get(
            "/udl/h3geohexcell",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id_h3_geo": id_h3_geo}, h3geohexcell_list_params.H3geohexcellListParams
                ),
            ),
            cast_to=H3geohexcellListResponse,
        )

    async def count(
        self,
        *,
        id_h3_geo: str,
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
                    {"id_h3_geo": id_h3_geo}, h3geohexcell_count_params.H3geohexcellCountParams
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/h3geohexcell/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        id_h3_geo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> H3geohexcellTupleResponse:
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
                    },
                    h3geohexcell_tuple_params.H3geohexcellTupleParams,
                ),
            ),
            cast_to=H3geohexcellTupleResponse,
        )


class H3geohexcellResourceWithRawResponse:
    def __init__(self, h3geohexcell: H3geohexcellResource) -> None:
        self._h3geohexcell = h3geohexcell

        self.list = to_raw_response_wrapper(
            h3geohexcell.list,
        )
        self.count = to_raw_response_wrapper(
            h3geohexcell.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            h3geohexcell.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            h3geohexcell.tuple,
        )


class AsyncH3geohexcellResourceWithRawResponse:
    def __init__(self, h3geohexcell: AsyncH3geohexcellResource) -> None:
        self._h3geohexcell = h3geohexcell

        self.list = async_to_raw_response_wrapper(
            h3geohexcell.list,
        )
        self.count = async_to_raw_response_wrapper(
            h3geohexcell.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            h3geohexcell.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            h3geohexcell.tuple,
        )


class H3geohexcellResourceWithStreamingResponse:
    def __init__(self, h3geohexcell: H3geohexcellResource) -> None:
        self._h3geohexcell = h3geohexcell

        self.list = to_streamed_response_wrapper(
            h3geohexcell.list,
        )
        self.count = to_streamed_response_wrapper(
            h3geohexcell.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            h3geohexcell.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            h3geohexcell.tuple,
        )


class AsyncH3geohexcellResourceWithStreamingResponse:
    def __init__(self, h3geohexcell: AsyncH3geohexcellResource) -> None:
        self._h3geohexcell = h3geohexcell

        self.list = async_to_streamed_response_wrapper(
            h3geohexcell.list,
        )
        self.count = async_to_streamed_response_wrapper(
            h3geohexcell.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            h3geohexcell.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            h3geohexcell.tuple,
        )
