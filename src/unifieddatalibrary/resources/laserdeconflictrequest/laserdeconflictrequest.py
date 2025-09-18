# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    laserdeconflictrequest_get_params,
    laserdeconflictrequest_list_params,
    laserdeconflictrequest_count_params,
    laserdeconflictrequest_tuple_params,
    laserdeconflictrequest_create_params,
    laserdeconflictrequest_unvalidated_publish_params,
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
from ...types.laserdeconflictrequest_get_response import LaserdeconflictrequestGetResponse
from ...types.laserdeconflictrequest_list_response import LaserdeconflictrequestListResponse
from ...types.laserdeconflictrequest_tuple_response import LaserdeconflictrequestTupleResponse
from ...types.laserdeconflictrequest_queryhelp_response import LaserdeconflictrequestQueryhelpResponse

__all__ = ["LaserdeconflictrequestResource", "AsyncLaserdeconflictrequestResource"]


class LaserdeconflictrequestResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> LaserdeconflictrequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LaserdeconflictrequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LaserdeconflictrequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return LaserdeconflictrequestResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_date: Union[str, datetime],
        id_laser_emitters: SequenceNotStr[str],
        num_targets: int,
        request_id: str,
        request_ts: Union[str, datetime],
        source: str,
        start_date: Union[str, datetime],
        id: str | Omit = omit,
        centerline_azimuth: float | Omit = omit,
        centerline_elevation: float | Omit = omit,
        default_cha: float | Omit = omit,
        enable_dss: bool | Omit = omit,
        fixed_points: Iterable[laserdeconflictrequest_create_params.FixedPoint] | Omit = omit,
        geopotential_model: str | Omit = omit,
        laser_deconflict_targets: Iterable[laserdeconflictrequest_create_params.LaserDeconflictTarget] | Omit = omit,
        laser_system_name: str | Omit = omit,
        length_centerline: float | Omit = omit,
        length_left_right: float | Omit = omit,
        length_up_down: float | Omit = omit,
        maximum_height: float | Omit = omit,
        minimum_height: float | Omit = omit,
        mission_name: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        platform_location_name: str | Omit = omit,
        platform_location_type: str | Omit = omit,
        program_id: str | Omit = omit,
        propagator: str | Omit = omit,
        protect_list: Iterable[int] | Omit = omit,
        sat_no: int | Omit = omit,
        source_enabled: bool | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_enabled: bool | Omit = omit,
        target_type: str | Omit = omit,
        transaction_id: str | Omit = omit,
        treat_earth_as: str | Omit = omit,
        use_field_of_regard: bool | Omit = omit,
        victim_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single LaserDeconflictRequest record as a POST body
        and ingest into the database. This operation does not persist any
        LaserDeconflictTarget datatypes that may be present in the body of the request.
        This operation is not intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

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

          end_date: End date of the time windows associated with this LaserDeconflictRequest, in ISO
              8601 UTC format with millisecond precision.

          id_laser_emitters: A list containing the id strings of the LaserEmitter records in UDL detailing
              the physical parameters of each laser/emitter operationally involved with this
              request. All laser/emitter components must be accurately described using the
              LaserEmitter schema and ingested into the UDL LaserEmitter service before
              creating a LaserDeconflictRequest. Users should create new LaserEmitter records
              for non-existent emitters and update existing records for any modifications.

          num_targets: The number of targets included in this request.

          request_id: External identifier for this LaserDeconflictRequest record.

          request_ts: The datetime that this LaserDeconflictRequest record was created, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          centerline_azimuth: The azimuth angle of the centerline of the geospatial box that confines
              positions of the laser platform, in degrees.

          centerline_elevation: The elevation angle of the centerline of the geospatial box that confines the
              positions of the laser platform, in degrees.

          default_cha: The half-angle of the safety cone of the laser beam, in degrees.

          enable_dss: Boolean enabling Dynamic Satellite Susceptibility (DSS) algorithms.

          fixed_points: A collection of latitude, longitude, and altitude fields which can be used to
              specify the geometry of the coordinate space in which the laser platform(s) will
              be operational for this request. For example, a BOX_2_WAYPOINTS would include
              two data points, while a BOX_4_SURFACE_POINTS would include four data points.

          geopotential_model: Indicates the geopotential model used in the propagation calculation for this
              request (e.g. EGM-96, WGS-84, WGS-72, WGS66, WGS60, JGM-2, or GEM-T3).

          laser_deconflict_targets: A list containing all laser illumination target object specifications for which
              deconflictions must be calculated, as planned for this request.

          laser_system_name: The name of the laser/beam director system. The Laser Clearinghouse will append
              identifiers to the name using standard conventions.

          length_centerline: The length of the centerline that passes through the center point of the
              geospatial box that confines the positions of the laser platform, in kilometers.

          length_left_right: Specifies the length of the horizontal dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          length_up_down: Specifies the length of the vertical dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          maximum_height: The maximum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          minimum_height: The minimum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          mission_name: The name of the mission with which this LaserDeconflictRequest is associated.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source provider to indicate the on-orbit
              laser platform. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          platform_location_name: The name of the laser platform.

          platform_location_type: Indicates the type of location(s) the laser platform will be operational for
              this request (BOX_2_WAYPOINTS, BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE,
              EXTERNAL_EPHEMERIS, FIXED_POINT, SATELLITE).

          program_id: External identifier for the program that is responsible for this
              LaserDeconflictRequest.

          propagator: The type of propagator utilized in the deconfliction/predictive avoidance
              calculation.

          protect_list: A list of satellite/catalog numbers that should be protected from any and all
              incidence of laser illumination for the duration of this request.

          sat_no: The satellite/catalog number of the on-orbit laser platform.

          source_enabled: Boolean indicating whether error growth of the laser beam is enabled for this
              request.

          status: Status of this request (APPROVED, COMPLETE_WITH_ERRORS, COMPLETE_WITH_WARNINGS,
              FAILURE, IN_PROGRESS, REQUESTED, SUCCESS).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          target_enabled: Boolean indicating whether target error growth is enabled for this request.

          target_type: The target type that concerns this request (BOX_2_WAYPOINTS,
              BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE, EXTERNAL_EPHEMERIS, FIXED_POINT,
              SATELLITE).

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          treat_earth_as: Indicates the treatment of earth (INVISIBLE, VICTIM, SHIELD) for this
              LaserDeconflictRequest record.

          use_field_of_regard: Boolean indicating that, for deconfliction events in which the potential target
              is an optical imaging satellite, line of sight computation between target and
              source is ensured when the source emitter is contained within the field of
              regard (field of view) of the satellite's optical telescope.

          victim_enabled: Boolean indicating whether victim error growth is enabled as input to the
              deconfliction calculations for this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/laserdeconflictrequest",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_date": end_date,
                    "id_laser_emitters": id_laser_emitters,
                    "num_targets": num_targets,
                    "request_id": request_id,
                    "request_ts": request_ts,
                    "source": source,
                    "start_date": start_date,
                    "id": id,
                    "centerline_azimuth": centerline_azimuth,
                    "centerline_elevation": centerline_elevation,
                    "default_cha": default_cha,
                    "enable_dss": enable_dss,
                    "fixed_points": fixed_points,
                    "geopotential_model": geopotential_model,
                    "laser_deconflict_targets": laser_deconflict_targets,
                    "laser_system_name": laser_system_name,
                    "length_centerline": length_centerline,
                    "length_left_right": length_left_right,
                    "length_up_down": length_up_down,
                    "maximum_height": maximum_height,
                    "minimum_height": minimum_height,
                    "mission_name": mission_name,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "platform_location_name": platform_location_name,
                    "platform_location_type": platform_location_type,
                    "program_id": program_id,
                    "propagator": propagator,
                    "protect_list": protect_list,
                    "sat_no": sat_no,
                    "source_enabled": source_enabled,
                    "status": status,
                    "tags": tags,
                    "target_enabled": target_enabled,
                    "target_type": target_type,
                    "transaction_id": transaction_id,
                    "treat_earth_as": treat_earth_as,
                    "use_field_of_regard": use_field_of_regard,
                    "victim_enabled": victim_enabled,
                },
                laserdeconflictrequest_create_params.LaserdeconflictrequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        start_date: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[LaserdeconflictrequestListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/laserdeconflictrequest",
            page=SyncOffsetPage[LaserdeconflictrequestListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_date": start_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    laserdeconflictrequest_list_params.LaserdeconflictrequestListParams,
                ),
            ),
            model=LaserdeconflictrequestListResponse,
        )

    def count(
        self,
        *,
        start_date: Union[str, datetime],
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
          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/laserdeconflictrequest/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_date": start_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    laserdeconflictrequest_count_params.LaserdeconflictrequestCountParams,
                ),
            ),
            cast_to=str,
        )

    def get(
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
    ) -> LaserdeconflictrequestGetResponse:
        """
        Service operation to get a single LaserDeconflictRequest record by its unique ID
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
            f"/udl/laserdeconflictrequest/{id}",
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
                    laserdeconflictrequest_get_params.LaserdeconflictrequestGetParams,
                ),
            ),
            cast_to=LaserdeconflictrequestGetResponse,
        )

    def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LaserdeconflictrequestQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/laserdeconflictrequest/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LaserdeconflictrequestQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        start_date: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LaserdeconflictrequestTupleResponse:
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

          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/laserdeconflictrequest/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "start_date": start_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    laserdeconflictrequest_tuple_params.LaserdeconflictrequestTupleParams,
                ),
            ),
            cast_to=LaserdeconflictrequestTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_date: Union[str, datetime],
        id_laser_emitters: SequenceNotStr[str],
        num_targets: int,
        request_id: str,
        request_ts: Union[str, datetime],
        source: str,
        start_date: Union[str, datetime],
        id: str | Omit = omit,
        centerline_azimuth: float | Omit = omit,
        centerline_elevation: float | Omit = omit,
        default_cha: float | Omit = omit,
        enable_dss: bool | Omit = omit,
        fixed_points: Iterable[laserdeconflictrequest_unvalidated_publish_params.FixedPoint] | Omit = omit,
        geopotential_model: str | Omit = omit,
        laser_deconflict_targets: Iterable[laserdeconflictrequest_unvalidated_publish_params.LaserDeconflictTarget]
        | Omit = omit,
        laser_system_name: str | Omit = omit,
        length_centerline: float | Omit = omit,
        length_left_right: float | Omit = omit,
        length_up_down: float | Omit = omit,
        maximum_height: float | Omit = omit,
        minimum_height: float | Omit = omit,
        mission_name: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        platform_location_name: str | Omit = omit,
        platform_location_type: str | Omit = omit,
        program_id: str | Omit = omit,
        propagator: str | Omit = omit,
        protect_list: Iterable[int] | Omit = omit,
        sat_no: int | Omit = omit,
        source_enabled: bool | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_enabled: bool | Omit = omit,
        target_type: str | Omit = omit,
        transaction_id: str | Omit = omit,
        treat_earth_as: str | Omit = omit,
        use_field_of_regard: bool | Omit = omit,
        victim_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single LaserDeconflictRequest record as a POST body
        and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
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

          end_date: End date of the time windows associated with this LaserDeconflictRequest, in ISO
              8601 UTC format with millisecond precision.

          id_laser_emitters: A list containing the id strings of the LaserEmitter records in UDL detailing
              the physical parameters of each laser/emitter operationally involved with this
              request. All laser/emitter components must be accurately described using the
              LaserEmitter schema and ingested into the UDL LaserEmitter service before
              creating a LaserDeconflictRequest. Users should create new LaserEmitter records
              for non-existent emitters and update existing records for any modifications.

          num_targets: The number of targets included in this request.

          request_id: External identifier for this LaserDeconflictRequest record.

          request_ts: The datetime that this LaserDeconflictRequest record was created, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          centerline_azimuth: The azimuth angle of the centerline of the geospatial box that confines
              positions of the laser platform, in degrees.

          centerline_elevation: The elevation angle of the centerline of the geospatial box that confines the
              positions of the laser platform, in degrees.

          default_cha: The half-angle of the safety cone of the laser beam, in degrees.

          enable_dss: Boolean enabling Dynamic Satellite Susceptibility (DSS) algorithms.

          fixed_points: A collection of latitude, longitude, and altitude fields which can be used to
              specify the geometry of the coordinate space in which the laser platform(s) will
              be operational for this request. For example, a BOX_2_WAYPOINTS would include
              two data points, while a BOX_4_SURFACE_POINTS would include four data points.

          geopotential_model: Indicates the geopotential model used in the propagation calculation for this
              request (e.g. EGM-96, WGS-84, WGS-72, WGS66, WGS60, JGM-2, or GEM-T3).

          laser_deconflict_targets: A list containing all laser illumination target object specifications for which
              deconflictions must be calculated, as planned for this request.

          laser_system_name: The name of the laser/beam director system. The Laser Clearinghouse will append
              identifiers to the name using standard conventions.

          length_centerline: The length of the centerline that passes through the center point of the
              geospatial box that confines the positions of the laser platform, in kilometers.

          length_left_right: Specifies the length of the horizontal dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          length_up_down: Specifies the length of the vertical dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          maximum_height: The maximum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          minimum_height: The minimum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          mission_name: The name of the mission with which this LaserDeconflictRequest is associated.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source provider to indicate the on-orbit
              laser platform. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          platform_location_name: The name of the laser platform.

          platform_location_type: Indicates the type of location(s) the laser platform will be operational for
              this request (BOX_2_WAYPOINTS, BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE,
              EXTERNAL_EPHEMERIS, FIXED_POINT, SATELLITE).

          program_id: External identifier for the program that is responsible for this
              LaserDeconflictRequest.

          propagator: The type of propagator utilized in the deconfliction/predictive avoidance
              calculation.

          protect_list: A list of satellite/catalog numbers that should be protected from any and all
              incidence of laser illumination for the duration of this request.

          sat_no: The satellite/catalog number of the on-orbit laser platform.

          source_enabled: Boolean indicating whether error growth of the laser beam is enabled for this
              request.

          status: Status of this request (APPROVED, COMPLETE_WITH_ERRORS, COMPLETE_WITH_WARNINGS,
              FAILURE, IN_PROGRESS, REQUESTED, SUCCESS).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          target_enabled: Boolean indicating whether target error growth is enabled for this request.

          target_type: The target type that concerns this request (BOX_2_WAYPOINTS,
              BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE, EXTERNAL_EPHEMERIS, FIXED_POINT,
              SATELLITE).

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          treat_earth_as: Indicates the treatment of earth (INVISIBLE, VICTIM, SHIELD) for this
              LaserDeconflictRequest record.

          use_field_of_regard: Boolean indicating that, for deconfliction events in which the potential target
              is an optical imaging satellite, line of sight computation between target and
              source is ensured when the source emitter is contained within the field of
              regard (field of view) of the satellite's optical telescope.

          victim_enabled: Boolean indicating whether victim error growth is enabled as input to the
              deconfliction calculations for this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-laserdeconflictrequest",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_date": end_date,
                    "id_laser_emitters": id_laser_emitters,
                    "num_targets": num_targets,
                    "request_id": request_id,
                    "request_ts": request_ts,
                    "source": source,
                    "start_date": start_date,
                    "id": id,
                    "centerline_azimuth": centerline_azimuth,
                    "centerline_elevation": centerline_elevation,
                    "default_cha": default_cha,
                    "enable_dss": enable_dss,
                    "fixed_points": fixed_points,
                    "geopotential_model": geopotential_model,
                    "laser_deconflict_targets": laser_deconflict_targets,
                    "laser_system_name": laser_system_name,
                    "length_centerline": length_centerline,
                    "length_left_right": length_left_right,
                    "length_up_down": length_up_down,
                    "maximum_height": maximum_height,
                    "minimum_height": minimum_height,
                    "mission_name": mission_name,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "platform_location_name": platform_location_name,
                    "platform_location_type": platform_location_type,
                    "program_id": program_id,
                    "propagator": propagator,
                    "protect_list": protect_list,
                    "sat_no": sat_no,
                    "source_enabled": source_enabled,
                    "status": status,
                    "tags": tags,
                    "target_enabled": target_enabled,
                    "target_type": target_type,
                    "transaction_id": transaction_id,
                    "treat_earth_as": treat_earth_as,
                    "use_field_of_regard": use_field_of_regard,
                    "victim_enabled": victim_enabled,
                },
                laserdeconflictrequest_unvalidated_publish_params.LaserdeconflictrequestUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLaserdeconflictrequestResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLaserdeconflictrequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLaserdeconflictrequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLaserdeconflictrequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncLaserdeconflictrequestResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_date: Union[str, datetime],
        id_laser_emitters: SequenceNotStr[str],
        num_targets: int,
        request_id: str,
        request_ts: Union[str, datetime],
        source: str,
        start_date: Union[str, datetime],
        id: str | Omit = omit,
        centerline_azimuth: float | Omit = omit,
        centerline_elevation: float | Omit = omit,
        default_cha: float | Omit = omit,
        enable_dss: bool | Omit = omit,
        fixed_points: Iterable[laserdeconflictrequest_create_params.FixedPoint] | Omit = omit,
        geopotential_model: str | Omit = omit,
        laser_deconflict_targets: Iterable[laserdeconflictrequest_create_params.LaserDeconflictTarget] | Omit = omit,
        laser_system_name: str | Omit = omit,
        length_centerline: float | Omit = omit,
        length_left_right: float | Omit = omit,
        length_up_down: float | Omit = omit,
        maximum_height: float | Omit = omit,
        minimum_height: float | Omit = omit,
        mission_name: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        platform_location_name: str | Omit = omit,
        platform_location_type: str | Omit = omit,
        program_id: str | Omit = omit,
        propagator: str | Omit = omit,
        protect_list: Iterable[int] | Omit = omit,
        sat_no: int | Omit = omit,
        source_enabled: bool | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_enabled: bool | Omit = omit,
        target_type: str | Omit = omit,
        transaction_id: str | Omit = omit,
        treat_earth_as: str | Omit = omit,
        use_field_of_regard: bool | Omit = omit,
        victim_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single LaserDeconflictRequest record as a POST body
        and ingest into the database. This operation does not persist any
        LaserDeconflictTarget datatypes that may be present in the body of the request.
        This operation is not intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

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

          end_date: End date of the time windows associated with this LaserDeconflictRequest, in ISO
              8601 UTC format with millisecond precision.

          id_laser_emitters: A list containing the id strings of the LaserEmitter records in UDL detailing
              the physical parameters of each laser/emitter operationally involved with this
              request. All laser/emitter components must be accurately described using the
              LaserEmitter schema and ingested into the UDL LaserEmitter service before
              creating a LaserDeconflictRequest. Users should create new LaserEmitter records
              for non-existent emitters and update existing records for any modifications.

          num_targets: The number of targets included in this request.

          request_id: External identifier for this LaserDeconflictRequest record.

          request_ts: The datetime that this LaserDeconflictRequest record was created, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          centerline_azimuth: The azimuth angle of the centerline of the geospatial box that confines
              positions of the laser platform, in degrees.

          centerline_elevation: The elevation angle of the centerline of the geospatial box that confines the
              positions of the laser platform, in degrees.

          default_cha: The half-angle of the safety cone of the laser beam, in degrees.

          enable_dss: Boolean enabling Dynamic Satellite Susceptibility (DSS) algorithms.

          fixed_points: A collection of latitude, longitude, and altitude fields which can be used to
              specify the geometry of the coordinate space in which the laser platform(s) will
              be operational for this request. For example, a BOX_2_WAYPOINTS would include
              two data points, while a BOX_4_SURFACE_POINTS would include four data points.

          geopotential_model: Indicates the geopotential model used in the propagation calculation for this
              request (e.g. EGM-96, WGS-84, WGS-72, WGS66, WGS60, JGM-2, or GEM-T3).

          laser_deconflict_targets: A list containing all laser illumination target object specifications for which
              deconflictions must be calculated, as planned for this request.

          laser_system_name: The name of the laser/beam director system. The Laser Clearinghouse will append
              identifiers to the name using standard conventions.

          length_centerline: The length of the centerline that passes through the center point of the
              geospatial box that confines the positions of the laser platform, in kilometers.

          length_left_right: Specifies the length of the horizontal dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          length_up_down: Specifies the length of the vertical dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          maximum_height: The maximum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          minimum_height: The minimum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          mission_name: The name of the mission with which this LaserDeconflictRequest is associated.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source provider to indicate the on-orbit
              laser platform. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          platform_location_name: The name of the laser platform.

          platform_location_type: Indicates the type of location(s) the laser platform will be operational for
              this request (BOX_2_WAYPOINTS, BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE,
              EXTERNAL_EPHEMERIS, FIXED_POINT, SATELLITE).

          program_id: External identifier for the program that is responsible for this
              LaserDeconflictRequest.

          propagator: The type of propagator utilized in the deconfliction/predictive avoidance
              calculation.

          protect_list: A list of satellite/catalog numbers that should be protected from any and all
              incidence of laser illumination for the duration of this request.

          sat_no: The satellite/catalog number of the on-orbit laser platform.

          source_enabled: Boolean indicating whether error growth of the laser beam is enabled for this
              request.

          status: Status of this request (APPROVED, COMPLETE_WITH_ERRORS, COMPLETE_WITH_WARNINGS,
              FAILURE, IN_PROGRESS, REQUESTED, SUCCESS).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          target_enabled: Boolean indicating whether target error growth is enabled for this request.

          target_type: The target type that concerns this request (BOX_2_WAYPOINTS,
              BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE, EXTERNAL_EPHEMERIS, FIXED_POINT,
              SATELLITE).

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          treat_earth_as: Indicates the treatment of earth (INVISIBLE, VICTIM, SHIELD) for this
              LaserDeconflictRequest record.

          use_field_of_regard: Boolean indicating that, for deconfliction events in which the potential target
              is an optical imaging satellite, line of sight computation between target and
              source is ensured when the source emitter is contained within the field of
              regard (field of view) of the satellite's optical telescope.

          victim_enabled: Boolean indicating whether victim error growth is enabled as input to the
              deconfliction calculations for this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/laserdeconflictrequest",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_date": end_date,
                    "id_laser_emitters": id_laser_emitters,
                    "num_targets": num_targets,
                    "request_id": request_id,
                    "request_ts": request_ts,
                    "source": source,
                    "start_date": start_date,
                    "id": id,
                    "centerline_azimuth": centerline_azimuth,
                    "centerline_elevation": centerline_elevation,
                    "default_cha": default_cha,
                    "enable_dss": enable_dss,
                    "fixed_points": fixed_points,
                    "geopotential_model": geopotential_model,
                    "laser_deconflict_targets": laser_deconflict_targets,
                    "laser_system_name": laser_system_name,
                    "length_centerline": length_centerline,
                    "length_left_right": length_left_right,
                    "length_up_down": length_up_down,
                    "maximum_height": maximum_height,
                    "minimum_height": minimum_height,
                    "mission_name": mission_name,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "platform_location_name": platform_location_name,
                    "platform_location_type": platform_location_type,
                    "program_id": program_id,
                    "propagator": propagator,
                    "protect_list": protect_list,
                    "sat_no": sat_no,
                    "source_enabled": source_enabled,
                    "status": status,
                    "tags": tags,
                    "target_enabled": target_enabled,
                    "target_type": target_type,
                    "transaction_id": transaction_id,
                    "treat_earth_as": treat_earth_as,
                    "use_field_of_regard": use_field_of_regard,
                    "victim_enabled": victim_enabled,
                },
                laserdeconflictrequest_create_params.LaserdeconflictrequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        start_date: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LaserdeconflictrequestListResponse, AsyncOffsetPage[LaserdeconflictrequestListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/laserdeconflictrequest",
            page=AsyncOffsetPage[LaserdeconflictrequestListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_date": start_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    laserdeconflictrequest_list_params.LaserdeconflictrequestListParams,
                ),
            ),
            model=LaserdeconflictrequestListResponse,
        )

    async def count(
        self,
        *,
        start_date: Union[str, datetime],
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
          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/laserdeconflictrequest/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_date": start_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    laserdeconflictrequest_count_params.LaserdeconflictrequestCountParams,
                ),
            ),
            cast_to=str,
        )

    async def get(
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
    ) -> LaserdeconflictrequestGetResponse:
        """
        Service operation to get a single LaserDeconflictRequest record by its unique ID
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
            f"/udl/laserdeconflictrequest/{id}",
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
                    laserdeconflictrequest_get_params.LaserdeconflictrequestGetParams,
                ),
            ),
            cast_to=LaserdeconflictrequestGetResponse,
        )

    async def queryhelp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LaserdeconflictrequestQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/laserdeconflictrequest/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LaserdeconflictrequestQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        start_date: Union[str, datetime],
        first_result: int | Omit = omit,
        max_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LaserdeconflictrequestTupleResponse:
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

          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision. (YYYY-MM-DDTHH:MM:SS.sssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/laserdeconflictrequest/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "start_date": start_date,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    laserdeconflictrequest_tuple_params.LaserdeconflictrequestTupleParams,
                ),
            ),
            cast_to=LaserdeconflictrequestTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_date: Union[str, datetime],
        id_laser_emitters: SequenceNotStr[str],
        num_targets: int,
        request_id: str,
        request_ts: Union[str, datetime],
        source: str,
        start_date: Union[str, datetime],
        id: str | Omit = omit,
        centerline_azimuth: float | Omit = omit,
        centerline_elevation: float | Omit = omit,
        default_cha: float | Omit = omit,
        enable_dss: bool | Omit = omit,
        fixed_points: Iterable[laserdeconflictrequest_unvalidated_publish_params.FixedPoint] | Omit = omit,
        geopotential_model: str | Omit = omit,
        laser_deconflict_targets: Iterable[laserdeconflictrequest_unvalidated_publish_params.LaserDeconflictTarget]
        | Omit = omit,
        laser_system_name: str | Omit = omit,
        length_centerline: float | Omit = omit,
        length_left_right: float | Omit = omit,
        length_up_down: float | Omit = omit,
        maximum_height: float | Omit = omit,
        minimum_height: float | Omit = omit,
        mission_name: str | Omit = omit,
        origin: str | Omit = omit,
        orig_object_id: str | Omit = omit,
        platform_location_name: str | Omit = omit,
        platform_location_type: str | Omit = omit,
        program_id: str | Omit = omit,
        propagator: str | Omit = omit,
        protect_list: Iterable[int] | Omit = omit,
        sat_no: int | Omit = omit,
        source_enabled: bool | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_enabled: bool | Omit = omit,
        target_type: str | Omit = omit,
        transaction_id: str | Omit = omit,
        treat_earth_as: str | Omit = omit,
        use_field_of_regard: bool | Omit = omit,
        victim_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Service operation to take a single LaserDeconflictRequest record as a POST body
        and ingest into the database. This operation is intended to be used for
        automated feeds into UDL. A specific role is required to perform this service
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

          end_date: End date of the time windows associated with this LaserDeconflictRequest, in ISO
              8601 UTC format with millisecond precision.

          id_laser_emitters: A list containing the id strings of the LaserEmitter records in UDL detailing
              the physical parameters of each laser/emitter operationally involved with this
              request. All laser/emitter components must be accurately described using the
              LaserEmitter schema and ingested into the UDL LaserEmitter service before
              creating a LaserDeconflictRequest. Users should create new LaserEmitter records
              for non-existent emitters and update existing records for any modifications.

          num_targets: The number of targets included in this request.

          request_id: External identifier for this LaserDeconflictRequest record.

          request_ts: The datetime that this LaserDeconflictRequest record was created, in ISO 8601
              UTC format with millisecond precision.

          source: Source of the data.

          start_date: Start date of the time windows associated with this LaserDeconflictRequest, in
              ISO 8601 UTC format with millisecond precision.

          id: Unique identifier of the record, auto-generated by the system if not provided on
              create operations.

          centerline_azimuth: The azimuth angle of the centerline of the geospatial box that confines
              positions of the laser platform, in degrees.

          centerline_elevation: The elevation angle of the centerline of the geospatial box that confines the
              positions of the laser platform, in degrees.

          default_cha: The half-angle of the safety cone of the laser beam, in degrees.

          enable_dss: Boolean enabling Dynamic Satellite Susceptibility (DSS) algorithms.

          fixed_points: A collection of latitude, longitude, and altitude fields which can be used to
              specify the geometry of the coordinate space in which the laser platform(s) will
              be operational for this request. For example, a BOX_2_WAYPOINTS would include
              two data points, while a BOX_4_SURFACE_POINTS would include four data points.

          geopotential_model: Indicates the geopotential model used in the propagation calculation for this
              request (e.g. EGM-96, WGS-84, WGS-72, WGS66, WGS60, JGM-2, or GEM-T3).

          laser_deconflict_targets: A list containing all laser illumination target object specifications for which
              deconflictions must be calculated, as planned for this request.

          laser_system_name: The name of the laser/beam director system. The Laser Clearinghouse will append
              identifiers to the name using standard conventions.

          length_centerline: The length of the centerline that passes through the center point of the
              geospatial box that confines the positions of the laser platform, in kilometers.

          length_left_right: Specifies the length of the horizontal dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          length_up_down: Specifies the length of the vertical dimension of the geospatial box that
              confines the positions of the laser platform, in kilometers.

          maximum_height: The maximum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          minimum_height: The minimum laser operating altitude specified as the height above/below the
              WGS84 ellipsoid where the laser is omitted from, in kilometers.

          mission_name: The name of the mission with which this LaserDeconflictRequest is associated.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the source provider to indicate the on-orbit
              laser platform. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          platform_location_name: The name of the laser platform.

          platform_location_type: Indicates the type of location(s) the laser platform will be operational for
              this request (BOX_2_WAYPOINTS, BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE,
              EXTERNAL_EPHEMERIS, FIXED_POINT, SATELLITE).

          program_id: External identifier for the program that is responsible for this
              LaserDeconflictRequest.

          propagator: The type of propagator utilized in the deconfliction/predictive avoidance
              calculation.

          protect_list: A list of satellite/catalog numbers that should be protected from any and all
              incidence of laser illumination for the duration of this request.

          sat_no: The satellite/catalog number of the on-orbit laser platform.

          source_enabled: Boolean indicating whether error growth of the laser beam is enabled for this
              request.

          status: Status of this request (APPROVED, COMPLETE_WITH_ERRORS, COMPLETE_WITH_WARNINGS,
              FAILURE, IN_PROGRESS, REQUESTED, SUCCESS).

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          target_enabled: Boolean indicating whether target error growth is enabled for this request.

          target_type: The target type that concerns this request (BOX_2_WAYPOINTS,
              BOX_4_SURFACE_POINTS, BOX_CENTER_POINT_LINE, EXTERNAL_EPHEMERIS, FIXED_POINT,
              SATELLITE).

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          treat_earth_as: Indicates the treatment of earth (INVISIBLE, VICTIM, SHIELD) for this
              LaserDeconflictRequest record.

          use_field_of_regard: Boolean indicating that, for deconfliction events in which the potential target
              is an optical imaging satellite, line of sight computation between target and
              source is ensured when the source emitter is contained within the field of
              regard (field of view) of the satellite's optical telescope.

          victim_enabled: Boolean indicating whether victim error growth is enabled as input to the
              deconfliction calculations for this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-laserdeconflictrequest",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_date": end_date,
                    "id_laser_emitters": id_laser_emitters,
                    "num_targets": num_targets,
                    "request_id": request_id,
                    "request_ts": request_ts,
                    "source": source,
                    "start_date": start_date,
                    "id": id,
                    "centerline_azimuth": centerline_azimuth,
                    "centerline_elevation": centerline_elevation,
                    "default_cha": default_cha,
                    "enable_dss": enable_dss,
                    "fixed_points": fixed_points,
                    "geopotential_model": geopotential_model,
                    "laser_deconflict_targets": laser_deconflict_targets,
                    "laser_system_name": laser_system_name,
                    "length_centerline": length_centerline,
                    "length_left_right": length_left_right,
                    "length_up_down": length_up_down,
                    "maximum_height": maximum_height,
                    "minimum_height": minimum_height,
                    "mission_name": mission_name,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "platform_location_name": platform_location_name,
                    "platform_location_type": platform_location_type,
                    "program_id": program_id,
                    "propagator": propagator,
                    "protect_list": protect_list,
                    "sat_no": sat_no,
                    "source_enabled": source_enabled,
                    "status": status,
                    "tags": tags,
                    "target_enabled": target_enabled,
                    "target_type": target_type,
                    "transaction_id": transaction_id,
                    "treat_earth_as": treat_earth_as,
                    "use_field_of_regard": use_field_of_regard,
                    "victim_enabled": victim_enabled,
                },
                laserdeconflictrequest_unvalidated_publish_params.LaserdeconflictrequestUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LaserdeconflictrequestResourceWithRawResponse:
    def __init__(self, laserdeconflictrequest: LaserdeconflictrequestResource) -> None:
        self._laserdeconflictrequest = laserdeconflictrequest

        self.create = to_raw_response_wrapper(
            laserdeconflictrequest.create,
        )
        self.list = to_raw_response_wrapper(
            laserdeconflictrequest.list,
        )
        self.count = to_raw_response_wrapper(
            laserdeconflictrequest.count,
        )
        self.get = to_raw_response_wrapper(
            laserdeconflictrequest.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            laserdeconflictrequest.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            laserdeconflictrequest.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            laserdeconflictrequest.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._laserdeconflictrequest.history)


