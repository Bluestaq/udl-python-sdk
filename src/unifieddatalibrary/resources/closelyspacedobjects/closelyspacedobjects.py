# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    closelyspacedobject_list_params,
    closelyspacedobject_count_params,
    closelyspacedobject_tuple_params,
    closelyspacedobject_create_params,
    closelyspacedobject_retrieve_params,
    closelyspacedobject_create_bulk_params,
    closelyspacedobject_unvalidated_publish_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.closelyspacedobjects_abridged import CloselyspacedobjectsAbridged
from ...types.closelyspacedobject_tuple_response import CloselyspacedobjectTupleResponse
from ...types.closelyspacedobject_retrieve_response import CloselyspacedobjectRetrieveResponse
from ...types.closelyspacedobject_query_help_response import CloselyspacedobjectQueryHelpResponse

__all__ = ["CloselyspacedobjectsResource", "AsyncCloselyspacedobjectsResource"]


class CloselyspacedobjectsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloselyspacedobjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CloselyspacedobjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloselyspacedobjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CloselyspacedobjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        cso_state: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        event_type: str,
        source: str,
        id: str | Omit = omit,
        actor_sv_epoch: Union[str, datetime] | Omit = omit,
        analysis_duration: float | Omit = omit,
        analysis_epoch: Union[str, datetime] | Omit = omit,
        comp_type: str | Omit = omit,
        context_keys: SequenceNotStr[str] | Omit = omit,
        context_values: SequenceNotStr[str] | Omit = omit,
        cso_details: Iterable[closelyspacedobject_create_params.CsoDetail] | Omit = omit,
        delta_v_tol: float | Omit = omit,
        duration_threshold: float | Omit = omit,
        event_end_time: Union[str, datetime] | Omit = omit,
        event_interval_coverage: float | Omit = omit,
        ext_id: str | Omit = omit,
        hohmann_delta_v: float | Omit = omit,
        id_actor_sv: str | Omit = omit,
        id_on_orbit1: str | Omit = omit,
        id_on_orbit2: str | Omit = omit,
        id_target_sv: str | Omit = omit,
        inclination_delta_v: float | Omit = omit,
        indication_source: str | Omit = omit,
        lon_tol: float | Omit = omit,
        max_range: float | Omit = omit,
        min_plane_sep_angle: float | Omit = omit,
        min_plane_sep_epoch: Union[str, datetime] | Omit = omit,
        min_range: float | Omit = omit,
        min_range_analysis_duration: float | Omit = omit,
        min_range_epoch: Union[str, datetime] | Omit = omit,
        notes: str | Omit = omit,
        num_sub_intervals: int | Omit = omit,
        orbit_align_del: float | Omit = omit,
        orbit_plane_tol: float | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id1: str | Omit = omit,
        orig_object_id2: str | Omit = omit,
        range_threshold: float | Omit = omit,
        range_tol: float | Omit = omit,
        rel_pos: Iterable[float] | Omit = omit,
        rel_pos_mag: float | Omit = omit,
        rel_speed_mag: float | Omit = omit,
        rel_vel: Iterable[float] | Omit = omit,
        sat_no1: int | Omit = omit,
        sat_no2: int | Omit = omit,
        station_lim_lon_tol: float | Omit = omit,
        target_sv_epoch: Union[str, datetime] | Omit = omit,
        total_delta_v: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single CloselySpacedObjects (CSO) as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cso_state: Indicates the current state that characterizes Closely Spaced Objects (CSO)
              analysis steps and conclusions. Values include: ACTIVE, ACTUAL, CANCELED,
              CLOSED, COMPLETED, DETECTED, INDICATED, PENDING, PLANNED, POSSIBLE, PREDICTED,
              SEPARATED, UPDATED.

          data_mode:
              Indicator of whether the data is REAL, TEST, EXERCISE, or SIMULATED data:

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision.

          event_type: The type of event associated with this record. Values include: DOCK, UNDOCK,
              SEPARATION, RENDEZVOUS, PROXIMITY, PEZ, WEZ.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          actor_sv_epoch: State vector epoch time of the actor satellite in ISO 8601 UTC format with
              millisecond precision.

          analysis_duration: Timespan of the rendezvous analysis in seconds.

          analysis_epoch: Epoch time of the beginning of the analysis period in ISO 8601 UTC format with
              millisecond precision.

          comp_type: Computation type, values (e.g. PLANARALIGNMENT, LONGITUDE).

          context_keys: An optional string array containing additional data (keys) representing relevant
              items for context of fields not specifically defined in this schema. This array
              is paired with the contextValues string array and must contain the same number
              of items. Please note these fields are intended for contextual use only and do
              not pertain to core schema information. To ensure proper integration and avoid
              misuse, coordination of how these fields are populated and consumed is required
              during onboarding.

          context_values: An optional string array containing the values associated with the contextKeys
              array. This array is paired with the contextKeys string array and must contain
              the same number of items. Please note these fields are intended for contextual
              use only and do not pertain to core schema information. To ensure proper
              integration and avoid misuse, coordination of how these fields are populated and
              consumed is required during onboarding.

          cso_details: A collection of orbital metrics for the event at the start and end times, and
              the mean values of the primary and secondary objects, as well as the deltas
              between the primary and secondary objects.

          delta_v_tol: The tolerance value for the DeltaV, in kilometers per second.

          duration_threshold: The threshold of the event duration in seconds.

          event_end_time: Timestamp representing the events end time in ISO 8601 UTC format with
              millisecond precision.

          event_interval_coverage: Percentage of the event interval that is within the plane tolerance specified as
              a percent value between 0 and 100.

          ext_id: Unique identifier of the record from the originating system. This field has no
              meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          hohmann_delta_v: The Hohmann DeltaV (kilometers per second) is the minimum delta velocity for the
              in-plane orbit change. The in-plane maneuvers change the semi-major axis
              (perigee and/or apogee). It is the minimum assuming two maneuvers; a lower delta
              velocity is possible with bi-elliptic transfers involving three maneuvers.

          id_actor_sv: Optional ID of the UDL State Vector at epoch time of the actor satellite. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the actor state vector.

          id_on_orbit1: Unique identifier of the primary satellite on-orbit object, if correlated. For
              rendezvous and proximity operations, this is the target on-orbit object. When
              the secondary object is on the rendezvous capable list, this can be any object.

          id_on_orbit2: Unique identifier of the secondary satellite on-orbit object, if correlated. For
              rendezvous and proximity operations, this is the actor. When the primary object
              is a satellite being protected on the neighborhood watch list (NWL), this can be
              any object encroaching on the primary.

          id_target_sv: Optional ID of the UDL State Vector at epoch time of the target satellite. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the target state vector.

          inclination_delta_v: The Inclination DeltaV is the minimum delta velocity for the out-of-plane
              change, assuming alignment of the right ascensions measured in kilometers per
              second.

          indication_source: Identifies the source of the indication, if the latest event info was manually
              input, not computed.

          lon_tol: The tolerance value for the longitude in degrees.

          max_range: Maximum range (apogee and perigee differences) within the event interval
              measured in kilometers.

          min_plane_sep_angle: Minimum angle between the target's position and the projection of the actor's
              position into the target's nominal orbit plane over the event interval measured
              in degrees.

          min_plane_sep_epoch: Epoch time of the minimum in-plane separation angle occurrence in ISO 8601 UTC
              format with millisecond precision.

          min_range: Minimum range (apogee and perigee differences) within the event interval
              measured in kilometers.

          min_range_analysis_duration: Timespan of satellites within the range tolerance in seconds.

          min_range_epoch: Epoch time of the minimum range occurrence in ISO 8601 UTC format with
              millisecond precision.

          notes: Contains other descriptive information associated with an indicated event.

          num_sub_intervals: The number of oscillations within the event interval which are within the plane
              tolerance.

          orbit_align_del: The change in angle between the angular momentum vectors between the actor and
              target relative to plane orientation in degrees.

          orbit_plane_tol: The tolerance value for the difference in the orbital plane measured in degrees.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id1: Optional place holder for an OnOrbit ID that does not exist in UDL.

          orig_object_id2: Optional place holder for an OnOrbit ID that does not exist in UDL.

          range_threshold: The threshold of the event range in kilometers.

          range_tol: The tolerance value for the range in kilometers.

          rel_pos: Indicates the relative position vector of the event occurrence measured in
              kilometers.

          rel_pos_mag: Range of closest approach: relative position magnitude, in kilometers, of the
              difference in the physical position between the actor and target objects.

          rel_speed_mag: Indicates the closure rate specified as a relative velocity magnitude in
              kilometers per second of the difference in the velocities between the actor and
              target objects.

          rel_vel: Indicates the relative velocity vector of the event occurrence measured in
              kilometers per second.

          sat_no1: Satellite/catalog number of the target on-orbit primary object.

          sat_no2: Satellite/catalog number of the target on-orbit secondary object.

          station_lim_lon_tol: The tolerance value for the optimal longitude for station-keeping in degrees.

          target_sv_epoch: State vector epoch time of the target satellite in ISO 8601 UTC format with
              millisecond precision.

          total_delta_v: The Total DeltaV is the sum of the Hohmann and Inclination DeltaVs measured in
              kilometers per second.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/closelyspacedobjects",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "cso_state": cso_state,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "event_type": event_type,
                    "source": source,
                    "id": id,
                    "actor_sv_epoch": actor_sv_epoch,
                    "analysis_duration": analysis_duration,
                    "analysis_epoch": analysis_epoch,
                    "comp_type": comp_type,
                    "context_keys": context_keys,
                    "context_values": context_values,
                    "cso_details": cso_details,
                    "delta_v_tol": delta_v_tol,
                    "duration_threshold": duration_threshold,
                    "event_end_time": event_end_time,
                    "event_interval_coverage": event_interval_coverage,
                    "ext_id": ext_id,
                    "hohmann_delta_v": hohmann_delta_v,
                    "id_actor_sv": id_actor_sv,
                    "id_on_orbit1": id_on_orbit1,
                    "id_on_orbit2": id_on_orbit2,
                    "id_target_sv": id_target_sv,
                    "inclination_delta_v": inclination_delta_v,
                    "indication_source": indication_source,
                    "lon_tol": lon_tol,
                    "max_range": max_range,
                    "min_plane_sep_angle": min_plane_sep_angle,
                    "min_plane_sep_epoch": min_plane_sep_epoch,
                    "min_range": min_range,
                    "min_range_analysis_duration": min_range_analysis_duration,
                    "min_range_epoch": min_range_epoch,
                    "notes": notes,
                    "num_sub_intervals": num_sub_intervals,
                    "orbit_align_del": orbit_align_del,
                    "orbit_plane_tol": orbit_plane_tol,
                    "origin": origin,
                    "orig_object_id1": orig_object_id1,
                    "orig_object_id2": orig_object_id2,
                    "range_threshold": range_threshold,
                    "range_tol": range_tol,
                    "rel_pos": rel_pos,
                    "rel_pos_mag": rel_pos_mag,
                    "rel_speed_mag": rel_speed_mag,
                    "rel_vel": rel_vel,
                    "sat_no1": sat_no1,
                    "sat_no2": sat_no2,
                    "station_lim_lon_tol": station_lim_lon_tol,
                    "target_sv_epoch": target_sv_epoch,
                    "total_delta_v": total_delta_v,
                },
                closelyspacedobject_create_params.CloselyspacedobjectCreateParams,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloselyspacedobjectRetrieveResponse:
        """
        Service operation to get a single CloselySpacedObjects (CSO) record by its
        unique ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/closelyspacedobjects/{id}",
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
                    closelyspacedobject_retrieve_params.CloselyspacedobjectRetrieveParams,
                ),
            ),
            cast_to=CloselyspacedobjectRetrieveResponse,
        )

    def list(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[CloselyspacedobjectsAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/closelyspacedobjects",
            page=SyncOffsetPage[CloselyspacedobjectsAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    closelyspacedobject_list_params.CloselyspacedobjectListParams,
                ),
            ),
            model=CloselyspacedobjectsAbridged,
        )

    def count(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/closelyspacedobjects/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    closelyspacedobject_count_params.CloselyspacedobjectCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[closelyspacedobject_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        CloselySpacedObjects (CSO) records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
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
            "/udl/closelyspacedobjects/createBulk",
            body=maybe_transform(body, Iterable[closelyspacedobject_create_bulk_params.Body]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloselyspacedobjectQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/closelyspacedobjects/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloselyspacedobjectQueryHelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloselyspacedobjectTupleResponse:
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

          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/closelyspacedobjects/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    closelyspacedobject_tuple_params.CloselyspacedobjectTupleParams,
                ),
            ),
            cast_to=CloselyspacedobjectTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[closelyspacedobject_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple CloselySpacedObjects (CSO) records as a POST
        body and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-closelyspacedobjects",
            body=maybe_transform(body, Iterable[closelyspacedobject_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCloselyspacedobjectsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloselyspacedobjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCloselyspacedobjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloselyspacedobjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCloselyspacedobjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        cso_state: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        event_type: str,
        source: str,
        id: str | Omit = omit,
        actor_sv_epoch: Union[str, datetime] | Omit = omit,
        analysis_duration: float | Omit = omit,
        analysis_epoch: Union[str, datetime] | Omit = omit,
        comp_type: str | Omit = omit,
        context_keys: SequenceNotStr[str] | Omit = omit,
        context_values: SequenceNotStr[str] | Omit = omit,
        cso_details: Iterable[closelyspacedobject_create_params.CsoDetail] | Omit = omit,
        delta_v_tol: float | Omit = omit,
        duration_threshold: float | Omit = omit,
        event_end_time: Union[str, datetime] | Omit = omit,
        event_interval_coverage: float | Omit = omit,
        ext_id: str | Omit = omit,
        hohmann_delta_v: float | Omit = omit,
        id_actor_sv: str | Omit = omit,
        id_on_orbit1: str | Omit = omit,
        id_on_orbit2: str | Omit = omit,
        id_target_sv: str | Omit = omit,
        inclination_delta_v: float | Omit = omit,
        indication_source: str | Omit = omit,
        lon_tol: float | Omit = omit,
        max_range: float | Omit = omit,
        min_plane_sep_angle: float | Omit = omit,
        min_plane_sep_epoch: Union[str, datetime] | Omit = omit,
        min_range: float | Omit = omit,
        min_range_analysis_duration: float | Omit = omit,
        min_range_epoch: Union[str, datetime] | Omit = omit,
        notes: str | Omit = omit,
        num_sub_intervals: int | Omit = omit,
        orbit_align_del: float | Omit = omit,
        orbit_plane_tol: float | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id1: str | Omit = omit,
        orig_object_id2: str | Omit = omit,
        range_threshold: float | Omit = omit,
        range_tol: float | Omit = omit,
        rel_pos: Iterable[float] | Omit = omit,
        rel_pos_mag: float | Omit = omit,
        rel_speed_mag: float | Omit = omit,
        rel_vel: Iterable[float] | Omit = omit,
        sat_no1: int | Omit = omit,
        sat_no2: int | Omit = omit,
        station_lim_lon_tol: float | Omit = omit,
        target_sv_epoch: Union[str, datetime] | Omit = omit,
        total_delta_v: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single CloselySpacedObjects (CSO) as a POST body and
        ingest into the database. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          classification_marking: Classification marking of the data in IC/CAPCO Portion-marked format.

          cso_state: Indicates the current state that characterizes Closely Spaced Objects (CSO)
              analysis steps and conclusions. Values include: ACTIVE, ACTUAL, CANCELED,
              CLOSED, COMPLETED, DETECTED, INDICATED, PENDING, PLANNED, POSSIBLE, PREDICTED,
              SEPARATED, UPDATED.

          data_mode:
              Indicator of whether the data is REAL, TEST, EXERCISE, or SIMULATED data:

              REAL:&nbsp;Data collected or produced that pertains to real-world objects,
              events, and analysis.

              TEST:&nbsp;Specific datasets used to evaluate compliance with specifications and
              requirements, and for validating technical, functional, and performance
              characteristics.

              EXERCISE:&nbsp;Data pertaining to a government or military exercise. The data
              may include both real and simulated data.

              SIMULATED:&nbsp;Synthetic data generated by a model to mimic real-world
              datasets.

          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision.

          event_type: The type of event associated with this record. Values include: DOCK, UNDOCK,
              SEPARATION, RENDEZVOUS, PROXIMITY, PEZ, WEZ.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          actor_sv_epoch: State vector epoch time of the actor satellite in ISO 8601 UTC format with
              millisecond precision.

          analysis_duration: Timespan of the rendezvous analysis in seconds.

          analysis_epoch: Epoch time of the beginning of the analysis period in ISO 8601 UTC format with
              millisecond precision.

          comp_type: Computation type, values (e.g. PLANARALIGNMENT, LONGITUDE).

          context_keys: An optional string array containing additional data (keys) representing relevant
              items for context of fields not specifically defined in this schema. This array
              is paired with the contextValues string array and must contain the same number
              of items. Please note these fields are intended for contextual use only and do
              not pertain to core schema information. To ensure proper integration and avoid
              misuse, coordination of how these fields are populated and consumed is required
              during onboarding.

          context_values: An optional string array containing the values associated with the contextKeys
              array. This array is paired with the contextKeys string array and must contain
              the same number of items. Please note these fields are intended for contextual
              use only and do not pertain to core schema information. To ensure proper
              integration and avoid misuse, coordination of how these fields are populated and
              consumed is required during onboarding.

          cso_details: A collection of orbital metrics for the event at the start and end times, and
              the mean values of the primary and secondary objects, as well as the deltas
              between the primary and secondary objects.

          delta_v_tol: The tolerance value for the DeltaV, in kilometers per second.

          duration_threshold: The threshold of the event duration in seconds.

          event_end_time: Timestamp representing the events end time in ISO 8601 UTC format with
              millisecond precision.

          event_interval_coverage: Percentage of the event interval that is within the plane tolerance specified as
              a percent value between 0 and 100.

          ext_id: Unique identifier of the record from the originating system. This field has no
              meaning within UDL and is provided as a convenience for systems that require
              tracking of an internal system generated ID.

          hohmann_delta_v: The Hohmann DeltaV (kilometers per second) is the minimum delta velocity for the
              in-plane orbit change. The in-plane maneuvers change the semi-major axis
              (perigee and/or apogee). It is the minimum assuming two maneuvers; a lower delta
              velocity is possible with bi-elliptic transfers involving three maneuvers.

          id_actor_sv: Optional ID of the UDL State Vector at epoch time of the actor satellite. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the actor state vector.

          id_on_orbit1: Unique identifier of the primary satellite on-orbit object, if correlated. For
              rendezvous and proximity operations, this is the target on-orbit object. When
              the secondary object is on the rendezvous capable list, this can be any object.

          id_on_orbit2: Unique identifier of the secondary satellite on-orbit object, if correlated. For
              rendezvous and proximity operations, this is the actor. When the primary object
              is a satellite being protected on the neighborhood watch list (NWL), this can be
              any object encroaching on the primary.

          id_target_sv: Optional ID of the UDL State Vector at epoch time of the target satellite. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the target state vector.

          inclination_delta_v: The Inclination DeltaV is the minimum delta velocity for the out-of-plane
              change, assuming alignment of the right ascensions measured in kilometers per
              second.

          indication_source: Identifies the source of the indication, if the latest event info was manually
              input, not computed.

          lon_tol: The tolerance value for the longitude in degrees.

          max_range: Maximum range (apogee and perigee differences) within the event interval
              measured in kilometers.

          min_plane_sep_angle: Minimum angle between the target's position and the projection of the actor's
              position into the target's nominal orbit plane over the event interval measured
              in degrees.

          min_plane_sep_epoch: Epoch time of the minimum in-plane separation angle occurrence in ISO 8601 UTC
              format with millisecond precision.

          min_range: Minimum range (apogee and perigee differences) within the event interval
              measured in kilometers.

          min_range_analysis_duration: Timespan of satellites within the range tolerance in seconds.

          min_range_epoch: Epoch time of the minimum range occurrence in ISO 8601 UTC format with
              millisecond precision.

          notes: Contains other descriptive information associated with an indicated event.

          num_sub_intervals: The number of oscillations within the event interval which are within the plane
              tolerance.

          orbit_align_del: The change in angle between the angular momentum vectors between the actor and
              target relative to plane orientation in degrees.

          orbit_plane_tol: The tolerance value for the difference in the orbital plane measured in degrees.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id1: Optional place holder for an OnOrbit ID that does not exist in UDL.

          orig_object_id2: Optional place holder for an OnOrbit ID that does not exist in UDL.

          range_threshold: The threshold of the event range in kilometers.

          range_tol: The tolerance value for the range in kilometers.

          rel_pos: Indicates the relative position vector of the event occurrence measured in
              kilometers.

          rel_pos_mag: Range of closest approach: relative position magnitude, in kilometers, of the
              difference in the physical position between the actor and target objects.

          rel_speed_mag: Indicates the closure rate specified as a relative velocity magnitude in
              kilometers per second of the difference in the velocities between the actor and
              target objects.

          rel_vel: Indicates the relative velocity vector of the event occurrence measured in
              kilometers per second.

          sat_no1: Satellite/catalog number of the target on-orbit primary object.

          sat_no2: Satellite/catalog number of the target on-orbit secondary object.

          station_lim_lon_tol: The tolerance value for the optimal longitude for station-keeping in degrees.

          target_sv_epoch: State vector epoch time of the target satellite in ISO 8601 UTC format with
              millisecond precision.

          total_delta_v: The Total DeltaV is the sum of the Hohmann and Inclination DeltaVs measured in
              kilometers per second.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/closelyspacedobjects",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "cso_state": cso_state,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "event_type": event_type,
                    "source": source,
                    "id": id,
                    "actor_sv_epoch": actor_sv_epoch,
                    "analysis_duration": analysis_duration,
                    "analysis_epoch": analysis_epoch,
                    "comp_type": comp_type,
                    "context_keys": context_keys,
                    "context_values": context_values,
                    "cso_details": cso_details,
                    "delta_v_tol": delta_v_tol,
                    "duration_threshold": duration_threshold,
                    "event_end_time": event_end_time,
                    "event_interval_coverage": event_interval_coverage,
                    "ext_id": ext_id,
                    "hohmann_delta_v": hohmann_delta_v,
                    "id_actor_sv": id_actor_sv,
                    "id_on_orbit1": id_on_orbit1,
                    "id_on_orbit2": id_on_orbit2,
                    "id_target_sv": id_target_sv,
                    "inclination_delta_v": inclination_delta_v,
                    "indication_source": indication_source,
                    "lon_tol": lon_tol,
                    "max_range": max_range,
                    "min_plane_sep_angle": min_plane_sep_angle,
                    "min_plane_sep_epoch": min_plane_sep_epoch,
                    "min_range": min_range,
                    "min_range_analysis_duration": min_range_analysis_duration,
                    "min_range_epoch": min_range_epoch,
                    "notes": notes,
                    "num_sub_intervals": num_sub_intervals,
                    "orbit_align_del": orbit_align_del,
                    "orbit_plane_tol": orbit_plane_tol,
                    "origin": origin,
                    "orig_object_id1": orig_object_id1,
                    "orig_object_id2": orig_object_id2,
                    "range_threshold": range_threshold,
                    "range_tol": range_tol,
                    "rel_pos": rel_pos,
                    "rel_pos_mag": rel_pos_mag,
                    "rel_speed_mag": rel_speed_mag,
                    "rel_vel": rel_vel,
                    "sat_no1": sat_no1,
                    "sat_no2": sat_no2,
                    "station_lim_lon_tol": station_lim_lon_tol,
                    "target_sv_epoch": target_sv_epoch,
                    "total_delta_v": total_delta_v,
                },
                closelyspacedobject_create_params.CloselyspacedobjectCreateParams,
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
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloselyspacedobjectRetrieveResponse:
        """
        Service operation to get a single CloselySpacedObjects (CSO) record by its
        unique ID passed as a path parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/closelyspacedobjects/{id}",
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
                    closelyspacedobject_retrieve_params.CloselyspacedobjectRetrieveParams,
                ),
            ),
            cast_to=CloselyspacedobjectRetrieveResponse,
        )

    def list(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CloselyspacedobjectsAbridged, AsyncOffsetPage[CloselyspacedobjectsAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/closelyspacedobjects",
            page=AsyncOffsetPage[CloselyspacedobjectsAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    closelyspacedobject_list_params.CloselyspacedobjectListParams,
                ),
            ),
            model=CloselyspacedobjectsAbridged,
        )

    async def count(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Service operation to return the count of records satisfying the specified query
        parameters. This operation is useful to determine how many records pass a
        particular query criteria without retrieving large amounts of data. See the
        queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on
        valid/required query parameter information.

        Args:
          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/closelyspacedobjects/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    closelyspacedobject_count_params.CloselyspacedobjectCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[closelyspacedobject_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        CloselySpacedObjects (CSO) records as a POST body and ingest into the database.
        This operation is not intended to be used for automated feeds into UDL. Data
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
            "/udl/closelyspacedobjects/createBulk",
            body=await async_maybe_transform(body, Iterable[closelyspacedobject_create_bulk_params.Body]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloselyspacedobjectQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/closelyspacedobjects/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloselyspacedobjectQueryHelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        event_start_time: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloselyspacedobjectTupleResponse:
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

          event_start_time: Timestamp representing the events start time in ISO 8601 UTC format with
              millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/closelyspacedobjects/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "event_start_time": event_start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    closelyspacedobject_tuple_params.CloselyspacedobjectTupleParams,
                ),
            ),
            cast_to=CloselyspacedobjectTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[closelyspacedobject_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take multiple CloselySpacedObjects (CSO) records as a POST
        body and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-closelyspacedobjects",
            body=await async_maybe_transform(body, Iterable[closelyspacedobject_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CloselyspacedobjectsResourceWithRawResponse:
    def __init__(self, closelyspacedobjects: CloselyspacedobjectsResource) -> None:
        self._closelyspacedobjects = closelyspacedobjects

        self.create = to_raw_response_wrapper(
            closelyspacedobjects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            closelyspacedobjects.retrieve,
        )
        self.list = to_raw_response_wrapper(
            closelyspacedobjects.list,
        )
        self.count = to_raw_response_wrapper(
            closelyspacedobjects.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            closelyspacedobjects.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            closelyspacedobjects.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            closelyspacedobjects.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            closelyspacedobjects.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._closelyspacedobjects.history)


class AsyncCloselyspacedobjectsResourceWithRawResponse:
    def __init__(self, closelyspacedobjects: AsyncCloselyspacedobjectsResource) -> None:
        self._closelyspacedobjects = closelyspacedobjects

        self.create = async_to_raw_response_wrapper(
            closelyspacedobjects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            closelyspacedobjects.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            closelyspacedobjects.list,
        )
        self.count = async_to_raw_response_wrapper(
            closelyspacedobjects.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            closelyspacedobjects.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            closelyspacedobjects.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            closelyspacedobjects.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            closelyspacedobjects.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._closelyspacedobjects.history)


class CloselyspacedobjectsResourceWithStreamingResponse:
    def __init__(self, closelyspacedobjects: CloselyspacedobjectsResource) -> None:
        self._closelyspacedobjects = closelyspacedobjects

        self.create = to_streamed_response_wrapper(
            closelyspacedobjects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            closelyspacedobjects.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            closelyspacedobjects.list,
        )
        self.count = to_streamed_response_wrapper(
            closelyspacedobjects.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            closelyspacedobjects.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            closelyspacedobjects.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            closelyspacedobjects.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            closelyspacedobjects.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._closelyspacedobjects.history)


class AsyncCloselyspacedobjectsResourceWithStreamingResponse:
    def __init__(self, closelyspacedobjects: AsyncCloselyspacedobjectsResource) -> None:
        self._closelyspacedobjects = closelyspacedobjects

        self.create = async_to_streamed_response_wrapper(
            closelyspacedobjects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            closelyspacedobjects.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            closelyspacedobjects.list,
        )
        self.count = async_to_streamed_response_wrapper(
            closelyspacedobjects.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            closelyspacedobjects.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            closelyspacedobjects.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            closelyspacedobjects.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            closelyspacedobjects.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._closelyspacedobjects.history)
