# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    logistics_support_get_params,
    logistics_support_list_params,
    logistics_support_count_params,
    logistics_support_tuple_params,
    logistics_support_create_params,
    logistics_support_update_params,
    logistics_support_create_bulk_params,
    logistics_support_unvalidated_publish_params,
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
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.logistics_support_get_response import LogisticsSupportGetResponse
from ...types.logistics_support_list_response import LogisticsSupportListResponse
from ...types.logistics_support_tuple_response import LogisticsSupportTupleResponse

__all__ = ["LogisticsSupportResource", "AsyncLogisticsSupportResource"]


class LogisticsSupportResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> LogisticsSupportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LogisticsSupportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogisticsSupportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return LogisticsSupportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        rpt_created_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        curr_icao: str | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etmc: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ext_system_id: str | NotGiven = NOT_GIVEN,
        logistic_action: str | NotGiven = NOT_GIVEN,
        logistics_discrepancy_infos: Iterable[logistics_support_create_params.LogisticsDiscrepancyInfo]
        | NotGiven = NOT_GIVEN,
        logistics_record_id: str | NotGiven = NOT_GIVEN,
        logistics_remarks: Iterable[logistics_support_create_params.LogisticsRemark] | NotGiven = NOT_GIVEN,
        logistics_support_items: Iterable[logistics_support_create_params.LogisticsSupportItem] | NotGiven = NOT_GIVEN,
        logistics_transportation_plans: Iterable[logistics_support_create_params.LogisticsTransportationPlan]
        | NotGiven = NOT_GIVEN,
        maint_status_code: str | NotGiven = NOT_GIVEN,
        mc_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        me_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        reopen_flag: bool | NotGiven = NOT_GIVEN,
        rpt_closed_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        supp_icao: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single LogisticsSupport record as a POST body and
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

          rpt_created_time: The time this report was created, in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as, but not constrained
              to, MIL-STD-6016 environment dependent specific type designations.

          curr_icao: The current ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          etic: The estimated time mission capable for the aircraft, in ISO 8601 UCT format with
              millisecond precision. This is the estimated time when the aircraft is mission
              ready.

          etmc: Logistics estimated time mission capable.

          ext_system_id: Optional system identifier from external systs. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          logistic_action: This field identifies the pacing event for bringing the aircraft to Mission
              Capable status. It is used in calculating the Estimated Time Mission Capable
              (ETMC) value. Acceptable values are WA (Will Advise), INW (In Work), P+hhh.h
              (where P=parts and hhh.h is the number of hours up to 999 plus tenths of hours),
              EQ+hhh.h (EQ=equipment), MRT+hhh.h (MRT=maintenance recovery team).

          logistics_discrepancy_infos: Discrepancy information associated with this LogisticsSupport record.

          logistics_record_id: The identifier that represents a Logistics Master Record.

          logistics_remarks: Remarks associated with this LogisticsSupport record.

          logistics_support_items: Support items associated with this LogisticsSupport record.

          logistics_transportation_plans: Transportation plans associated with this LogisticsSupport record, used to
              coordinate maintenance efforts.

          maint_status_code: The maintenance status code of the aircraft which may be based on pilot
              descriptions or evaluation codes. Contact the source provider for details.

          mc_time: The time indicating when all mission essential problems with a given aircraft
              have been fixed and is mission capable. This datetime should be in ISO 8601 UTC
              format with millisecond precision.

          me_time: The time indicating when a given aircraft breaks for a mission essential reason.
              This datetime should be in ISO 8601 UTC format with millisecond precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: The organization that owns this logistics record.

          reopen_flag: This is used to indicate whether a closed master record has been reopened.

          rpt_closed_time: The time this report was closed, in ISO 8601 UTC format with millisecond
              precision.

          supp_icao: The supplying ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          tail_number: The tail number of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/logisticssupport",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "rpt_created_time": rpt_created_time,
                    "source": source,
                    "id": id,
                    "aircraft_mds": aircraft_mds,
                    "curr_icao": curr_icao,
                    "etic": etic,
                    "etmc": etmc,
                    "ext_system_id": ext_system_id,
                    "logistic_action": logistic_action,
                    "logistics_discrepancy_infos": logistics_discrepancy_infos,
                    "logistics_record_id": logistics_record_id,
                    "logistics_remarks": logistics_remarks,
                    "logistics_support_items": logistics_support_items,
                    "logistics_transportation_plans": logistics_transportation_plans,
                    "maint_status_code": maint_status_code,
                    "mc_time": mc_time,
                    "me_time": me_time,
                    "origin": origin,
                    "owner": owner,
                    "reopen_flag": reopen_flag,
                    "rpt_closed_time": rpt_closed_time,
                    "supp_icao": supp_icao,
                    "tail_number": tail_number,
                },
                logistics_support_create_params.LogisticsSupportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        rpt_created_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        curr_icao: str | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etmc: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ext_system_id: str | NotGiven = NOT_GIVEN,
        logistic_action: str | NotGiven = NOT_GIVEN,
        logistics_discrepancy_infos: Iterable[logistics_support_update_params.LogisticsDiscrepancyInfo]
        | NotGiven = NOT_GIVEN,
        logistics_record_id: str | NotGiven = NOT_GIVEN,
        logistics_remarks: Iterable[logistics_support_update_params.LogisticsRemark] | NotGiven = NOT_GIVEN,
        logistics_support_items: Iterable[logistics_support_update_params.LogisticsSupportItem] | NotGiven = NOT_GIVEN,
        logistics_transportation_plans: Iterable[logistics_support_update_params.LogisticsTransportationPlan]
        | NotGiven = NOT_GIVEN,
        maint_status_code: str | NotGiven = NOT_GIVEN,
        mc_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        me_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        reopen_flag: bool | NotGiven = NOT_GIVEN,
        rpt_closed_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        supp_icao: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single LogisticsSupport record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

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

          rpt_created_time: The time this report was created, in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as, but not constrained
              to, MIL-STD-6016 environment dependent specific type designations.

          curr_icao: The current ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          etic: The estimated time mission capable for the aircraft, in ISO 8601 UCT format with
              millisecond precision. This is the estimated time when the aircraft is mission
              ready.

          etmc: Logistics estimated time mission capable.

          ext_system_id: Optional system identifier from external systs. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          logistic_action: This field identifies the pacing event for bringing the aircraft to Mission
              Capable status. It is used in calculating the Estimated Time Mission Capable
              (ETMC) value. Acceptable values are WA (Will Advise), INW (In Work), P+hhh.h
              (where P=parts and hhh.h is the number of hours up to 999 plus tenths of hours),
              EQ+hhh.h (EQ=equipment), MRT+hhh.h (MRT=maintenance recovery team).

          logistics_discrepancy_infos: Discrepancy information associated with this LogisticsSupport record.

          logistics_record_id: The identifier that represents a Logistics Master Record.

          logistics_remarks: Remarks associated with this LogisticsSupport record.

          logistics_support_items: Support items associated with this LogisticsSupport record.

          logistics_transportation_plans: Transportation plans associated with this LogisticsSupport record, used to
              coordinate maintenance efforts.

          maint_status_code: The maintenance status code of the aircraft which may be based on pilot
              descriptions or evaluation codes. Contact the source provider for details.

          mc_time: The time indicating when all mission essential problems with a given aircraft
              have been fixed and is mission capable. This datetime should be in ISO 8601 UTC
              format with millisecond precision.

          me_time: The time indicating when a given aircraft breaks for a mission essential reason.
              This datetime should be in ISO 8601 UTC format with millisecond precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: The organization that owns this logistics record.

          reopen_flag: This is used to indicate whether a closed master record has been reopened.

          rpt_closed_time: The time this report was closed, in ISO 8601 UTC format with millisecond
              precision.

          supp_icao: The supplying ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          tail_number: The tail number of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/logisticssupport/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "rpt_created_time": rpt_created_time,
                    "source": source,
                    "body_id": body_id,
                    "aircraft_mds": aircraft_mds,
                    "curr_icao": curr_icao,
                    "etic": etic,
                    "etmc": etmc,
                    "ext_system_id": ext_system_id,
                    "logistic_action": logistic_action,
                    "logistics_discrepancy_infos": logistics_discrepancy_infos,
                    "logistics_record_id": logistics_record_id,
                    "logistics_remarks": logistics_remarks,
                    "logistics_support_items": logistics_support_items,
                    "logistics_transportation_plans": logistics_transportation_plans,
                    "maint_status_code": maint_status_code,
                    "mc_time": mc_time,
                    "me_time": me_time,
                    "origin": origin,
                    "owner": owner,
                    "reopen_flag": reopen_flag,
                    "rpt_closed_time": rpt_closed_time,
                    "supp_icao": supp_icao,
                    "tail_number": tail_number,
                },
                logistics_support_update_params.LogisticsSupportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SyncOffsetPage[LogisticsSupportListResponse]:
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
            "/udl/logisticssupport",
            page=SyncOffsetPage[LogisticsSupportListResponse],
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
                    logistics_support_list_params.LogisticsSupportListParams,
                ),
            ),
            model=LogisticsSupportListResponse,
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
            "/udl/logisticssupport/count",
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
                    logistics_support_count_params.LogisticsSupportCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[logistics_support_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        LogisticsSupport records as a POST body and ingest into the database. This
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
            "/udl/logisticssupport/createBulk",
            body=maybe_transform(body, Iterable[logistics_support_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> LogisticsSupportGetResponse:
        """
        Service operation to get a single LogisticsSupport record by its unique ID
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
            f"/udl/logisticssupport/{id}",
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
                    logistics_support_get_params.LogisticsSupportGetParams,
                ),
            ),
            cast_to=LogisticsSupportGetResponse,
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
            "/udl/logisticssupport/queryhelp",
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
    ) -> LogisticsSupportTupleResponse:
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
            "/udl/logisticssupport/tuple",
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
                    logistics_support_tuple_params.LogisticsSupportTupleParams,
                ),
            ),
            cast_to=LogisticsSupportTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[logistics_support_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple logisticssupport records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-logisticssupport",
            body=maybe_transform(body, Iterable[logistics_support_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLogisticsSupportResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogisticsSupportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLogisticsSupportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogisticsSupportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncLogisticsSupportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        rpt_created_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        curr_icao: str | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etmc: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ext_system_id: str | NotGiven = NOT_GIVEN,
        logistic_action: str | NotGiven = NOT_GIVEN,
        logistics_discrepancy_infos: Iterable[logistics_support_create_params.LogisticsDiscrepancyInfo]
        | NotGiven = NOT_GIVEN,
        logistics_record_id: str | NotGiven = NOT_GIVEN,
        logistics_remarks: Iterable[logistics_support_create_params.LogisticsRemark] | NotGiven = NOT_GIVEN,
        logistics_support_items: Iterable[logistics_support_create_params.LogisticsSupportItem] | NotGiven = NOT_GIVEN,
        logistics_transportation_plans: Iterable[logistics_support_create_params.LogisticsTransportationPlan]
        | NotGiven = NOT_GIVEN,
        maint_status_code: str | NotGiven = NOT_GIVEN,
        mc_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        me_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        reopen_flag: bool | NotGiven = NOT_GIVEN,
        rpt_closed_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        supp_icao: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single LogisticsSupport record as a POST body and
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

          rpt_created_time: The time this report was created, in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as, but not constrained
              to, MIL-STD-6016 environment dependent specific type designations.

          curr_icao: The current ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          etic: The estimated time mission capable for the aircraft, in ISO 8601 UCT format with
              millisecond precision. This is the estimated time when the aircraft is mission
              ready.

          etmc: Logistics estimated time mission capable.

          ext_system_id: Optional system identifier from external systs. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          logistic_action: This field identifies the pacing event for bringing the aircraft to Mission
              Capable status. It is used in calculating the Estimated Time Mission Capable
              (ETMC) value. Acceptable values are WA (Will Advise), INW (In Work), P+hhh.h
              (where P=parts and hhh.h is the number of hours up to 999 plus tenths of hours),
              EQ+hhh.h (EQ=equipment), MRT+hhh.h (MRT=maintenance recovery team).

          logistics_discrepancy_infos: Discrepancy information associated with this LogisticsSupport record.

          logistics_record_id: The identifier that represents a Logistics Master Record.

          logistics_remarks: Remarks associated with this LogisticsSupport record.

          logistics_support_items: Support items associated with this LogisticsSupport record.

          logistics_transportation_plans: Transportation plans associated with this LogisticsSupport record, used to
              coordinate maintenance efforts.

          maint_status_code: The maintenance status code of the aircraft which may be based on pilot
              descriptions or evaluation codes. Contact the source provider for details.

          mc_time: The time indicating when all mission essential problems with a given aircraft
              have been fixed and is mission capable. This datetime should be in ISO 8601 UTC
              format with millisecond precision.

          me_time: The time indicating when a given aircraft breaks for a mission essential reason.
              This datetime should be in ISO 8601 UTC format with millisecond precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: The organization that owns this logistics record.

          reopen_flag: This is used to indicate whether a closed master record has been reopened.

          rpt_closed_time: The time this report was closed, in ISO 8601 UTC format with millisecond
              precision.

          supp_icao: The supplying ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          tail_number: The tail number of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/logisticssupport",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "rpt_created_time": rpt_created_time,
                    "source": source,
                    "id": id,
                    "aircraft_mds": aircraft_mds,
                    "curr_icao": curr_icao,
                    "etic": etic,
                    "etmc": etmc,
                    "ext_system_id": ext_system_id,
                    "logistic_action": logistic_action,
                    "logistics_discrepancy_infos": logistics_discrepancy_infos,
                    "logistics_record_id": logistics_record_id,
                    "logistics_remarks": logistics_remarks,
                    "logistics_support_items": logistics_support_items,
                    "logistics_transportation_plans": logistics_transportation_plans,
                    "maint_status_code": maint_status_code,
                    "mc_time": mc_time,
                    "me_time": me_time,
                    "origin": origin,
                    "owner": owner,
                    "reopen_flag": reopen_flag,
                    "rpt_closed_time": rpt_closed_time,
                    "supp_icao": supp_icao,
                    "tail_number": tail_number,
                },
                logistics_support_create_params.LogisticsSupportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        rpt_created_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        curr_icao: str | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etmc: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ext_system_id: str | NotGiven = NOT_GIVEN,
        logistic_action: str | NotGiven = NOT_GIVEN,
        logistics_discrepancy_infos: Iterable[logistics_support_update_params.LogisticsDiscrepancyInfo]
        | NotGiven = NOT_GIVEN,
        logistics_record_id: str | NotGiven = NOT_GIVEN,
        logistics_remarks: Iterable[logistics_support_update_params.LogisticsRemark] | NotGiven = NOT_GIVEN,
        logistics_support_items: Iterable[logistics_support_update_params.LogisticsSupportItem] | NotGiven = NOT_GIVEN,
        logistics_transportation_plans: Iterable[logistics_support_update_params.LogisticsTransportationPlan]
        | NotGiven = NOT_GIVEN,
        maint_status_code: str | NotGiven = NOT_GIVEN,
        mc_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        me_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        reopen_flag: bool | NotGiven = NOT_GIVEN,
        rpt_closed_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        supp_icao: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single LogisticsSupport record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

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

          rpt_created_time: The time this report was created, in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of this aircraft. Intended as, but not constrained
              to, MIL-STD-6016 environment dependent specific type designations.

          curr_icao: The current ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          etic: The estimated time mission capable for the aircraft, in ISO 8601 UCT format with
              millisecond precision. This is the estimated time when the aircraft is mission
              ready.

          etmc: Logistics estimated time mission capable.

          ext_system_id: Optional system identifier from external systs. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          logistic_action: This field identifies the pacing event for bringing the aircraft to Mission
              Capable status. It is used in calculating the Estimated Time Mission Capable
              (ETMC) value. Acceptable values are WA (Will Advise), INW (In Work), P+hhh.h
              (where P=parts and hhh.h is the number of hours up to 999 plus tenths of hours),
              EQ+hhh.h (EQ=equipment), MRT+hhh.h (MRT=maintenance recovery team).

          logistics_discrepancy_infos: Discrepancy information associated with this LogisticsSupport record.

          logistics_record_id: The identifier that represents a Logistics Master Record.

          logistics_remarks: Remarks associated with this LogisticsSupport record.

          logistics_support_items: Support items associated with this LogisticsSupport record.

          logistics_transportation_plans: Transportation plans associated with this LogisticsSupport record, used to
              coordinate maintenance efforts.

          maint_status_code: The maintenance status code of the aircraft which may be based on pilot
              descriptions or evaluation codes. Contact the source provider for details.

          mc_time: The time indicating when all mission essential problems with a given aircraft
              have been fixed and is mission capable. This datetime should be in ISO 8601 UTC
              format with millisecond precision.

          me_time: The time indicating when a given aircraft breaks for a mission essential reason.
              This datetime should be in ISO 8601 UTC format with millisecond precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: The organization that owns this logistics record.

          reopen_flag: This is used to indicate whether a closed master record has been reopened.

          rpt_closed_time: The time this report was closed, in ISO 8601 UTC format with millisecond
              precision.

          supp_icao: The supplying ICAO of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          tail_number: The tail number of the aircraft that is the subject of this
              LogisticsSupportDetails record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/logisticssupport/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "rpt_created_time": rpt_created_time,
                    "source": source,
                    "body_id": body_id,
                    "aircraft_mds": aircraft_mds,
                    "curr_icao": curr_icao,
                    "etic": etic,
                    "etmc": etmc,
                    "ext_system_id": ext_system_id,
                    "logistic_action": logistic_action,
                    "logistics_discrepancy_infos": logistics_discrepancy_infos,
                    "logistics_record_id": logistics_record_id,
                    "logistics_remarks": logistics_remarks,
                    "logistics_support_items": logistics_support_items,
                    "logistics_transportation_plans": logistics_transportation_plans,
                    "maint_status_code": maint_status_code,
                    "mc_time": mc_time,
                    "me_time": me_time,
                    "origin": origin,
                    "owner": owner,
                    "reopen_flag": reopen_flag,
                    "rpt_closed_time": rpt_closed_time,
                    "supp_icao": supp_icao,
                    "tail_number": tail_number,
                },
                logistics_support_update_params.LogisticsSupportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> AsyncPaginator[LogisticsSupportListResponse, AsyncOffsetPage[LogisticsSupportListResponse]]:
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
            "/udl/logisticssupport",
            page=AsyncOffsetPage[LogisticsSupportListResponse],
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
                    logistics_support_list_params.LogisticsSupportListParams,
                ),
            ),
            model=LogisticsSupportListResponse,
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
            "/udl/logisticssupport/count",
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
                    logistics_support_count_params.LogisticsSupportCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[logistics_support_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        LogisticsSupport records as a POST body and ingest into the database. This
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
            "/udl/logisticssupport/createBulk",
            body=await async_maybe_transform(body, Iterable[logistics_support_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> LogisticsSupportGetResponse:
        """
        Service operation to get a single LogisticsSupport record by its unique ID
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
            f"/udl/logisticssupport/{id}",
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
                    logistics_support_get_params.LogisticsSupportGetParams,
                ),
            ),
            cast_to=LogisticsSupportGetResponse,
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
            "/udl/logisticssupport/queryhelp",
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
    ) -> LogisticsSupportTupleResponse:
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
            "/udl/logisticssupport/tuple",
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
                    logistics_support_tuple_params.LogisticsSupportTupleParams,
                ),
            ),
            cast_to=LogisticsSupportTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[logistics_support_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple logisticssupport records as a POST body and
        ingest into the database. This operation is intended to be used for automated
        feeds into UDL. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-logisticssupport",
            body=await async_maybe_transform(body, Iterable[logistics_support_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LogisticsSupportResourceWithRawResponse:
    def __init__(self, logistics_support: LogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

        self.create = to_raw_response_wrapper(
            logistics_support.create,
        )
        self.update = to_raw_response_wrapper(
            logistics_support.update,
        )
        self.list = to_raw_response_wrapper(
            logistics_support.list,
        )
        self.count = to_raw_response_wrapper(
            logistics_support.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            logistics_support.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            logistics_support.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            logistics_support.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            logistics_support.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            logistics_support.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._logistics_support.history)


class AsyncLogisticsSupportResourceWithRawResponse:
    def __init__(self, logistics_support: AsyncLogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

        self.create = async_to_raw_response_wrapper(
            logistics_support.create,
        )
        self.update = async_to_raw_response_wrapper(
            logistics_support.update,
        )
        self.list = async_to_raw_response_wrapper(
            logistics_support.list,
        )
        self.count = async_to_raw_response_wrapper(
            logistics_support.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            logistics_support.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            logistics_support.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            logistics_support.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            logistics_support.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            logistics_support.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._logistics_support.history)


class LogisticsSupportResourceWithStreamingResponse:
    def __init__(self, logistics_support: LogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

        self.create = to_streamed_response_wrapper(
            logistics_support.create,
        )
        self.update = to_streamed_response_wrapper(
            logistics_support.update,
        )
        self.list = to_streamed_response_wrapper(
            logistics_support.list,
        )
        self.count = to_streamed_response_wrapper(
            logistics_support.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            logistics_support.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            logistics_support.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            logistics_support.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            logistics_support.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            logistics_support.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._logistics_support.history)


class AsyncLogisticsSupportResourceWithStreamingResponse:
    def __init__(self, logistics_support: AsyncLogisticsSupportResource) -> None:
        self._logistics_support = logistics_support

        self.create = async_to_streamed_response_wrapper(
            logistics_support.create,
        )
        self.update = async_to_streamed_response_wrapper(
            logistics_support.update,
        )
        self.list = async_to_streamed_response_wrapper(
            logistics_support.list,
        )
        self.count = async_to_streamed_response_wrapper(
            logistics_support.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            logistics_support.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            logistics_support.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            logistics_support.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            logistics_support.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            logistics_support.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._logistics_support.history)
