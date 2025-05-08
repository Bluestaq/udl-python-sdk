# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    object_of_interest_get_params,
    object_of_interest_list_params,
    object_of_interest_count_params,
    object_of_interest_tuple_params,
    object_of_interest_create_params,
    object_of_interest_update_params,
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
from ..types.object_of_interest_get_response import ObjectOfInterestGetResponse
from ..types.object_of_interest_list_response import ObjectOfInterestListResponse
from ..types.object_of_interest_tuple_response import ObjectOfInterestTupleResponse

__all__ = ["ObjectOfInterestResource", "AsyncObjectOfInterestResource"]


class ObjectOfInterestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectOfInterestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ObjectOfInterestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectOfInterestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ObjectOfInterestResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_on_orbit: str,
        sensor_tasking_start_time: Union[str, datetime],
        source: str,
        status_date: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        affected_objects: List[str] | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        b_star: float | NotGiven = NOT_GIVEN,
        delta_ts: Iterable[float] | NotGiven = NOT_GIVEN,
        delta_vs: Iterable[float] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        elset_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mean_anomaly: float | NotGiven = NOT_GIVEN,
        mean_motion: float | NotGiven = NOT_GIVEN,
        mean_motion_d_dot: float | NotGiven = NOT_GIVEN,
        mean_motion_dot: float | NotGiven = NOT_GIVEN,
        missed_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        sensor_tasking_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        sv_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        x: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        y: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        z: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single ObjectOfInterest as a POST body and ingest
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

          id_on_orbit: UUID of the parent Onorbit record.

          sensor_tasking_start_time: Sensor tasking start time for object of interest.

          source: Source of the data.

          status_date: Time of last status change of the object of interest event.

          id: Unique identifier of the record, auto-generated by the system.

          affected_objects: Optional array of Onorbit IDs (idOnOrbit) representing satellites potentially
              affected by this object of interest.

          apogee: Last reported apogee. The Orbit point furthest from the center of the earth in
              kilometers.

          arg_of_perigee: Last reported argument of perigee. The argument of perigee is the angle in
              degrees formed between the perigee and the ascending node. If the perigee would
              occur at the ascending node, the argument of perigee would be 0.

          b_star: Last reported drag term for SGP4 orbital model, used for calculating decay
              constants for altitude, eccentricity etc, measured in inverse earth radii.

          delta_ts: Possible delta time applications for the object of interest, in seconds.

          delta_vs: Possible delta V applications for the object of interest, in km/sec.

          description: Description of the object of interest event.

          eccentricity: Last reported eccentricity of the object. The orbital eccentricity of an
              astronomical object is a parameter that determines the amount by which its orbit
              around another body deviates from a perfect circle. A value of 0 is a circular
              orbit, values between 0 and 1 form an elliptic orbit, 1 is a parabolic escape
              orbit, and greater than 1 is a hyperbolic escape orbit.

          elset_epoch: Last reported elset epoch time in ISO 8601 UTC time, with microsecond precision.

          inclination: Last reported inclination of the object. Inclination is the angle between the
              equator and the orbit when looking from the center of the Earth. If the orbit
              went exactly around the equator from left to right, then the inclination would
              be 0. The inclination ranges from 0 to 180 degrees.

          last_ob_time: Last reported observation time in ISO 8601 UTC time, with microsecond precision.

          mean_anomaly: Last reported meanAnomaly. Mean anomoly is where the satellite is in its orbital
              path. The mean anomaly ranges from 0 to 360 degrees. The mean anomaly is
              referenced to the perigee. If the satellite were at the perigee, the mean
              anomaly would be 0.

          mean_motion: Last reported mean motion of the object. Mean motion is the angular speed
              required for a body to complete one orbit, assuming constant speed in a circular
              orbit which completes in the same time as the variable speed, elliptical orbit
              of the actual body. Measured in revolutions per day.

          mean_motion_d_dot: Last reported 2nd derivative of the mean motion with respect to time. Units are
              revolutions per day cubed.

          mean_motion_dot: Last reported 1st derivative of the mean motion with respect to time. Units are
              revolutions per day squared.

          missed_ob_time: The time at which an attempted observation of the object of interest noticed it
              was missing, in ISO 8601 UTC time, with microsecond precision.

          name: Unique name of the object of interest event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          perigee: Last reported perigee. The orbit point nearest to the center of the earth in
              kilometers.

          period: Last reported orbit period. Period of the orbit is equal to inverse of mean
              motion.

          priority: Priority of the object of interest as an integer (1=highest priority).

          raan: Last reported raan. Right ascension of the ascending node, or RAAN is the angle
              as measured in degrees eastwards (or, as seen from the north, counterclockwise)
              from the First Point of Aries to the ascending node, which is where the orbit
              crosses the equator when traveling north.

          rev_no: The last reported revolution number. The value is incremented when a satellite
              crosses the equator on an ascending pass.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          semi_major_axis: Last reported semi major axis, which is the sum of the periapsis and apoapsis
              distances divided by two. For circular orbits, the semimajor axis is the
              distance between the centers of the bodies, not the distance of the bodies from
              the center of mass.

          sensor_tasking_stop_time: Sensor tasking stop time for object of interest.

          status: Status of the object of interest event (e.g. OPEN, CLOSED, CANCELLED).

          sv_epoch: Last reported state vector epoch time in ISO 8601 UTC time, with microsecond
              precision.

          x: Last reported x position of the object in km, in J2000 coordinates.

          xvel: Last reported x velocity of the object in km/sec, in J2000 coordinates.

          y: Last reported y position of the object in km, in J2000 coordinates.

          yvel: Last reported y velocity of the object in km/sec, in J2000 coordinates.

          z: Last reported z position of the object in km, in J2000 coordinates.

          zvel: Last reported z velocity of the object in km/sec, in J2000 coordinates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/objectofinterest",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "sensor_tasking_start_time": sensor_tasking_start_time,
                    "source": source,
                    "status_date": status_date,
                    "id": id,
                    "affected_objects": affected_objects,
                    "apogee": apogee,
                    "arg_of_perigee": arg_of_perigee,
                    "b_star": b_star,
                    "delta_ts": delta_ts,
                    "delta_vs": delta_vs,
                    "description": description,
                    "eccentricity": eccentricity,
                    "elset_epoch": elset_epoch,
                    "inclination": inclination,
                    "last_ob_time": last_ob_time,
                    "mean_anomaly": mean_anomaly,
                    "mean_motion": mean_motion,
                    "mean_motion_d_dot": mean_motion_d_dot,
                    "mean_motion_dot": mean_motion_dot,
                    "missed_ob_time": missed_ob_time,
                    "name": name,
                    "origin": origin,
                    "perigee": perigee,
                    "period": period,
                    "priority": priority,
                    "raan": raan,
                    "rev_no": rev_no,
                    "sat_no": sat_no,
                    "semi_major_axis": semi_major_axis,
                    "sensor_tasking_stop_time": sensor_tasking_stop_time,
                    "status": status,
                    "sv_epoch": sv_epoch,
                    "x": x,
                    "xvel": xvel,
                    "y": y,
                    "yvel": yvel,
                    "z": z,
                    "zvel": zvel,
                },
                object_of_interest_create_params.ObjectOfInterestCreateParams,
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
        id_on_orbit: str,
        sensor_tasking_start_time: Union[str, datetime],
        source: str,
        status_date: Union[str, datetime],
        body_id: str | NotGiven = NOT_GIVEN,
        affected_objects: List[str] | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        b_star: float | NotGiven = NOT_GIVEN,
        delta_ts: Iterable[float] | NotGiven = NOT_GIVEN,
        delta_vs: Iterable[float] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        elset_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mean_anomaly: float | NotGiven = NOT_GIVEN,
        mean_motion: float | NotGiven = NOT_GIVEN,
        mean_motion_d_dot: float | NotGiven = NOT_GIVEN,
        mean_motion_dot: float | NotGiven = NOT_GIVEN,
        missed_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        sensor_tasking_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        sv_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        x: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        y: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        z: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single ObjectOfInterest.

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

          id_on_orbit: UUID of the parent Onorbit record.

          sensor_tasking_start_time: Sensor tasking start time for object of interest.

          source: Source of the data.

          status_date: Time of last status change of the object of interest event.

          body_id: Unique identifier of the record, auto-generated by the system.

          affected_objects: Optional array of Onorbit IDs (idOnOrbit) representing satellites potentially
              affected by this object of interest.

          apogee: Last reported apogee. The Orbit point furthest from the center of the earth in
              kilometers.

          arg_of_perigee: Last reported argument of perigee. The argument of perigee is the angle in
              degrees formed between the perigee and the ascending node. If the perigee would
              occur at the ascending node, the argument of perigee would be 0.

          b_star: Last reported drag term for SGP4 orbital model, used for calculating decay
              constants for altitude, eccentricity etc, measured in inverse earth radii.

          delta_ts: Possible delta time applications for the object of interest, in seconds.

          delta_vs: Possible delta V applications for the object of interest, in km/sec.

          description: Description of the object of interest event.

          eccentricity: Last reported eccentricity of the object. The orbital eccentricity of an
              astronomical object is a parameter that determines the amount by which its orbit
              around another body deviates from a perfect circle. A value of 0 is a circular
              orbit, values between 0 and 1 form an elliptic orbit, 1 is a parabolic escape
              orbit, and greater than 1 is a hyperbolic escape orbit.

          elset_epoch: Last reported elset epoch time in ISO 8601 UTC time, with microsecond precision.

          inclination: Last reported inclination of the object. Inclination is the angle between the
              equator and the orbit when looking from the center of the Earth. If the orbit
              went exactly around the equator from left to right, then the inclination would
              be 0. The inclination ranges from 0 to 180 degrees.

          last_ob_time: Last reported observation time in ISO 8601 UTC time, with microsecond precision.

          mean_anomaly: Last reported meanAnomaly. Mean anomoly is where the satellite is in its orbital
              path. The mean anomaly ranges from 0 to 360 degrees. The mean anomaly is
              referenced to the perigee. If the satellite were at the perigee, the mean
              anomaly would be 0.

          mean_motion: Last reported mean motion of the object. Mean motion is the angular speed
              required for a body to complete one orbit, assuming constant speed in a circular
              orbit which completes in the same time as the variable speed, elliptical orbit
              of the actual body. Measured in revolutions per day.

          mean_motion_d_dot: Last reported 2nd derivative of the mean motion with respect to time. Units are
              revolutions per day cubed.

          mean_motion_dot: Last reported 1st derivative of the mean motion with respect to time. Units are
              revolutions per day squared.

          missed_ob_time: The time at which an attempted observation of the object of interest noticed it
              was missing, in ISO 8601 UTC time, with microsecond precision.

          name: Unique name of the object of interest event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          perigee: Last reported perigee. The orbit point nearest to the center of the earth in
              kilometers.

          period: Last reported orbit period. Period of the orbit is equal to inverse of mean
              motion.

          priority: Priority of the object of interest as an integer (1=highest priority).

          raan: Last reported raan. Right ascension of the ascending node, or RAAN is the angle
              as measured in degrees eastwards (or, as seen from the north, counterclockwise)
              from the First Point of Aries to the ascending node, which is where the orbit
              crosses the equator when traveling north.

          rev_no: The last reported revolution number. The value is incremented when a satellite
              crosses the equator on an ascending pass.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          semi_major_axis: Last reported semi major axis, which is the sum of the periapsis and apoapsis
              distances divided by two. For circular orbits, the semimajor axis is the
              distance between the centers of the bodies, not the distance of the bodies from
              the center of mass.

          sensor_tasking_stop_time: Sensor tasking stop time for object of interest.

          status: Status of the object of interest event (e.g. OPEN, CLOSED, CANCELLED).

          sv_epoch: Last reported state vector epoch time in ISO 8601 UTC time, with microsecond
              precision.

          x: Last reported x position of the object in km, in J2000 coordinates.

          xvel: Last reported x velocity of the object in km/sec, in J2000 coordinates.

          y: Last reported y position of the object in km, in J2000 coordinates.

          yvel: Last reported y velocity of the object in km/sec, in J2000 coordinates.

          z: Last reported z position of the object in km, in J2000 coordinates.

          zvel: Last reported z velocity of the object in km/sec, in J2000 coordinates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/objectofinterest/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "sensor_tasking_start_time": sensor_tasking_start_time,
                    "source": source,
                    "status_date": status_date,
                    "body_id": body_id,
                    "affected_objects": affected_objects,
                    "apogee": apogee,
                    "arg_of_perigee": arg_of_perigee,
                    "b_star": b_star,
                    "delta_ts": delta_ts,
                    "delta_vs": delta_vs,
                    "description": description,
                    "eccentricity": eccentricity,
                    "elset_epoch": elset_epoch,
                    "inclination": inclination,
                    "last_ob_time": last_ob_time,
                    "mean_anomaly": mean_anomaly,
                    "mean_motion": mean_motion,
                    "mean_motion_d_dot": mean_motion_d_dot,
                    "mean_motion_dot": mean_motion_dot,
                    "missed_ob_time": missed_ob_time,
                    "name": name,
                    "origin": origin,
                    "perigee": perigee,
                    "period": period,
                    "priority": priority,
                    "raan": raan,
                    "rev_no": rev_no,
                    "sat_no": sat_no,
                    "semi_major_axis": semi_major_axis,
                    "sensor_tasking_stop_time": sensor_tasking_stop_time,
                    "status": status,
                    "sv_epoch": sv_epoch,
                    "x": x,
                    "xvel": xvel,
                    "y": y,
                    "yvel": yvel,
                    "z": z,
                    "zvel": zvel,
                },
                object_of_interest_update_params.ObjectOfInterestUpdateParams,
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
    ) -> SyncOffsetPage[ObjectOfInterestListResponse]:
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
            "/udl/objectofinterest",
            page=SyncOffsetPage[ObjectOfInterestListResponse],
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
                    object_of_interest_list_params.ObjectOfInterestListParams,
                ),
            ),
            model=ObjectOfInterestListResponse,
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
        Service operation to delete a ObjectOfInterest object specified by the passed ID
        path parameter. A ObjectOfInterest is an on-orbit ObjectOfInterestunications
        payload, including supporting data such as transponders and channels, etc. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

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
            f"/udl/objectofinterest/{id}",
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
            "/udl/objectofinterest/count",
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
                    object_of_interest_count_params.ObjectOfInterestCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> ObjectOfInterestGetResponse:
        """
        Service operation to get a single ObjectOfInterest record by its unique ID
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
            f"/udl/objectofinterest/{id}",
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
                    object_of_interest_get_params.ObjectOfInterestGetParams,
                ),
            ),
            cast_to=ObjectOfInterestGetResponse,
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
            "/udl/objectofinterest/queryhelp",
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
    ) -> ObjectOfInterestTupleResponse:
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
            "/udl/objectofinterest/tuple",
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
                    object_of_interest_tuple_params.ObjectOfInterestTupleParams,
                ),
            ),
            cast_to=ObjectOfInterestTupleResponse,
        )


class AsyncObjectOfInterestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectOfInterestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectOfInterestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectOfInterestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncObjectOfInterestResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_on_orbit: str,
        sensor_tasking_start_time: Union[str, datetime],
        source: str,
        status_date: Union[str, datetime],
        id: str | NotGiven = NOT_GIVEN,
        affected_objects: List[str] | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        b_star: float | NotGiven = NOT_GIVEN,
        delta_ts: Iterable[float] | NotGiven = NOT_GIVEN,
        delta_vs: Iterable[float] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        elset_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mean_anomaly: float | NotGiven = NOT_GIVEN,
        mean_motion: float | NotGiven = NOT_GIVEN,
        mean_motion_d_dot: float | NotGiven = NOT_GIVEN,
        mean_motion_dot: float | NotGiven = NOT_GIVEN,
        missed_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        sensor_tasking_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        sv_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        x: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        y: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        z: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single ObjectOfInterest as a POST body and ingest
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

          id_on_orbit: UUID of the parent Onorbit record.

          sensor_tasking_start_time: Sensor tasking start time for object of interest.

          source: Source of the data.

          status_date: Time of last status change of the object of interest event.

          id: Unique identifier of the record, auto-generated by the system.

          affected_objects: Optional array of Onorbit IDs (idOnOrbit) representing satellites potentially
              affected by this object of interest.

          apogee: Last reported apogee. The Orbit point furthest from the center of the earth in
              kilometers.

          arg_of_perigee: Last reported argument of perigee. The argument of perigee is the angle in
              degrees formed between the perigee and the ascending node. If the perigee would
              occur at the ascending node, the argument of perigee would be 0.

          b_star: Last reported drag term for SGP4 orbital model, used for calculating decay
              constants for altitude, eccentricity etc, measured in inverse earth radii.

          delta_ts: Possible delta time applications for the object of interest, in seconds.

          delta_vs: Possible delta V applications for the object of interest, in km/sec.

          description: Description of the object of interest event.

          eccentricity: Last reported eccentricity of the object. The orbital eccentricity of an
              astronomical object is a parameter that determines the amount by which its orbit
              around another body deviates from a perfect circle. A value of 0 is a circular
              orbit, values between 0 and 1 form an elliptic orbit, 1 is a parabolic escape
              orbit, and greater than 1 is a hyperbolic escape orbit.

          elset_epoch: Last reported elset epoch time in ISO 8601 UTC time, with microsecond precision.

          inclination: Last reported inclination of the object. Inclination is the angle between the
              equator and the orbit when looking from the center of the Earth. If the orbit
              went exactly around the equator from left to right, then the inclination would
              be 0. The inclination ranges from 0 to 180 degrees.

          last_ob_time: Last reported observation time in ISO 8601 UTC time, with microsecond precision.

          mean_anomaly: Last reported meanAnomaly. Mean anomoly is where the satellite is in its orbital
              path. The mean anomaly ranges from 0 to 360 degrees. The mean anomaly is
              referenced to the perigee. If the satellite were at the perigee, the mean
              anomaly would be 0.

          mean_motion: Last reported mean motion of the object. Mean motion is the angular speed
              required for a body to complete one orbit, assuming constant speed in a circular
              orbit which completes in the same time as the variable speed, elliptical orbit
              of the actual body. Measured in revolutions per day.

          mean_motion_d_dot: Last reported 2nd derivative of the mean motion with respect to time. Units are
              revolutions per day cubed.

          mean_motion_dot: Last reported 1st derivative of the mean motion with respect to time. Units are
              revolutions per day squared.

          missed_ob_time: The time at which an attempted observation of the object of interest noticed it
              was missing, in ISO 8601 UTC time, with microsecond precision.

          name: Unique name of the object of interest event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          perigee: Last reported perigee. The orbit point nearest to the center of the earth in
              kilometers.

          period: Last reported orbit period. Period of the orbit is equal to inverse of mean
              motion.

          priority: Priority of the object of interest as an integer (1=highest priority).

          raan: Last reported raan. Right ascension of the ascending node, or RAAN is the angle
              as measured in degrees eastwards (or, as seen from the north, counterclockwise)
              from the First Point of Aries to the ascending node, which is where the orbit
              crosses the equator when traveling north.

          rev_no: The last reported revolution number. The value is incremented when a satellite
              crosses the equator on an ascending pass.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          semi_major_axis: Last reported semi major axis, which is the sum of the periapsis and apoapsis
              distances divided by two. For circular orbits, the semimajor axis is the
              distance between the centers of the bodies, not the distance of the bodies from
              the center of mass.

          sensor_tasking_stop_time: Sensor tasking stop time for object of interest.

          status: Status of the object of interest event (e.g. OPEN, CLOSED, CANCELLED).

          sv_epoch: Last reported state vector epoch time in ISO 8601 UTC time, with microsecond
              precision.

          x: Last reported x position of the object in km, in J2000 coordinates.

          xvel: Last reported x velocity of the object in km/sec, in J2000 coordinates.

          y: Last reported y position of the object in km, in J2000 coordinates.

          yvel: Last reported y velocity of the object in km/sec, in J2000 coordinates.

          z: Last reported z position of the object in km, in J2000 coordinates.

          zvel: Last reported z velocity of the object in km/sec, in J2000 coordinates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/objectofinterest",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "sensor_tasking_start_time": sensor_tasking_start_time,
                    "source": source,
                    "status_date": status_date,
                    "id": id,
                    "affected_objects": affected_objects,
                    "apogee": apogee,
                    "arg_of_perigee": arg_of_perigee,
                    "b_star": b_star,
                    "delta_ts": delta_ts,
                    "delta_vs": delta_vs,
                    "description": description,
                    "eccentricity": eccentricity,
                    "elset_epoch": elset_epoch,
                    "inclination": inclination,
                    "last_ob_time": last_ob_time,
                    "mean_anomaly": mean_anomaly,
                    "mean_motion": mean_motion,
                    "mean_motion_d_dot": mean_motion_d_dot,
                    "mean_motion_dot": mean_motion_dot,
                    "missed_ob_time": missed_ob_time,
                    "name": name,
                    "origin": origin,
                    "perigee": perigee,
                    "period": period,
                    "priority": priority,
                    "raan": raan,
                    "rev_no": rev_no,
                    "sat_no": sat_no,
                    "semi_major_axis": semi_major_axis,
                    "sensor_tasking_stop_time": sensor_tasking_stop_time,
                    "status": status,
                    "sv_epoch": sv_epoch,
                    "x": x,
                    "xvel": xvel,
                    "y": y,
                    "yvel": yvel,
                    "z": z,
                    "zvel": zvel,
                },
                object_of_interest_create_params.ObjectOfInterestCreateParams,
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
        id_on_orbit: str,
        sensor_tasking_start_time: Union[str, datetime],
        source: str,
        status_date: Union[str, datetime],
        body_id: str | NotGiven = NOT_GIVEN,
        affected_objects: List[str] | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        b_star: float | NotGiven = NOT_GIVEN,
        delta_ts: Iterable[float] | NotGiven = NOT_GIVEN,
        delta_vs: Iterable[float] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        elset_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mean_anomaly: float | NotGiven = NOT_GIVEN,
        mean_motion: float | NotGiven = NOT_GIVEN,
        mean_motion_d_dot: float | NotGiven = NOT_GIVEN,
        mean_motion_dot: float | NotGiven = NOT_GIVEN,
        missed_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        rev_no: int | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        sensor_tasking_stop_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        sv_epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        x: float | NotGiven = NOT_GIVEN,
        xvel: float | NotGiven = NOT_GIVEN,
        y: float | NotGiven = NOT_GIVEN,
        yvel: float | NotGiven = NOT_GIVEN,
        z: float | NotGiven = NOT_GIVEN,
        zvel: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single ObjectOfInterest.

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

          id_on_orbit: UUID of the parent Onorbit record.

          sensor_tasking_start_time: Sensor tasking start time for object of interest.

          source: Source of the data.

          status_date: Time of last status change of the object of interest event.

          body_id: Unique identifier of the record, auto-generated by the system.

          affected_objects: Optional array of Onorbit IDs (idOnOrbit) representing satellites potentially
              affected by this object of interest.

          apogee: Last reported apogee. The Orbit point furthest from the center of the earth in
              kilometers.

          arg_of_perigee: Last reported argument of perigee. The argument of perigee is the angle in
              degrees formed between the perigee and the ascending node. If the perigee would
              occur at the ascending node, the argument of perigee would be 0.

          b_star: Last reported drag term for SGP4 orbital model, used for calculating decay
              constants for altitude, eccentricity etc, measured in inverse earth radii.

          delta_ts: Possible delta time applications for the object of interest, in seconds.

          delta_vs: Possible delta V applications for the object of interest, in km/sec.

          description: Description of the object of interest event.

          eccentricity: Last reported eccentricity of the object. The orbital eccentricity of an
              astronomical object is a parameter that determines the amount by which its orbit
              around another body deviates from a perfect circle. A value of 0 is a circular
              orbit, values between 0 and 1 form an elliptic orbit, 1 is a parabolic escape
              orbit, and greater than 1 is a hyperbolic escape orbit.

          elset_epoch: Last reported elset epoch time in ISO 8601 UTC time, with microsecond precision.

          inclination: Last reported inclination of the object. Inclination is the angle between the
              equator and the orbit when looking from the center of the Earth. If the orbit
              went exactly around the equator from left to right, then the inclination would
              be 0. The inclination ranges from 0 to 180 degrees.

          last_ob_time: Last reported observation time in ISO 8601 UTC time, with microsecond precision.

          mean_anomaly: Last reported meanAnomaly. Mean anomoly is where the satellite is in its orbital
              path. The mean anomaly ranges from 0 to 360 degrees. The mean anomaly is
              referenced to the perigee. If the satellite were at the perigee, the mean
              anomaly would be 0.

          mean_motion: Last reported mean motion of the object. Mean motion is the angular speed
              required for a body to complete one orbit, assuming constant speed in a circular
              orbit which completes in the same time as the variable speed, elliptical orbit
              of the actual body. Measured in revolutions per day.

          mean_motion_d_dot: Last reported 2nd derivative of the mean motion with respect to time. Units are
              revolutions per day cubed.

          mean_motion_dot: Last reported 1st derivative of the mean motion with respect to time. Units are
              revolutions per day squared.

          missed_ob_time: The time at which an attempted observation of the object of interest noticed it
              was missing, in ISO 8601 UTC time, with microsecond precision.

          name: Unique name of the object of interest event.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          perigee: Last reported perigee. The orbit point nearest to the center of the earth in
              kilometers.

          period: Last reported orbit period. Period of the orbit is equal to inverse of mean
              motion.

          priority: Priority of the object of interest as an integer (1=highest priority).

          raan: Last reported raan. Right ascension of the ascending node, or RAAN is the angle
              as measured in degrees eastwards (or, as seen from the north, counterclockwise)
              from the First Point of Aries to the ascending node, which is where the orbit
              crosses the equator when traveling north.

          rev_no: The last reported revolution number. The value is incremented when a satellite
              crosses the equator on an ascending pass.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          semi_major_axis: Last reported semi major axis, which is the sum of the periapsis and apoapsis
              distances divided by two. For circular orbits, the semimajor axis is the
              distance between the centers of the bodies, not the distance of the bodies from
              the center of mass.

          sensor_tasking_stop_time: Sensor tasking stop time for object of interest.

          status: Status of the object of interest event (e.g. OPEN, CLOSED, CANCELLED).

          sv_epoch: Last reported state vector epoch time in ISO 8601 UTC time, with microsecond
              precision.

          x: Last reported x position of the object in km, in J2000 coordinates.

          xvel: Last reported x velocity of the object in km/sec, in J2000 coordinates.

          y: Last reported y position of the object in km, in J2000 coordinates.

          yvel: Last reported y velocity of the object in km/sec, in J2000 coordinates.

          z: Last reported z position of the object in km, in J2000 coordinates.

          zvel: Last reported z velocity of the object in km/sec, in J2000 coordinates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/objectofinterest/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "sensor_tasking_start_time": sensor_tasking_start_time,
                    "source": source,
                    "status_date": status_date,
                    "body_id": body_id,
                    "affected_objects": affected_objects,
                    "apogee": apogee,
                    "arg_of_perigee": arg_of_perigee,
                    "b_star": b_star,
                    "delta_ts": delta_ts,
                    "delta_vs": delta_vs,
                    "description": description,
                    "eccentricity": eccentricity,
                    "elset_epoch": elset_epoch,
                    "inclination": inclination,
                    "last_ob_time": last_ob_time,
                    "mean_anomaly": mean_anomaly,
                    "mean_motion": mean_motion,
                    "mean_motion_d_dot": mean_motion_d_dot,
                    "mean_motion_dot": mean_motion_dot,
                    "missed_ob_time": missed_ob_time,
                    "name": name,
                    "origin": origin,
                    "perigee": perigee,
                    "period": period,
                    "priority": priority,
                    "raan": raan,
                    "rev_no": rev_no,
                    "sat_no": sat_no,
                    "semi_major_axis": semi_major_axis,
                    "sensor_tasking_stop_time": sensor_tasking_stop_time,
                    "status": status,
                    "sv_epoch": sv_epoch,
                    "x": x,
                    "xvel": xvel,
                    "y": y,
                    "yvel": yvel,
                    "z": z,
                    "zvel": zvel,
                },
                object_of_interest_update_params.ObjectOfInterestUpdateParams,
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
    ) -> AsyncPaginator[ObjectOfInterestListResponse, AsyncOffsetPage[ObjectOfInterestListResponse]]:
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
            "/udl/objectofinterest",
            page=AsyncOffsetPage[ObjectOfInterestListResponse],
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
                    object_of_interest_list_params.ObjectOfInterestListParams,
                ),
            ),
            model=ObjectOfInterestListResponse,
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
        Service operation to delete a ObjectOfInterest object specified by the passed ID
        path parameter. A ObjectOfInterest is an on-orbit ObjectOfInterestunications
        payload, including supporting data such as transponders and channels, etc. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

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
            f"/udl/objectofinterest/{id}",
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
            "/udl/objectofinterest/count",
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
                    object_of_interest_count_params.ObjectOfInterestCountParams,
                ),
            ),
            cast_to=str,
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
    ) -> ObjectOfInterestGetResponse:
        """
        Service operation to get a single ObjectOfInterest record by its unique ID
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
            f"/udl/objectofinterest/{id}",
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
                    object_of_interest_get_params.ObjectOfInterestGetParams,
                ),
            ),
            cast_to=ObjectOfInterestGetResponse,
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
            "/udl/objectofinterest/queryhelp",
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
    ) -> ObjectOfInterestTupleResponse:
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
            "/udl/objectofinterest/tuple",
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
                    object_of_interest_tuple_params.ObjectOfInterestTupleParams,
                ),
            ),
            cast_to=ObjectOfInterestTupleResponse,
        )


