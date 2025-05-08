# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    airspace_control_order_list_params,
    airspace_control_order_count_params,
    airspace_control_order_tuple_params,
    airspace_control_order_create_params,
    airspace_control_order_retrieve_params,
    airspace_control_order_create_bulk_params,
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
from ..types.airspacecontrolorder_full import AirspacecontrolorderFull
from ..types.airspacecontrolorder_abridged import AirspacecontrolorderAbridged
from ..types.airspace_control_order_tuple_response import AirspaceControlOrderTupleResponse

__all__ = ["AirspaceControlOrdersResource", "AsyncAirspaceControlOrdersResource"]


class AirspaceControlOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AirspaceControlOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirspaceControlOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirspaceControlOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirspaceControlOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        op_ex_name: str,
        originator: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        aco_comments: str | NotGiven = NOT_GIVEN,
        aco_serial_num: str | NotGiven = NOT_GIVEN,
        airspace_control_means_status: Iterable[airspace_control_order_create_params.AirspaceControlMeansStatus]
        | NotGiven = NOT_GIVEN,
        airspace_control_order_references: Iterable[airspace_control_order_create_params.AirspaceControlOrderReference]
        | NotGiven = NOT_GIVEN,
        area_of_validity: str | NotGiven = NOT_GIVEN,
        class_reasons: List[str] | NotGiven = NOT_GIVEN,
        class_source: str | NotGiven = NOT_GIVEN,
        declass_exemption_codes: List[str] | NotGiven = NOT_GIVEN,
        downgrade_ins_dates: List[str] | NotGiven = NOT_GIVEN,
        geo_datum: str | NotGiven = NOT_GIVEN,
        month: str | NotGiven = NOT_GIVEN,
        op_ex_info: str | NotGiven = NOT_GIVEN,
        op_ex_info_alt: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        plan_orig_num: str | NotGiven = NOT_GIVEN,
        qualifier: str | NotGiven = NOT_GIVEN,
        qual_sn: int | NotGiven = NOT_GIVEN,
        serial_num: str | NotGiven = NOT_GIVEN,
        stop_qualifier: str | NotGiven = NOT_GIVEN,
        stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        und_lnk_trks: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single AirspaceControlOrder record as a POST body
        and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          op_ex_name: Specifies the unique operation or exercise name, nickname, or codeword assigned
              to a joint exercise or operation plan.

          originator: The identifier of the originator of this message.

          source: Source of the data.

          start_time: The start of the effective time period of this airspace control order, in ISO
              8601 UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          aco_comments: Free text information expressed in natural language.

          aco_serial_num: The serial number of this airspace control order.

          airspace_control_means_status: Mandatory nested segment to report multiple airspace control means statuses
              within an ACOID.

          airspace_control_order_references: The airspaceControlReferences set provides both USMTF and non-USMTF references
              for this airspace control order.

          area_of_validity: Name of the area of the command for which the ACO is valid.

          class_reasons: Mandatory if classSource uses the "IORIG" designator. Must be a REASON FOR
              CLASSIFICATION code.

          class_source: Markings defining the source material or the original classification authority
              for the ACO message.

          declass_exemption_codes: Coded entries that provide justification for exemption from automatic
              downgrading or declassification of the airspace control order.

          downgrade_ins_dates: Markings providing the literal guidance or date for downgrading or declassifying
              the airspace control order.

          geo_datum: Specifies the geodetic datum by which the spatial coordinates of the controlled
              airspace are calculated.

          month: The month in which the message originated.

          op_ex_info: Supplementary name that can be used to further identify exercise nicknames, or
              to provide the primary nickname of the option or the alternative of an
              operational plan.

          op_ex_info_alt: The secondary supplementary nickname of the option or the alternative of the
              operational plan or order.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          plan_orig_num: The official identifier of the military establishment responsible for the
              operation plan and the identification number assigned to this plan.

          qualifier: The qualifier which caveats the message status.

          qual_sn: The serial number associated with the message qualifier.

          serial_num: The unique message identifier sequentially assigned by the originator.

          stop_qualifier: A qualifier for the end of the effective time period of this airspace control
              order, such as AFTER, ASOF, NLT, etc. Used with field stopTime to indicate a
              relative time.

          stop_time: The end of the effective time period of this airspace control order, in ISO 8601
              UTC format with millisecond precision.

          und_lnk_trks: Array of unique link 16 identifiers that will be assigned to a future airspace
              control means.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airspacecontrolorder",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "op_ex_name": op_ex_name,
                    "originator": originator,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "aco_comments": aco_comments,
                    "aco_serial_num": aco_serial_num,
                    "airspace_control_means_status": airspace_control_means_status,
                    "airspace_control_order_references": airspace_control_order_references,
                    "area_of_validity": area_of_validity,
                    "class_reasons": class_reasons,
                    "class_source": class_source,
                    "declass_exemption_codes": declass_exemption_codes,
                    "downgrade_ins_dates": downgrade_ins_dates,
                    "geo_datum": geo_datum,
                    "month": month,
                    "op_ex_info": op_ex_info,
                    "op_ex_info_alt": op_ex_info_alt,
                    "origin": origin,
                    "plan_orig_num": plan_orig_num,
                    "qualifier": qualifier,
                    "qual_sn": qual_sn,
                    "serial_num": serial_num,
                    "stop_qualifier": stop_qualifier,
                    "stop_time": stop_time,
                    "und_lnk_trks": und_lnk_trks,
                },
                airspace_control_order_create_params.AirspaceControlOrderCreateParams,
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
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirspacecontrolorderFull:
        """
        Service operation to get a single AirspaceControlOrder record by its unique ID
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
            f"/udl/airspacecontrolorder/{id}",
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
                    airspace_control_order_retrieve_params.AirspaceControlOrderRetrieveParams,
                ),
            ),
            cast_to=AirspacecontrolorderFull,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[AirspacecontrolorderAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/airspacecontrolorder",
            page=SyncOffsetPage[AirspacecontrolorderAbridged],
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
                    airspace_control_order_list_params.AirspaceControlOrderListParams,
                ),
            ),
            model=AirspacecontrolorderAbridged,
        )

    def count(
        self,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/airspacecontrolorder/count",
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
                    airspace_control_order_count_params.AirspaceControlOrderCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[airspace_control_order_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        AirspaceControlOrder records as a POST body and ingest into the database. This
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
            "/udl/airspacecontrolorder/createBulk",
            body=maybe_transform(body, Iterable[airspace_control_order_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/airspacecontrolorder/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirspaceControlOrderTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/airspacecontrolorder/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airspace_control_order_tuple_params.AirspaceControlOrderTupleParams,
                ),
            ),
            cast_to=AirspaceControlOrderTupleResponse,
        )


class AsyncAirspaceControlOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAirspaceControlOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirspaceControlOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirspaceControlOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirspaceControlOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        op_ex_name: str,
        originator: str,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        aco_comments: str | NotGiven = NOT_GIVEN,
        aco_serial_num: str | NotGiven = NOT_GIVEN,
        airspace_control_means_status: Iterable[airspace_control_order_create_params.AirspaceControlMeansStatus]
        | NotGiven = NOT_GIVEN,
        airspace_control_order_references: Iterable[airspace_control_order_create_params.AirspaceControlOrderReference]
        | NotGiven = NOT_GIVEN,
        area_of_validity: str | NotGiven = NOT_GIVEN,
        class_reasons: List[str] | NotGiven = NOT_GIVEN,
        class_source: str | NotGiven = NOT_GIVEN,
        declass_exemption_codes: List[str] | NotGiven = NOT_GIVEN,
        downgrade_ins_dates: List[str] | NotGiven = NOT_GIVEN,
        geo_datum: str | NotGiven = NOT_GIVEN,
        month: str | NotGiven = NOT_GIVEN,
        op_ex_info: str | NotGiven = NOT_GIVEN,
        op_ex_info_alt: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        plan_orig_num: str | NotGiven = NOT_GIVEN,
        qualifier: str | NotGiven = NOT_GIVEN,
        qual_sn: int | NotGiven = NOT_GIVEN,
        serial_num: str | NotGiven = NOT_GIVEN,
        stop_qualifier: str | NotGiven = NOT_GIVEN,
        stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        und_lnk_trks: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single AirspaceControlOrder record as a POST body
        and ingest into the database. A specific role is required to perform this
        service operation. Please contact the UDL team for assistance.

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

          op_ex_name: Specifies the unique operation or exercise name, nickname, or codeword assigned
              to a joint exercise or operation plan.

          originator: The identifier of the originator of this message.

          source: Source of the data.

          start_time: The start of the effective time period of this airspace control order, in ISO
              8601 UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system.

          aco_comments: Free text information expressed in natural language.

          aco_serial_num: The serial number of this airspace control order.

          airspace_control_means_status: Mandatory nested segment to report multiple airspace control means statuses
              within an ACOID.

          airspace_control_order_references: The airspaceControlReferences set provides both USMTF and non-USMTF references
              for this airspace control order.

          area_of_validity: Name of the area of the command for which the ACO is valid.

          class_reasons: Mandatory if classSource uses the "IORIG" designator. Must be a REASON FOR
              CLASSIFICATION code.

          class_source: Markings defining the source material or the original classification authority
              for the ACO message.

          declass_exemption_codes: Coded entries that provide justification for exemption from automatic
              downgrading or declassification of the airspace control order.

          downgrade_ins_dates: Markings providing the literal guidance or date for downgrading or declassifying
              the airspace control order.

          geo_datum: Specifies the geodetic datum by which the spatial coordinates of the controlled
              airspace are calculated.

          month: The month in which the message originated.

          op_ex_info: Supplementary name that can be used to further identify exercise nicknames, or
              to provide the primary nickname of the option or the alternative of an
              operational plan.

          op_ex_info_alt: The secondary supplementary nickname of the option or the alternative of the
              operational plan or order.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          plan_orig_num: The official identifier of the military establishment responsible for the
              operation plan and the identification number assigned to this plan.

          qualifier: The qualifier which caveats the message status.

          qual_sn: The serial number associated with the message qualifier.

          serial_num: The unique message identifier sequentially assigned by the originator.

          stop_qualifier: A qualifier for the end of the effective time period of this airspace control
              order, such as AFTER, ASOF, NLT, etc. Used with field stopTime to indicate a
              relative time.

          stop_time: The end of the effective time period of this airspace control order, in ISO 8601
              UTC format with millisecond precision.

          und_lnk_trks: Array of unique link 16 identifiers that will be assigned to a future airspace
              control means.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airspacecontrolorder",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "op_ex_name": op_ex_name,
                    "originator": originator,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "aco_comments": aco_comments,
                    "aco_serial_num": aco_serial_num,
                    "airspace_control_means_status": airspace_control_means_status,
                    "airspace_control_order_references": airspace_control_order_references,
                    "area_of_validity": area_of_validity,
                    "class_reasons": class_reasons,
                    "class_source": class_source,
                    "declass_exemption_codes": declass_exemption_codes,
                    "downgrade_ins_dates": downgrade_ins_dates,
                    "geo_datum": geo_datum,
                    "month": month,
                    "op_ex_info": op_ex_info,
                    "op_ex_info_alt": op_ex_info_alt,
                    "origin": origin,
                    "plan_orig_num": plan_orig_num,
                    "qualifier": qualifier,
                    "qual_sn": qual_sn,
                    "serial_num": serial_num,
                    "stop_qualifier": stop_qualifier,
                    "stop_time": stop_time,
                    "und_lnk_trks": und_lnk_trks,
                },
                airspace_control_order_create_params.AirspaceControlOrderCreateParams,
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
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirspacecontrolorderFull:
        """
        Service operation to get a single AirspaceControlOrder record by its unique ID
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
            f"/udl/airspacecontrolorder/{id}",
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
                    airspace_control_order_retrieve_params.AirspaceControlOrderRetrieveParams,
                ),
            ),
            cast_to=AirspacecontrolorderFull,
        )

    def list(
        self,
        *,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AirspacecontrolorderAbridged, AsyncOffsetPage[AirspacecontrolorderAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/airspacecontrolorder",
            page=AsyncOffsetPage[AirspacecontrolorderAbridged],
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
                    airspace_control_order_list_params.AirspaceControlOrderListParams,
                ),
            ),
            model=AirspacecontrolorderAbridged,
        )

    async def count(
        self,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/airspacecontrolorder/count",
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
                    airspace_control_order_count_params.AirspaceControlOrderCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[airspace_control_order_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        AirspaceControlOrder records as a POST body and ingest into the database. This
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
            "/udl/airspacecontrolorder/createBulk",
            body=await async_maybe_transform(body, Iterable[airspace_control_order_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/airspacecontrolorder/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirspaceControlOrderTupleResponse:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/airspacecontrolorder/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airspace_control_order_tuple_params.AirspaceControlOrderTupleParams,
                ),
            ),
            cast_to=AirspaceControlOrderTupleResponse,
        )


class AirspaceControlOrdersResourceWithRawResponse:
    def __init__(self, airspace_control_orders: AirspaceControlOrdersResource) -> None:
        self._airspace_control_orders = airspace_control_orders

        self.create = to_raw_response_wrapper(
            airspace_control_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            airspace_control_orders.retrieve,
        )
        self.list = to_raw_response_wrapper(
            airspace_control_orders.list,
        )
        self.count = to_raw_response_wrapper(
            airspace_control_orders.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            airspace_control_orders.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            airspace_control_orders.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            airspace_control_orders.tuple,
        )


class AsyncAirspaceControlOrdersResourceWithRawResponse:
    def __init__(self, airspace_control_orders: AsyncAirspaceControlOrdersResource) -> None:
        self._airspace_control_orders = airspace_control_orders

        self.create = async_to_raw_response_wrapper(
            airspace_control_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            airspace_control_orders.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            airspace_control_orders.list,
        )
        self.count = async_to_raw_response_wrapper(
            airspace_control_orders.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            airspace_control_orders.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            airspace_control_orders.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            airspace_control_orders.tuple,
        )


class AirspaceControlOrdersResourceWithStreamingResponse:
    def __init__(self, airspace_control_orders: AirspaceControlOrdersResource) -> None:
        self._airspace_control_orders = airspace_control_orders

        self.create = to_streamed_response_wrapper(
            airspace_control_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            airspace_control_orders.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            airspace_control_orders.list,
        )
        self.count = to_streamed_response_wrapper(
            airspace_control_orders.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            airspace_control_orders.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            airspace_control_orders.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            airspace_control_orders.tuple,
        )


class AsyncAirspaceControlOrdersResourceWithStreamingResponse:
    def __init__(self, airspace_control_orders: AsyncAirspaceControlOrdersResource) -> None:
        self._airspace_control_orders = airspace_control_orders

        self.create = async_to_streamed_response_wrapper(
            airspace_control_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            airspace_control_orders.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            airspace_control_orders.list,
        )
        self.count = async_to_streamed_response_wrapper(
            airspace_control_orders.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            airspace_control_orders.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            airspace_control_orders.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            airspace_control_orders.tuple,
        )
