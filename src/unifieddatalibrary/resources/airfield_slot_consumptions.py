# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    airfield_slot_consumption_list_params,
    airfield_slot_consumption_count_params,
    airfield_slot_consumption_tuple_params,
    airfield_slot_consumption_create_params,
    airfield_slot_consumption_update_params,
    airfield_slot_consumption_retrieve_params,
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
from ..types.airfieldslotconsumption_abridged import AirfieldslotconsumptionAbridged
from ..types.shared.airfieldslotconsumption_full import AirfieldslotconsumptionFull
from ..types.airfield_slot_consumption_tuple_response import AirfieldSlotConsumptionTupleResponse
from ..types.airfield_slot_consumption_queryhelp_response import AirfieldSlotConsumptionQueryhelpResponse

__all__ = ["AirfieldSlotConsumptionsResource", "AsyncAirfieldSlotConsumptionsResource"]


class AirfieldSlotConsumptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AirfieldSlotConsumptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirfieldSlotConsumptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirfieldSlotConsumptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirfieldSlotConsumptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield_slot: str,
        num_aircraft: int,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        alt_arr_sortie_id: str | NotGiven = NOT_GIVEN,
        alt_dep_sortie_id: str | NotGiven = NOT_GIVEN,
        app_comment: str | NotGiven = NOT_GIVEN,
        app_initials: str | NotGiven = NOT_GIVEN,
        app_org: str | NotGiven = NOT_GIVEN,
        call_signs: List[str] | NotGiven = NOT_GIVEN,
        consumer: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        id_arr_sortie: str | NotGiven = NOT_GIVEN,
        id_dep_sortie: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        occ_aircraft_mds: str | NotGiven = NOT_GIVEN,
        occ_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        occ_tail_number: str | NotGiven = NOT_GIVEN,
        occupied: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        req_comment: str | NotGiven = NOT_GIVEN,
        req_initials: str | NotGiven = NOT_GIVEN,
        req_org: str | NotGiven = NOT_GIVEN,
        res_aircraft_mds: str | NotGiven = NOT_GIVEN,
        res_mission_id: str | NotGiven = NOT_GIVEN,
        res_reason: str | NotGiven = NOT_GIVEN,
        res_tail_number: str | NotGiven = NOT_GIVEN,
        res_type: str | NotGiven = NOT_GIVEN,
        status: Literal["REQUESTED", "APPROVED", "DENIED", "BLOCKED", "OTHER"] | NotGiven = NOT_GIVEN,
        target_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airfieldslotconsumption record as a POST body
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

          id_airfield_slot: Unique identifier of the airfield slot for which this slot consumption record is
              referencing.

          num_aircraft: Number of aircraft using this slot for this time.

          source: Source of the data.

          start_time: The start of the slot window, in ISO 8601 UTC format.

          id: Unique identifier of the record, auto-generated by the system.

          alt_arr_sortie_id: Alternate identifier of the sortie arriving at the slot start time provided by
              the source.

          alt_dep_sortie_id: Alternate identifier of the sortie departing at the slot end time provided by
              the source.

          app_comment: Comments from the approver.

          app_initials: Initials of the person approving the use of this slot. Use SYSTEM if
              auto-approved without human involvement.

          app_org: Short name of the organization approving the use of this slot.

          call_signs: Array of call signs of the aircraft using this slot.

          consumer: Identifying name of the aircraft using this slot. Names are often Prior
              Permission Required (PPR) numbers or other similar human-readable identifiers.

          end_time: The end of the slot window, in ISO 8601 UTC format.

          id_arr_sortie: Unique identifier of the sortie arriving at the slot start time.

          id_dep_sortie: Unique identifier of the sortie departing at the slot end time.

          mission_id: Mission identifier using this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          occ_aircraft_mds: The aircraft Model Design Series designation of the aircraft occupying this
              slot.

          occ_start_time: Time the aircraft began occupying this slot, in ISO 8601 UTC format with
              millisecond precision.

          occ_tail_number: The tail number of the aircraft occupying this slot.

          occupied: Flag indicating if the slot is occupied.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          req_comment: Comments from the requester.

          req_initials: Initials of the person requesting the use of this slot. Use SYSTEM if this
              request is auto-generated by an auto-planning system.

          req_org: Short name of the organization requesting use of this slot.

          res_aircraft_mds: The aircraft Model Design Series designation of the aircraft this slot is
              reserved for.

          res_mission_id: Mission identifier reserving this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          res_reason: The reason the slot reservation was made.

          res_tail_number: The tail number of the aircraft this slot is reserved for.

          res_type: Indicates the type of reservation (e.g. M for Mission, A for Aircraft, O for
              Other).

          status: Current status of this slot (REQUESTED / APPROVED / DENIED / BLOCKED / OTHER).

          target_time: The desired time for aircraft action such as landing, take off, parking, etc.,
              in ISO 8601 UTC format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airfieldslotconsumption",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield_slot": id_airfield_slot,
                    "num_aircraft": num_aircraft,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "alt_arr_sortie_id": alt_arr_sortie_id,
                    "alt_dep_sortie_id": alt_dep_sortie_id,
                    "app_comment": app_comment,
                    "app_initials": app_initials,
                    "app_org": app_org,
                    "call_signs": call_signs,
                    "consumer": consumer,
                    "end_time": end_time,
                    "id_arr_sortie": id_arr_sortie,
                    "id_dep_sortie": id_dep_sortie,
                    "mission_id": mission_id,
                    "occ_aircraft_mds": occ_aircraft_mds,
                    "occ_start_time": occ_start_time,
                    "occ_tail_number": occ_tail_number,
                    "occupied": occupied,
                    "origin": origin,
                    "req_comment": req_comment,
                    "req_initials": req_initials,
                    "req_org": req_org,
                    "res_aircraft_mds": res_aircraft_mds,
                    "res_mission_id": res_mission_id,
                    "res_reason": res_reason,
                    "res_tail_number": res_tail_number,
                    "res_type": res_type,
                    "status": status,
                    "target_time": target_time,
                },
                airfield_slot_consumption_create_params.AirfieldSlotConsumptionCreateParams,
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
    ) -> AirfieldslotconsumptionFull:
        """
        Service operation to get a single airfieldslotconsumption record by its unique
        ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/airfieldslotconsumption/{id}",
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
                    airfield_slot_consumption_retrieve_params.AirfieldSlotConsumptionRetrieveParams,
                ),
            ),
            cast_to=AirfieldslotconsumptionFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield_slot: str,
        num_aircraft: int,
        source: str,
        start_time: Union[str, datetime],
        body_id: str | NotGiven = NOT_GIVEN,
        alt_arr_sortie_id: str | NotGiven = NOT_GIVEN,
        alt_dep_sortie_id: str | NotGiven = NOT_GIVEN,
        app_comment: str | NotGiven = NOT_GIVEN,
        app_initials: str | NotGiven = NOT_GIVEN,
        app_org: str | NotGiven = NOT_GIVEN,
        call_signs: List[str] | NotGiven = NOT_GIVEN,
        consumer: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        id_arr_sortie: str | NotGiven = NOT_GIVEN,
        id_dep_sortie: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        occ_aircraft_mds: str | NotGiven = NOT_GIVEN,
        occ_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        occ_tail_number: str | NotGiven = NOT_GIVEN,
        occupied: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        req_comment: str | NotGiven = NOT_GIVEN,
        req_initials: str | NotGiven = NOT_GIVEN,
        req_org: str | NotGiven = NOT_GIVEN,
        res_aircraft_mds: str | NotGiven = NOT_GIVEN,
        res_mission_id: str | NotGiven = NOT_GIVEN,
        res_reason: str | NotGiven = NOT_GIVEN,
        res_tail_number: str | NotGiven = NOT_GIVEN,
        res_type: str | NotGiven = NOT_GIVEN,
        status: Literal["REQUESTED", "APPROVED", "DENIED", "BLOCKED", "OTHER"] | NotGiven = NOT_GIVEN,
        target_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AirfieldSlotConsumption.

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

          id_airfield_slot: Unique identifier of the airfield slot for which this slot consumption record is
              referencing.

          num_aircraft: Number of aircraft using this slot for this time.

          source: Source of the data.

          start_time: The start of the slot window, in ISO 8601 UTC format.

          body_id: Unique identifier of the record, auto-generated by the system.

          alt_arr_sortie_id: Alternate identifier of the sortie arriving at the slot start time provided by
              the source.

          alt_dep_sortie_id: Alternate identifier of the sortie departing at the slot end time provided by
              the source.

          app_comment: Comments from the approver.

          app_initials: Initials of the person approving the use of this slot. Use SYSTEM if
              auto-approved without human involvement.

          app_org: Short name of the organization approving the use of this slot.

          call_signs: Array of call signs of the aircraft using this slot.

          consumer: Identifying name of the aircraft using this slot. Names are often Prior
              Permission Required (PPR) numbers or other similar human-readable identifiers.

          end_time: The end of the slot window, in ISO 8601 UTC format.

          id_arr_sortie: Unique identifier of the sortie arriving at the slot start time.

          id_dep_sortie: Unique identifier of the sortie departing at the slot end time.

          mission_id: Mission identifier using this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          occ_aircraft_mds: The aircraft Model Design Series designation of the aircraft occupying this
              slot.

          occ_start_time: Time the aircraft began occupying this slot, in ISO 8601 UTC format with
              millisecond precision.

          occ_tail_number: The tail number of the aircraft occupying this slot.

          occupied: Flag indicating if the slot is occupied.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          req_comment: Comments from the requester.

          req_initials: Initials of the person requesting the use of this slot. Use SYSTEM if this
              request is auto-generated by an auto-planning system.

          req_org: Short name of the organization requesting use of this slot.

          res_aircraft_mds: The aircraft Model Design Series designation of the aircraft this slot is
              reserved for.

          res_mission_id: Mission identifier reserving this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          res_reason: The reason the slot reservation was made.

          res_tail_number: The tail number of the aircraft this slot is reserved for.

          res_type: Indicates the type of reservation (e.g. M for Mission, A for Aircraft, O for
              Other).

          status: Current status of this slot (REQUESTED / APPROVED / DENIED / BLOCKED / OTHER).

          target_time: The desired time for aircraft action such as landing, take off, parking, etc.,
              in ISO 8601 UTC format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/airfieldslotconsumption/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield_slot": id_airfield_slot,
                    "num_aircraft": num_aircraft,
                    "source": source,
                    "start_time": start_time,
                    "body_id": body_id,
                    "alt_arr_sortie_id": alt_arr_sortie_id,
                    "alt_dep_sortie_id": alt_dep_sortie_id,
                    "app_comment": app_comment,
                    "app_initials": app_initials,
                    "app_org": app_org,
                    "call_signs": call_signs,
                    "consumer": consumer,
                    "end_time": end_time,
                    "id_arr_sortie": id_arr_sortie,
                    "id_dep_sortie": id_dep_sortie,
                    "mission_id": mission_id,
                    "occ_aircraft_mds": occ_aircraft_mds,
                    "occ_start_time": occ_start_time,
                    "occ_tail_number": occ_tail_number,
                    "occupied": occupied,
                    "origin": origin,
                    "req_comment": req_comment,
                    "req_initials": req_initials,
                    "req_org": req_org,
                    "res_aircraft_mds": res_aircraft_mds,
                    "res_mission_id": res_mission_id,
                    "res_reason": res_reason,
                    "res_tail_number": res_tail_number,
                    "res_type": res_type,
                    "status": status,
                    "target_time": target_time,
                },
                airfield_slot_consumption_update_params.AirfieldSlotConsumptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[AirfieldslotconsumptionAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start of the slot window, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/airfieldslotconsumption",
            page=SyncOffsetPage[AirfieldslotconsumptionAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airfield_slot_consumption_list_params.AirfieldSlotConsumptionListParams,
                ),
            ),
            model=AirfieldslotconsumptionAbridged,
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
        Service operation to delete an airfieldslotconsumption record specified by the
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
            f"/udl/airfieldslotconsumption/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The start of the slot window, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/airfieldslotconsumption/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airfield_slot_consumption_count_params.AirfieldSlotConsumptionCountParams,
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
    ) -> AirfieldSlotConsumptionQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/airfieldslotconsumption/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirfieldSlotConsumptionQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirfieldSlotConsumptionTupleResponse:
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

          start_time: The start of the slot window, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/airfieldslotconsumption/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airfield_slot_consumption_tuple_params.AirfieldSlotConsumptionTupleParams,
                ),
            ),
            cast_to=AirfieldSlotConsumptionTupleResponse,
        )


class AsyncAirfieldSlotConsumptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAirfieldSlotConsumptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirfieldSlotConsumptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield_slot: str,
        num_aircraft: int,
        source: str,
        start_time: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        alt_arr_sortie_id: str | NotGiven = NOT_GIVEN,
        alt_dep_sortie_id: str | NotGiven = NOT_GIVEN,
        app_comment: str | NotGiven = NOT_GIVEN,
        app_initials: str | NotGiven = NOT_GIVEN,
        app_org: str | NotGiven = NOT_GIVEN,
        call_signs: List[str] | NotGiven = NOT_GIVEN,
        consumer: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        id_arr_sortie: str | NotGiven = NOT_GIVEN,
        id_dep_sortie: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        occ_aircraft_mds: str | NotGiven = NOT_GIVEN,
        occ_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        occ_tail_number: str | NotGiven = NOT_GIVEN,
        occupied: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        req_comment: str | NotGiven = NOT_GIVEN,
        req_initials: str | NotGiven = NOT_GIVEN,
        req_org: str | NotGiven = NOT_GIVEN,
        res_aircraft_mds: str | NotGiven = NOT_GIVEN,
        res_mission_id: str | NotGiven = NOT_GIVEN,
        res_reason: str | NotGiven = NOT_GIVEN,
        res_tail_number: str | NotGiven = NOT_GIVEN,
        res_type: str | NotGiven = NOT_GIVEN,
        status: Literal["REQUESTED", "APPROVED", "DENIED", "BLOCKED", "OTHER"] | NotGiven = NOT_GIVEN,
        target_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airfieldslotconsumption record as a POST body
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

          id_airfield_slot: Unique identifier of the airfield slot for which this slot consumption record is
              referencing.

          num_aircraft: Number of aircraft using this slot for this time.

          source: Source of the data.

          start_time: The start of the slot window, in ISO 8601 UTC format.

          id: Unique identifier of the record, auto-generated by the system.

          alt_arr_sortie_id: Alternate identifier of the sortie arriving at the slot start time provided by
              the source.

          alt_dep_sortie_id: Alternate identifier of the sortie departing at the slot end time provided by
              the source.

          app_comment: Comments from the approver.

          app_initials: Initials of the person approving the use of this slot. Use SYSTEM if
              auto-approved without human involvement.

          app_org: Short name of the organization approving the use of this slot.

          call_signs: Array of call signs of the aircraft using this slot.

          consumer: Identifying name of the aircraft using this slot. Names are often Prior
              Permission Required (PPR) numbers or other similar human-readable identifiers.

          end_time: The end of the slot window, in ISO 8601 UTC format.

          id_arr_sortie: Unique identifier of the sortie arriving at the slot start time.

          id_dep_sortie: Unique identifier of the sortie departing at the slot end time.

          mission_id: Mission identifier using this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          occ_aircraft_mds: The aircraft Model Design Series designation of the aircraft occupying this
              slot.

          occ_start_time: Time the aircraft began occupying this slot, in ISO 8601 UTC format with
              millisecond precision.

          occ_tail_number: The tail number of the aircraft occupying this slot.

          occupied: Flag indicating if the slot is occupied.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          req_comment: Comments from the requester.

          req_initials: Initials of the person requesting the use of this slot. Use SYSTEM if this
              request is auto-generated by an auto-planning system.

          req_org: Short name of the organization requesting use of this slot.

          res_aircraft_mds: The aircraft Model Design Series designation of the aircraft this slot is
              reserved for.

          res_mission_id: Mission identifier reserving this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          res_reason: The reason the slot reservation was made.

          res_tail_number: The tail number of the aircraft this slot is reserved for.

          res_type: Indicates the type of reservation (e.g. M for Mission, A for Aircraft, O for
              Other).

          status: Current status of this slot (REQUESTED / APPROVED / DENIED / BLOCKED / OTHER).

          target_time: The desired time for aircraft action such as landing, take off, parking, etc.,
              in ISO 8601 UTC format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airfieldslotconsumption",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield_slot": id_airfield_slot,
                    "num_aircraft": num_aircraft,
                    "source": source,
                    "start_time": start_time,
                    "id": id,
                    "alt_arr_sortie_id": alt_arr_sortie_id,
                    "alt_dep_sortie_id": alt_dep_sortie_id,
                    "app_comment": app_comment,
                    "app_initials": app_initials,
                    "app_org": app_org,
                    "call_signs": call_signs,
                    "consumer": consumer,
                    "end_time": end_time,
                    "id_arr_sortie": id_arr_sortie,
                    "id_dep_sortie": id_dep_sortie,
                    "mission_id": mission_id,
                    "occ_aircraft_mds": occ_aircraft_mds,
                    "occ_start_time": occ_start_time,
                    "occ_tail_number": occ_tail_number,
                    "occupied": occupied,
                    "origin": origin,
                    "req_comment": req_comment,
                    "req_initials": req_initials,
                    "req_org": req_org,
                    "res_aircraft_mds": res_aircraft_mds,
                    "res_mission_id": res_mission_id,
                    "res_reason": res_reason,
                    "res_tail_number": res_tail_number,
                    "res_type": res_type,
                    "status": status,
                    "target_time": target_time,
                },
                airfield_slot_consumption_create_params.AirfieldSlotConsumptionCreateParams,
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
    ) -> AirfieldslotconsumptionFull:
        """
        Service operation to get a single airfieldslotconsumption record by its unique
        ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/airfieldslotconsumption/{id}",
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
                    airfield_slot_consumption_retrieve_params.AirfieldSlotConsumptionRetrieveParams,
                ),
            ),
            cast_to=AirfieldslotconsumptionFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_airfield_slot: str,
        num_aircraft: int,
        source: str,
        start_time: Union[str, datetime],
        body_id: str | NotGiven = NOT_GIVEN,
        alt_arr_sortie_id: str | NotGiven = NOT_GIVEN,
        alt_dep_sortie_id: str | NotGiven = NOT_GIVEN,
        app_comment: str | NotGiven = NOT_GIVEN,
        app_initials: str | NotGiven = NOT_GIVEN,
        app_org: str | NotGiven = NOT_GIVEN,
        call_signs: List[str] | NotGiven = NOT_GIVEN,
        consumer: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        id_arr_sortie: str | NotGiven = NOT_GIVEN,
        id_dep_sortie: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        occ_aircraft_mds: str | NotGiven = NOT_GIVEN,
        occ_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        occ_tail_number: str | NotGiven = NOT_GIVEN,
        occupied: bool | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        req_comment: str | NotGiven = NOT_GIVEN,
        req_initials: str | NotGiven = NOT_GIVEN,
        req_org: str | NotGiven = NOT_GIVEN,
        res_aircraft_mds: str | NotGiven = NOT_GIVEN,
        res_mission_id: str | NotGiven = NOT_GIVEN,
        res_reason: str | NotGiven = NOT_GIVEN,
        res_tail_number: str | NotGiven = NOT_GIVEN,
        res_type: str | NotGiven = NOT_GIVEN,
        status: Literal["REQUESTED", "APPROVED", "DENIED", "BLOCKED", "OTHER"] | NotGiven = NOT_GIVEN,
        target_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AirfieldSlotConsumption.

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

          id_airfield_slot: Unique identifier of the airfield slot for which this slot consumption record is
              referencing.

          num_aircraft: Number of aircraft using this slot for this time.

          source: Source of the data.

          start_time: The start of the slot window, in ISO 8601 UTC format.

          body_id: Unique identifier of the record, auto-generated by the system.

          alt_arr_sortie_id: Alternate identifier of the sortie arriving at the slot start time provided by
              the source.

          alt_dep_sortie_id: Alternate identifier of the sortie departing at the slot end time provided by
              the source.

          app_comment: Comments from the approver.

          app_initials: Initials of the person approving the use of this slot. Use SYSTEM if
              auto-approved without human involvement.

          app_org: Short name of the organization approving the use of this slot.

          call_signs: Array of call signs of the aircraft using this slot.

          consumer: Identifying name of the aircraft using this slot. Names are often Prior
              Permission Required (PPR) numbers or other similar human-readable identifiers.

          end_time: The end of the slot window, in ISO 8601 UTC format.

          id_arr_sortie: Unique identifier of the sortie arriving at the slot start time.

          id_dep_sortie: Unique identifier of the sortie departing at the slot end time.

          mission_id: Mission identifier using this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          occ_aircraft_mds: The aircraft Model Design Series designation of the aircraft occupying this
              slot.

          occ_start_time: Time the aircraft began occupying this slot, in ISO 8601 UTC format with
              millisecond precision.

          occ_tail_number: The tail number of the aircraft occupying this slot.

          occupied: Flag indicating if the slot is occupied.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          req_comment: Comments from the requester.

          req_initials: Initials of the person requesting the use of this slot. Use SYSTEM if this
              request is auto-generated by an auto-planning system.

          req_org: Short name of the organization requesting use of this slot.

          res_aircraft_mds: The aircraft Model Design Series designation of the aircraft this slot is
              reserved for.

          res_mission_id: Mission identifier reserving this slot according to Mobility Air Forces (MAF)
              Encode/Decode procedures.

          res_reason: The reason the slot reservation was made.

          res_tail_number: The tail number of the aircraft this slot is reserved for.

          res_type: Indicates the type of reservation (e.g. M for Mission, A for Aircraft, O for
              Other).

          status: Current status of this slot (REQUESTED / APPROVED / DENIED / BLOCKED / OTHER).

          target_time: The desired time for aircraft action such as landing, take off, parking, etc.,
              in ISO 8601 UTC format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/airfieldslotconsumption/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_airfield_slot": id_airfield_slot,
                    "num_aircraft": num_aircraft,
                    "source": source,
                    "start_time": start_time,
                    "body_id": body_id,
                    "alt_arr_sortie_id": alt_arr_sortie_id,
                    "alt_dep_sortie_id": alt_dep_sortie_id,
                    "app_comment": app_comment,
                    "app_initials": app_initials,
                    "app_org": app_org,
                    "call_signs": call_signs,
                    "consumer": consumer,
                    "end_time": end_time,
                    "id_arr_sortie": id_arr_sortie,
                    "id_dep_sortie": id_dep_sortie,
                    "mission_id": mission_id,
                    "occ_aircraft_mds": occ_aircraft_mds,
                    "occ_start_time": occ_start_time,
                    "occ_tail_number": occ_tail_number,
                    "occupied": occupied,
                    "origin": origin,
                    "req_comment": req_comment,
                    "req_initials": req_initials,
                    "req_org": req_org,
                    "res_aircraft_mds": res_aircraft_mds,
                    "res_mission_id": res_mission_id,
                    "res_reason": res_reason,
                    "res_tail_number": res_tail_number,
                    "res_type": res_type,
                    "status": status,
                    "target_time": target_time,
                },
                airfield_slot_consumption_update_params.AirfieldSlotConsumptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AirfieldslotconsumptionAbridged, AsyncOffsetPage[AirfieldslotconsumptionAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start of the slot window, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/airfieldslotconsumption",
            page=AsyncOffsetPage[AirfieldslotconsumptionAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airfield_slot_consumption_list_params.AirfieldSlotConsumptionListParams,
                ),
            ),
            model=AirfieldslotconsumptionAbridged,
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
        Service operation to delete an airfieldslotconsumption record specified by the
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
            f"/udl/airfieldslotconsumption/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The start of the slot window, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/airfieldslotconsumption/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airfield_slot_consumption_count_params.AirfieldSlotConsumptionCountParams,
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
    ) -> AirfieldSlotConsumptionQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/airfieldslotconsumption/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirfieldSlotConsumptionQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirfieldSlotConsumptionTupleResponse:
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

          start_time: The start of the slot window, in ISO 8601 UTC format. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/airfieldslotconsumption/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airfield_slot_consumption_tuple_params.AirfieldSlotConsumptionTupleParams,
                ),
            ),
            cast_to=AirfieldSlotConsumptionTupleResponse,
        )


