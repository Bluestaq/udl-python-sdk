# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

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
from ...types.evac import tuple_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.evac_full import EvacFull

__all__ = ["TupleResource", "AsyncTupleResource"]


class TupleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TupleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TupleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TupleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return TupleResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        columns: str,
        req_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EvacFull]:
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

          req_time: The request time, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/evac/tuple",
            page=SyncOffsetPage[EvacFull],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "req_time": req_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    tuple_list_params.TupleListParams,
                ),
            ),
            model=EvacFull,
        )


class AsyncTupleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTupleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTupleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTupleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncTupleResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        columns: str,
        req_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EvacFull, AsyncOffsetPage[EvacFull]]:
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

          req_time: The request time, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/evac/tuple",
            page=AsyncOffsetPage[EvacFull],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "req_time": req_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    tuple_list_params.TupleListParams,
                ),
            ),
            model=EvacFull,
        )


class TupleResourceWithRawResponse:
    def __init__(self, tuple: TupleResource) -> None:
        self._tuple = tuple

        self.list = to_raw_response_wrapper(
            tuple.list,
        )


class AsyncTupleResourceWithRawResponse:
    def __init__(self, tuple: AsyncTupleResource) -> None:
        self._tuple = tuple

        self.list = async_to_raw_response_wrapper(
            tuple.list,
        )


class TupleResourceWithStreamingResponse:
    def __init__(self, tuple: TupleResource) -> None:
        self._tuple = tuple

        self.list = to_streamed_response_wrapper(
            tuple.list,
        )


class AsyncTupleResourceWithStreamingResponse:
    def __init__(self, tuple: AsyncTupleResource) -> None:
        self._tuple = tuple

        self.list = async_to_streamed_response_wrapper(
            tuple.list,
        )
