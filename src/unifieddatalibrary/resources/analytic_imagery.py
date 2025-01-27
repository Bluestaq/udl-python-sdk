# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    analytic_imagery_list_params,
    analytic_imagery_count_params,
    analytic_imagery_tuple_params,
    analytic_imagery_create_params,
    analytic_imagery_history_params,
    analytic_imagery_history_aodr_params,
    analytic_imagery_history_count_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from .._base_client import make_request_options
from ..types.analytic_imagery_full import AnalyticImageryFull
from ..types.analytic_imagery_list_response import AnalyticImageryListResponse
from ..types.analytic_imagery_tuple_response import AnalyticImageryTupleResponse
from ..types.analytic_imagery_history_response import AnalyticImageryHistoryResponse

__all__ = ["AnalyticImageryResource", "AsyncAnalyticImageryResource"]


class AnalyticImageryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AnalyticImageryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        content: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        description: str,
        filename: str,
        filesize: int,
        image_type: str,
        msg_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        ann_lims: Iterable[Iterable[int]] | NotGiven = NOT_GIVEN,
        ann_text: List[str] | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        data_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        data_stop: Union[str, datetime] | NotGiven = NOT_GIVEN,
        image_set_id: str | NotGiven = NOT_GIVEN,
        image_set_length: int | NotGiven = NOT_GIVEN,
        img_height: int | NotGiven = NOT_GIVEN,
        img_width: int | NotGiven = NOT_GIVEN,
        keywords: List[str] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        sat_id: List[str] | NotGiven = NOT_GIVEN,
        sat_id_conf: Iterable[float] | NotGiven = NOT_GIVEN,
        sequence_id: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        x_units: str | NotGiven = NOT_GIVEN,
        y_units: str | NotGiven = NOT_GIVEN,
        z_units: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The analytic imagery service allows for contribution of general images, such as
        data plots, graphs, heatmaps, and other graphics not supported as UDL ground or
        sky imagery. This service operation requires a zip file in the body of the POST
        request. The zip file must contain exactly two files. <h3> 1) A json file with
        any file name that ends in .json e.g. MyFitsFile.json The contents of the json
        file must be valid according to the schema for Analytic Imagery. 2) A binary
        image file of the specified types allowed for AnalyticImagery. </h3> The
        metadata and image files will be stored and associated with each other allowing
        queries of the data retrieval of the binary images. This operation is intended
        to be used for automated feeds into UDL. A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          content: General type of content of this image (CONTOUR, DIAGRAM, HEATMAP, HISTOGRAM,
              PLOT, SCREENSHOT).

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          description: Description of the image content and utility.

          filename: The image file name.

          filesize: The image file size, in bytes. The maximum file size for this service is
              40,000,000 bytes (40MB). Files exceeding the maximum size will be rejected.

          image_type: The type of image associated with this record (GIF, JPG, PNG, TIF).

          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          ann_lims: Rectangular annotation limits, specified in pixels, as an array of arrays of the
              coordinates [ [UL1x, UL1y], [UR1x, UR1y], [LR1x, LR1y], [LL1x, LL1y] ],
              indicating the corners of a rectangle beginning with the Upper Left (UL) and
              moving clockwise. Allows the image provider to highlight one or more rectangular
              area(s) of interest. The array must contain Nx4 two-element arrays, where N is
              the number of rectangles of interest. The associated annotation(s) should be
              included in the annText array.

          ann_text: Annotation text, a string array of annotation(s) corresponding to the
              rectangular areas specified in annLims. This array contains the annotation text
              associated with the areas of interest indicated in annLims, in order. This array
              should contain one annotation per four values of the area (annLims) array.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          data_start: The start time, in ISO8601 UTC format with millisecond precision, of the data
              used in the analysis or composition of the image content, when applicable.

          data_stop: The stop time, in ISO8601 UTC format with millisecond precision, of the data
              used in the analysis or composition of the image content, when applicable.

          image_set_id: User-defined set ID of a sequence of images. Used to associate related analytic
              image records.

          image_set_length: The number of images in an image set.

          img_height: The image height (vertical), in pixels.

          img_width: The image width (horizontal), in pixels.

          keywords: Array of searchable keywords for this analytic imagery record.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          sat_id: Assessed satellite ID (NORAD RSO object number). The 'satId' and 'satIdConf'
              arrays must match in size.

          sat_id_conf: Assessed satellite confidence corresponding to an assessment ID. Values are
              between 0.0 and 1.0. The 'satId' and 'satIdConf' arrays must match in size.

          sequence_id: The sequence number of an image within an image set. If null, then it is assumed
              that the order of images in an imageSet is not relevant.

          src_ids: Array of UUIDs of the UDL data records that are related to this image. See the
              associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object.

          src_typs: Array of UDL record types (AIS, CONJUNCTION, DOA, ELSET, EO, ESID, GROUNDIMAGE,
              POI, MANEUVER, MTI, NOTIFICATION, RADAR, RF, SIGACT, SKYIMAGE, SV, TRACK) that
              are related to this image. See the associated 'srcIds' array for the record
              UUIDs, positionally corresponding to the record types in this array. The
              'srcTyps' and 'srcIds' arrays must match in size.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          x_units: Optional field indicating the units that apply to the x-axis of the attached
              image, when applicable.

          y_units: Optional field indicating the units that apply to the y-axis of the attached
              image, when applicable.

          z_units: Optional field indicating the units that apply to the z-axis of the attached
              image, when applicable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-analyticimagery",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "content": content,
                    "data_mode": data_mode,
                    "description": description,
                    "filename": filename,
                    "filesize": filesize,
                    "image_type": image_type,
                    "msg_time": msg_time,
                    "source": source,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "ann_lims": ann_lims,
                    "ann_text": ann_text,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "data_start": data_start,
                    "data_stop": data_stop,
                    "image_set_id": image_set_id,
                    "image_set_length": image_set_length,
                    "img_height": img_height,
                    "img_width": img_width,
                    "keywords": keywords,
                    "origin": origin,
                    "sat_id": sat_id,
                    "sat_id_conf": sat_id_conf,
                    "sequence_id": sequence_id,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "x_units": x_units,
                    "y_units": y_units,
                    "z_units": z_units,
                },
                analytic_imagery_create_params.AnalyticImageryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        id: str,
        *,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticImageryFull,
        )

    def list(
        self,
        *,
        msg_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticImageryListResponse:
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
        return self._get(
            "/udl/analyticimagery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"msg_time": msg_time}, analytic_imagery_list_params.AnalyticImageryListParams),
            ),
            cast_to=AnalyticImageryListResponse,
        )

    def count(
        self,
        *,
        msg_time: Union[str, datetime],
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
                query=maybe_transform({"msg_time": msg_time}, analytic_imagery_count_params.AnalyticImageryCountParams),
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def history(
        self,
        *,
        msg_time: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
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
                    {"msg_time": msg_time}, analytic_imagery_history_count_params.AnalyticImageryHistoryCountParams
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/analyticimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        msg_time: Union[str, datetime],
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
                    },
                    analytic_imagery_tuple_params.AnalyticImageryTupleParams,
                ),
            ),
            cast_to=AnalyticImageryTupleResponse,
        )


class AsyncAnalyticImageryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticImageryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticImageryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticImageryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unifieddatalibrary-python#with_streaming_response
        """
        return AsyncAnalyticImageryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        content: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        description: str,
        filename: str,
        filesize: int,
        image_type: str,
        msg_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        agjson: str | NotGiven = NOT_GIVEN,
        andims: int | NotGiven = NOT_GIVEN,
        ann_lims: Iterable[Iterable[int]] | NotGiven = NOT_GIVEN,
        ann_text: List[str] | NotGiven = NOT_GIVEN,
        area: str | NotGiven = NOT_GIVEN,
        asrid: int | NotGiven = NOT_GIVEN,
        atext: str | NotGiven = NOT_GIVEN,
        atype: str | NotGiven = NOT_GIVEN,
        data_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        data_stop: Union[str, datetime] | NotGiven = NOT_GIVEN,
        image_set_id: str | NotGiven = NOT_GIVEN,
        image_set_length: int | NotGiven = NOT_GIVEN,
        img_height: int | NotGiven = NOT_GIVEN,
        img_width: int | NotGiven = NOT_GIVEN,
        keywords: List[str] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        sat_id: List[str] | NotGiven = NOT_GIVEN,
        sat_id_conf: Iterable[float] | NotGiven = NOT_GIVEN,
        sequence_id: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        x_units: str | NotGiven = NOT_GIVEN,
        y_units: str | NotGiven = NOT_GIVEN,
        z_units: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The analytic imagery service allows for contribution of general images, such as
        data plots, graphs, heatmaps, and other graphics not supported as UDL ground or
        sky imagery. This service operation requires a zip file in the body of the POST
        request. The zip file must contain exactly two files. <h3> 1) A json file with
        any file name that ends in .json e.g. MyFitsFile.json The contents of the json
        file must be valid according to the schema for Analytic Imagery. 2) A binary
        image file of the specified types allowed for AnalyticImagery. </h3> The
        metadata and image files will be stored and associated with each other allowing
        queries of the data retrieval of the binary images. This operation is intended
        to be used for automated feeds into UDL. A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          content: General type of content of this image (CONTOUR, DIAGRAM, HEATMAP, HISTOGRAM,
              PLOT, SCREENSHOT).

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          description: Description of the image content and utility.

          filename: The image file name.

          filesize: The image file size, in bytes. The maximum file size for this service is
              40,000,000 bytes (40MB). Files exceeding the maximum size will be rejected.

          image_type: The type of image associated with this record (GIF, JPG, PNG, TIF).

          msg_time: The message time of this image record, in ISO8601 UTC format with millisecond
              precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          agjson: Geographical region or polygon (lat/lon pairs), as depicted by the GeoJSON
              representation of the geometry/geography, of the image as projected on the
              ground. GeoJSON Reference: https://geojson.org/. Ignored if included with a POST
              or PUT request that also specifies a valid 'area' or 'atext' field.

          andims: Number of dimensions of the geometry depicted by region.

          ann_lims: Rectangular annotation limits, specified in pixels, as an array of arrays of the
              coordinates [ [UL1x, UL1y], [UR1x, UR1y], [LR1x, LR1y], [LL1x, LL1y] ],
              indicating the corners of a rectangle beginning with the Upper Left (UL) and
              moving clockwise. Allows the image provider to highlight one or more rectangular
              area(s) of interest. The array must contain Nx4 two-element arrays, where N is
              the number of rectangles of interest. The associated annotation(s) should be
              included in the annText array.

          ann_text: Annotation text, a string array of annotation(s) corresponding to the
              rectangular areas specified in annLims. This array contains the annotation text
              associated with the areas of interest indicated in annLims, in order. This array
              should contain one annotation per four values of the area (annLims) array.

          area: Optional geographical region or polygon (lat/lon pairs) of the area surrounding
              the point of interest as projected on the ground.

          asrid: Geographical spatial_ref_sys for region.

          atext: Geographical region or polygon (lon/lat pairs), as depicted by the Well-Known
              Text representation of the geometry/geography, of the image as projected on the
              ground. WKT reference: https://www.opengeospatial.org/standards/wkt-crs. Ignored
              if included with a POST or PUT request that also specifies a valid 'area' field.

          atype: Type of region as projected on the ground.

          data_start: The start time, in ISO8601 UTC format with millisecond precision, of the data
              used in the analysis or composition of the image content, when applicable.

          data_stop: The stop time, in ISO8601 UTC format with millisecond precision, of the data
              used in the analysis or composition of the image content, when applicable.

          image_set_id: User-defined set ID of a sequence of images. Used to associate related analytic
              image records.

          image_set_length: The number of images in an image set.

          img_height: The image height (vertical), in pixels.

          img_width: The image width (horizontal), in pixels.

          keywords: Array of searchable keywords for this analytic imagery record.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          sat_id: Assessed satellite ID (NORAD RSO object number). The 'satId' and 'satIdConf'
              arrays must match in size.

          sat_id_conf: Assessed satellite confidence corresponding to an assessment ID. Values are
              between 0.0 and 1.0. The 'satId' and 'satIdConf' arrays must match in size.

          sequence_id: The sequence number of an image within an image set. If null, then it is assumed
              that the order of images in an imageSet is not relevant.

          src_ids: Array of UUIDs of the UDL data records that are related to this image. See the
              associated 'srcTyps' array for the specific types of data, positionally
              corresponding to the UUIDs in this array. The 'srcTyps' and 'srcIds' arrays must
              match in size. See the corresponding srcTyps array element for the data type of
              the UUID and use the appropriate API operation to retrieve that object.

          src_typs: Array of UDL record types (AIS, CONJUNCTION, DOA, ELSET, EO, ESID, GROUNDIMAGE,
              POI, MANEUVER, MTI, NOTIFICATION, RADAR, RF, SIGACT, SKYIMAGE, SV, TRACK) that
              are related to this image. See the associated 'srcIds' array for the record
              UUIDs, positionally corresponding to the record types in this array. The
              'srcTyps' and 'srcIds' arrays must match in size.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          x_units: Optional field indicating the units that apply to the x-axis of the attached
              image, when applicable.

          y_units: Optional field indicating the units that apply to the y-axis of the attached
              image, when applicable.

          z_units: Optional field indicating the units that apply to the z-axis of the attached
              image, when applicable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-analyticimagery",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "content": content,
                    "data_mode": data_mode,
                    "description": description,
                    "filename": filename,
                    "filesize": filesize,
                    "image_type": image_type,
                    "msg_time": msg_time,
                    "source": source,
                    "id": id,
                    "agjson": agjson,
                    "andims": andims,
                    "ann_lims": ann_lims,
                    "ann_text": ann_text,
                    "area": area,
                    "asrid": asrid,
                    "atext": atext,
                    "atype": atype,
                    "data_start": data_start,
                    "data_stop": data_stop,
                    "image_set_id": image_set_id,
                    "image_set_length": image_set_length,
                    "img_height": img_height,
                    "img_width": img_width,
                    "keywords": keywords,
                    "origin": origin,
                    "sat_id": sat_id,
                    "sat_id_conf": sat_id_conf,
                    "sequence_id": sequence_id,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "x_units": x_units,
                    "y_units": y_units,
                    "z_units": z_units,
                },
                analytic_imagery_create_params.AnalyticImageryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        id: str,
        *,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalyticImageryFull,
        )

    async def list(
        self,
        *,
        msg_time: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyticImageryListResponse:
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
        return await self._get(
            "/udl/analyticimagery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"msg_time": msg_time}, analytic_imagery_list_params.AnalyticImageryListParams
                ),
            ),
            cast_to=AnalyticImageryListResponse,
        )

    async def count(
        self,
        *,
        msg_time: Union[str, datetime],
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
                    {"msg_time": msg_time}, analytic_imagery_count_params.AnalyticImageryCountParams
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def history(
        self,
        *,
        msg_time: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
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
                    {"msg_time": msg_time}, analytic_imagery_history_count_params.AnalyticImageryHistoryCountParams
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
            "/udl/analyticimagery/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        msg_time: Union[str, datetime],
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
                    },
                    analytic_imagery_tuple_params.AnalyticImageryTupleParams,
                ),
            ),
            cast_to=AnalyticImageryTupleResponse,
        )


class AnalyticImageryResourceWithRawResponse:
    def __init__(self, analytic_imagery: AnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.create = to_raw_response_wrapper(
            analytic_imagery.create,
        )
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


class AsyncAnalyticImageryResourceWithRawResponse:
    def __init__(self, analytic_imagery: AsyncAnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.create = async_to_raw_response_wrapper(
            analytic_imagery.create,
        )
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


class AnalyticImageryResourceWithStreamingResponse:
    def __init__(self, analytic_imagery: AnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.create = to_streamed_response_wrapper(
            analytic_imagery.create,
        )
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


class AsyncAnalyticImageryResourceWithStreamingResponse:
    def __init__(self, analytic_imagery: AsyncAnalyticImageryResource) -> None:
        self._analytic_imagery = analytic_imagery

        self.create = async_to_streamed_response_wrapper(
            analytic_imagery.create,
        )
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
