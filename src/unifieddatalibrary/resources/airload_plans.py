# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    airload_plan_list_params,
    airload_plan_count_params,
    airload_plan_tuple_params,
    airload_plan_create_params,
    airload_plan_update_params,
    airload_plan_retrieve_params,
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
from ..types.airloadplan_abridged import AirloadplanAbridged
from ..types.shared.airloadplan_full import AirloadplanFull
from ..types.airload_plan_tuple_response import AirloadPlanTupleResponse
from ..types.airload_plan_queryhelp_response import AirloadPlanQueryhelpResponse

__all__ = ["AirloadPlansResource", "AsyncAirloadPlansResource"]


class AirloadPlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AirloadPlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirloadPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirloadPlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirloadPlansResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        est_dep_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        acl_onboard: float | NotGiven = NOT_GIVEN,
        acl_released: float | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_load_plan_hazmat_actuals: Iterable[airload_plan_create_params.AirLoadPlanHazmatActual]
        | NotGiven = NOT_GIVEN,
        air_load_plan_hr: Iterable[airload_plan_create_params.AirLoadPlanHr] | NotGiven = NOT_GIVEN,
        air_load_plan_pallet_details: Iterable[airload_plan_create_params.AirLoadPlanPalletDetail]
        | NotGiven = NOT_GIVEN,
        air_load_plan_pax_cargo: Iterable[airload_plan_create_params.AirLoadPlanPaxCargo] | NotGiven = NOT_GIVEN,
        air_load_plan_uln_actuals: Iterable[airload_plan_create_params.AirLoadPlanUlnActual] | NotGiven = NOT_GIVEN,
        arr_airfield: str | NotGiven = NOT_GIVEN,
        arr_icao: str | NotGiven = NOT_GIVEN,
        available_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        basic_moment: float | NotGiven = NOT_GIVEN,
        basic_weight: float | NotGiven = NOT_GIVEN,
        brief_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_bay_fs_max: float | NotGiven = NOT_GIVEN,
        cargo_bay_fs_min: float | NotGiven = NOT_GIVEN,
        cargo_bay_width: float | NotGiven = NOT_GIVEN,
        cargo_config: str | NotGiven = NOT_GIVEN,
        cargo_moment: float | NotGiven = NOT_GIVEN,
        cargo_volume: float | NotGiven = NOT_GIVEN,
        cargo_weight: float | NotGiven = NOT_GIVEN,
        crew_size: int | NotGiven = NOT_GIVEN,
        dep_airfield: str | NotGiven = NOT_GIVEN,
        dep_icao: str | NotGiven = NOT_GIVEN,
        equip_config: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_landing_fuel_moment: float | NotGiven = NOT_GIVEN,
        est_landing_fuel_weight: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fuel_moment: float | NotGiven = NOT_GIVEN,
        fuel_weight: float | NotGiven = NOT_GIVEN,
        gross_cg: float | NotGiven = NOT_GIVEN,
        gross_moment: float | NotGiven = NOT_GIVEN,
        gross_weight: float | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        landing_cg: float | NotGiven = NOT_GIVEN,
        landing_moment: float | NotGiven = NOT_GIVEN,
        landing_weight: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        loadmaster_name: str | NotGiven = NOT_GIVEN,
        loadmaster_rank: str | NotGiven = NOT_GIVEN,
        load_remarks: str | NotGiven = NOT_GIVEN,
        mission_number: str | NotGiven = NOT_GIVEN,
        operating_moment: float | NotGiven = NOT_GIVEN,
        operating_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pp_onboard: int | NotGiven = NOT_GIVEN,
        pp_released: int | NotGiven = NOT_GIVEN,
        sched_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        seats_onboard: int | NotGiven = NOT_GIVEN,
        seats_released: int | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        tank_config: str | NotGiven = NOT_GIVEN,
        util_code: str | NotGiven = NOT_GIVEN,
        zero_fuel_cg: float | NotGiven = NOT_GIVEN,
        zero_fuel_moment: float | NotGiven = NOT_GIVEN,
        zero_fuel_weight: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airloadplan record as a POST body and ingest
        into the database. A specific role is required to perform this service
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

          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          acl_onboard: Allowable Cabin Load (ACL) onboard the aircraft. The maximum weight of
              passengers, baggage, and cargo that can be safely transported in the aircraft
              cabin, in kilograms.

          acl_released: Allowable Cabin Load (ACL) released this leg. The weight of passengers, baggage,
              and cargo released from the aircraft cabin, in kilograms.

          aircraft_mds: The Model Design Series designation of the aircraft supporting this load plan.

          air_load_plan_hazmat_actuals: Collection of hazmat actuals associated with this load plan.

          air_load_plan_hr: Collection of human remains transport information associated with this load
              plan.

          air_load_plan_pallet_details: Collection of cargo information located at the pallet positions associated with
              this load plan.

          air_load_plan_pax_cargo: Collection of passenger and cargo details associated with this load plan for
              this leg of the mission.

          air_load_plan_uln_actuals: Collection of unit line number actuals associated with this load plan.

          arr_airfield: Optional identifier of arrival airfield with no International Civil Organization
              (ICAO) code.

          arr_icao: The arrival International Civil Organization (ICAO) code of the landing
              airfield.

          available_time: Time the loadmaster or boom operator is available for cargo loading/unloading,
              in ISO 8601 UTC format with millisecond precision.

          basic_moment: The basic weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          basic_weight: The weight of the aircraft without passengers, cargo, equipment, or usable fuel,
              in kilograms.

          brief_time: Time the cargo briefing was given to the loadmaster or boom operator, in ISO
              8601 UTC format with millisecond precision.

          call_sign: The call sign of the mission supporting this load plan.

          cargo_bay_fs_max: Maximum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_fs_min: Minimum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_width: Width of the cargo bay, in meters.

          cargo_config: The cargo configuration required for this leg (e.g. C-1, C-2, C-3, DV-1, DV-2,
              AE-1, etc.). Configuration meanings are determined by the data source.

          cargo_moment: The sum of cargo moments of all cargo on board the aircraft, in Newton-meters.
              Each individual cargo moment is the weight of the cargo multiplied by the
              distance between the reference datum and the cargo's center of gravity.

          cargo_volume: Volume of cargo space in the aircraft, in cubic meters.

          cargo_weight: The weight of the cargo on board the aircraft, in kilograms.

          crew_size: The number of crew members on the aircraft.

          dep_airfield: Optional identifier of departure airfield with no International Civil
              Organization (ICAO) code.

          dep_icao: The departure International Civil Organization (ICAO) code of the departure
              airfield.

          equip_config: Description of the equipment configuration (e.g. Standard, Ferry, JBLM, CHS,
              Combat, etc.). Configuration meanings are determined by the data source.

          est_arr_time: The current estimated time that the aircraft is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          est_landing_fuel_moment: The estimated weight of usable fuel upon landing multiplied by the distance
              between the reference datum and the fuel's center of gravity, in Newton-meters.

          est_landing_fuel_weight: The estimated weight of usable fuel upon landing, in kilograms.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          fuel_moment: The fuel weight on board the aircraft multiplied by the distance between the
              reference datum and the fuel's center of gravity, in Newton-meters.

          fuel_weight: The weight of usable fuel on board the aircraft, in kilograms.

          gross_cg: The center of gravity of the aircraft using the gross weight and gross moment,
              as a percentage of the mean aerodynamic chord (%MAC).

          gross_moment: The sum of moments of all items making up the gross weight of the aircraft, in
              Newton-meters.

          gross_weight: The total weight of the aircraft at takeoff including passengers, cargo,
              equipment, and usable fuel, in kilograms.

          id_mission: The UDL ID of the mission this record is associated with.

          id_sortie: The UDL ID of the aircraft sortie this record is associated with.

          landing_cg: The center of gravity of the aircraft using the landing weight and landing
              moment, as a percentage of the mean aerodynamic chord (%MAC).

          landing_moment: The sum of moments of all items making up the gross weight of the aircraft upon
              landing, in Newton-meters.

          landing_weight: The gross weight of the aircraft upon landing, in kilograms.

          leg_num: The leg number of the mission supporting this load plan.

          loadmaster_name: Name of the loadmaster or boom operator who received the cargo briefing.

          loadmaster_rank: Rank of the loadmaster or boom operator overseeing cargo loading/unloading.

          load_remarks: Remarks concerning this load plan.

          mission_number: The mission number of the mission supporting this load plan.

          operating_moment: The operating weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          operating_weight: The basic weight of the aircraft including passengers and equipment, in
              kilograms.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pp_onboard: Number of pallet positions on the aircraft.

          pp_released: Number of pallet positions released this leg.

          sched_time: Time the loadmaster or boom operator is scheduled to begin overseeing cargo
              loading/unloading, in ISO 8601 UTC format with millisecond precision.

          seats_onboard: Number of passenger seats on the aircraft.

          seats_released: Number of passenger seats released this leg.

          tail_number: The tail number of the aircraft supporting this load plan.

          tank_config: Description of the fuel tank(s) configuration (e.g. ER, NON-ER, etc.).
              Configuration meanings are determined by the data source.

          util_code: Alphanumeric code that describes general cargo-related utilization and
              characteristics for an itinerary point.

          zero_fuel_cg: The center of gravity of the aircraft using the zero fuel weight and zero fuel
              total moment, as a percentage of the mean aerodynamic chord (%MAC).

          zero_fuel_moment: The zero fuel weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          zero_fuel_weight: The operating weight of the aircraft including cargo, mail, baggage, and
              passengers, but without usable fuel, in kilograms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airloadplan",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "est_dep_time": est_dep_time,
                    "source": source,
                    "id": id,
                    "acl_onboard": acl_onboard,
                    "acl_released": acl_released,
                    "aircraft_mds": aircraft_mds,
                    "air_load_plan_hazmat_actuals": air_load_plan_hazmat_actuals,
                    "air_load_plan_hr": air_load_plan_hr,
                    "air_load_plan_pallet_details": air_load_plan_pallet_details,
                    "air_load_plan_pax_cargo": air_load_plan_pax_cargo,
                    "air_load_plan_uln_actuals": air_load_plan_uln_actuals,
                    "arr_airfield": arr_airfield,
                    "arr_icao": arr_icao,
                    "available_time": available_time,
                    "basic_moment": basic_moment,
                    "basic_weight": basic_weight,
                    "brief_time": brief_time,
                    "call_sign": call_sign,
                    "cargo_bay_fs_max": cargo_bay_fs_max,
                    "cargo_bay_fs_min": cargo_bay_fs_min,
                    "cargo_bay_width": cargo_bay_width,
                    "cargo_config": cargo_config,
                    "cargo_moment": cargo_moment,
                    "cargo_volume": cargo_volume,
                    "cargo_weight": cargo_weight,
                    "crew_size": crew_size,
                    "dep_airfield": dep_airfield,
                    "dep_icao": dep_icao,
                    "equip_config": equip_config,
                    "est_arr_time": est_arr_time,
                    "est_landing_fuel_moment": est_landing_fuel_moment,
                    "est_landing_fuel_weight": est_landing_fuel_weight,
                    "external_id": external_id,
                    "fuel_moment": fuel_moment,
                    "fuel_weight": fuel_weight,
                    "gross_cg": gross_cg,
                    "gross_moment": gross_moment,
                    "gross_weight": gross_weight,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "landing_cg": landing_cg,
                    "landing_moment": landing_moment,
                    "landing_weight": landing_weight,
                    "leg_num": leg_num,
                    "loadmaster_name": loadmaster_name,
                    "loadmaster_rank": loadmaster_rank,
                    "load_remarks": load_remarks,
                    "mission_number": mission_number,
                    "operating_moment": operating_moment,
                    "operating_weight": operating_weight,
                    "origin": origin,
                    "pp_onboard": pp_onboard,
                    "pp_released": pp_released,
                    "sched_time": sched_time,
                    "seats_onboard": seats_onboard,
                    "seats_released": seats_released,
                    "tail_number": tail_number,
                    "tank_config": tank_config,
                    "util_code": util_code,
                    "zero_fuel_cg": zero_fuel_cg,
                    "zero_fuel_moment": zero_fuel_moment,
                    "zero_fuel_weight": zero_fuel_weight,
                },
                airload_plan_create_params.AirloadPlanCreateParams,
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
    ) -> AirloadplanFull:
        """
        Service operation to get a single airloadplan record by its unique ID passed as
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
            f"/udl/airloadplan/{id}",
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
                    airload_plan_retrieve_params.AirloadPlanRetrieveParams,
                ),
            ),
            cast_to=AirloadplanFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        est_dep_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        acl_onboard: float | NotGiven = NOT_GIVEN,
        acl_released: float | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_load_plan_hazmat_actuals: Iterable[airload_plan_update_params.AirLoadPlanHazmatActual]
        | NotGiven = NOT_GIVEN,
        air_load_plan_hr: Iterable[airload_plan_update_params.AirLoadPlanHr] | NotGiven = NOT_GIVEN,
        air_load_plan_pallet_details: Iterable[airload_plan_update_params.AirLoadPlanPalletDetail]
        | NotGiven = NOT_GIVEN,
        air_load_plan_pax_cargo: Iterable[airload_plan_update_params.AirLoadPlanPaxCargo] | NotGiven = NOT_GIVEN,
        air_load_plan_uln_actuals: Iterable[airload_plan_update_params.AirLoadPlanUlnActual] | NotGiven = NOT_GIVEN,
        arr_airfield: str | NotGiven = NOT_GIVEN,
        arr_icao: str | NotGiven = NOT_GIVEN,
        available_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        basic_moment: float | NotGiven = NOT_GIVEN,
        basic_weight: float | NotGiven = NOT_GIVEN,
        brief_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_bay_fs_max: float | NotGiven = NOT_GIVEN,
        cargo_bay_fs_min: float | NotGiven = NOT_GIVEN,
        cargo_bay_width: float | NotGiven = NOT_GIVEN,
        cargo_config: str | NotGiven = NOT_GIVEN,
        cargo_moment: float | NotGiven = NOT_GIVEN,
        cargo_volume: float | NotGiven = NOT_GIVEN,
        cargo_weight: float | NotGiven = NOT_GIVEN,
        crew_size: int | NotGiven = NOT_GIVEN,
        dep_airfield: str | NotGiven = NOT_GIVEN,
        dep_icao: str | NotGiven = NOT_GIVEN,
        equip_config: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_landing_fuel_moment: float | NotGiven = NOT_GIVEN,
        est_landing_fuel_weight: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fuel_moment: float | NotGiven = NOT_GIVEN,
        fuel_weight: float | NotGiven = NOT_GIVEN,
        gross_cg: float | NotGiven = NOT_GIVEN,
        gross_moment: float | NotGiven = NOT_GIVEN,
        gross_weight: float | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        landing_cg: float | NotGiven = NOT_GIVEN,
        landing_moment: float | NotGiven = NOT_GIVEN,
        landing_weight: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        loadmaster_name: str | NotGiven = NOT_GIVEN,
        loadmaster_rank: str | NotGiven = NOT_GIVEN,
        load_remarks: str | NotGiven = NOT_GIVEN,
        mission_number: str | NotGiven = NOT_GIVEN,
        operating_moment: float | NotGiven = NOT_GIVEN,
        operating_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pp_onboard: int | NotGiven = NOT_GIVEN,
        pp_released: int | NotGiven = NOT_GIVEN,
        sched_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        seats_onboard: int | NotGiven = NOT_GIVEN,
        seats_released: int | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        tank_config: str | NotGiven = NOT_GIVEN,
        util_code: str | NotGiven = NOT_GIVEN,
        zero_fuel_cg: float | NotGiven = NOT_GIVEN,
        zero_fuel_moment: float | NotGiven = NOT_GIVEN,
        zero_fuel_weight: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single airloadplan record.

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

          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          acl_onboard: Allowable Cabin Load (ACL) onboard the aircraft. The maximum weight of
              passengers, baggage, and cargo that can be safely transported in the aircraft
              cabin, in kilograms.

          acl_released: Allowable Cabin Load (ACL) released this leg. The weight of passengers, baggage,
              and cargo released from the aircraft cabin, in kilograms.

          aircraft_mds: The Model Design Series designation of the aircraft supporting this load plan.

          air_load_plan_hazmat_actuals: Collection of hazmat actuals associated with this load plan.

          air_load_plan_hr: Collection of human remains transport information associated with this load
              plan.

          air_load_plan_pallet_details: Collection of cargo information located at the pallet positions associated with
              this load plan.

          air_load_plan_pax_cargo: Collection of passenger and cargo details associated with this load plan for
              this leg of the mission.

          air_load_plan_uln_actuals: Collection of unit line number actuals associated with this load plan.

          arr_airfield: Optional identifier of arrival airfield with no International Civil Organization
              (ICAO) code.

          arr_icao: The arrival International Civil Organization (ICAO) code of the landing
              airfield.

          available_time: Time the loadmaster or boom operator is available for cargo loading/unloading,
              in ISO 8601 UTC format with millisecond precision.

          basic_moment: The basic weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          basic_weight: The weight of the aircraft without passengers, cargo, equipment, or usable fuel,
              in kilograms.

          brief_time: Time the cargo briefing was given to the loadmaster or boom operator, in ISO
              8601 UTC format with millisecond precision.

          call_sign: The call sign of the mission supporting this load plan.

          cargo_bay_fs_max: Maximum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_fs_min: Minimum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_width: Width of the cargo bay, in meters.

          cargo_config: The cargo configuration required for this leg (e.g. C-1, C-2, C-3, DV-1, DV-2,
              AE-1, etc.). Configuration meanings are determined by the data source.

          cargo_moment: The sum of cargo moments of all cargo on board the aircraft, in Newton-meters.
              Each individual cargo moment is the weight of the cargo multiplied by the
              distance between the reference datum and the cargo's center of gravity.

          cargo_volume: Volume of cargo space in the aircraft, in cubic meters.

          cargo_weight: The weight of the cargo on board the aircraft, in kilograms.

          crew_size: The number of crew members on the aircraft.

          dep_airfield: Optional identifier of departure airfield with no International Civil
              Organization (ICAO) code.

          dep_icao: The departure International Civil Organization (ICAO) code of the departure
              airfield.

          equip_config: Description of the equipment configuration (e.g. Standard, Ferry, JBLM, CHS,
              Combat, etc.). Configuration meanings are determined by the data source.

          est_arr_time: The current estimated time that the aircraft is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          est_landing_fuel_moment: The estimated weight of usable fuel upon landing multiplied by the distance
              between the reference datum and the fuel's center of gravity, in Newton-meters.

          est_landing_fuel_weight: The estimated weight of usable fuel upon landing, in kilograms.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          fuel_moment: The fuel weight on board the aircraft multiplied by the distance between the
              reference datum and the fuel's center of gravity, in Newton-meters.

          fuel_weight: The weight of usable fuel on board the aircraft, in kilograms.

          gross_cg: The center of gravity of the aircraft using the gross weight and gross moment,
              as a percentage of the mean aerodynamic chord (%MAC).

          gross_moment: The sum of moments of all items making up the gross weight of the aircraft, in
              Newton-meters.

          gross_weight: The total weight of the aircraft at takeoff including passengers, cargo,
              equipment, and usable fuel, in kilograms.

          id_mission: The UDL ID of the mission this record is associated with.

          id_sortie: The UDL ID of the aircraft sortie this record is associated with.

          landing_cg: The center of gravity of the aircraft using the landing weight and landing
              moment, as a percentage of the mean aerodynamic chord (%MAC).

          landing_moment: The sum of moments of all items making up the gross weight of the aircraft upon
              landing, in Newton-meters.

          landing_weight: The gross weight of the aircraft upon landing, in kilograms.

          leg_num: The leg number of the mission supporting this load plan.

          loadmaster_name: Name of the loadmaster or boom operator who received the cargo briefing.

          loadmaster_rank: Rank of the loadmaster or boom operator overseeing cargo loading/unloading.

          load_remarks: Remarks concerning this load plan.

          mission_number: The mission number of the mission supporting this load plan.

          operating_moment: The operating weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          operating_weight: The basic weight of the aircraft including passengers and equipment, in
              kilograms.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pp_onboard: Number of pallet positions on the aircraft.

          pp_released: Number of pallet positions released this leg.

          sched_time: Time the loadmaster or boom operator is scheduled to begin overseeing cargo
              loading/unloading, in ISO 8601 UTC format with millisecond precision.

          seats_onboard: Number of passenger seats on the aircraft.

          seats_released: Number of passenger seats released this leg.

          tail_number: The tail number of the aircraft supporting this load plan.

          tank_config: Description of the fuel tank(s) configuration (e.g. ER, NON-ER, etc.).
              Configuration meanings are determined by the data source.

          util_code: Alphanumeric code that describes general cargo-related utilization and
              characteristics for an itinerary point.

          zero_fuel_cg: The center of gravity of the aircraft using the zero fuel weight and zero fuel
              total moment, as a percentage of the mean aerodynamic chord (%MAC).

          zero_fuel_moment: The zero fuel weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          zero_fuel_weight: The operating weight of the aircraft including cargo, mail, baggage, and
              passengers, but without usable fuel, in kilograms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/airloadplan/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "est_dep_time": est_dep_time,
                    "source": source,
                    "body_id": body_id,
                    "acl_onboard": acl_onboard,
                    "acl_released": acl_released,
                    "aircraft_mds": aircraft_mds,
                    "air_load_plan_hazmat_actuals": air_load_plan_hazmat_actuals,
                    "air_load_plan_hr": air_load_plan_hr,
                    "air_load_plan_pallet_details": air_load_plan_pallet_details,
                    "air_load_plan_pax_cargo": air_load_plan_pax_cargo,
                    "air_load_plan_uln_actuals": air_load_plan_uln_actuals,
                    "arr_airfield": arr_airfield,
                    "arr_icao": arr_icao,
                    "available_time": available_time,
                    "basic_moment": basic_moment,
                    "basic_weight": basic_weight,
                    "brief_time": brief_time,
                    "call_sign": call_sign,
                    "cargo_bay_fs_max": cargo_bay_fs_max,
                    "cargo_bay_fs_min": cargo_bay_fs_min,
                    "cargo_bay_width": cargo_bay_width,
                    "cargo_config": cargo_config,
                    "cargo_moment": cargo_moment,
                    "cargo_volume": cargo_volume,
                    "cargo_weight": cargo_weight,
                    "crew_size": crew_size,
                    "dep_airfield": dep_airfield,
                    "dep_icao": dep_icao,
                    "equip_config": equip_config,
                    "est_arr_time": est_arr_time,
                    "est_landing_fuel_moment": est_landing_fuel_moment,
                    "est_landing_fuel_weight": est_landing_fuel_weight,
                    "external_id": external_id,
                    "fuel_moment": fuel_moment,
                    "fuel_weight": fuel_weight,
                    "gross_cg": gross_cg,
                    "gross_moment": gross_moment,
                    "gross_weight": gross_weight,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "landing_cg": landing_cg,
                    "landing_moment": landing_moment,
                    "landing_weight": landing_weight,
                    "leg_num": leg_num,
                    "loadmaster_name": loadmaster_name,
                    "loadmaster_rank": loadmaster_rank,
                    "load_remarks": load_remarks,
                    "mission_number": mission_number,
                    "operating_moment": operating_moment,
                    "operating_weight": operating_weight,
                    "origin": origin,
                    "pp_onboard": pp_onboard,
                    "pp_released": pp_released,
                    "sched_time": sched_time,
                    "seats_onboard": seats_onboard,
                    "seats_released": seats_released,
                    "tail_number": tail_number,
                    "tank_config": tank_config,
                    "util_code": util_code,
                    "zero_fuel_cg": zero_fuel_cg,
                    "zero_fuel_moment": zero_fuel_moment,
                    "zero_fuel_weight": zero_fuel_weight,
                },
                airload_plan_update_params.AirloadPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        est_dep_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[AirloadplanAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/airloadplan",
            page=SyncOffsetPage[AirloadplanAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "est_dep_time": est_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airload_plan_list_params.AirloadPlanListParams,
                ),
            ),
            model=AirloadplanAbridged,
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
        Service operation to delete a airloadplan record specified by the passed ID path
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
            f"/udl/airloadplan/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        est_dep_time: Union[str, datetime],
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
          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/airloadplan/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "est_dep_time": est_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airload_plan_count_params.AirloadPlanCountParams,
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
    ) -> AirloadPlanQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/airloadplan/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirloadPlanQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        est_dep_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirloadPlanTupleResponse:
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

          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/airloadplan/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "est_dep_time": est_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airload_plan_tuple_params.AirloadPlanTupleParams,
                ),
            ),
            cast_to=AirloadPlanTupleResponse,
        )


class AsyncAirloadPlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAirloadPlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirloadPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirloadPlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirloadPlansResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        est_dep_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        acl_onboard: float | NotGiven = NOT_GIVEN,
        acl_released: float | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_load_plan_hazmat_actuals: Iterable[airload_plan_create_params.AirLoadPlanHazmatActual]
        | NotGiven = NOT_GIVEN,
        air_load_plan_hr: Iterable[airload_plan_create_params.AirLoadPlanHr] | NotGiven = NOT_GIVEN,
        air_load_plan_pallet_details: Iterable[airload_plan_create_params.AirLoadPlanPalletDetail]
        | NotGiven = NOT_GIVEN,
        air_load_plan_pax_cargo: Iterable[airload_plan_create_params.AirLoadPlanPaxCargo] | NotGiven = NOT_GIVEN,
        air_load_plan_uln_actuals: Iterable[airload_plan_create_params.AirLoadPlanUlnActual] | NotGiven = NOT_GIVEN,
        arr_airfield: str | NotGiven = NOT_GIVEN,
        arr_icao: str | NotGiven = NOT_GIVEN,
        available_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        basic_moment: float | NotGiven = NOT_GIVEN,
        basic_weight: float | NotGiven = NOT_GIVEN,
        brief_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_bay_fs_max: float | NotGiven = NOT_GIVEN,
        cargo_bay_fs_min: float | NotGiven = NOT_GIVEN,
        cargo_bay_width: float | NotGiven = NOT_GIVEN,
        cargo_config: str | NotGiven = NOT_GIVEN,
        cargo_moment: float | NotGiven = NOT_GIVEN,
        cargo_volume: float | NotGiven = NOT_GIVEN,
        cargo_weight: float | NotGiven = NOT_GIVEN,
        crew_size: int | NotGiven = NOT_GIVEN,
        dep_airfield: str | NotGiven = NOT_GIVEN,
        dep_icao: str | NotGiven = NOT_GIVEN,
        equip_config: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_landing_fuel_moment: float | NotGiven = NOT_GIVEN,
        est_landing_fuel_weight: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fuel_moment: float | NotGiven = NOT_GIVEN,
        fuel_weight: float | NotGiven = NOT_GIVEN,
        gross_cg: float | NotGiven = NOT_GIVEN,
        gross_moment: float | NotGiven = NOT_GIVEN,
        gross_weight: float | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        landing_cg: float | NotGiven = NOT_GIVEN,
        landing_moment: float | NotGiven = NOT_GIVEN,
        landing_weight: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        loadmaster_name: str | NotGiven = NOT_GIVEN,
        loadmaster_rank: str | NotGiven = NOT_GIVEN,
        load_remarks: str | NotGiven = NOT_GIVEN,
        mission_number: str | NotGiven = NOT_GIVEN,
        operating_moment: float | NotGiven = NOT_GIVEN,
        operating_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pp_onboard: int | NotGiven = NOT_GIVEN,
        pp_released: int | NotGiven = NOT_GIVEN,
        sched_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        seats_onboard: int | NotGiven = NOT_GIVEN,
        seats_released: int | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        tank_config: str | NotGiven = NOT_GIVEN,
        util_code: str | NotGiven = NOT_GIVEN,
        zero_fuel_cg: float | NotGiven = NOT_GIVEN,
        zero_fuel_moment: float | NotGiven = NOT_GIVEN,
        zero_fuel_weight: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airloadplan record as a POST body and ingest
        into the database. A specific role is required to perform this service
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

          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          acl_onboard: Allowable Cabin Load (ACL) onboard the aircraft. The maximum weight of
              passengers, baggage, and cargo that can be safely transported in the aircraft
              cabin, in kilograms.

          acl_released: Allowable Cabin Load (ACL) released this leg. The weight of passengers, baggage,
              and cargo released from the aircraft cabin, in kilograms.

          aircraft_mds: The Model Design Series designation of the aircraft supporting this load plan.

          air_load_plan_hazmat_actuals: Collection of hazmat actuals associated with this load plan.

          air_load_plan_hr: Collection of human remains transport information associated with this load
              plan.

          air_load_plan_pallet_details: Collection of cargo information located at the pallet positions associated with
              this load plan.

          air_load_plan_pax_cargo: Collection of passenger and cargo details associated with this load plan for
              this leg of the mission.

          air_load_plan_uln_actuals: Collection of unit line number actuals associated with this load plan.

          arr_airfield: Optional identifier of arrival airfield with no International Civil Organization
              (ICAO) code.

          arr_icao: The arrival International Civil Organization (ICAO) code of the landing
              airfield.

          available_time: Time the loadmaster or boom operator is available for cargo loading/unloading,
              in ISO 8601 UTC format with millisecond precision.

          basic_moment: The basic weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          basic_weight: The weight of the aircraft without passengers, cargo, equipment, or usable fuel,
              in kilograms.

          brief_time: Time the cargo briefing was given to the loadmaster or boom operator, in ISO
              8601 UTC format with millisecond precision.

          call_sign: The call sign of the mission supporting this load plan.

          cargo_bay_fs_max: Maximum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_fs_min: Minimum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_width: Width of the cargo bay, in meters.

          cargo_config: The cargo configuration required for this leg (e.g. C-1, C-2, C-3, DV-1, DV-2,
              AE-1, etc.). Configuration meanings are determined by the data source.

          cargo_moment: The sum of cargo moments of all cargo on board the aircraft, in Newton-meters.
              Each individual cargo moment is the weight of the cargo multiplied by the
              distance between the reference datum and the cargo's center of gravity.

          cargo_volume: Volume of cargo space in the aircraft, in cubic meters.

          cargo_weight: The weight of the cargo on board the aircraft, in kilograms.

          crew_size: The number of crew members on the aircraft.

          dep_airfield: Optional identifier of departure airfield with no International Civil
              Organization (ICAO) code.

          dep_icao: The departure International Civil Organization (ICAO) code of the departure
              airfield.

          equip_config: Description of the equipment configuration (e.g. Standard, Ferry, JBLM, CHS,
              Combat, etc.). Configuration meanings are determined by the data source.

          est_arr_time: The current estimated time that the aircraft is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          est_landing_fuel_moment: The estimated weight of usable fuel upon landing multiplied by the distance
              between the reference datum and the fuel's center of gravity, in Newton-meters.

          est_landing_fuel_weight: The estimated weight of usable fuel upon landing, in kilograms.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          fuel_moment: The fuel weight on board the aircraft multiplied by the distance between the
              reference datum and the fuel's center of gravity, in Newton-meters.

          fuel_weight: The weight of usable fuel on board the aircraft, in kilograms.

          gross_cg: The center of gravity of the aircraft using the gross weight and gross moment,
              as a percentage of the mean aerodynamic chord (%MAC).

          gross_moment: The sum of moments of all items making up the gross weight of the aircraft, in
              Newton-meters.

          gross_weight: The total weight of the aircraft at takeoff including passengers, cargo,
              equipment, and usable fuel, in kilograms.

          id_mission: The UDL ID of the mission this record is associated with.

          id_sortie: The UDL ID of the aircraft sortie this record is associated with.

          landing_cg: The center of gravity of the aircraft using the landing weight and landing
              moment, as a percentage of the mean aerodynamic chord (%MAC).

          landing_moment: The sum of moments of all items making up the gross weight of the aircraft upon
              landing, in Newton-meters.

          landing_weight: The gross weight of the aircraft upon landing, in kilograms.

          leg_num: The leg number of the mission supporting this load plan.

          loadmaster_name: Name of the loadmaster or boom operator who received the cargo briefing.

          loadmaster_rank: Rank of the loadmaster or boom operator overseeing cargo loading/unloading.

          load_remarks: Remarks concerning this load plan.

          mission_number: The mission number of the mission supporting this load plan.

          operating_moment: The operating weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          operating_weight: The basic weight of the aircraft including passengers and equipment, in
              kilograms.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pp_onboard: Number of pallet positions on the aircraft.

          pp_released: Number of pallet positions released this leg.

          sched_time: Time the loadmaster or boom operator is scheduled to begin overseeing cargo
              loading/unloading, in ISO 8601 UTC format with millisecond precision.

          seats_onboard: Number of passenger seats on the aircraft.

          seats_released: Number of passenger seats released this leg.

          tail_number: The tail number of the aircraft supporting this load plan.

          tank_config: Description of the fuel tank(s) configuration (e.g. ER, NON-ER, etc.).
              Configuration meanings are determined by the data source.

          util_code: Alphanumeric code that describes general cargo-related utilization and
              characteristics for an itinerary point.

          zero_fuel_cg: The center of gravity of the aircraft using the zero fuel weight and zero fuel
              total moment, as a percentage of the mean aerodynamic chord (%MAC).

          zero_fuel_moment: The zero fuel weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          zero_fuel_weight: The operating weight of the aircraft including cargo, mail, baggage, and
              passengers, but without usable fuel, in kilograms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airloadplan",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "est_dep_time": est_dep_time,
                    "source": source,
                    "id": id,
                    "acl_onboard": acl_onboard,
                    "acl_released": acl_released,
                    "aircraft_mds": aircraft_mds,
                    "air_load_plan_hazmat_actuals": air_load_plan_hazmat_actuals,
                    "air_load_plan_hr": air_load_plan_hr,
                    "air_load_plan_pallet_details": air_load_plan_pallet_details,
                    "air_load_plan_pax_cargo": air_load_plan_pax_cargo,
                    "air_load_plan_uln_actuals": air_load_plan_uln_actuals,
                    "arr_airfield": arr_airfield,
                    "arr_icao": arr_icao,
                    "available_time": available_time,
                    "basic_moment": basic_moment,
                    "basic_weight": basic_weight,
                    "brief_time": brief_time,
                    "call_sign": call_sign,
                    "cargo_bay_fs_max": cargo_bay_fs_max,
                    "cargo_bay_fs_min": cargo_bay_fs_min,
                    "cargo_bay_width": cargo_bay_width,
                    "cargo_config": cargo_config,
                    "cargo_moment": cargo_moment,
                    "cargo_volume": cargo_volume,
                    "cargo_weight": cargo_weight,
                    "crew_size": crew_size,
                    "dep_airfield": dep_airfield,
                    "dep_icao": dep_icao,
                    "equip_config": equip_config,
                    "est_arr_time": est_arr_time,
                    "est_landing_fuel_moment": est_landing_fuel_moment,
                    "est_landing_fuel_weight": est_landing_fuel_weight,
                    "external_id": external_id,
                    "fuel_moment": fuel_moment,
                    "fuel_weight": fuel_weight,
                    "gross_cg": gross_cg,
                    "gross_moment": gross_moment,
                    "gross_weight": gross_weight,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "landing_cg": landing_cg,
                    "landing_moment": landing_moment,
                    "landing_weight": landing_weight,
                    "leg_num": leg_num,
                    "loadmaster_name": loadmaster_name,
                    "loadmaster_rank": loadmaster_rank,
                    "load_remarks": load_remarks,
                    "mission_number": mission_number,
                    "operating_moment": operating_moment,
                    "operating_weight": operating_weight,
                    "origin": origin,
                    "pp_onboard": pp_onboard,
                    "pp_released": pp_released,
                    "sched_time": sched_time,
                    "seats_onboard": seats_onboard,
                    "seats_released": seats_released,
                    "tail_number": tail_number,
                    "tank_config": tank_config,
                    "util_code": util_code,
                    "zero_fuel_cg": zero_fuel_cg,
                    "zero_fuel_moment": zero_fuel_moment,
                    "zero_fuel_weight": zero_fuel_weight,
                },
                airload_plan_create_params.AirloadPlanCreateParams,
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
    ) -> AirloadplanFull:
        """
        Service operation to get a single airloadplan record by its unique ID passed as
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
            f"/udl/airloadplan/{id}",
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
                    airload_plan_retrieve_params.AirloadPlanRetrieveParams,
                ),
            ),
            cast_to=AirloadplanFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        est_dep_time: Union[str, datetime],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        acl_onboard: float | NotGiven = NOT_GIVEN,
        acl_released: float | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        air_load_plan_hazmat_actuals: Iterable[airload_plan_update_params.AirLoadPlanHazmatActual]
        | NotGiven = NOT_GIVEN,
        air_load_plan_hr: Iterable[airload_plan_update_params.AirLoadPlanHr] | NotGiven = NOT_GIVEN,
        air_load_plan_pallet_details: Iterable[airload_plan_update_params.AirLoadPlanPalletDetail]
        | NotGiven = NOT_GIVEN,
        air_load_plan_pax_cargo: Iterable[airload_plan_update_params.AirLoadPlanPaxCargo] | NotGiven = NOT_GIVEN,
        air_load_plan_uln_actuals: Iterable[airload_plan_update_params.AirLoadPlanUlnActual] | NotGiven = NOT_GIVEN,
        arr_airfield: str | NotGiven = NOT_GIVEN,
        arr_icao: str | NotGiven = NOT_GIVEN,
        available_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        basic_moment: float | NotGiven = NOT_GIVEN,
        basic_weight: float | NotGiven = NOT_GIVEN,
        brief_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cargo_bay_fs_max: float | NotGiven = NOT_GIVEN,
        cargo_bay_fs_min: float | NotGiven = NOT_GIVEN,
        cargo_bay_width: float | NotGiven = NOT_GIVEN,
        cargo_config: str | NotGiven = NOT_GIVEN,
        cargo_moment: float | NotGiven = NOT_GIVEN,
        cargo_volume: float | NotGiven = NOT_GIVEN,
        cargo_weight: float | NotGiven = NOT_GIVEN,
        crew_size: int | NotGiven = NOT_GIVEN,
        dep_airfield: str | NotGiven = NOT_GIVEN,
        dep_icao: str | NotGiven = NOT_GIVEN,
        equip_config: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_landing_fuel_moment: float | NotGiven = NOT_GIVEN,
        est_landing_fuel_weight: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fuel_moment: float | NotGiven = NOT_GIVEN,
        fuel_weight: float | NotGiven = NOT_GIVEN,
        gross_cg: float | NotGiven = NOT_GIVEN,
        gross_moment: float | NotGiven = NOT_GIVEN,
        gross_weight: float | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        landing_cg: float | NotGiven = NOT_GIVEN,
        landing_moment: float | NotGiven = NOT_GIVEN,
        landing_weight: float | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        loadmaster_name: str | NotGiven = NOT_GIVEN,
        loadmaster_rank: str | NotGiven = NOT_GIVEN,
        load_remarks: str | NotGiven = NOT_GIVEN,
        mission_number: str | NotGiven = NOT_GIVEN,
        operating_moment: float | NotGiven = NOT_GIVEN,
        operating_weight: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        pp_onboard: int | NotGiven = NOT_GIVEN,
        pp_released: int | NotGiven = NOT_GIVEN,
        sched_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        seats_onboard: int | NotGiven = NOT_GIVEN,
        seats_released: int | NotGiven = NOT_GIVEN,
        tail_number: str | NotGiven = NOT_GIVEN,
        tank_config: str | NotGiven = NOT_GIVEN,
        util_code: str | NotGiven = NOT_GIVEN,
        zero_fuel_cg: float | NotGiven = NOT_GIVEN,
        zero_fuel_moment: float | NotGiven = NOT_GIVEN,
        zero_fuel_weight: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single airloadplan record.

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

          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          acl_onboard: Allowable Cabin Load (ACL) onboard the aircraft. The maximum weight of
              passengers, baggage, and cargo that can be safely transported in the aircraft
              cabin, in kilograms.

          acl_released: Allowable Cabin Load (ACL) released this leg. The weight of passengers, baggage,
              and cargo released from the aircraft cabin, in kilograms.

          aircraft_mds: The Model Design Series designation of the aircraft supporting this load plan.

          air_load_plan_hazmat_actuals: Collection of hazmat actuals associated with this load plan.

          air_load_plan_hr: Collection of human remains transport information associated with this load
              plan.

          air_load_plan_pallet_details: Collection of cargo information located at the pallet positions associated with
              this load plan.

          air_load_plan_pax_cargo: Collection of passenger and cargo details associated with this load plan for
              this leg of the mission.

          air_load_plan_uln_actuals: Collection of unit line number actuals associated with this load plan.

          arr_airfield: Optional identifier of arrival airfield with no International Civil Organization
              (ICAO) code.

          arr_icao: The arrival International Civil Organization (ICAO) code of the landing
              airfield.

          available_time: Time the loadmaster or boom operator is available for cargo loading/unloading,
              in ISO 8601 UTC format with millisecond precision.

          basic_moment: The basic weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          basic_weight: The weight of the aircraft without passengers, cargo, equipment, or usable fuel,
              in kilograms.

          brief_time: Time the cargo briefing was given to the loadmaster or boom operator, in ISO
              8601 UTC format with millisecond precision.

          call_sign: The call sign of the mission supporting this load plan.

          cargo_bay_fs_max: Maximum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_fs_min: Minimum fuselage station (FS) where cargo can be stored. FS is the distance from
              the reference datum, in meters.

          cargo_bay_width: Width of the cargo bay, in meters.

          cargo_config: The cargo configuration required for this leg (e.g. C-1, C-2, C-3, DV-1, DV-2,
              AE-1, etc.). Configuration meanings are determined by the data source.

          cargo_moment: The sum of cargo moments of all cargo on board the aircraft, in Newton-meters.
              Each individual cargo moment is the weight of the cargo multiplied by the
              distance between the reference datum and the cargo's center of gravity.

          cargo_volume: Volume of cargo space in the aircraft, in cubic meters.

          cargo_weight: The weight of the cargo on board the aircraft, in kilograms.

          crew_size: The number of crew members on the aircraft.

          dep_airfield: Optional identifier of departure airfield with no International Civil
              Organization (ICAO) code.

          dep_icao: The departure International Civil Organization (ICAO) code of the departure
              airfield.

          equip_config: Description of the equipment configuration (e.g. Standard, Ferry, JBLM, CHS,
              Combat, etc.). Configuration meanings are determined by the data source.

          est_arr_time: The current estimated time that the aircraft is planned to arrive, in ISO 8601
              UTC format with millisecond precision.

          est_landing_fuel_moment: The estimated weight of usable fuel upon landing multiplied by the distance
              between the reference datum and the fuel's center of gravity, in Newton-meters.

          est_landing_fuel_weight: The estimated weight of usable fuel upon landing, in kilograms.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          fuel_moment: The fuel weight on board the aircraft multiplied by the distance between the
              reference datum and the fuel's center of gravity, in Newton-meters.

          fuel_weight: The weight of usable fuel on board the aircraft, in kilograms.

          gross_cg: The center of gravity of the aircraft using the gross weight and gross moment,
              as a percentage of the mean aerodynamic chord (%MAC).

          gross_moment: The sum of moments of all items making up the gross weight of the aircraft, in
              Newton-meters.

          gross_weight: The total weight of the aircraft at takeoff including passengers, cargo,
              equipment, and usable fuel, in kilograms.

          id_mission: The UDL ID of the mission this record is associated with.

          id_sortie: The UDL ID of the aircraft sortie this record is associated with.

          landing_cg: The center of gravity of the aircraft using the landing weight and landing
              moment, as a percentage of the mean aerodynamic chord (%MAC).

          landing_moment: The sum of moments of all items making up the gross weight of the aircraft upon
              landing, in Newton-meters.

          landing_weight: The gross weight of the aircraft upon landing, in kilograms.

          leg_num: The leg number of the mission supporting this load plan.

          loadmaster_name: Name of the loadmaster or boom operator who received the cargo briefing.

          loadmaster_rank: Rank of the loadmaster or boom operator overseeing cargo loading/unloading.

          load_remarks: Remarks concerning this load plan.

          mission_number: The mission number of the mission supporting this load plan.

          operating_moment: The operating weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          operating_weight: The basic weight of the aircraft including passengers and equipment, in
              kilograms.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          pp_onboard: Number of pallet positions on the aircraft.

          pp_released: Number of pallet positions released this leg.

          sched_time: Time the loadmaster or boom operator is scheduled to begin overseeing cargo
              loading/unloading, in ISO 8601 UTC format with millisecond precision.

          seats_onboard: Number of passenger seats on the aircraft.

          seats_released: Number of passenger seats released this leg.

          tail_number: The tail number of the aircraft supporting this load plan.

          tank_config: Description of the fuel tank(s) configuration (e.g. ER, NON-ER, etc.).
              Configuration meanings are determined by the data source.

          util_code: Alphanumeric code that describes general cargo-related utilization and
              characteristics for an itinerary point.

          zero_fuel_cg: The center of gravity of the aircraft using the zero fuel weight and zero fuel
              total moment, as a percentage of the mean aerodynamic chord (%MAC).

          zero_fuel_moment: The zero fuel weight of the aircraft multiplied by the distance between the
              reference datum and the aircraft's center of gravity, in Newton-meters.

          zero_fuel_weight: The operating weight of the aircraft including cargo, mail, baggage, and
              passengers, but without usable fuel, in kilograms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/airloadplan/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "est_dep_time": est_dep_time,
                    "source": source,
                    "body_id": body_id,
                    "acl_onboard": acl_onboard,
                    "acl_released": acl_released,
                    "aircraft_mds": aircraft_mds,
                    "air_load_plan_hazmat_actuals": air_load_plan_hazmat_actuals,
                    "air_load_plan_hr": air_load_plan_hr,
                    "air_load_plan_pallet_details": air_load_plan_pallet_details,
                    "air_load_plan_pax_cargo": air_load_plan_pax_cargo,
                    "air_load_plan_uln_actuals": air_load_plan_uln_actuals,
                    "arr_airfield": arr_airfield,
                    "arr_icao": arr_icao,
                    "available_time": available_time,
                    "basic_moment": basic_moment,
                    "basic_weight": basic_weight,
                    "brief_time": brief_time,
                    "call_sign": call_sign,
                    "cargo_bay_fs_max": cargo_bay_fs_max,
                    "cargo_bay_fs_min": cargo_bay_fs_min,
                    "cargo_bay_width": cargo_bay_width,
                    "cargo_config": cargo_config,
                    "cargo_moment": cargo_moment,
                    "cargo_volume": cargo_volume,
                    "cargo_weight": cargo_weight,
                    "crew_size": crew_size,
                    "dep_airfield": dep_airfield,
                    "dep_icao": dep_icao,
                    "equip_config": equip_config,
                    "est_arr_time": est_arr_time,
                    "est_landing_fuel_moment": est_landing_fuel_moment,
                    "est_landing_fuel_weight": est_landing_fuel_weight,
                    "external_id": external_id,
                    "fuel_moment": fuel_moment,
                    "fuel_weight": fuel_weight,
                    "gross_cg": gross_cg,
                    "gross_moment": gross_moment,
                    "gross_weight": gross_weight,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "landing_cg": landing_cg,
                    "landing_moment": landing_moment,
                    "landing_weight": landing_weight,
                    "leg_num": leg_num,
                    "loadmaster_name": loadmaster_name,
                    "loadmaster_rank": loadmaster_rank,
                    "load_remarks": load_remarks,
                    "mission_number": mission_number,
                    "operating_moment": operating_moment,
                    "operating_weight": operating_weight,
                    "origin": origin,
                    "pp_onboard": pp_onboard,
                    "pp_released": pp_released,
                    "sched_time": sched_time,
                    "seats_onboard": seats_onboard,
                    "seats_released": seats_released,
                    "tail_number": tail_number,
                    "tank_config": tank_config,
                    "util_code": util_code,
                    "zero_fuel_cg": zero_fuel_cg,
                    "zero_fuel_moment": zero_fuel_moment,
                    "zero_fuel_weight": zero_fuel_weight,
                },
                airload_plan_update_params.AirloadPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        est_dep_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AirloadplanAbridged, AsyncOffsetPage[AirloadplanAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/airloadplan",
            page=AsyncOffsetPage[AirloadplanAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "est_dep_time": est_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airload_plan_list_params.AirloadPlanListParams,
                ),
            ),
            model=AirloadplanAbridged,
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
        Service operation to delete a airloadplan record specified by the passed ID path
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
            f"/udl/airloadplan/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        est_dep_time: Union[str, datetime],
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
          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/airloadplan/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "est_dep_time": est_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airload_plan_count_params.AirloadPlanCountParams,
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
    ) -> AirloadPlanQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/airloadplan/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirloadPlanQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        est_dep_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirloadPlanTupleResponse:
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

          est_dep_time: The current estimated time that the aircraft is planned to depart, in ISO 8601
              UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/airloadplan/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "est_dep_time": est_dep_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    airload_plan_tuple_params.AirloadPlanTupleParams,
                ),
            ),
            cast_to=AirloadPlanTupleResponse,
        )