class AsyncLaserdeconflictrequestResourceWithRawResponse:
    def __init__(self, laserdeconflictrequest: AsyncLaserdeconflictrequestResource) -> None:
        self._laserdeconflictrequest = laserdeconflictrequest

        self.create = async_to_raw_response_wrapper(
            laserdeconflictrequest.create,
        )
        self.list = async_to_raw_response_wrapper(
            laserdeconflictrequest.list,
        )
        self.count = async_to_raw_response_wrapper(
            laserdeconflictrequest.count,
        )
        self.get = async_to_raw_response_wrapper(
            laserdeconflictrequest.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            laserdeconflictrequest.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            laserdeconflictrequest.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            laserdeconflictrequest.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._laserdeconflictrequest.history)


class LaserdeconflictrequestResourceWithStreamingResponse:
    def __init__(self, laserdeconflictrequest: LaserdeconflictrequestResource) -> None:
        self._laserdeconflictrequest = laserdeconflictrequest

        self.create = to_streamed_response_wrapper(
            laserdeconflictrequest.create,
        )
        self.list = to_streamed_response_wrapper(
            laserdeconflictrequest.list,
        )
        self.count = to_streamed_response_wrapper(
            laserdeconflictrequest.count,
        )
        self.get = to_streamed_response_wrapper(
            laserdeconflictrequest.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            laserdeconflictrequest.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            laserdeconflictrequest.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            laserdeconflictrequest.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._laserdeconflictrequest.history)


class AsyncLaserdeconflictrequestResourceWithStreamingResponse:
    def __init__(self, laserdeconflictrequest: AsyncLaserdeconflictrequestResource) -> None:
        self._laserdeconflictrequest = laserdeconflictrequest

        self.create = async_to_streamed_response_wrapper(
            laserdeconflictrequest.create,
        )
        self.list = async_to_streamed_response_wrapper(
            laserdeconflictrequest.list,
        )
        self.count = async_to_streamed_response_wrapper(
            laserdeconflictrequest.count,
        )
        self.get = async_to_streamed_response_wrapper(
            laserdeconflictrequest.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            laserdeconflictrequest.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            laserdeconflictrequest.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            laserdeconflictrequest.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._laserdeconflictrequest.history)
