# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    track_route_get_params,
    track_route_list_params,
    track_route_count_params,
    track_route_tuple_params,
    track_route_create_params,
    track_route_update_params,
    track_route_unvalidated_publish_params,
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
from ...types.track_route_ingest_param import TrackRouteIngestParam
from ...types.route_points_ingest_param import RoutePointsIngestParam
from ...types.track_route_list_response import TrackRouteListResponse
from ...types.track_route_tuple_response import TrackRouteTupleResponse
from ...types.altitude_blocks_ingest_param import AltitudeBlocksIngestParam
from ...types.track_route.track_route_full import TrackRouteFull
from ...types.point_of_contact_ingest_param import PointOfContactIngestParam
from ...types.track_route_queryhelp_response import TrackRouteQueryhelpResponse

__all__ = ["TrackRouteResource", "AsyncTrackRouteResource"]


class TrackRouteResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> TrackRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TrackRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrackRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return TrackRouteResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_update_date: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        altitude_blocks: Iterable[AltitudeBlocksIngestParam] | NotGiven = NOT_GIVEN,
        apn_setting: str | NotGiven = NOT_GIVEN,
        apx_beacon_code: str | NotGiven = NOT_GIVEN,
        artcc_message: str | NotGiven = NOT_GIVEN,
        creating_org: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_used_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        location_track_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        poc: Iterable[PointOfContactIngestParam] | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        receiver_tanker_ch_code: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        route_points: Iterable[RoutePointsIngestParam] | NotGiven = NOT_GIVEN,
        scheduler_org_name: str | NotGiven = NOT_GIVEN,
        scheduler_org_unit: str | NotGiven = NOT_GIVEN,
        sec_freq: float | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        sic: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_name: str | NotGiven = NOT_GIVEN,
        type_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single trackroute record as a POST body and ingest
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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          type: The track route type represented by this record (ex. AIR REFUELING).

          id: Unique identifier of the record, auto-generated by the system.

          altitude_blocks: Minimum and maximum altitude bounds for the track.

          apn_setting: The APN radar code sent and received by the aircraft for identification.

          apx_beacon_code: The APX radar code sent and received by the aircraft for identification.

          artcc_message: Air Refueling Track Control Center message.

          creating_org: The name of the creating organization of the track route.

          direction: The principal compass direction (cardinal or ordinal) of the track route.

          effective_date: The date which the DAFIF track was last updated/validated in ISO 8601 UTC format
              with millisecond precision.

          external_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          last_used_date: Used to show last time the track route was added to an itinerary in ISO 8601 UTC
              format with millisecond precision.

          location_track_id: Track location ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          poc: Point of contacts for scheduling or modifying the route.

          pri_freq: The primary UHF radio frequency used for the track route in megahertz.

          receiver_tanker_ch_code: The receiver tanker channel identifer for air refueling tracks.

          region_code: Region code indicating where the track resides as determined by the data source.

          region_name: Region where the track resides.

          review_date: Date the track needs to be reviewed for accuracy or deletion in ISO 8601 UTC
              format with millisecond precision.

          route_points: Points identified within the route.

          scheduler_org_name: Point of contact for the air refueling track route scheduler.

          scheduler_org_unit: The unit responsible for scheduling the track route.

          sec_freq: The secondary UHF radio frequency used for the track route in megahertz.

          short_name: Abbreviated name of the track.

          sic: Standard Indicator Code of the air refueling track.

          track_id: Identifier of the track.

          track_name: Name of the track.

          type_code: Type of process used by AMC to schedule an air refueling event. Possible values
              are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched Theater
              Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S (Soft Air
              Refueling), T (Matched Theater Operation Short Notice (Theater Assets)), V
              (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short Notice (AMC
              Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z (Other Air
              Refueling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/trackroute",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "last_update_date": last_update_date,
                    "source": source,
                    "type": type,
                    "id": id,
                    "altitude_blocks": altitude_blocks,
                    "apn_setting": apn_setting,
                    "apx_beacon_code": apx_beacon_code,
                    "artcc_message": artcc_message,
                    "creating_org": creating_org,
                    "direction": direction,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "last_used_date": last_used_date,
                    "location_track_id": location_track_id,
                    "origin": origin,
                    "poc": poc,
                    "pri_freq": pri_freq,
                    "receiver_tanker_ch_code": receiver_tanker_ch_code,
                    "region_code": region_code,
                    "region_name": region_name,
                    "review_date": review_date,
                    "route_points": route_points,
                    "scheduler_org_name": scheduler_org_name,
                    "scheduler_org_unit": scheduler_org_unit,
                    "sec_freq": sec_freq,
                    "short_name": short_name,
                    "sic": sic,
                    "track_id": track_id,
                    "track_name": track_name,
                    "type_code": type_code,
                },
                track_route_create_params.TrackRouteCreateParams,
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
        last_update_date: Union[str, datetime],
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        altitude_blocks: Iterable[AltitudeBlocksIngestParam] | NotGiven = NOT_GIVEN,
        apn_setting: str | NotGiven = NOT_GIVEN,
        apx_beacon_code: str | NotGiven = NOT_GIVEN,
        artcc_message: str | NotGiven = NOT_GIVEN,
        creating_org: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_used_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        location_track_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        poc: Iterable[PointOfContactIngestParam] | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        receiver_tanker_ch_code: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        route_points: Iterable[RoutePointsIngestParam] | NotGiven = NOT_GIVEN,
        scheduler_org_name: str | NotGiven = NOT_GIVEN,
        scheduler_org_unit: str | NotGiven = NOT_GIVEN,
        sec_freq: float | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        sic: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_name: str | NotGiven = NOT_GIVEN,
        type_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single trackroute record.

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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          type: The track route type represented by this record (ex. AIR REFUELING).

          body_id: Unique identifier of the record, auto-generated by the system.

          altitude_blocks: Minimum and maximum altitude bounds for the track.

          apn_setting: The APN radar code sent and received by the aircraft for identification.

          apx_beacon_code: The APX radar code sent and received by the aircraft for identification.

          artcc_message: Air Refueling Track Control Center message.

          creating_org: The name of the creating organization of the track route.

          direction: The principal compass direction (cardinal or ordinal) of the track route.

          effective_date: The date which the DAFIF track was last updated/validated in ISO 8601 UTC format
              with millisecond precision.

          external_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          last_used_date: Used to show last time the track route was added to an itinerary in ISO 8601 UTC
              format with millisecond precision.

          location_track_id: Track location ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          poc: Point of contacts for scheduling or modifying the route.

          pri_freq: The primary UHF radio frequency used for the track route in megahertz.

          receiver_tanker_ch_code: The receiver tanker channel identifer for air refueling tracks.

          region_code: Region code indicating where the track resides as determined by the data source.

          region_name: Region where the track resides.

          review_date: Date the track needs to be reviewed for accuracy or deletion in ISO 8601 UTC
              format with millisecond precision.

          route_points: Points identified within the route.

          scheduler_org_name: Point of contact for the air refueling track route scheduler.

          scheduler_org_unit: The unit responsible for scheduling the track route.

          sec_freq: The secondary UHF radio frequency used for the track route in megahertz.

          short_name: Abbreviated name of the track.

          sic: Standard Indicator Code of the air refueling track.

          track_id: Identifier of the track.

          track_name: Name of the track.

          type_code: Type of process used by AMC to schedule an air refueling event. Possible values
              are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched Theater
              Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S (Soft Air
              Refueling), T (Matched Theater Operation Short Notice (Theater Assets)), V
              (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short Notice (AMC
              Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z (Other Air
              Refueling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/trackroute/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "last_update_date": last_update_date,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "altitude_blocks": altitude_blocks,
                    "apn_setting": apn_setting,
                    "apx_beacon_code": apx_beacon_code,
                    "artcc_message": artcc_message,
                    "creating_org": creating_org,
                    "direction": direction,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "last_used_date": last_used_date,
                    "location_track_id": location_track_id,
                    "origin": origin,
                    "poc": poc,
                    "pri_freq": pri_freq,
                    "receiver_tanker_ch_code": receiver_tanker_ch_code,
                    "region_code": region_code,
                    "region_name": region_name,
                    "review_date": review_date,
                    "route_points": route_points,
                    "scheduler_org_name": scheduler_org_name,
                    "scheduler_org_unit": scheduler_org_unit,
                    "sec_freq": sec_freq,
                    "short_name": short_name,
                    "sic": sic,
                    "track_id": track_id,
                    "track_name": track_name,
                    "type_code": type_code,
                },
                track_route_update_params.TrackRouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        last_update_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[TrackRouteListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/trackroute",
            page=SyncOffsetPage[TrackRouteListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "last_update_date": last_update_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    track_route_list_params.TrackRouteListParams,
                ),
            ),
            model=TrackRouteListResponse,
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
        Service operation to delete a trackroute record specified by the passed ID path
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
            f"/udl/trackroute/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def count(
        self,
        *,
        last_update_date: Union[str, datetime],
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
          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/trackroute/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "last_update_date": last_update_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    track_route_count_params.TrackRouteCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[TrackRouteIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        trackroute records as a POST body and ingest into the database. This operation
        is not intended to be used for automated feeds into UDL. Data providers should
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
            "/udl/trackroute/createBulk",
            body=maybe_transform(body, Iterable[TrackRouteIngestParam]),
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
    ) -> TrackRouteFull:
        """
        Service operation to get a single trackroute record by its unique ID passed as a
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
            f"/udl/trackroute/{id}",
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
                    track_route_get_params.TrackRouteGetParams,
                ),
            ),
            cast_to=TrackRouteFull,
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
    ) -> TrackRouteQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/trackroute/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackRouteQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        last_update_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrackRouteTupleResponse:
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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/trackroute/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "last_update_date": last_update_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    track_route_tuple_params.TrackRouteTupleParams,
                ),
            ),
            cast_to=TrackRouteTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_update_date: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        altitude_blocks: Iterable[AltitudeBlocksIngestParam] | NotGiven = NOT_GIVEN,
        apn_setting: str | NotGiven = NOT_GIVEN,
        apx_beacon_code: str | NotGiven = NOT_GIVEN,
        artcc_message: str | NotGiven = NOT_GIVEN,
        creating_org: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_used_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        location_track_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        poc: Iterable[PointOfContactIngestParam] | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        receiver_tanker_ch_code: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        route_points: Iterable[RoutePointsIngestParam] | NotGiven = NOT_GIVEN,
        scheduler_org_name: str | NotGiven = NOT_GIVEN,
        scheduler_org_unit: str | NotGiven = NOT_GIVEN,
        sec_freq: float | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        sic: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_name: str | NotGiven = NOT_GIVEN,
        type_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple trackroute records as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          type: The track route type represented by this record (ex. AIR REFUELING).

          id: Unique identifier of the record, auto-generated by the system.

          altitude_blocks: Minimum and maximum altitude bounds for the track.

          apn_setting: The APN radar code sent and received by the aircraft for identification.

          apx_beacon_code: The APX radar code sent and received by the aircraft for identification.

          artcc_message: Air Refueling Track Control Center message.

          creating_org: The name of the creating organization of the track route.

          direction: The principal compass direction (cardinal or ordinal) of the track route.

          effective_date: The date which the DAFIF track was last updated/validated in ISO 8601 UTC format
              with millisecond precision.

          external_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          last_used_date: Used to show last time the track route was added to an itinerary in ISO 8601 UTC
              format with millisecond precision.

          location_track_id: Track location ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          poc: Point of contacts for scheduling or modifying the route.

          pri_freq: The primary UHF radio frequency used for the track route in megahertz.

          receiver_tanker_ch_code: The receiver tanker channel identifer for air refueling tracks.

          region_code: Region code indicating where the track resides as determined by the data source.

          region_name: Region where the track resides.

          review_date: Date the track needs to be reviewed for accuracy or deletion in ISO 8601 UTC
              format with millisecond precision.

          route_points: Points identified within the route.

          scheduler_org_name: Point of contact for the air refueling track route scheduler.

          scheduler_org_unit: The unit responsible for scheduling the track route.

          sec_freq: The secondary UHF radio frequency used for the track route in megahertz.

          short_name: Abbreviated name of the track.

          sic: Standard Indicator Code of the air refueling track.

          track_id: Identifier of the track.

          track_name: Name of the track.

          type_code: Type of process used by AMC to schedule an air refueling event. Possible values
              are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched Theater
              Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S (Soft Air
              Refueling), T (Matched Theater Operation Short Notice (Theater Assets)), V
              (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short Notice (AMC
              Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z (Other Air
              Refueling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-trackroute",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "last_update_date": last_update_date,
                    "source": source,
                    "type": type,
                    "id": id,
                    "altitude_blocks": altitude_blocks,
                    "apn_setting": apn_setting,
                    "apx_beacon_code": apx_beacon_code,
                    "artcc_message": artcc_message,
                    "creating_org": creating_org,
                    "direction": direction,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "last_used_date": last_used_date,
                    "location_track_id": location_track_id,
                    "origin": origin,
                    "poc": poc,
                    "pri_freq": pri_freq,
                    "receiver_tanker_ch_code": receiver_tanker_ch_code,
                    "region_code": region_code,
                    "region_name": region_name,
                    "review_date": review_date,
                    "route_points": route_points,
                    "scheduler_org_name": scheduler_org_name,
                    "scheduler_org_unit": scheduler_org_unit,
                    "sec_freq": sec_freq,
                    "short_name": short_name,
                    "sic": sic,
                    "track_id": track_id,
                    "track_name": track_name,
                    "type_code": type_code,
                },
                track_route_unvalidated_publish_params.TrackRouteUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTrackRouteResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTrackRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTrackRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrackRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncTrackRouteResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_update_date: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        altitude_blocks: Iterable[AltitudeBlocksIngestParam] | NotGiven = NOT_GIVEN,
        apn_setting: str | NotGiven = NOT_GIVEN,
        apx_beacon_code: str | NotGiven = NOT_GIVEN,
        artcc_message: str | NotGiven = NOT_GIVEN,
        creating_org: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_used_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        location_track_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        poc: Iterable[PointOfContactIngestParam] | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        receiver_tanker_ch_code: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        route_points: Iterable[RoutePointsIngestParam] | NotGiven = NOT_GIVEN,
        scheduler_org_name: str | NotGiven = NOT_GIVEN,
        scheduler_org_unit: str | NotGiven = NOT_GIVEN,
        sec_freq: float | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        sic: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_name: str | NotGiven = NOT_GIVEN,
        type_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single trackroute record as a POST body and ingest
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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          type: The track route type represented by this record (ex. AIR REFUELING).

          id: Unique identifier of the record, auto-generated by the system.

          altitude_blocks: Minimum and maximum altitude bounds for the track.

          apn_setting: The APN radar code sent and received by the aircraft for identification.

          apx_beacon_code: The APX radar code sent and received by the aircraft for identification.

          artcc_message: Air Refueling Track Control Center message.

          creating_org: The name of the creating organization of the track route.

          direction: The principal compass direction (cardinal or ordinal) of the track route.

          effective_date: The date which the DAFIF track was last updated/validated in ISO 8601 UTC format
              with millisecond precision.

          external_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          last_used_date: Used to show last time the track route was added to an itinerary in ISO 8601 UTC
              format with millisecond precision.

          location_track_id: Track location ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          poc: Point of contacts for scheduling or modifying the route.

          pri_freq: The primary UHF radio frequency used for the track route in megahertz.

          receiver_tanker_ch_code: The receiver tanker channel identifer for air refueling tracks.

          region_code: Region code indicating where the track resides as determined by the data source.

          region_name: Region where the track resides.

          review_date: Date the track needs to be reviewed for accuracy or deletion in ISO 8601 UTC
              format with millisecond precision.

          route_points: Points identified within the route.

          scheduler_org_name: Point of contact for the air refueling track route scheduler.

          scheduler_org_unit: The unit responsible for scheduling the track route.

          sec_freq: The secondary UHF radio frequency used for the track route in megahertz.

          short_name: Abbreviated name of the track.

          sic: Standard Indicator Code of the air refueling track.

          track_id: Identifier of the track.

          track_name: Name of the track.

          type_code: Type of process used by AMC to schedule an air refueling event. Possible values
              are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched Theater
              Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S (Soft Air
              Refueling), T (Matched Theater Operation Short Notice (Theater Assets)), V
              (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short Notice (AMC
              Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z (Other Air
              Refueling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/trackroute",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "last_update_date": last_update_date,
                    "source": source,
                    "type": type,
                    "id": id,
                    "altitude_blocks": altitude_blocks,
                    "apn_setting": apn_setting,
                    "apx_beacon_code": apx_beacon_code,
                    "artcc_message": artcc_message,
                    "creating_org": creating_org,
                    "direction": direction,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "last_used_date": last_used_date,
                    "location_track_id": location_track_id,
                    "origin": origin,
                    "poc": poc,
                    "pri_freq": pri_freq,
                    "receiver_tanker_ch_code": receiver_tanker_ch_code,
                    "region_code": region_code,
                    "region_name": region_name,
                    "review_date": review_date,
                    "route_points": route_points,
                    "scheduler_org_name": scheduler_org_name,
                    "scheduler_org_unit": scheduler_org_unit,
                    "sec_freq": sec_freq,
                    "short_name": short_name,
                    "sic": sic,
                    "track_id": track_id,
                    "track_name": track_name,
                    "type_code": type_code,
                },
                track_route_create_params.TrackRouteCreateParams,
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
        last_update_date: Union[str, datetime],
        source: str,
        type: str,
        body_id: str | NotGiven = NOT_GIVEN,
        altitude_blocks: Iterable[AltitudeBlocksIngestParam] | NotGiven = NOT_GIVEN,
        apn_setting: str | NotGiven = NOT_GIVEN,
        apx_beacon_code: str | NotGiven = NOT_GIVEN,
        artcc_message: str | NotGiven = NOT_GIVEN,
        creating_org: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_used_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        location_track_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        poc: Iterable[PointOfContactIngestParam] | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        receiver_tanker_ch_code: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        route_points: Iterable[RoutePointsIngestParam] | NotGiven = NOT_GIVEN,
        scheduler_org_name: str | NotGiven = NOT_GIVEN,
        scheduler_org_unit: str | NotGiven = NOT_GIVEN,
        sec_freq: float | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        sic: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_name: str | NotGiven = NOT_GIVEN,
        type_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single trackroute record.

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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          type: The track route type represented by this record (ex. AIR REFUELING).

          body_id: Unique identifier of the record, auto-generated by the system.

          altitude_blocks: Minimum and maximum altitude bounds for the track.

          apn_setting: The APN radar code sent and received by the aircraft for identification.

          apx_beacon_code: The APX radar code sent and received by the aircraft for identification.

          artcc_message: Air Refueling Track Control Center message.

          creating_org: The name of the creating organization of the track route.

          direction: The principal compass direction (cardinal or ordinal) of the track route.

          effective_date: The date which the DAFIF track was last updated/validated in ISO 8601 UTC format
              with millisecond precision.

          external_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          last_used_date: Used to show last time the track route was added to an itinerary in ISO 8601 UTC
              format with millisecond precision.

          location_track_id: Track location ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          poc: Point of contacts for scheduling or modifying the route.

          pri_freq: The primary UHF radio frequency used for the track route in megahertz.

          receiver_tanker_ch_code: The receiver tanker channel identifer for air refueling tracks.

          region_code: Region code indicating where the track resides as determined by the data source.

          region_name: Region where the track resides.

          review_date: Date the track needs to be reviewed for accuracy or deletion in ISO 8601 UTC
              format with millisecond precision.

          route_points: Points identified within the route.

          scheduler_org_name: Point of contact for the air refueling track route scheduler.

          scheduler_org_unit: The unit responsible for scheduling the track route.

          sec_freq: The secondary UHF radio frequency used for the track route in megahertz.

          short_name: Abbreviated name of the track.

          sic: Standard Indicator Code of the air refueling track.

          track_id: Identifier of the track.

          track_name: Name of the track.

          type_code: Type of process used by AMC to schedule an air refueling event. Possible values
              are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched Theater
              Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S (Soft Air
              Refueling), T (Matched Theater Operation Short Notice (Theater Assets)), V
              (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short Notice (AMC
              Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z (Other Air
              Refueling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/trackroute/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "last_update_date": last_update_date,
                    "source": source,
                    "type": type,
                    "body_id": body_id,
                    "altitude_blocks": altitude_blocks,
                    "apn_setting": apn_setting,
                    "apx_beacon_code": apx_beacon_code,
                    "artcc_message": artcc_message,
                    "creating_org": creating_org,
                    "direction": direction,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "last_used_date": last_used_date,
                    "location_track_id": location_track_id,
                    "origin": origin,
                    "poc": poc,
                    "pri_freq": pri_freq,
                    "receiver_tanker_ch_code": receiver_tanker_ch_code,
                    "region_code": region_code,
                    "region_name": region_name,
                    "review_date": review_date,
                    "route_points": route_points,
                    "scheduler_org_name": scheduler_org_name,
                    "scheduler_org_unit": scheduler_org_unit,
                    "sec_freq": sec_freq,
                    "short_name": short_name,
                    "sic": sic,
                    "track_id": track_id,
                    "track_name": track_name,
                    "type_code": type_code,
                },
                track_route_update_params.TrackRouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        last_update_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TrackRouteListResponse, AsyncOffsetPage[TrackRouteListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/trackroute",
            page=AsyncOffsetPage[TrackRouteListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "last_update_date": last_update_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    track_route_list_params.TrackRouteListParams,
                ),
            ),
            model=TrackRouteListResponse,
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
        Service operation to delete a trackroute record specified by the passed ID path
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
            f"/udl/trackroute/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def count(
        self,
        *,
        last_update_date: Union[str, datetime],
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
          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/trackroute/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "last_update_date": last_update_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    track_route_count_params.TrackRouteCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[TrackRouteIngestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        trackroute records as a POST body and ingest into the database. This operation
        is not intended to be used for automated feeds into UDL. Data providers should
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
            "/udl/trackroute/createBulk",
            body=await async_maybe_transform(body, Iterable[TrackRouteIngestParam]),
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
    ) -> TrackRouteFull:
        """
        Service operation to get a single trackroute record by its unique ID passed as a
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
            f"/udl/trackroute/{id}",
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
                    track_route_get_params.TrackRouteGetParams,
                ),
            ),
            cast_to=TrackRouteFull,
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
    ) -> TrackRouteQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/trackroute/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackRouteQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        last_update_date: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrackRouteTupleResponse:
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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/trackroute/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "last_update_date": last_update_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    track_route_tuple_params.TrackRouteTupleParams,
                ),
            ),
            cast_to=TrackRouteTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        last_update_date: Union[str, datetime],
        source: str,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        altitude_blocks: Iterable[AltitudeBlocksIngestParam] | NotGiven = NOT_GIVEN,
        apn_setting: str | NotGiven = NOT_GIVEN,
        apx_beacon_code: str | NotGiven = NOT_GIVEN,
        artcc_message: str | NotGiven = NOT_GIVEN,
        creating_org: str | NotGiven = NOT_GIVEN,
        direction: str | NotGiven = NOT_GIVEN,
        effective_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        last_used_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        location_track_id: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        poc: Iterable[PointOfContactIngestParam] | NotGiven = NOT_GIVEN,
        pri_freq: float | NotGiven = NOT_GIVEN,
        receiver_tanker_ch_code: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        region_name: str | NotGiven = NOT_GIVEN,
        review_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        route_points: Iterable[RoutePointsIngestParam] | NotGiven = NOT_GIVEN,
        scheduler_org_name: str | NotGiven = NOT_GIVEN,
        scheduler_org_unit: str | NotGiven = NOT_GIVEN,
        sec_freq: float | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        sic: str | NotGiven = NOT_GIVEN,
        track_id: str | NotGiven = NOT_GIVEN,
        track_name: str | NotGiven = NOT_GIVEN,
        type_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple trackroute records as a POST body and ingest
        into the database. This operation is intended to be used for automated feeds
        into UDL. A specific role is required to perform this service operation. Please
        contact the UDL team for assistance.

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

          last_update_date: The last updated date of the track route in ISO 8601 UTC format with millisecond
              precision.

          source: Source of the data.

          type: The track route type represented by this record (ex. AIR REFUELING).

          id: Unique identifier of the record, auto-generated by the system.

          altitude_blocks: Minimum and maximum altitude bounds for the track.

          apn_setting: The APN radar code sent and received by the aircraft for identification.

          apx_beacon_code: The APX radar code sent and received by the aircraft for identification.

          artcc_message: Air Refueling Track Control Center message.

          creating_org: The name of the creating organization of the track route.

          direction: The principal compass direction (cardinal or ordinal) of the track route.

          effective_date: The date which the DAFIF track was last updated/validated in ISO 8601 UTC format
              with millisecond precision.

          external_id: Optional air refueling track ID from external systems. This field has no meaning
              within UDL and is provided as a convenience for systems that require tracking of
              an internal system generated ID.

          last_used_date: Used to show last time the track route was added to an itinerary in ISO 8601 UTC
              format with millisecond precision.

          location_track_id: Track location ID.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          poc: Point of contacts for scheduling or modifying the route.

          pri_freq: The primary UHF radio frequency used for the track route in megahertz.

          receiver_tanker_ch_code: The receiver tanker channel identifer for air refueling tracks.

          region_code: Region code indicating where the track resides as determined by the data source.

          region_name: Region where the track resides.

          review_date: Date the track needs to be reviewed for accuracy or deletion in ISO 8601 UTC
              format with millisecond precision.

          route_points: Points identified within the route.

          scheduler_org_name: Point of contact for the air refueling track route scheduler.

          scheduler_org_unit: The unit responsible for scheduling the track route.

          sec_freq: The secondary UHF radio frequency used for the track route in megahertz.

          short_name: Abbreviated name of the track.

          sic: Standard Indicator Code of the air refueling track.

          track_id: Identifier of the track.

          track_name: Name of the track.

          type_code: Type of process used by AMC to schedule an air refueling event. Possible values
              are A (Matched Long Range), F (Matched AMC Short Notice), N (Unmatched Theater
              Operation Short Notice (Theater Assets)), R, Unmatched Long Range, S (Soft Air
              Refueling), T (Matched Theater Operation Short Notice (Theater Assets)), V
              (Unmatched AMC Short Notice), X (Unmatched Theater Operation Short Notice (AMC
              Assets)), Y (Matched Theater Operation Short Notice (AMC Assets)), Z (Other Air
              Refueling).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-trackroute",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "last_update_date": last_update_date,
                    "source": source,
                    "type": type,
                    "id": id,
                    "altitude_blocks": altitude_blocks,
                    "apn_setting": apn_setting,
                    "apx_beacon_code": apx_beacon_code,
                    "artcc_message": artcc_message,
                    "creating_org": creating_org,
                    "direction": direction,
                    "effective_date": effective_date,
                    "external_id": external_id,
                    "last_used_date": last_used_date,
                    "location_track_id": location_track_id,
                    "origin": origin,
                    "poc": poc,
                    "pri_freq": pri_freq,
                    "receiver_tanker_ch_code": receiver_tanker_ch_code,
                    "region_code": region_code,
                    "region_name": region_name,
                    "review_date": review_date,
                    "route_points": route_points,
                    "scheduler_org_name": scheduler_org_name,
                    "scheduler_org_unit": scheduler_org_unit,
                    "sec_freq": sec_freq,
                    "short_name": short_name,
                    "sic": sic,
                    "track_id": track_id,
                    "track_name": track_name,
                    "type_code": type_code,
                },
                track_route_unvalidated_publish_params.TrackRouteUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TrackRouteResourceWithRawResponse:
    def __init__(self, track_route: TrackRouteResource) -> None:
        self._track_route = track_route

        self.create = to_raw_response_wrapper(
            track_route.create,
        )
        self.update = to_raw_response_wrapper(
            track_route.update,
        )
        self.list = to_raw_response_wrapper(
            track_route.list,
        )
        self.delete = to_raw_response_wrapper(
            track_route.delete,
        )
        self.count = to_raw_response_wrapper(
            track_route.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            track_route.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            track_route.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            track_route.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            track_route.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            track_route.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._track_route.history)