class AirloadPlansResourceWithRawResponse:
    def __init__(self, airload_plans: AirloadPlansResource) -> None:
        self._airload_plans = airload_plans

        self.create = to_raw_response_wrapper(
            airload_plans.create,
        )
        self.retrieve = to_raw_response_wrapper(
            airload_plans.retrieve,
        )
        self.update = to_raw_response_wrapper(
            airload_plans.update,
        )
        self.list = to_raw_response_wrapper(
            airload_plans.list,
        )
        self.delete = to_raw_response_wrapper(
            airload_plans.delete,
        )
        self.count = to_raw_response_wrapper(
            airload_plans.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            airload_plans.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            airload_plans.tuple,
        )


class AsyncAirloadPlansResourceWithRawResponse:
    def __init__(self, airload_plans: AsyncAirloadPlansResource) -> None:
        self._airload_plans = airload_plans

        self.create = async_to_raw_response_wrapper(
            airload_plans.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            airload_plans.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            airload_plans.update,
        )
        self.list = async_to_raw_response_wrapper(
            airload_plans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            airload_plans.delete,
        )
        self.count = async_to_raw_response_wrapper(
            airload_plans.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            airload_plans.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            airload_plans.tuple,
        )


class AirloadPlansResourceWithStreamingResponse:
    def __init__(self, airload_plans: AirloadPlansResource) -> None:
        self._airload_plans = airload_plans

        self.create = to_streamed_response_wrapper(
            airload_plans.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            airload_plans.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            airload_plans.update,
        )
        self.list = to_streamed_response_wrapper(
            airload_plans.list,
        )
        self.delete = to_streamed_response_wrapper(
            airload_plans.delete,
        )
        self.count = to_streamed_response_wrapper(
            airload_plans.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            airload_plans.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            airload_plans.tuple,
        )


class AsyncAirloadPlansResourceWithStreamingResponse:
    def __init__(self, airload_plans: AsyncAirloadPlansResource) -> None:
        self._airload_plans = airload_plans

        self.create = async_to_streamed_response_wrapper(
            airload_plans.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            airload_plans.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            airload_plans.update,
        )
        self.list = async_to_streamed_response_wrapper(
            airload_plans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            airload_plans.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            airload_plans.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            airload_plans.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            airload_plans.tuple,
        )
