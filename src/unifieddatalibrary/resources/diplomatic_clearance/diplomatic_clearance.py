# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    diplomatic_clearance_list_params,
    diplomatic_clearance_count_params,
    diplomatic_clearance_tuple_params,
    diplomatic_clearance_create_params,
    diplomatic_clearance_update_params,
    diplomatic_clearance_retrieve_params,
    diplomatic_clearance_create_bulk_params,
)
from .country import (
    CountryResource,
    AsyncCountryResource,
    CountryResourceWithRawResponse,
    AsyncCountryResourceWithRawResponse,
    CountryResourceWithStreamingResponse,
    AsyncCountryResourceWithStreamingResponse,
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
from ...types.diplomatic_clearance_tuple_response import DiplomaticClearanceTupleResponse
from ...types.air_operations.diplomaticclearance_full import DiplomaticclearanceFull
from ...types.air_operations.diplomaticclearance_abridged import DiplomaticclearanceAbridged

__all__ = ["DiplomaticClearanceResource", "AsyncDiplomaticClearanceResource"]


class DiplomaticClearanceResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def country(self) -> CountryResource:
        return CountryResource(self._client)

    @cached_property
    def with_raw_response(self) -> DiplomaticClearanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DiplomaticClearanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiplomaticClearanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return DiplomaticClearanceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        first_dep_date: Union[str, datetime],
        id_mission: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_details: Iterable[diplomatic_clearance_create_params.DiplomaticClearanceDetail]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_remarks: Iterable[diplomatic_clearance_create_params.DiplomaticClearanceRemark]
        | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        doc_deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_worksheet_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single diplomatic clearance record as a POST body
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

          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision.

          id_mission: Unique identifier of the Mission associated with this diplomatic clearance
              record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve this clearance request.

          diplomatic_clearance_details: Collection of diplomatic clearance details.

          diplomatic_clearance_remarks: Collection of diplomatic clearance remarks.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          doc_deadline: Suspense date for the diplomatic clearance worksheet to be worked, in ISO 8601
              UTC format with millisecond precision.

          external_worksheet_id: Optional diplomatic clearance worksheet ID from external systems. This field has
              no meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/diplomaticclearance",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "first_dep_date": first_dep_date,
                    "id_mission": id_mission,
                    "source": source,
                    "id": id,
                    "apacs_id": apacs_id,
                    "diplomatic_clearance_details": diplomatic_clearance_details,
                    "diplomatic_clearance_remarks": diplomatic_clearance_remarks,
                    "dip_worksheet_name": dip_worksheet_name,
                    "doc_deadline": doc_deadline,
                    "external_worksheet_id": external_worksheet_id,
                    "origin": origin,
                },
                diplomatic_clearance_create_params.DiplomaticClearanceCreateParams,
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
    ) -> DiplomaticclearanceFull:
        """
        Service operation to get a single diplomatic clearance record by its unique ID
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
            f"/udl/diplomaticclearance/{id}",
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
                    diplomatic_clearance_retrieve_params.DiplomaticClearanceRetrieveParams,
                ),
            ),
            cast_to=DiplomaticclearanceFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        first_dep_date: Union[str, datetime],
        id_mission: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_details: Iterable[diplomatic_clearance_update_params.DiplomaticClearanceDetail]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_remarks: Iterable[diplomatic_clearance_update_params.DiplomaticClearanceRemark]
        | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        doc_deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_worksheet_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single diplomatic clearance record.

        A specific
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

          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision.

          id_mission: Unique identifier of the Mission associated with this diplomatic clearance
              record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve this clearance request.

          diplomatic_clearance_details: Collection of diplomatic clearance details.

          diplomatic_clearance_remarks: Collection of diplomatic clearance remarks.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          doc_deadline: Suspense date for the diplomatic clearance worksheet to be worked, in ISO 8601
              UTC format with millisecond precision.

          external_worksheet_id: Optional diplomatic clearance worksheet ID from external systems. This field has
              no meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/diplomaticclearance/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "first_dep_date": first_dep_date,
                    "id_mission": id_mission,
                    "source": source,
                    "body_id": body_id,
                    "apacs_id": apacs_id,
                    "diplomatic_clearance_details": diplomatic_clearance_details,
                    "diplomatic_clearance_remarks": diplomatic_clearance_remarks,
                    "dip_worksheet_name": dip_worksheet_name,
                    "doc_deadline": doc_deadline,
                    "external_worksheet_id": external_worksheet_id,
                    "origin": origin,
                },
                diplomatic_clearance_update_params.DiplomaticClearanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_dep_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[DiplomaticclearanceAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/diplomaticclearance",
            page=SyncOffsetPage[DiplomaticclearanceAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_dep_date": first_dep_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    diplomatic_clearance_list_params.DiplomaticClearanceListParams,
                ),
            ),
            model=DiplomaticclearanceAbridged,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete a diplomatic clearance record specified by the
        passed ID path parameter. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/udl/diplomaticclearance/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        first_dep_date: Union[str, datetime],
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
          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/diplomaticclearance/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_dep_date": first_dep_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    diplomatic_clearance_count_params.DiplomaticClearanceCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[diplomatic_clearance_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        diplomaticclearance records as a POST body and ingest into the database. This
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
            "/udl/diplomaticclearance/createBulk",
            body=maybe_transform(body, Iterable[diplomatic_clearance_create_bulk_params.Body]),
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
            "/udl/diplomaticclearance/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        first_dep_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiplomaticClearanceTupleResponse:
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

          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/diplomaticclearance/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "first_dep_date": first_dep_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    diplomatic_clearance_tuple_params.DiplomaticClearanceTupleParams,
                ),
            ),
            cast_to=DiplomaticClearanceTupleResponse,
        )


class AsyncDiplomaticClearanceResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def country(self) -> AsyncCountryResource:
        return AsyncCountryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiplomaticClearanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDiplomaticClearanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiplomaticClearanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncDiplomaticClearanceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        first_dep_date: Union[str, datetime],
        id_mission: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_details: Iterable[diplomatic_clearance_create_params.DiplomaticClearanceDetail]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_remarks: Iterable[diplomatic_clearance_create_params.DiplomaticClearanceRemark]
        | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        doc_deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_worksheet_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single diplomatic clearance record as a POST body
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

          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision.

          id_mission: Unique identifier of the Mission associated with this diplomatic clearance
              record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve this clearance request.

          diplomatic_clearance_details: Collection of diplomatic clearance details.

          diplomatic_clearance_remarks: Collection of diplomatic clearance remarks.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          doc_deadline: Suspense date for the diplomatic clearance worksheet to be worked, in ISO 8601
              UTC format with millisecond precision.

          external_worksheet_id: Optional diplomatic clearance worksheet ID from external systems. This field has
              no meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/diplomaticclearance",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "first_dep_date": first_dep_date,
                    "id_mission": id_mission,
                    "source": source,
                    "id": id,
                    "apacs_id": apacs_id,
                    "diplomatic_clearance_details": diplomatic_clearance_details,
                    "diplomatic_clearance_remarks": diplomatic_clearance_remarks,
                    "dip_worksheet_name": dip_worksheet_name,
                    "doc_deadline": doc_deadline,
                    "external_worksheet_id": external_worksheet_id,
                    "origin": origin,
                },
                diplomatic_clearance_create_params.DiplomaticClearanceCreateParams,
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
    ) -> DiplomaticclearanceFull:
        """
        Service operation to get a single diplomatic clearance record by its unique ID
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
            f"/udl/diplomaticclearance/{id}",
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
                    diplomatic_clearance_retrieve_params.DiplomaticClearanceRetrieveParams,
                ),
            ),
            cast_to=DiplomaticclearanceFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        first_dep_date: Union[str, datetime],
        id_mission: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        diplomatic_clearance_details: Iterable[diplomatic_clearance_update_params.DiplomaticClearanceDetail]
        | NotGiven = NOT_GIVEN,
        diplomatic_clearance_remarks: Iterable[diplomatic_clearance_update_params.DiplomaticClearanceRemark]
        | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        doc_deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_worksheet_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single diplomatic clearance record.

        A specific
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

          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision.

          id_mission: Unique identifier of the Mission associated with this diplomatic clearance
              record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve this clearance request.

          diplomatic_clearance_details: Collection of diplomatic clearance details.

          diplomatic_clearance_remarks: Collection of diplomatic clearance remarks.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          doc_deadline: Suspense date for the diplomatic clearance worksheet to be worked, in ISO 8601
              UTC format with millisecond precision.

          external_worksheet_id: Optional diplomatic clearance worksheet ID from external systems. This field has
              no meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/diplomaticclearance/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "first_dep_date": first_dep_date,
                    "id_mission": id_mission,
                    "source": source,
                    "body_id": body_id,
                    "apacs_id": apacs_id,
                    "diplomatic_clearance_details": diplomatic_clearance_details,
                    "diplomatic_clearance_remarks": diplomatic_clearance_remarks,
                    "dip_worksheet_name": dip_worksheet_name,
                    "doc_deadline": doc_deadline,
                    "external_worksheet_id": external_worksheet_id,
                    "origin": origin,
                },
                diplomatic_clearance_update_params.DiplomaticClearanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        first_dep_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DiplomaticclearanceAbridged, AsyncOffsetPage[DiplomaticclearanceAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/diplomaticclearance",
            page=AsyncOffsetPage[DiplomaticclearanceAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "first_dep_date": first_dep_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    diplomatic_clearance_list_params.DiplomaticClearanceListParams,
                ),
            ),
            model=DiplomaticclearanceAbridged,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to delete a diplomatic clearance record specified by the
        passed ID path parameter. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/udl/diplomaticclearance/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        first_dep_date: Union[str, datetime],
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
          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/diplomaticclearance/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "first_dep_date": first_dep_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    diplomatic_clearance_count_params.DiplomaticClearanceCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[diplomatic_clearance_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        diplomaticclearance records as a POST body and ingest into the database. This
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
            "/udl/diplomaticclearance/createBulk",
            body=await async_maybe_transform(body, Iterable[diplomatic_clearance_create_bulk_params.Body]),
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
            "/udl/diplomaticclearance/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        first_dep_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiplomaticClearanceTupleResponse:
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

          first_dep_date: The First Departure Date (FDD) the mission is scheduled for departure, in ISO
              8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/diplomaticclearance/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "first_dep_date": first_dep_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    diplomatic_clearance_tuple_params.DiplomaticClearanceTupleParams,
                ),
            ),
            cast_to=DiplomaticClearanceTupleResponse,
        )


