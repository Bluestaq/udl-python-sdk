# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    air_event_get_params,
    air_event_list_params,
    air_event_count_params,
    air_event_tuple_params,
    air_event_create_params,
    air_event_update_params,
    air_event_create_bulk_params,
    air_event_unvalidated_publish_params,
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
from ..types.air_event_get_response import AirEventGetResponse
from ..types.air_event_list_response import AirEventListResponse
from ..types.air_event_tuple_response import AirEventTupleResponse
from ..types.air_event_queryhelp_response import AirEventQueryhelpResponse

__all__ = ["AirEventsResource", "AsyncAirEventsResource"]


class AirEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AirEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AirEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AirEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AirEventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        actual_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        arct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ar_event_type: str | NotGiven = NOT_GIVEN,
        arr_purpose: str | NotGiven = NOT_GIVEN,
        ar_track_id: str | NotGiven = NOT_GIVEN,
        ar_track_name: str | NotGiven = NOT_GIVEN,
        base_alt: float | NotGiven = NOT_GIVEN,
        cancelled: bool | NotGiven = NOT_GIVEN,
        dep_purpose: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_air_event_id: str | NotGiven = NOT_GIVEN,
        external_ar_track_id: str | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        num_tankers: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        planned_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        planned_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        receivers: Iterable[air_event_create_params.Receiver] | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_event_create_params.Remark] | NotGiven = NOT_GIVEN,
        rev_track: bool | NotGiven = NOT_GIVEN,
        rzct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        rz_point: str | NotGiven = NOT_GIVEN,
        rz_type: str | NotGiven = NOT_GIVEN,
        short_track: bool | NotGiven = NOT_GIVEN,
        status_code: str | NotGiven = NOT_GIVEN,
        tankers: Iterable[air_event_create_params.Tanker] | NotGiven = NOT_GIVEN,
        track_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airevent object as a POST body and ingest
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

          source: Source of the data.

          type: Type of air event (e.g. FUEL TRANSFER, AIR DROP, etc).

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          actual_arr_time: The actual arrival time of the aircraft at the air event, in ISO 8601 UTC format
              with millisecond precision.

          actual_dep_time: The actual departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          arct: The Air Refueling Control Time is the planned time the tanker aircraft will
              transfer fuel to the receiver aircraft, in ISO 8601 UTC format, with millisecond
              precision.

          ar_event_type: Type of process used by AMC to schedule this air refueling event. Possible
              values are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched
              Theater Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S
              (Soft Air Refueling), T (Matched Theater Operation Short Notice (Theater
              Assets)), V (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short
              Notice (AMC Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z
              (Other Air Refueling).

          arr_purpose: The purpose of the air event at the arrival location. Can be either descriptive
              text such as 'fuel onload' or a purpose code specified by the provider, such as
              'A'.

          ar_track_id: Identifier of the air refueling track, if applicable.

          ar_track_name: Name of the air refueling track, if applicable.

          base_alt: Altitude of this air event, in feet.

          cancelled: Flag indicating that this air refueling event has been cancelled.

          dep_purpose: The purpose of the air event at the departure location. Can be either
              descriptive text such as 'fuel onload' or a purpose code specified by the
              provider, such as 'A'.

          est_arr_time: The current estimated arrival time of the aircraft at the air event, in ISO 8601
              UTC format with millisecond precision.

          est_dep_time: The current estimated departure time of the aircraft from the air event, in ISO
              8601 UTC format with millisecond precision.

          external_air_event_id: Optional air event ID from external systems. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          external_ar_track_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          id_mission: The UDL unique identifier of the mission associated with this air event.

          id_sortie: The UDL unique identifier of the sortie associated with this air event.

          leg_num: Identifies the Itinerary point of a sortie where an air event occurs.

          location: The location representing this air event specified as a feature Id. Locations
              specified include air refueling track Ids and air drop event locations.

          num_tankers: The number of tankers requested for an air refueling event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          planned_arr_time: The scheduled arrival time of the aircraft at the air event, in ISO 8601 UTC
              format with millisecond precision.

          planned_dep_time: The scheduled departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          priority: Priority of this air event.

          receivers: Collection of receiver aircraft associated with this Air Event.

          remarks: Collection of remarks associated with this Air Event.

          rev_track: Flag indicating if the receiver unit has requested flying an air refueling track
              in both directions.

          rzct: The Rendezvous Control Time is the planned time the tanker and receiver aircraft
              will rendezvous for an en route type air refueling event, in ISO 8601 UTC
              format, with millisecond precision.

          rz_point: Rendezvous point for the tanker and receiver during this air refueling event.
              Possible values are AN (Anchor Nav Point), AP (Anchor Pattern), CP (Control
              Point), ET (Entry Point), EX (Exit Point), IP (Initial Point), NC (Nav Check
              Point).

          rz_type: Type of rendezvous used for this air refueling event. Possible values are BUD
              (Buddy), EN (Enroute), GCI (Ground Control), PP (Point Parallel).

          short_track: Flag indicating that the receiver unit has requested flying a short portion of
              an air refueling track.

          status_code: Status of this air refueling event track reservation. Receivers are responsible
              for scheduling or reserving air refueling tracks. Possible values are A
              (Altitude Reservation), R (Reserved), or Q (Questionable).

          tankers: Collection of tanker aircraft associated with this Air Event.

          track_time: Length of time the receiver unit has requested for an air event, in hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airevent",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "type": type,
                    "id": id,
                    "actual_arr_time": actual_arr_time,
                    "actual_dep_time": actual_dep_time,
                    "arct": arct,
                    "ar_event_type": ar_event_type,
                    "arr_purpose": arr_purpose,
                    "ar_track_id": ar_track_id,
                    "ar_track_name": ar_track_name,
                    "base_alt": base_alt,
                    "cancelled": cancelled,
                    "dep_purpose": dep_purpose,
                    "est_arr_time": est_arr_time,
                    "est_dep_time": est_dep_time,
                    "external_air_event_id": external_air_event_id,
                    "external_ar_track_id": external_ar_track_id,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "leg_num": leg_num,
                    "location": location,
                    "num_tankers": num_tankers,
                    "origin": origin,
                    "planned_arr_time": planned_arr_time,
                    "planned_dep_time": planned_dep_time,
                    "priority": priority,
                    "receivers": receivers,
                    "remarks": remarks,
                    "rev_track": rev_track,
                    "rzct": rzct,
                    "rz_point": rz_point,
                    "rz_type": rz_type,
                    "short_track": short_track,
                    "status_code": status_code,
                    "tankers": tankers,
                    "track_time": track_time,
                },
                air_event_create_params.AirEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        actual_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        arct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ar_event_type: str | NotGiven = NOT_GIVEN,
        arr_purpose: str | NotGiven = NOT_GIVEN,
        ar_track_id: str | NotGiven = NOT_GIVEN,
        ar_track_name: str | NotGiven = NOT_GIVEN,
        base_alt: float | NotGiven = NOT_GIVEN,
        cancelled: bool | NotGiven = NOT_GIVEN,
        dep_purpose: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_air_event_id: str | NotGiven = NOT_GIVEN,
        external_ar_track_id: str | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        num_tankers: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        planned_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        planned_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        receivers: Iterable[air_event_update_params.Receiver] | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_event_update_params.Remark] | NotGiven = NOT_GIVEN,
        rev_track: bool | NotGiven = NOT_GIVEN,
        rzct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        rz_point: str | NotGiven = NOT_GIVEN,
        rz_type: str | NotGiven = NOT_GIVEN,
        short_track: bool | NotGiven = NOT_GIVEN,
        status_code: str | NotGiven = NOT_GIVEN,
        tankers: Iterable[air_event_update_params.Tanker] | NotGiven = NOT_GIVEN,
        track_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single airevent record.

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

          source: Source of the data.

          type: Type of air event (e.g. FUEL TRANSFER, AIR DROP, etc).

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          actual_arr_time: The actual arrival time of the aircraft at the air event, in ISO 8601 UTC format
              with millisecond precision.

          actual_dep_time: The actual departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          arct: The Air Refueling Control Time is the planned time the tanker aircraft will
              transfer fuel to the receiver aircraft, in ISO 8601 UTC format, with millisecond
              precision.

          ar_event_type: Type of process used by AMC to schedule this air refueling event. Possible
              values are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched
              Theater Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S
              (Soft Air Refueling), T (Matched Theater Operation Short Notice (Theater
              Assets)), V (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short
              Notice (AMC Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z
              (Other Air Refueling).

          arr_purpose: The purpose of the air event at the arrival location. Can be either descriptive
              text such as 'fuel onload' or a purpose code specified by the provider, such as
              'A'.

          ar_track_id: Identifier of the air refueling track, if applicable.

          ar_track_name: Name of the air refueling track, if applicable.

          base_alt: Altitude of this air event, in feet.

          cancelled: Flag indicating that this air refueling event has been cancelled.

          dep_purpose: The purpose of the air event at the departure location. Can be either
              descriptive text such as 'fuel onload' or a purpose code specified by the
              provider, such as 'A'.

          est_arr_time: The current estimated arrival time of the aircraft at the air event, in ISO 8601
              UTC format with millisecond precision.

          est_dep_time: The current estimated departure time of the aircraft from the air event, in ISO
              8601 UTC format with millisecond precision.

          external_air_event_id: Optional air event ID from external systems. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          external_ar_track_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          id_mission: The UDL unique identifier of the mission associated with this air event.

          id_sortie: The UDL unique identifier of the sortie associated with this air event.

          leg_num: Identifies the Itinerary point of a sortie where an air event occurs.

          location: The location representing this air event specified as a feature Id. Locations
              specified include air refueling track Ids and air drop event locations.

          num_tankers: The number of tankers requested for an air refueling event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          planned_arr_time: The scheduled arrival time of the aircraft at the air event, in ISO 8601 UTC
              format with millisecond precision.

          planned_dep_time: The scheduled departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          priority: Priority of this air event.

          receivers: Collection of receiver aircraft associated with this Air Event.

          remarks: Collection of remarks associated with this Air Event.

          rev_track: Flag indicating if the receiver unit has requested flying an air refueling track
              in both directions.

          rzct: The Rendezvous Control Time is the planned time the tanker and receiver aircraft
              will rendezvous for an en route type air refueling event, in ISO 8601 UTC
              format, with millisecond precision.

          rz_point: Rendezvous point for the tanker and receiver during this air refueling event.
              Possible values are AN (Anchor Nav Point), AP (Anchor Pattern), CP (Control
              Point), ET (Entry Point), EX (Exit Point), IP (Initial Point), NC (Nav Check
              Point).

          rz_type: Type of rendezvous used for this air refueling event. Possible values are BUD
              (Buddy), EN (Enroute), GCI (Ground Control), PP (Point Parallel).

          short_track: Flag indicating that the receiver unit has requested flying a short portion of
              an air refueling track.

          status_code: Status of this air refueling event track reservation. Receivers are responsible
              for scheduling or reserving air refueling tracks. Possible values are A
              (Altitude Reservation), R (Reserved), or Q (Questionable).

          tankers: Collection of tanker aircraft associated with this Air Event.

          track_time: Length of time the receiver unit has requested for an air event, in hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/airevent/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "actual_arr_time": actual_arr_time,
                    "actual_dep_time": actual_dep_time,
                    "arct": arct,
                    "ar_event_type": ar_event_type,
                    "arr_purpose": arr_purpose,
                    "ar_track_id": ar_track_id,
                    "ar_track_name": ar_track_name,
                    "base_alt": base_alt,
                    "cancelled": cancelled,
                    "dep_purpose": dep_purpose,
                    "est_arr_time": est_arr_time,
                    "est_dep_time": est_dep_time,
                    "external_air_event_id": external_air_event_id,
                    "external_ar_track_id": external_ar_track_id,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "leg_num": leg_num,
                    "location": location,
                    "num_tankers": num_tankers,
                    "origin": origin,
                    "planned_arr_time": planned_arr_time,
                    "planned_dep_time": planned_dep_time,
                    "priority": priority,
                    "receivers": receivers,
                    "remarks": remarks,
                    "rev_track": rev_track,
                    "rzct": rzct,
                    "rz_point": rz_point,
                    "rz_type": rz_type,
                    "short_track": short_track,
                    "status_code": status_code,
                    "tankers": tankers,
                    "track_time": track_time,
                },
                air_event_update_params.AirEventUpdateParams,
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
    ) -> SyncOffsetPage[AirEventListResponse]:
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
            "/udl/airevent",
            page=SyncOffsetPage[AirEventListResponse],
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
                    air_event_list_params.AirEventListParams,
                ),
            ),
            model=AirEventListResponse,
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
        Service operation to delete an airevent record specified by the passed ID path
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
            f"/udl/airevent/{id}",
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
            "/udl/airevent/count",
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
                    air_event_count_params.AirEventCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[air_event_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list
        ofService operation intended for initial integration only, to take a list of
        airevent records as a POST body and ingest into the database. This operation is
        not intended to be used for automated feeds into UDL. Data providers should
        contact the UDL team for specific role assignments and for instructions on
        setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/airevent/createBulk",
            body=maybe_transform(body, Iterable[air_event_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
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
    ) -> AirEventGetResponse:
        """
        Service operation to get a single airevent record by its unique ID passed as a
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
            f"/udl/airevent/{id}",
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
                    air_event_get_params.AirEventGetParams,
                ),
            ),
            cast_to=AirEventGetResponse,
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
    ) -> AirEventQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/airevent/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirEventQueryhelpResponse,
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
    ) -> AirEventTupleResponse:
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
            "/udl/airevent/tuple",
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
                    air_event_tuple_params.AirEventTupleParams,
                ),
            ),
            cast_to=AirEventTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[air_event_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple airevent records as a POST body and ingest
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
            "/filedrop/udl-airevent",
            body=maybe_transform(body, Iterable[air_event_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAirEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAirEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAirEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAirEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAirEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        actual_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        arct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ar_event_type: str | NotGiven = NOT_GIVEN,
        arr_purpose: str | NotGiven = NOT_GIVEN,
        ar_track_id: str | NotGiven = NOT_GIVEN,
        ar_track_name: str | NotGiven = NOT_GIVEN,
        base_alt: float | NotGiven = NOT_GIVEN,
        cancelled: bool | NotGiven = NOT_GIVEN,
        dep_purpose: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_air_event_id: str | NotGiven = NOT_GIVEN,
        external_ar_track_id: str | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        num_tankers: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        planned_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        planned_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        receivers: Iterable[air_event_create_params.Receiver] | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_event_create_params.Remark] | NotGiven = NOT_GIVEN,
        rev_track: bool | NotGiven = NOT_GIVEN,
        rzct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        rz_point: str | NotGiven = NOT_GIVEN,
        rz_type: str | NotGiven = NOT_GIVEN,
        short_track: bool | NotGiven = NOT_GIVEN,
        status_code: str | NotGiven = NOT_GIVEN,
        tankers: Iterable[air_event_create_params.Tanker] | NotGiven = NOT_GIVEN,
        track_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single airevent object as a POST body and ingest
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

          source: Source of the data.

          type: Type of air event (e.g. FUEL TRANSFER, AIR DROP, etc).

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          actual_arr_time: The actual arrival time of the aircraft at the air event, in ISO 8601 UTC format
              with millisecond precision.

          actual_dep_time: The actual departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          arct: The Air Refueling Control Time is the planned time the tanker aircraft will
              transfer fuel to the receiver aircraft, in ISO 8601 UTC format, with millisecond
              precision.

          ar_event_type: Type of process used by AMC to schedule this air refueling event. Possible
              values are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched
              Theater Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S
              (Soft Air Refueling), T (Matched Theater Operation Short Notice (Theater
              Assets)), V (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short
              Notice (AMC Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z
              (Other Air Refueling).

          arr_purpose: The purpose of the air event at the arrival location. Can be either descriptive
              text such as 'fuel onload' or a purpose code specified by the provider, such as
              'A'.

          ar_track_id: Identifier of the air refueling track, if applicable.

          ar_track_name: Name of the air refueling track, if applicable.

          base_alt: Altitude of this air event, in feet.

          cancelled: Flag indicating that this air refueling event has been cancelled.

          dep_purpose: The purpose of the air event at the departure location. Can be either
              descriptive text such as 'fuel onload' or a purpose code specified by the
              provider, such as 'A'.

          est_arr_time: The current estimated arrival time of the aircraft at the air event, in ISO 8601
              UTC format with millisecond precision.

          est_dep_time: The current estimated departure time of the aircraft from the air event, in ISO
              8601 UTC format with millisecond precision.

          external_air_event_id: Optional air event ID from external systems. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          external_ar_track_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          id_mission: The UDL unique identifier of the mission associated with this air event.

          id_sortie: The UDL unique identifier of the sortie associated with this air event.

          leg_num: Identifies the Itinerary point of a sortie where an air event occurs.

          location: The location representing this air event specified as a feature Id. Locations
              specified include air refueling track Ids and air drop event locations.

          num_tankers: The number of tankers requested for an air refueling event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          planned_arr_time: The scheduled arrival time of the aircraft at the air event, in ISO 8601 UTC
              format with millisecond precision.

          planned_dep_time: The scheduled departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          priority: Priority of this air event.

          receivers: Collection of receiver aircraft associated with this Air Event.

          remarks: Collection of remarks associated with this Air Event.

          rev_track: Flag indicating if the receiver unit has requested flying an air refueling track
              in both directions.

          rzct: The Rendezvous Control Time is the planned time the tanker and receiver aircraft
              will rendezvous for an en route type air refueling event, in ISO 8601 UTC
              format, with millisecond precision.

          rz_point: Rendezvous point for the tanker and receiver during this air refueling event.
              Possible values are AN (Anchor Nav Point), AP (Anchor Pattern), CP (Control
              Point), ET (Entry Point), EX (Exit Point), IP (Initial Point), NC (Nav Check
              Point).

          rz_type: Type of rendezvous used for this air refueling event. Possible values are BUD
              (Buddy), EN (Enroute), GCI (Ground Control), PP (Point Parallel).

          short_track: Flag indicating that the receiver unit has requested flying a short portion of
              an air refueling track.

          status_code: Status of this air refueling event track reservation. Receivers are responsible
              for scheduling or reserving air refueling tracks. Possible values are A
              (Altitude Reservation), R (Reserved), or Q (Questionable).

          tankers: Collection of tanker aircraft associated with this Air Event.

          track_time: Length of time the receiver unit has requested for an air event, in hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airevent",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "type": type,
                    "id": id,
                    "actual_arr_time": actual_arr_time,
                    "actual_dep_time": actual_dep_time,
                    "arct": arct,
                    "ar_event_type": ar_event_type,
                    "arr_purpose": arr_purpose,
                    "ar_track_id": ar_track_id,
                    "ar_track_name": ar_track_name,
                    "base_alt": base_alt,
                    "cancelled": cancelled,
                    "dep_purpose": dep_purpose,
                    "est_arr_time": est_arr_time,
                    "est_dep_time": est_dep_time,
                    "external_air_event_id": external_air_event_id,
                    "external_ar_track_id": external_ar_track_id,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "leg_num": leg_num,
                    "location": location,
                    "num_tankers": num_tankers,
                    "origin": origin,
                    "planned_arr_time": planned_arr_time,
                    "planned_dep_time": planned_dep_time,
                    "priority": priority,
                    "receivers": receivers,
                    "remarks": remarks,
                    "rev_track": rev_track,
                    "rzct": rzct,
                    "rz_point": rz_point,
                    "rz_type": rz_type,
                    "short_track": short_track,
                    "status_code": status_code,
                    "tankers": tankers,
                    "track_time": track_time,
                },
                air_event_create_params.AirEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        path_id: str,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        actual_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        actual_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        arct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ar_event_type: str | NotGiven = NOT_GIVEN,
        arr_purpose: str | NotGiven = NOT_GIVEN,
        ar_track_id: str | NotGiven = NOT_GIVEN,
        ar_track_name: str | NotGiven = NOT_GIVEN,
        base_alt: float | NotGiven = NOT_GIVEN,
        cancelled: bool | NotGiven = NOT_GIVEN,
        dep_purpose: str | NotGiven = NOT_GIVEN,
        est_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        est_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_air_event_id: str | NotGiven = NOT_GIVEN,
        external_ar_track_id: str | NotGiven = NOT_GIVEN,
        id_mission: str | NotGiven = NOT_GIVEN,
        id_sortie: str | NotGiven = NOT_GIVEN,
        leg_num: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        num_tankers: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        planned_arr_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        planned_dep_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        receivers: Iterable[air_event_update_params.Receiver] | NotGiven = NOT_GIVEN,
        remarks: Iterable[air_event_update_params.Remark] | NotGiven = NOT_GIVEN,
        rev_track: bool | NotGiven = NOT_GIVEN,
        rzct: Union[str, datetime] | NotGiven = NOT_GIVEN,
        rz_point: str | NotGiven = NOT_GIVEN,
        rz_type: str | NotGiven = NOT_GIVEN,
        short_track: bool | NotGiven = NOT_GIVEN,
        status_code: str | NotGiven = NOT_GIVEN,
        tankers: Iterable[air_event_update_params.Tanker] | NotGiven = NOT_GIVEN,
        track_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single airevent record.

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

          source: Source of the data.

          type: Type of air event (e.g. FUEL TRANSFER, AIR DROP, etc).

          body_id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          actual_arr_time: The actual arrival time of the aircraft at the air event, in ISO 8601 UTC format
              with millisecond precision.

          actual_dep_time: The actual departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          arct: The Air Refueling Control Time is the planned time the tanker aircraft will
              transfer fuel to the receiver aircraft, in ISO 8601 UTC format, with millisecond
              precision.

          ar_event_type: Type of process used by AMC to schedule this air refueling event. Possible
              values are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched
              Theater Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S
              (Soft Air Refueling), T (Matched Theater Operation Short Notice (Theater
              Assets)), V (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short
              Notice (AMC Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z
              (Other Air Refueling).

          arr_purpose: The purpose of the air event at the arrival location. Can be either descriptive
              text such as 'fuel onload' or a purpose code specified by the provider, such as
              'A'.

          ar_track_id: Identifier of the air refueling track, if applicable.

          ar_track_name: Name of the air refueling track, if applicable.

          base_alt: Altitude of this air event, in feet.

          cancelled: Flag indicating that this air refueling event has been cancelled.

          dep_purpose: The purpose of the air event at the departure location. Can be either
              descriptive text such as 'fuel onload' or a purpose code specified by the
              provider, such as 'A'.

          est_arr_time: The current estimated arrival time of the aircraft at the air event, in ISO 8601
              UTC format with millisecond precision.

          est_dep_time: The current estimated departure time of the aircraft from the air event, in ISO
              8601 UTC format with millisecond precision.

          external_air_event_id: Optional air event ID from external systems. This field has no meaning within
              UDL and is provided as a convenience for systems that require tracking of an
              internal system generated ID.

          external_ar_track_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          id_mission: The UDL unique identifier of the mission associated with this air event.

          id_sortie: The UDL unique identifier of the sortie associated with this air event.

          leg_num: Identifies the Itinerary point of a sortie where an air event occurs.

          location: The location representing this air event specified as a feature Id. Locations
              specified include air refueling track Ids and air drop event locations.

          num_tankers: The number of tankers requested for an air refueling event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          planned_arr_time: The scheduled arrival time of the aircraft at the air event, in ISO 8601 UTC
              format with millisecond precision.

          planned_dep_time: The scheduled departure time of the aircraft from the air event, in ISO 8601 UTC
              format with millisecond precision.

          priority: Priority of this air event.

          receivers: Collection of receiver aircraft associated with this Air Event.

          remarks: Collection of remarks associated with this Air Event.

          rev_track: Flag indicating if the receiver unit has requested flying an air refueling track
              in both directions.

          rzct: The Rendezvous Control Time is the planned time the tanker and receiver aircraft
              will rendezvous for an en route type air refueling event, in ISO 8601 UTC
              format, with millisecond precision.

          rz_point: Rendezvous point for the tanker and receiver during this air refueling event.
              Possible values are AN (Anchor Nav Point), AP (Anchor Pattern), CP (Control
              Point), ET (Entry Point), EX (Exit Point), IP (Initial Point), NC (Nav Check
              Point).

          rz_type: Type of rendezvous used for this air refueling event. Possible values are BUD
              (Buddy), EN (Enroute), GCI (Ground Control), PP (Point Parallel).

          short_track: Flag indicating that the receiver unit has requested flying a short portion of
              an air refueling track.

          status_code: Status of this air refueling event track reservation. Receivers are responsible
              for scheduling or reserving air refueling tracks. Possible values are A
              (Altitude Reservation), R (Reserved), or Q (Questionable).

          tankers: Collection of tanker aircraft associated with this Air Event.

          track_time: Length of time the receiver unit has requested for an air event, in hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/airevent/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "actual_arr_time": actual_arr_time,
                    "actual_dep_time": actual_dep_time,
                    "arct": arct,
                    "ar_event_type": ar_event_type,
                    "arr_purpose": arr_purpose,
                    "ar_track_id": ar_track_id,
                    "ar_track_name": ar_track_name,
                    "base_alt": base_alt,
                    "cancelled": cancelled,
                    "dep_purpose": dep_purpose,
                    "est_arr_time": est_arr_time,
                    "est_dep_time": est_dep_time,
                    "external_air_event_id": external_air_event_id,
                    "external_ar_track_id": external_ar_track_id,
                    "id_mission": id_mission,
                    "id_sortie": id_sortie,
                    "leg_num": leg_num,
                    "location": location,
                    "num_tankers": num_tankers,
                    "origin": origin,
                    "planned_arr_time": planned_arr_time,
                    "planned_dep_time": planned_dep_time,
                    "priority": priority,
                    "receivers": receivers,
                    "remarks": remarks,
                    "rev_track": rev_track,
                    "rzct": rzct,
                    "rz_point": rz_point,
                    "rz_type": rz_type,
                    "short_track": short_track,
                    "status_code": status_code,
                    "tankers": tankers,
                    "track_time": track_time,
                },
                air_event_update_params.AirEventUpdateParams,
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
    ) -> AsyncPaginator[AirEventListResponse, AsyncOffsetPage[AirEventListResponse]]:
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
            "/udl/airevent",
            page=AsyncOffsetPage[AirEventListResponse],
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
                    air_event_list_params.AirEventListParams,
                ),
            ),
            model=AirEventListResponse,
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
        Service operation to delete an airevent record specified by the passed ID path
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
            f"/udl/airevent/{id}",
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
            "/udl/airevent/count",
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
                    air_event_count_params.AirEventCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[air_event_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list
        ofService operation intended for initial integration only, to take a list of
        airevent records as a POST body and ingest into the database. This operation is
        not intended to be used for automated feeds into UDL. Data providers should
        contact the UDL team for specific role assignments and for instructions on
        setting up a permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/airevent/createBulk",
            body=await async_maybe_transform(body, Iterable[air_event_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
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
    ) -> AirEventGetResponse:
        """
        Service operation to get a single airevent record by its unique ID passed as a
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
            f"/udl/airevent/{id}",
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
                    air_event_get_params.AirEventGetParams,
                ),
            ),
            cast_to=AirEventGetResponse,
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
    ) -> AirEventQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/airevent/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AirEventQueryhelpResponse,
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
    ) -> AirEventTupleResponse:
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
            "/udl/airevent/tuple",
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
                    air_event_tuple_params.AirEventTupleParams,
                ),
            ),
            cast_to=AirEventTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[air_event_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple airevent records as a POST body and ingest
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
            "/filedrop/udl-airevent",
            body=await async_maybe_transform(body, Iterable[air_event_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AirEventsResourceWithRawResponse:
    def __init__(self, air_events: AirEventsResource) -> None:
        self._air_events = air_events

        self.create = to_raw_response_wrapper(
            air_events.create,
        )
        self.update = to_raw_response_wrapper(
            air_events.update,
        )
        self.list = to_raw_response_wrapper(
            air_events.list,
        )
        self.delete = to_raw_response_wrapper(
            air_events.delete,
        )
        self.count = to_raw_response_wrapper(
            air_events.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            air_events.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            air_events.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            air_events.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            air_events.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            air_events.unvalidated_publish,
        )


class AsyncAirEventsResourceWithRawResponse:
    def __init__(self, air_events: AsyncAirEventsResource) -> None:
        self._air_events = air_events

        self.create = async_to_raw_response_wrapper(
            air_events.create,
        )
        self.update = async_to_raw_response_wrapper(
            air_events.update,
        )
        self.list = async_to_raw_response_wrapper(
            air_events.list,
        )
        self.delete = async_to_raw_response_wrapper(
            air_events.delete,
        )
        self.count = async_to_raw_response_wrapper(
            air_events.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            air_events.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            air_events.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            air_events.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            air_events.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            air_events.unvalidated_publish,
        )


class AirEventsResourceWithStreamingResponse:
    def __init__(self, air_events: AirEventsResource) -> None:
        self._air_events = air_events

        self.create = to_streamed_response_wrapper(
            air_events.create,
        )
        self.update = to_streamed_response_wrapper(
            air_events.update,
        )
        self.list = to_streamed_response_wrapper(
            air_events.list,
        )
        self.delete = to_streamed_response_wrapper(
            air_events.delete,
        )
        self.count = to_streamed_response_wrapper(
            air_events.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            air_events.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            air_events.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            air_events.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            air_events.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            air_events.unvalidated_publish,
        )


class AsyncAirEventsResourceWithStreamingResponse:
    def __init__(self, air_events: AsyncAirEventsResource) -> None:
        self._air_events = air_events

        self.create = async_to_streamed_response_wrapper(
            air_events.create,
        )
        self.update = async_to_streamed_response_wrapper(
            air_events.update,
        )
        self.list = async_to_streamed_response_wrapper(
            air_events.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            air_events.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            air_events.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            air_events.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            air_events.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            air_events.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            air_events.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            air_events.unvalidated_publish,
        )
