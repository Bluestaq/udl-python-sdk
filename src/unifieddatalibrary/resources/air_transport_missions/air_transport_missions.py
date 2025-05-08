# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import (
    air_transport_mission_list_params,
    air_transport_mission_count_params,
    air_transport_mission_tuple_params,
    air_transport_mission_create_params,
    air_transport_mission_update_params,
    air_transport_mission_retrieve_params,
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
from ...types.air_transport_mission_abridged import AirTransportMissionAbridged
from ...types.shared.air_transport_mission_full import AirTransportMissionFull
from ...types.air_transport_mission_tuple_response import AirTransportMissionTupleResponse

__all__ = ["AirTransportMissionsResource", "AsyncAirTransportMissionsResource"]


class AirTransportMissionsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AirTransportMissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirTransportMissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirTransportMissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirTransportMissionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        abp: str | NotGiven = NOT_GIVEN,
        alias: str | NotGiven = NOT_GIVEN,
        allocated_unit: str | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        ato_call_sign: str | NotGiven = NOT_GIVEN,
        ato_mission_id: str | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cw: bool | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        first_pick_up: str | NotGiven = NOT_GIVEN,
        gdss_mission_id: str | NotGiven = NOT_GIVEN,
        haz_mat: Iterable[air_transport_mission_create_params.HazMat] | NotGiven = NOT_GIVEN,
        jcs_priority: str | NotGiven = NOT_GIVEN,
        last_drop_off: str | NotGiven = NOT_GIVEN,
        load_category_type: str | NotGiven = NOT_GIVEN,
        m1: str | NotGiven = NOT_GIVEN,
        m2: str | NotGiven = NOT_GIVEN,
        m3a: str | NotGiven = NOT_GIVEN,
        naf: str | NotGiven = NOT_GIVEN,
        next_amc_mission_id: str | NotGiven = NOT_GIVEN,
        next_mission_id: str | NotGiven = NOT_GIVEN,
        node: str | NotGiven = NOT_GIVEN,
        objective: str | NotGiven = NOT_GIVEN,
        operation: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_mission_id: str | NotGiven = NOT_GIVEN,
        prev_amc_mission_id: str | NotGiven = NOT_GIVEN,
        prev_mission_id: str | NotGiven = NOT_GIVEN,
        purpose: str | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_transport_mission_create_params.Remark] | NotGiven = NOT_GIVEN,
        requirements: Iterable[air_transport_mission_create_params.Requirement] | NotGiven = NOT_GIVEN,
        source_sys_deviation: float | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single AirTransportMission object as a POST body and
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

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          abp: The Air Battle Plan used to coordinate and integrate air assets for this
              mission.

          alias: Mission alias.

          allocated_unit: The unit the mission is allocated to.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) Encode/Decode procedures.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve clearance requests.

          ato_call_sign: The call sign assigned to this mission according to the Air Tasking Order (ATO).

          ato_mission_id: The mission number according to the Air Tasking Order (ATO).

          call_sign: The call sign for this mission.

          cw: Flag indicating this is a close watch mission.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          first_pick_up: The International Civil Aviation Organization (ICAO) site code of first cargo
              pick up.

          gdss_mission_id: Global Decision Support System (GDSS) mission unique identifier.

          haz_mat: Collection of Hazardous Material information planned to be associated with this
              Air Transport Mission.

          jcs_priority: Highest Joint Chiefs of Staff priority of this mission.

          last_drop_off: The International Civil Aviation Organization (ICAO) site code of last cargo
              drop off.

          load_category_type: Load type of this mission (e.g. CARGO, MIXED, PASSENGER).

          m1: Mode-1 interrogation response (mission code), indicating mission or aircraft
              type.

          m2: Mode-2 interrogation response (military identification code).

          m3a: Mode-3/A interrogation response (aircraft identification), provides a 4-digit
              octal identification code for the aircraft, assigned by the air traffic
              controller. Mode-3/A is shared military/civilian use.

          naf: Numbered Air Force (NAF) organization that owns the mission.

          next_amc_mission_id: Air Mobility Command (AMC) mission identifier of the next air transport mission.
              Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          next_mission_id: Unique identifier of the next mission provided by the originating source.
              Provides a method for the data provider to link air transport missions together
              chronologically for tasking and planning purposes.

          node: Designates the location responsible for mission transportation, logistics, or
              distribution activities for an Area of Responsibility (AOR) within USTRANSCOM.

          objective: A description of this mission's objective.

          operation: The name of the operation that this mission supports.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_mission_id: The mission identifier provided by the originating source.

          prev_amc_mission_id: Air Mobility Command (AMC) mission identifier of the previous air transport
              mission. Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          prev_mission_id: Unique identifier of the previous air transport mission provided by the
              originating source. Provides a method for the data provider to link air
              transport missions together chronologically for tasking and planning purposes.

          purpose: A description of this mission's purpose (e.g. why this mission needs to happen,
              what is the mission supporting, etc.).

          remarks: Information related to the planning, load, status, and deployment or dispatch of
              one aircraft to carry out a mission.

          requirements: Collection of Requirements planned to be associated with this Air Transport
              Mission.

          source_sys_deviation: The number of minutes a mission is off schedule based on the source system's
              business rules. Positive numbers are early, negative numbers are late.

          state: Current state of the mission.

          type: The type of mission (e.g. SAAM, CHNL, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airtransportmission",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "id": id,
                    "abp": abp,
                    "alias": alias,
                    "allocated_unit": allocated_unit,
                    "amc_mission_id": amc_mission_id,
                    "apacs_id": apacs_id,
                    "ato_call_sign": ato_call_sign,
                    "ato_mission_id": ato_mission_id,
                    "call_sign": call_sign,
                    "cw": cw,
                    "dip_worksheet_name": dip_worksheet_name,
                    "first_pick_up": first_pick_up,
                    "gdss_mission_id": gdss_mission_id,
                    "haz_mat": haz_mat,
                    "jcs_priority": jcs_priority,
                    "last_drop_off": last_drop_off,
                    "load_category_type": load_category_type,
                    "m1": m1,
                    "m2": m2,
                    "m3a": m3a,
                    "naf": naf,
                    "next_amc_mission_id": next_amc_mission_id,
                    "next_mission_id": next_mission_id,
                    "node": node,
                    "objective": objective,
                    "operation": operation,
                    "origin": origin,
                    "orig_mission_id": orig_mission_id,
                    "prev_amc_mission_id": prev_amc_mission_id,
                    "prev_mission_id": prev_mission_id,
                    "purpose": purpose,
                    "remarks": remarks,
                    "requirements": requirements,
                    "source_sys_deviation": source_sys_deviation,
                    "state": state,
                    "type": type,
                },
                air_transport_mission_create_params.AirTransportMissionCreateParams,
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
    ) -> AirTransportMissionFull:
        """
        Service operation to get a single Air Transport Mission record by its unique ID
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
            f"/udl/airtransportmission/{id}",
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
                    air_transport_mission_retrieve_params.AirTransportMissionRetrieveParams,
                ),
            ),
            cast_to=AirTransportMissionFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        abp: str | NotGiven = NOT_GIVEN,
        alias: str | NotGiven = NOT_GIVEN,
        allocated_unit: str | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        ato_call_sign: str | NotGiven = NOT_GIVEN,
        ato_mission_id: str | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cw: bool | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        first_pick_up: str | NotGiven = NOT_GIVEN,
        gdss_mission_id: str | NotGiven = NOT_GIVEN,
        haz_mat: Iterable[air_transport_mission_update_params.HazMat] | NotGiven = NOT_GIVEN,
        jcs_priority: str | NotGiven = NOT_GIVEN,
        last_drop_off: str | NotGiven = NOT_GIVEN,
        load_category_type: str | NotGiven = NOT_GIVEN,
        m1: str | NotGiven = NOT_GIVEN,
        m2: str | NotGiven = NOT_GIVEN,
        m3a: str | NotGiven = NOT_GIVEN,
        naf: str | NotGiven = NOT_GIVEN,
        next_amc_mission_id: str | NotGiven = NOT_GIVEN,
        next_mission_id: str | NotGiven = NOT_GIVEN,
        node: str | NotGiven = NOT_GIVEN,
        objective: str | NotGiven = NOT_GIVEN,
        operation: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_mission_id: str | NotGiven = NOT_GIVEN,
        prev_amc_mission_id: str | NotGiven = NOT_GIVEN,
        prev_mission_id: str | NotGiven = NOT_GIVEN,
        purpose: str | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_transport_mission_update_params.Remark] | NotGiven = NOT_GIVEN,
        requirements: Iterable[air_transport_mission_update_params.Requirement] | NotGiven = NOT_GIVEN,
        source_sys_deviation: float | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AirTransportMission record.

        A specific role
        is required to perform this service operation. Please contact the UDL team for
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

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          abp: The Air Battle Plan used to coordinate and integrate air assets for this
              mission.

          alias: Mission alias.

          allocated_unit: The unit the mission is allocated to.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) Encode/Decode procedures.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve clearance requests.

          ato_call_sign: The call sign assigned to this mission according to the Air Tasking Order (ATO).

          ato_mission_id: The mission number according to the Air Tasking Order (ATO).

          call_sign: The call sign for this mission.

          cw: Flag indicating this is a close watch mission.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          first_pick_up: The International Civil Aviation Organization (ICAO) site code of first cargo
              pick up.

          gdss_mission_id: Global Decision Support System (GDSS) mission unique identifier.

          haz_mat: Collection of Hazardous Material information planned to be associated with this
              Air Transport Mission.

          jcs_priority: Highest Joint Chiefs of Staff priority of this mission.

          last_drop_off: The International Civil Aviation Organization (ICAO) site code of last cargo
              drop off.

          load_category_type: Load type of this mission (e.g. CARGO, MIXED, PASSENGER).

          m1: Mode-1 interrogation response (mission code), indicating mission or aircraft
              type.

          m2: Mode-2 interrogation response (military identification code).

          m3a: Mode-3/A interrogation response (aircraft identification), provides a 4-digit
              octal identification code for the aircraft, assigned by the air traffic
              controller. Mode-3/A is shared military/civilian use.

          naf: Numbered Air Force (NAF) organization that owns the mission.

          next_amc_mission_id: Air Mobility Command (AMC) mission identifier of the next air transport mission.
              Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          next_mission_id: Unique identifier of the next mission provided by the originating source.
              Provides a method for the data provider to link air transport missions together
              chronologically for tasking and planning purposes.

          node: Designates the location responsible for mission transportation, logistics, or
              distribution activities for an Area of Responsibility (AOR) within USTRANSCOM.

          objective: A description of this mission's objective.

          operation: The name of the operation that this mission supports.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_mission_id: The mission identifier provided by the originating source.

          prev_amc_mission_id: Air Mobility Command (AMC) mission identifier of the previous air transport
              mission. Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          prev_mission_id: Unique identifier of the previous air transport mission provided by the
              originating source. Provides a method for the data provider to link air
              transport missions together chronologically for tasking and planning purposes.

          purpose: A description of this mission's purpose (e.g. why this mission needs to happen,
              what is the mission supporting, etc.).

          remarks: Information related to the planning, load, status, and deployment or dispatch of
              one aircraft to carry out a mission.

          requirements: Collection of Requirements planned to be associated with this Air Transport
              Mission.

          source_sys_deviation: The number of minutes a mission is off schedule based on the source system's
              business rules. Positive numbers are early, negative numbers are late.

          state: Current state of the mission.

          type: The type of mission (e.g. SAAM, CHNL, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/airtransportmission/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "body_id": body_id,
                    "abp": abp,
                    "alias": alias,
                    "allocated_unit": allocated_unit,
                    "amc_mission_id": amc_mission_id,
                    "apacs_id": apacs_id,
                    "ato_call_sign": ato_call_sign,
                    "ato_mission_id": ato_mission_id,
                    "call_sign": call_sign,
                    "cw": cw,
                    "dip_worksheet_name": dip_worksheet_name,
                    "first_pick_up": first_pick_up,
                    "gdss_mission_id": gdss_mission_id,
                    "haz_mat": haz_mat,
                    "jcs_priority": jcs_priority,
                    "last_drop_off": last_drop_off,
                    "load_category_type": load_category_type,
                    "m1": m1,
                    "m2": m2,
                    "m3a": m3a,
                    "naf": naf,
                    "next_amc_mission_id": next_amc_mission_id,
                    "next_mission_id": next_mission_id,
                    "node": node,
                    "objective": objective,
                    "operation": operation,
                    "origin": origin,
                    "orig_mission_id": orig_mission_id,
                    "prev_amc_mission_id": prev_amc_mission_id,
                    "prev_mission_id": prev_mission_id,
                    "purpose": purpose,
                    "remarks": remarks,
                    "requirements": requirements,
                    "source_sys_deviation": source_sys_deviation,
                    "state": state,
                    "type": type,
                },
                air_transport_mission_update_params.AirTransportMissionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> SyncOffsetPage[AirTransportMissionAbridged]:
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
            "/udl/airtransportmission",
            page=SyncOffsetPage[AirTransportMissionAbridged],
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
                    air_transport_mission_list_params.AirTransportMissionListParams,
                ),
            ),
            model=AirTransportMissionAbridged,
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
            "/udl/airtransportmission/count",
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
                    air_transport_mission_count_params.AirTransportMissionCountParams,
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
            "/udl/airtransportmission/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirTransportMissionTupleResponse:
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

          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/airtransportmission/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    air_transport_mission_tuple_params.AirTransportMissionTupleParams,
                ),
            ),
            cast_to=AirTransportMissionTupleResponse,
        )


class AsyncAirTransportMissionsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAirTransportMissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirTransportMissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirTransportMissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirTransportMissionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        abp: str | NotGiven = NOT_GIVEN,
        alias: str | NotGiven = NOT_GIVEN,
        allocated_unit: str | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        ato_call_sign: str | NotGiven = NOT_GIVEN,
        ato_mission_id: str | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cw: bool | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        first_pick_up: str | NotGiven = NOT_GIVEN,
        gdss_mission_id: str | NotGiven = NOT_GIVEN,
        haz_mat: Iterable[air_transport_mission_create_params.HazMat] | NotGiven = NOT_GIVEN,
        jcs_priority: str | NotGiven = NOT_GIVEN,
        last_drop_off: str | NotGiven = NOT_GIVEN,
        load_category_type: str | NotGiven = NOT_GIVEN,
        m1: str | NotGiven = NOT_GIVEN,
        m2: str | NotGiven = NOT_GIVEN,
        m3a: str | NotGiven = NOT_GIVEN,
        naf: str | NotGiven = NOT_GIVEN,
        next_amc_mission_id: str | NotGiven = NOT_GIVEN,
        next_mission_id: str | NotGiven = NOT_GIVEN,
        node: str | NotGiven = NOT_GIVEN,
        objective: str | NotGiven = NOT_GIVEN,
        operation: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_mission_id: str | NotGiven = NOT_GIVEN,
        prev_amc_mission_id: str | NotGiven = NOT_GIVEN,
        prev_mission_id: str | NotGiven = NOT_GIVEN,
        purpose: str | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_transport_mission_create_params.Remark] | NotGiven = NOT_GIVEN,
        requirements: Iterable[air_transport_mission_create_params.Requirement] | NotGiven = NOT_GIVEN,
        source_sys_deviation: float | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single AirTransportMission object as a POST body and
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

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          abp: The Air Battle Plan used to coordinate and integrate air assets for this
              mission.

          alias: Mission alias.

          allocated_unit: The unit the mission is allocated to.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) Encode/Decode procedures.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve clearance requests.

          ato_call_sign: The call sign assigned to this mission according to the Air Tasking Order (ATO).

          ato_mission_id: The mission number according to the Air Tasking Order (ATO).

          call_sign: The call sign for this mission.

          cw: Flag indicating this is a close watch mission.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          first_pick_up: The International Civil Aviation Organization (ICAO) site code of first cargo
              pick up.

          gdss_mission_id: Global Decision Support System (GDSS) mission unique identifier.

          haz_mat: Collection of Hazardous Material information planned to be associated with this
              Air Transport Mission.

          jcs_priority: Highest Joint Chiefs of Staff priority of this mission.

          last_drop_off: The International Civil Aviation Organization (ICAO) site code of last cargo
              drop off.

          load_category_type: Load type of this mission (e.g. CARGO, MIXED, PASSENGER).

          m1: Mode-1 interrogation response (mission code), indicating mission or aircraft
              type.

          m2: Mode-2 interrogation response (military identification code).

          m3a: Mode-3/A interrogation response (aircraft identification), provides a 4-digit
              octal identification code for the aircraft, assigned by the air traffic
              controller. Mode-3/A is shared military/civilian use.

          naf: Numbered Air Force (NAF) organization that owns the mission.

          next_amc_mission_id: Air Mobility Command (AMC) mission identifier of the next air transport mission.
              Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          next_mission_id: Unique identifier of the next mission provided by the originating source.
              Provides a method for the data provider to link air transport missions together
              chronologically for tasking and planning purposes.

          node: Designates the location responsible for mission transportation, logistics, or
              distribution activities for an Area of Responsibility (AOR) within USTRANSCOM.

          objective: A description of this mission's objective.

          operation: The name of the operation that this mission supports.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_mission_id: The mission identifier provided by the originating source.

          prev_amc_mission_id: Air Mobility Command (AMC) mission identifier of the previous air transport
              mission. Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          prev_mission_id: Unique identifier of the previous air transport mission provided by the
              originating source. Provides a method for the data provider to link air
              transport missions together chronologically for tasking and planning purposes.

          purpose: A description of this mission's purpose (e.g. why this mission needs to happen,
              what is the mission supporting, etc.).

          remarks: Information related to the planning, load, status, and deployment or dispatch of
              one aircraft to carry out a mission.

          requirements: Collection of Requirements planned to be associated with this Air Transport
              Mission.

          source_sys_deviation: The number of minutes a mission is off schedule based on the source system's
              business rules. Positive numbers are early, negative numbers are late.

          state: Current state of the mission.

          type: The type of mission (e.g. SAAM, CHNL, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airtransportmission",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "id": id,
                    "abp": abp,
                    "alias": alias,
                    "allocated_unit": allocated_unit,
                    "amc_mission_id": amc_mission_id,
                    "apacs_id": apacs_id,
                    "ato_call_sign": ato_call_sign,
                    "ato_mission_id": ato_mission_id,
                    "call_sign": call_sign,
                    "cw": cw,
                    "dip_worksheet_name": dip_worksheet_name,
                    "first_pick_up": first_pick_up,
                    "gdss_mission_id": gdss_mission_id,
                    "haz_mat": haz_mat,
                    "jcs_priority": jcs_priority,
                    "last_drop_off": last_drop_off,
                    "load_category_type": load_category_type,
                    "m1": m1,
                    "m2": m2,
                    "m3a": m3a,
                    "naf": naf,
                    "next_amc_mission_id": next_amc_mission_id,
                    "next_mission_id": next_mission_id,
                    "node": node,
                    "objective": objective,
                    "operation": operation,
                    "origin": origin,
                    "orig_mission_id": orig_mission_id,
                    "prev_amc_mission_id": prev_amc_mission_id,
                    "prev_mission_id": prev_mission_id,
                    "purpose": purpose,
                    "remarks": remarks,
                    "requirements": requirements,
                    "source_sys_deviation": source_sys_deviation,
                    "state": state,
                    "type": type,
                },
                air_transport_mission_create_params.AirTransportMissionCreateParams,
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
    ) -> AirTransportMissionFull:
        """
        Service operation to get a single Air Transport Mission record by its unique ID
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
            f"/udl/airtransportmission/{id}",
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
                    air_transport_mission_retrieve_params.AirTransportMissionRetrieveParams,
                ),
            ),
            cast_to=AirTransportMissionFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        abp: str | NotGiven = NOT_GIVEN,
        alias: str | NotGiven = NOT_GIVEN,
        allocated_unit: str | NotGiven = NOT_GIVEN,
        amc_mission_id: str | NotGiven = NOT_GIVEN,
        apacs_id: str | NotGiven = NOT_GIVEN,
        ato_call_sign: str | NotGiven = NOT_GIVEN,
        ato_mission_id: str | NotGiven = NOT_GIVEN,
        call_sign: str | NotGiven = NOT_GIVEN,
        cw: bool | NotGiven = NOT_GIVEN,
        dip_worksheet_name: str | NotGiven = NOT_GIVEN,
        first_pick_up: str | NotGiven = NOT_GIVEN,
        gdss_mission_id: str | NotGiven = NOT_GIVEN,
        haz_mat: Iterable[air_transport_mission_update_params.HazMat] | NotGiven = NOT_GIVEN,
        jcs_priority: str | NotGiven = NOT_GIVEN,
        last_drop_off: str | NotGiven = NOT_GIVEN,
        load_category_type: str | NotGiven = NOT_GIVEN,
        m1: str | NotGiven = NOT_GIVEN,
        m2: str | NotGiven = NOT_GIVEN,
        m3a: str | NotGiven = NOT_GIVEN,
        naf: str | NotGiven = NOT_GIVEN,
        next_amc_mission_id: str | NotGiven = NOT_GIVEN,
        next_mission_id: str | NotGiven = NOT_GIVEN,
        node: str | NotGiven = NOT_GIVEN,
        objective: str | NotGiven = NOT_GIVEN,
        operation: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_mission_id: str | NotGiven = NOT_GIVEN,
        prev_amc_mission_id: str | NotGiven = NOT_GIVEN,
        prev_mission_id: str | NotGiven = NOT_GIVEN,
        purpose: str | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_transport_mission_update_params.Remark] | NotGiven = NOT_GIVEN,
        requirements: Iterable[air_transport_mission_update_params.Requirement] | NotGiven = NOT_GIVEN,
        source_sys_deviation: float | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single AirTransportMission record.

        A specific role
        is required to perform this service operation. Please contact the UDL team for
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

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          abp: The Air Battle Plan used to coordinate and integrate air assets for this
              mission.

          alias: Mission alias.

          allocated_unit: The unit the mission is allocated to.

          amc_mission_id: Air Mobility Command (AMC) mission identifier according to Mobility Air Forces
              (MAF) Encode/Decode procedures.

          apacs_id: The Aircraft and Personnel Automated Clearance System (APACS) system identifier
              used to process and approve clearance requests.

          ato_call_sign: The call sign assigned to this mission according to the Air Tasking Order (ATO).

          ato_mission_id: The mission number according to the Air Tasking Order (ATO).

          call_sign: The call sign for this mission.

          cw: Flag indicating this is a close watch mission.

          dip_worksheet_name: Identifier of the Diplomatic Clearance Worksheet used to coordinate aircraft
              clearance requests.

          first_pick_up: The International Civil Aviation Organization (ICAO) site code of first cargo
              pick up.

          gdss_mission_id: Global Decision Support System (GDSS) mission unique identifier.

          haz_mat: Collection of Hazardous Material information planned to be associated with this
              Air Transport Mission.

          jcs_priority: Highest Joint Chiefs of Staff priority of this mission.

          last_drop_off: The International Civil Aviation Organization (ICAO) site code of last cargo
              drop off.

          load_category_type: Load type of this mission (e.g. CARGO, MIXED, PASSENGER).

          m1: Mode-1 interrogation response (mission code), indicating mission or aircraft
              type.

          m2: Mode-2 interrogation response (military identification code).

          m3a: Mode-3/A interrogation response (aircraft identification), provides a 4-digit
              octal identification code for the aircraft, assigned by the air traffic
              controller. Mode-3/A is shared military/civilian use.

          naf: Numbered Air Force (NAF) organization that owns the mission.

          next_amc_mission_id: Air Mobility Command (AMC) mission identifier of the next air transport mission.
              Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          next_mission_id: Unique identifier of the next mission provided by the originating source.
              Provides a method for the data provider to link air transport missions together
              chronologically for tasking and planning purposes.

          node: Designates the location responsible for mission transportation, logistics, or
              distribution activities for an Area of Responsibility (AOR) within USTRANSCOM.

          objective: A description of this mission's objective.

          operation: The name of the operation that this mission supports.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_mission_id: The mission identifier provided by the originating source.

          prev_amc_mission_id: Air Mobility Command (AMC) mission identifier of the previous air transport
              mission. Provides a method for AMC to link air transport missions together
              chronologically for tasking and planning purposes.

          prev_mission_id: Unique identifier of the previous air transport mission provided by the
              originating source. Provides a method for the data provider to link air
              transport missions together chronologically for tasking and planning purposes.

          purpose: A description of this mission's purpose (e.g. why this mission needs to happen,
              what is the mission supporting, etc.).

          remarks: Information related to the planning, load, status, and deployment or dispatch of
              one aircraft to carry out a mission.

          requirements: Collection of Requirements planned to be associated with this Air Transport
              Mission.

          source_sys_deviation: The number of minutes a mission is off schedule based on the source system's
              business rules. Positive numbers are early, negative numbers are late.

          state: Current state of the mission.

          type: The type of mission (e.g. SAAM, CHNL, etc.).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/airtransportmission/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "body_id": body_id,
                    "abp": abp,
                    "alias": alias,
                    "allocated_unit": allocated_unit,
                    "amc_mission_id": amc_mission_id,
                    "apacs_id": apacs_id,
                    "ato_call_sign": ato_call_sign,
                    "ato_mission_id": ato_mission_id,
                    "call_sign": call_sign,
                    "cw": cw,
                    "dip_worksheet_name": dip_worksheet_name,
                    "first_pick_up": first_pick_up,
                    "gdss_mission_id": gdss_mission_id,
                    "haz_mat": haz_mat,
                    "jcs_priority": jcs_priority,
                    "last_drop_off": last_drop_off,
                    "load_category_type": load_category_type,
                    "m1": m1,
                    "m2": m2,
                    "m3a": m3a,
                    "naf": naf,
                    "next_amc_mission_id": next_amc_mission_id,
                    "next_mission_id": next_mission_id,
                    "node": node,
                    "objective": objective,
                    "operation": operation,
                    "origin": origin,
                    "orig_mission_id": orig_mission_id,
                    "prev_amc_mission_id": prev_amc_mission_id,
                    "prev_mission_id": prev_mission_id,
                    "purpose": purpose,
                    "remarks": remarks,
                    "requirements": requirements,
                    "source_sys_deviation": source_sys_deviation,
                    "state": state,
                    "type": type,
                },
                air_transport_mission_update_params.AirTransportMissionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> AsyncPaginator[AirTransportMissionAbridged, AsyncOffsetPage[AirTransportMissionAbridged]]:
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
            "/udl/airtransportmission",
            page=AsyncOffsetPage[AirTransportMissionAbridged],
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
                    air_transport_mission_list_params.AirTransportMissionListParams,
                ),
            ),
            model=AirTransportMissionAbridged,
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
            "/udl/airtransportmission/count",
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
                    air_transport_mission_count_params.AirTransportMissionCountParams,
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
            "/udl/airtransportmission/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        created_at: Union[str, date],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AirTransportMissionTupleResponse:
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

          created_at: Time the row was created in the database, auto-populated by the system.
              (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/airtransportmission/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "created_at": created_at,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    air_transport_mission_tuple_params.AirTransportMissionTupleParams,
                ),
            ),
            cast_to=AirTransportMissionTupleResponse,
        )


