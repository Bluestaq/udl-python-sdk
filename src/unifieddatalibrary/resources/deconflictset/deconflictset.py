# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    deconflictset_get_params,
    deconflictset_list_params,
    deconflictset_count_params,
    deconflictset_tuple_params,
    deconflictset_create_params,
    deconflictset_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.deconflictset_get_response import DeconflictsetGetResponse
from ...types.deconflictset_list_response import DeconflictsetListResponse
from ...types.deconflictset_tuple_response import DeconflictsetTupleResponse
from ...types.deconflictset_queryhelp_response import DeconflictsetQueryhelpResponse

__all__ = ["DeconflictsetResource", "AsyncDeconflictsetResource"]


class DeconflictsetResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeconflictsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DeconflictsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeconflictsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DeconflictsetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        num_windows: int,
        source: str,
        id: str | Omit = omit,
        calculation_end_time: Union[str, datetime] | Omit = omit,
        calculation_id: str | Omit = omit,
        calculation_start_time: Union[str, datetime] | Omit = omit,
        deconflict_windows: Iterable[deconflictset_create_params.DeconflictWindow] | Omit = omit,
        errors: SequenceNotStr[str] | Omit = omit,
        event_end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        id_laser_deconflict_request: str | Omit = omit,
        origin: str | Omit = omit,
        reference_frame: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        warnings: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single DeconflictSet record as a POST body and
        ingest into the database. This operation does not persist any DeconflictWindow
        datatypes that may be present in the body of the request. This operation is not
        intended to be used for automated feeds into UDL. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          num_windows: The number of windows provided by this DeconflictSet record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          calculation_end_time: The time at which the window calculations completed, in ISO 8601 UTC format with
              millisecond precision.

          calculation_id: The algorithm execution id associated with the generation of this DeconflictSet.

          calculation_start_time: The time at which the window calculations started, in ISO 8601 UTC format with
              millisecond precision.

          deconflict_windows: Array of DeconflictWindow records associated with this DeconflictSet.

          errors: Array of error messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          event_end_time: The end time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          event_type: The type of event associated with this DeconflictSet record.

          id_laser_deconflict_request: The id of the LaserDeconflictRequest record used as input in the generation of
              this DeconflictSet, if applicable.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          warnings: Array of warning messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/deconflictset",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "num_windows": num_windows,
                    "source": source,
                    "id": id,
                    "calculation_end_time": calculation_end_time,
                    "calculation_id": calculation_id,
                    "calculation_start_time": calculation_start_time,
                    "deconflict_windows": deconflict_windows,
                    "errors": errors,
                    "event_end_time": event_end_time,
                    "event_type": event_type,
                    "id_laser_deconflict_request": id_laser_deconflict_request,
                    "origin": origin,
                    "reference_frame": reference_frame,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "warnings": warnings,
                },
                deconflictset_create_params.DeconflictsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[DeconflictsetListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/deconflictset",
            page=SyncOffsetPage[DeconflictsetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    deconflictset_list_params.DeconflictsetListParams,
                ),
            ),
            model=DeconflictsetListResponse,
        )

    def count(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/deconflictset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    deconflictset_count_params.DeconflictsetCountParams,
                ),
            ),
            cast_to=str,
        )

    def get(
        self,
        id: str,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeconflictsetGetResponse:
        """
        Service operation to get a single DeconflictSet record by its unique ID passed
        as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/deconflictset/{id}",
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
                    deconflictset_get_params.DeconflictsetGetParams,
                ),
            ),
            cast_to=DeconflictsetGetResponse,
        )

    def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeconflictsetQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/deconflictset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeconflictsetQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeconflictsetTupleResponse:
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

          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/deconflictset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    deconflictset_tuple_params.DeconflictsetTupleParams,
                ),
            ),
            cast_to=DeconflictsetTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        num_windows: int,
        source: str,
        id: str | Omit = omit,
        calculation_end_time: Union[str, datetime] | Omit = omit,
        calculation_id: str | Omit = omit,
        calculation_start_time: Union[str, datetime] | Omit = omit,
        deconflict_windows: Iterable[deconflictset_unvalidated_publish_params.DeconflictWindow] | Omit = omit,
        errors: SequenceNotStr[str] | Omit = omit,
        event_end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        id_laser_deconflict_request: str | Omit = omit,
        origin: str | Omit = omit,
        reference_frame: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        warnings: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single DeconflictSet record as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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

          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          num_windows: The number of windows provided by this DeconflictSet record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          calculation_end_time: The time at which the window calculations completed, in ISO 8601 UTC format with
              millisecond precision.

          calculation_id: The algorithm execution id associated with the generation of this DeconflictSet.

          calculation_start_time: The time at which the window calculations started, in ISO 8601 UTC format with
              millisecond precision.

          deconflict_windows: Array of DeconflictWindow records associated with this DeconflictSet.

          errors: Array of error messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          event_end_time: The end time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          event_type: The type of event associated with this DeconflictSet record.

          id_laser_deconflict_request: The id of the LaserDeconflictRequest record used as input in the generation of
              this DeconflictSet, if applicable.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          warnings: Array of warning messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-deconflictset",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "num_windows": num_windows,
                    "source": source,
                    "id": id,
                    "calculation_end_time": calculation_end_time,
                    "calculation_id": calculation_id,
                    "calculation_start_time": calculation_start_time,
                    "deconflict_windows": deconflict_windows,
                    "errors": errors,
                    "event_end_time": event_end_time,
                    "event_type": event_type,
                    "id_laser_deconflict_request": id_laser_deconflict_request,
                    "origin": origin,
                    "reference_frame": reference_frame,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "warnings": warnings,
                },
                deconflictset_unvalidated_publish_params.DeconflictsetUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDeconflictsetResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeconflictsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDeconflictsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeconflictsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDeconflictsetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        num_windows: int,
        source: str,
        id: str | Omit = omit,
        calculation_end_time: Union[str, datetime] | Omit = omit,
        calculation_id: str | Omit = omit,
        calculation_start_time: Union[str, datetime] | Omit = omit,
        deconflict_windows: Iterable[deconflictset_create_params.DeconflictWindow] | Omit = omit,
        errors: SequenceNotStr[str] | Omit = omit,
        event_end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        id_laser_deconflict_request: str | Omit = omit,
        origin: str | Omit = omit,
        reference_frame: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        warnings: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single DeconflictSet record as a POST body and
        ingest into the database. This operation does not persist any DeconflictWindow
        datatypes that may be present in the body of the request. This operation is not
        intended to be used for automated feeds into UDL. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          num_windows: The number of windows provided by this DeconflictSet record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          calculation_end_time: The time at which the window calculations completed, in ISO 8601 UTC format with
              millisecond precision.

          calculation_id: The algorithm execution id associated with the generation of this DeconflictSet.

          calculation_start_time: The time at which the window calculations started, in ISO 8601 UTC format with
              millisecond precision.

          deconflict_windows: Array of DeconflictWindow records associated with this DeconflictSet.

          errors: Array of error messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          event_end_time: The end time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          event_type: The type of event associated with this DeconflictSet record.

          id_laser_deconflict_request: The id of the LaserDeconflictRequest record used as input in the generation of
              this DeconflictSet, if applicable.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          warnings: Array of warning messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/deconflictset",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "num_windows": num_windows,
                    "source": source,
                    "id": id,
                    "calculation_end_time": calculation_end_time,
                    "calculation_id": calculation_id,
                    "calculation_start_time": calculation_start_time,
                    "deconflict_windows": deconflict_windows,
                    "errors": errors,
                    "event_end_time": event_end_time,
                    "event_type": event_type,
                    "id_laser_deconflict_request": id_laser_deconflict_request,
                    "origin": origin,
                    "reference_frame": reference_frame,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "warnings": warnings,
                },
                deconflictset_create_params.DeconflictsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DeconflictsetListResponse, AsyncOffsetPage[DeconflictsetListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/deconflictset",
            page=AsyncOffsetPage[DeconflictsetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    deconflictset_list_params.DeconflictsetListParams,
                ),
            ),
            model=DeconflictsetListResponse,
        )

    async def count(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/deconflictset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    deconflictset_count_params.DeconflictsetCountParams,
                ),
            ),
            cast_to=str,
        )

    async def get(
        self,
        id: str,
        *,
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeconflictsetGetResponse:
        """
        Service operation to get a single DeconflictSet record by its unique ID passed
        as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/deconflictset/{id}",
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
                    deconflictset_get_params.DeconflictsetGetParams,
                ),
            ),
            cast_to=DeconflictsetGetResponse,
        )

    async def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeconflictsetQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/deconflictset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeconflictsetQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeconflictsetTupleResponse:
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

          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/deconflictset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    deconflictset_tuple_params.DeconflictsetTupleParams,
                ),
            ),
            cast_to=DeconflictsetTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        num_windows: int,
        source: str,
        id: str | Omit = omit,
        calculation_end_time: Union[str, datetime] | Omit = omit,
        calculation_id: str | Omit = omit,
        calculation_start_time: Union[str, datetime] | Omit = omit,
        deconflict_windows: Iterable[deconflictset_unvalidated_publish_params.DeconflictWindow] | Omit = omit,
        errors: SequenceNotStr[str] | Omit = omit,
        event_end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        id_laser_deconflict_request: str | Omit = omit,
        origin: str | Omit = omit,
        reference_frame: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transaction_id: str | Omit = omit,
        warnings: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single DeconflictSet record as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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

          event_start_time: The start time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          num_windows: The number of windows provided by this DeconflictSet record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          calculation_end_time: The time at which the window calculations completed, in ISO 8601 UTC format with
              millisecond precision.

          calculation_id: The algorithm execution id associated with the generation of this DeconflictSet.

          calculation_start_time: The time at which the window calculations started, in ISO 8601 UTC format with
              millisecond precision.

          deconflict_windows: Array of DeconflictWindow records associated with this DeconflictSet.

          errors: Array of error messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          event_end_time: The end time of the event associated with the set of DeconflictWindow records,
              in ISO 8601 UTC format with millisecond precision.

          event_type: The type of event associated with this DeconflictSet record.

          id_laser_deconflict_request: The id of the LaserDeconflictRequest record used as input in the generation of
              this DeconflictSet, if applicable.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          reference_frame: The reference frame of the cartesian orbital states. If the referenceFrame is
              null it is assumed to be J2000.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          warnings: Array of warning messages that potentially contain information about the reasons
              this deconflict response calculation may be inaccurate, or why it failed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-deconflictset",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "num_windows": num_windows,
                    "source": source,
                    "id": id,
                    "calculation_end_time": calculation_end_time,
                    "calculation_id": calculation_id,
                    "calculation_start_time": calculation_start_time,
                    "deconflict_windows": deconflict_windows,
                    "errors": errors,
                    "event_end_time": event_end_time,
                    "event_type": event_type,
                    "id_laser_deconflict_request": id_laser_deconflict_request,
                    "origin": origin,
                    "reference_frame": reference_frame,
                    "tags": tags,
                    "transaction_id": transaction_id,
                    "warnings": warnings,
                },
                deconflictset_unvalidated_publish_params.DeconflictsetUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DeconflictsetResourceWithRawResponse:
    def __init__(self, deconflictset: DeconflictsetResource) -> None:
        self._deconflictset = deconflictset

        self.create = to_raw_response_wrapper(
            deconflictset.create,
        )
        self.list = to_raw_response_wrapper(
            deconflictset.list,
        )
        self.count = to_raw_response_wrapper(
            deconflictset.count,
        )
        self.get = to_raw_response_wrapper(
            deconflictset.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            deconflictset.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            deconflictset.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            deconflictset.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._deconflictset.history)