class DiplomaticClearanceResourceWithRawResponse:
    def __init__(self, diplomatic_clearance: DiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.create = to_raw_response_wrapper(
            diplomatic_clearance.create,
        )
        self.retrieve = to_raw_response_wrapper(
            diplomatic_clearance.retrieve,
        )
        self.update = to_raw_response_wrapper(
            diplomatic_clearance.update,
        )
        self.list = to_raw_response_wrapper(
            diplomatic_clearance.list,
        )
        self.delete = to_raw_response_wrapper(
            diplomatic_clearance.delete,
        )
        self.count = to_raw_response_wrapper(
            diplomatic_clearance.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            diplomatic_clearance.create_bulk,
        )
        self.queryhelp = to_raw_response_wrapper(
            diplomatic_clearance.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            diplomatic_clearance.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._diplomatic_clearance.history)

    @cached_property
    def country(self) -> CountryResourceWithRawResponse:
        return CountryResourceWithRawResponse(self._diplomatic_clearance.country)


class AsyncDiplomaticClearanceResourceWithRawResponse:
    def __init__(self, diplomatic_clearance: AsyncDiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.create = async_to_raw_response_wrapper(
            diplomatic_clearance.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            diplomatic_clearance.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            diplomatic_clearance.update,
        )
        self.list = async_to_raw_response_wrapper(
            diplomatic_clearance.list,
        )
        self.delete = async_to_raw_response_wrapper(
            diplomatic_clearance.delete,
        )
        self.count = async_to_raw_response_wrapper(
            diplomatic_clearance.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            diplomatic_clearance.create_bulk,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            diplomatic_clearance.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            diplomatic_clearance.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._diplomatic_clearance.history)

    @cached_property
    def country(self) -> AsyncCountryResourceWithRawResponse:
        return AsyncCountryResourceWithRawResponse(self._diplomatic_clearance.country)


class DiplomaticClearanceResourceWithStreamingResponse:
    def __init__(self, diplomatic_clearance: DiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.create = to_streamed_response_wrapper(
            diplomatic_clearance.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            diplomatic_clearance.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            diplomatic_clearance.update,
        )
        self.list = to_streamed_response_wrapper(
            diplomatic_clearance.list,
        )
        self.delete = to_streamed_response_wrapper(
            diplomatic_clearance.delete,
        )
        self.count = to_streamed_response_wrapper(
            diplomatic_clearance.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            diplomatic_clearance.create_bulk,
        )
        self.queryhelp = to_streamed_response_wrapper(
            diplomatic_clearance.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            diplomatic_clearance.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._diplomatic_clearance.history)

    @cached_property
    def country(self) -> CountryResourceWithStreamingResponse:
        return CountryResourceWithStreamingResponse(self._diplomatic_clearance.country)


class AsyncDiplomaticClearanceResourceWithStreamingResponse:
    def __init__(self, diplomatic_clearance: AsyncDiplomaticClearanceResource) -> None:
        self._diplomatic_clearance = diplomatic_clearance

        self.create = async_to_streamed_response_wrapper(
            diplomatic_clearance.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            diplomatic_clearance.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            diplomatic_clearance.update,
        )
        self.list = async_to_streamed_response_wrapper(
            diplomatic_clearance.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            diplomatic_clearance.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            diplomatic_clearance.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            diplomatic_clearance.create_bulk,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            diplomatic_clearance.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            diplomatic_clearance.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._diplomatic_clearance.history)

    @cached_property
    def country(self) -> AsyncCountryResourceWithStreamingResponse:
        return AsyncCountryResourceWithStreamingResponse(self._diplomatic_clearance.country)