class AirTransportMissionsResourceWithRawResponse:
    def __init__(self, air_transport_missions: AirTransportMissionsResource) -> None:
        self._air_transport_missions = air_transport_missions

        self.create = to_raw_response_wrapper(
            air_transport_missions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            air_transport_missions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            air_transport_missions.update,
        )
        self.list = to_raw_response_wrapper(
            air_transport_missions.list,
        )
        self.count = to_raw_response_wrapper(
            air_transport_missions.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            air_transport_missions.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            air_transport_missions.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._air_transport_missions.history)


class AsyncAirTransportMissionsResourceWithRawResponse:
    def __init__(self, air_transport_missions: AsyncAirTransportMissionsResource) -> None:
        self._air_transport_missions = air_transport_missions

        self.create = async_to_raw_response_wrapper(
            air_transport_missions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            air_transport_missions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            air_transport_missions.update,
        )
        self.list = async_to_raw_response_wrapper(
            air_transport_missions.list,
        )
        self.count = async_to_raw_response_wrapper(
            air_transport_missions.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            air_transport_missions.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            air_transport_missions.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._air_transport_missions.history)


class AirTransportMissionsResourceWithStreamingResponse:
    def __init__(self, air_transport_missions: AirTransportMissionsResource) -> None:
        self._air_transport_missions = air_transport_missions

        self.create = to_streamed_response_wrapper(
            air_transport_missions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            air_transport_missions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            air_transport_missions.update,
        )
        self.list = to_streamed_response_wrapper(
            air_transport_missions.list,
        )
        self.count = to_streamed_response_wrapper(
            air_transport_missions.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            air_transport_missions.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            air_transport_missions.tuple,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._air_transport_missions.history)


class AsyncAirTransportMissionsResourceWithStreamingResponse:
    def __init__(self, air_transport_missions: AsyncAirTransportMissionsResource) -> None:
        self._air_transport_missions = air_transport_missions

        self.create = async_to_streamed_response_wrapper(
            air_transport_missions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            air_transport_missions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            air_transport_missions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            air_transport_missions.list,
        )
        self.count = async_to_streamed_response_wrapper(
            air_transport_missions.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            air_transport_missions.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            air_transport_missions.tuple,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._air_transport_missions.history)
