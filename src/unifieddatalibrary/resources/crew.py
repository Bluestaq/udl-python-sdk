# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    crew_list_params,
    crew_count_params,
    crew_tuple_params,
    crew_create_params,
    crew_update_params,
    crew_retrieve_params,
    crew_unvalidated_publish_params,
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
from ..types.crew_abridged import CrewAbridged
from ..types.shared.crew_full import CrewFull
from ..types.crew_tuple_response import CrewTupleResponse
from ..types.crew_queryhelp_response import CrewQueryhelpResponse

__all__ = ["CrewResource", "AsyncCrewResource"]


class CrewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CrewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CrewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CrewResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        orig_crew_id: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        adj_return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        adj_return_time_approver: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        alerted_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alert_type: str | NotGiven = NOT_GIVEN,
        arms_crew_unit: str | NotGiven = NOT_GIVEN,
        assigned_qual_code: List[str] | NotGiven = NOT_GIVEN,
        commander_id: str | NotGiven = NOT_GIVEN,
        commander_last4_ssn: str | NotGiven = NOT_GIVEN,
        commander_name: str | NotGiven = NOT_GIVEN,
        crew_home: bool | NotGiven = NOT_GIVEN,
        crew_members: Iterable[crew_create_params.CrewMember] | NotGiven = NOT_GIVEN,
        crew_name: str | NotGiven = NOT_GIVEN,
        crew_rms: str | NotGiven = NOT_GIVEN,
        crew_role: str | NotGiven = NOT_GIVEN,
        crew_source: str | NotGiven = NOT_GIVEN,
        crew_squadron: str | NotGiven = NOT_GIVEN,
        crew_type: str | NotGiven = NOT_GIVEN,
        crew_unit: str | NotGiven = NOT_GIVEN,
        crew_wing: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        fdp_elig_type: str | NotGiven = NOT_GIVEN,
        fdp_type: str | NotGiven = NOT_GIVEN,
        female_enlisted_qty: int | NotGiven = NOT_GIVEN,
        female_officer_qty: int | NotGiven = NOT_GIVEN,
        flt_auth_num: str | NotGiven = NOT_GIVEN,
        id_site_current: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        init_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_bravo_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        linked_task: bool | NotGiven = NOT_GIVEN,
        male_enlisted_qty: int | NotGiven = NOT_GIVEN,
        male_officer_qty: int | NotGiven = NOT_GIVEN,
        mission_alias: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        personnel_type: str | NotGiven = NOT_GIVEN,
        pickup_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_applied: bool | NotGiven = NOT_GIVEN,
        post_rest_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_offset: str | NotGiven = NOT_GIVEN,
        pre_rest_applied: bool | NotGiven = NOT_GIVEN,
        pre_rest_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        req_qual_code: List[str] | NotGiven = NOT_GIVEN,
        return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stage1_qual: str | NotGiven = NOT_GIVEN,
        stage2_qual: str | NotGiven = NOT_GIVEN,
        stage3_qual: str | NotGiven = NOT_GIVEN,
        stage_name: str | NotGiven = NOT_GIVEN,
        stage_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        transport_req: bool | NotGiven = NOT_GIVEN,
        trip_kit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Crew object as a POST body and ingest into
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

          orig_crew_id: Unique identifier of the formed crew provided by the originating source.
              Provided for systems that require tracking of an internal system generated ID.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          adj_return_time: Adjusted return time, in ISO 8601 UTC format with millisecond precision.

          adj_return_time_approver: Last name of the adjusted return time approver.

          aircraft_mds: The aircraft Model Design Series designation assigned for this crew.

          alerted_time: Time the crew was alerted, in ISO 8601 UTC format with millisecond precision.

          alert_type: Type of alert for the crew (e.g., ALPHA for maximum readiness, BRAVO for
              standby, etc.).

          arms_crew_unit: The crew's Aviation Resource Management System (ARMS) unit. If multiple units
              exist, use the Aircraft Commander's Unit.

          assigned_qual_code: Array of qualification codes assigned to this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          commander_id: Unique identifier of the crew commander assigned by the originating source.

          commander_last4_ssn: Last four digits of the crew commander's social security number.

          commander_name: The name of the crew commander.

          crew_home: Flag indicating whether this crew task takes the crew home and out of the stage.

          crew_members: CrewMembers Collection.

          crew_name: Name of the formed crew.

          crew_rms: The resource management system managing and reporting data on this crew.

          crew_role: The crew's role on the mission (e.g., DEADHEAD, MEDICAL, PRIMARY).

          crew_source: The military component that comprises the crew (e.g., ACTIVE, RESERVE, GUARD,
              MIXED, UNKNOWN, etc.).

          crew_squadron: The squadron the crew serves.

          crew_type: The type of crew required to meet mission objectives (e.g., AIRDROP, AIRLAND,
              AIR REFUELING, etc.).

          crew_unit: The crew's squadron as identified in its resource management system. If the crew
              is composed of members from multiple units, then the Crew Commander's unit
              should be indicated as the crew unit.

          crew_wing: The wing the crew serves.

          current_icao: The International Civil Aviation Organization (ICAO) code of the airfield at
              which the crew is currently located.

          fdp_elig_type: Crew Flight Duty Period (FDP) eligibility type.

          fdp_type: Flight Duty Period (FDP) type.

          female_enlisted_qty: The number of female enlisted crew members.

          female_officer_qty: The number of female officer crew members.

          flt_auth_num: Authorization number used on the flight order.

          id_site_current: Unique identifier of the Site at which the crew is currently located. This ID
              can be used to obtain additional information on a Site using the 'get by ID'
              operation (e.g. /udl/site/{id}). For example, the Site object with idSite = abc
              would be queried as /udl/site/abc.

          id_sortie: Unique identifier of the Aircraft Sortie associated with this crew record.

          init_start_time: Initial start time of the crew's linked task that was delinked due to mission
              closure, in ISO 8601 UTC format with millisecond precision.

          last_alert_time: The last time the crew can be alerted, in ISO 8601 UTC format with millisecond
              precision.

          legal_alert_time: Time the crew is legal for alert, in ISO 8601 UTC format with millisecond
              precision.

          legal_bravo_time: Time the crew is legally authorized or scheduled to remain on standby for duty,
              in ISO 8601 UTC format with millisecond precision.

          linked_task: Flag indicating whether this crew is part of a linked flying task.

          male_enlisted_qty: The number of male enlisted crew members.

          male_officer_qty: The number of male officer crew members.

          mission_alias: User-defined alias designation for the mission.

          mission_id: The mission ID the crew is supporting according to the source system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          personnel_type: The type of personnel that comprises the crew (e.g., AIRCREW, MEDCREW, etc.).

          pickup_time: Time the crew will be picked up from lodging, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_applied: Flag indicating whether post-mission crew rest is applied to the last sortie of
              a crew's task.

          post_rest_end: End time of the crew rest period after the mission, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_offset: The scheduled delay or adjustment in the start time of a crew's rest period
              after a mission, expressed as +/-HH:MM.

          pre_rest_applied: Flag indicating whether pre-mission crew rest is applied to the first sortie of
              a crew's task.

          pre_rest_start: Start time of the crew rest period before the mission, in ISO 8601 UTC format
              with millisecond precision.

          req_qual_code: Array of qualification codes required for this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          return_time: Scheduled return time, in ISO 8601 UTC format with millisecond precision.

          stage1_qual: The stage 1 qualifications the crew must have for a mission, such as having
              basic knowledge of crew operations and aircraft systems.

          stage2_qual: The stage 2 qualifications the crew must have for a mission, such as completion
              of advanced mission-specific training.

          stage3_qual: The stage 3 qualifications the crew must have for a mission, such as full
              mission-ready certification and the capability of leading complex operations.

          stage_name: Stage name for the crew. A stage is a pool of crews supporting a given operation
              plan.

          stage_time: Time the crew entered the stage, in ISO 8601 UTC format with millisecond
              precision.

          status: Crew status (e.g. NEEDCREW, ASSIGNED, APPROVED, NOTIFIED, PARTIAL, UNKNOWN,
              etc.).

          transport_req: Flag indicating that one or more crew members requires transportation to the
              departure location.

          trip_kit: Identifies the trip kit needed by the crew. A trip kit contains charts,
              regulations, maps, etc. carried by the crew during missions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/crew",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "orig_crew_id": orig_crew_id,
                    "source": source,
                    "id": id,
                    "adj_return_time": adj_return_time,
                    "adj_return_time_approver": adj_return_time_approver,
                    "aircraft_mds": aircraft_mds,
                    "alerted_time": alerted_time,
                    "alert_type": alert_type,
                    "arms_crew_unit": arms_crew_unit,
                    "assigned_qual_code": assigned_qual_code,
                    "commander_id": commander_id,
                    "commander_last4_ssn": commander_last4_ssn,
                    "commander_name": commander_name,
                    "crew_home": crew_home,
                    "crew_members": crew_members,
                    "crew_name": crew_name,
                    "crew_rms": crew_rms,
                    "crew_role": crew_role,
                    "crew_source": crew_source,
                    "crew_squadron": crew_squadron,
                    "crew_type": crew_type,
                    "crew_unit": crew_unit,
                    "crew_wing": crew_wing,
                    "current_icao": current_icao,
                    "fdp_elig_type": fdp_elig_type,
                    "fdp_type": fdp_type,
                    "female_enlisted_qty": female_enlisted_qty,
                    "female_officer_qty": female_officer_qty,
                    "flt_auth_num": flt_auth_num,
                    "id_site_current": id_site_current,
                    "id_sortie": id_sortie,
                    "init_start_time": init_start_time,
                    "last_alert_time": last_alert_time,
                    "legal_alert_time": legal_alert_time,
                    "legal_bravo_time": legal_bravo_time,
                    "linked_task": linked_task,
                    "male_enlisted_qty": male_enlisted_qty,
                    "male_officer_qty": male_officer_qty,
                    "mission_alias": mission_alias,
                    "mission_id": mission_id,
                    "origin": origin,
                    "personnel_type": personnel_type,
                    "pickup_time": pickup_time,
                    "post_rest_applied": post_rest_applied,
                    "post_rest_end": post_rest_end,
                    "post_rest_offset": post_rest_offset,
                    "pre_rest_applied": pre_rest_applied,
                    "pre_rest_start": pre_rest_start,
                    "req_qual_code": req_qual_code,
                    "return_time": return_time,
                    "stage1_qual": stage1_qual,
                    "stage2_qual": stage2_qual,
                    "stage3_qual": stage3_qual,
                    "stage_name": stage_name,
                    "stage_time": stage_time,
                    "status": status,
                    "transport_req": transport_req,
                    "trip_kit": trip_kit,
                },
                crew_create_params.CrewCreateParams,
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
    ) -> CrewFull:
        """
        Service operation to get a single Crew record by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/crew/{id}",
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
                    crew_retrieve_params.CrewRetrieveParams,
                ),
            ),
            cast_to=CrewFull,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        orig_crew_id: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        adj_return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        adj_return_time_approver: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        alerted_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alert_type: str | NotGiven = NOT_GIVEN,
        arms_crew_unit: str | NotGiven = NOT_GIVEN,
        assigned_qual_code: List[str] | NotGiven = NOT_GIVEN,
        commander_id: str | NotGiven = NOT_GIVEN,
        commander_last4_ssn: str | NotGiven = NOT_GIVEN,
        commander_name: str | NotGiven = NOT_GIVEN,
        crew_home: bool | NotGiven = NOT_GIVEN,
        crew_members: Iterable[crew_update_params.CrewMember] | NotGiven = NOT_GIVEN,
        crew_name: str | NotGiven = NOT_GIVEN,
        crew_rms: str | NotGiven = NOT_GIVEN,
        crew_role: str | NotGiven = NOT_GIVEN,
        crew_source: str | NotGiven = NOT_GIVEN,
        crew_squadron: str | NotGiven = NOT_GIVEN,
        crew_type: str | NotGiven = NOT_GIVEN,
        crew_unit: str | NotGiven = NOT_GIVEN,
        crew_wing: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        fdp_elig_type: str | NotGiven = NOT_GIVEN,
        fdp_type: str | NotGiven = NOT_GIVEN,
        female_enlisted_qty: int | NotGiven = NOT_GIVEN,
        female_officer_qty: int | NotGiven = NOT_GIVEN,
        flt_auth_num: str | NotGiven = NOT_GIVEN,
        id_site_current: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        init_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_bravo_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        linked_task: bool | NotGiven = NOT_GIVEN,
        male_enlisted_qty: int | NotGiven = NOT_GIVEN,
        male_officer_qty: int | NotGiven = NOT_GIVEN,
        mission_alias: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        personnel_type: str | NotGiven = NOT_GIVEN,
        pickup_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_applied: bool | NotGiven = NOT_GIVEN,
        post_rest_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_offset: str | NotGiven = NOT_GIVEN,
        pre_rest_applied: bool | NotGiven = NOT_GIVEN,
        pre_rest_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        req_qual_code: List[str] | NotGiven = NOT_GIVEN,
        return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stage1_qual: str | NotGiven = NOT_GIVEN,
        stage2_qual: str | NotGiven = NOT_GIVEN,
        stage3_qual: str | NotGiven = NOT_GIVEN,
        stage_name: str | NotGiven = NOT_GIVEN,
        stage_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        transport_req: bool | NotGiven = NOT_GIVEN,
        trip_kit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Crew record.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          orig_crew_id: Unique identifier of the formed crew provided by the originating source.
              Provided for systems that require tracking of an internal system generated ID.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          adj_return_time: Adjusted return time, in ISO 8601 UTC format with millisecond precision.

          adj_return_time_approver: Last name of the adjusted return time approver.

          aircraft_mds: The aircraft Model Design Series designation assigned for this crew.

          alerted_time: Time the crew was alerted, in ISO 8601 UTC format with millisecond precision.

          alert_type: Type of alert for the crew (e.g., ALPHA for maximum readiness, BRAVO for
              standby, etc.).

          arms_crew_unit: The crew's Aviation Resource Management System (ARMS) unit. If multiple units
              exist, use the Aircraft Commander's Unit.

          assigned_qual_code: Array of qualification codes assigned to this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          commander_id: Unique identifier of the crew commander assigned by the originating source.

          commander_last4_ssn: Last four digits of the crew commander's social security number.

          commander_name: The name of the crew commander.

          crew_home: Flag indicating whether this crew task takes the crew home and out of the stage.

          crew_members: CrewMembers Collection.

          crew_name: Name of the formed crew.

          crew_rms: The resource management system managing and reporting data on this crew.

          crew_role: The crew's role on the mission (e.g., DEADHEAD, MEDICAL, PRIMARY).

          crew_source: The military component that comprises the crew (e.g., ACTIVE, RESERVE, GUARD,
              MIXED, UNKNOWN, etc.).

          crew_squadron: The squadron the crew serves.

          crew_type: The type of crew required to meet mission objectives (e.g., AIRDROP, AIRLAND,
              AIR REFUELING, etc.).

          crew_unit: The crew's squadron as identified in its resource management system. If the crew
              is composed of members from multiple units, then the Crew Commander's unit
              should be indicated as the crew unit.

          crew_wing: The wing the crew serves.

          current_icao: The International Civil Aviation Organization (ICAO) code of the airfield at
              which the crew is currently located.

          fdp_elig_type: Crew Flight Duty Period (FDP) eligibility type.

          fdp_type: Flight Duty Period (FDP) type.

          female_enlisted_qty: The number of female enlisted crew members.

          female_officer_qty: The number of female officer crew members.

          flt_auth_num: Authorization number used on the flight order.

          id_site_current: Unique identifier of the Site at which the crew is currently located. This ID
              can be used to obtain additional information on a Site using the 'get by ID'
              operation (e.g. /udl/site/{id}). For example, the Site object with idSite = abc
              would be queried as /udl/site/abc.

          id_sortie: Unique identifier of the Aircraft Sortie associated with this crew record.

          init_start_time: Initial start time of the crew's linked task that was delinked due to mission
              closure, in ISO 8601 UTC format with millisecond precision.

          last_alert_time: The last time the crew can be alerted, in ISO 8601 UTC format with millisecond
              precision.

          legal_alert_time: Time the crew is legal for alert, in ISO 8601 UTC format with millisecond
              precision.

          legal_bravo_time: Time the crew is legally authorized or scheduled to remain on standby for duty,
              in ISO 8601 UTC format with millisecond precision.

          linked_task: Flag indicating whether this crew is part of a linked flying task.

          male_enlisted_qty: The number of male enlisted crew members.

          male_officer_qty: The number of male officer crew members.

          mission_alias: User-defined alias designation for the mission.

          mission_id: The mission ID the crew is supporting according to the source system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          personnel_type: The type of personnel that comprises the crew (e.g., AIRCREW, MEDCREW, etc.).

          pickup_time: Time the crew will be picked up from lodging, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_applied: Flag indicating whether post-mission crew rest is applied to the last sortie of
              a crew's task.

          post_rest_end: End time of the crew rest period after the mission, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_offset: The scheduled delay or adjustment in the start time of a crew's rest period
              after a mission, expressed as +/-HH:MM.

          pre_rest_applied: Flag indicating whether pre-mission crew rest is applied to the first sortie of
              a crew's task.

          pre_rest_start: Start time of the crew rest period before the mission, in ISO 8601 UTC format
              with millisecond precision.

          req_qual_code: Array of qualification codes required for this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          return_time: Scheduled return time, in ISO 8601 UTC format with millisecond precision.

          stage1_qual: The stage 1 qualifications the crew must have for a mission, such as having
              basic knowledge of crew operations and aircraft systems.

          stage2_qual: The stage 2 qualifications the crew must have for a mission, such as completion
              of advanced mission-specific training.

          stage3_qual: The stage 3 qualifications the crew must have for a mission, such as full
              mission-ready certification and the capability of leading complex operations.

          stage_name: Stage name for the crew. A stage is a pool of crews supporting a given operation
              plan.

          stage_time: Time the crew entered the stage, in ISO 8601 UTC format with millisecond
              precision.

          status: Crew status (e.g. NEEDCREW, ASSIGNED, APPROVED, NOTIFIED, PARTIAL, UNKNOWN,
              etc.).

          transport_req: Flag indicating that one or more crew members requires transportation to the
              departure location.

          trip_kit: Identifies the trip kit needed by the crew. A trip kit contains charts,
              regulations, maps, etc. carried by the crew during missions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/crew/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "orig_crew_id": orig_crew_id,
                    "source": source,
                    "body_id": body_id,
                    "adj_return_time": adj_return_time,
                    "adj_return_time_approver": adj_return_time_approver,
                    "aircraft_mds": aircraft_mds,
                    "alerted_time": alerted_time,
                    "alert_type": alert_type,
                    "arms_crew_unit": arms_crew_unit,
                    "assigned_qual_code": assigned_qual_code,
                    "commander_id": commander_id,
                    "commander_last4_ssn": commander_last4_ssn,
                    "commander_name": commander_name,
                    "crew_home": crew_home,
                    "crew_members": crew_members,
                    "crew_name": crew_name,
                    "crew_rms": crew_rms,
                    "crew_role": crew_role,
                    "crew_source": crew_source,
                    "crew_squadron": crew_squadron,
                    "crew_type": crew_type,
                    "crew_unit": crew_unit,
                    "crew_wing": crew_wing,
                    "current_icao": current_icao,
                    "fdp_elig_type": fdp_elig_type,
                    "fdp_type": fdp_type,
                    "female_enlisted_qty": female_enlisted_qty,
                    "female_officer_qty": female_officer_qty,
                    "flt_auth_num": flt_auth_num,
                    "id_site_current": id_site_current,
                    "id_sortie": id_sortie,
                    "init_start_time": init_start_time,
                    "last_alert_time": last_alert_time,
                    "legal_alert_time": legal_alert_time,
                    "legal_bravo_time": legal_bravo_time,
                    "linked_task": linked_task,
                    "male_enlisted_qty": male_enlisted_qty,
                    "male_officer_qty": male_officer_qty,
                    "mission_alias": mission_alias,
                    "mission_id": mission_id,
                    "origin": origin,
                    "personnel_type": personnel_type,
                    "pickup_time": pickup_time,
                    "post_rest_applied": post_rest_applied,
                    "post_rest_end": post_rest_end,
                    "post_rest_offset": post_rest_offset,
                    "pre_rest_applied": pre_rest_applied,
                    "pre_rest_start": pre_rest_start,
                    "req_qual_code": req_qual_code,
                    "return_time": return_time,
                    "stage1_qual": stage1_qual,
                    "stage2_qual": stage2_qual,
                    "stage3_qual": stage3_qual,
                    "stage_name": stage_name,
                    "stage_time": stage_time,
                    "status": status,
                    "transport_req": transport_req,
                    "trip_kit": trip_kit,
                },
                crew_update_params.CrewUpdateParams,
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
    ) -> SyncOffsetPage[CrewAbridged]:
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
            "/udl/crew",
            page=SyncOffsetPage[CrewAbridged],
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
                    crew_list_params.CrewListParams,
                ),
            ),
            model=CrewAbridged,
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
            "/udl/crew/count",
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
                    crew_count_params.CrewCountParams,
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
    ) -> CrewQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/crew/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrewQueryhelpResponse,
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
    ) -> CrewTupleResponse:
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
            "/udl/crew/tuple",
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
                    crew_tuple_params.CrewTupleParams,
                ),
            ),
            cast_to=CrewTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[crew_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple Crew objects as a POST body and ingest into
        the database. This operation is intended to be used for automated feeds into
        UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-crew",
            body=maybe_transform(body, Iterable[crew_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCrewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCrewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCrewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCrewResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        orig_crew_id: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        adj_return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        adj_return_time_approver: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        alerted_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alert_type: str | NotGiven = NOT_GIVEN,
        arms_crew_unit: str | NotGiven = NOT_GIVEN,
        assigned_qual_code: List[str] | NotGiven = NOT_GIVEN,
        commander_id: str | NotGiven = NOT_GIVEN,
        commander_last4_ssn: str | NotGiven = NOT_GIVEN,
        commander_name: str | NotGiven = NOT_GIVEN,
        crew_home: bool | NotGiven = NOT_GIVEN,
        crew_members: Iterable[crew_create_params.CrewMember] | NotGiven = NOT_GIVEN,
        crew_name: str | NotGiven = NOT_GIVEN,
        crew_rms: str | NotGiven = NOT_GIVEN,
        crew_role: str | NotGiven = NOT_GIVEN,
        crew_source: str | NotGiven = NOT_GIVEN,
        crew_squadron: str | NotGiven = NOT_GIVEN,
        crew_type: str | NotGiven = NOT_GIVEN,
        crew_unit: str | NotGiven = NOT_GIVEN,
        crew_wing: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        fdp_elig_type: str | NotGiven = NOT_GIVEN,
        fdp_type: str | NotGiven = NOT_GIVEN,
        female_enlisted_qty: int | NotGiven = NOT_GIVEN,
        female_officer_qty: int | NotGiven = NOT_GIVEN,
        flt_auth_num: str | NotGiven = NOT_GIVEN,
        id_site_current: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        init_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_bravo_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        linked_task: bool | NotGiven = NOT_GIVEN,
        male_enlisted_qty: int | NotGiven = NOT_GIVEN,
        male_officer_qty: int | NotGiven = NOT_GIVEN,
        mission_alias: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        personnel_type: str | NotGiven = NOT_GIVEN,
        pickup_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_applied: bool | NotGiven = NOT_GIVEN,
        post_rest_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_offset: str | NotGiven = NOT_GIVEN,
        pre_rest_applied: bool | NotGiven = NOT_GIVEN,
        pre_rest_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        req_qual_code: List[str] | NotGiven = NOT_GIVEN,
        return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stage1_qual: str | NotGiven = NOT_GIVEN,
        stage2_qual: str | NotGiven = NOT_GIVEN,
        stage3_qual: str | NotGiven = NOT_GIVEN,
        stage_name: str | NotGiven = NOT_GIVEN,
        stage_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        transport_req: bool | NotGiven = NOT_GIVEN,
        trip_kit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Crew object as a POST body and ingest into
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

          orig_crew_id: Unique identifier of the formed crew provided by the originating source.
              Provided for systems that require tracking of an internal system generated ID.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          adj_return_time: Adjusted return time, in ISO 8601 UTC format with millisecond precision.

          adj_return_time_approver: Last name of the adjusted return time approver.

          aircraft_mds: The aircraft Model Design Series designation assigned for this crew.

          alerted_time: Time the crew was alerted, in ISO 8601 UTC format with millisecond precision.

          alert_type: Type of alert for the crew (e.g., ALPHA for maximum readiness, BRAVO for
              standby, etc.).

          arms_crew_unit: The crew's Aviation Resource Management System (ARMS) unit. If multiple units
              exist, use the Aircraft Commander's Unit.

          assigned_qual_code: Array of qualification codes assigned to this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          commander_id: Unique identifier of the crew commander assigned by the originating source.

          commander_last4_ssn: Last four digits of the crew commander's social security number.

          commander_name: The name of the crew commander.

          crew_home: Flag indicating whether this crew task takes the crew home and out of the stage.

          crew_members: CrewMembers Collection.

          crew_name: Name of the formed crew.

          crew_rms: The resource management system managing and reporting data on this crew.

          crew_role: The crew's role on the mission (e.g., DEADHEAD, MEDICAL, PRIMARY).

          crew_source: The military component that comprises the crew (e.g., ACTIVE, RESERVE, GUARD,
              MIXED, UNKNOWN, etc.).

          crew_squadron: The squadron the crew serves.

          crew_type: The type of crew required to meet mission objectives (e.g., AIRDROP, AIRLAND,
              AIR REFUELING, etc.).

          crew_unit: The crew's squadron as identified in its resource management system. If the crew
              is composed of members from multiple units, then the Crew Commander's unit
              should be indicated as the crew unit.

          crew_wing: The wing the crew serves.

          current_icao: The International Civil Aviation Organization (ICAO) code of the airfield at
              which the crew is currently located.

          fdp_elig_type: Crew Flight Duty Period (FDP) eligibility type.

          fdp_type: Flight Duty Period (FDP) type.

          female_enlisted_qty: The number of female enlisted crew members.

          female_officer_qty: The number of female officer crew members.

          flt_auth_num: Authorization number used on the flight order.

          id_site_current: Unique identifier of the Site at which the crew is currently located. This ID
              can be used to obtain additional information on a Site using the 'get by ID'
              operation (e.g. /udl/site/{id}). For example, the Site object with idSite = abc
              would be queried as /udl/site/abc.

          id_sortie: Unique identifier of the Aircraft Sortie associated with this crew record.

          init_start_time: Initial start time of the crew's linked task that was delinked due to mission
              closure, in ISO 8601 UTC format with millisecond precision.

          last_alert_time: The last time the crew can be alerted, in ISO 8601 UTC format with millisecond
              precision.

          legal_alert_time: Time the crew is legal for alert, in ISO 8601 UTC format with millisecond
              precision.

          legal_bravo_time: Time the crew is legally authorized or scheduled to remain on standby for duty,
              in ISO 8601 UTC format with millisecond precision.

          linked_task: Flag indicating whether this crew is part of a linked flying task.

          male_enlisted_qty: The number of male enlisted crew members.

          male_officer_qty: The number of male officer crew members.

          mission_alias: User-defined alias designation for the mission.

          mission_id: The mission ID the crew is supporting according to the source system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          personnel_type: The type of personnel that comprises the crew (e.g., AIRCREW, MEDCREW, etc.).

          pickup_time: Time the crew will be picked up from lodging, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_applied: Flag indicating whether post-mission crew rest is applied to the last sortie of
              a crew's task.

          post_rest_end: End time of the crew rest period after the mission, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_offset: The scheduled delay or adjustment in the start time of a crew's rest period
              after a mission, expressed as +/-HH:MM.

          pre_rest_applied: Flag indicating whether pre-mission crew rest is applied to the first sortie of
              a crew's task.

          pre_rest_start: Start time of the crew rest period before the mission, in ISO 8601 UTC format
              with millisecond precision.

          req_qual_code: Array of qualification codes required for this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          return_time: Scheduled return time, in ISO 8601 UTC format with millisecond precision.

          stage1_qual: The stage 1 qualifications the crew must have for a mission, such as having
              basic knowledge of crew operations and aircraft systems.

          stage2_qual: The stage 2 qualifications the crew must have for a mission, such as completion
              of advanced mission-specific training.

          stage3_qual: The stage 3 qualifications the crew must have for a mission, such as full
              mission-ready certification and the capability of leading complex operations.

          stage_name: Stage name for the crew. A stage is a pool of crews supporting a given operation
              plan.

          stage_time: Time the crew entered the stage, in ISO 8601 UTC format with millisecond
              precision.

          status: Crew status (e.g. NEEDCREW, ASSIGNED, APPROVED, NOTIFIED, PARTIAL, UNKNOWN,
              etc.).

          transport_req: Flag indicating that one or more crew members requires transportation to the
              departure location.

          trip_kit: Identifies the trip kit needed by the crew. A trip kit contains charts,
              regulations, maps, etc. carried by the crew during missions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/crew",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "orig_crew_id": orig_crew_id,
                    "source": source,
                    "id": id,
                    "adj_return_time": adj_return_time,
                    "adj_return_time_approver": adj_return_time_approver,
                    "aircraft_mds": aircraft_mds,
                    "alerted_time": alerted_time,
                    "alert_type": alert_type,
                    "arms_crew_unit": arms_crew_unit,
                    "assigned_qual_code": assigned_qual_code,
                    "commander_id": commander_id,
                    "commander_last4_ssn": commander_last4_ssn,
                    "commander_name": commander_name,
                    "crew_home": crew_home,
                    "crew_members": crew_members,
                    "crew_name": crew_name,
                    "crew_rms": crew_rms,
                    "crew_role": crew_role,
                    "crew_source": crew_source,
                    "crew_squadron": crew_squadron,
                    "crew_type": crew_type,
                    "crew_unit": crew_unit,
                    "crew_wing": crew_wing,
                    "current_icao": current_icao,
                    "fdp_elig_type": fdp_elig_type,
                    "fdp_type": fdp_type,
                    "female_enlisted_qty": female_enlisted_qty,
                    "female_officer_qty": female_officer_qty,
                    "flt_auth_num": flt_auth_num,
                    "id_site_current": id_site_current,
                    "id_sortie": id_sortie,
                    "init_start_time": init_start_time,
                    "last_alert_time": last_alert_time,
                    "legal_alert_time": legal_alert_time,
                    "legal_bravo_time": legal_bravo_time,
                    "linked_task": linked_task,
                    "male_enlisted_qty": male_enlisted_qty,
                    "male_officer_qty": male_officer_qty,
                    "mission_alias": mission_alias,
                    "mission_id": mission_id,
                    "origin": origin,
                    "personnel_type": personnel_type,
                    "pickup_time": pickup_time,
                    "post_rest_applied": post_rest_applied,
                    "post_rest_end": post_rest_end,
                    "post_rest_offset": post_rest_offset,
                    "pre_rest_applied": pre_rest_applied,
                    "pre_rest_start": pre_rest_start,
                    "req_qual_code": req_qual_code,
                    "return_time": return_time,
                    "stage1_qual": stage1_qual,
                    "stage2_qual": stage2_qual,
                    "stage3_qual": stage3_qual,
                    "stage_name": stage_name,
                    "stage_time": stage_time,
                    "status": status,
                    "transport_req": transport_req,
                    "trip_kit": trip_kit,
                },
                crew_create_params.CrewCreateParams,
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
    ) -> CrewFull:
        """
        Service operation to get a single Crew record by its unique ID passed as a path
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/crew/{id}",
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
                    crew_retrieve_params.CrewRetrieveParams,
                ),
            ),
            cast_to=CrewFull,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        orig_crew_id: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        adj_return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        adj_return_time_approver: str | NotGiven = NOT_GIVEN,
        aircraft_mds: str | NotGiven = NOT_GIVEN,
        alerted_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        alert_type: str | NotGiven = NOT_GIVEN,
        arms_crew_unit: str | NotGiven = NOT_GIVEN,
        assigned_qual_code: List[str] | NotGiven = NOT_GIVEN,
        commander_id: str | NotGiven = NOT_GIVEN,
        commander_last4_ssn: str | NotGiven = NOT_GIVEN,
        commander_name: str | NotGiven = NOT_GIVEN,
        crew_home: bool | NotGiven = NOT_GIVEN,
        crew_members: Iterable[crew_update_params.CrewMember] | NotGiven = NOT_GIVEN,
        crew_name: str | NotGiven = NOT_GIVEN,
        crew_rms: str | NotGiven = NOT_GIVEN,
        crew_role: str | NotGiven = NOT_GIVEN,
        crew_source: str | NotGiven = NOT_GIVEN,
        crew_squadron: str | NotGiven = NOT_GIVEN,
        crew_type: str | NotGiven = NOT_GIVEN,
        crew_unit: str | NotGiven = NOT_GIVEN,
        crew_wing: str | NotGiven = NOT_GIVEN,
        current_icao: str | NotGiven = NOT_GIVEN,
        fdp_elig_type: str | NotGiven = NOT_GIVEN,
        fdp_type: str | NotGiven = NOT_GIVEN,
        female_enlisted_qty: int | NotGiven = NOT_GIVEN,
        female_officer_qty: int | NotGiven = NOT_GIVEN,
        flt_auth_num: str | NotGiven = NOT_GIVEN,
        id_site_current: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        init_start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_alert_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        legal_bravo_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        linked_task: bool | NotGiven = NOT_GIVEN,
        male_enlisted_qty: int | NotGiven = NOT_GIVEN,
        male_officer_qty: int | NotGiven = NOT_GIVEN,
        mission_alias: str | NotGiven = NOT_GIVEN,
        mission_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        personnel_type: str | NotGiven = NOT_GIVEN,
        pickup_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_applied: bool | NotGiven = NOT_GIVEN,
        post_rest_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        post_rest_offset: str | NotGiven = NOT_GIVEN,
        pre_rest_applied: bool | NotGiven = NOT_GIVEN,
        pre_rest_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        req_qual_code: List[str] | NotGiven = NOT_GIVEN,
        return_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        stage1_qual: str | NotGiven = NOT_GIVEN,
        stage2_qual: str | NotGiven = NOT_GIVEN,
        stage3_qual: str | NotGiven = NOT_GIVEN,
        stage_name: str | NotGiven = NOT_GIVEN,
        stage_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        transport_req: bool | NotGiven = NOT_GIVEN,
        trip_kit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Crew record.

        A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          orig_crew_id: Unique identifier of the formed crew provided by the originating source.
              Provided for systems that require tracking of an internal system generated ID.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          adj_return_time: Adjusted return time, in ISO 8601 UTC format with millisecond precision.

          adj_return_time_approver: Last name of the adjusted return time approver.

          aircraft_mds: The aircraft Model Design Series designation assigned for this crew.

          alerted_time: Time the crew was alerted, in ISO 8601 UTC format with millisecond precision.

          alert_type: Type of alert for the crew (e.g., ALPHA for maximum readiness, BRAVO for
              standby, etc.).

          arms_crew_unit: The crew's Aviation Resource Management System (ARMS) unit. If multiple units
              exist, use the Aircraft Commander's Unit.

          assigned_qual_code: Array of qualification codes assigned to this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          commander_id: Unique identifier of the crew commander assigned by the originating source.

          commander_last4_ssn: Last four digits of the crew commander's social security number.

          commander_name: The name of the crew commander.

          crew_home: Flag indicating whether this crew task takes the crew home and out of the stage.

          crew_members: CrewMembers Collection.

          crew_name: Name of the formed crew.

          crew_rms: The resource management system managing and reporting data on this crew.

          crew_role: The crew's role on the mission (e.g., DEADHEAD, MEDICAL, PRIMARY).

          crew_source: The military component that comprises the crew (e.g., ACTIVE, RESERVE, GUARD,
              MIXED, UNKNOWN, etc.).

          crew_squadron: The squadron the crew serves.

          crew_type: The type of crew required to meet mission objectives (e.g., AIRDROP, AIRLAND,
              AIR REFUELING, etc.).

          crew_unit: The crew's squadron as identified in its resource management system. If the crew
              is composed of members from multiple units, then the Crew Commander's unit
              should be indicated as the crew unit.

          crew_wing: The wing the crew serves.

          current_icao: The International Civil Aviation Organization (ICAO) code of the airfield at
              which the crew is currently located.

          fdp_elig_type: Crew Flight Duty Period (FDP) eligibility type.

          fdp_type: Flight Duty Period (FDP) type.

          female_enlisted_qty: The number of female enlisted crew members.

          female_officer_qty: The number of female officer crew members.

          flt_auth_num: Authorization number used on the flight order.

          id_site_current: Unique identifier of the Site at which the crew is currently located. This ID
              can be used to obtain additional information on a Site using the 'get by ID'
              operation (e.g. /udl/site/{id}). For example, the Site object with idSite = abc
              would be queried as /udl/site/abc.

          id_sortie: Unique identifier of the Aircraft Sortie associated with this crew record.

          init_start_time: Initial start time of the crew's linked task that was delinked due to mission
              closure, in ISO 8601 UTC format with millisecond precision.

          last_alert_time: The last time the crew can be alerted, in ISO 8601 UTC format with millisecond
              precision.

          legal_alert_time: Time the crew is legal for alert, in ISO 8601 UTC format with millisecond
              precision.

          legal_bravo_time: Time the crew is legally authorized or scheduled to remain on standby for duty,
              in ISO 8601 UTC format with millisecond precision.

          linked_task: Flag indicating whether this crew is part of a linked flying task.

          male_enlisted_qty: The number of male enlisted crew members.

          male_officer_qty: The number of male officer crew members.

          mission_alias: User-defined alias designation for the mission.

          mission_id: The mission ID the crew is supporting according to the source system.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          personnel_type: The type of personnel that comprises the crew (e.g., AIRCREW, MEDCREW, etc.).

          pickup_time: Time the crew will be picked up from lodging, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_applied: Flag indicating whether post-mission crew rest is applied to the last sortie of
              a crew's task.

          post_rest_end: End time of the crew rest period after the mission, in ISO 8601 UTC format with
              millisecond precision.

          post_rest_offset: The scheduled delay or adjustment in the start time of a crew's rest period
              after a mission, expressed as +/-HH:MM.

          pre_rest_applied: Flag indicating whether pre-mission crew rest is applied to the first sortie of
              a crew's task.

          pre_rest_start: Start time of the crew rest period before the mission, in ISO 8601 UTC format
              with millisecond precision.

          req_qual_code: Array of qualification codes required for this crew (e.g., AL for Aircraft
              Leader, CS for Combat Systems Operator, etc.).

          return_time: Scheduled return time, in ISO 8601 UTC format with millisecond precision.

          stage1_qual: The stage 1 qualifications the crew must have for a mission, such as having
              basic knowledge of crew operations and aircraft systems.

          stage2_qual: The stage 2 qualifications the crew must have for a mission, such as completion
              of advanced mission-specific training.

          stage3_qual: The stage 3 qualifications the crew must have for a mission, such as full
              mission-ready certification and the capability of leading complex operations.

          stage_name: Stage name for the crew. A stage is a pool of crews supporting a given operation
              plan.

          stage_time: Time the crew entered the stage, in ISO 8601 UTC format with millisecond
              precision.

          status: Crew status (e.g. NEEDCREW, ASSIGNED, APPROVED, NOTIFIED, PARTIAL, UNKNOWN,
              etc.).

          transport_req: Flag indicating that one or more crew members requires transportation to the
              departure location.

          trip_kit: Identifies the trip kit needed by the crew. A trip kit contains charts,
              regulations, maps, etc. carried by the crew during missions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/crew/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "orig_crew_id": orig_crew_id,
                    "source": source,
                    "body_id": body_id,
                    "adj_return_time": adj_return_time,
                    "adj_return_time_approver": adj_return_time_approver,
                    "aircraft_mds": aircraft_mds,
                    "alerted_time": alerted_time,
                    "alert_type": alert_type,
                    "arms_crew_unit": arms_crew_unit,
                    "assigned_qual_code": assigned_qual_code,
                    "commander_id": commander_id,
                    "commander_last4_ssn": commander_last4_ssn,
                    "commander_name": commander_name,
                    "crew_home": crew_home,
                    "crew_members": crew_members,
                    "crew_name": crew_name,
                    "crew_rms": crew_rms,
                    "crew_role": crew_role,
                    "crew_source": crew_source,
                    "crew_squadron": crew_squadron,
                    "crew_type": crew_type,
                    "crew_unit": crew_unit,
                    "crew_wing": crew_wing,
                    "current_icao": current_icao,
                    "fdp_elig_type": fdp_elig_type,
                    "fdp_type": fdp_type,
                    "female_enlisted_qty": female_enlisted_qty,
                    "female_officer_qty": female_officer_qty,
                    "flt_auth_num": flt_auth_num,
                    "id_site_current": id_site_current,
                    "id_sortie": id_sortie,
                    "init_start_time": init_start_time,
                    "last_alert_time": last_alert_time,
                    "legal_alert_time": legal_alert_time,
                    "legal_bravo_time": legal_bravo_time,
                    "linked_task": linked_task,
                    "male_enlisted_qty": male_enlisted_qty,
                    "male_officer_qty": male_officer_qty,
                    "mission_alias": mission_alias,
                    "mission_id": mission_id,
                    "origin": origin,
                    "personnel_type": personnel_type,
                    "pickup_time": pickup_time,
                    "post_rest_applied": post_rest_applied,
                    "post_rest_end": post_rest_end,
                    "post_rest_offset": post_rest_offset,
                    "pre_rest_applied": pre_rest_applied,
                    "pre_rest_start": pre_rest_start,
                    "req_qual_code": req_qual_code,
                    "return_time": return_time,
                    "stage1_qual": stage1_qual,
                    "stage2_qual": stage2_qual,
                    "stage3_qual": stage3_qual,
                    "stage_name": stage_name,
                    "stage_time": stage_time,
                    "status": status,
                    "transport_req": transport_req,
                    "trip_kit": trip_kit,
                },
                crew_update_params.CrewUpdateParams,
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
    ) -> AsyncPaginator[CrewAbridged, AsyncOffsetPage[CrewAbridged]]:
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
            "/udl/crew",
            page=AsyncOffsetPage[CrewAbridged],
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
                    crew_list_params.CrewListParams,
                ),
            ),
            model=CrewAbridged,
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
            "/udl/crew/count",
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
                    crew_count_params.CrewCountParams,
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
    ) -> CrewQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/crew/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrewQueryhelpResponse,
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
    ) -> CrewTupleResponse:
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
            "/udl/crew/tuple",
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
                    crew_tuple_params.CrewTupleParams,
                ),
            ),
            cast_to=CrewTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[crew_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple Crew objects as a POST body and ingest into
        the database. This operation is intended to be used for automated feeds into
        UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-crew",
            body=await async_maybe_transform(body, Iterable[crew_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CrewResourceWithRawResponse:
    def __init__(self, crew: CrewResource) -> None:
        self._crew = crew

        self.create = to_raw_response_wrapper(
            crew.create,
        )
        self.retrieve = to_raw_response_wrapper(
            crew.retrieve,
        )
        self.update = to_raw_response_wrapper(
            crew.update,
        )
        self.list = to_raw_response_wrapper(
            crew.list,
        )
        self.count = to_raw_response_wrapper(
            crew.count,
        )
        self.queryhelp = to_raw_response_wrapper(
            crew.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            crew.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            crew.unvalidated_publish,
        )


class AsyncCrewResourceWithRawResponse:
    def __init__(self, crew: AsyncCrewResource) -> None:
        self._crew = crew

        self.create = async_to_raw_response_wrapper(
            crew.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            crew.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            crew.update,
        )
        self.list = async_to_raw_response_wrapper(
            crew.list,
        )
        self.count = async_to_raw_response_wrapper(
            crew.count,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            crew.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            crew.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            crew.unvalidated_publish,
        )


class CrewResourceWithStreamingResponse:
    def __init__(self, crew: CrewResource) -> None:
        self._crew = crew

        self.create = to_streamed_response_wrapper(
            crew.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            crew.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            crew.update,
        )
        self.list = to_streamed_response_wrapper(
            crew.list,
        )
        self.count = to_streamed_response_wrapper(
            crew.count,
        )
        self.queryhelp = to_streamed_response_wrapper(
            crew.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            crew.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            crew.unvalidated_publish,
        )


class AsyncCrewResourceWithStreamingResponse:
    def __init__(self, crew: AsyncCrewResource) -> None:
        self._crew = crew

        self.create = async_to_streamed_response_wrapper(
            crew.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            crew.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            crew.update,
        )
        self.list = async_to_streamed_response_wrapper(
            crew.list,
        )
        self.count = async_to_streamed_response_wrapper(
            crew.count,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            crew.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            crew.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            crew.unvalidated_publish,
        )
