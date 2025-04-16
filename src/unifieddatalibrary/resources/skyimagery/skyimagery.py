# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, cast
from datetime import datetime

import httpx

from ...types import (
    skyimagery_list_params,
    skyimagery_count_params,
    skyimagery_tuple_params,
    skyimagery_upload_zip_params,
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
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
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
from ..._base_client import make_request_options
from ...types.skyimagery_list_response import SkyimageryListResponse
from ...types.skyimagery_tuple_response import SkyimageryTupleResponse
from ...types.udl.skyimagery.skyimagery_full import SkyimageryFull

__all__ = ["SkyimageryResource", "AsyncSkyimageryResource"]


class SkyimageryResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkyimageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SkyimageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkyimageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return SkyimageryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        exp_start_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyimageryListResponse:
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
        return self._get(
            "/udl/skyimagery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exp_start_time": exp_start_time}, skyimagery_list_params.SkyimageryListParams),
            ),
            cast_to=SkyimageryListResponse,
        )

    def count(
        self,
        *,
        exp_start_time: Union[str, datetime],
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
                    {"exp_start_time": exp_start_time}, skyimagery_count_params.SkyimageryCountParams
                ),
            ),
            cast_to=str,
        )

    def file_get(
        self,
        id: str,
        *,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyimageryFull:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkyimageryFull,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyimageryTupleResponse:
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
                    },
                    skyimagery_tuple_params.SkyimageryTupleParams,
                ),
            ),
            cast_to=SkyimageryTupleResponse,
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
            "/filedrop/udl-skyimagery",
            body=maybe_transform(body, skyimagery_upload_zip_params.SkyimageryUploadZipParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSkyimageryResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkyimageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSkyimageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkyimageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSkyimageryResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        exp_start_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyimageryListResponse:
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
        return await self._get(
            "/udl/skyimagery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"exp_start_time": exp_start_time}, skyimagery_list_params.SkyimageryListParams
                ),
            ),
            cast_to=SkyimageryListResponse,
        )

    async def count(
        self,
        *,
        exp_start_time: Union[str, datetime],
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
                    {"exp_start_time": exp_start_time}, skyimagery_count_params.SkyimageryCountParams
                ),
            ),
            cast_to=str,
        )

    async def file_get(
        self,
        id: str,
        *,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyimageryFull:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkyimageryFull,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkyimageryTupleResponse:
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
                    },
                    skyimagery_tuple_params.SkyimageryTupleParams,
                ),
            ),
            cast_to=SkyimageryTupleResponse,
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
            "/filedrop/udl-skyimagery",
            body=await async_maybe_transform(body, skyimagery_upload_zip_params.SkyimageryUploadZipParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SkyimageryResourceWithRawResponse:
    def __init__(self, skyimagery: SkyimageryResource) -> None:
        self._skyimagery = skyimagery

        self.list = to_raw_response_wrapper(
            skyimagery.list,
        )
        self.count = to_raw_response_wrapper(
            skyimagery.count,
        )
        self.file_get = to_custom_raw_response_wrapper(
            skyimagery.file_get,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            skyimagery.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            skyimagery.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            skyimagery.tuple,
        )
        self.upload_zip = to_raw_response_wrapper(
            skyimagery.upload_zip,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._skyimagery.history)


class AsyncSkyimageryResourceWithRawResponse:
    def __init__(self, skyimagery: AsyncSkyimageryResource) -> None:
        self._skyimagery = skyimagery

        self.list = async_to_raw_response_wrapper(
            skyimagery.list,
        )
        self.count = async_to_raw_response_wrapper(
            skyimagery.count,
        )
        self.file_get = async_to_custom_raw_response_wrapper(
            skyimagery.file_get,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            skyimagery.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            skyimagery.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            skyimagery.tuple,
        )
        self.upload_zip = async_to_raw_response_wrapper(
            skyimagery.upload_zip,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._skyimagery.history)


class SkyimageryResourceWithStreamingResponse:
    def __init__(self, skyimagery: SkyimageryResource) -> None:
        self._skyimagery = skyimagery

        self.list = to_streamed_response_wrapper(
            skyimagery.list,
        )
        self.count = to_streamed_response_wrapper(
            skyimagery.count,
        )
        self.file_get = to_custom_streamed_response_wrapper(
            skyimagery.file_get,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            skyimagery.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            skyimagery.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            skyimagery.tuple,
        )
        self.upload_zip = to_streamed_response_wrapper(
            skyimagery.upload_zip,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._skyimagery.history)


class AsyncSkyimageryResourceWithStreamingResponse:
    def __init__(self, skyimagery: AsyncSkyimageryResource) -> None:
        self._skyimagery = skyimagery

        self.list = async_to_streamed_response_wrapper(
            skyimagery.list,
        )
        self.count = async_to_streamed_response_wrapper(
            skyimagery.count,
        )
        self.file_get = async_to_custom_streamed_response_wrapper(
            skyimagery.file_get,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            skyimagery.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            skyimagery.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            skyimagery.tuple,
        )
        self.upload_zip = async_to_streamed_response_wrapper(
            skyimagery.upload_zip,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._skyimagery.history)
