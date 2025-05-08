# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    attitude_set_list_params,
    attitude_set_count_params,
    attitude_set_tuple_params,
    attitude_set_create_params,
    attitude_set_unvalidated_publish_params,
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
from ...types.attitudeset_abridged import AttitudesetAbridged
from ...types.attitude_set_tuple_response import AttitudeSetTupleResponse

__all__ = ["AttitudeSetsResource", "AsyncAttitudeSetsResource"]


class AttitudeSetsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AttitudeSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AttitudeSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttitudeSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AttitudeSetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        frame1: str,
        frame2: str,
        num_points: int,
        source: str,
        start_time: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        as_ref: List[str] | NotGiven = NOT_GIVEN,
        attitude_list: Iterable[attitude_set_create_params.AttitudeList] | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        euler_rot_seq: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        interpolator: str | NotGiven = NOT_GIVEN,
        interpolator_degree: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        prec_angle_init: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        spin_angle_init: float | NotGiven = NOT_GIVEN,
        step_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation intended for initial integration only.

        Takes a single
        AttitudeSet as a POST body and ingest into the database. This operation does not
        persist any Onorbit Attitude points that may be present in the body of the
        request. This operation is not intended to be used for automated feeds into UDL.
        A specific role is required to perform this service operation. Please contact
        the UDL team for assistance.

        The following rules apply to this operation:

        <h3>
         * Attitude Set numPoints value must correspond exactly to the number of Onorbit Attitude states associated with that Attitude Set.  The numPoints value is checked against the actual posted number of states and mismatch will result in the post being rejected.
         * Attitude Set startTime and endTime must correspond to the earliest and latest state times, respectively, of the associated Onorbit Attitude states.
         * Either satNo, idOnOrbit, or origObjectId must be provided.  The preferred option is to post with satNo for a cataloged object with (only) origObjectId for an unknown, uncatalogued, or internal/test object.  There are several cases for the logic associated with these fields:
           + If satNo is provided and correlates to a known UDL sat number then the idOnOrbit will be populated appropriately in addition to the satNo.
           + If satNo is provided and does not correlate to a known UDL sat number then the provided satNo value will be moved to the origObjectId field and satNo left null.
           + If origObjectId and a valid satNo or idOnOrbit are provided then both the satNo/idOnOrbit and origObjectId will maintain the provided values.
           + If only origObjectId is provided then origObjectId will be populated with the posted value.  In this case, no checks are made against existing UDL sat numbers.
        </h3>

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

          end_time: The end time of the attitude ephemeris, in ISO 8601 UTC format, with microsecond
              precision. If this set is constituted by a single epoch attitude message then
              endTime should match the startTime.

          frame1: Reference frame 1 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          frame2: Reference frame 2 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          num_points: Number of attitude records contained in this set.

          source: Source of the data.

          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.

          type: The type of attitude message or messages associated with this set.

              AEM = Attitude Ephemeris Message, specifying the attitude state of a single
              object at multiple epochs.

              APM = Attitude Parameters Message, specifying the attitude state of a single
              object at a single epoch.

          id: Unique identifier of the record, auto-generated by the system.

          as_ref: Array of UDL UUIDs of one or more AttitudeSet records associated with this set.
              For example, a spacecraft Attitude Ephemeris Set might include a reference to an
              Attitude Parameter Message defining the sensor to body frame transformation for
              a sensor onboard the spacecraft, which allows for calculation of the sensor
              orientation in frame2 of the attitude ephemeris.

          attitude_list: Collection of attitude data associated with this Attitude Set.

          es_id: Unique identifier of the parent (positional) Ephemeris Set, if this data is
              correlated with an Ephemeris.

          euler_rot_seq: The rotation sequence of the Euler angles in which attitude reference frame
              transformation occurs (from left to right). One, two, or three axis rotations
              are supported and are represented by one, two, or three characters respectively.
              Repeated axis rotations are also supported, however, these rotations should not
              be sequential. The numeric sequence values correspond to the body angles/rates
              as follows: 1 - xAngle/xRate, 2 - yAngle/yRate, and 3 - zAngle/zRate. Valid
              sequences are: 123, 132, 213, 231, 312, 321, 121, 131, 212, 232, 313, 323, 12,
              13, 21, 23, 31, 32, 1, 2, and 3.

              The following represent examples of possible rotation sequences: A single
              rotation about the Y-axis can be expressed as '2', a double rotation with X-Z
              sequence can be expressed as '13', and a triple rotation with Z-X-Y sequence can
              be expressed as '312'.

          id_sensor: Unique identifier of the sensor to which this attitude set applies IF this set
              is reporting a single sensor orientation.

          interpolator: Recommended interpolation method for estimating attitude ephemeris data.

          interpolator_degree: Recommended polynomial interpolation degree.

          notes: Optional notes/comments for this attitude set.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the record source to indicate the target object
              of this attitude set. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier to which this attitude set applies IF this set is reporting a single
              sensor orientation. This may be an internal identifier and not necessarily a
              valid sensor ID.

          prec_angle_init: Initial precession angle (ECI J2000 frame) in degrees.

          sat_no: Satellite/catalog number of the on-orbit object to which this attitude set
              applies.

          spin_angle_init: Initial spin angle (ECI J2000 frame) in degrees.

          step_size: Attitude ephemeris step size, in seconds. This applies to Attitude Ephemeris
              Messages (AEM) that employ a fixed step size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/attitudeset",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "frame1": frame1,
                    "frame2": frame2,
                    "num_points": num_points,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "as_ref": as_ref,
                    "attitude_list": attitude_list,
                    "es_id": es_id,
                    "euler_rot_seq": euler_rot_seq,
                    "id_sensor": id_sensor,
                    "interpolator": interpolator,
                    "interpolator_degree": interpolator_degree,
                    "notes": notes,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "prec_angle_init": prec_angle_init,
                    "sat_no": sat_no,
                    "spin_angle_init": spin_angle_init,
                    "step_size": step_size,
                },
                attitude_set_create_params.AttitudeSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[AttitudesetAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/attitudeset",
            page=SyncOffsetPage[AttitudesetAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_set_list_params.AttitudeSetListParams,
                ),
            ),
            model=AttitudesetAbridged,
        )

    def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/attitudeset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_set_count_params.AttitudeSetCountParams,
                ),
            ),
            cast_to=str,
        )

    def query_help(
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
            "/udl/attitudeset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudeSetTupleResponse:
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

          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/attitudeset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_set_tuple_params.AttitudeSetTupleParams,
                ),
            ),
            cast_to=AttitudeSetTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        frame1: str,
        frame2: str,
        num_points: int,
        source: str,
        start_time: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        as_ref: List[str] | NotGiven = NOT_GIVEN,
        attitude_list: Iterable[attitude_set_unvalidated_publish_params.AttitudeList] | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        euler_rot_seq: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        interpolator: str | NotGiven = NOT_GIVEN,
        interpolator_degree: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        prec_angle_init: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        spin_angle_init: float | NotGiven = NOT_GIVEN,
        step_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Attitude Set and many associated Onorbit
        Attitude records as a POST body for ingest into the database. A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        The following rules apply to this operation:

        <h3>
          * Attitude Set numPoints value must correspond exactly to the number of Onorbit Attitude states associated with that Attitude Set. The numPoints value is checked against the actual posted number of states and mismatch will result in the post being rejected.
          * Attitude Set startTime and endTime must correspond to the earliest and latest state times, respectively, of the associated Onorbit Attitude states.
          * Either satNo, idOnOrbit, or origObjectId must be provided. The preferred option is to post with satNo for a cataloged object, and with (only) origObjectId for an unknown, uncatalogued, or internal/test object.  There are several cases for the logic associated with these fields:
            + If satNo is provided and correlates to a known UDL sat number then the idOnOrbit will be populated appropriately in addition to the satNo.
            + If satNo is provided and does not correlate to a known UDL sat number then the provided satNo value will be moved to the origObjectId field and satNo left null.
            + If origObjectId and a valid satNo or idOnOrbit are provided then both the satNo/idOnOrbit and origObjectId will maintain the provided values.
            + If only origObjectId is provided then origObjectId will be populated with the posted value.  In this case, no checks are made against existing UDL sat numbers.
        </h3>

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

          end_time: The end time of the attitude ephemeris, in ISO 8601 UTC format, with microsecond
              precision. If this set is constituted by a single epoch attitude message then
              endTime should match the startTime.

          frame1: Reference frame 1 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          frame2: Reference frame 2 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          num_points: Number of attitude records contained in this set.

          source: Source of the data.

          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.

          type: The type of attitude message or messages associated with this set.

              AEM = Attitude Ephemeris Message, specifying the attitude state of a single
              object at multiple epochs.

              APM = Attitude Parameters Message, specifying the attitude state of a single
              object at a single epoch.

          id: Unique identifier of the record, auto-generated by the system.

          as_ref: Array of UDL UUIDs of one or more AttitudeSet records associated with this set.
              For example, a spacecraft Attitude Ephemeris Set might include a reference to an
              Attitude Parameter Message defining the sensor to body frame transformation for
              a sensor onboard the spacecraft, which allows for calculation of the sensor
              orientation in frame2 of the attitude ephemeris.

          attitude_list: Collection of attitude data associated with this Attitude Set.

          es_id: Unique identifier of the parent (positional) Ephemeris Set, if this data is
              correlated with an Ephemeris.

          euler_rot_seq: The rotation sequence of the Euler angles in which attitude reference frame
              transformation occurs (from left to right). One, two, or three axis rotations
              are supported and are represented by one, two, or three characters respectively.
              Repeated axis rotations are also supported, however, these rotations should not
              be sequential. The numeric sequence values correspond to the body angles/rates
              as follows: 1 - xAngle/xRate, 2 - yAngle/yRate, and 3 - zAngle/zRate. Valid
              sequences are: 123, 132, 213, 231, 312, 321, 121, 131, 212, 232, 313, 323, 12,
              13, 21, 23, 31, 32, 1, 2, and 3.

              The following represent examples of possible rotation sequences: A single
              rotation about the Y-axis can be expressed as '2', a double rotation with X-Z
              sequence can be expressed as '13', and a triple rotation with Z-X-Y sequence can
              be expressed as '312'.

          id_sensor: Unique identifier of the sensor to which this attitude set applies IF this set
              is reporting a single sensor orientation.

          interpolator: Recommended interpolation method for estimating attitude ephemeris data.

          interpolator_degree: Recommended polynomial interpolation degree.

          notes: Optional notes/comments for this attitude set.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the record source to indicate the target object
              of this attitude set. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier to which this attitude set applies IF this set is reporting a single
              sensor orientation. This may be an internal identifier and not necessarily a
              valid sensor ID.

          prec_angle_init: Initial precession angle (ECI J2000 frame) in degrees.

          sat_no: Satellite/catalog number of the on-orbit object to which this attitude set
              applies.

          spin_angle_init: Initial spin angle (ECI J2000 frame) in degrees.

          step_size: Attitude ephemeris step size, in seconds. This applies to Attitude Ephemeris
              Messages (AEM) that employ a fixed step size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-attitudeset",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "frame1": frame1,
                    "frame2": frame2,
                    "num_points": num_points,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "as_ref": as_ref,
                    "attitude_list": attitude_list,
                    "es_id": es_id,
                    "euler_rot_seq": euler_rot_seq,
                    "id_sensor": id_sensor,
                    "interpolator": interpolator,
                    "interpolator_degree": interpolator_degree,
                    "notes": notes,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "prec_angle_init": prec_angle_init,
                    "sat_no": sat_no,
                    "spin_angle_init": spin_angle_init,
                    "step_size": step_size,
                },
                attitude_set_unvalidated_publish_params.AttitudeSetUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAttitudeSetsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAttitudeSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAttitudeSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttitudeSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncAttitudeSetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        frame1: str,
        frame2: str,
        num_points: int,
        source: str,
        start_time: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        as_ref: List[str] | NotGiven = NOT_GIVEN,
        attitude_list: Iterable[attitude_set_create_params.AttitudeList] | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        euler_rot_seq: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        interpolator: str | NotGiven = NOT_GIVEN,
        interpolator_degree: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        prec_angle_init: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        spin_angle_init: float | NotGiven = NOT_GIVEN,
        step_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation intended for initial integration only.

        Takes a single
        AttitudeSet as a POST body and ingest into the database. This operation does not
        persist any Onorbit Attitude points that may be present in the body of the
        request. This operation is not intended to be used for automated feeds into UDL.
        A specific role is required to perform this service operation. Please contact
        the UDL team for assistance.

        The following rules apply to this operation:

        <h3>
         * Attitude Set numPoints value must correspond exactly to the number of Onorbit Attitude states associated with that Attitude Set.  The numPoints value is checked against the actual posted number of states and mismatch will result in the post being rejected.
         * Attitude Set startTime and endTime must correspond to the earliest and latest state times, respectively, of the associated Onorbit Attitude states.
         * Either satNo, idOnOrbit, or origObjectId must be provided.  The preferred option is to post with satNo for a cataloged object with (only) origObjectId for an unknown, uncatalogued, or internal/test object.  There are several cases for the logic associated with these fields:
           + If satNo is provided and correlates to a known UDL sat number then the idOnOrbit will be populated appropriately in addition to the satNo.
           + If satNo is provided and does not correlate to a known UDL sat number then the provided satNo value will be moved to the origObjectId field and satNo left null.
           + If origObjectId and a valid satNo or idOnOrbit are provided then both the satNo/idOnOrbit and origObjectId will maintain the provided values.
           + If only origObjectId is provided then origObjectId will be populated with the posted value.  In this case, no checks are made against existing UDL sat numbers.
        </h3>

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

          end_time: The end time of the attitude ephemeris, in ISO 8601 UTC format, with microsecond
              precision. If this set is constituted by a single epoch attitude message then
              endTime should match the startTime.

          frame1: Reference frame 1 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          frame2: Reference frame 2 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          num_points: Number of attitude records contained in this set.

          source: Source of the data.

          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.

          type: The type of attitude message or messages associated with this set.

              AEM = Attitude Ephemeris Message, specifying the attitude state of a single
              object at multiple epochs.

              APM = Attitude Parameters Message, specifying the attitude state of a single
              object at a single epoch.

          id: Unique identifier of the record, auto-generated by the system.

          as_ref: Array of UDL UUIDs of one or more AttitudeSet records associated with this set.
              For example, a spacecraft Attitude Ephemeris Set might include a reference to an
              Attitude Parameter Message defining the sensor to body frame transformation for
              a sensor onboard the spacecraft, which allows for calculation of the sensor
              orientation in frame2 of the attitude ephemeris.

          attitude_list: Collection of attitude data associated with this Attitude Set.

          es_id: Unique identifier of the parent (positional) Ephemeris Set, if this data is
              correlated with an Ephemeris.

          euler_rot_seq: The rotation sequence of the Euler angles in which attitude reference frame
              transformation occurs (from left to right). One, two, or three axis rotations
              are supported and are represented by one, two, or three characters respectively.
              Repeated axis rotations are also supported, however, these rotations should not
              be sequential. The numeric sequence values correspond to the body angles/rates
              as follows: 1 - xAngle/xRate, 2 - yAngle/yRate, and 3 - zAngle/zRate. Valid
              sequences are: 123, 132, 213, 231, 312, 321, 121, 131, 212, 232, 313, 323, 12,
              13, 21, 23, 31, 32, 1, 2, and 3.

              The following represent examples of possible rotation sequences: A single
              rotation about the Y-axis can be expressed as '2', a double rotation with X-Z
              sequence can be expressed as '13', and a triple rotation with Z-X-Y sequence can
              be expressed as '312'.

          id_sensor: Unique identifier of the sensor to which this attitude set applies IF this set
              is reporting a single sensor orientation.

          interpolator: Recommended interpolation method for estimating attitude ephemeris data.

          interpolator_degree: Recommended polynomial interpolation degree.

          notes: Optional notes/comments for this attitude set.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the record source to indicate the target object
              of this attitude set. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier to which this attitude set applies IF this set is reporting a single
              sensor orientation. This may be an internal identifier and not necessarily a
              valid sensor ID.

          prec_angle_init: Initial precession angle (ECI J2000 frame) in degrees.

          sat_no: Satellite/catalog number of the on-orbit object to which this attitude set
              applies.

          spin_angle_init: Initial spin angle (ECI J2000 frame) in degrees.

          step_size: Attitude ephemeris step size, in seconds. This applies to Attitude Ephemeris
              Messages (AEM) that employ a fixed step size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/attitudeset",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "frame1": frame1,
                    "frame2": frame2,
                    "num_points": num_points,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "as_ref": as_ref,
                    "attitude_list": attitude_list,
                    "es_id": es_id,
                    "euler_rot_seq": euler_rot_seq,
                    "id_sensor": id_sensor,
                    "interpolator": interpolator,
                    "interpolator_degree": interpolator_degree,
                    "notes": notes,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "prec_angle_init": prec_angle_init,
                    "sat_no": sat_no,
                    "spin_angle_init": spin_angle_init,
                    "step_size": step_size,
                },
                attitude_set_create_params.AttitudeSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AttitudesetAbridged, AsyncOffsetPage[AttitudesetAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/attitudeset",
            page=AsyncOffsetPage[AttitudesetAbridged],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_set_list_params.AttitudeSetListParams,
                ),
            ),
            model=AttitudesetAbridged,
        )

    async def count(
        self,
        *,
        start_time: Union[str, datetime],
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
          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/attitudeset/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_set_count_params.AttitudeSetCountParams,
                ),
            ),
            cast_to=str,
        )

    async def query_help(
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
            "/udl/attitudeset/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tuple(
        self,
        *,
        columns: str,
        start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttitudeSetTupleResponse:
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

          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.
              (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/attitudeset/tuple",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "columns": columns,
                        "start_time": start_time,
                        "first_result": first_result,
                        "max_results": max_results,
                    },
                    attitude_set_tuple_params.AttitudeSetTupleParams,
                ),
            ),
            cast_to=AttitudeSetTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        end_time: Union[str, datetime],
        frame1: str,
        frame2: str,
        num_points: int,
        source: str,
        start_time: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        as_ref: List[str] | NotGiven = NOT_GIVEN,
        attitude_list: Iterable[attitude_set_unvalidated_publish_params.AttitudeList] | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        euler_rot_seq: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        interpolator: str | NotGiven = NOT_GIVEN,
        interpolator_degree: int | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        prec_angle_init: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        spin_angle_init: float | NotGiven = NOT_GIVEN,
        step_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Attitude Set and many associated Onorbit
        Attitude records as a POST body for ingest into the database. A specific role is
        required to perform this service operation. Please contact the UDL team for
        assistance.

        The following rules apply to this operation:

        <h3>
          * Attitude Set numPoints value must correspond exactly to the number of Onorbit Attitude states associated with that Attitude Set. The numPoints value is checked against the actual posted number of states and mismatch will result in the post being rejected.
          * Attitude Set startTime and endTime must correspond to the earliest and latest state times, respectively, of the associated Onorbit Attitude states.
          * Either satNo, idOnOrbit, or origObjectId must be provided. The preferred option is to post with satNo for a cataloged object, and with (only) origObjectId for an unknown, uncatalogued, or internal/test object.  There are several cases for the logic associated with these fields:
            + If satNo is provided and correlates to a known UDL sat number then the idOnOrbit will be populated appropriately in addition to the satNo.
            + If satNo is provided and does not correlate to a known UDL sat number then the provided satNo value will be moved to the origObjectId field and satNo left null.
            + If origObjectId and a valid satNo or idOnOrbit are provided then both the satNo/idOnOrbit and origObjectId will maintain the provided values.
            + If only origObjectId is provided then origObjectId will be populated with the posted value.  In this case, no checks are made against existing UDL sat numbers.
        </h3>

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

          end_time: The end time of the attitude ephemeris, in ISO 8601 UTC format, with microsecond
              precision. If this set is constituted by a single epoch attitude message then
              endTime should match the startTime.

          frame1: Reference frame 1 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          frame2: Reference frame 2 of the quaternion or Euler angle transformation utilized in
              this attitude parameter or attitude ephemeris. The UDL convention is that
              transformations occur FROM frame1 TO frame2. A specific spacecraft frame or
              instrument name may be provided with the assumption the consumer understands the
              location of these frames (ex. SC BODY, J2000, LVLH, ICRF, INSTRUMENTx,
              THRUSTERx, etc.).

          num_points: Number of attitude records contained in this set.

          source: Source of the data.

          start_time: The epoch or start time of the attitude parameter or attitude ephemeris, in ISO
              8601 UTC format, with microsecond precision. If this set is constituted by a
              single attitude parameter message then startTime is the epoch.

          type: The type of attitude message or messages associated with this set.

              AEM = Attitude Ephemeris Message, specifying the attitude state of a single
              object at multiple epochs.

              APM = Attitude Parameters Message, specifying the attitude state of a single
              object at a single epoch.

          id: Unique identifier of the record, auto-generated by the system.

          as_ref: Array of UDL UUIDs of one or more AttitudeSet records associated with this set.
              For example, a spacecraft Attitude Ephemeris Set might include a reference to an
              Attitude Parameter Message defining the sensor to body frame transformation for
              a sensor onboard the spacecraft, which allows for calculation of the sensor
              orientation in frame2 of the attitude ephemeris.

          attitude_list: Collection of attitude data associated with this Attitude Set.

          es_id: Unique identifier of the parent (positional) Ephemeris Set, if this data is
              correlated with an Ephemeris.

          euler_rot_seq: The rotation sequence of the Euler angles in which attitude reference frame
              transformation occurs (from left to right). One, two, or three axis rotations
              are supported and are represented by one, two, or three characters respectively.
              Repeated axis rotations are also supported, however, these rotations should not
              be sequential. The numeric sequence values correspond to the body angles/rates
              as follows: 1 - xAngle/xRate, 2 - yAngle/yRate, and 3 - zAngle/zRate. Valid
              sequences are: 123, 132, 213, 231, 312, 321, 121, 131, 212, 232, 313, 323, 12,
              13, 21, 23, 31, 32, 1, 2, and 3.

              The following represent examples of possible rotation sequences: A single
              rotation about the Y-axis can be expressed as '2', a double rotation with X-Z
              sequence can be expressed as '13', and a triple rotation with Z-X-Y sequence can
              be expressed as '312'.

          id_sensor: Unique identifier of the sensor to which this attitude set applies IF this set
              is reporting a single sensor orientation.

          interpolator: Recommended interpolation method for estimating attitude ephemeris data.

          interpolator_degree: Recommended polynomial interpolation degree.

          notes: Optional notes/comments for this attitude set.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the record source to indicate the target object
              of this attitude set. This may be an internal identifier and not necessarily map
              to a valid satellite number.

          orig_sensor_id: Optional identifier provided by the record source to indicate the sensor
              identifier to which this attitude set applies IF this set is reporting a single
              sensor orientation. This may be an internal identifier and not necessarily a
              valid sensor ID.

          prec_angle_init: Initial precession angle (ECI J2000 frame) in degrees.

          sat_no: Satellite/catalog number of the on-orbit object to which this attitude set
              applies.

          spin_angle_init: Initial spin angle (ECI J2000 frame) in degrees.

          step_size: Attitude ephemeris step size, in seconds. This applies to Attitude Ephemeris
              Messages (AEM) that employ a fixed step size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-attitudeset",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "end_time": end_time,
                    "frame1": frame1,
                    "frame2": frame2,
                    "num_points": num_points,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "as_ref": as_ref,
                    "attitude_list": attitude_list,
                    "es_id": es_id,
                    "euler_rot_seq": euler_rot_seq,
                    "id_sensor": id_sensor,
                    "interpolator": interpolator,
                    "interpolator_degree": interpolator_degree,
                    "notes": notes,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "prec_angle_init": prec_angle_init,
                    "sat_no": sat_no,
                    "spin_angle_init": spin_angle_init,
                    "step_size": step_size,
                },
                attitude_set_unvalidated_publish_params.AttitudeSetUnvalidatedPublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AttitudeSetsResourceWithRawResponse:
    def __init__(self, attitude_sets: AttitudeSetsResource) -> None:
        self._attitude_sets = attitude_sets

        self.create = to_raw_response_wrapper(
            attitude_sets.create,
        )
        self.list = to_raw_response_wrapper(
            attitude_sets.list,
        )
        self.count = to_raw_response_wrapper(
            attitude_sets.count,
        )
        self.query_help = to_raw_response_wrapper(
            attitude_sets.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            attitude_sets.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            attitude_sets.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._attitude_sets.history)


