# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    aircraft_status_list_params,
    aircraft_status_count_params,
    aircraft_status_tuple_params,
    aircraft_status_create_params,
    aircraft_status_update_params,
    aircraft_status_retrieve_params,
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
from ...types.aircraftstatus_abridged import AircraftstatusAbridged
from ...types.shared.aircraftstatus_full import AircraftstatusFull
from ...types.aircraft_status_tuple_response import AircraftStatusTupleResponse

__all__ = ["AircraftStatusesResource", "AsyncAircraftStatusesResource"]


class AircraftStatusesResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AircraftStatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AircraftStatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AircraftStatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AircraftStatusesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_aircraft: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        additional_sys: List[str] | NotGiven = NOT_GIVEN,
        air_to_air_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        air_to_ground_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        alpha_status_code: str | NotGiven = NOT_GIVEN,
        alt_aircraft_id: str | NotGiven = NOT_GIVEN,
        contamination_status: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        current_state: str | NotGiven = NOT_GIVEN,
        earliest_ta_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flight_phase: str | NotGiven = NOT_GIVEN,
        fuel: int | NotGiven = NOT_GIVEN,
        fuel_function: str | NotGiven = NOT_GIVEN,
        fuel_status: str | NotGiven = NOT_GIVEN,
        geo_loc: str | NotGiven = NOT_GIVEN,
        ground_status: str | NotGiven = NOT_GIVEN,
        gun_capable: bool | NotGiven = NOT_GIVEN,
        gun_rds_max: int | NotGiven = NOT_GIVEN,
        gun_rds_min: int | NotGiven = NOT_GIVEN,
        gun_rds_type: str | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        id_poi: str | NotGiven = NOT_GIVEN,
        inventory: List[str] | NotGiven = NOT_GIVEN,
        inventory_max: Iterable[int] | NotGiven = NOT_GIVEN,
        inventory_min: Iterable[int] | NotGiven = NOT_GIVEN,
        last_inspection_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_updated_by: str | NotGiven = NOT_GIVEN,
        maint_poc: str | NotGiven = NOT_GIVEN,
        maint_priority: str | NotGiven = NOT_GIVEN,
        maint_status: str | NotGiven = NOT_GIVEN,
        maint_status_driver: str | NotGiven = NOT_GIVEN,
        maint_status_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mission_readiness: str | NotGiven = NOT_GIVEN,
        mx_remark: str | NotGiven = NOT_GIVEN,
        next_icao: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        park_location: str | NotGiven = NOT_GIVEN,
        park_location_system: str | NotGiven = NOT_GIVEN,
        previous_icao: str | NotGiven = NOT_GIVEN,
        ta_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        troubleshoot_etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        unavailable_sys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single AircraftStatus as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
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

          id_aircraft: Unique identifier of the aircraft.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          additional_sys: List of additional operational systems on this aircraft beyond what is normally
              available.

          air_to_air_status: The status of the air-to-air weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          air_to_ground_status: The status of the air-to-ground weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          alpha_status_code: Aircraft alpha status code that indicates the aircraft maintenance status
              estimated by the pilot.

          alt_aircraft_id: Alternate Aircraft Identifier provided by source.

          contamination_status: The contamination status of the aircraft (e.g. CLEAR, CONTAMINATED,
              DECONTAMINATED, UNKNOWN, etc.).

          current_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              is currently located or has most recently departed, if airborne.

          current_state: The current readiness state of the aircraft (e.g. AIRBORNE, ALERTCOCKED,
              AVAILABLE, BATTLESTATION, RUNWAY ALERT, SUITUP).

          earliest_ta_end_time: The earliest time that turnaround of the aircraft may complete, in ISO 8601 UTC
              format with millisecond precision.

          etic: The Expected Time in Commission (ETIC) for this aircraft, in ISO 8601 UTC format
              with millisecond precision. This is the estimated time when the issue will be
              resolved.

          flight_phase: Current flight phase (e.g. AIR REFUELING, GROUND, LANDING, etc.) of the
              aircraft.

          fuel: The mass of fuel remaining on the aircraft, in kilograms.

          fuel_function: Used in conjunction with the fuel field to indicate either burnable or offload
              fuel.

          fuel_status: The state of the aircraft fuel status (e.g. DELIVERED, DUMPED, EMPTY, FULL,
              OTHER, REQUESTED, etc.).

          geo_loc: US Air Force geographic location code of the airfield where the aircraft is
              located.

          ground_status: The ground status of the aircraft (e.g. ALERT, CREW READY, ENGINE START, HANGAR,
              etc.).

          gun_capable: Flag indicating that the aircraft is capable of making at least one gun pass.

          gun_rds_max: The upper bound of the estimated number of gun rounds available.

          gun_rds_min: The lower bound of the estimated number of gun rounds available.

          gun_rds_type: The type of gun rounds available (e.g. 7.62 MM, 20 MM, 25 MM, etc.).

          id_airfield: If not airborne, the unique identifier of the installation currently hosting the
              aircraft.

          id_poi: Unique identifier of the Point of Interest (POI) record related to this aircraft
              status. This will generally represent the location of an aircraft on the ground.

          inventory: Array of inventory item(s) for which estimate(s) are available (e.g. AIM-9
              SIDEWINDER, AIM-120 AMRAAM, AIM-92 STINGER, CHAFF DECOY, FLARE TP 400, etc.).
              Intended as, but not constrained to, MIL-STD-6016 environment dependent
              specific/store type designations. This array must be the same length as
              inventoryMin and inventoryMax.

          inventory_max: Array of the upper bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMin.

          inventory_min: Array of the lower bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMax.

          last_inspection_date: Date when the military aircraft inspection was last performed, in ISO 8601 UTC
              format with millisecond precision.

          last_updated_by: The name or ID of the external user that updated this status.

          maint_poc: Military aircraft maintenance point of contact for this aircraft.

          maint_priority: Indicates the priority of the maintenance effort.

          maint_status: The maintenance status of the aircraft.

          maint_status_driver: Indicates the maintenance discrepancy that drives the current maintenance
              status.

          maint_status_update: The time of the last maintenance status update, in ISO 8601 UTC format with
              millisecond precision.

          mission_readiness: The Operational Capability of the reported aircraft (ABLE, LOFUEL, UNABLE).

          mx_remark: Maintenance pacing remarks assocociated with this aircraft.

          next_icao: The International Civil Aviation Organization (ICAO) code of the next
              destination of this aircraft.

          notes: Optional notes/comments concerning this aircraft status.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          park_location: The parking location of this aircraft.

          park_location_system: The system that designated the parking location (e.g. EMOC, GDSS, PEX, etc.).

          previous_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              was previously located.

          ta_start_time: The turnaround start time, in ISO 8601 UTC format with millisecond precision.

          troubleshoot_etic: Estimated Time for Completion (ETIC) of an aircraft issue, in ISO 8601 UTC
              format with millisecond precision. This is the estimated time when the course of
              action to resolve the issue will be determined.

          unavailable_sys: List of unavailable systems that would normally be on this aircraft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/aircraftstatus",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_aircraft": id_aircraft,
                    "source": source,
                    "id": id,
                    "additional_sys": additional_sys,
                    "air_to_air_status": air_to_air_status,
                    "air_to_ground_status": air_to_ground_status,
                    "alpha_status_code": alpha_status_code,
                    "alt_aircraft_id": alt_aircraft_id,
                    "contamination_status": contamination_status,
                    "current_icao": current_icao,
                    "current_state": current_state,
                    "earliest_ta_end_time": earliest_ta_end_time,
                    "etic": etic,
                    "flight_phase": flight_phase,
                    "fuel": fuel,
                    "fuel_function": fuel_function,
                    "fuel_status": fuel_status,
                    "geo_loc": geo_loc,
                    "ground_status": ground_status,
                    "gun_capable": gun_capable,
                    "gun_rds_max": gun_rds_max,
                    "gun_rds_min": gun_rds_min,
                    "gun_rds_type": gun_rds_type,
                    "id_airfield": id_airfield,
                    "id_poi": id_poi,
                    "inventory": inventory,
                    "inventory_max": inventory_max,
                    "inventory_min": inventory_min,
                    "last_inspection_date": last_inspection_date,
                    "last_updated_by": last_updated_by,
                    "maint_poc": maint_poc,
                    "maint_priority": maint_priority,
                    "maint_status": maint_status,
                    "maint_status_driver": maint_status_driver,
                    "maint_status_update": maint_status_update,
                    "mission_readiness": mission_readiness,
                    "mx_remark": mx_remark,
                    "next_icao": next_icao,
                    "notes": notes,
                    "origin": origin,
                    "park_location": park_location,
                    "park_location_system": park_location_system,
                    "previous_icao": previous_icao,
                    "ta_start_time": ta_start_time,
                    "troubleshoot_etic": troubleshoot_etic,
                    "unavailable_sys": unavailable_sys,
                },
                aircraft_status_create_params.AircraftStatusCreateParams,
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
    ) -> AircraftstatusFull:
        """
        Service operation to get a single AircraftStatus record by its unique ID passed
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
            f"/udl/aircraftstatus/{id}",
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
                    aircraft_status_retrieve_params.AircraftStatusRetrieveParams,
                ),
            ),
            cast_to=AircraftstatusFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_aircraft: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        additional_sys: List[str] | NotGiven = NOT_GIVEN,
        air_to_air_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        air_to_ground_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        alpha_status_code: str | NotGiven = NOT_GIVEN,
        alt_aircraft_id: str | NotGiven = NOT_GIVEN,
        contamination_status: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        current_state: str | NotGiven = NOT_GIVEN,
        earliest_ta_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flight_phase: str | NotGiven = NOT_GIVEN,
        fuel: int | NotGiven = NOT_GIVEN,
        fuel_function: str | NotGiven = NOT_GIVEN,
        fuel_status: str | NotGiven = NOT_GIVEN,
        geo_loc: str | NotGiven = NOT_GIVEN,
        ground_status: str | NotGiven = NOT_GIVEN,
        gun_capable: bool | NotGiven = NOT_GIVEN,
        gun_rds_max: int | NotGiven = NOT_GIVEN,
        gun_rds_min: int | NotGiven = NOT_GIVEN,
        gun_rds_type: str | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        id_poi: str | NotGiven = NOT_GIVEN,
        inventory: List[str] | NotGiven = NOT_GIVEN,
        inventory_max: Iterable[int] | NotGiven = NOT_GIVEN,
        inventory_min: Iterable[int] | NotGiven = NOT_GIVEN,
        last_inspection_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_updated_by: str | NotGiven = NOT_GIVEN,
        maint_poc: str | NotGiven = NOT_GIVEN,
        maint_priority: str | NotGiven = NOT_GIVEN,
        maint_status: str | NotGiven = NOT_GIVEN,
        maint_status_driver: str | NotGiven = NOT_GIVEN,
        maint_status_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mission_readiness: str | NotGiven = NOT_GIVEN,
        mx_remark: str | NotGiven = NOT_GIVEN,
        next_icao: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        park_location: str | NotGiven = NOT_GIVEN,
        park_location_system: str | NotGiven = NOT_GIVEN,
        previous_icao: str | NotGiven = NOT_GIVEN,
        ta_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        troubleshoot_etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        unavailable_sys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AircraftStatus.

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

          id_aircraft: Unique identifier of the aircraft.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          additional_sys: List of additional operational systems on this aircraft beyond what is normally
              available.

          air_to_air_status: The status of the air-to-air weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          air_to_ground_status: The status of the air-to-ground weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          alpha_status_code: Aircraft alpha status code that indicates the aircraft maintenance status
              estimated by the pilot.

          alt_aircraft_id: Alternate Aircraft Identifier provided by source.

          contamination_status: The contamination status of the aircraft (e.g. CLEAR, CONTAMINATED,
              DECONTAMINATED, UNKNOWN, etc.).

          current_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              is currently located or has most recently departed, if airborne.

          current_state: The current readiness state of the aircraft (e.g. AIRBORNE, ALERTCOCKED,
              AVAILABLE, BATTLESTATION, RUNWAY ALERT, SUITUP).

          earliest_ta_end_time: The earliest time that turnaround of the aircraft may complete, in ISO 8601 UTC
              format with millisecond precision.

          etic: The Expected Time in Commission (ETIC) for this aircraft, in ISO 8601 UTC format
              with millisecond precision. This is the estimated time when the issue will be
              resolved.

          flight_phase: Current flight phase (e.g. AIR REFUELING, GROUND, LANDING, etc.) of the
              aircraft.

          fuel: The mass of fuel remaining on the aircraft, in kilograms.

          fuel_function: Used in conjunction with the fuel field to indicate either burnable or offload
              fuel.

          fuel_status: The state of the aircraft fuel status (e.g. DELIVERED, DUMPED, EMPTY, FULL,
              OTHER, REQUESTED, etc.).

          geo_loc: US Air Force geographic location code of the airfield where the aircraft is
              located.

          ground_status: The ground status of the aircraft (e.g. ALERT, CREW READY, ENGINE START, HANGAR,
              etc.).

          gun_capable: Flag indicating that the aircraft is capable of making at least one gun pass.

          gun_rds_max: The upper bound of the estimated number of gun rounds available.

          gun_rds_min: The lower bound of the estimated number of gun rounds available.

          gun_rds_type: The type of gun rounds available (e.g. 7.62 MM, 20 MM, 25 MM, etc.).

          id_airfield: If not airborne, the unique identifier of the installation currently hosting the
              aircraft.

          id_poi: Unique identifier of the Point of Interest (POI) record related to this aircraft
              status. This will generally represent the location of an aircraft on the ground.

          inventory: Array of inventory item(s) for which estimate(s) are available (e.g. AIM-9
              SIDEWINDER, AIM-120 AMRAAM, AIM-92 STINGER, CHAFF DECOY, FLARE TP 400, etc.).
              Intended as, but not constrained to, MIL-STD-6016 environment dependent
              specific/store type designations. This array must be the same length as
              inventoryMin and inventoryMax.

          inventory_max: Array of the upper bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMin.

          inventory_min: Array of the lower bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMax.

          last_inspection_date: Date when the military aircraft inspection was last performed, in ISO 8601 UTC
              format with millisecond precision.

          last_updated_by: The name or ID of the external user that updated this status.

          maint_poc: Military aircraft maintenance point of contact for this aircraft.

          maint_priority: Indicates the priority of the maintenance effort.

          maint_status: The maintenance status of the aircraft.

          maint_status_driver: Indicates the maintenance discrepancy that drives the current maintenance
              status.

          maint_status_update: The time of the last maintenance status update, in ISO 8601 UTC format with
              millisecond precision.

          mission_readiness: The Operational Capability of the reported aircraft (ABLE, LOFUEL, UNABLE).

          mx_remark: Maintenance pacing remarks assocociated with this aircraft.

          next_icao: The International Civil Aviation Organization (ICAO) code of the next
              destination of this aircraft.

          notes: Optional notes/comments concerning this aircraft status.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          park_location: The parking location of this aircraft.

          park_location_system: The system that designated the parking location (e.g. EMOC, GDSS, PEX, etc.).

          previous_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              was previously located.

          ta_start_time: The turnaround start time, in ISO 8601 UTC format with millisecond precision.

          troubleshoot_etic: Estimated Time for Completion (ETIC) of an aircraft issue, in ISO 8601 UTC
              format with millisecond precision. This is the estimated time when the course of
              action to resolve the issue will be determined.

          unavailable_sys: List of unavailable systems that would normally be on this aircraft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/aircraftstatus/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_aircraft": id_aircraft,
                    "source": source,
                    "body_id": body_id,
                    "additional_sys": additional_sys,
                    "air_to_air_status": air_to_air_status,
                    "air_to_ground_status": air_to_ground_status,
                    "alpha_status_code": alpha_status_code,
                    "alt_aircraft_id": alt_aircraft_id,
                    "contamination_status": contamination_status,
                    "current_icao": current_icao,
                    "current_state": current_state,
                    "earliest_ta_end_time": earliest_ta_end_time,
                    "etic": etic,
                    "flight_phase": flight_phase,
                    "fuel": fuel,
                    "fuel_function": fuel_function,
                    "fuel_status": fuel_status,
                    "geo_loc": geo_loc,
                    "ground_status": ground_status,
                    "gun_capable": gun_capable,
                    "gun_rds_max": gun_rds_max,
                    "gun_rds_min": gun_rds_min,
                    "gun_rds_type": gun_rds_type,
                    "id_airfield": id_airfield,
                    "id_poi": id_poi,
                    "inventory": inventory,
                    "inventory_max": inventory_max,
                    "inventory_min": inventory_min,
                    "last_inspection_date": last_inspection_date,
                    "last_updated_by": last_updated_by,
                    "maint_poc": maint_poc,
                    "maint_priority": maint_priority,
                    "maint_status": maint_status,
                    "maint_status_driver": maint_status_driver,
                    "maint_status_update": maint_status_update,
                    "mission_readiness": mission_readiness,
                    "mx_remark": mx_remark,
                    "next_icao": next_icao,
                    "notes": notes,
                    "origin": origin,
                    "park_location": park_location,
                    "park_location_system": park_location_system,
                    "previous_icao": previous_icao,
                    "ta_start_time": ta_start_time,
                    "troubleshoot_etic": troubleshoot_etic,
                    "unavailable_sys": unavailable_sys,
                },
                aircraft_status_update_params.AircraftStatusUpdateParams,
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
    ) -> SyncOffsetPage[AircraftstatusAbridged]:
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
            "/udl/aircraftstatus",
            page=SyncOffsetPage[AircraftstatusAbridged],
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
                    aircraft_status_list_params.AircraftStatusListParams,
                ),
            ),
            model=AircraftstatusAbridged,
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
        Service operation to delete a Status object specified by the passed ID path
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
            f"/udl/aircraftstatus/{id}",
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
            "/udl/aircraftstatus/count",
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
                    aircraft_status_count_params.AircraftStatusCountParams,
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
            "/udl/aircraftstatus/queryhelp",
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
    ) -> AircraftStatusTupleResponse:
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
            "/udl/aircraftstatus/tuple",
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
                    aircraft_status_tuple_params.AircraftStatusTupleParams,
                ),
            ),
            cast_to=AircraftStatusTupleResponse,
        )


class AsyncAircraftStatusesResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAircraftStatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAircraftStatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAircraftStatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAircraftStatusesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_aircraft: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        additional_sys: List[str] | NotGiven = NOT_GIVEN,
        air_to_air_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        air_to_ground_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        alpha_status_code: str | NotGiven = NOT_GIVEN,
        alt_aircraft_id: str | NotGiven = NOT_GIVEN,
        contamination_status: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        current_state: str | NotGiven = NOT_GIVEN,
        earliest_ta_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flight_phase: str | NotGiven = NOT_GIVEN,
        fuel: int | NotGiven = NOT_GIVEN,
        fuel_function: str | NotGiven = NOT_GIVEN,
        fuel_status: str | NotGiven = NOT_GIVEN,
        geo_loc: str | NotGiven = NOT_GIVEN,
        ground_status: str | NotGiven = NOT_GIVEN,
        gun_capable: bool | NotGiven = NOT_GIVEN,
        gun_rds_max: int | NotGiven = NOT_GIVEN,
        gun_rds_min: int | NotGiven = NOT_GIVEN,
        gun_rds_type: str | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        id_poi: str | NotGiven = NOT_GIVEN,
        inventory: List[str] | NotGiven = NOT_GIVEN,
        inventory_max: Iterable[int] | NotGiven = NOT_GIVEN,
        inventory_min: Iterable[int] | NotGiven = NOT_GIVEN,
        last_inspection_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_updated_by: str | NotGiven = NOT_GIVEN,
        maint_poc: str | NotGiven = NOT_GIVEN,
        maint_priority: str | NotGiven = NOT_GIVEN,
        maint_status: str | NotGiven = NOT_GIVEN,
        maint_status_driver: str | NotGiven = NOT_GIVEN,
        maint_status_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mission_readiness: str | NotGiven = NOT_GIVEN,
        mx_remark: str | NotGiven = NOT_GIVEN,
        next_icao: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        park_location: str | NotGiven = NOT_GIVEN,
        park_location_system: str | NotGiven = NOT_GIVEN,
        previous_icao: str | NotGiven = NOT_GIVEN,
        ta_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        troubleshoot_etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        unavailable_sys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single AircraftStatus as a POST body and ingest into
        the database. A specific role is required to perform this service operation.
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

          id_aircraft: Unique identifier of the aircraft.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          additional_sys: List of additional operational systems on this aircraft beyond what is normally
              available.

          air_to_air_status: The status of the air-to-air weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          air_to_ground_status: The status of the air-to-ground weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          alpha_status_code: Aircraft alpha status code that indicates the aircraft maintenance status
              estimated by the pilot.

          alt_aircraft_id: Alternate Aircraft Identifier provided by source.

          contamination_status: The contamination status of the aircraft (e.g. CLEAR, CONTAMINATED,
              DECONTAMINATED, UNKNOWN, etc.).

          current_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              is currently located or has most recently departed, if airborne.

          current_state: The current readiness state of the aircraft (e.g. AIRBORNE, ALERTCOCKED,
              AVAILABLE, BATTLESTATION, RUNWAY ALERT, SUITUP).

          earliest_ta_end_time: The earliest time that turnaround of the aircraft may complete, in ISO 8601 UTC
              format with millisecond precision.

          etic: The Expected Time in Commission (ETIC) for this aircraft, in ISO 8601 UTC format
              with millisecond precision. This is the estimated time when the issue will be
              resolved.

          flight_phase: Current flight phase (e.g. AIR REFUELING, GROUND, LANDING, etc.) of the
              aircraft.

          fuel: The mass of fuel remaining on the aircraft, in kilograms.

          fuel_function: Used in conjunction with the fuel field to indicate either burnable or offload
              fuel.

          fuel_status: The state of the aircraft fuel status (e.g. DELIVERED, DUMPED, EMPTY, FULL,
              OTHER, REQUESTED, etc.).

          geo_loc: US Air Force geographic location code of the airfield where the aircraft is
              located.

          ground_status: The ground status of the aircraft (e.g. ALERT, CREW READY, ENGINE START, HANGAR,
              etc.).

          gun_capable: Flag indicating that the aircraft is capable of making at least one gun pass.

          gun_rds_max: The upper bound of the estimated number of gun rounds available.

          gun_rds_min: The lower bound of the estimated number of gun rounds available.

          gun_rds_type: The type of gun rounds available (e.g. 7.62 MM, 20 MM, 25 MM, etc.).

          id_airfield: If not airborne, the unique identifier of the installation currently hosting the
              aircraft.

          id_poi: Unique identifier of the Point of Interest (POI) record related to this aircraft
              status. This will generally represent the location of an aircraft on the ground.

          inventory: Array of inventory item(s) for which estimate(s) are available (e.g. AIM-9
              SIDEWINDER, AIM-120 AMRAAM, AIM-92 STINGER, CHAFF DECOY, FLARE TP 400, etc.).
              Intended as, but not constrained to, MIL-STD-6016 environment dependent
              specific/store type designations. This array must be the same length as
              inventoryMin and inventoryMax.

          inventory_max: Array of the upper bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMin.

          inventory_min: Array of the lower bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMax.

          last_inspection_date: Date when the military aircraft inspection was last performed, in ISO 8601 UTC
              format with millisecond precision.

          last_updated_by: The name or ID of the external user that updated this status.

          maint_poc: Military aircraft maintenance point of contact for this aircraft.

          maint_priority: Indicates the priority of the maintenance effort.

          maint_status: The maintenance status of the aircraft.

          maint_status_driver: Indicates the maintenance discrepancy that drives the current maintenance
              status.

          maint_status_update: The time of the last maintenance status update, in ISO 8601 UTC format with
              millisecond precision.

          mission_readiness: The Operational Capability of the reported aircraft (ABLE, LOFUEL, UNABLE).

          mx_remark: Maintenance pacing remarks assocociated with this aircraft.

          next_icao: The International Civil Aviation Organization (ICAO) code of the next
              destination of this aircraft.

          notes: Optional notes/comments concerning this aircraft status.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          park_location: The parking location of this aircraft.

          park_location_system: The system that designated the parking location (e.g. EMOC, GDSS, PEX, etc.).

          previous_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              was previously located.

          ta_start_time: The turnaround start time, in ISO 8601 UTC format with millisecond precision.

          troubleshoot_etic: Estimated Time for Completion (ETIC) of an aircraft issue, in ISO 8601 UTC
              format with millisecond precision. This is the estimated time when the course of
              action to resolve the issue will be determined.

          unavailable_sys: List of unavailable systems that would normally be on this aircraft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/aircraftstatus",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_aircraft": id_aircraft,
                    "source": source,
                    "id": id,
                    "additional_sys": additional_sys,
                    "air_to_air_status": air_to_air_status,
                    "air_to_ground_status": air_to_ground_status,
                    "alpha_status_code": alpha_status_code,
                    "alt_aircraft_id": alt_aircraft_id,
                    "contamination_status": contamination_status,
                    "current_icao": current_icao,
                    "current_state": current_state,
                    "earliest_ta_end_time": earliest_ta_end_time,
                    "etic": etic,
                    "flight_phase": flight_phase,
                    "fuel": fuel,
                    "fuel_function": fuel_function,
                    "fuel_status": fuel_status,
                    "geo_loc": geo_loc,
                    "ground_status": ground_status,
                    "gun_capable": gun_capable,
                    "gun_rds_max": gun_rds_max,
                    "gun_rds_min": gun_rds_min,
                    "gun_rds_type": gun_rds_type,
                    "id_airfield": id_airfield,
                    "id_poi": id_poi,
                    "inventory": inventory,
                    "inventory_max": inventory_max,
                    "inventory_min": inventory_min,
                    "last_inspection_date": last_inspection_date,
                    "last_updated_by": last_updated_by,
                    "maint_poc": maint_poc,
                    "maint_priority": maint_priority,
                    "maint_status": maint_status,
                    "maint_status_driver": maint_status_driver,
                    "maint_status_update": maint_status_update,
                    "mission_readiness": mission_readiness,
                    "mx_remark": mx_remark,
                    "next_icao": next_icao,
                    "notes": notes,
                    "origin": origin,
                    "park_location": park_location,
                    "park_location_system": park_location_system,
                    "previous_icao": previous_icao,
                    "ta_start_time": ta_start_time,
                    "troubleshoot_etic": troubleshoot_etic,
                    "unavailable_sys": unavailable_sys,
                },
                aircraft_status_create_params.AircraftStatusCreateParams,
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
    ) -> AircraftstatusFull:
        """
        Service operation to get a single AircraftStatus record by its unique ID passed
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
            f"/udl/aircraftstatus/{id}",
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
                    aircraft_status_retrieve_params.AircraftStatusRetrieveParams,
                ),
            ),
            cast_to=AircraftstatusFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_aircraft: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        additional_sys: List[str] | NotGiven = NOT_GIVEN,
        air_to_air_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        air_to_ground_status: Literal["OPERATIONAL", "NON-OPERATIONAL", "OFF"] | NotGiven = NOT_GIVEN,
        alpha_status_code: str | NotGiven = NOT_GIVEN,
        alt_aircraft_id: str | NotGiven = NOT_GIVEN,
        contamination_status: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        current_state: str | NotGiven = NOT_GIVEN,
        earliest_ta_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        flight_phase: str | NotGiven = NOT_GIVEN,
        fuel: int | NotGiven = NOT_GIVEN,
        fuel_function: str | NotGiven = NOT_GIVEN,
        fuel_status: str | NotGiven = NOT_GIVEN,
        geo_loc: str | NotGiven = NOT_GIVEN,
        ground_status: str | NotGiven = NOT_GIVEN,
        gun_capable: bool | NotGiven = NOT_GIVEN,
        gun_rds_max: int | NotGiven = NOT_GIVEN,
        gun_rds_min: int | NotGiven = NOT_GIVEN,
        gun_rds_type: str | NotGiven = NOT_GIVEN,
        id_airfield: str | NotGiven = NOT_GIVEN,
        id_poi: str | NotGiven = NOT_GIVEN,
        inventory: List[str] | NotGiven = NOT_GIVEN,
        inventory_max: Iterable[int] | NotGiven = NOT_GIVEN,
        inventory_min: Iterable[int] | NotGiven = NOT_GIVEN,
        last_inspection_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_updated_by: str | NotGiven = NOT_GIVEN,
        maint_poc: str | NotGiven = NOT_GIVEN,
        maint_priority: str | NotGiven = NOT_GIVEN,
        maint_status: str | NotGiven = NOT_GIVEN,
        maint_status_driver: str | NotGiven = NOT_GIVEN,
        maint_status_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mission_readiness: str | NotGiven = NOT_GIVEN,
        mx_remark: str | NotGiven = NOT_GIVEN,
        next_icao: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        park_location: str | NotGiven = NOT_GIVEN,
        park_location_system: str | NotGiven = NOT_GIVEN,
        previous_icao: str | NotGiven = NOT_GIVEN,
        ta_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        troubleshoot_etic: Union[str, datetime] | NotGiven = NOT_GIVEN,
        unavailable_sys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AircraftStatus.

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

          id_aircraft: Unique identifier of the aircraft.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          additional_sys: List of additional operational systems on this aircraft beyond what is normally
              available.

          air_to_air_status: The status of the air-to-air weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          air_to_ground_status: The status of the air-to-ground weapon release system (OPERATIONAL,
              NON-OPERATIONAL, OFF).

          alpha_status_code: Aircraft alpha status code that indicates the aircraft maintenance status
              estimated by the pilot.

          alt_aircraft_id: Alternate Aircraft Identifier provided by source.

          contamination_status: The contamination status of the aircraft (e.g. CLEAR, CONTAMINATED,
              DECONTAMINATED, UNKNOWN, etc.).

          current_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              is currently located or has most recently departed, if airborne.

          current_state: The current readiness state of the aircraft (e.g. AIRBORNE, ALERTCOCKED,
              AVAILABLE, BATTLESTATION, RUNWAY ALERT, SUITUP).

          earliest_ta_end_time: The earliest time that turnaround of the aircraft may complete, in ISO 8601 UTC
              format with millisecond precision.

          etic: The Expected Time in Commission (ETIC) for this aircraft, in ISO 8601 UTC format
              with millisecond precision. This is the estimated time when the issue will be
              resolved.

          flight_phase: Current flight phase (e.g. AIR REFUELING, GROUND, LANDING, etc.) of the
              aircraft.

          fuel: The mass of fuel remaining on the aircraft, in kilograms.

          fuel_function: Used in conjunction with the fuel field to indicate either burnable or offload
              fuel.

          fuel_status: The state of the aircraft fuel status (e.g. DELIVERED, DUMPED, EMPTY, FULL,
              OTHER, REQUESTED, etc.).

          geo_loc: US Air Force geographic location code of the airfield where the aircraft is
              located.

          ground_status: The ground status of the aircraft (e.g. ALERT, CREW READY, ENGINE START, HANGAR,
              etc.).

          gun_capable: Flag indicating that the aircraft is capable of making at least one gun pass.

          gun_rds_max: The upper bound of the estimated number of gun rounds available.

          gun_rds_min: The lower bound of the estimated number of gun rounds available.

          gun_rds_type: The type of gun rounds available (e.g. 7.62 MM, 20 MM, 25 MM, etc.).

          id_airfield: If not airborne, the unique identifier of the installation currently hosting the
              aircraft.

          id_poi: Unique identifier of the Point of Interest (POI) record related to this aircraft
              status. This will generally represent the location of an aircraft on the ground.

          inventory: Array of inventory item(s) for which estimate(s) are available (e.g. AIM-9
              SIDEWINDER, AIM-120 AMRAAM, AIM-92 STINGER, CHAFF DECOY, FLARE TP 400, etc.).
              Intended as, but not constrained to, MIL-STD-6016 environment dependent
              specific/store type designations. This array must be the same length as
              inventoryMin and inventoryMax.

          inventory_max: Array of the upper bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMin.

          inventory_min: Array of the lower bound quantity for each of the inventory items. The values in
              this array must correspond to position index in the inventory array. This array
              must be the same length as inventory and inventoryMax.

          last_inspection_date: Date when the military aircraft inspection was last performed, in ISO 8601 UTC
              format with millisecond precision.

          last_updated_by: The name or ID of the external user that updated this status.

          maint_poc: Military aircraft maintenance point of contact for this aircraft.

          maint_priority: Indicates the priority of the maintenance effort.

          maint_status: The maintenance status of the aircraft.

          maint_status_driver: Indicates the maintenance discrepancy that drives the current maintenance
              status.

          maint_status_update: The time of the last maintenance status update, in ISO 8601 UTC format with
              millisecond precision.

          mission_readiness: The Operational Capability of the reported aircraft (ABLE, LOFUEL, UNABLE).

          mx_remark: Maintenance pacing remarks assocociated with this aircraft.

          next_icao: The International Civil Aviation Organization (ICAO) code of the next
              destination of this aircraft.

          notes: Optional notes/comments concerning this aircraft status.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          park_location: The parking location of this aircraft.

          park_location_system: The system that designated the parking location (e.g. EMOC, GDSS, PEX, etc.).

          previous_icao: The International Civil Aviation Organization (ICAO) code at which this aircraft
              was previously located.

          ta_start_time: The turnaround start time, in ISO 8601 UTC format with millisecond precision.

          troubleshoot_etic: Estimated Time for Completion (ETIC) of an aircraft issue, in ISO 8601 UTC
              format with millisecond precision. This is the estimated time when the course of
              action to resolve the issue will be determined.

          unavailable_sys: List of unavailable systems that would normally be on this aircraft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/aircraftstatus/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_aircraft": id_aircraft,
                    "source": source,
                    "body_id": body_id,
                    "additional_sys": additional_sys,
                    "air_to_air_status": air_to_air_status,
                    "air_to_ground_status": air_to_ground_status,
                    "alpha_status_code": alpha_status_code,
                    "alt_aircraft_id": alt_aircraft_id,
                    "contamination_status": contamination_status,
                    "current_icao": current_icao,
                    "current_state": current_state,
                    "earliest_ta_end_time": earliest_ta_end_time,
                    "etic": etic,
                    "flight_phase": flight_phase,
                    "fuel": fuel,
                    "fuel_function": fuel_function,
                    "fuel_status": fuel_status,
                    "geo_loc": geo_loc,
                    "ground_status": ground_status,
                    "gun_capable": gun_capable,
                    "gun_rds_max": gun_rds_max,
                    "gun_rds_min": gun_rds_min,
                    "gun_rds_type": gun_rds_type,
                    "id_airfield": id_airfield,
                    "id_poi": id_poi,
                    "inventory": inventory,
                    "inventory_max": inventory_max,
                    "inventory_min": inventory_min,
                    "last_inspection_date": last_inspection_date,
                    "last_updated_by": last_updated_by,
                    "maint_poc": maint_poc,
                    "maint_priority": maint_priority,
                    "maint_status": maint_status,
                    "maint_status_driver": maint_status_driver,
                    "maint_status_update": maint_status_update,
                    "mission_readiness": mission_readiness,
                    "mx_remark": mx_remark,
                    "next_icao": next_icao,
                    "notes": notes,
                    "origin": origin,
                    "park_location": park_location,
                    "park_location_system": park_location_system,
                    "previous_icao": previous_icao,
                    "ta_start_time": ta_start_time,
                    "troubleshoot_etic": troubleshoot_etic,
                    "unavailable_sys": unavailable_sys,
                },
                aircraft_status_update_params.AircraftStatusUpdateParams,
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
    ) -> AsyncPaginator[AircraftstatusAbridged, AsyncOffsetPage[AircraftstatusAbridged]]:
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
            "/udl/aircraftstatus",
            page=AsyncOffsetPage[AircraftstatusAbridged],
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
                    aircraft_status_list_params.AircraftStatusListParams,
                ),
            ),
            model=AircraftstatusAbridged,
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
        Service operation to delete a Status object specified by the passed ID path
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
            f"/udl/aircraftstatus/{id}",
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
            "/udl/aircraftstatus/count",
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
                    aircraft_status_count_params.AircraftStatusCountParams,
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
            "/udl/aircraftstatus/queryhelp",
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
    ) -> AircraftStatusTupleResponse:
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
            "/udl/aircraftstatus/tuple",
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
                    aircraft_status_tuple_params.AircraftStatusTupleParams,
                ),
            ),
            cast_to=AircraftStatusTupleResponse,
        )


