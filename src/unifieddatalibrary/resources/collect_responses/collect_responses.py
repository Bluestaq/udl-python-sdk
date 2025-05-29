# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .tuple import (
    TupleResource,
    AsyncTupleResource,
    TupleResourceWithRawResponse,
    AsyncTupleResourceWithRawResponse,
    TupleResourceWithStreamingResponse,
    AsyncTupleResourceWithStreamingResponse,
)
from ...types import (
    collect_response_list_params,
    collect_response_count_params,
    collect_response_create_params,
    collect_response_retrieve_params,
    collect_response_create_bulk_params,
    collect_response_unvalidated_publish_params,
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
from .history.history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...types.collect_response_abridged import CollectResponseAbridged
from ...types.shared.collect_response_full import CollectResponseFull
from ...types.collect_response_query_help_response import CollectResponseQueryHelpResponse

__all__ = ["CollectResponsesResource", "AsyncCollectResponsesResource"]


class CollectResponsesResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def tuple(self) -> TupleResource:
        return TupleResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CollectResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CollectResponsesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_request: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        actual_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alt_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alt_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        err_code: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        id_plan: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Collect Response object as a POST body and
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

          id_request: Unique identifier of the request associated with this response.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          actual_end_time: The actual end time of the collect or contact, in ISO 8601 UTC format.

          actual_start_time: The actual start time of the collect or contact, in ISO 8601 UTC format.

          alt_end_time: Proposed alternative end time, in ISO 8601 UTC format.

          alt_start_time: Proposed alternative start time, in ISO 8601 UTC format.

          err_code: Error code associated with this request/response.

          external_id: UUID from external systems. This field has no meaning within UDL and is provided
              as a convenience for systems that require tracking of internal system generated
              ID.

          id_plan: Unique identifier of the parent plan or schedule associated with the
              request/response.

          id_sensor: Unique identifier of the reporting sensor.

          notes: Notes or comments associated with this response.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by data source to indicate the target object of
              this response. This may be an internal identifier and not necessarily a valid
              satellite number.

          orig_sensor_id: Optional identifier provided by the collection source to indicate the sensor
              identifier responding to this collect or contact. This may be an internal
              identifier and not necessarily a valid sensor ID.

          sat_no: Satellite/catalog number of the target on-orbit object.

          src_ids: Array of UUIDs of the UDL data record(s) collected in response to the associated
              request. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. The appropriate API operation can be used to
              retrieve the specified object(s) (e.g. /udl/rfobservation/{uuid}).

          src_typs: Array of UDL record type(s) (DOA, ELSET, EO, RADAR, RF, SV) collected or
              produced in response to the associated request. See the associated 'srcIds'
              array for the record UUIDs, positionally corresponding to the record types in
              this array. The 'srcTyps' and 'srcIds' arrays must match in size. The
              appropriate API operation can be used to retrieve the specified object(s) (e.g.
              /udl/rfobservation/{uuid}).

          status: The status of the request (ACCEPTED, CANCELLED, COLLECTED, COMPLETED, DELIVERED,
              FAILED, PARTIAL, PROPOSED, REJECTED, SCHEDULED):

              ACCEPTED: The collect or contact request has been received and accepted.

              CANCELLED: A previously scheduled collect or contact whose execution was
              cancelled.

              COLLECTED: The collect has been accomplished. A collected state implies that
              additional activity is required for delivery/completion.

              COMPLETED: The collect or contact has been completed. For many systems completed
              and delivered constitute an equivalent successful end state.

              DELIVERED: The collected observation(s) have been delivered to the requestor.
              For many systems completed and delivered constitute an equivalent successful end
              state. A DELIVERED state is typically used for systems that exhibit a delay
              between collect and delivery, such as with space-based systems which require
              ground contact to deliver observations.

              FAILED: The collect or contact was attempted and failed, or the delivery of the
              collected observation(s) failed. A FAILED status may be accompanied by an error
              code (errCode), if available.

              PARTIAL: A PARTIAL state indicates that a part of a multi-track request has been
              accomplished, but the full request is incomplete. A PARTIAL status should
              ultimately be resolved to an end state.

              PROPOSED: Indicates that the request was received and alternate collect or
              contact time(s) (altStartTime, altEndTime) have been proposed. If an alternate
              is accepted by the requestor the current request should be cancelled and a new
              request created.

              REJECTED: The request has been received and rejected by the provider. A REJECTED
              status may be accompanied by an explanation (notes) of the reason that the
              request was rejected.

              SCHEDULED: The request was received and has been scheduled for execution.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional task ID associated with the request/response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/collectresponse",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_request": id_request,
                    "source": source,
                    "id": id,
                    "actual_end_time": actual_end_time,
                    "actual_start_time": actual_start_time,
                    "alt_end_time": alt_end_time,
                    "alt_start_time": alt_start_time,
                    "err_code": err_code,
                    "external_id": external_id,
                    "id_plan": id_plan,
                    "id_sensor": id_sensor,
                    "notes": notes,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "sat_no": sat_no,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "status": status,
                    "tags": tags,
                    "task_id": task_id,
                },
                collect_response_create_params.CollectResponseCreateParams,
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
    ) -> CollectResponseFull:
        """
        Service operation to get a single Collect Response record by its unique ID
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
            f"/udl/collectresponse/{id}",
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
                    collect_response_retrieve_params.CollectResponseRetrieveParams,
                ),
            ),
            cast_to=CollectResponseFull,
        )

    def list(
        self,
        *,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[CollectResponseAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/collectresponse",
            page=SyncOffsetPage[CollectResponseAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    collect_response_list_params.CollectResponseListParams,
                ),
            ),
            model=CollectResponseAbridged,
        )

    def count(
        self,
        *,
        created_at: Union[str, date],
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
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/collectresponse/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    collect_response_count_params.CollectResponseCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[collect_response_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Collect Response objects as a POST body and ingest into the database. This
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
            "/udl/collectresponse/createBulk",
            body=maybe_transform(body, Iterable[collect_response_create_bulk_params.Body]),
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
    ) -> CollectResponseQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/collectresponse/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectResponseQueryHelpResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[collect_response_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of CollectResponse as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-collectresponse",
            body=maybe_transform(body, Iterable[collect_response_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCollectResponsesResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def tuple(self) -> AsyncTupleResource:
        return AsyncTupleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCollectResponsesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_request: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        actual_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alt_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alt_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        err_code: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        id_plan: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        src_ids: List[str] | NotGiven = NOT_GIVEN,
        src_typs: List[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Collect Response object as a POST body and
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

          id_request: Unique identifier of the request associated with this response.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          actual_end_time: The actual end time of the collect or contact, in ISO 8601 UTC format.

          actual_start_time: The actual start time of the collect or contact, in ISO 8601 UTC format.

          alt_end_time: Proposed alternative end time, in ISO 8601 UTC format.

          alt_start_time: Proposed alternative start time, in ISO 8601 UTC format.

          err_code: Error code associated with this request/response.

          external_id: UUID from external systems. This field has no meaning within UDL and is provided
              as a convenience for systems that require tracking of internal system generated
              ID.

          id_plan: Unique identifier of the parent plan or schedule associated with the
              request/response.

          id_sensor: Unique identifier of the reporting sensor.

          notes: Notes or comments associated with this response.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by data source to indicate the target object of
              this response. This may be an internal identifier and not necessarily a valid
              satellite number.

          orig_sensor_id: Optional identifier provided by the collection source to indicate the sensor
              identifier responding to this collect or contact. This may be an internal
              identifier and not necessarily a valid sensor ID.

          sat_no: Satellite/catalog number of the target on-orbit object.

          src_ids: Array of UUIDs of the UDL data record(s) collected in response to the associated
              request. See the associated 'srcTyps' array for the specific types of data,
              positionally corresponding to the UUIDs in this array. The 'srcTyps' and
              'srcIds' arrays must match in size. The appropriate API operation can be used to
              retrieve the specified object(s) (e.g. /udl/rfobservation/{uuid}).

          src_typs: Array of UDL record type(s) (DOA, ELSET, EO, RADAR, RF, SV) collected or
              produced in response to the associated request. See the associated 'srcIds'
              array for the record UUIDs, positionally corresponding to the record types in
              this array. The 'srcTyps' and 'srcIds' arrays must match in size. The
              appropriate API operation can be used to retrieve the specified object(s) (e.g.
              /udl/rfobservation/{uuid}).

          status: The status of the request (ACCEPTED, CANCELLED, COLLECTED, COMPLETED, DELIVERED,
              FAILED, PARTIAL, PROPOSED, REJECTED, SCHEDULED):

              ACCEPTED: The collect or contact request has been received and accepted.

              CANCELLED: A previously scheduled collect or contact whose execution was
              cancelled.

              COLLECTED: The collect has been accomplished. A collected state implies that
              additional activity is required for delivery/completion.

              COMPLETED: The collect or contact has been completed. For many systems completed
              and delivered constitute an equivalent successful end state.

              DELIVERED: The collected observation(s) have been delivered to the requestor.
              For many systems completed and delivered constitute an equivalent successful end
              state. A DELIVERED state is typically used for systems that exhibit a delay
              between collect and delivery, such as with space-based systems which require
              ground contact to deliver observations.

              FAILED: The collect or contact was attempted and failed, or the delivery of the
              collected observation(s) failed. A FAILED status may be accompanied by an error
              code (errCode), if available.

              PARTIAL: A PARTIAL state indicates that a part of a multi-track request has been
              accomplished, but the full request is incomplete. A PARTIAL status should
              ultimately be resolved to an end state.

              PROPOSED: Indicates that the request was received and alternate collect or
              contact time(s) (altStartTime, altEndTime) have been proposed. If an alternate
              is accepted by the requestor the current request should be cancelled and a new
              request created.

              REJECTED: The request has been received and rejected by the provider. A REJECTED
              status may be accompanied by an explanation (notes) of the reason that the
              request was rejected.

              SCHEDULED: The request was received and has been scheduled for execution.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          task_id: Optional task ID associated with the request/response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/collectresponse",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_request": id_request,
                    "source": source,
                    "id": id,
                    "actual_end_time": actual_end_time,
                    "actual_start_time": actual_start_time,
                    "alt_end_time": alt_end_time,
                    "alt_start_time": alt_start_time,
                    "err_code": err_code,
                    "external_id": external_id,
                    "id_plan": id_plan,
                    "id_sensor": id_sensor,
                    "notes": notes,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "sat_no": sat_no,
                    "src_ids": src_ids,
                    "src_typs": src_typs,
                    "status": status,
                    "tags": tags,
                    "task_id": task_id,
                },
                collect_response_create_params.CollectResponseCreateParams,
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
    ) -> CollectResponseFull:
        """
        Service operation to get a single Collect Response record by its unique ID
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
            f"/udl/collectresponse/{id}",
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
                    collect_response_retrieve_params.CollectResponseRetrieveParams,
                ),
            ),
            cast_to=CollectResponseFull,
        )

    def list(
        self,
        *,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CollectResponseAbridged, AsyncOffsetPage[CollectResponseAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/collectresponse",
            page=AsyncOffsetPage[CollectResponseAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    collect_response_list_params.CollectResponseListParams,
                ),
            ),
            model=CollectResponseAbridged,
        )

    async def count(
        self,
        *,
        created_at: Union[str, date],
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
          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/collectresponse/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    collect_response_count_params.CollectResponseCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[collect_response_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Collect Response objects as a POST body and ingest into the database. This
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
            "/udl/collectresponse/createBulk",
            body=await async_maybe_transform(body, Iterable[collect_response_create_bulk_params.Body]),
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
    ) -> CollectResponseQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/collectresponse/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectResponseQueryHelpResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[collect_response_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of CollectResponse as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-collectresponse",
            body=await async_maybe_transform(body, Iterable[collect_response_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CollectResponsesResourceWithRawResponse:
    def __init__(self, collect_responses: CollectResponsesResource) -> None:
        self._collect_responses = collect_responses

        self.create = to_raw_response_wrapper(
            collect_responses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collect_responses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            collect_responses.list,
        )
        self.count = to_raw_response_wrapper(
            collect_responses.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            collect_responses.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            collect_responses.query_help,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            collect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._collect_responses.history)

    @cached_property
    def tuple(self) -> TupleResourceWithRawResponse:
        return TupleResourceWithRawResponse(self._collect_responses.tuple)


class AsyncCollectResponsesResourceWithRawResponse:
    def __init__(self, collect_responses: AsyncCollectResponsesResource) -> None:
        self._collect_responses = collect_responses

        self.create = async_to_raw_response_wrapper(
            collect_responses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collect_responses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            collect_responses.list,
        )
        self.count = async_to_raw_response_wrapper(
            collect_responses.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            collect_responses.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            collect_responses.query_help,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            collect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._collect_responses.history)

    @cached_property
    def tuple(self) -> AsyncTupleResourceWithRawResponse:
        return AsyncTupleResourceWithRawResponse(self._collect_responses.tuple)


class CollectResponsesResourceWithStreamingResponse:
    def __init__(self, collect_responses: CollectResponsesResource) -> None:
        self._collect_responses = collect_responses

        self.create = to_streamed_response_wrapper(
            collect_responses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collect_responses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            collect_responses.list,
        )
        self.count = to_streamed_response_wrapper(
            collect_responses.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            collect_responses.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            collect_responses.query_help,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            collect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._collect_responses.history)

    @cached_property
    def tuple(self) -> TupleResourceWithStreamingResponse:
        return TupleResourceWithStreamingResponse(self._collect_responses.tuple)


class AsyncCollectResponsesResourceWithStreamingResponse:
    def __init__(self, collect_responses: AsyncCollectResponsesResource) -> None:
        self._collect_responses = collect_responses

        self.create = async_to_streamed_response_wrapper(
            collect_responses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collect_responses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            collect_responses.list,
        )
        self.count = async_to_streamed_response_wrapper(
            collect_responses.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            collect_responses.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            collect_responses.query_help,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            collect_responses.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._collect_responses.history)

    @cached_property
    def tuple(self) -> AsyncTupleResourceWithStreamingResponse:
        return AsyncTupleResourceWithStreamingResponse(self._collect_responses.tuple)
