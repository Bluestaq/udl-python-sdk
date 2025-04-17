# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import airfieldslot_tuple_params, airfieldslot_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.airfieldslot_full import AirfieldslotFull
from ..types.airfieldslot_tuple_response import AirfieldslotTupleResponse

__all__ = ["AirfieldslotsResource", "AsyncAirfieldslotsResource"]


class AirfieldslotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AirfieldslotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirfieldslotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirfieldslotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirfieldslotsResourceWithStreamingResponse(self)

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
    ) -> AirfieldslotFull:
        """
        Service operation to get a single airfieldslot record by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/airfieldslot/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirfieldslotFull,
        )

    def update(
        self,
        path_id: str,
        *,
        airfield_name: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        ac_slot_cat: Literal["WIDE", "NARROW", "HELO", "ALL", "OTHER"] | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        capacity: int | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        min_separation: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        type: Literal["WORKING", "PARKING", "TAKEOFF", "LANDING", "OTHER"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single airfieldslot record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          airfield_name: The name of the airfield where this slot is located.

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

          name: Name of this slot.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          ac_slot_cat: Largest category of aircraft supported in this slot (WIDE, NARROW, HELO, ALL,
              OTHER).

          alt_airfield_id: Alternate airfield identifier provided by the source.

          capacity: Number of aircraft that can fit in this slot at the same time.

          end_time: Latest zulu time this slot is available based on daily standard hours. Not
              applicable to slots with type PARKING. Abnormal hours, such as holidays, should
              be marked via the AirfieldSlotConsumption schema.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield.

          id_airfield: Unique identifier of the Airfield for which this slot information applies.

          min_separation: Minimum time that must elapse between different aircraft leaving and entering
              this slot, in minutes.

          notes: Optional notes/comments for this airfield slot.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          start_time: Zulu time this slot is first available based on daily standard hours. Not
              applicable to slots with type PARKING. Abnormal hours, such as holidays, should
              be marked via the AirfieldSlotConsumption schema.

          type: Designates how this slot can be used (WORKING, PARKING, TAKEOFF, LANDING,
              OTHER).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/airfieldslot/{path_id}",
            body=maybe_transform(
                {
                    "airfield_name": airfield_name,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "ac_slot_cat": ac_slot_cat,
                    "alt_airfield_id": alt_airfield_id,
                    "capacity": capacity,
                    "end_time": end_time,
                    "icao": icao,
                    "id_airfield": id_airfield,
                    "min_separation": min_separation,
                    "notes": notes,
                    "origin": origin,
                    "start_time": start_time,
                    "type": type,
                },
                airfieldslot_update_params.AirfieldslotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Service operation to delete an airfieldslot record specified by the passed ID
        path parameter. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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
            f"/udl/airfieldslot/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
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
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/airfieldslot/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            "/udl/airfieldslot/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirfieldslotTupleResponse:
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
            "/udl/airfieldslot/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"columns": columns}, airfieldslot_tuple_params.AirfieldslotTupleParams),
            ),
            cast_to=AirfieldslotTupleResponse,
        )


class AsyncAirfieldslotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAirfieldslotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirfieldslotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirfieldslotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsivilli-bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirfieldslotsResourceWithStreamingResponse(self)

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
    ) -> AirfieldslotFull:
        """
        Service operation to get a single airfieldslot record by its unique ID passed as
        a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/airfieldslot/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirfieldslotFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        airfield_name: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        ac_slot_cat: Literal["WIDE", "NARROW", "HELO", "ALL", "OTHER"] | NotGiven = NOT_GIVEN,
        alt_airfield_id: str | NotGiven = NOT_GIVEN,
        capacity: int | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        icao: str | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        min_separation: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        type: Literal["WORKING", "PARKING", "TAKEOFF", "LANDING", "OTHER"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single airfieldslot record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          airfield_name: The name of the airfield where this slot is located.

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

          name: Name of this slot.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          ac_slot_cat: Largest category of aircraft supported in this slot (WIDE, NARROW, HELO, ALL,
              OTHER).

          alt_airfield_id: Alternate airfield identifier provided by the source.

          capacity: Number of aircraft that can fit in this slot at the same time.

          end_time: Latest zulu time this slot is available based on daily standard hours. Not
              applicable to slots with type PARKING. Abnormal hours, such as holidays, should
              be marked via the AirfieldSlotConsumption schema.

          icao: The International Civil Aviation Organization (ICAO) code of the airfield.

          id_airfield: Unique identifier of the Airfield for which this slot information applies.

          min_separation: Minimum time that must elapse between different aircraft leaving and entering
              this slot, in minutes.

          notes: Optional notes/comments for this airfield slot.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          start_time: Zulu time this slot is first available based on daily standard hours. Not
              applicable to slots with type PARKING. Abnormal hours, such as holidays, should
              be marked via the AirfieldSlotConsumption schema.

          type: Designates how this slot can be used (WORKING, PARKING, TAKEOFF, LANDING,
              OTHER).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/airfieldslot/{path_id}",
            body=await async_maybe_transform(
                {
                    "airfield_name": airfield_name,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "ac_slot_cat": ac_slot_cat,
                    "alt_airfield_id": alt_airfield_id,
                    "capacity": capacity,
                    "end_time": end_time,
                    "icao": icao,
                    "id_airfield": id_airfield,
                    "min_separation": min_separation,
                    "notes": notes,
                    "origin": origin,
                    "start_time": start_time,
                    "type": type,
                },
                airfieldslot_update_params.AirfieldslotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Service operation to delete an airfieldslot record specified by the passed ID
        path parameter. A specific role is required to perform this service operation.
        Please contact the UDL team for assistance.

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
            f"/udl/airfieldslot/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
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
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/airfieldslot/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            "/udl/airfieldslot/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirfieldslotTupleResponse:
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
            "/udl/airfieldslot/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"columns": columns}, airfieldslot_tuple_params.AirfieldslotTupleParams
                ),
            ),
            cast_to=AirfieldslotTupleResponse,
        )


