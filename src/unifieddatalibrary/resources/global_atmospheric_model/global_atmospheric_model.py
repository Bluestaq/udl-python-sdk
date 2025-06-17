# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    global_atmospheric_model_count_params,
    global_atmospheric_model_query_params,
    global_atmospheric_model_tuple_params,
    global_atmospheric_model_get_file_params,
    global_atmospheric_model_retrieve_params,
    global_atmospheric_model_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.global_atmospheric_model_query_response import GlobalAtmosphericModelQueryResponse
from ...types.global_atmospheric_model_tuple_response import GlobalAtmosphericModelTupleResponse
from ...types.global_atmospheric_model_retrieve_response import GlobalAtmosphericModelRetrieveResponse
from ...types.global_atmospheric_model_query_help_response import GlobalAtmosphericModelQueryHelpResponse

__all__ = ["GlobalAtmosphericModelResource", "AsyncGlobalAtmosphericModelResource"]


class GlobalAtmosphericModelResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> GlobalAtmosphericModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GlobalAtmosphericModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalAtmosphericModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return GlobalAtmosphericModelResourceWithStreamingResponse(self)

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
    ) -> GlobalAtmosphericModelRetrieveResponse:
        """
        Service operation to get a single GlobalAtmosphericModel record by its unique ID
        passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/globalatmosphericmodel/{id}",
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
                    global_atmospheric_model_retrieve_params.GlobalAtmosphericModelRetrieveParams,
                ),
            ),
            cast_to=GlobalAtmosphericModelRetrieveResponse,
        )

    def count(
        self,
        *,
        ts: Union[str, datetime],
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
          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/globalatmosphericmodel/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    global_atmospheric_model_count_params.GlobalAtmosphericModelCountParams,
                ),
            ),
            cast_to=str,
        )

    def get_file(
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
        Service operation to get a single GlobalAtmosphericModel compressed data file by
        its unique ID passed as a path parameter. The compressed data file is returned
        as an attachment Content-Disposition.

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
            f"/udl/globalatmosphericmodel/getFile/{id}",
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
                    global_atmospheric_model_get_file_params.GlobalAtmosphericModelGetFileParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def query(
        self,
        *,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalAtmosphericModelQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/globalatmosphericmodel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    global_atmospheric_model_query_params.GlobalAtmosphericModelQueryParams,
                ),
            ),
            cast_to=GlobalAtmosphericModelQueryResponse,
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
    ) -> GlobalAtmosphericModelQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/globalatmosphericmodel/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalAtmosphericModelQueryHelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalAtmosphericModelTupleResponse:
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

          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/globalatmosphericmodel/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    global_atmospheric_model_tuple_params.GlobalAtmosphericModelTupleParams,
                ),
            ),
            cast_to=GlobalAtmosphericModelTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        ts: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        cadence: int | NotGiven = NOT_GIVEN,
        end_alt: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        num_alt: int | NotGiven = NOT_GIVEN,
        num_lat: int | NotGiven = NOT_GIVEN,
        num_lon: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_alt: float | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        step_lat: float | NotGiven = NOT_GIVEN,
        step_lon: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Upload a file with its metadata.

        The request body requires a zip file containing exactly two files:\\
        1\\)) A file with the `.json` file extension whose content conforms to the `GlobalAtmosphericModel_Ingest`
        schema.\\
        2\\)) A file with the `.geojson` file extension.

        The JSON and GEOJSON files will be associated with each other other via the `id`
        field. Query the metadata via `GET /udl/globalatmosphericmodel` and use
        `GET /udl/globalatmosphericmodel/getFile/{id}` to retrieve the compressed
        GEOJSON file as `.gz` extension.

        This operation only accepts application/zip media. The application/json request
        body is documented to provide a convenient reference to the ingest schema.

        This operation is intended to be used for automated feeds into UDL. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          source: Source of the data.

          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.

          type: Type of data associated with this record (e.g. Global Total Electron Density,
              Global Total Electron Content).

          id: Unique identifier of the record, auto-generated by the system.

          cadence: Model execution cadence, in minutes.

          end_alt: Ending altitude of model outputs, in kilometers.

          end_lat: WGS-84 ending latitude of model output, in degrees. -90 to 90 degrees (negative
              values south of equator).

          end_lon: WGS-84 ending longitude of model output, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          filename: The file name of the uploaded file.

          filesize: The uploaded file size, in bytes. The maximum file size for this service is
              104857600 bytes (100MB). Files exceeding the maximum size will be rejected.

          num_alt: Number of altitude points.

          num_lat: Number of latitude points.

          num_lon: Number of longitude points.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          report_time: The time that this record was created, in ISO 8601 UTC format with millisecond
              precision.

          start_alt: Starting altitude of model outputs, in kilometers.

          start_lat: WGS-84 starting latitude of model output, in degrees. -90 to 90 degrees
              (negative values south of equator).

          start_lon: WGS-84 starting longitude of model output, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          state: State value indicating whether the values in this record are PREDICTED or
              OBSERVED.

          step_lat: Separation in latitude between subsequent model outputs, in degrees.

          step_lon: Separation in longitude between subsequent model outputs, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-globalatmosphericmodel",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "ts": ts,
                    "type": type,
                    "id": id,
                    "cadence": cadence,
                    "end_alt": end_alt,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "filename": filename,
                    "filesize": filesize,
                    "num_alt": num_alt,
                    "num_lat": num_lat,
                    "num_lon": num_lon,
                    "origin": origin,
                    "report_time": report_time,
                    "start_alt": start_alt,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "state": state,
                    "step_lat": step_lat,
                    "step_lon": step_lon,
                },
                global_atmospheric_model_unvalidated_publish_params.GlobalAtmosphericModelUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGlobalAtmosphericModelResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGlobalAtmosphericModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalAtmosphericModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalAtmosphericModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncGlobalAtmosphericModelResourceWithStreamingResponse(self)

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
    ) -> GlobalAtmosphericModelRetrieveResponse:
        """
        Service operation to get a single GlobalAtmosphericModel record by its unique ID
        passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/globalatmosphericmodel/{id}",
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
                    global_atmospheric_model_retrieve_params.GlobalAtmosphericModelRetrieveParams,
                ),
            ),
            cast_to=GlobalAtmosphericModelRetrieveResponse,
        )

    async def count(
        self,
        *,
        ts: Union[str, datetime],
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
          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/globalatmosphericmodel/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    global_atmospheric_model_count_params.GlobalAtmosphericModelCountParams,
                ),
            ),
            cast_to=str,
        )

    async def get_file(
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
        Service operation to get a single GlobalAtmosphericModel compressed data file by
        its unique ID passed as a path parameter. The compressed data file is returned
        as an attachment Content-Disposition.

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
            f"/udl/globalatmosphericmodel/getFile/{id}",
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
                    global_atmospheric_model_get_file_params.GlobalAtmosphericModelGetFileParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def query(
        self,
        *,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalAtmosphericModelQueryResponse:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/globalatmosphericmodel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    global_atmospheric_model_query_params.GlobalAtmosphericModelQueryParams,
                ),
            ),
            cast_to=GlobalAtmosphericModelQueryResponse,
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
    ) -> GlobalAtmosphericModelQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/globalatmosphericmodel/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalAtmosphericModelQueryHelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        ts: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalAtmosphericModelTupleResponse:
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

          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/globalatmosphericmodel/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "ts": ts,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    global_atmospheric_model_tuple_params.GlobalAtmosphericModelTupleParams,
                ),
            ),
            cast_to=GlobalAtmosphericModelTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        ts: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        cadence: int | NotGiven = NOT_GIVEN,
        end_alt: float | NotGiven = NOT_GIVEN,
        end_lat: float | NotGiven = NOT_GIVEN,
        end_lon: float | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        num_alt: int | NotGiven = NOT_GIVEN,
        num_lat: int | NotGiven = NOT_GIVEN,
        num_lon: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_alt: float | NotGiven = NOT_GIVEN,
        start_lat: float | NotGiven = NOT_GIVEN,
        start_lon: float | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        step_lat: float | NotGiven = NOT_GIVEN,
        step_lon: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Upload a file with its metadata.

        The request body requires a zip file containing exactly two files:\\
        1\\)) A file with the `.json` file extension whose content conforms to the `GlobalAtmosphericModel_Ingest`
        schema.\\
        2\\)) A file with the `.geojson` file extension.

        The JSON and GEOJSON files will be associated with each other other via the `id`
        field. Query the metadata via `GET /udl/globalatmosphericmodel` and use
        `GET /udl/globalatmosphericmodel/getFile/{id}` to retrieve the compressed
        GEOJSON file as `.gz` extension.

        This operation only accepts application/zip media. The application/json request
        body is documented to provide a convenient reference to the ingest schema.

        This operation is intended to be used for automated feeds into UDL. A specific
        role is required to perform this service operation. Please contact the UDL team
        for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode:
              Indicator of whether the data is EXERCISE, REAL, SIMULATED, or TEST data:

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

          source: Source of the data.

          ts: Target time of the model in ISO 8601 UTC format with millisecond precision.

          type: Type of data associated with this record (e.g. Global Total Electron Density,
              Global Total Electron Content).

          id: Unique identifier of the record, auto-generated by the system.

          cadence: Model execution cadence, in minutes.

          end_alt: Ending altitude of model outputs, in kilometers.

          end_lat: WGS-84 ending latitude of model output, in degrees. -90 to 90 degrees (negative
              values south of equator).

          end_lon: WGS-84 ending longitude of model output, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          filename: The file name of the uploaded file.

          filesize: The uploaded file size, in bytes. The maximum file size for this service is
              104857600 bytes (100MB). Files exceeding the maximum size will be rejected.

          num_alt: Number of altitude points.

          num_lat: Number of latitude points.

          num_lon: Number of longitude points.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          report_time: The time that this record was created, in ISO 8601 UTC format with millisecond
              precision.

          start_alt: Starting altitude of model outputs, in kilometers.

          start_lat: WGS-84 starting latitude of model output, in degrees. -90 to 90 degrees
              (negative values south of equator).

          start_lon: WGS-84 starting longitude of model output, in degrees. -180 to 180 degrees
              (negative values west of Prime Meridian).

          state: State value indicating whether the values in this record are PREDICTED or
              OBSERVED.

          step_lat: Separation in latitude between subsequent model outputs, in degrees.

          step_lon: Separation in longitude between subsequent model outputs, in degrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-globalatmosphericmodel",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "ts": ts,
                    "type": type,
                    "id": id,
                    "cadence": cadence,
                    "end_alt": end_alt,
                    "end_lat": end_lat,
                    "end_lon": end_lon,
                    "filename": filename,
                    "filesize": filesize,
                    "num_alt": num_alt,
                    "num_lat": num_lat,
                    "num_lon": num_lon,
                    "origin": origin,
                    "report_time": report_time,
                    "start_alt": start_alt,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "state": state,
                    "step_lat": step_lat,
                    "step_lon": step_lon,
                },
                global_atmospheric_model_unvalidated_publish_params.GlobalAtmosphericModelUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GlobalAtmosphericModelResourceWithRawResponse:
    def __init__(self, global_atmospheric_model: GlobalAtmosphericModelResource) -> None:
        self._global_atmospheric_model = global_atmospheric_model

        self.retrieve = to_raw_response_wrapper(
            global_atmospheric_model.retrieve,
        )
        self.count = to_raw_response_wrapper(
            global_atmospheric_model.count,
        )
        self.get_file = to_custom_raw_response_wrapper(
            global_atmospheric_model.get_file,
            BinaryAPIResponse,
        )
        self.query = to_raw_response_wrapper(
            global_atmospheric_model.query,
        )
        self.query_help = to_raw_response_wrapper(
            global_atmospheric_model.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            global_atmospheric_model.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            global_atmospheric_model.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._global_atmospheric_model.history)


