# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    conjunction_list_params,
    conjunction_count_params,
    conjunction_tuple_params,
    conjunction_retrieve_params,
    conjunction_create_udl_params,
    conjunction_create_bulk_params,
    conjunction_get_history_params,
    conjunction_unvalidated_publish_params,
    conjunction_upload_conjunction_data_message_params,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
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
from ...types.conjunction_full import ConjunctionFull
from ...types.conjunction_abridged import ConjunctionAbridged
from ...types.conjunction_tuple_response import ConjunctionTupleResponse
from ...types.conjunction_get_history_response import ConjunctionGetHistoryResponse

__all__ = ["ConjunctionsResource", "AsyncConjunctionsResource"]


class ConjunctionsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConjunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConjunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConjunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ConjunctionsResourceWithStreamingResponse(self)

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
    ) -> ConjunctionFull:
        """
        Service operation to get a single conjunction by its unique ID passed as a path
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
            f"/udl/conjunction/{id}",
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
                    conjunction_retrieve_params.ConjunctionRetrieveParams,
                ),
            ),
            cast_to=ConjunctionFull,
        )

    def list(
        self,
        *,
        tca: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[ConjunctionAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/conjunction",
            page=SyncOffsetPage[ConjunctionAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tca": tca,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_list_params.ConjunctionListParams,
                ),
            ),
            model=ConjunctionAbridged,
        )

    def count(
        self,
        *,
        tca: Union[str, datetime],
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
          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/conjunction/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tca": tca,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_count_params.ConjunctionCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_udl(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        tca: Union[str, datetime],
        convert_pos_vel: bool | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        ccir: str | NotGiven = NOT_GIVEN,
        cd_ao_m1: float | NotGiven = NOT_GIVEN,
        cd_ao_m2: float | NotGiven = NOT_GIVEN,
        collision_prob: float | NotGiven = NOT_GIVEN,
        collision_prob_method: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        concern_notes: str | NotGiven = NOT_GIVEN,
        cr_ao_m1: float | NotGiven = NOT_GIVEN,
        cr_ao_m2: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        ephem_name1: str | NotGiven = NOT_GIVEN,
        ephem_name2: str | NotGiven = NOT_GIVEN,
        es_id1: str | NotGiven = NOT_GIVEN,
        es_id2: str | NotGiven = NOT_GIVEN,
        event_id: str | NotGiven = NOT_GIVEN,
        id_state_vector1: str | NotGiven = NOT_GIVEN,
        id_state_vector2: str | NotGiven = NOT_GIVEN,
        large_cov_warning: bool | NotGiven = NOT_GIVEN,
        large_rel_pos_warning: bool | NotGiven = NOT_GIVEN,
        last_ob_time1: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_ob_time2: Union[str, datetime] | NotGiven = NOT_GIVEN,
        message_for: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        miss_distance: float | NotGiven = NOT_GIVEN,
        orig_id_on_orbit1: str | NotGiven = NOT_GIVEN,
        orig_id_on_orbit2: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        originator: str | NotGiven = NOT_GIVEN,
        owner_contacted: bool | NotGiven = NOT_GIVEN,
        penetration_level_sigma: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rel_pos_n: float | NotGiven = NOT_GIVEN,
        rel_pos_r: float | NotGiven = NOT_GIVEN,
        rel_pos_t: float | NotGiven = NOT_GIVEN,
        rel_vel_mag: float | NotGiven = NOT_GIVEN,
        rel_vel_n: float | NotGiven = NOT_GIVEN,
        rel_vel_r: float | NotGiven = NOT_GIVEN,
        rel_vel_t: float | NotGiven = NOT_GIVEN,
        sat_no1: int | NotGiven = NOT_GIVEN,
        sat_no2: int | NotGiven = NOT_GIVEN,
        screen_entry_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        screen_exit_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        screen_volume_x: float | NotGiven = NOT_GIVEN,
        screen_volume_y: float | NotGiven = NOT_GIVEN,
        screen_volume_z: float | NotGiven = NOT_GIVEN,
        small_cov_warning: bool | NotGiven = NOT_GIVEN,
        small_rel_vel_warning: bool | NotGiven = NOT_GIVEN,
        state_dept_notified: bool | NotGiven = NOT_GIVEN,
        state_vector1: conjunction_create_udl_params.StateVector1 | NotGiven = NOT_GIVEN,
        state_vector2: conjunction_create_udl_params.StateVector2 | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        thrust_accel1: float | NotGiven = NOT_GIVEN,
        thrust_accel2: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        uvw_warn: bool | NotGiven = NOT_GIVEN,
        vol_entry_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        vol_exit_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        vol_shape: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Conjunction as a POST body and ingest into
        the database. A Conjunction is analysis of probability of collision; the data
        can include state vectors for primary and secondary satellites. A specific role
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

          tca: Time of closest approach (TCA) in UTC.

          convert_pos_vel: Flag to convert Conjunction PosVels into J2000 reference frame.

          id: Unique identifier of the record, auto-generated by the system.

          ccir: Commander's critical information requirements notes.

          cd_ao_m1: The value of the primary (object1) Area times the drag coefficient over the
              object Mass, expressed in m^2/kg, used for propagation of the primary state
              vector and covariance to TCA.

          cd_ao_m2: The value of the secondary (object2) Area times the drag coefficient over the
              object Mass, expressed in m^2/kg, used for propagation of the primary state
              vector and covariance to TCA.

          collision_prob: Probability of Collision is the probability (denoted p, where 0.0<=p<=1.0), that
              Object1 and Object2 will collide.

          collision_prob_method: The method that was used to calculate the collision probability, ex.
              FOSTER-1992.

          comments: Additional notes from data providers.

          concern_notes: Emergency comments.

          cr_ao_m1: The value of the primary (object1) Area times the solar radiation pressure
              coefficient over the object Mass, expressed in m^2/kg, used for propagation of
              the primary state vector and covariance to TCA. This parameter is sometimes
              referred to as AGOM.

          cr_ao_m2: The value of the secondary (object2) Area times the solar radiation pressure
              coefficient over the object Mass, expressed in m^2/kg, used for propagation of
              the primary state vector and covariance to TCA. This parameter is sometimes
              referred to as AGOM.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          ephem_name1: The filename of the primary (object1) ephemeris used in the screening, if
              applicable.

          ephem_name2: The filename of the secondary (object2) ephemeris used in the screening, if
              applicable.

          es_id1: Unique identifier of the parent Ephemeris Set of the primary (object1) ephemeris
              used in the screening, if applicable.

          es_id2: Unique identifier of the parent Ephemeris Set of the secondary (object2)
              ephemeris used in the screening, if applicable.

          event_id: Optional source-provided identifier for this conjunction event. In the case
              where multiple conjunction records are submitted for the same event, this field
              can be used to tie them together to the same event.

          id_state_vector1: Optional ID of the UDL State Vector at TCA of the primary object. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the stateVector1.

          id_state_vector2: Optional ID of the UDL State Vector at TCA of the secondary object. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the stateVector2.

          large_cov_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          large_rel_pos_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          last_ob_time1: Time of last positive metric observation of the primary satellite.

          last_ob_time2: Time of last positive metric observation of the secondary satellite.

          message_for: Spacecraft name(s) for which the Collision message is provided.

          message_id: JMS provided message ID link.

          miss_distance: Distance between objects at Time of Closest Approach (TCA) in meters.

          orig_id_on_orbit1: Optional place holder for an OnOrbit ID that does not exist in UDL.

          orig_id_on_orbit2: Optional place holder for an OnOrbit ID that does not exist in UDL.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          originator: Creating agency or owner/operator (may be different than provider who submitted
              the conjunction message).

          owner_contacted: Flag indicating if owner was contacted.

          penetration_level_sigma: Penetration Level Sigma.

          raw_file_uri: Link to filename associated with JMS record.

          rel_pos_n: Distance between objects along Normal vector in meters.

          rel_pos_r: Distance between objects along Radial Vector at Time of Closest Approach in
              meters.

          rel_pos_t: Distance between objects along Tangential Vector in meters.

          rel_vel_mag: Closing velocity magnitude (relative speed) at Time of Closest Approach in
              meters/sec.

          rel_vel_n: Closing velocity between objects along Normal Vector in meters/sec.

          rel_vel_r: Closing velocity between objects along Radial Vector at Time of Closest Approach
              in meters/sec.

          rel_vel_t: Closing velocity between objects along Tangential Vector in meters/sec.

          sat_no1: Satellite/catalog number of the target on-orbit primary object.

          sat_no2: Satellite/catalog number of the target on-orbit secondary object.

          screen_entry_time: The start time in UTC of the screening period for the conjunction assessment.

          screen_exit_time: The stop time in UTC of the screening period for the conjunction assessment.

          screen_volume_x: Component size of screen in X component of RTN (Radial, Transverse and Normal)
              frame in meters.

          screen_volume_y: Component size of screen in Y component of RTN (Radial, Transverse and Normal)
              frame in meters.

          screen_volume_z: Component size of screen in Z component of RTN (Radial, Transverse and Normal)
              frame in meters.

          small_cov_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          small_rel_vel_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          state_dept_notified: Flag indicating if State department was notified.

          state_vector1: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          state_vector2: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          thrust_accel1: The primary (object1) acceleration, expressed in m/s^2, due to in-track thrust
              used to propagate the primary state vector and covariance to TCA.

          thrust_accel2: The secondary (object2) acceleration, expressed in m/s^2, due to in-track thrust
              used to propagate the primary state vector and covariance to TCA.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of data represented in this conjunction record (e.g. CONJUNCTION,
              CARA-WORKLIST, etc.). If type is null the record is assumed to be a Conjunction.

          uvw_warn: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          vol_entry_time: The time at which the secondary (object2) enters the screening volume, in ISO
              8601 UTC format with microsecond precision.

          vol_exit_time: The time at which the secondary (object2) exits the screening volume, in ISO
              8601 UTC format with microsecond precision.

          vol_shape: The shape (BOX, ELLIPSOID) of the screening volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/conjunction",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "tca": tca,
                    "id": id,
                    "ccir": ccir,
                    "cd_ao_m1": cd_ao_m1,
                    "cd_ao_m2": cd_ao_m2,
                    "collision_prob": collision_prob,
                    "collision_prob_method": collision_prob_method,
                    "comments": comments,
                    "concern_notes": concern_notes,
                    "cr_ao_m1": cr_ao_m1,
                    "cr_ao_m2": cr_ao_m2,
                    "descriptor": descriptor,
                    "ephem_name1": ephem_name1,
                    "ephem_name2": ephem_name2,
                    "es_id1": es_id1,
                    "es_id2": es_id2,
                    "event_id": event_id,
                    "id_state_vector1": id_state_vector1,
                    "id_state_vector2": id_state_vector2,
                    "large_cov_warning": large_cov_warning,
                    "large_rel_pos_warning": large_rel_pos_warning,
                    "last_ob_time1": last_ob_time1,
                    "last_ob_time2": last_ob_time2,
                    "message_for": message_for,
                    "message_id": message_id,
                    "miss_distance": miss_distance,
                    "orig_id_on_orbit1": orig_id_on_orbit1,
                    "orig_id_on_orbit2": orig_id_on_orbit2,
                    "origin": origin,
                    "originator": originator,
                    "owner_contacted": owner_contacted,
                    "penetration_level_sigma": penetration_level_sigma,
                    "raw_file_uri": raw_file_uri,
                    "rel_pos_n": rel_pos_n,
                    "rel_pos_r": rel_pos_r,
                    "rel_pos_t": rel_pos_t,
                    "rel_vel_mag": rel_vel_mag,
                    "rel_vel_n": rel_vel_n,
                    "rel_vel_r": rel_vel_r,
                    "rel_vel_t": rel_vel_t,
                    "sat_no1": sat_no1,
                    "sat_no2": sat_no2,
                    "screen_entry_time": screen_entry_time,
                    "screen_exit_time": screen_exit_time,
                    "screen_volume_x": screen_volume_x,
                    "screen_volume_y": screen_volume_y,
                    "screen_volume_z": screen_volume_z,
                    "small_cov_warning": small_cov_warning,
                    "small_rel_vel_warning": small_rel_vel_warning,
                    "state_dept_notified": state_dept_notified,
                    "state_vector1": state_vector1,
                    "state_vector2": state_vector2,
                    "tags": tags,
                    "thrust_accel1": thrust_accel1,
                    "thrust_accel2": thrust_accel2,
                    "transaction_id": transaction_id,
                    "type": type,
                    "uvw_warn": uvw_warn,
                    "vol_entry_time": vol_entry_time,
                    "vol_exit_time": vol_exit_time,
                    "vol_shape": vol_shape,
                },
                conjunction_create_udl_params.ConjunctionCreateUdlParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"convert_pos_vel": convert_pos_vel}, conjunction_create_udl_params.ConjunctionCreateUdlParams
                ),
            ),
            cast_to=NoneType,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[conjunction_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Conjunctions as a POST body and ingest into the database. A Conjunction is
        analysis of probability of collision; the data can include state vectors for
        primary and secondary satellites. This operation is not intended to be used for
        automated feeds into UDL. Data providers should contact the UDL team for
        specific role assignments and for instructions on setting up a permanent feed
        through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/conjunction/createBulk",
            body=maybe_transform(body, Iterable[conjunction_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_history(
        self,
        *,
        tca: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConjunctionGetHistoryResponse:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/conjunction/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tca": tca,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_get_history_params.ConjunctionGetHistoryParams,
                ),
            ),
            cast_to=ConjunctionGetHistoryResponse,
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
            "/udl/conjunction/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        tca: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConjunctionTupleResponse:
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

          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/conjunction/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "tca": tca,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_tuple_params.ConjunctionTupleParams,
                ),
            ),
            cast_to=ConjunctionTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[conjunction_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Conjunctions as a POST body and ingest into
        the database. A Conjunction is analysis of probability of collision; the data
        can include state vectors for primary and secondary satellites. This operation
        is intended to be used for automated feeds into UDL. A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-conjunction",
            body=maybe_transform(body, Iterable[conjunction_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upload_conjunction_data_message(
        self,
        *,
        classification: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        filename: str,
        source: str,
        body: FileTypes,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service to accept multiple CDMs in as zip file or a single CDM as payload.

        The
        service converts key-value pair formatted CDMs to UDL formats and stores them.
        The CDM format is as described in https://ccsds.org document CCSDS 508.0-B-1. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        **Example:**
        /filedrop/cdms?filename=conj.zip&classification=U&dataMode=TEST&source=Bluestaq&tags=tag1,tag2

        Args:
          classification: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          filename: Filename of the payload.

          source: Source of the data.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/cdms",
            body=maybe_transform(
                body, conjunction_upload_conjunction_data_message_params.ConjunctionUploadConjunctionDataMessageParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "classification": classification,
                        "data_mode": data_mode,
                        "filename": filename,
                        "source": source,
                        "tags": tags,
                    },
                    conjunction_upload_conjunction_data_message_params.ConjunctionUploadConjunctionDataMessageParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncConjunctionsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConjunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConjunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConjunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncConjunctionsResourceWithStreamingResponse(self)

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
    ) -> ConjunctionFull:
        """
        Service operation to get a single conjunction by its unique ID passed as a path
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
            f"/udl/conjunction/{id}",
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
                    conjunction_retrieve_params.ConjunctionRetrieveParams,
                ),
            ),
            cast_to=ConjunctionFull,
        )

    def list(
        self,
        *,
        tca: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ConjunctionAbridged, AsyncOffsetPage[ConjunctionAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/conjunction",
            page=AsyncOffsetPage[ConjunctionAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tca": tca,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_list_params.ConjunctionListParams,
                ),
            ),
            model=ConjunctionAbridged,
        )

    async def count(
        self,
        *,
        tca: Union[str, datetime],
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
          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/conjunction/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tca": tca,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_count_params.ConjunctionCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_udl(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        tca: Union[str, datetime],
        convert_pos_vel: bool | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        ccir: str | NotGiven = NOT_GIVEN,
        cd_ao_m1: float | NotGiven = NOT_GIVEN,
        cd_ao_m2: float | NotGiven = NOT_GIVEN,
        collision_prob: float | NotGiven = NOT_GIVEN,
        collision_prob_method: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        concern_notes: str | NotGiven = NOT_GIVEN,
        cr_ao_m1: float | NotGiven = NOT_GIVEN,
        cr_ao_m2: float | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        ephem_name1: str | NotGiven = NOT_GIVEN,
        ephem_name2: str | NotGiven = NOT_GIVEN,
        es_id1: str | NotGiven = NOT_GIVEN,
        es_id2: str | NotGiven = NOT_GIVEN,
        event_id: str | NotGiven = NOT_GIVEN,
        id_state_vector1: str | NotGiven = NOT_GIVEN,
        id_state_vector2: str | NotGiven = NOT_GIVEN,
        large_cov_warning: bool | NotGiven = NOT_GIVEN,
        large_rel_pos_warning: bool | NotGiven = NOT_GIVEN,
        last_ob_time1: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_ob_time2: Union[str, datetime] | NotGiven = NOT_GIVEN,
        message_for: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        miss_distance: float | NotGiven = NOT_GIVEN,
        orig_id_on_orbit1: str | NotGiven = NOT_GIVEN,
        orig_id_on_orbit2: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        originator: str | NotGiven = NOT_GIVEN,
        owner_contacted: bool | NotGiven = NOT_GIVEN,
        penetration_level_sigma: float | NotGiven = NOT_GIVEN,
        raw_file_uri: str | NotGiven = NOT_GIVEN,
        rel_pos_n: float | NotGiven = NOT_GIVEN,
        rel_pos_r: float | NotGiven = NOT_GIVEN,
        rel_pos_t: float | NotGiven = NOT_GIVEN,
        rel_vel_mag: float | NotGiven = NOT_GIVEN,
        rel_vel_n: float | NotGiven = NOT_GIVEN,
        rel_vel_r: float | NotGiven = NOT_GIVEN,
        rel_vel_t: float | NotGiven = NOT_GIVEN,
        sat_no1: int | NotGiven = NOT_GIVEN,
        sat_no2: int | NotGiven = NOT_GIVEN,
        screen_entry_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        screen_exit_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        screen_volume_x: float | NotGiven = NOT_GIVEN,
        screen_volume_y: float | NotGiven = NOT_GIVEN,
        screen_volume_z: float | NotGiven = NOT_GIVEN,
        small_cov_warning: bool | NotGiven = NOT_GIVEN,
        small_rel_vel_warning: bool | NotGiven = NOT_GIVEN,
        state_dept_notified: bool | NotGiven = NOT_GIVEN,
        state_vector1: conjunction_create_udl_params.StateVector1 | NotGiven = NOT_GIVEN,
        state_vector2: conjunction_create_udl_params.StateVector2 | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        thrust_accel1: float | NotGiven = NOT_GIVEN,
        thrust_accel2: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        uvw_warn: bool | NotGiven = NOT_GIVEN,
        vol_entry_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        vol_exit_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        vol_shape: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Conjunction as a POST body and ingest into
        the database. A Conjunction is analysis of probability of collision; the data
        can include state vectors for primary and secondary satellites. A specific role
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

          tca: Time of closest approach (TCA) in UTC.

          convert_pos_vel: Flag to convert Conjunction PosVels into J2000 reference frame.

          id: Unique identifier of the record, auto-generated by the system.

          ccir: Commander's critical information requirements notes.

          cd_ao_m1: The value of the primary (object1) Area times the drag coefficient over the
              object Mass, expressed in m^2/kg, used for propagation of the primary state
              vector and covariance to TCA.

          cd_ao_m2: The value of the secondary (object2) Area times the drag coefficient over the
              object Mass, expressed in m^2/kg, used for propagation of the primary state
              vector and covariance to TCA.

          collision_prob: Probability of Collision is the probability (denoted p, where 0.0<=p<=1.0), that
              Object1 and Object2 will collide.

          collision_prob_method: The method that was used to calculate the collision probability, ex.
              FOSTER-1992.

          comments: Additional notes from data providers.

          concern_notes: Emergency comments.

          cr_ao_m1: The value of the primary (object1) Area times the solar radiation pressure
              coefficient over the object Mass, expressed in m^2/kg, used for propagation of
              the primary state vector and covariance to TCA. This parameter is sometimes
              referred to as AGOM.

          cr_ao_m2: The value of the secondary (object2) Area times the solar radiation pressure
              coefficient over the object Mass, expressed in m^2/kg, used for propagation of
              the primary state vector and covariance to TCA. This parameter is sometimes
              referred to as AGOM.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          ephem_name1: The filename of the primary (object1) ephemeris used in the screening, if
              applicable.

          ephem_name2: The filename of the secondary (object2) ephemeris used in the screening, if
              applicable.

          es_id1: Unique identifier of the parent Ephemeris Set of the primary (object1) ephemeris
              used in the screening, if applicable.

          es_id2: Unique identifier of the parent Ephemeris Set of the secondary (object2)
              ephemeris used in the screening, if applicable.

          event_id: Optional source-provided identifier for this conjunction event. In the case
              where multiple conjunction records are submitted for the same event, this field
              can be used to tie them together to the same event.

          id_state_vector1: Optional ID of the UDL State Vector at TCA of the primary object. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the stateVector1.

          id_state_vector2: Optional ID of the UDL State Vector at TCA of the secondary object. When
              performing a create, this id will be ignored in favor of the UDL generated id of
              the stateVector2.

          large_cov_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          large_rel_pos_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          last_ob_time1: Time of last positive metric observation of the primary satellite.

          last_ob_time2: Time of last positive metric observation of the secondary satellite.

          message_for: Spacecraft name(s) for which the Collision message is provided.

          message_id: JMS provided message ID link.

          miss_distance: Distance between objects at Time of Closest Approach (TCA) in meters.

          orig_id_on_orbit1: Optional place holder for an OnOrbit ID that does not exist in UDL.

          orig_id_on_orbit2: Optional place holder for an OnOrbit ID that does not exist in UDL.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          originator: Creating agency or owner/operator (may be different than provider who submitted
              the conjunction message).

          owner_contacted: Flag indicating if owner was contacted.

          penetration_level_sigma: Penetration Level Sigma.

          raw_file_uri: Link to filename associated with JMS record.

          rel_pos_n: Distance between objects along Normal vector in meters.

          rel_pos_r: Distance between objects along Radial Vector at Time of Closest Approach in
              meters.

          rel_pos_t: Distance between objects along Tangential Vector in meters.

          rel_vel_mag: Closing velocity magnitude (relative speed) at Time of Closest Approach in
              meters/sec.

          rel_vel_n: Closing velocity between objects along Normal Vector in meters/sec.

          rel_vel_r: Closing velocity between objects along Radial Vector at Time of Closest Approach
              in meters/sec.

          rel_vel_t: Closing velocity between objects along Tangential Vector in meters/sec.

          sat_no1: Satellite/catalog number of the target on-orbit primary object.

          sat_no2: Satellite/catalog number of the target on-orbit secondary object.

          screen_entry_time: The start time in UTC of the screening period for the conjunction assessment.

          screen_exit_time: The stop time in UTC of the screening period for the conjunction assessment.

          screen_volume_x: Component size of screen in X component of RTN (Radial, Transverse and Normal)
              frame in meters.

          screen_volume_y: Component size of screen in Y component of RTN (Radial, Transverse and Normal)
              frame in meters.

          screen_volume_z: Component size of screen in Z component of RTN (Radial, Transverse and Normal)
              frame in meters.

          small_cov_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          small_rel_vel_warning: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          state_dept_notified: Flag indicating if State department was notified.

          state_vector1: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          state_vector2: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          thrust_accel1: The primary (object1) acceleration, expressed in m/s^2, due to in-track thrust
              used to propagate the primary state vector and covariance to TCA.

          thrust_accel2: The secondary (object2) acceleration, expressed in m/s^2, due to in-track thrust
              used to propagate the primary state vector and covariance to TCA.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          type: The type of data represented in this conjunction record (e.g. CONJUNCTION,
              CARA-WORKLIST, etc.). If type is null the record is assumed to be a Conjunction.

          uvw_warn: Used for probability of collision calculation, not Warning/Alert Threshold
              notifications.

          vol_entry_time: The time at which the secondary (object2) enters the screening volume, in ISO
              8601 UTC format with microsecond precision.

          vol_exit_time: The time at which the secondary (object2) exits the screening volume, in ISO
              8601 UTC format with microsecond precision.

          vol_shape: The shape (BOX, ELLIPSOID) of the screening volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/conjunction",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "tca": tca,
                    "id": id,
                    "ccir": ccir,
                    "cd_ao_m1": cd_ao_m1,
                    "cd_ao_m2": cd_ao_m2,
                    "collision_prob": collision_prob,
                    "collision_prob_method": collision_prob_method,
                    "comments": comments,
                    "concern_notes": concern_notes,
                    "cr_ao_m1": cr_ao_m1,
                    "cr_ao_m2": cr_ao_m2,
                    "descriptor": descriptor,
                    "ephem_name1": ephem_name1,
                    "ephem_name2": ephem_name2,
                    "es_id1": es_id1,
                    "es_id2": es_id2,
                    "event_id": event_id,
                    "id_state_vector1": id_state_vector1,
                    "id_state_vector2": id_state_vector2,
                    "large_cov_warning": large_cov_warning,
                    "large_rel_pos_warning": large_rel_pos_warning,
                    "last_ob_time1": last_ob_time1,
                    "last_ob_time2": last_ob_time2,
                    "message_for": message_for,
                    "message_id": message_id,
                    "miss_distance": miss_distance,
                    "orig_id_on_orbit1": orig_id_on_orbit1,
                    "orig_id_on_orbit2": orig_id_on_orbit2,
                    "origin": origin,
                    "originator": originator,
                    "owner_contacted": owner_contacted,
                    "penetration_level_sigma": penetration_level_sigma,
                    "raw_file_uri": raw_file_uri,
                    "rel_pos_n": rel_pos_n,
                    "rel_pos_r": rel_pos_r,
                    "rel_pos_t": rel_pos_t,
                    "rel_vel_mag": rel_vel_mag,
                    "rel_vel_n": rel_vel_n,
                    "rel_vel_r": rel_vel_r,
                    "rel_vel_t": rel_vel_t,
                    "sat_no1": sat_no1,
                    "sat_no2": sat_no2,
                    "screen_entry_time": screen_entry_time,
                    "screen_exit_time": screen_exit_time,
                    "screen_volume_x": screen_volume_x,
                    "screen_volume_y": screen_volume_y,
                    "screen_volume_z": screen_volume_z,
                    "small_cov_warning": small_cov_warning,
                    "small_rel_vel_warning": small_rel_vel_warning,
                    "state_dept_notified": state_dept_notified,
                    "state_vector1": state_vector1,
                    "state_vector2": state_vector2,
                    "tags": tags,
                    "thrust_accel1": thrust_accel1,
                    "thrust_accel2": thrust_accel2,
                    "transaction_id": transaction_id,
                    "type": type,
                    "uvw_warn": uvw_warn,
                    "vol_entry_time": vol_entry_time,
                    "vol_exit_time": vol_exit_time,
                    "vol_shape": vol_shape,
                },
                conjunction_create_udl_params.ConjunctionCreateUdlParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"convert_pos_vel": convert_pos_vel}, conjunction_create_udl_params.ConjunctionCreateUdlParams
                ),
            ),
            cast_to=NoneType,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[conjunction_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        Conjunctions as a POST body and ingest into the database. A Conjunction is
        analysis of probability of collision; the data can include state vectors for
        primary and secondary satellites. This operation is not intended to be used for
        automated feeds into UDL. Data providers should contact the UDL team for
        specific role assignments and for instructions on setting up a permanent feed
        through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/conjunction/createBulk",
            body=await async_maybe_transform(body, Iterable[conjunction_create_bulk_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_history(
        self,
        *,
        tca: Union[str, datetime],
        columns: str | NotGiven = NOT_GIVEN,
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConjunctionGetHistoryResponse:
        """
        Service operation to dynamically query historical data by a variety of query
        parameters not specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          columns: optional, fields for retrieval. When omitted, ALL fields are assumed. See the
              queryhelp operation (/udl/&lt;datatype&gt;/queryhelp) for more details on valid
              query fields that can be selected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/conjunction/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tca": tca,
                        "columns": columns,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_get_history_params.ConjunctionGetHistoryParams,
                ),
            ),
            cast_to=ConjunctionGetHistoryResponse,
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
            "/udl/conjunction/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        tca: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConjunctionTupleResponse:
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

          tca: Time of closest approach (TCA) in UTC. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/conjunction/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "tca": tca,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    conjunction_tuple_params.ConjunctionTupleParams,
                ),
            ),
            cast_to=ConjunctionTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[conjunction_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of Conjunctions as a POST body and ingest into
        the database. A Conjunction is analysis of probability of collision; the data
        can include state vectors for primary and secondary satellites. This operation
        is intended to be used for automated feeds into UDL. A specific role is required
        to perform this service operation. Please contact the UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-conjunction",
            body=await async_maybe_transform(body, Iterable[conjunction_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upload_conjunction_data_message(
        self,
        *,
        classification: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        filename: str,
        source: str,
        body: FileTypes,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service to accept multiple CDMs in as zip file or a single CDM as payload.

        The
        service converts key-value pair formatted CDMs to UDL formats and stores them.
        The CDM format is as described in https://ccsds.org document CCSDS 508.0-B-1. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        **Example:**
        /filedrop/cdms?filename=conj.zip&classification=U&dataMode=TEST&source=Bluestaq&tags=tag1,tag2

        Args:
          classification: Classification marking of the data in IC/CAPCO Portion-marked format.

          data_mode: Indicator of whether the data is REAL, TEST, SIMULATED, or EXERCISE data.

          filename: Filename of the payload.

          source: Source of the data.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/cdms",
            body=await async_maybe_transform(
                body, conjunction_upload_conjunction_data_message_params.ConjunctionUploadConjunctionDataMessageParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "classification": classification,
                        "data_mode": data_mode,
                        "filename": filename,
                        "source": source,
                        "tags": tags,
                    },
                    conjunction_upload_conjunction_data_message_params.ConjunctionUploadConjunctionDataMessageParams,
                ),
            ),
            cast_to=NoneType,
        )


class ConjunctionsResourceWithRawResponse:
    def __init__(self, conjunctions: ConjunctionsResource) -> None:
        self._conjunctions = conjunctions

        self.retrieve = to_raw_response_wrapper(
            conjunctions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            conjunctions.list,
        )
        self.count = to_raw_response_wrapper(
            conjunctions.count,
        )
        self.create_udl = to_raw_response_wrapper(
            conjunctions.create_udl,
        )
        self.create_bulk = to_raw_response_wrapper(
            conjunctions.create_bulk,
        )
        self.get_history = to_raw_response_wrapper(
            conjunctions.get_history,
        )
        self.queryhelp = to_raw_response_wrapper(
            conjunctions.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            conjunctions.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            conjunctions.unvalidated_publish,
        )
        self.upload_conjunction_data_message = to_raw_response_wrapper(
            conjunctions.upload_conjunction_data_message,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._conjunctions.history)


class AsyncConjunctionsResourceWithRawResponse:
    def __init__(self, conjunctions: AsyncConjunctionsResource) -> None:
        self._conjunctions = conjunctions

        self.retrieve = async_to_raw_response_wrapper(
            conjunctions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            conjunctions.list,
        )
        self.count = async_to_raw_response_wrapper(
            conjunctions.count,
        )
        self.create_udl = async_to_raw_response_wrapper(
            conjunctions.create_udl,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            conjunctions.create_bulk,
        )
        self.get_history = async_to_raw_response_wrapper(
            conjunctions.get_history,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            conjunctions.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            conjunctions.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            conjunctions.unvalidated_publish,
        )
        self.upload_conjunction_data_message = async_to_raw_response_wrapper(
            conjunctions.upload_conjunction_data_message,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._conjunctions.history)


class ConjunctionsResourceWithStreamingResponse:
    def __init__(self, conjunctions: ConjunctionsResource) -> None:
        self._conjunctions = conjunctions

        self.retrieve = to_streamed_response_wrapper(
            conjunctions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            conjunctions.list,
        )
        self.count = to_streamed_response_wrapper(
            conjunctions.count,
        )
        self.create_udl = to_streamed_response_wrapper(
            conjunctions.create_udl,
        )
        self.create_bulk = to_streamed_response_wrapper(
            conjunctions.create_bulk,
        )
        self.get_history = to_streamed_response_wrapper(
            conjunctions.get_history,
        )
        self.queryhelp = to_streamed_response_wrapper(
            conjunctions.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            conjunctions.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            conjunctions.unvalidated_publish,
        )
        self.upload_conjunction_data_message = to_streamed_response_wrapper(
            conjunctions.upload_conjunction_data_message,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._conjunctions.history)


class AsyncConjunctionsResourceWithStreamingResponse:
    def __init__(self, conjunctions: AsyncConjunctionsResource) -> None:
        self._conjunctions = conjunctions

        self.retrieve = async_to_streamed_response_wrapper(
            conjunctions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            conjunctions.list,
        )
        self.count = async_to_streamed_response_wrapper(
            conjunctions.count,
        )
        self.create_udl = async_to_streamed_response_wrapper(
            conjunctions.create_udl,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            conjunctions.create_bulk,
        )
        self.get_history = async_to_streamed_response_wrapper(
            conjunctions.get_history,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            conjunctions.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            conjunctions.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            conjunctions.unvalidated_publish,
        )
        self.upload_conjunction_data_message = async_to_streamed_response_wrapper(
            conjunctions.upload_conjunction_data_message,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._conjunctions.history)