class AsyncDeconflictsetResourceWithRawResponse:
    def __init__(self, deconflictset: AsyncDeconflictsetResource) -> None:
        self._deconflictset = deconflictset

        self.create = async_to_raw_response_wrapper(
            deconflictset.create,
        )
        self.list = async_to_raw_response_wrapper(
            deconflictset.list,
        )
        self.count = async_to_raw_response_wrapper(
            deconflictset.count,
        )
        self.get = async_to_raw_response_wrapper(
            deconflictset.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            deconflictset.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            deconflictset.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            deconflictset.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._deconflictset.history)


class DeconflictsetResourceWithStreamingResponse:
    def __init__(self, deconflictset: DeconflictsetResource) -> None:
        self._deconflictset = deconflictset

        self.create = to_streamed_response_wrapper(
            deconflictset.create,
        )
        self.list = to_streamed_response_wrapper(
            deconflictset.list,
        )
        self.count = to_streamed_response_wrapper(
            deconflictset.count,
        )
        self.get = to_streamed_response_wrapper(
            deconflictset.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            deconflictset.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            deconflictset.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            deconflictset.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._deconflictset.history)


class AsyncDeconflictsetResourceWithStreamingResponse:
    def __init__(self, deconflictset: AsyncDeconflictsetResource) -> None:
        self._deconflictset = deconflictset

        self.create = async_to_streamed_response_wrapper(
            deconflictset.create,
        )
        self.list = async_to_streamed_response_wrapper(
            deconflictset.list,
        )
        self.count = async_to_streamed_response_wrapper(
            deconflictset.count,
        )
        self.get = async_to_streamed_response_wrapper(
            deconflictset.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            deconflictset.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            deconflictset.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            deconflictset.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._deconflictset.history)