class AirfieldslotsResourceWithRawResponse:
    def __init__(self, airfieldslots: AirfieldslotsResource) -> None:
        self._airfieldslots = airfieldslots

        self.retrieve = to_raw_response_wrapper(
            airfieldslots.retrieve,
        )
        self.update = to_raw_response_wrapper(
            airfieldslots.update,
        )
        self.delete = to_raw_response_wrapper(
            airfieldslots.delete,
        )
        self.count = to_raw_response_wrapper(
            airfieldslots.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            airfieldslots.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            airfieldslots.tuple,
        )


class AsyncAirfieldslotsResourceWithRawResponse:
    def __init__(self, airfieldslots: AsyncAirfieldslotsResource) -> None:
        self._airfieldslots = airfieldslots

        self.retrieve = async_to_raw_response_wrapper(
            airfieldslots.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            airfieldslots.update,
        )
        self.delete = async_to_raw_response_wrapper(
            airfieldslots.delete,
        )
        self.count = async_to_raw_response_wrapper(
            airfieldslots.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            airfieldslots.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            airfieldslots.tuple,
        )


class AirfieldslotsResourceWithStreamingResponse:
    def __init__(self, airfieldslots: AirfieldslotsResource) -> None:
        self._airfieldslots = airfieldslots

        self.retrieve = to_streamed_response_wrapper(
            airfieldslots.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            airfieldslots.update,
        )
        self.delete = to_streamed_response_wrapper(
            airfieldslots.delete,
        )
        self.count = to_streamed_response_wrapper(
            airfieldslots.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            airfieldslots.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            airfieldslots.tuple,
        )


class AsyncAirfieldslotsResourceWithStreamingResponse:
    def __init__(self, airfieldslots: AsyncAirfieldslotsResource) -> None:
        self._airfieldslots = airfieldslots

        self.retrieve = async_to_streamed_response_wrapper(
            airfieldslots.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            airfieldslots.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            airfieldslots.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            airfieldslots.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            airfieldslots.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            airfieldslots.tuple,
        )
