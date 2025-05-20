# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Mapping, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    ground_imagery_get_params,
    ground_imagery_list_params,
    ground_imagery_count_params,
    ground_imagery_tuple_params,
    ground_imagery_create_params,
    ground_imagery_get_file_params,
    ground_imagery_upload_zip_params,
    ground_imagery_history_aodr_params,
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
from ...types.ground_imagery_get_response import GroundImageryGetResponse
from ...types.ground_imagery_list_response import GroundImageryListResponse
from ...types.ground_imagery_tuple_response import GroundImageryTupleResponse

__all__ = ["GroundImageryResource", "AsyncGroundImageryResource"]


class GroundImageryResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> GroundImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GroundImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroundImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return GroundImageryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        filename: str,
        image_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        checksum_value: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        keywords: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        region_geo_json: str | NotGiven = NOT_GIVEN,
        region_n_dims: int | NotGiven = NOT_GIVEN,
        region_s_rid: int | NotGiven = NOT_GIVEN,
        region_text: str | NotGiven = NOT_GIVEN,
        region_type: str | NotGiven = NOT_GIVEN,
        subject_id: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single GroundImagery object as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          filename: Name of the image file.

          image_time: Timestamp the image was captured/produced.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          checksum_value: MD5 value of the file. The ingest/create operation will automatically generate
              the value.

          filesize: Size of the image file. Units in bytes. If filesize is provided without an
              associated file, it defaults to 0.

          format: Optional, field indicating type of image, NITF, PNG, etc.

          id_sensor: Optional ID of the sensor that produced this ground image.

          keywords: Optional array of keywords for this image.

          name: Optional name/description associated with this image.

          notes: Description and notes of the image.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by source to indicate the sensor identifier used to
              detect this event. This may be an internal identifier and not necessarily a
              valid sensor ID.

          region: Geographical region or polygon (lon/lat pairs) of the image as projected on the
              ground in geoJSON or geoText format. This is an optional convenience field only
              used for create operations. The system will auto-detect the format (Well Known
              Text or GeoJSON) and populate both regionText and regionGeoJSON fields
              appropriately. When omitted, regionText or regionGeoJSON is expected.

          region_geo_json: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. Reference: https://geojson.org/. Ignored if included with a create
              operation that also specifies a valid region or regionText.

          region_n_dims: Number of dimensions of the geometry depicted by region.

          region_s_rid: Geographical spatial_ref_sys for region.

          region_text: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a create operation that also specifies a valid region.

          region_type: Type of region as projected on the ground.

          subject_id: Optional identifier of the subject/target of the image, useful for correlating
              multiple images of the same subject.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/groundimagery",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "filename": filename,
                    "image_time": image_time,
                    "source": source,
                    "id": id,
                    "checksum_value": checksum_value,
                    "filesize": filesize,
                    "format": format,
                    "id_sensor": id_sensor,
                    "keywords": keywords,
                    "name": name,
                    "notes": notes,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "region": region,
                    "region_geo_json": region_geo_json,
                    "region_n_dims": region_n_dims,
                    "region_s_rid": region_s_rid,
                    "region_text": region_text,
                    "region_type": region_type,
                    "subject_id": subject_id,
                    "tags": tags,
                    "transaction_id": transaction_id,
                },
                ground_imagery_create_params.GroundImageryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        image_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[GroundImageryListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/groundimagery",
            page=SyncOffsetPage[GroundImageryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "image_time": image_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ground_imagery_list_params.GroundImageryListParams,
                ),
            ),
            model=GroundImageryListResponse,
        )

    def count(
        self,
        *,
        image_time: Union[str, datetime],
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
          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/groundimagery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "image_time": image_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ground_imagery_count_params.GroundImageryCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> GroundImageryGetResponse:
        """
        Service operation to get a single GroundImagery record by its unique ID passed
        as a path parameter. GroundImagery represents metadata about a ground image, as
        well as the actual binary image data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/groundimagery/{id}",
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
                    ground_imagery_get_params.GroundImageryGetParams,
                ),
            ),
            cast_to=GroundImageryGetResponse,
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
        Service operation to get a single GroundImagery binary image by its unique ID
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
            f"/udl/groundimagery/getFile/{id}",
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
                    ground_imagery_get_file_params.GroundImageryGetFileParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def history_aodr(
        self,
        *,
        image_time: Union[str, datetime],
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
          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

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
            "/udl/groundimagery/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "image_time": image_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    ground_imagery_history_aodr_params.GroundImageryHistoryAodrParams,
                ),
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
            "/udl/groundimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        image_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroundImageryTupleResponse:
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

          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/groundimagery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "image_time": image_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ground_imagery_tuple_params.GroundImageryTupleParams,
                ),
            ),
            cast_to=GroundImageryTupleResponse,
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
        1\\)) A file with the `.json` file extension whose content conforms to the `GroundImagery_Ingest`
        schema. 2\\)) A binary image file of the allowed types for this service.

        The JSON and image files will be associated with each other via the `id` field.
        Query the metadata via `GET /udl/groundimagery` and use
        `GET /udl/groundimagery/getFile/{id}` to retrieve the binary image file.

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
            "/filedrop/udl-groundimagery"
            if self._client._base_url_overridden
            else "https://imagery.unifieddatalibrary.com/filedrop/udl-groundimagery",
            body=maybe_transform(body, ground_imagery_upload_zip_params.GroundImageryUploadZipParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGroundImageryResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGroundImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGroundImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroundImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncGroundImageryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        filename: str,
        image_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        checksum_value: str | NotGiven = NOT_GIVEN,
        filesize: int | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        keywords: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        region_geo_json: str | NotGiven = NOT_GIVEN,
        region_n_dims: int | NotGiven = NOT_GIVEN,
        region_s_rid: int | NotGiven = NOT_GIVEN,
        region_text: str | NotGiven = NOT_GIVEN,
        region_type: str | NotGiven = NOT_GIVEN,
        subject_id: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single GroundImagery object as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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

          filename: Name of the image file.

          image_time: Timestamp the image was captured/produced.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          checksum_value: MD5 value of the file. The ingest/create operation will automatically generate
              the value.

          filesize: Size of the image file. Units in bytes. If filesize is provided without an
              associated file, it defaults to 0.

          format: Optional, field indicating type of image, NITF, PNG, etc.

          id_sensor: Optional ID of the sensor that produced this ground image.

          keywords: Optional array of keywords for this image.

          name: Optional name/description associated with this image.

          notes: Description and notes of the image.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sensor_id: Optional identifier provided by source to indicate the sensor identifier used to
              detect this event. This may be an internal identifier and not necessarily a
              valid sensor ID.

          region: Geographical region or polygon (lon/lat pairs) of the image as projected on the
              ground in geoJSON or geoText format. This is an optional convenience field only
              used for create operations. The system will auto-detect the format (Well Known
              Text or GeoJSON) and populate both regionText and regionGeoJSON fields
              appropriately. When omitted, regionText or regionGeoJSON is expected.

          region_geo_json: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. Reference: https://geojson.org/. Ignored if included with a create
              operation that also specifies a valid region or regionText.

          region_n_dims: Number of dimensions of the geometry depicted by region.

          region_s_rid: Geographical spatial_ref_sys for region.

          region_text: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a create operation that also specifies a valid region.

          region_type: Type of region as projected on the ground.

          subject_id: Optional identifier of the subject/target of the image, useful for correlating
              multiple images of the same subject.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/groundimagery",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "filename": filename,
                    "image_time": image_time,
                    "source": source,
                    "id": id,
                    "checksum_value": checksum_value,
                    "filesize": filesize,
                    "format": format,
                    "id_sensor": id_sensor,
                    "keywords": keywords,
                    "name": name,
                    "notes": notes,
                    "origin": origin,
                    "orig_sensor_id": orig_sensor_id,
                    "region": region,
                    "region_geo_json": region_geo_json,
                    "region_n_dims": region_n_dims,
                    "region_s_rid": region_s_rid,
                    "region_text": region_text,
                    "region_type": region_type,
                    "subject_id": subject_id,
                    "tags": tags,
                    "transaction_id": transaction_id,
                },
                ground_imagery_create_params.GroundImageryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        image_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[GroundImageryListResponse, AsyncOffsetPage[GroundImageryListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/groundimagery",
            page=AsyncOffsetPage[GroundImageryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "image_time": image_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ground_imagery_list_params.GroundImageryListParams,
                ),
            ),
            model=GroundImageryListResponse,
        )

    async def count(
        self,
        *,
        image_time: Union[str, datetime],
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
          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/groundimagery/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "image_time": image_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ground_imagery_count_params.GroundImageryCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> GroundImageryGetResponse:
        """
        Service operation to get a single GroundImagery record by its unique ID passed
        as a path parameter. GroundImagery represents metadata about a ground image, as
        well as the actual binary image data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/groundimagery/{id}",
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
                    ground_imagery_get_params.GroundImageryGetParams,
                ),
            ),
            cast_to=GroundImageryGetResponse,
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
        Service operation to get a single GroundImagery binary image by its unique ID
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
            f"/udl/groundimagery/getFile/{id}",
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
                    ground_imagery_get_file_params.GroundImageryGetFileParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def history_aodr(
        self,
        *,
        image_time: Union[str, datetime],
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
          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

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
            "/udl/groundimagery/history/aodr",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "image_time": image_time,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                        "notification": notification,
                        "output_delimiter": output_delimiter,
                        "output_format": output_format,
                    },
                    ground_imagery_history_aodr_params.GroundImageryHistoryAodrParams,
                ),
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
            "/udl/groundimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        image_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroundImageryTupleResponse:
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

          image_time: Timestamp the image was captured/produced. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/groundimagery/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "image_time": image_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    ground_imagery_tuple_params.GroundImageryTupleParams,
                ),
            ),
            cast_to=GroundImageryTupleResponse,
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
        1\\)) A file with the `.json` file extension whose content conforms to the `GroundImagery_Ingest`
        schema. 2\\)) A binary image file of the allowed types for this service.

        The JSON and image files will be associated with each other via the `id` field.
        Query the metadata via `GET /udl/groundimagery` and use
        `GET /udl/groundimagery/getFile/{id}` to retrieve the binary image file.

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
            "/filedrop/udl-groundimagery"
            if self._client._base_url_overridden
            else "https://imagery.unifieddatalibrary.com/filedrop/udl-groundimagery",
            body=await async_maybe_transform(body, ground_imagery_upload_zip_params.GroundImageryUploadZipParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GroundImageryResourceWithRawResponse:
    def __init__(self, ground_imagery: GroundImageryResource) -> None:
        self._ground_imagery = ground_imagery

        self.create = to_raw_response_wrapper(
            ground_imagery.create,
        )
        self.list = to_raw_response_wrapper(
            ground_imagery.list,
        )
        self.count = to_raw_response_wrapper(
            ground_imagery.count,
        )
        self.get = to_raw_response_wrapper(
            ground_imagery.get,
        )
        self.get_file = to_custom_raw_response_wrapper(
            ground_imagery.get_file,
            BinaryAPIResponse,
        )
        self.history_aodr = to_raw_response_wrapper(
            ground_imagery.history_aodr,
        )
        self.queryhelp = to_raw_response_wrapper(
            ground_imagery.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            ground_imagery.tuple,
        )
        self.upload_zip = to_raw_response_wrapper(
            ground_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._ground_imagery.history)


class AsyncGroundImageryResourceWithRawResponse:
    def __init__(self, ground_imagery: AsyncGroundImageryResource) -> None:
        self._ground_imagery = ground_imagery

        self.create = async_to_raw_response_wrapper(
            ground_imagery.create,
        )
        self.list = async_to_raw_response_wrapper(
            ground_imagery.list,
        )
        self.count = async_to_raw_response_wrapper(
            ground_imagery.count,
        )
        self.get = async_to_raw_response_wrapper(
            ground_imagery.get,
        )
        self.get_file = async_to_custom_raw_response_wrapper(
            ground_imagery.get_file,
            AsyncBinaryAPIResponse,
        )
        self.history_aodr = async_to_raw_response_wrapper(
            ground_imagery.history_aodr,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            ground_imagery.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            ground_imagery.tuple,
        )
        self.upload_zip = async_to_raw_response_wrapper(
            ground_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._ground_imagery.history)


class GroundImageryResourceWithStreamingResponse:
    def __init__(self, ground_imagery: GroundImageryResource) -> None:
        self._ground_imagery = ground_imagery

        self.create = to_streamed_response_wrapper(
            ground_imagery.create,
        )
        self.list = to_streamed_response_wrapper(
            ground_imagery.list,
        )
        self.count = to_streamed_response_wrapper(
            ground_imagery.count,
        )
        self.get = to_streamed_response_wrapper(
            ground_imagery.get,
        )
        self.get_file = to_custom_streamed_response_wrapper(
            ground_imagery.get_file,
            StreamedBinaryAPIResponse,
        )
        self.history_aodr = to_streamed_response_wrapper(
            ground_imagery.history_aodr,
        )
        self.queryhelp = to_streamed_response_wrapper(
            ground_imagery.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            ground_imagery.tuple,
        )
        self.upload_zip = to_streamed_response_wrapper(
            ground_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._ground_imagery.history)


class AsyncGroundImageryResourceWithStreamingResponse:
    def __init__(self, ground_imagery: AsyncGroundImageryResource) -> None:
        self._ground_imagery = ground_imagery

        self.create = async_to_streamed_response_wrapper(
            ground_imagery.create,
        )
        self.list = async_to_streamed_response_wrapper(
            ground_imagery.list,
        )
        self.count = async_to_streamed_response_wrapper(
            ground_imagery.count,
        )
        self.get = async_to_streamed_response_wrapper(
            ground_imagery.get,
        )
        self.get_file = async_to_custom_streamed_response_wrapper(
            ground_imagery.get_file,
            AsyncStreamedBinaryAPIResponse,
        )
        self.history_aodr = async_to_streamed_response_wrapper(
            ground_imagery.history_aodr,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            ground_imagery.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            ground_imagery.tuple,
        )
        self.upload_zip = async_to_streamed_response_wrapper(
            ground_imagery.upload_zip,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._ground_imagery.history)