class AsyncTrackRouteResourceWithRawResponse:
    def __init__(self, track_route: AsyncTrackRouteResource) -> None:
        self._track_route = track_route

        self.create = async_to_raw_response_wrapper(
            track_route.create,
        )
        self.update = async_to_raw_response_wrapper(
            track_route.update,
        )
        self.list = async_to_raw_response_wrapper(
            track_route.list,
        )
        self.delete = async_to_raw_response_wrapper(
            track_route.delete,
        )
        self.count = async_to_raw_response_wrapper(
            track_route.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            track_route.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            track_route.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            track_route.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            track_route.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            track_route.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._track_route.history)


class TrackRouteResourceWithStreamingResponse:
    def __init__(self, track_route: TrackRouteResource) -> None:
        self._track_route = track_route

        self.create = to_streamed_response_wrapper(
            track_route.create,
        )
        self.update = to_streamed_response_wrapper(
            track_route.update,
        )
        self.list = to_streamed_response_wrapper(
            track_route.list,
        )
        self.delete = to_streamed_response_wrapper(
            track_route.delete,
        )
        self.count = to_streamed_response_wrapper(
            track_route.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            track_route.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            track_route.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            track_route.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            track_route.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            track_route.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._track_route.history)


class AsyncTrackRouteResourceWithStreamingResponse:
    def __init__(self, track_route: AsyncTrackRouteResource) -> None:
        self._track_route = track_route

        self.create = async_to_streamed_response_wrapper(
            track_route.create,
        )
        self.update = async_to_streamed_response_wrapper(
            track_route.update,
        )
        self.list = async_to_streamed_response_wrapper(
            track_route.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            track_route.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            track_route.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            track_route.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            track_route.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            track_route.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            track_route.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            track_route.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._track_route.history)
