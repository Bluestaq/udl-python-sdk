# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..types import (
    ion_oobservation_list_params,
    ion_oobservation_count_params,
    ion_oobservation_tuple_params,
    ion_oobservation_create_bulk_params,
    ion_oobservation_unvalidated_publish_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.ion_oobservation_list_response import IonOobservationListResponse
from ..types.ion_oobservation_tuple_response import IonOobservationTupleResponse

__all__ = ["IonOobservationResource", "AsyncIonOobservationResource"]


class IonOobservationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IonOobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return IonOobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IonOobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return IonOobservationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        start_time_utc: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[IonOobservationListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time_utc: Sounding Start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ionoobservation",
            page=SyncOffsetPage[IonOobservationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time_utc": start_time_utc,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ion_oobservation_list_params.IonOobservationListParams,
                ),
            ),
            model=IonOobservationListResponse,
        )

    def count(
        self,
        *,
        start_time_utc: Union[str, datetime],
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
          start_time_utc: Sounding Start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/ionoobservation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time_utc": start_time_utc,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ion_oobservation_count_params.IonOobservationCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[ion_oobservation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        IonoObservation records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/ionoobservation/createBulk",
            body=maybe_transform(body, Iterable[ion_oobservation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/ionoobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        start_time_utc: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IonOobservationTupleResponse:
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

          start_time_utc: Sounding Start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/ionoobservation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "start_time_utc": start_time_utc,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ion_oobservation_tuple_params.IonOobservationTupleParams,
                ),
            ),
            cast_to=IonOobservationTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[ion_oobservation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take Ionospheric Observation entries as a POST body and
        ingest into the database with or without dupe detection. Default is no dupe
        checking. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-ionoobs",
            body=maybe_transform(body, Iterable[ion_oobservation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncIonOobservationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIonOobservationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIonOobservationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIonOobservationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncIonOobservationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        start_time_utc: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IonOobservationListResponse, AsyncOffsetPage[IonOobservationListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time_utc: Sounding Start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/ionoobservation",
            page=AsyncOffsetPage[IonOobservationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time_utc": start_time_utc,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ion_oobservation_list_params.IonOobservationListParams,
                ),
            ),
            model=IonOobservationListResponse,
        )

    async def count(
        self,
        *,
        start_time_utc: Union[str, datetime],
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
          start_time_utc: Sounding Start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/ionoobservation/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time_utc": start_time_utc,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ion_oobservation_count_params.IonOobservationCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[ion_oobservation_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        IonoObservation records as a POST body and ingest into the database. This
        operation is not intended to be used for automated feeds into UDL. Data
        providers should contact the UDL team for specific role assignments and for
        instructions on setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/ionoobservation/createBulk",
            body=await async_maybe_transform(body, Iterable[ion_oobservation_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/ionoobservation/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        start_time_utc: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IonOobservationTupleResponse:
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

          start_time_utc: Sounding Start time in ISO8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/ionoobservation/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "start_time_utc": start_time_utc,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ion_oobservation_tuple_params.IonOobservationTupleParams,
                ),
            ),
            cast_to=IonOobservationTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[ion_oobservation_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take Ionospheric Observation entries as a POST body and
        ingest into the database with or without dupe detection. Default is no dupe
        checking. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-ionoobs",
            body=await async_maybe_transform(body, Iterable[ion_oobservation_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class IonOobservationResourceWithRawResponse:
    def __init__(self, ion_oobservation: IonOobservationResource) -> None:
        self._ion_oobservation = ion_oobservation

        self.list = to_raw_response_wrapper(
            ion_oobservation.list,
        )
        self.count = to_raw_response_wrapper(
            ion_oobservation.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            ion_oobservation.create_bulk,
        )
        self.queryhelp = to_raw_response_wrapper(
            ion_oobservation.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            ion_oobservation.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            ion_oobservation.unvalidated_publish,
        )


class AsyncIonOobservationResourceWithRawResponse:
    def __init__(self, ion_oobservation: AsyncIonOobservationResource) -> None:
        self._ion_oobservation = ion_oobservation

        self.list = async_to_raw_response_wrapper(
            ion_oobservation.list,
        )
        self.count = async_to_raw_response_wrapper(
            ion_oobservation.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            ion_oobservation.create_bulk,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            ion_oobservation.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            ion_oobservation.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            ion_oobservation.unvalidated_publish,
        )


class IonOobservationResourceWithStreamingResponse:
    def __init__(self, ion_oobservation: IonOobservationResource) -> None:
        self._ion_oobservation = ion_oobservation

        self.list = to_streamed_response_wrapper(
            ion_oobservation.list,
        )
        self.count = to_streamed_response_wrapper(
            ion_oobservation.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            ion_oobservation.create_bulk,
        )
        self.queryhelp = to_streamed_response_wrapper(
            ion_oobservation.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            ion_oobservation.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            ion_oobservation.unvalidated_publish,
        )


class AsyncIonOobservationResourceWithStreamingResponse:
    def __init__(self, ion_oobservation: AsyncIonOobservationResource) -> None:
        self._ion_oobservation = ion_oobservation

        self.list = async_to_streamed_response_wrapper(
            ion_oobservation.list,
        )
        self.count = async_to_streamed_response_wrapper(
            ion_oobservation.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            ion_oobservation.create_bulk,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            ion_oobservation.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            ion_oobservation.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            ion_oobservation.unvalidated_publish,
        )