class AsyncAttitudeSetsResourceWithRawResponse:
    def __init__(self, attitude_sets: AsyncAttitudeSetsResource) -> None:
        self._attitude_sets = attitude_sets

        self.create = async_to_raw_response_wrapper(
            attitude_sets.create,
        )
        self.list = async_to_raw_response_wrapper(
            attitude_sets.list,
        )
        self.count = async_to_raw_response_wrapper(
            attitude_sets.count,
        )
        self.query_help = async_to_raw_response_wrapper(
            attitude_sets.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            attitude_sets.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            attitude_sets.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._attitude_sets.history)


class AttitudeSetsResourceWithStreamingResponse:
    def __init__(self, attitude_sets: AttitudeSetsResource) -> None:
        self._attitude_sets = attitude_sets

        self.create = to_streamed_response_wrapper(
            attitude_sets.create,
        )
        self.list = to_streamed_response_wrapper(
            attitude_sets.list,
        )
        self.count = to_streamed_response_wrapper(
            attitude_sets.count,
        )
        self.query_help = to_streamed_response_wrapper(
            attitude_sets.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            attitude_sets.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            attitude_sets.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._attitude_sets.history)


class AsyncAttitudeSetsResourceWithStreamingResponse:
    def __init__(self, attitude_sets: AsyncAttitudeSetsResource) -> None:
        self._attitude_sets = attitude_sets

        self.create = async_to_streamed_response_wrapper(
            attitude_sets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            attitude_sets.list,
        )
        self.count = async_to_streamed_response_wrapper(
            attitude_sets.count,
        )
        self.query_help = async_to_streamed_response_wrapper(
            attitude_sets.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            attitude_sets.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            attitude_sets.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._attitude_sets.history)