class ObjectOfInterestResourceWithRawResponse:
    def __init__(self, object_of_interest: ObjectOfInterestResource) -> None:
        self._object_of_interest = object_of_interest

        self.create = to_raw_response_wrapper(
            object_of_interest.create,
        )
        self.update = to_raw_response_wrapper(
            object_of_interest.update,
        )
        self.list = to_raw_response_wrapper(
            object_of_interest.list,
        )
        self.delete = to_raw_response_wrapper(
            object_of_interest.delete,
        )
        self.count = to_raw_response_wrapper(
            object_of_interest.count,
        )
        self.get = to_raw_response_wrapper(
            object_of_interest.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            object_of_interest.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            object_of_interest.tuple,
        )


class AsyncObjectOfInterestResourceWithRawResponse:
    def __init__(self, object_of_interest: AsyncObjectOfInterestResource) -> None:
        self._object_of_interest = object_of_interest

        self.create = async_to_raw_response_wrapper(
            object_of_interest.create,
        )
        self.update = async_to_raw_response_wrapper(
            object_of_interest.update,
        )
        self.list = async_to_raw_response_wrapper(
            object_of_interest.list,
        )
        self.delete = async_to_raw_response_wrapper(
            object_of_interest.delete,
        )
        self.count = async_to_raw_response_wrapper(
            object_of_interest.count,
        )
        self.get = async_to_raw_response_wrapper(
            object_of_interest.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            object_of_interest.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            object_of_interest.tuple,
        )