class AircraftStatusesResourceWithRawResponse:
    def __init__(self, aircraft_statuses: AircraftStatusesResource) -> None:
        self._aircraft_statuses = aircraft_statuses

        self.create = to_raw_response_wrapper(
            aircraft_statuses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            aircraft_statuses.retrieve,
        )
        self.update = to_raw_response_wrapper(
            aircraft_statuses.update,
        )
        self.list = to_raw_response_wrapper(
            aircraft_statuses.list,
        )
        self.delete = to_raw_response_wrapper(
            aircraft_statuses.delete,
        )
        self.count = to_raw_response_wrapper(
            aircraft_statuses.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            aircraft_statuses.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            aircraft_statuses.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._aircraft_statuses.history)


class AsyncAircraftStatusesResourceWithRawResponse:
    def __init__(self, aircraft_statuses: AsyncAircraftStatusesResource) -> None:
        self._aircraft_statuses = aircraft_statuses

        self.create = async_to_raw_response_wrapper(
            aircraft_statuses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            aircraft_statuses.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            aircraft_statuses.update,
        )
        self.list = async_to_raw_response_wrapper(
            aircraft_statuses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            aircraft_statuses.delete,
        )
        self.count = async_to_raw_response_wrapper(
            aircraft_statuses.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            aircraft_statuses.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            aircraft_statuses.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._aircraft_statuses.history)


class AircraftStatusesResourceWithStreamingResponse:
    def __init__(self, aircraft_statuses: AircraftStatusesResource) -> None:
        self._aircraft_statuses = aircraft_statuses

        self.create = to_streamed_response_wrapper(
            aircraft_statuses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            aircraft_statuses.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            aircraft_statuses.update,
        )
        self.list = to_streamed_response_wrapper(
            aircraft_statuses.list,
        )
        self.delete = to_streamed_response_wrapper(
            aircraft_statuses.delete,
        )
        self.count = to_streamed_response_wrapper(
            aircraft_statuses.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            aircraft_statuses.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            aircraft_statuses.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._aircraft_statuses.history)


class AsyncAircraftStatusesResourceWithStreamingResponse:
    def __init__(self, aircraft_statuses: AsyncAircraftStatusesResource) -> None:
        self._aircraft_statuses = aircraft_statuses

        self.create = async_to_streamed_response_wrapper(
            aircraft_statuses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            aircraft_statuses.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            aircraft_statuses.update,
        )
        self.list = async_to_streamed_response_wrapper(
            aircraft_statuses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            aircraft_statuses.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            aircraft_statuses.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            aircraft_statuses.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            aircraft_statuses.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._aircraft_statuses.history)
