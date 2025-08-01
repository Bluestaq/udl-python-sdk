# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, cast
from datetime import datetime

import httpx

from ..types import (
    analytic_imagery_list_params,
    analytic_imagery_count_params,
    analytic_imagery_tuple_params,
    analytic_imagery_history_params,
    analytic_imagery_file_get_params,
    analytic_imagery_retrieve_params,
    analytic_imagery_history_aodr_params,
    analytic_imagery_history_count_params,
    analytic_imagery_unvalidated_publish_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.analytic_imagery_abridged import AnalyticImageryAbridged
from ..types.shared.analytic_imagery_full import AnalyticImageryFull
from ..types.analytic_imagery_tuple_response import AnalyticImageryTupleResponse
from ..types.analytic_imagery_history_response import AnalyticImageryHistoryResponse
from ..types.analytic_imagery_queryhelp_response import AnalyticImageryQueryhelpResponse

__all__ = ["AnalyticImageryResource", "AsyncAnalyticImageryResource"]


class AnalyticImageryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AnalyticImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AnalyticImageryResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> AnalyticImageryFull:
        """
        Service operation to get a single AnalyticImagery record by its unique ID passed
        as a path parameter. AnalyticImagery represents metadata about an image, as well
        as the actual binary image data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/analyticimagery/{id}",
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
                    analytic_imagery_retrieve_params.AnalyticImageryRetrieveParams,
                ),
            ),
            cast_to=AnalyticImageryFull,
        )

    def list(
        self,
        *,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[AnalyticImageryAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/analyticimagery",
            page=SyncOffsetPage[AnalyticImageryAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_list_params.AnalyticImageryListParams,
                ),
            ),
            model=AnalyticImageryAbridged,
        )

    def count(
        self,
        *,
        msg_time: Union[str, datetime],
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
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/analyticimagery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_count_params.AnalyticImageryCountParams,
                ),
            ),
            cast_to=str,
        )

    def file_get(
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
    ) -> BinaryAPIResponse:
        """
        Service operation to get a single AnalyticImagery binary image by its unique ID
        passed as a path parameter. The image is returned as an attachment
        Content-Disposition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/udl/analyticimagery/getFile/{id}",
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
                    analytic_imagery_file_get_params.AnalyticImageryFileGetParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def history(
        self,
        *,
        msg_time: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticImageryHistoryResponse:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/analyticimagery/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_history_params.AnalyticImageryHistoryParams,
                ),
            ),
            cast_to=AnalyticImageryHistoryResponse,
        )

    def history_aodr(
        self,
        *,
        msg_time: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        notification: str | NotGiven = NOT_GIVEN,
        output_delimiter: str | NotGiven = NOT_GIVEN,
        output_format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation, then write that data to the
        Secure Content Store. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/analyticimagery/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    analytic_imagery_history_aodr_params.AnalyticImageryHistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
        )

    def history_count(
        self,
        *,
        msg_time: Union[str, datetime],
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
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/analyticimagery/history/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_history_count_params.AnalyticImageryHistoryCountParams,
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
    ) -> AnalyticImageryQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/analyticimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticImageryQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticImageryTupleResponse:
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

          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/analyticimagery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_tuple_params.AnalyticImageryTupleParams,
                ),
            ),
            cast_to=AnalyticImageryTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Upload a new image with its metadata.

        The request body requires a zip file containing exactly two files:\\
        1\\)) A file with the `.json` file extension whose content conforms to the `AnalyticImagery_Ingest`
        schema.\\
        2\\)) A binary image file of the allowed types for this service.

        The JSON and image files will be associated with each other via the `id` field.
        Query the metadata via `GET /udl/analyticimagery` and use
        `GET /udl/analyticimagery/getFile/{id}` to retrieve the binary image file.

        This operation only accepts application/zip media. The application/json request
        body is documented to provide a convenient reference to the ingest schema.

        This operation is intended to be used for automated feeds into UDL. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          file: Zip file containing files described in the specification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/filedrop/udl-analyticimagery"
            if self._client._base_url_overridden
            else "https://imagery.unifieddatalibrary.com/filedrop/udl-analyticimagery",
            body=maybe_transform(
                body, analytic_imagery_unvalidated_publish_params.AnalyticImageryUnvalidatedPublishParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAnalyticImageryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAnalyticImageryResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> AnalyticImageryFull:
        """
        Service operation to get a single AnalyticImagery record by its unique ID passed
        as a path parameter. AnalyticImagery represents metadata about an image, as well
        as the actual binary image data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/analyticimagery/{id}",
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
                    analytic_imagery_retrieve_params.AnalyticImageryRetrieveParams,
                ),
            ),
            cast_to=AnalyticImageryFull,
        )

    def list(
        self,
        *,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AnalyticImageryAbridged, AsyncOffsetPage[AnalyticImageryAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/analyticimagery",
            page=AsyncOffsetPage[AnalyticImageryAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_list_params.AnalyticImageryListParams,
                ),
            ),
            model=AnalyticImageryAbridged,
        )

    async def count(
        self,
        *,
        msg_time: Union[str, datetime],
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
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/analyticimagery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_count_params.AnalyticImageryCountParams,
                ),
            ),
            cast_to=str,
        )

    async def file_get(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Service operation to get a single AnalyticImagery binary image by its unique ID
        passed as a path parameter. The image is returned as an attachment
        Content-Disposition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/udl/analyticimagery/getFile/{id}",
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
                    analytic_imagery_file_get_params.AnalyticImageryFileGetParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def history(
        self,
        *,
        msg_time: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticImageryHistoryResponse:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/analyticimagery/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "msg_time": msg_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_history_params.AnalyticImageryHistoryParams,
                ),
            ),
            cast_to=AnalyticImageryHistoryResponse,
        )

    async def history_aodr(
        self,
        *,
        msg_time: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        notification: str | NotGiven = NOT_GIVEN,
        output_delimiter: str | NotGiven = NOT_GIVEN,
        output_format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation, then write that data to the
        Secure Content Store. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          notification: optional, notification method for the created file link. When omitted, EMAIL is
              assumed. Current valid values are: EMAIL, SMS.

          output_delimiter: optional, field delimiter when the created file is not JSON. Must be a single
              character chosen from this set: (',', ';', ':', '|'). When omitted, "," is used.
              It is strongly encouraged that your field delimiter be a character unlikely to
              occur within the data.

          output_format: optional, output format for the file. When omitted, JSON is assumed. Current
              valid values are: JSON and CSV.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/analyticimagery/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "msg_time": msg_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    analytic_imagery_history_aodr_params.AnalyticImageryHistoryAodrParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def history_count(
        self,
        *,
        msg_time: Union[str, datetime],
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
          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/analyticimagery/history/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_history_count_params.AnalyticImageryHistoryCountParams,
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
    ) -> AnalyticImageryQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/analyticimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticImageryQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        msg_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticImageryTupleResponse:
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

          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/analyticimagery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "msg_time": msg_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    analytic_imagery_tuple_params.AnalyticImageryTupleParams,
                ),
            ),
            cast_to=AnalyticImageryTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Upload a new image with its metadata.

        The request body requires a zip file containing exactly two files:\\
        1\\)) A file with the `.json` file extension whose content conforms to the `AnalyticImagery_Ingest`
        schema.\\
        2\\)) A binary image file of the allowed types for this service.

        The JSON and image files will be associated with each other via the `id` field.
        Query the metadata via `GET /udl/analyticimagery` and use
        `GET /udl/analyticimagery/getFile/{id}` to retrieve the binary image file.

        This operation only accepts application/zip media. The application/json request
        body is documented to provide a convenient reference to the ingest schema.

        This operation is intended to be used for automated feeds into UDL. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          file: Zip file containing files described in the specification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/filedrop/udl-analyticimagery"
            if self._client._base_url_overridden
            else "https://imagery.unifieddatalibrary.com/filedrop/udl-analyticimagery",
            body=await async_maybe_transform(
                body, analytic_imagery_unvalidated_publish_params.AnalyticImageryUnvalidatedPublishParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AnalyticImageryResourceWithRawResponse:
    def __init__(self, analytic_imagery: AnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.retrieve = to_raw_response_wrapper(
            analytic_imagery.retrieve,
        )
        self.list = to_raw_response_wrapper(
            analytic_imagery.list,
        )
        self.count = to_raw_response_wrapper(
            analytic_imagery.count,
        )
        self.file_get = to_custom_raw_response_wrapper(
            analytic_imagery.file_get,
            BinaryAPIResponse,
        )
        self.history = to_raw_response_wrapper(
            analytic_imagery.history,
        )
        self.history_aodr = to_raw_response_wrapper(
            analytic_imagery.history_aodr,
        )
        self.history_count = to_raw_response_wrapper(
            analytic_imagery.history_count,
        )
        self.queryhelp = to_raw_response_wrapper(
            analytic_imagery.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            analytic_imagery.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            analytic_imagery.unvalidated_publish,
        )


class AsyncAnalyticImageryResourceWithRawResponse:
    def __init__(self, analytic_imagery: AsyncAnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.retrieve = async_to_raw_response_wrapper(
            analytic_imagery.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            analytic_imagery.list,
        )
        self.count = async_to_raw_response_wrapper(
            analytic_imagery.count,
        )
        self.file_get = async_to_custom_raw_response_wrapper(
            analytic_imagery.file_get,
            AsyncBinaryAPIResponse,
        )
        self.history = async_to_raw_response_wrapper(
            analytic_imagery.history,
        )
        self.history_aodr = async_to_raw_response_wrapper(
            analytic_imagery.history_aodr,
        )
        self.history_count = async_to_raw_response_wrapper(
            analytic_imagery.history_count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            analytic_imagery.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            analytic_imagery.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            analytic_imagery.unvalidated_publish,
        )


class AnalyticImageryResourceWithStreamingResponse:
    def __init__(self, analytic_imagery: AnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.retrieve = to_streamed_response_wrapper(
            analytic_imagery.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            analytic_imagery.list,
        )
        self.count = to_streamed_response_wrapper(
            analytic_imagery.count,
        )
        self.file_get = to_custom_streamed_response_wrapper(
            analytic_imagery.file_get,
            StreamedBinaryAPIResponse,
        )
        self.history = to_streamed_response_wrapper(
            analytic_imagery.history,
        )
        self.history_aodr = to_streamed_response_wrapper(
            analytic_imagery.history_aodr,
        )
        self.history_count = to_streamed_response_wrapper(
            analytic_imagery.history_count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            analytic_imagery.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            analytic_imagery.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            analytic_imagery.unvalidated_publish,
        )


class AsyncAnalyticImageryResourceWithStreamingResponse:
    def __init__(self, analytic_imagery: AsyncAnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.retrieve = async_to_streamed_response_wrapper(
            analytic_imagery.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            analytic_imagery.list,
        )
        self.count = async_to_streamed_response_wrapper(
            analytic_imagery.count,
        )
        self.file_get = async_to_custom_streamed_response_wrapper(
            analytic_imagery.file_get,
            AsyncStreamedBinaryAPIResponse,
        )
        self.history = async_to_streamed_response_wrapper(
            analytic_imagery.history,
        )
        self.history_aodr = async_to_streamed_response_wrapper(
            analytic_imagery.history_aodr,
        )
        self.history_count = async_to_streamed_response_wrapper(
            analytic_imagery.history_count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            analytic_imagery.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            analytic_imagery.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            analytic_imagery.unvalidated_publish,
        )