class ObjectOfInterestResourceWithStreamingResponse:
    def __init__(self, object_of_interest: ObjectOfInterestResource) -> None:
        self._object_of_interest = object_of_interest

        self.create = to_streamed_response_wrapper(
            object_of_interest.create,
        )
        self.update = to_streamed_response_wrapper(
            object_of_interest.update,
        )
        self.list = to_streamed_response_wrapper(
            object_of_interest.list,
        )
        self.delete = to_streamed_response_wrapper(
            object_of_interest.delete,
        )
        self.count = to_streamed_response_wrapper(
            object_of_interest.count,
        )
        self.get = to_streamed_response_wrapper(
            object_of_interest.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            object_of_interest.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            object_of_interest.tuple,
        )


class AsyncObjectOfInterestResourceWithStreamingResponse:
    def __init__(self, object_of_interest: AsyncObjectOfInterestResource) -> None:
        self._object_of_interest = object_of_interest

        self.create = async_to_streamed_response_wrapper(
            object_of_interest.create,
        )
        self.update = async_to_streamed_response_wrapper(
            object_of_interest.update,
        )
        self.list = async_to_streamed_response_wrapper(
            object_of_interest.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            object_of_interest.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            object_of_interest.count,
        )
        self.get = async_to_streamed_response_wrapper(
            object_of_interest.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            object_of_interest.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            object_of_interest.tuple,
        )
