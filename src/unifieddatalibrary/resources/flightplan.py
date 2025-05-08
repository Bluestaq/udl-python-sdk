# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    flightplan_list_params,
    flightplan_count_params,
    flightplan_tuple_params,
    flightplan_create_params,
    flightplan_update_params,
    flightplan_retrieve_params,
    flightplan_unvalidated_publish_params,
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
from ..types.flight_plan_abridged import FlightPlanAbridged
from ..types.shared.flight_plan_full import FlightPlanFull
from ..types.flightplan_tuple_response import FlightplanTupleResponse

__all__ = ["FlightplanResource", "AsyncFlightplanResource"]


class FlightplanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlightplanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FlightplanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlightplanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return FlightplanResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        arr_airfield: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dep_airfield: str,
        gen_ts: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_refuel_events: Iterable[flightplan_create_params.AirRefuelEvent] | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        app_landing_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate1: str | NotGiven = NOT_GIVEN,
        arr_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate2: str | NotGiven = NOT_GIVEN,
        arr_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        arr_ice_fuel: float | NotGiven = NOT_GIVEN,
        arr_runway: str | NotGiven = NOT_GIVEN,
        atc_addresses: List[str] | NotGiven = NOT_GIVEN,
        avg_temp_dev: float | NotGiven = NOT_GIVEN,
        burned_fuel: float | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_remark: str | NotGiven = NOT_GIVEN,
        climb_fuel: float | NotGiven = NOT_GIVEN,
        climb_time: str | NotGiven = NOT_GIVEN,
        contingency_fuel: float | NotGiven = NOT_GIVEN,
        country_codes: List[str] | NotGiven = NOT_GIVEN,
        dep_alternate: str | NotGiven = NOT_GIVEN,
        depress_fuel: float | NotGiven = NOT_GIVEN,
        dep_runway: str | NotGiven = NOT_GIVEN,
        drag_index: float | NotGiven = NOT_GIVEN,
        early_descent_fuel: float | NotGiven = NOT_GIVEN,
        endurance_time: str | NotGiven = NOT_GIVEN,
        enroute_fuel: float | NotGiven = NOT_GIVEN,
        enroute_time: str | NotGiven = NOT_GIVEN,
        equipment: str | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etops_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_alt_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_rating: str | NotGiven = NOT_GIVEN,
        etops_val_window: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        flight_plan_messages: Iterable[flightplan_create_params.FlightPlanMessage] | NotGiven = NOT_GIVEN,
        flight_plan_point_groups: Iterable[flightplan_create_params.FlightPlanPointGroup] | NotGiven = NOT_GIVEN,
        flight_plan_waypoints: Iterable[flightplan_create_params.FlightPlanWaypoint] | NotGiven = NOT_GIVEN,
        flight_rules: str | NotGiven = NOT_GIVEN,
        flight_type: str | NotGiven = NOT_GIVEN,
        fuel_degrade: float | NotGiven = NOT_GIVEN,
        gps_raim: str | NotGiven = NOT_GIVEN,
        hold_down_fuel: float | NotGiven = NOT_GIVEN,
        hold_fuel: float | NotGiven = NOT_GIVEN,
        hold_time: str | NotGiven = NOT_GIVEN,
        id_aircraft: str | NotGiven = NOT_GIVEN,
        id_arr_airfield: str | NotGiven = NOT_GIVEN,
        id_dep_airfield: str | NotGiven = NOT_GIVEN,
        ident_extra_fuel: float | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        initial_cruise_speed: str | NotGiven = NOT_GIVEN,
        initial_flight_level: str | NotGiven = NOT_GIVEN,
        landing_fuel: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        min_divert_fuel: float | NotGiven = NOT_GIVEN,
        msn_index: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_aircraft: int | NotGiven = NOT_GIVEN,
        op_condition_fuel: float | NotGiven = NOT_GIVEN,
        op_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        originator: str | NotGiven = NOT_GIVEN,
        planner_remark: str | NotGiven = NOT_GIVEN,
        ramp_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        reserve_fuel: float | NotGiven = NOT_GIVEN,
        route_string: str | NotGiven = NOT_GIVEN,
        sid: str | NotGiven = NOT_GIVEN,
        star: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        takeoff_fuel: float | NotGiven = NOT_GIVEN,
        taxi_fuel: float | NotGiven = NOT_GIVEN,
        thunder_avoid_fuel: float | NotGiven = NOT_GIVEN,
        toc_fuel: float | NotGiven = NOT_GIVEN,
        toc_ice_fuel: float | NotGiven = NOT_GIVEN,
        tod_fuel: float | NotGiven = NOT_GIVEN,
        tod_ice_fuel: float | NotGiven = NOT_GIVEN,
        unident_extra_fuel: float | NotGiven = NOT_GIVEN,
        unusable_fuel: float | NotGiven = NOT_GIVEN,
        wake_turb_cat: str | NotGiven = NOT_GIVEN,
        wind_fac1: float | NotGiven = NOT_GIVEN,
        wind_fac2: float | NotGiven = NOT_GIVEN,
        wind_fac_avg: float | NotGiven = NOT_GIVEN,
        wx_valid_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        wx_valid_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single FlightPlan object as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          arr_airfield: The airfield identifier of the arrival location, International Civil Aviation
              Organization (ICAO) code preferred.

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

          dep_airfield: The airfield identifier of the departure location, International Civil Aviation
              Organization (ICAO) code preferred.

          gen_ts: The generation time of this flight plan in ISO 8601 UTC format, with millisecond
              precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of the aircraft associated with this flight plan.
              Intended as, but not constrained to, MIL-STD-6016 environment dependent specific
              type designations.

          air_refuel_events: Collection of air refueling events occurring on this flight.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) encode/decode procedures.

          app_landing_fuel: Fuel burned from the initial approach point to landing in pounds.

          arr_alternate1: The first designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate1_fuel: Fuel required to fly to alternate landing site 1 and land in pounds.

          arr_alternate2: The second designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate2_fuel: Fuel required to fly to alternate landing site 2 and land in pounds.

          arr_ice_fuel: Additional fuel burned at landing/missed approach for icing during arrival in
              pounds.

          arr_runway: The arrival runway for this flight.

          atc_addresses: Array of Air Traffic Control (ATC) addresses.

          avg_temp_dev: Average temperature deviation of the primary, divert, and alternate path for the
              route between first Top of Climb and last Top of Descent in degrees Celsius.

          burned_fuel: Fuel planned to be burned during the flight in pounds.

          call_sign: The call sign assigned to the aircraft for this flight plan.

          cargo_remark: Remarks about the planned cargo associated with this flight plan.

          climb_fuel: Fuel required from brake release to Top of Climb in pounds.

          climb_time: Time required from brake release to Top of Climb expressed as HH:MM.

          contingency_fuel: The amount of contingency fuel in pounds.

          country_codes: Array of country codes for the countries overflown during this flight in ISO
              3166-1 Alpha-2 format.

          dep_alternate: The designated alternate departure airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          depress_fuel: The depressurization fuel required to fly from the Equal Time Point to the Last
              Suitable/First Suitable airfield at depressurization altitude in pounds.

          dep_runway: The departure runway for this flight.

          drag_index: The percent degrade due to drag for this aircraft.

          early_descent_fuel: Additional fuel burned at landing/missed approach for an early descent in
              pounds.

          endurance_time: Total endurance time based on the fuel on board expressed as HH:MM.

          enroute_fuel: Fuel required to fly from Top of Climb to Top of Descent in pounds.

          enroute_time: Time required to fly from Top of Climb to Top of Descent expressed as HH:MM.

          equipment: The list of equipment on the aircraft as defined in the Flight Information
              Publications (FLIP) General Planning (GP) manual.

          est_dep_time: The estimated time of departure for the aircraft, in ISO 8601 UTC format, with
              millisecond precision.

          etops_airfields: Array of Extended Operations (ETOPS) adequate landing airfields that are within
              the mission region.

          etops_alt_airfields: Array of Extended Operations (ETOPS) alternate suitable landing airfields that
              are within the mission region.

          etops_rating: The Extended Operations (ETOPS) rating used to calculate this flight plan.

          etops_val_window: The Extended Operations (ETOPS) validity window for the alternate airfield.

          external_id: The source ID of the flight plan from the generating system.

          flight_plan_messages: Collection of messages associated with this flight plan indicating the severity,
              the point where the message was generated, the path (Primary, Alternate, etc.),
              and the text of the message.

          flight_plan_point_groups: Collection of point groups generated for this flight plan. Groups include point
              sets for Extended Operations (ETOPS), Critical Fuel Point, and Equal Time Point
              (ETP).

          flight_plan_waypoints: Collection of waypoints associated with this flight plan.

          flight_rules: The flight rules this flight plan is being filed under.

          flight_type: The type of flight (MILITARY, CIVILIAN, etc).

          fuel_degrade: The fuel degrade percentage used for this mission.

          gps_raim: The GPS Receiver Autonomous Integrity Monitoring (RAIM) message. A RAIM system
              assesses the integrity of the GPS signals. This system predicts outages for a
              specified geographical area. These predictions are based on the location, path,
              and scheduled GPS satellite outages.

          hold_down_fuel: Additional fuel burned at Top of Climb in pounds.

          hold_fuel: Additional fuel burned at the destination for holding in pounds.

          hold_time: Additional time for holding at the destination expressed as HH:MM.

          id_aircraft: The UDL unique identifier of the aircraft associated with this flight plan.

          id_arr_airfield: The UDL unique identifier of the arrival airfield associated with this flight
              plan.

          id_dep_airfield: The UDL unique identifier of the departure airfield associated with this flight
              plan.

          ident_extra_fuel: The amount of identified extra fuel carried and not available in the burn plan
              in pounds.

          id_sortie: The UDL unique identifier of the aircraft sortie associated with this flight
              plan.

          initial_cruise_speed: A character string representation of the initial filed cruise speed for this
              flight (prepended values of K, N, and M represent kilometers per hour, knots,
              and Mach, respectively).

          initial_flight_level: A character string representation of the initial filed altitude level for this
              flight (prepended values of F, S, A, and M represent flight level in hundreds of
              feet, standard metric level in tens of meters, altitude in hundreds of feet, and
              altitude in tens of meters, respectively).

          landing_fuel: Fuel planned to be remaining on the airplane at landing in pounds.

          leg_num: The leg number of this flight plan.

          min_divert_fuel: The minimum fuel on board required to divert in pounds.

          msn_index: The mission index value for this mission. The mission index is the ratio of
              time-related cost of aircraft operation to the cost of fuel.

          notes: Additional remarks for air traffic control for this flight.

          num_aircraft: The number of aircraft flying this flight plan.

          op_condition_fuel: Additional fuel burned at Top of Descent for the operational condition in
              pounds.

          op_weight: Operating weight of the aircraft in pounds.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          originator: Air Traffic Control address filing the flight plan.

          planner_remark: Remarks from the planners concerning this flight plan.

          ramp_fuel: Total of all fuel required to complete the flight in pounds, including fuel to
              be dispensed on a refueling mission.

          rem_alternate1_fuel: Total fuel remaining at alternate landing site 1 in pounds.

          rem_alternate2_fuel: Total fuel remaining at alternate landing site 2 in pounds.

          reserve_fuel: The amount of reserve fuel in pounds.

          route_string: The 1801 fileable route of flight string for this flight. The route of flight
              string contains route designators, significant points, change of speed/altitude,
              change of flight rules, and cruise climbs.

          sid: Name of the planned Standard Instrument Departure (SID) procedure.

          star: Name of the planned Standard Terminal Arrival (STAR) procedure.

          status: Status of this flight plan (e.g., ACTIVE, APPROVED, PLANNED, etc.).

          tail_number: The tail number of the aircraft associated with this flight plan.

          takeoff_fuel: Fuel at takeoff, which is calculated as the ramp fuel minus the taxi fuel in
              pounds.

          taxi_fuel: Fuel required to start engines and taxi to the end of the runway in pounds.

          thunder_avoid_fuel: Additional fuel burned at Top of Descent for thunderstorm avoidance in pounds.

          toc_fuel: Fuel remaining at Top of Climb in pounds.

          toc_ice_fuel: Additional fuel burned at Top of Climb for icing in pounds.

          tod_fuel: Fuel remaining at Top of Descent in pounds.

          tod_ice_fuel: Additional fuel burned at Top of Descent for icing in pounds.

          unident_extra_fuel: The amount of unidentified extra fuel required to get to min landing in pounds.

          unusable_fuel: The amount of unusable fuel in pounds.

          wake_turb_cat: The wake turbulence category for this flight. The categories are assigned by the
              International Civil Aviation Organization (ICAO) and are based on maximum
              certified takeoff mass for the purpose of separating aircraft in flight due to
              wake turbulence. Valid values include LIGHT, MEDIUM, LARGE, HEAVY, and SUPER.

          wind_fac1: Wind factor for the first half of the route. This is the average wind factor
              from first Top of Climb to the mid-time of the entire route in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wind_fac2: Wind factor for the second half of the route. This is the average wind factor
              from the mid-time of the entire route to last Top of Descent in knots. A
              positive value indicates a headwind, while a negative value indicates a
              tailwind.

          wind_fac_avg: Average wind factor from Top of Climb to Top of Descent in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wx_valid_end: The date and time the weather valid period ends in ISO 8601 UTC format, with
              millisecond precision.

          wx_valid_start: The date and time the weather valid period begins in ISO 8601 UTC format, with
              millisecond precision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/flightplan",
            body=maybe_transform(
                {
                    "arr_airfield": arr_airfield,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "dep_airfield": dep_airfield,
                    "gen_ts": gen_ts,
                    "source": source,
                    "id": id,
                    "aircraft_mds": aircraft_mds,
                    "air_refuel_events": air_refuel_events,
                    "amc_mission_id": amc_mission_id,
                    "app_landing_fuel": app_landing_fuel,
                    "arr_alternate1": arr_alternate1,
                    "arr_alternate1_fuel": arr_alternate1_fuel,
                    "arr_alternate2": arr_alternate2,
                    "arr_alternate2_fuel": arr_alternate2_fuel,
                    "arr_ice_fuel": arr_ice_fuel,
                    "arr_runway": arr_runway,
                    "atc_addresses": atc_addresses,
                    "avg_temp_dev": avg_temp_dev,
                    "burned_fuel": burned_fuel,
                    "call_sign": call_sign,
                    "cargo_remark": cargo_remark,
                    "climb_fuel": climb_fuel,
                    "climb_time": climb_time,
                    "contingency_fuel": contingency_fuel,
                    "country_codes": country_codes,
                    "dep_alternate": dep_alternate,
                    "depress_fuel": depress_fuel,
                    "dep_runway": dep_runway,
                    "drag_index": drag_index,
                    "early_descent_fuel": early_descent_fuel,
                    "endurance_time": endurance_time,
                    "enroute_fuel": enroute_fuel,
                    "enroute_time": enroute_time,
                    "equipment": equipment,
                    "est_dep_time": est_dep_time,
                    "etops_airfields": etops_airfields,
                    "etops_alt_airfields": etops_alt_airfields,
                    "etops_rating": etops_rating,
                    "etops_val_window": etops_val_window,
                    "external_id": external_id,
                    "flight_plan_messages": flight_plan_messages,
                    "flight_plan_point_groups": flight_plan_point_groups,
                    "flight_plan_waypoints": flight_plan_waypoints,
                    "flight_rules": flight_rules,
                    "flight_type": flight_type,
                    "fuel_degrade": fuel_degrade,
                    "gps_raim": gps_raim,
                    "hold_down_fuel": hold_down_fuel,
                    "hold_fuel": hold_fuel,
                    "hold_time": hold_time,
                    "id_aircraft": id_aircraft,
                    "id_arr_airfield": id_arr_airfield,
                    "id_dep_airfield": id_dep_airfield,
                    "ident_extra_fuel": ident_extra_fuel,
                    "id_sortie": id_sortie,
                    "initial_cruise_speed": initial_cruise_speed,
                    "initial_flight_level": initial_flight_level,
                    "landing_fuel": landing_fuel,
                    "leg_num": leg_num,
                    "min_divert_fuel": min_divert_fuel,
                    "msn_index": msn_index,
                    "notes": notes,
                    "num_aircraft": num_aircraft,
                    "op_condition_fuel": op_condition_fuel,
                    "op_weight": op_weight,
                    "origin": origin,
                    "originator": originator,
                    "planner_remark": planner_remark,
                    "ramp_fuel": ramp_fuel,
                    "rem_alternate1_fuel": rem_alternate1_fuel,
                    "rem_alternate2_fuel": rem_alternate2_fuel,
                    "reserve_fuel": reserve_fuel,
                    "route_string": route_string,
                    "sid": sid,
                    "star": star,
                    "status": status,
                    "tail_number": tail_number,
                    "takeoff_fuel": takeoff_fuel,
                    "taxi_fuel": taxi_fuel,
                    "thunder_avoid_fuel": thunder_avoid_fuel,
                    "toc_fuel": toc_fuel,
                    "toc_ice_fuel": toc_ice_fuel,
                    "tod_fuel": tod_fuel,
                    "tod_ice_fuel": tod_ice_fuel,
                    "unident_extra_fuel": unident_extra_fuel,
                    "unusable_fuel": unusable_fuel,
                    "wake_turb_cat": wake_turb_cat,
                    "wind_fac1": wind_fac1,
                    "wind_fac2": wind_fac2,
                    "wind_fac_avg": wind_fac_avg,
                    "wx_valid_end": wx_valid_end,
                    "wx_valid_start": wx_valid_start,
                },
                flightplan_create_params.FlightplanCreateParams,
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
    ) -> FlightPlanFull:
        """
        Service operation to get a single FlightPlan record by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/flightplan/{id}",
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
                    flightplan_retrieve_params.FlightplanRetrieveParams,
                ),
            ),
            cast_to=FlightPlanFull,
        )

    def update(
        self,
        path_id: str,
        *,
        arr_airfield: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dep_airfield: str,
        gen_ts: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_refuel_events: Iterable[flightplan_update_params.AirRefuelEvent] | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        app_landing_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate1: str | NotGiven = NOT_GIVEN,
        arr_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate2: str | NotGiven = NOT_GIVEN,
        arr_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        arr_ice_fuel: float | NotGiven = NOT_GIVEN,
        arr_runway: str | NotGiven = NOT_GIVEN,
        atc_addresses: List[str] | NotGiven = NOT_GIVEN,
        avg_temp_dev: float | NotGiven = NOT_GIVEN,
        burned_fuel: float | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_remark: str | NotGiven = NOT_GIVEN,
        climb_fuel: float | NotGiven = NOT_GIVEN,
        climb_time: str | NotGiven = NOT_GIVEN,
        contingency_fuel: float | NotGiven = NOT_GIVEN,
        country_codes: List[str] | NotGiven = NOT_GIVEN,
        dep_alternate: str | NotGiven = NOT_GIVEN,
        depress_fuel: float | NotGiven = NOT_GIVEN,
        dep_runway: str | NotGiven = NOT_GIVEN,
        drag_index: float | NotGiven = NOT_GIVEN,
        early_descent_fuel: float | NotGiven = NOT_GIVEN,
        endurance_time: str | NotGiven = NOT_GIVEN,
        enroute_fuel: float | NotGiven = NOT_GIVEN,
        enroute_time: str | NotGiven = NOT_GIVEN,
        equipment: str | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etops_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_alt_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_rating: str | NotGiven = NOT_GIVEN,
        etops_val_window: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        flight_plan_messages: Iterable[flightplan_update_params.FlightPlanMessage] | NotGiven = NOT_GIVEN,
        flight_plan_point_groups: Iterable[flightplan_update_params.FlightPlanPointGroup] | NotGiven = NOT_GIVEN,
        flight_plan_waypoints: Iterable[flightplan_update_params.FlightPlanWaypoint] | NotGiven = NOT_GIVEN,
        flight_rules: str | NotGiven = NOT_GIVEN,
        flight_type: str | NotGiven = NOT_GIVEN,
        fuel_degrade: float | NotGiven = NOT_GIVEN,
        gps_raim: str | NotGiven = NOT_GIVEN,
        hold_down_fuel: float | NotGiven = NOT_GIVEN,
        hold_fuel: float | NotGiven = NOT_GIVEN,
        hold_time: str | NotGiven = NOT_GIVEN,
        id_aircraft: str | NotGiven = NOT_GIVEN,
        id_arr_airfield: str | NotGiven = NOT_GIVEN,
        id_dep_airfield: str | NotGiven = NOT_GIVEN,
        ident_extra_fuel: float | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        initial_cruise_speed: str | NotGiven = NOT_GIVEN,
        initial_flight_level: str | NotGiven = NOT_GIVEN,
        landing_fuel: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        min_divert_fuel: float | NotGiven = NOT_GIVEN,
        msn_index: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_aircraft: int | NotGiven = NOT_GIVEN,
        op_condition_fuel: float | NotGiven = NOT_GIVEN,
        op_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        originator: str | NotGiven = NOT_GIVEN,
        planner_remark: str | NotGiven = NOT_GIVEN,
        ramp_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        reserve_fuel: float | NotGiven = NOT_GIVEN,
        route_string: str | NotGiven = NOT_GIVEN,
        sid: str | NotGiven = NOT_GIVEN,
        star: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        takeoff_fuel: float | NotGiven = NOT_GIVEN,
        taxi_fuel: float | NotGiven = NOT_GIVEN,
        thunder_avoid_fuel: float | NotGiven = NOT_GIVEN,
        toc_fuel: float | NotGiven = NOT_GIVEN,
        toc_ice_fuel: float | NotGiven = NOT_GIVEN,
        tod_fuel: float | NotGiven = NOT_GIVEN,
        tod_ice_fuel: float | NotGiven = NOT_GIVEN,
        unident_extra_fuel: float | NotGiven = NOT_GIVEN,
        unusable_fuel: float | NotGiven = NOT_GIVEN,
        wake_turb_cat: str | NotGiven = NOT_GIVEN,
        wind_fac1: float | NotGiven = NOT_GIVEN,
        wind_fac2: float | NotGiven = NOT_GIVEN,
        wind_fac_avg: float | NotGiven = NOT_GIVEN,
        wx_valid_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        wx_valid_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single flightplan record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          arr_airfield: The airfield identifier of the arrival location, International Civil Aviation
              Organization (ICAO) code preferred.

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

          dep_airfield: The airfield identifier of the departure location, International Civil Aviation
              Organization (ICAO) code preferred.

          gen_ts: The generation time of this flight plan in ISO 8601 UTC format, with millisecond
              precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of the aircraft associated with this flight plan.
              Intended as, but not constrained to, MIL-STD-6016 environment dependent specific
              type designations.

          air_refuel_events: Collection of air refueling events occurring on this flight.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) encode/decode procedures.

          app_landing_fuel: Fuel burned from the initial approach point to landing in pounds.

          arr_alternate1: The first designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate1_fuel: Fuel required to fly to alternate landing site 1 and land in pounds.

          arr_alternate2: The second designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate2_fuel: Fuel required to fly to alternate landing site 2 and land in pounds.

          arr_ice_fuel: Additional fuel burned at landing/missed approach for icing during arrival in
              pounds.

          arr_runway: The arrival runway for this flight.

          atc_addresses: Array of Air Traffic Control (ATC) addresses.

          avg_temp_dev: Average temperature deviation of the primary, divert, and alternate path for the
              route between first Top of Climb and last Top of Descent in degrees Celsius.

          burned_fuel: Fuel planned to be burned during the flight in pounds.

          call_sign: The call sign assigned to the aircraft for this flight plan.

          cargo_remark: Remarks about the planned cargo associated with this flight plan.

          climb_fuel: Fuel required from brake release to Top of Climb in pounds.

          climb_time: Time required from brake release to Top of Climb expressed as HH:MM.

          contingency_fuel: The amount of contingency fuel in pounds.

          country_codes: Array of country codes for the countries overflown during this flight in ISO
              3166-1 Alpha-2 format.

          dep_alternate: The designated alternate departure airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          depress_fuel: The depressurization fuel required to fly from the Equal Time Point to the Last
              Suitable/First Suitable airfield at depressurization altitude in pounds.

          dep_runway: The departure runway for this flight.

          drag_index: The percent degrade due to drag for this aircraft.

          early_descent_fuel: Additional fuel burned at landing/missed approach for an early descent in
              pounds.

          endurance_time: Total endurance time based on the fuel on board expressed as HH:MM.

          enroute_fuel: Fuel required to fly from Top of Climb to Top of Descent in pounds.

          enroute_time: Time required to fly from Top of Climb to Top of Descent expressed as HH:MM.

          equipment: The list of equipment on the aircraft as defined in the Flight Information
              Publications (FLIP) General Planning (GP) manual.

          est_dep_time: The estimated time of departure for the aircraft, in ISO 8601 UTC format, with
              millisecond precision.

          etops_airfields: Array of Extended Operations (ETOPS) adequate landing airfields that are within
              the mission region.

          etops_alt_airfields: Array of Extended Operations (ETOPS) alternate suitable landing airfields that
              are within the mission region.

          etops_rating: The Extended Operations (ETOPS) rating used to calculate this flight plan.

          etops_val_window: The Extended Operations (ETOPS) validity window for the alternate airfield.

          external_id: The source ID of the flight plan from the generating system.

          flight_plan_messages: Collection of messages associated with this flight plan indicating the severity,
              the point where the message was generated, the path (Primary, Alternate, etc.),
              and the text of the message.

          flight_plan_point_groups: Collection of point groups generated for this flight plan. Groups include point
              sets for Extended Operations (ETOPS), Critical Fuel Point, and Equal Time Point
              (ETP).

          flight_plan_waypoints: Collection of waypoints associated with this flight plan.

          flight_rules: The flight rules this flight plan is being filed under.

          flight_type: The type of flight (MILITARY, CIVILIAN, etc).

          fuel_degrade: The fuel degrade percentage used for this mission.

          gps_raim: The GPS Receiver Autonomous Integrity Monitoring (RAIM) message. A RAIM system
              assesses the integrity of the GPS signals. This system predicts outages for a
              specified geographical area. These predictions are based on the location, path,
              and scheduled GPS satellite outages.

          hold_down_fuel: Additional fuel burned at Top of Climb in pounds.

          hold_fuel: Additional fuel burned at the destination for holding in pounds.

          hold_time: Additional time for holding at the destination expressed as HH:MM.

          id_aircraft: The UDL unique identifier of the aircraft associated with this flight plan.

          id_arr_airfield: The UDL unique identifier of the arrival airfield associated with this flight
              plan.

          id_dep_airfield: The UDL unique identifier of the departure airfield associated with this flight
              plan.

          ident_extra_fuel: The amount of identified extra fuel carried and not available in the burn plan
              in pounds.

          id_sortie: The UDL unique identifier of the aircraft sortie associated with this flight
              plan.

          initial_cruise_speed: A character string representation of the initial filed cruise speed for this
              flight (prepended values of K, N, and M represent kilometers per hour, knots,
              and Mach, respectively).

          initial_flight_level: A character string representation of the initial filed altitude level for this
              flight (prepended values of F, S, A, and M represent flight level in hundreds of
              feet, standard metric level in tens of meters, altitude in hundreds of feet, and
              altitude in tens of meters, respectively).

          landing_fuel: Fuel planned to be remaining on the airplane at landing in pounds.

          leg_num: The leg number of this flight plan.

          min_divert_fuel: The minimum fuel on board required to divert in pounds.

          msn_index: The mission index value for this mission. The mission index is the ratio of
              time-related cost of aircraft operation to the cost of fuel.

          notes: Additional remarks for air traffic control for this flight.

          num_aircraft: The number of aircraft flying this flight plan.

          op_condition_fuel: Additional fuel burned at Top of Descent for the operational condition in
              pounds.

          op_weight: Operating weight of the aircraft in pounds.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          originator: Air Traffic Control address filing the flight plan.

          planner_remark: Remarks from the planners concerning this flight plan.

          ramp_fuel: Total of all fuel required to complete the flight in pounds, including fuel to
              be dispensed on a refueling mission.

          rem_alternate1_fuel: Total fuel remaining at alternate landing site 1 in pounds.

          rem_alternate2_fuel: Total fuel remaining at alternate landing site 2 in pounds.

          reserve_fuel: The amount of reserve fuel in pounds.

          route_string: The 1801 fileable route of flight string for this flight. The route of flight
              string contains route designators, significant points, change of speed/altitude,
              change of flight rules, and cruise climbs.

          sid: Name of the planned Standard Instrument Departure (SID) procedure.

          star: Name of the planned Standard Terminal Arrival (STAR) procedure.

          status: Status of this flight plan (e.g., ACTIVE, APPROVED, PLANNED, etc.).

          tail_number: The tail number of the aircraft associated with this flight plan.

          takeoff_fuel: Fuel at takeoff, which is calculated as the ramp fuel minus the taxi fuel in
              pounds.

          taxi_fuel: Fuel required to start engines and taxi to the end of the runway in pounds.

          thunder_avoid_fuel: Additional fuel burned at Top of Descent for thunderstorm avoidance in pounds.

          toc_fuel: Fuel remaining at Top of Climb in pounds.

          toc_ice_fuel: Additional fuel burned at Top of Climb for icing in pounds.

          tod_fuel: Fuel remaining at Top of Descent in pounds.

          tod_ice_fuel: Additional fuel burned at Top of Descent for icing in pounds.

          unident_extra_fuel: The amount of unidentified extra fuel required to get to min landing in pounds.

          unusable_fuel: The amount of unusable fuel in pounds.

          wake_turb_cat: The wake turbulence category for this flight. The categories are assigned by the
              International Civil Aviation Organization (ICAO) and are based on maximum
              certified takeoff mass for the purpose of separating aircraft in flight due to
              wake turbulence. Valid values include LIGHT, MEDIUM, LARGE, HEAVY, and SUPER.

          wind_fac1: Wind factor for the first half of the route. This is the average wind factor
              from first Top of Climb to the mid-time of the entire route in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wind_fac2: Wind factor for the second half of the route. This is the average wind factor
              from the mid-time of the entire route to last Top of Descent in knots. A
              positive value indicates a headwind, while a negative value indicates a
              tailwind.

          wind_fac_avg: Average wind factor from Top of Climb to Top of Descent in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wx_valid_end: The date and time the weather valid period ends in ISO 8601 UTC format, with
              millisecond precision.

          wx_valid_start: The date and time the weather valid period begins in ISO 8601 UTC format, with
              millisecond precision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/flightplan/{path_id}",
            body=maybe_transform(
                {
                    "arr_airfield": arr_airfield,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "dep_airfield": dep_airfield,
                    "gen_ts": gen_ts,
                    "source": source,
                    "body_id": body_id,
                    "aircraft_mds": aircraft_mds,
                    "air_refuel_events": air_refuel_events,
                    "amc_mission_id": amc_mission_id,
                    "app_landing_fuel": app_landing_fuel,
                    "arr_alternate1": arr_alternate1,
                    "arr_alternate1_fuel": arr_alternate1_fuel,
                    "arr_alternate2": arr_alternate2,
                    "arr_alternate2_fuel": arr_alternate2_fuel,
                    "arr_ice_fuel": arr_ice_fuel,
                    "arr_runway": arr_runway,
                    "atc_addresses": atc_addresses,
                    "avg_temp_dev": avg_temp_dev,
                    "burned_fuel": burned_fuel,
                    "call_sign": call_sign,
                    "cargo_remark": cargo_remark,
                    "climb_fuel": climb_fuel,
                    "climb_time": climb_time,
                    "contingency_fuel": contingency_fuel,
                    "country_codes": country_codes,
                    "dep_alternate": dep_alternate,
                    "depress_fuel": depress_fuel,
                    "dep_runway": dep_runway,
                    "drag_index": drag_index,
                    "early_descent_fuel": early_descent_fuel,
                    "endurance_time": endurance_time,
                    "enroute_fuel": enroute_fuel,
                    "enroute_time": enroute_time,
                    "equipment": equipment,
                    "est_dep_time": est_dep_time,
                    "etops_airfields": etops_airfields,
                    "etops_alt_airfields": etops_alt_airfields,
                    "etops_rating": etops_rating,
                    "etops_val_window": etops_val_window,
                    "external_id": external_id,
                    "flight_plan_messages": flight_plan_messages,
                    "flight_plan_point_groups": flight_plan_point_groups,
                    "flight_plan_waypoints": flight_plan_waypoints,
                    "flight_rules": flight_rules,
                    "flight_type": flight_type,
                    "fuel_degrade": fuel_degrade,
                    "gps_raim": gps_raim,
                    "hold_down_fuel": hold_down_fuel,
                    "hold_fuel": hold_fuel,
                    "hold_time": hold_time,
                    "id_aircraft": id_aircraft,
                    "id_arr_airfield": id_arr_airfield,
                    "id_dep_airfield": id_dep_airfield,
                    "ident_extra_fuel": ident_extra_fuel,
                    "id_sortie": id_sortie,
                    "initial_cruise_speed": initial_cruise_speed,
                    "initial_flight_level": initial_flight_level,
                    "landing_fuel": landing_fuel,
                    "leg_num": leg_num,
                    "min_divert_fuel": min_divert_fuel,
                    "msn_index": msn_index,
                    "notes": notes,
                    "num_aircraft": num_aircraft,
                    "op_condition_fuel": op_condition_fuel,
                    "op_weight": op_weight,
                    "origin": origin,
                    "originator": originator,
                    "planner_remark": planner_remark,
                    "ramp_fuel": ramp_fuel,
                    "rem_alternate1_fuel": rem_alternate1_fuel,
                    "rem_alternate2_fuel": rem_alternate2_fuel,
                    "reserve_fuel": reserve_fuel,
                    "route_string": route_string,
                    "sid": sid,
                    "star": star,
                    "status": status,
                    "tail_number": tail_number,
                    "takeoff_fuel": takeoff_fuel,
                    "taxi_fuel": taxi_fuel,
                    "thunder_avoid_fuel": thunder_avoid_fuel,
                    "toc_fuel": toc_fuel,
                    "toc_ice_fuel": toc_ice_fuel,
                    "tod_fuel": tod_fuel,
                    "tod_ice_fuel": tod_ice_fuel,
                    "unident_extra_fuel": unident_extra_fuel,
                    "unusable_fuel": unusable_fuel,
                    "wake_turb_cat": wake_turb_cat,
                    "wind_fac1": wind_fac1,
                    "wind_fac2": wind_fac2,
                    "wind_fac_avg": wind_fac_avg,
                    "wx_valid_end": wx_valid_end,
                    "wx_valid_start": wx_valid_start,
                },
                flightplan_update_params.FlightplanUpdateParams,
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
    ) -> SyncOffsetPage[FlightPlanAbridged]:
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
            "/udl/flightplan",
            page=SyncOffsetPage[FlightPlanAbridged],
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
                    flightplan_list_params.FlightplanListParams,
                ),
            ),
            model=FlightPlanAbridged,
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
        Service operation to delete a flight plan record specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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
            f"/udl/flightplan/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/flightplan/count",
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
                    flightplan_count_params.FlightplanCountParams,
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
            "/udl/flightplan/queryhelp",
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
    ) -> FlightplanTupleResponse:
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
            "/udl/flightplan/tuple",
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
                    flightplan_tuple_params.FlightplanTupleParams,
                ),
            ),
            cast_to=FlightplanTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[flightplan_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take one or many flight plan records as a POST body and
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
            "/filedrop/udl-flightplan",
            body=maybe_transform(body, Iterable[flightplan_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFlightplanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlightplanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFlightplanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlightplanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncFlightplanResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        arr_airfield: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dep_airfield: str,
        gen_ts: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_refuel_events: Iterable[flightplan_create_params.AirRefuelEvent] | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        app_landing_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate1: str | NotGiven = NOT_GIVEN,
        arr_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate2: str | NotGiven = NOT_GIVEN,
        arr_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        arr_ice_fuel: float | NotGiven = NOT_GIVEN,
        arr_runway: str | NotGiven = NOT_GIVEN,
        atc_addresses: List[str] | NotGiven = NOT_GIVEN,
        avg_temp_dev: float | NotGiven = NOT_GIVEN,
        burned_fuel: float | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_remark: str | NotGiven = NOT_GIVEN,
        climb_fuel: float | NotGiven = NOT_GIVEN,
        climb_time: str | NotGiven = NOT_GIVEN,
        contingency_fuel: float | NotGiven = NOT_GIVEN,
        country_codes: List[str] | NotGiven = NOT_GIVEN,
        dep_alternate: str | NotGiven = NOT_GIVEN,
        depress_fuel: float | NotGiven = NOT_GIVEN,
        dep_runway: str | NotGiven = NOT_GIVEN,
        drag_index: float | NotGiven = NOT_GIVEN,
        early_descent_fuel: float | NotGiven = NOT_GIVEN,
        endurance_time: str | NotGiven = NOT_GIVEN,
        enroute_fuel: float | NotGiven = NOT_GIVEN,
        enroute_time: str | NotGiven = NOT_GIVEN,
        equipment: str | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etops_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_alt_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_rating: str | NotGiven = NOT_GIVEN,
        etops_val_window: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        flight_plan_messages: Iterable[flightplan_create_params.FlightPlanMessage] | NotGiven = NOT_GIVEN,
        flight_plan_point_groups: Iterable[flightplan_create_params.FlightPlanPointGroup] | NotGiven = NOT_GIVEN,
        flight_plan_waypoints: Iterable[flightplan_create_params.FlightPlanWaypoint] | NotGiven = NOT_GIVEN,
        flight_rules: str | NotGiven = NOT_GIVEN,
        flight_type: str | NotGiven = NOT_GIVEN,
        fuel_degrade: float | NotGiven = NOT_GIVEN,
        gps_raim: str | NotGiven = NOT_GIVEN,
        hold_down_fuel: float | NotGiven = NOT_GIVEN,
        hold_fuel: float | NotGiven = NOT_GIVEN,
        hold_time: str | NotGiven = NOT_GIVEN,
        id_aircraft: str | NotGiven = NOT_GIVEN,
        id_arr_airfield: str | NotGiven = NOT_GIVEN,
        id_dep_airfield: str | NotGiven = NOT_GIVEN,
        ident_extra_fuel: float | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        initial_cruise_speed: str | NotGiven = NOT_GIVEN,
        initial_flight_level: str | NotGiven = NOT_GIVEN,
        landing_fuel: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        min_divert_fuel: float | NotGiven = NOT_GIVEN,
        msn_index: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_aircraft: int | NotGiven = NOT_GIVEN,
        op_condition_fuel: float | NotGiven = NOT_GIVEN,
        op_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        originator: str | NotGiven = NOT_GIVEN,
        planner_remark: str | NotGiven = NOT_GIVEN,
        ramp_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        reserve_fuel: float | NotGiven = NOT_GIVEN,
        route_string: str | NotGiven = NOT_GIVEN,
        sid: str | NotGiven = NOT_GIVEN,
        star: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        takeoff_fuel: float | NotGiven = NOT_GIVEN,
        taxi_fuel: float | NotGiven = NOT_GIVEN,
        thunder_avoid_fuel: float | NotGiven = NOT_GIVEN,
        toc_fuel: float | NotGiven = NOT_GIVEN,
        toc_ice_fuel: float | NotGiven = NOT_GIVEN,
        tod_fuel: float | NotGiven = NOT_GIVEN,
        tod_ice_fuel: float | NotGiven = NOT_GIVEN,
        unident_extra_fuel: float | NotGiven = NOT_GIVEN,
        unusable_fuel: float | NotGiven = NOT_GIVEN,
        wake_turb_cat: str | NotGiven = NOT_GIVEN,
        wind_fac1: float | NotGiven = NOT_GIVEN,
        wind_fac2: float | NotGiven = NOT_GIVEN,
        wind_fac_avg: float | NotGiven = NOT_GIVEN,
        wx_valid_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        wx_valid_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single FlightPlan object as a POST body and ingest
        into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          arr_airfield: The airfield identifier of the arrival location, International Civil Aviation
              Organization (ICAO) code preferred.

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

          dep_airfield: The airfield identifier of the departure location, International Civil Aviation
              Organization (ICAO) code preferred.

          gen_ts: The generation time of this flight plan in ISO 8601 UTC format, with millisecond
              precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of the aircraft associated with this flight plan.
              Intended as, but not constrained to, MIL-STD-6016 environment dependent specific
              type designations.

          air_refuel_events: Collection of air refueling events occurring on this flight.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) encode/decode procedures.

          app_landing_fuel: Fuel burned from the initial approach point to landing in pounds.

          arr_alternate1: The first designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate1_fuel: Fuel required to fly to alternate landing site 1 and land in pounds.

          arr_alternate2: The second designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate2_fuel: Fuel required to fly to alternate landing site 2 and land in pounds.

          arr_ice_fuel: Additional fuel burned at landing/missed approach for icing during arrival in
              pounds.

          arr_runway: The arrival runway for this flight.

          atc_addresses: Array of Air Traffic Control (ATC) addresses.

          avg_temp_dev: Average temperature deviation of the primary, divert, and alternate path for the
              route between first Top of Climb and last Top of Descent in degrees Celsius.

          burned_fuel: Fuel planned to be burned during the flight in pounds.

          call_sign: The call sign assigned to the aircraft for this flight plan.

          cargo_remark: Remarks about the planned cargo associated with this flight plan.

          climb_fuel: Fuel required from brake release to Top of Climb in pounds.

          climb_time: Time required from brake release to Top of Climb expressed as HH:MM.

          contingency_fuel: The amount of contingency fuel in pounds.

          country_codes: Array of country codes for the countries overflown during this flight in ISO
              3166-1 Alpha-2 format.

          dep_alternate: The designated alternate departure airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          depress_fuel: The depressurization fuel required to fly from the Equal Time Point to the Last
              Suitable/First Suitable airfield at depressurization altitude in pounds.

          dep_runway: The departure runway for this flight.

          drag_index: The percent degrade due to drag for this aircraft.

          early_descent_fuel: Additional fuel burned at landing/missed approach for an early descent in
              pounds.

          endurance_time: Total endurance time based on the fuel on board expressed as HH:MM.

          enroute_fuel: Fuel required to fly from Top of Climb to Top of Descent in pounds.

          enroute_time: Time required to fly from Top of Climb to Top of Descent expressed as HH:MM.

          equipment: The list of equipment on the aircraft as defined in the Flight Information
              Publications (FLIP) General Planning (GP) manual.

          est_dep_time: The estimated time of departure for the aircraft, in ISO 8601 UTC format, with
              millisecond precision.

          etops_airfields: Array of Extended Operations (ETOPS) adequate landing airfields that are within
              the mission region.

          etops_alt_airfields: Array of Extended Operations (ETOPS) alternate suitable landing airfields that
              are within the mission region.

          etops_rating: The Extended Operations (ETOPS) rating used to calculate this flight plan.

          etops_val_window: The Extended Operations (ETOPS) validity window for the alternate airfield.

          external_id: The source ID of the flight plan from the generating system.

          flight_plan_messages: Collection of messages associated with this flight plan indicating the severity,
              the point where the message was generated, the path (Primary, Alternate, etc.),
              and the text of the message.

          flight_plan_point_groups: Collection of point groups generated for this flight plan. Groups include point
              sets for Extended Operations (ETOPS), Critical Fuel Point, and Equal Time Point
              (ETP).

          flight_plan_waypoints: Collection of waypoints associated with this flight plan.

          flight_rules: The flight rules this flight plan is being filed under.

          flight_type: The type of flight (MILITARY, CIVILIAN, etc).

          fuel_degrade: The fuel degrade percentage used for this mission.

          gps_raim: The GPS Receiver Autonomous Integrity Monitoring (RAIM) message. A RAIM system
              assesses the integrity of the GPS signals. This system predicts outages for a
              specified geographical area. These predictions are based on the location, path,
              and scheduled GPS satellite outages.

          hold_down_fuel: Additional fuel burned at Top of Climb in pounds.

          hold_fuel: Additional fuel burned at the destination for holding in pounds.

          hold_time: Additional time for holding at the destination expressed as HH:MM.

          id_aircraft: The UDL unique identifier of the aircraft associated with this flight plan.

          id_arr_airfield: The UDL unique identifier of the arrival airfield associated with this flight
              plan.

          id_dep_airfield: The UDL unique identifier of the departure airfield associated with this flight
              plan.

          ident_extra_fuel: The amount of identified extra fuel carried and not available in the burn plan
              in pounds.

          id_sortie: The UDL unique identifier of the aircraft sortie associated with this flight
              plan.

          initial_cruise_speed: A character string representation of the initial filed cruise speed for this
              flight (prepended values of K, N, and M represent kilometers per hour, knots,
              and Mach, respectively).

          initial_flight_level: A character string representation of the initial filed altitude level for this
              flight (prepended values of F, S, A, and M represent flight level in hundreds of
              feet, standard metric level in tens of meters, altitude in hundreds of feet, and
              altitude in tens of meters, respectively).

          landing_fuel: Fuel planned to be remaining on the airplane at landing in pounds.

          leg_num: The leg number of this flight plan.

          min_divert_fuel: The minimum fuel on board required to divert in pounds.

          msn_index: The mission index value for this mission. The mission index is the ratio of
              time-related cost of aircraft operation to the cost of fuel.

          notes: Additional remarks for air traffic control for this flight.

          num_aircraft: The number of aircraft flying this flight plan.

          op_condition_fuel: Additional fuel burned at Top of Descent for the operational condition in
              pounds.

          op_weight: Operating weight of the aircraft in pounds.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          originator: Air Traffic Control address filing the flight plan.

          planner_remark: Remarks from the planners concerning this flight plan.

          ramp_fuel: Total of all fuel required to complete the flight in pounds, including fuel to
              be dispensed on a refueling mission.

          rem_alternate1_fuel: Total fuel remaining at alternate landing site 1 in pounds.

          rem_alternate2_fuel: Total fuel remaining at alternate landing site 2 in pounds.

          reserve_fuel: The amount of reserve fuel in pounds.

          route_string: The 1801 fileable route of flight string for this flight. The route of flight
              string contains route designators, significant points, change of speed/altitude,
              change of flight rules, and cruise climbs.

          sid: Name of the planned Standard Instrument Departure (SID) procedure.

          star: Name of the planned Standard Terminal Arrival (STAR) procedure.

          status: Status of this flight plan (e.g., ACTIVE, APPROVED, PLANNED, etc.).

          tail_number: The tail number of the aircraft associated with this flight plan.

          takeoff_fuel: Fuel at takeoff, which is calculated as the ramp fuel minus the taxi fuel in
              pounds.

          taxi_fuel: Fuel required to start engines and taxi to the end of the runway in pounds.

          thunder_avoid_fuel: Additional fuel burned at Top of Descent for thunderstorm avoidance in pounds.

          toc_fuel: Fuel remaining at Top of Climb in pounds.

          toc_ice_fuel: Additional fuel burned at Top of Climb for icing in pounds.

          tod_fuel: Fuel remaining at Top of Descent in pounds.

          tod_ice_fuel: Additional fuel burned at Top of Descent for icing in pounds.

          unident_extra_fuel: The amount of unidentified extra fuel required to get to min landing in pounds.

          unusable_fuel: The amount of unusable fuel in pounds.

          wake_turb_cat: The wake turbulence category for this flight. The categories are assigned by the
              International Civil Aviation Organization (ICAO) and are based on maximum
              certified takeoff mass for the purpose of separating aircraft in flight due to
              wake turbulence. Valid values include LIGHT, MEDIUM, LARGE, HEAVY, and SUPER.

          wind_fac1: Wind factor for the first half of the route. This is the average wind factor
              from first Top of Climb to the mid-time of the entire route in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wind_fac2: Wind factor for the second half of the route. This is the average wind factor
              from the mid-time of the entire route to last Top of Descent in knots. A
              positive value indicates a headwind, while a negative value indicates a
              tailwind.

          wind_fac_avg: Average wind factor from Top of Climb to Top of Descent in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wx_valid_end: The date and time the weather valid period ends in ISO 8601 UTC format, with
              millisecond precision.

          wx_valid_start: The date and time the weather valid period begins in ISO 8601 UTC format, with
              millisecond precision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/flightplan",
            body=await async_maybe_transform(
                {
                    "arr_airfield": arr_airfield,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "dep_airfield": dep_airfield,
                    "gen_ts": gen_ts,
                    "source": source,
                    "id": id,
                    "aircraft_mds": aircraft_mds,
                    "air_refuel_events": air_refuel_events,
                    "amc_mission_id": amc_mission_id,
                    "app_landing_fuel": app_landing_fuel,
                    "arr_alternate1": arr_alternate1,
                    "arr_alternate1_fuel": arr_alternate1_fuel,
                    "arr_alternate2": arr_alternate2,
                    "arr_alternate2_fuel": arr_alternate2_fuel,
                    "arr_ice_fuel": arr_ice_fuel,
                    "arr_runway": arr_runway,
                    "atc_addresses": atc_addresses,
                    "avg_temp_dev": avg_temp_dev,
                    "burned_fuel": burned_fuel,
                    "call_sign": call_sign,
                    "cargo_remark": cargo_remark,
                    "climb_fuel": climb_fuel,
                    "climb_time": climb_time,
                    "contingency_fuel": contingency_fuel,
                    "country_codes": country_codes,
                    "dep_alternate": dep_alternate,
                    "depress_fuel": depress_fuel,
                    "dep_runway": dep_runway,
                    "drag_index": drag_index,
                    "early_descent_fuel": early_descent_fuel,
                    "endurance_time": endurance_time,
                    "enroute_fuel": enroute_fuel,
                    "enroute_time": enroute_time,
                    "equipment": equipment,
                    "est_dep_time": est_dep_time,
                    "etops_airfields": etops_airfields,
                    "etops_alt_airfields": etops_alt_airfields,
                    "etops_rating": etops_rating,
                    "etops_val_window": etops_val_window,
                    "external_id": external_id,
                    "flight_plan_messages": flight_plan_messages,
                    "flight_plan_point_groups": flight_plan_point_groups,
                    "flight_plan_waypoints": flight_plan_waypoints,
                    "flight_rules": flight_rules,
                    "flight_type": flight_type,
                    "fuel_degrade": fuel_degrade,
                    "gps_raim": gps_raim,
                    "hold_down_fuel": hold_down_fuel,
                    "hold_fuel": hold_fuel,
                    "hold_time": hold_time,
                    "id_aircraft": id_aircraft,
                    "id_arr_airfield": id_arr_airfield,
                    "id_dep_airfield": id_dep_airfield,
                    "ident_extra_fuel": ident_extra_fuel,
                    "id_sortie": id_sortie,
                    "initial_cruise_speed": initial_cruise_speed,
                    "initial_flight_level": initial_flight_level,
                    "landing_fuel": landing_fuel,
                    "leg_num": leg_num,
                    "min_divert_fuel": min_divert_fuel,
                    "msn_index": msn_index,
                    "notes": notes,
                    "num_aircraft": num_aircraft,
                    "op_condition_fuel": op_condition_fuel,
                    "op_weight": op_weight,
                    "origin": origin,
                    "originator": originator,
                    "planner_remark": planner_remark,
                    "ramp_fuel": ramp_fuel,
                    "rem_alternate1_fuel": rem_alternate1_fuel,
                    "rem_alternate2_fuel": rem_alternate2_fuel,
                    "reserve_fuel": reserve_fuel,
                    "route_string": route_string,
                    "sid": sid,
                    "star": star,
                    "status": status,
                    "tail_number": tail_number,
                    "takeoff_fuel": takeoff_fuel,
                    "taxi_fuel": taxi_fuel,
                    "thunder_avoid_fuel": thunder_avoid_fuel,
                    "toc_fuel": toc_fuel,
                    "toc_ice_fuel": toc_ice_fuel,
                    "tod_fuel": tod_fuel,
                    "tod_ice_fuel": tod_ice_fuel,
                    "unident_extra_fuel": unident_extra_fuel,
                    "unusable_fuel": unusable_fuel,
                    "wake_turb_cat": wake_turb_cat,
                    "wind_fac1": wind_fac1,
                    "wind_fac2": wind_fac2,
                    "wind_fac_avg": wind_fac_avg,
                    "wx_valid_end": wx_valid_end,
                    "wx_valid_start": wx_valid_start,
                },
                flightplan_create_params.FlightplanCreateParams,
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
    ) -> FlightPlanFull:
        """
        Service operation to get a single FlightPlan record by its unique ID passed as a
        path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/flightplan/{id}",
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
                    flightplan_retrieve_params.FlightplanRetrieveParams,
                ),
            ),
            cast_to=FlightPlanFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        arr_airfield: str,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        dep_airfield: str,
        gen_ts: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_refuel_events: Iterable[flightplan_update_params.AirRefuelEvent] | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        app_landing_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate1: str | NotGiven = NOT_GIVEN,
        arr_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        arr_alternate2: str | NotGiven = NOT_GIVEN,
        arr_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        arr_ice_fuel: float | NotGiven = NOT_GIVEN,
        arr_runway: str | NotGiven = NOT_GIVEN,
        atc_addresses: List[str] | NotGiven = NOT_GIVEN,
        avg_temp_dev: float | NotGiven = NOT_GIVEN,
        burned_fuel: float | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_remark: str | NotGiven = NOT_GIVEN,
        climb_fuel: float | NotGiven = NOT_GIVEN,
        climb_time: str | NotGiven = NOT_GIVEN,
        contingency_fuel: float | NotGiven = NOT_GIVEN,
        country_codes: List[str] | NotGiven = NOT_GIVEN,
        dep_alternate: str | NotGiven = NOT_GIVEN,
        depress_fuel: float | NotGiven = NOT_GIVEN,
        dep_runway: str | NotGiven = NOT_GIVEN,
        drag_index: float | NotGiven = NOT_GIVEN,
        early_descent_fuel: float | NotGiven = NOT_GIVEN,
        endurance_time: str | NotGiven = NOT_GIVEN,
        enroute_fuel: float | NotGiven = NOT_GIVEN,
        enroute_time: str | NotGiven = NOT_GIVEN,
        equipment: str | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etops_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_alt_airfields: List[str] | NotGiven = NOT_GIVEN,
        etops_rating: str | NotGiven = NOT_GIVEN,
        etops_val_window: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        flight_plan_messages: Iterable[flightplan_update_params.FlightPlanMessage] | NotGiven = NOT_GIVEN,
        flight_plan_point_groups: Iterable[flightplan_update_params.FlightPlanPointGroup] | NotGiven = NOT_GIVEN,
        flight_plan_waypoints: Iterable[flightplan_update_params.FlightPlanWaypoint] | NotGiven = NOT_GIVEN,
        flight_rules: str | NotGiven = NOT_GIVEN,
        flight_type: str | NotGiven = NOT_GIVEN,
        fuel_degrade: float | NotGiven = NOT_GIVEN,
        gps_raim: str | NotGiven = NOT_GIVEN,
        hold_down_fuel: float | NotGiven = NOT_GIVEN,
        hold_fuel: float | NotGiven = NOT_GIVEN,
        hold_time: str | NotGiven = NOT_GIVEN,
        id_aircraft: str | NotGiven = NOT_GIVEN,
        id_arr_airfield: str | NotGiven = NOT_GIVEN,
        id_dep_airfield: str | NotGiven = NOT_GIVEN,
        ident_extra_fuel: float | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        initial_cruise_speed: str | NotGiven = NOT_GIVEN,
        initial_flight_level: str | NotGiven = NOT_GIVEN,
        landing_fuel: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        min_divert_fuel: float | NotGiven = NOT_GIVEN,
        msn_index: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_aircraft: int | NotGiven = NOT_GIVEN,
        op_condition_fuel: float | NotGiven = NOT_GIVEN,
        op_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        originator: str | NotGiven = NOT_GIVEN,
        planner_remark: str | NotGiven = NOT_GIVEN,
        ramp_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate1_fuel: float | NotGiven = NOT_GIVEN,
        rem_alternate2_fuel: float | NotGiven = NOT_GIVEN,
        reserve_fuel: float | NotGiven = NOT_GIVEN,
        route_string: str | NotGiven = NOT_GIVEN,
        sid: str | NotGiven = NOT_GIVEN,
        star: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        takeoff_fuel: float | NotGiven = NOT_GIVEN,
        taxi_fuel: float | NotGiven = NOT_GIVEN,
        thunder_avoid_fuel: float | NotGiven = NOT_GIVEN,
        toc_fuel: float | NotGiven = NOT_GIVEN,
        toc_ice_fuel: float | NotGiven = NOT_GIVEN,
        tod_fuel: float | NotGiven = NOT_GIVEN,
        tod_ice_fuel: float | NotGiven = NOT_GIVEN,
        unident_extra_fuel: float | NotGiven = NOT_GIVEN,
        unusable_fuel: float | NotGiven = NOT_GIVEN,
        wake_turb_cat: str | NotGiven = NOT_GIVEN,
        wind_fac1: float | NotGiven = NOT_GIVEN,
        wind_fac2: float | NotGiven = NOT_GIVEN,
        wind_fac_avg: float | NotGiven = NOT_GIVEN,
        wx_valid_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        wx_valid_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single flightplan record.

        A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        Args:
          arr_airfield: The airfield identifier of the arrival location, International Civil Aviation
              Organization (ICAO) code preferred.

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

          dep_airfield: The airfield identifier of the departure location, International Civil Aviation
              Organization (ICAO) code preferred.

          gen_ts: The generation time of this flight plan in ISO 8601 UTC format, with millisecond
              precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          aircraft_mds: The aircraft Model Design Series (MDS) designation (e.g. E-2C HAWKEYE, F-15
              EAGLE, KC-130 HERCULES, etc.) of the aircraft associated with this flight plan.
              Intended as, but not constrained to, MIL-STD-6016 environment dependent specific
              type designations.

          air_refuel_events: Collection of air refueling events occurring on this flight.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) encode/decode procedures.

          app_landing_fuel: Fuel burned from the initial approach point to landing in pounds.

          arr_alternate1: The first designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate1_fuel: Fuel required to fly to alternate landing site 1 and land in pounds.

          arr_alternate2: The second designated alternate arrival airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          arr_alternate2_fuel: Fuel required to fly to alternate landing site 2 and land in pounds.

          arr_ice_fuel: Additional fuel burned at landing/missed approach for icing during arrival in
              pounds.

          arr_runway: The arrival runway for this flight.

          atc_addresses: Array of Air Traffic Control (ATC) addresses.

          avg_temp_dev: Average temperature deviation of the primary, divert, and alternate path for the
              route between first Top of Climb and last Top of Descent in degrees Celsius.

          burned_fuel: Fuel planned to be burned during the flight in pounds.

          call_sign: The call sign assigned to the aircraft for this flight plan.

          cargo_remark: Remarks about the planned cargo associated with this flight plan.

          climb_fuel: Fuel required from brake release to Top of Climb in pounds.

          climb_time: Time required from brake release to Top of Climb expressed as HH:MM.

          contingency_fuel: The amount of contingency fuel in pounds.

          country_codes: Array of country codes for the countries overflown during this flight in ISO
              3166-1 Alpha-2 format.

          dep_alternate: The designated alternate departure airfield, International Civil Aviation
              Organization (ICAO) code preferred.

          depress_fuel: The depressurization fuel required to fly from the Equal Time Point to the Last
              Suitable/First Suitable airfield at depressurization altitude in pounds.

          dep_runway: The departure runway for this flight.

          drag_index: The percent degrade due to drag for this aircraft.

          early_descent_fuel: Additional fuel burned at landing/missed approach for an early descent in
              pounds.

          endurance_time: Total endurance time based on the fuel on board expressed as HH:MM.

          enroute_fuel: Fuel required to fly from Top of Climb to Top of Descent in pounds.

          enroute_time: Time required to fly from Top of Climb to Top of Descent expressed as HH:MM.

          equipment: The list of equipment on the aircraft as defined in the Flight Information
              Publications (FLIP) General Planning (GP) manual.

          est_dep_time: The estimated time of departure for the aircraft, in ISO 8601 UTC format, with
              millisecond precision.

          etops_airfields: Array of Extended Operations (ETOPS) adequate landing airfields that are within
              the mission region.

          etops_alt_airfields: Array of Extended Operations (ETOPS) alternate suitable landing airfields that
              are within the mission region.

          etops_rating: The Extended Operations (ETOPS) rating used to calculate this flight plan.

          etops_val_window: The Extended Operations (ETOPS) validity window for the alternate airfield.

          external_id: The source ID of the flight plan from the generating system.

          flight_plan_messages: Collection of messages associated with this flight plan indicating the severity,
              the point where the message was generated, the path (Primary, Alternate, etc.),
              and the text of the message.

          flight_plan_point_groups: Collection of point groups generated for this flight plan. Groups include point
              sets for Extended Operations (ETOPS), Critical Fuel Point, and Equal Time Point
              (ETP).

          flight_plan_waypoints: Collection of waypoints associated with this flight plan.

          flight_rules: The flight rules this flight plan is being filed under.

          flight_type: The type of flight (MILITARY, CIVILIAN, etc).

          fuel_degrade: The fuel degrade percentage used for this mission.

          gps_raim: The GPS Receiver Autonomous Integrity Monitoring (RAIM) message. A RAIM system
              assesses the integrity of the GPS signals. This system predicts outages for a
              specified geographical area. These predictions are based on the location, path,
              and scheduled GPS satellite outages.

          hold_down_fuel: Additional fuel burned at Top of Climb in pounds.

          hold_fuel: Additional fuel burned at the destination for holding in pounds.

          hold_time: Additional time for holding at the destination expressed as HH:MM.

          id_aircraft: The UDL unique identifier of the aircraft associated with this flight plan.

          id_arr_airfield: The UDL unique identifier of the arrival airfield associated with this flight
              plan.

          id_dep_airfield: The UDL unique identifier of the departure airfield associated with this flight
              plan.

          ident_extra_fuel: The amount of identified extra fuel carried and not available in the burn plan
              in pounds.

          id_sortie: The UDL unique identifier of the aircraft sortie associated with this flight
              plan.

          initial_cruise_speed: A character string representation of the initial filed cruise speed for this
              flight (prepended values of K, N, and M represent kilometers per hour, knots,
              and Mach, respectively).

          initial_flight_level: A character string representation of the initial filed altitude level for this
              flight (prepended values of F, S, A, and M represent flight level in hundreds of
              feet, standard metric level in tens of meters, altitude in hundreds of feet, and
              altitude in tens of meters, respectively).

          landing_fuel: Fuel planned to be remaining on the airplane at landing in pounds.

          leg_num: The leg number of this flight plan.

          min_divert_fuel: The minimum fuel on board required to divert in pounds.

          msn_index: The mission index value for this mission. The mission index is the ratio of
              time-related cost of aircraft operation to the cost of fuel.

          notes: Additional remarks for air traffic control for this flight.

          num_aircraft: The number of aircraft flying this flight plan.

          op_condition_fuel: Additional fuel burned at Top of Descent for the operational condition in
              pounds.

          op_weight: Operating weight of the aircraft in pounds.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          originator: Air Traffic Control address filing the flight plan.

          planner_remark: Remarks from the planners concerning this flight plan.

          ramp_fuel: Total of all fuel required to complete the flight in pounds, including fuel to
              be dispensed on a refueling mission.

          rem_alternate1_fuel: Total fuel remaining at alternate landing site 1 in pounds.

          rem_alternate2_fuel: Total fuel remaining at alternate landing site 2 in pounds.

          reserve_fuel: The amount of reserve fuel in pounds.

          route_string: The 1801 fileable route of flight string for this flight. The route of flight
              string contains route designators, significant points, change of speed/altitude,
              change of flight rules, and cruise climbs.

          sid: Name of the planned Standard Instrument Departure (SID) procedure.

          star: Name of the planned Standard Terminal Arrival (STAR) procedure.

          status: Status of this flight plan (e.g., ACTIVE, APPROVED, PLANNED, etc.).

          tail_number: The tail number of the aircraft associated with this flight plan.

          takeoff_fuel: Fuel at takeoff, which is calculated as the ramp fuel minus the taxi fuel in
              pounds.

          taxi_fuel: Fuel required to start engines and taxi to the end of the runway in pounds.

          thunder_avoid_fuel: Additional fuel burned at Top of Descent for thunderstorm avoidance in pounds.

          toc_fuel: Fuel remaining at Top of Climb in pounds.

          toc_ice_fuel: Additional fuel burned at Top of Climb for icing in pounds.

          tod_fuel: Fuel remaining at Top of Descent in pounds.

          tod_ice_fuel: Additional fuel burned at Top of Descent for icing in pounds.

          unident_extra_fuel: The amount of unidentified extra fuel required to get to min landing in pounds.

          unusable_fuel: The amount of unusable fuel in pounds.

          wake_turb_cat: The wake turbulence category for this flight. The categories are assigned by the
              International Civil Aviation Organization (ICAO) and are based on maximum
              certified takeoff mass for the purpose of separating aircraft in flight due to
              wake turbulence. Valid values include LIGHT, MEDIUM, LARGE, HEAVY, and SUPER.

          wind_fac1: Wind factor for the first half of the route. This is the average wind factor
              from first Top of Climb to the mid-time of the entire route in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wind_fac2: Wind factor for the second half of the route. This is the average wind factor
              from the mid-time of the entire route to last Top of Descent in knots. A
              positive value indicates a headwind, while a negative value indicates a
              tailwind.

          wind_fac_avg: Average wind factor from Top of Climb to Top of Descent in knots. A positive
              value indicates a headwind, while a negative value indicates a tailwind.

          wx_valid_end: The date and time the weather valid period ends in ISO 8601 UTC format, with
              millisecond precision.

          wx_valid_start: The date and time the weather valid period begins in ISO 8601 UTC format, with
              millisecond precision.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/flightplan/{path_id}",
            body=await async_maybe_transform(
                {
                    "arr_airfield": arr_airfield,
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "dep_airfield": dep_airfield,
                    "gen_ts": gen_ts,
                    "source": source,
                    "body_id": body_id,
                    "aircraft_mds": aircraft_mds,
                    "air_refuel_events": air_refuel_events,
                    "amc_mission_id": amc_mission_id,
                    "app_landing_fuel": app_landing_fuel,
                    "arr_alternate1": arr_alternate1,
                    "arr_alternate1_fuel": arr_alternate1_fuel,
                    "arr_alternate2": arr_alternate2,
                    "arr_alternate2_fuel": arr_alternate2_fuel,
                    "arr_ice_fuel": arr_ice_fuel,
                    "arr_runway": arr_runway,
                    "atc_addresses": atc_addresses,
                    "avg_temp_dev": avg_temp_dev,
                    "burned_fuel": burned_fuel,
                    "call_sign": call_sign,
                    "cargo_remark": cargo_remark,
                    "climb_fuel": climb_fuel,
                    "climb_time": climb_time,
                    "contingency_fuel": contingency_fuel,
                    "country_codes": country_codes,
                    "dep_alternate": dep_alternate,
                    "depress_fuel": depress_fuel,
                    "dep_runway": dep_runway,
                    "drag_index": drag_index,
                    "early_descent_fuel": early_descent_fuel,
                    "endurance_time": endurance_time,
                    "enroute_fuel": enroute_fuel,
                    "enroute_time": enroute_time,
                    "equipment": equipment,
                    "est_dep_time": est_dep_time,
                    "etops_airfields": etops_airfields,
                    "etops_alt_airfields": etops_alt_airfields,
                    "etops_rating": etops_rating,
                    "etops_val_window": etops_val_window,
                    "external_id": external_id,
                    "flight_plan_messages": flight_plan_messages,
                    "flight_plan_point_groups": flight_plan_point_groups,
                    "flight_plan_waypoints": flight_plan_waypoints,
                    "flight_rules": flight_rules,
                    "flight_type": flight_type,
                    "fuel_degrade": fuel_degrade,
                    "gps_raim": gps_raim,
                    "hold_down_fuel": hold_down_fuel,
                    "hold_fuel": hold_fuel,
                    "hold_time": hold_time,
                    "id_aircraft": id_aircraft,
                    "id_arr_airfield": id_arr_airfield,
                    "id_dep_airfield": id_dep_airfield,
                    "ident_extra_fuel": ident_extra_fuel,
                    "id_sortie": id_sortie,
                    "initial_cruise_speed": initial_cruise_speed,
                    "initial_flight_level": initial_flight_level,
                    "landing_fuel": landing_fuel,
                    "leg_num": leg_num,
                    "min_divert_fuel": min_divert_fuel,
                    "msn_index": msn_index,
                    "notes": notes,
                    "num_aircraft": num_aircraft,
                    "op_condition_fuel": op_condition_fuel,
                    "op_weight": op_weight,
                    "origin": origin,
                    "originator": originator,
                    "planner_remark": planner_remark,
                    "ramp_fuel": ramp_fuel,
                    "rem_alternate1_fuel": rem_alternate1_fuel,
                    "rem_alternate2_fuel": rem_alternate2_fuel,
                    "reserve_fuel": reserve_fuel,
                    "route_string": route_string,
                    "sid": sid,
                    "star": star,
                    "status": status,
                    "tail_number": tail_number,
                    "takeoff_fuel": takeoff_fuel,
                    "taxi_fuel": taxi_fuel,
                    "thunder_avoid_fuel": thunder_avoid_fuel,
                    "toc_fuel": toc_fuel,
                    "toc_ice_fuel": toc_ice_fuel,
                    "tod_fuel": tod_fuel,
                    "tod_ice_fuel": tod_ice_fuel,
                    "unident_extra_fuel": unident_extra_fuel,
                    "unusable_fuel": unusable_fuel,
                    "wake_turb_cat": wake_turb_cat,
                    "wind_fac1": wind_fac1,
                    "wind_fac2": wind_fac2,
                    "wind_fac_avg": wind_fac_avg,
                    "wx_valid_end": wx_valid_end,
                    "wx_valid_start": wx_valid_start,
                },
                flightplan_update_params.FlightplanUpdateParams,
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
    ) -> AsyncPaginator[FlightPlanAbridged, AsyncOffsetPage[FlightPlanAbridged]]:
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
            "/udl/flightplan",
            page=AsyncOffsetPage[FlightPlanAbridged],
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
                    flightplan_list_params.FlightplanListParams,
                ),
            ),
            model=FlightPlanAbridged,
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
        Service operation to delete a flight plan record specified by the passed ID path
        parameter. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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
            f"/udl/flightplan/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            "/udl/flightplan/count",
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
                    flightplan_count_params.FlightplanCountParams,
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
            "/udl/flightplan/queryhelp",
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
    ) -> FlightplanTupleResponse:
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
            "/udl/flightplan/tuple",
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
                    flightplan_tuple_params.FlightplanTupleParams,
                ),
            ),
            cast_to=FlightplanTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[flightplan_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take one or many flight plan records as a POST body and
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
            "/filedrop/udl-flightplan",
            body=await async_maybe_transform(body, Iterable[flightplan_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FlightplanResourceWithRawResponse:
    def __init__(self, flightplan: FlightplanResource) -> None:
        self._flightplan = flightplan

        self.create = to_raw_response_wrapper(
            flightplan.create,
        )
        self.retrieve = to_raw_response_wrapper(
            flightplan.retrieve,
        )
        self.update = to_raw_response_wrapper(
            flightplan.update,
        )
        self.list = to_raw_response_wrapper(
            flightplan.list,
        )
        self.delete = to_raw_response_wrapper(
            flightplan.delete,
        )
        self.count = to_raw_response_wrapper(
            flightplan.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            flightplan.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            flightplan.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            flightplan.unvalidated_publish,
        )


class AsyncFlightplanResourceWithRawResponse:
    def __init__(self, flightplan: AsyncFlightplanResource) -> None:
        self._flightplan = flightplan

        self.create = async_to_raw_response_wrapper(
            flightplan.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            flightplan.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            flightplan.update,
        )
        self.list = async_to_raw_response_wrapper(
            flightplan.list,
        )
        self.delete = async_to_raw_response_wrapper(
            flightplan.delete,
        )
        self.count = async_to_raw_response_wrapper(
            flightplan.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            flightplan.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            flightplan.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            flightplan.unvalidated_publish,
        )


class FlightplanResourceWithStreamingResponse:
    def __init__(self, flightplan: FlightplanResource) -> None:
        self._flightplan = flightplan

        self.create = to_streamed_response_wrapper(
            flightplan.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            flightplan.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            flightplan.update,
        )
        self.list = to_streamed_response_wrapper(
            flightplan.list,
        )
        self.delete = to_streamed_response_wrapper(
            flightplan.delete,
        )
        self.count = to_streamed_response_wrapper(
            flightplan.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            flightplan.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            flightplan.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            flightplan.unvalidated_publish,
        )


class AsyncFlightplanResourceWithStreamingResponse:
    def __init__(self, flightplan: AsyncFlightplanResource) -> None:
        self._flightplan = flightplan

        self.create = async_to_streamed_response_wrapper(
            flightplan.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            flightplan.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            flightplan.update,
        )
        self.list = async_to_streamed_response_wrapper(
            flightplan.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            flightplan.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            flightplan.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            flightplan.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            flightplan.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            flightplan.unvalidated_publish,
        )
