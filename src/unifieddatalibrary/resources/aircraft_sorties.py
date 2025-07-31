# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import aircraft_sorty_tuple_params, aircraft_sorty_update_params, aircraft_sorty_retrieve_params
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
from .._base_client import make_request_options
from ..types.shared.aircraftsortie_full import AircraftsortieFull
from ..types.aircraft_sorty_tuple_response import AircraftSortyTupleResponse
from ..types.aircraft_sorty_queryhelp_response import AircraftSortyQueryhelpResponse

__all__ = ["AircraftSortiesResource", "AsyncAircraftSortiesResource"]


class AircraftSortiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AircraftSortiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AircraftSortiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AircraftSortiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AircraftSortiesResourceWithStreamingResponse(self)

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
    ) -> AircraftsortieFull:
        """
        Service operation to get a single AircraftSortie record by its unique ID passed
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
            f"/udl/aircraftsortie/{id}",
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
                    aircraft_sorty_retrieve_params.AircraftSortyRetrieveParams,
                ),
            ),
            cast_to=AircraftsortieFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        planned_dep_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        actual_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_block_in_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_block_out_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        aircraft_adsb: str | NotGiven = NOT_GIVEN,
        aircraft_alt_id: str | NotGiven = NOT_GIVEN,
        aircraft_event: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        aircraft_remarks: str | NotGiven = NOT_GIVEN,
        alert_status: int | NotGiven = NOT_GIVEN,
        alert_status_code: str | NotGiven = NOT_GIVEN,
        amc_msn_num: str | NotGiven = NOT_GIVEN,
        amc_msn_type: str | NotGiven = NOT_GIVEN,
        arr_faa: str | NotGiven = NOT_GIVEN,
        arr_iata: str | NotGiven = NOT_GIVEN,
        arr_icao: str | NotGiven = NOT_GIVEN,
        arr_itinerary: int | NotGiven = NOT_GIVEN,
        arr_purpose_code: str | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_config: str | NotGiven = NOT_GIVEN,
        commander_name: str | NotGiven = NOT_GIVEN,
        current_state: str | NotGiven = NOT_GIVEN,
        delay_code: str | NotGiven = NOT_GIVEN,
        dep_faa: str | NotGiven = NOT_GIVEN,
        dep_iata: str | NotGiven = NOT_GIVEN,
        dep_icao: str | NotGiven = NOT_GIVEN,
        dep_itinerary: int | NotGiven = NOT_GIVEN,
        dep_purpose_code: str | NotGiven = NOT_GIVEN,
        dhd: Union[str, datetime] | NotGiven = NOT_GIVEN,
        dhd_reason: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_block_in_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_block_out_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flight_time: float | NotGiven = NOT_GIVEN,
        fm_desk_num: str | NotGiven = NOT_GIVEN,
        fm_name: str | NotGiven = NOT_GIVEN,
        fuel_req: float | NotGiven = NOT_GIVEN,
        gnd_time: float | NotGiven = NOT_GIVEN,
        id_aircraft: str | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        jcs_priority: str | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        line_number: int | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        mission_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        objective_remarks: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sortie_id: str | NotGiven = NOT_GIVEN,
        oxy_on_crew: float | NotGiven = NOT_GIVEN,
        oxy_on_pax: float | NotGiven = NOT_GIVEN,
        oxy_req_crew: float | NotGiven = NOT_GIVEN,
        oxy_req_pax: float | NotGiven = NOT_GIVEN,
        parking_loc: str | NotGiven = NOT_GIVEN,
        passengers: int | NotGiven = NOT_GIVEN,
        planned_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ppr_status: Literal["NOT REQUIRED", "REQUIRED NOT REQUESTED", "GRANTED", "PENDING"] | NotGiven = NOT_GIVEN,
        primary_scl: str | NotGiven = NOT_GIVEN,
        req_config: str | NotGiven = NOT_GIVEN,
        result_remarks: str | NotGiven = NOT_GIVEN,
        rvn_req: Literal["N", "R", "C6", "R6"] | NotGiven = NOT_GIVEN,
        schedule_remarks: str | NotGiven = NOT_GIVEN,
        secondary_scl: str | NotGiven = NOT_GIVEN,
        soe: str | NotGiven = NOT_GIVEN,
        sortie_date: Union[str, date] | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AircraftSortie.

        A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          planned_dep_time: The scheduled time that the Aircraft sortie is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          actual_arr_time: The actual arrival time, in ISO 8601 UTC format with millisecond precision.

          actual_block_in_time: The actual time the Aircraft comes to a complete stop in its parking position,
              in ISO 8601 UTC format with millisecond precision.

          actual_block_out_time: The actual time the Aircraft begins to taxi from its parking position, in ISO
              8601 UTC format with millisecond precision.

          actual_dep_time: The actual departure time, in ISO 8601 UTC format.

          aircraft_adsb: The Automatic Dependent Surveillance-Broadcast (ADS-B) device identifier.

          aircraft_alt_id: Alternate Aircraft Identifier provided by source.

          aircraft_event: Aircraft event text.

          aircraft_mds: The aircraft Model Design Series designation assigned to this sortie.

          aircraft_remarks: Remarks concerning the aircraft.

          alert_status: The amount of time allowed between launch order and takeoff, in seconds.

          alert_status_code: The Alert Status code.

          amc_msn_num: The Air Mobility Command (AMC) mission number of the sortie.

          amc_msn_type: The type of mission (e.g. SAAM, CHNL, etc.).

          arr_faa: The arrival Federal Aviation Administration (FAA) code of this sortie.

          arr_iata: The arrival International Aviation Transport Association (IATA) code of this
              sortie.

          arr_icao: The arrival International Civil Aviation Organization (ICAO) of this sortie.

          arr_itinerary: The itinerary identifier of the arrival location.

          arr_purpose_code: Purpose code at the arrival location of this sortie.

          call_sign: The call sign assigned to the aircraft on this sortie.

          cargo_config: Description of the cargo configuration (e.g. C-1, C-2, C-3, DV-1, DV-2, AE-1,
              etc.) currently on board the aircraft. Configuration meanings are determined by
              the data source.

          commander_name: The last name of the aircraft commander.

          current_state: The current state of this sortie.

          delay_code: The primary delay code.

          dep_faa: The departure Federal Aviation Administration (FAA) code of this sortie.

          dep_iata: The departure International Aviation Transport Association (IATA) code of this
              sortie.

          dep_icao: The departure International Civil Aviation Organization (ICAO) of this sortie.

          dep_itinerary: The itinerary identifier of the departure location.

          dep_purpose_code: Purpose code at the departure location of this sortie.

          dhd: Due home date by which the aircraft must return to its home station, in ISO 8601
              UTC format with millisecond precision.

          dhd_reason: Reason the aircraft must return to home station by its due home date.

          est_arr_time: The current estimated time that the Aircraft is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          est_block_in_time: The estimated time the Aircraft will come to a complete stop in its parking
              position, in ISO 8601 UTC format with millisecond precision.

          est_block_out_time: The estimated time the Aircraft will begin to taxi from its parking position, in
              ISO 8601 UTC format with millisecond precision.

          est_dep_time: The current estimated time that the Aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          flight_time: The planned flight time for this sortie, in minutes.

          fm_desk_num: Desk phone number of the flight manager assigned to the sortie. Null when no
              flight manager is assigned.

          fm_name: Last name of the flight manager assigned to the sortie. Null when no flight
              manager is assigned.

          fuel_req: Mass of fuel required for this leg of the sortie, in kilograms.

          gnd_time: Scheduled ground time, in minutes.

          id_aircraft: Unique identifier of the aircraft.

          id_mission: The unique identifier of the mission to which this sortie is assigned.

          jcs_priority: Joint Chiefs of Staff priority of this sortie.

          leg_num: The leg number of this sortie.

          line_number: The external system line number of this sortie.

          mission_id: The mission ID according to the source system.

          mission_update: Time the associated mission data was last updated in relation to the aircraft
              assignment, in ISO 8601 UTC format with millisecond precision. If this time is
              coming from an external system, it may not sync with the latest mission time
              associated to this record.

          objective_remarks: Remarks concerning the sortie objective.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sortie_id: The sortie identifier provided by the originating source.

          oxy_on_crew: Liquid oxygen onboard the aircraft for the crew compartment, in liters.

          oxy_on_pax: Liquid oxygen onboard the aircraft for the troop compartment, in liters.

          oxy_req_crew: Liquid oxygen required on the aircraft for the crew compartment, in liters.

          oxy_req_pax: Liquid oxygen required on the aircraft for the troop compartment, in liters.

          parking_loc: The POI parking location.

          passengers: The number of passengers tasked for this sortie.

          planned_arr_time: The scheduled time that the Aircraft sortie is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          ppr_status: The prior permission required (PPR) status.

          primary_scl: The planned primary Standard Conventional Load of the aircraft for this sortie.

          req_config: Aircraft configuration required for the mission.

          result_remarks: Remarks concerning the results of this sortie.

          rvn_req: Type of Ravens required for this sortie (N - None, R - Raven (Security Team)
              required, C6 - Consider ravens (Ground time over 6 hours), R6 - Ravens required
              (Ground time over 6 hours)).

          schedule_remarks: Remarks concerning the schedule.

          secondary_scl: The planned secondary Standard Conventional Load of the aircraft for this
              sortie.

          soe: Indicates the group responsible for recording the completion time of the next
              event in the sequence of events assigned to this sortie (e.g. OPS - Operations,
              MX - Maintenance, TR - Transportation, etc.).

          sortie_date: The scheduled UTC date for this sortie, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          tail_number: The tail number of the aircraft assigned to this sortie.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/aircraftsortie/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "planned_dep_time": planned_dep_time,
                    "source": source,
                    "body_id": body_id,
                    "actual_arr_time": actual_arr_time,
                    "actual_block_in_time": actual_block_in_time,
                    "actual_block_out_time": actual_block_out_time,
                    "actual_dep_time": actual_dep_time,
                    "aircraft_adsb": aircraft_adsb,
                    "aircraft_alt_id": aircraft_alt_id,
                    "aircraft_event": aircraft_event,
                    "aircraft_mds": aircraft_mds,
                    "aircraft_remarks": aircraft_remarks,
                    "alert_status": alert_status,
                    "alert_status_code": alert_status_code,
                    "amc_msn_num": amc_msn_num,
                    "amc_msn_type": amc_msn_type,
                    "arr_faa": arr_faa,
                    "arr_iata": arr_iata,
                    "arr_icao": arr_icao,
                    "arr_itinerary": arr_itinerary,
                    "arr_purpose_code": arr_purpose_code,
                    "call_sign": call_sign,
                    "cargo_config": cargo_config,
                    "commander_name": commander_name,
                    "current_state": current_state,
                    "delay_code": delay_code,
                    "dep_faa": dep_faa,
                    "dep_iata": dep_iata,
                    "dep_icao": dep_icao,
                    "dep_itinerary": dep_itinerary,
                    "dep_purpose_code": dep_purpose_code,
                    "dhd": dhd,
                    "dhd_reason": dhd_reason,
                    "est_arr_time": est_arr_time,
                    "est_block_in_time": est_block_in_time,
                    "est_block_out_time": est_block_out_time,
                    "est_dep_time": est_dep_time,
                    "flight_time": flight_time,
                    "fm_desk_num": fm_desk_num,
                    "fm_name": fm_name,
                    "fuel_req": fuel_req,
                    "gnd_time": gnd_time,
                    "id_aircraft": id_aircraft,
                    "id_mission": id_mission,
                    "jcs_priority": jcs_priority,
                    "leg_num": leg_num,
                    "line_number": line_number,
                    "mission_id": mission_id,
                    "mission_update": mission_update,
                    "objective_remarks": objective_remarks,
                    "origin": origin,
                    "orig_sortie_id": orig_sortie_id,
                    "oxy_on_crew": oxy_on_crew,
                    "oxy_on_pax": oxy_on_pax,
                    "oxy_req_crew": oxy_req_crew,
                    "oxy_req_pax": oxy_req_pax,
                    "parking_loc": parking_loc,
                    "passengers": passengers,
                    "planned_arr_time": planned_arr_time,
                    "ppr_status": ppr_status,
                    "primary_scl": primary_scl,
                    "req_config": req_config,
                    "result_remarks": result_remarks,
                    "rvn_req": rvn_req,
                    "schedule_remarks": schedule_remarks,
                    "secondary_scl": secondary_scl,
                    "soe": soe,
                    "sortie_date": sortie_date,
                    "tail_number": tail_number,
                },
                aircraft_sorty_update_params.AircraftSortyUpdateParams,
            ),
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
    ) -> AircraftSortyQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/aircraftsortie/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AircraftSortyQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        planned_dep_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AircraftSortyTupleResponse:
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

          planned_dep_time: The scheduled time that the Aircraft sortie is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/aircraftsortie/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "planned_dep_time": planned_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    aircraft_sorty_tuple_params.AircraftSortyTupleParams,
                ),
            ),
            cast_to=AircraftSortyTupleResponse,
        )


class AsyncAircraftSortiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAircraftSortiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAircraftSortiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAircraftSortiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAircraftSortiesResourceWithStreamingResponse(self)

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
    ) -> AircraftsortieFull:
        """
        Service operation to get a single AircraftSortie record by its unique ID passed
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
            f"/udl/aircraftsortie/{id}",
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
                    aircraft_sorty_retrieve_params.AircraftSortyRetrieveParams,
                ),
            ),
            cast_to=AircraftsortieFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        planned_dep_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        actual_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_block_in_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_block_out_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        aircraft_adsb: str | NotGiven = NOT_GIVEN,
        aircraft_alt_id: str | NotGiven = NOT_GIVEN,
        aircraft_event: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        aircraft_remarks: str | NotGiven = NOT_GIVEN,
        alert_status: int | NotGiven = NOT_GIVEN,
        alert_status_code: str | NotGiven = NOT_GIVEN,
        amc_msn_num: str | NotGiven = NOT_GIVEN,
        amc_msn_type: str | NotGiven = NOT_GIVEN,
        arr_faa: str | NotGiven = NOT_GIVEN,
        arr_iata: str | NotGiven = NOT_GIVEN,
        arr_icao: str | NotGiven = NOT_GIVEN,
        arr_itinerary: int | NotGiven = NOT_GIVEN,
        arr_purpose_code: str | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_config: str | NotGiven = NOT_GIVEN,
        commander_name: str | NotGiven = NOT_GIVEN,
        current_state: str | NotGiven = NOT_GIVEN,
        delay_code: str | NotGiven = NOT_GIVEN,
        dep_faa: str | NotGiven = NOT_GIVEN,
        dep_iata: str | NotGiven = NOT_GIVEN,
        dep_icao: str | NotGiven = NOT_GIVEN,
        dep_itinerary: int | NotGiven = NOT_GIVEN,
        dep_purpose_code: str | NotGiven = NOT_GIVEN,
        dhd: Union[str, datetime] | NotGiven = NOT_GIVEN,
        dhd_reason: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_block_in_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_block_out_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flight_time: float | NotGiven = NOT_GIVEN,
        fm_desk_num: str | NotGiven = NOT_GIVEN,
        fm_name: str | NotGiven = NOT_GIVEN,
        fuel_req: float | NotGiven = NOT_GIVEN,
        gnd_time: float | NotGiven = NOT_GIVEN,
        id_aircraft: str | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        jcs_priority: str | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        line_number: int | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        mission_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        objective_remarks: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_sortie_id: str | NotGiven = NOT_GIVEN,
        oxy_on_crew: float | NotGiven = NOT_GIVEN,
        oxy_on_pax: float | NotGiven = NOT_GIVEN,
        oxy_req_crew: float | NotGiven = NOT_GIVEN,
        oxy_req_pax: float | NotGiven = NOT_GIVEN,
        parking_loc: str | NotGiven = NOT_GIVEN,
        passengers: int | NotGiven = NOT_GIVEN,
        planned_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ppr_status: Literal["NOT REQUIRED", "REQUIRED NOT REQUESTED", "GRANTED", "PENDING"] | NotGiven = NOT_GIVEN,
        primary_scl: str | NotGiven = NOT_GIVEN,
        req_config: str | NotGiven = NOT_GIVEN,
        result_remarks: str | NotGiven = NOT_GIVEN,
        rvn_req: Literal["N", "R", "C6", "R6"] | NotGiven = NOT_GIVEN,
        schedule_remarks: str | NotGiven = NOT_GIVEN,
        secondary_scl: str | NotGiven = NOT_GIVEN,
        soe: str | NotGiven = NOT_GIVEN,
        sortie_date: Union[str, date] | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AircraftSortie.

        A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

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

          planned_dep_time: The scheduled time that the Aircraft sortie is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          actual_arr_time: The actual arrival time, in ISO 8601 UTC format with millisecond precision.

          actual_block_in_time: The actual time the Aircraft comes to a complete stop in its parking position,
              in ISO 8601 UTC format with millisecond precision.

          actual_block_out_time: The actual time the Aircraft begins to taxi from its parking position, in ISO
              8601 UTC format with millisecond precision.

          actual_dep_time: The actual departure time, in ISO 8601 UTC format.

          aircraft_adsb: The Automatic Dependent Surveillance-Broadcast (ADS-B) device identifier.

          aircraft_alt_id: Alternate Aircraft Identifier provided by source.

          aircraft_event: Aircraft event text.

          aircraft_mds: The aircraft Model Design Series designation assigned to this sortie.

          aircraft_remarks: Remarks concerning the aircraft.

          alert_status: The amount of time allowed between launch order and takeoff, in seconds.

          alert_status_code: The Alert Status code.

          amc_msn_num: The Air Mobility Command (AMC) mission number of the sortie.

          amc_msn_type: The type of mission (e.g. SAAM, CHNL, etc.).

          arr_faa: The arrival Federal Aviation Administration (FAA) code of this sortie.

          arr_iata: The arrival International Aviation Transport Association (IATA) code of this
              sortie.

          arr_icao: The arrival International Civil Aviation Organization (ICAO) of this sortie.

          arr_itinerary: The itinerary identifier of the arrival location.

          arr_purpose_code: Purpose code at the arrival location of this sortie.

          call_sign: The call sign assigned to the aircraft on this sortie.

          cargo_config: Description of the cargo configuration (e.g. C-1, C-2, C-3, DV-1, DV-2, AE-1,
              etc.) currently on board the aircraft. Configuration meanings are determined by
              the data source.

          commander_name: The last name of the aircraft commander.

          current_state: The current state of this sortie.

          delay_code: The primary delay code.

          dep_faa: The departure Federal Aviation Administration (FAA) code of this sortie.

          dep_iata: The departure International Aviation Transport Association (IATA) code of this
              sortie.

          dep_icao: The departure International Civil Aviation Organization (ICAO) of this sortie.

          dep_itinerary: The itinerary identifier of the departure location.

          dep_purpose_code: Purpose code at the departure location of this sortie.

          dhd: Due home date by which the aircraft must return to its home station, in ISO 8601
              UTC format with millisecond precision.

          dhd_reason: Reason the aircraft must return to home station by its due home date.

          est_arr_time: The current estimated time that the Aircraft is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          est_block_in_time: The estimated time the Aircraft will come to a complete stop in its parking
              position, in ISO 8601 UTC format with millisecond precision.

          est_block_out_time: The estimated time the Aircraft will begin to taxi from its parking position, in
              ISO 8601 UTC format with millisecond precision.

          est_dep_time: The current estimated time that the Aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          flight_time: The planned flight time for this sortie, in minutes.

          fm_desk_num: Desk phone number of the flight manager assigned to the sortie. Null when no
              flight manager is assigned.

          fm_name: Last name of the flight manager assigned to the sortie. Null when no flight
              manager is assigned.

          fuel_req: Mass of fuel required for this leg of the sortie, in kilograms.

          gnd_time: Scheduled ground time, in minutes.

          id_aircraft: Unique identifier of the aircraft.

          id_mission: The unique identifier of the mission to which this sortie is assigned.

          jcs_priority: Joint Chiefs of Staff priority of this sortie.

          leg_num: The leg number of this sortie.

          line_number: The external system line number of this sortie.

          mission_id: The mission ID according to the source system.

          mission_update: Time the associated mission data was last updated in relation to the aircraft
              assignment, in ISO 8601 UTC format with millisecond precision. If this time is
              coming from an external system, it may not sync with the latest mission time
              associated to this record.

          objective_remarks: Remarks concerning the sortie objective.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_sortie_id: The sortie identifier provided by the originating source.

          oxy_on_crew: Liquid oxygen onboard the aircraft for the crew compartment, in liters.

          oxy_on_pax: Liquid oxygen onboard the aircraft for the troop compartment, in liters.

          oxy_req_crew: Liquid oxygen required on the aircraft for the crew compartment, in liters.

          oxy_req_pax: Liquid oxygen required on the aircraft for the troop compartment, in liters.

          parking_loc: The POI parking location.

          passengers: The number of passengers tasked for this sortie.

          planned_arr_time: The scheduled time that the Aircraft sortie is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          ppr_status: The prior permission required (PPR) status.

          primary_scl: The planned primary Standard Conventional Load of the aircraft for this sortie.

          req_config: Aircraft configuration required for the mission.

          result_remarks: Remarks concerning the results of this sortie.

          rvn_req: Type of Ravens required for this sortie (N - None, R - Raven (Security Team)
              required, C6 - Consider ravens (Ground time over 6 hours), R6 - Ravens required
              (Ground time over 6 hours)).

          schedule_remarks: Remarks concerning the schedule.

          secondary_scl: The planned secondary Standard Conventional Load of the aircraft for this
              sortie.

          soe: Indicates the group responsible for recording the completion time of the next
              event in the sequence of events assigned to this sortie (e.g. OPS - Operations,
              MX - Maintenance, TR - Transportation, etc.).

          sortie_date: The scheduled UTC date for this sortie, in ISO 8601 date-only format (ex.
              YYYY-MM-DD).

          tail_number: The tail number of the aircraft assigned to this sortie.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/aircraftsortie/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "planned_dep_time": planned_dep_time,
                    "source": source,
                    "body_id": body_id,
                    "actual_arr_time": actual_arr_time,
                    "actual_block_in_time": actual_block_in_time,
                    "actual_block_out_time": actual_block_out_time,
                    "actual_dep_time": actual_dep_time,
                    "aircraft_adsb": aircraft_adsb,
                    "aircraft_alt_id": aircraft_alt_id,
                    "aircraft_event": aircraft_event,
                    "aircraft_mds": aircraft_mds,
                    "aircraft_remarks": aircraft_remarks,
                    "alert_status": alert_status,
                    "alert_status_code": alert_status_code,
                    "amc_msn_num": amc_msn_num,
                    "amc_msn_type": amc_msn_type,
                    "arr_faa": arr_faa,
                    "arr_iata": arr_iata,
                    "arr_icao": arr_icao,
                    "arr_itinerary": arr_itinerary,
                    "arr_purpose_code": arr_purpose_code,
                    "call_sign": call_sign,
                    "cargo_config": cargo_config,
                    "commander_name": commander_name,
                    "current_state": current_state,
                    "delay_code": delay_code,
                    "dep_faa": dep_faa,
                    "dep_iata": dep_iata,
                    "dep_icao": dep_icao,
                    "dep_itinerary": dep_itinerary,
                    "dep_purpose_code": dep_purpose_code,
                    "dhd": dhd,
                    "dhd_reason": dhd_reason,
                    "est_arr_time": est_arr_time,
                    "est_block_in_time": est_block_in_time,
                    "est_block_out_time": est_block_out_time,
                    "est_dep_time": est_dep_time,
                    "flight_time": flight_time,
                    "fm_desk_num": fm_desk_num,
                    "fm_name": fm_name,
                    "fuel_req": fuel_req,
                    "gnd_time": gnd_time,
                    "id_aircraft": id_aircraft,
                    "id_mission": id_mission,
                    "jcs_priority": jcs_priority,
                    "leg_num": leg_num,
                    "line_number": line_number,
                    "mission_id": mission_id,
                    "mission_update": mission_update,
                    "objective_remarks": objective_remarks,
                    "origin": origin,
                    "orig_sortie_id": orig_sortie_id,
                    "oxy_on_crew": oxy_on_crew,
                    "oxy_on_pax": oxy_on_pax,
                    "oxy_req_crew": oxy_req_crew,
                    "oxy_req_pax": oxy_req_pax,
                    "parking_loc": parking_loc,
                    "passengers": passengers,
                    "planned_arr_time": planned_arr_time,
                    "ppr_status": ppr_status,
                    "primary_scl": primary_scl,
                    "req_config": req_config,
                    "result_remarks": result_remarks,
                    "rvn_req": rvn_req,
                    "schedule_remarks": schedule_remarks,
                    "secondary_scl": secondary_scl,
                    "soe": soe,
                    "sortie_date": sortie_date,
                    "tail_number": tail_number,
                },
                aircraft_sorty_update_params.AircraftSortyUpdateParams,
            ),
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
    ) -> AircraftSortyQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/aircraftsortie/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AircraftSortyQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        planned_dep_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AircraftSortyTupleResponse:
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

          planned_dep_time: The scheduled time that the Aircraft sortie is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/aircraftsortie/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "planned_dep_time": planned_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    aircraft_sorty_tuple_params.AircraftSortyTupleParams,
                ),
            ),
            cast_to=AircraftSortyTupleResponse,
        )