class AirfieldSlotConsumptionsResourceWithRawResponse:
    def __init__(self, airfield_slot_consumptions: AirfieldSlotConsumptionsResource) -> None:
        self._airfield_slot_consumptions = airfield_slot_consumptions

        self.create = to_raw_response_wrapper(
            airfield_slot_consumptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            airfield_slot_consumptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            airfield_slot_consumptions.update,
        )
        self.list = to_raw_response_wrapper(
            airfield_slot_consumptions.list,
        )
        self.delete = to_raw_response_wrapper(
            airfield_slot_consumptions.delete,
        )
        self.count = to_raw_response_wrapper(
            airfield_slot_consumptions.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            airfield_slot_consumptions.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            airfield_slot_consumptions.tuple,
        )


class AsyncAirfieldSlotConsumptionsResourceWithRawResponse:
    def __init__(self, airfield_slot_consumptions: AsyncAirfieldSlotConsumptionsResource) -> None:
        self._airfield_slot_consumptions = airfield_slot_consumptions

        self.create = async_to_raw_response_wrapper(
            airfield_slot_consumptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            airfield_slot_consumptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            airfield_slot_consumptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            airfield_slot_consumptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            airfield_slot_consumptions.delete,
        )
        self.count = async_to_raw_response_wrapper(
            airfield_slot_consumptions.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            airfield_slot_consumptions.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            airfield_slot_consumptions.tuple,
        )


class AirfieldSlotConsumptionsResourceWithStreamingResponse:
    def __init__(self, airfield_slot_consumptions: AirfieldSlotConsumptionsResource) -> None:
        self._airfield_slot_consumptions = airfield_slot_consumptions

        self.create = to_streamed_response_wrapper(
            airfield_slot_consumptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            airfield_slot_consumptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            airfield_slot_consumptions.update,
        )
        self.list = to_streamed_response_wrapper(
            airfield_slot_consumptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            airfield_slot_consumptions.delete,
        )
        self.count = to_streamed_response_wrapper(
            airfield_slot_consumptions.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            airfield_slot_consumptions.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            airfield_slot_consumptions.tuple,
        )


class AsyncAirfieldSlotConsumptionsResourceWithStreamingResponse:
    def __init__(self, airfield_slot_consumptions: AsyncAirfieldSlotConsumptionsResource) -> None:
        self._airfield_slot_consumptions = airfield_slot_consumptions

        self.create = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            airfield_slot_consumptions.tuple,
        )