class AsyncGlobalAtmosphericModelResourceWithRawResponse:
    def __init__(self, global_atmospheric_model: AsyncGlobalAtmosphericModelResource) -> None:
        self._global_atmospheric_model = global_atmospheric_model

        self.retrieve = async_to_raw_response_wrapper(
            global_atmospheric_model.retrieve,
        )
        self.count = async_to_raw_response_wrapper(
            global_atmospheric_model.count,
        )
        self.get_file = async_to_custom_raw_response_wrapper(
            global_atmospheric_model.get_file,
            AsyncBinaryAPIResponse,
        )
        self.query = async_to_raw_response_wrapper(
            global_atmospheric_model.query,
        )
        self.query_help = async_to_raw_response_wrapper(
            global_atmospheric_model.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            global_atmospheric_model.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            global_atmospheric_model.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._global_atmospheric_model.history)


class GlobalAtmosphericModelResourceWithStreamingResponse:
    def __init__(self, global_atmospheric_model: GlobalAtmosphericModelResource) -> None:
        self._global_atmospheric_model = global_atmospheric_model

        self.retrieve = to_streamed_response_wrapper(
            global_atmospheric_model.retrieve,
        )
        self.count = to_streamed_response_wrapper(
            global_atmospheric_model.count,
        )
        self.get_file = to_custom_streamed_response_wrapper(
            global_atmospheric_model.get_file,
            StreamedBinaryAPIResponse,
        )
        self.query = to_streamed_response_wrapper(
            global_atmospheric_model.query,
        )
        self.query_help = to_streamed_response_wrapper(
            global_atmospheric_model.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            global_atmospheric_model.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            global_atmospheric_model.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._global_atmospheric_model.history)


class AsyncGlobalAtmosphericModelResourceWithStreamingResponse:
    def __init__(self, global_atmospheric_model: AsyncGlobalAtmosphericModelResource) -> None:
        self._global_atmospheric_model = global_atmospheric_model

        self.retrieve = async_to_streamed_response_wrapper(
            global_atmospheric_model.retrieve,
        )
        self.count = async_to_streamed_response_wrapper(
            global_atmospheric_model.count,
        )
        self.get_file = async_to_custom_streamed_response_wrapper(
            global_atmospheric_model.get_file,
            AsyncStreamedBinaryAPIResponse,
        )
        self.query = async_to_streamed_response_wrapper(
            global_atmospheric_model.query,
        )
        self.query_help = async_to_streamed_response_wrapper(
            global_atmospheric_model.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            global_atmospheric_model.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            global_atmospheric_model.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._global_atmospheric_model.history)