class AircraftSortiesResourceWithRawResponse:
    def __init__(self, aircraft_sorties: AircraftSortiesResource) -> None:
        self._aircraft_sorties = aircraft_sorties

        self.retrieve = to_raw_response_wrapper(
            aircraft_sorties.retrieve,
        )
        self.update = to_raw_response_wrapper(
            aircraft_sorties.update,
        )
        self.queryhelp = to_raw_response_wrapper(
            aircraft_sorties.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            aircraft_sorties.tuple,
        )


class AsyncAircraftSortiesResourceWithRawResponse:
    def __init__(self, aircraft_sorties: AsyncAircraftSortiesResource) -> None:
        self._aircraft_sorties = aircraft_sorties

        self.retrieve = async_to_raw_response_wrapper(
            aircraft_sorties.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            aircraft_sorties.update,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            aircraft_sorties.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            aircraft_sorties.tuple,
        )


class AircraftSortiesResourceWithStreamingResponse:
    def __init__(self, aircraft_sorties: AircraftSortiesResource) -> None:
        self._aircraft_sorties = aircraft_sorties

        self.retrieve = to_streamed_response_wrapper(
            aircraft_sorties.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            aircraft_sorties.update,
        )
        self.queryhelp = to_streamed_response_wrapper(
            aircraft_sorties.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            aircraft_sorties.tuple,
        )


class AsyncAircraftSortiesResourceWithStreamingResponse:
    def __init__(self, aircraft_sorties: AsyncAircraftSortiesResource) -> None:
        self._aircraft_sorties = aircraft_sorties

        self.retrieve = async_to_streamed_response_wrapper(
            aircraft_sorties.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            aircraft_sorties.update,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            aircraft_sorties.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            aircraft_sorties.tuple,
        )
