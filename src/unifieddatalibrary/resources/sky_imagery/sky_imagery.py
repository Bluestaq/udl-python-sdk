# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, cast
from datetime import datetime

import httpx

from ...types import (
    sky_imagery_get_params,
    sky_imagery_list_params,
    sky_imagery_count_params,
    sky_imagery_tuple_params,
    sky_imagery_file_get_params,
    sky_imagery_upload_zip_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.sky_imagery_get_response import SkyImageryGetResponse
from ...types.sky_imagery_list_response import SkyImageryListResponse
from ...types.sky_imagery_tuple_response import SkyImageryTupleResponse

__all__ = ["SkyImageryResource", "AsyncSkyImageryResource"]


class SkyImageryResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkyImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SkyImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkyImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SkyImageryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        exp_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SkyImageryListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/skyimagery",
            page=SyncOffsetPage[SkyImageryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exp_start_time": exp_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sky_imagery_list_params.SkyImageryListParams,
                ),
            ),
            model=SkyImageryListResponse,
        )

    def count(
        self,
        *,
        exp_start_time: Union[str, datetime],
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
          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/skyimagery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exp_start_time": exp_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sky_imagery_count_params.SkyImageryCountParams,
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
        Service operation to get a single SkyImagery binary image by its unique ID
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
            f"/udl/skyimagery/getFile/{id}",
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
                    sky_imagery_file_get_params.SkyImageryFileGetParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
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
    ) -> SkyImageryGetResponse:
        """
        Service operation to get a single SkyImagery record by its unique ID passed as a
        path parameter. SkyImagery represents metadata about a sky image, as well as the
        actual binary image data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/skyimagery/{id}",
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
                    sky_imagery_get_params.SkyImageryGetParams,
                ),
            ),
            cast_to=SkyImageryGetResponse,
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
            "/udl/skyimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        exp_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyImageryTupleResponse:
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

          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/skyimagery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "exp_start_time": exp_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sky_imagery_tuple_params.SkyImageryTupleParams,
                ),
            ),
            cast_to=SkyImageryTupleResponse,
        )

    def upload_zip(
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
        1\\)) A file with the `.json` file extension whose content conforms to the `SkyImagery_Ingest`
        schema.\\
        2\\)) A binary image file of the allowed types for this service.

        The JSON and image files will be associated with each other via the `id` field.
        Query the metadata via `GET /udl/skyimagery` and use
        `GET /udl/skyimagery/getFile/{id}` to retrieve the binary image file.

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
            "/filedrop/udl-skyimagery"
            if self._client._base_url_overridden
            else "https://imagery.unifieddatalibrary.com/filedrop/udl-skyimagery",
            body=maybe_transform(body, sky_imagery_upload_zip_params.SkyImageryUploadZipParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSkyImageryResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkyImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSkyImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkyImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSkyImageryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        exp_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SkyImageryListResponse, AsyncOffsetPage[SkyImageryListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/skyimagery",
            page=AsyncOffsetPage[SkyImageryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exp_start_time": exp_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sky_imagery_list_params.SkyImageryListParams,
                ),
            ),
            model=SkyImageryListResponse,
        )

    async def count(
        self,
        *,
        exp_start_time: Union[str, datetime],
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
          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/skyimagery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exp_start_time": exp_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sky_imagery_count_params.SkyImageryCountParams,
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
        Service operation to get a single SkyImagery binary image by its unique ID
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
            f"/udl/skyimagery/getFile/{id}",
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
                    sky_imagery_file_get_params.SkyImageryFileGetParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
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
    ) -> SkyImageryGetResponse:
        """
        Service operation to get a single SkyImagery record by its unique ID passed as a
        path parameter. SkyImagery represents metadata about a sky image, as well as the
        actual binary image data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/skyimagery/{id}",
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
                    sky_imagery_get_params.SkyImageryGetParams,
                ),
            ),
            cast_to=SkyImageryGetResponse,
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
            "/udl/skyimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        exp_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyImageryTupleResponse:
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

          exp_start_time: Start time of the exposure, in ISO 8601 UTC format with microsecond precision.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/skyimagery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "exp_start_time": exp_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    sky_imagery_tuple_params.SkyImageryTupleParams,
                ),
            ),
            cast_to=SkyImageryTupleResponse,
        )

    async def upload_zip(
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
        1\\)) A file with the `.json` file extension whose content conforms to the `SkyImagery_Ingest`
        schema.\\
        2\\)) A binary image file of the allowed types for this service.

        The JSON and image files will be associated with each other via the `id` field.
        Query the metadata via `GET /udl/skyimagery` and use
        `GET /udl/skyimagery/getFile/{id}` to retrieve the binary image file.

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
            "/filedrop/udl-skyimagery"
            if self._client._base_url_overridden
            else "https://imagery.unifieddatalibrary.com/filedrop/udl-skyimagery",
            body=await async_maybe_transform(body, sky_imagery_upload_zip_params.SkyImageryUploadZipParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SkyImageryResourceWithRawResponse:
    def __init__(self, sky_imagery: SkyImageryResource) -> None:
        self._sky_imagery = sky_imagery

        self.list = to_raw_response_wrapper(
            sky_imagery.list,
        )
        self.count = to_raw_response_wrapper(
            sky_imagery.count,
        )
        self.file_get = to_custom_raw_response_wrapper(
            sky_imagery.file_get,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            sky_imagery.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            sky_imagery.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            sky_imagery.tuple,
        )
        self.upload_zip = to_raw_response_wrapper(
            sky_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._sky_imagery.history)


class AsyncSkyImageryResourceWithRawResponse:
    def __init__(self, sky_imagery: AsyncSkyImageryResource) -> None:
        self._sky_imagery = sky_imagery

        self.list = async_to_raw_response_wrapper(
            sky_imagery.list,
        )
        self.count = async_to_raw_response_wrapper(
            sky_imagery.count,
        )
        self.file_get = async_to_custom_raw_response_wrapper(
            sky_imagery.file_get,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            sky_imagery.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            sky_imagery.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            sky_imagery.tuple,
        )
        self.upload_zip = async_to_raw_response_wrapper(
            sky_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._sky_imagery.history)


class SkyImageryResourceWithStreamingResponse:
    def __init__(self, sky_imagery: SkyImageryResource) -> None:
        self._sky_imagery = sky_imagery

        self.list = to_streamed_response_wrapper(
            sky_imagery.list,
        )
        self.count = to_streamed_response_wrapper(
            sky_imagery.count,
        )
        self.file_get = to_custom_streamed_response_wrapper(
            sky_imagery.file_get,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            sky_imagery.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            sky_imagery.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            sky_imagery.tuple,
        )
        self.upload_zip = to_streamed_response_wrapper(
            sky_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._sky_imagery.history)


class AsyncSkyImageryResourceWithStreamingResponse:
    def __init__(self, sky_imagery: AsyncSkyImageryResource) -> None:
        self._sky_imagery = sky_imagery

        self.list = async_to_streamed_response_wrapper(
            sky_imagery.list,
        )
        self.count = async_to_streamed_response_wrapper(
            sky_imagery.count,
        )
        self.file_get = async_to_custom_streamed_response_wrapper(
            sky_imagery.file_get,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            sky_imagery.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            sky_imagery.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            sky_imagery.tuple,
        )
        self.upload_zip = async_to_streamed_response_wrapper(
            sky_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._sky_imagery.history)
