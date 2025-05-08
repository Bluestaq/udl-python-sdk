# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    collect_request_list_params,
    collect_request_count_params,
    collect_request_tuple_params,
    collect_request_create_params,
    collect_request_retrieve_params,
    collect_request_create_bulk_params,
    collect_request_unvalidated_publish_params,
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
from ...types.collect_request_abridged import CollectRequestAbridged
from ...types.shared.collect_request_full import CollectRequestFull
from ...types.collect_request_tuple_response import CollectRequestTupleResponse

__all__ = ["CollectRequestsResource", "AsyncCollectRequestsResource"]


class CollectRequestsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CollectRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return CollectRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        start_time: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        az: float | NotGiven = NOT_GIVEN,
        customer: str | NotGiven = NOT_GIVEN,
        dec: float | NotGiven = NOT_GIVEN,
        duration: int | NotGiven = NOT_GIVEN,
        dwell_id: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        el: float | NotGiven = NOT_GIVEN,
        elset: collect_request_create_params.Elset | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        extent_az: float | NotGiven = NOT_GIVEN,
        extent_el: float | NotGiven = NOT_GIVEN,
        extent_range: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        frame_rate: float | NotGiven = NOT_GIVEN,
        freq: float | NotGiven = NOT_GIVEN,
        freq_max: float | NotGiven = NOT_GIVEN,
        freq_min: float | NotGiven = NOT_GIVEN,
        id_elset: str | NotGiven = NOT_GIVEN,
        id_manifold: str | NotGiven = NOT_GIVEN,
        id_parent_req: str | NotGiven = NOT_GIVEN,
        id_plan: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_state_vector: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        integration_time: float | NotGiven = NOT_GIVEN,
        iron: int | NotGiven = NOT_GIVEN,
        irradiance: float | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        msg_create_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        msg_type: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_frames: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_tracks: int | NotGiven = NOT_GIVEN,
        ob_type: str | NotGiven = NOT_GIVEN,
        orbit_regime: str | NotGiven = NOT_GIVEN,
        orient_angle: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        plan_index: int | NotGiven = NOT_GIVEN,
        polarization: str | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_max: float | NotGiven = NOT_GIVEN,
        rcs_min: float | NotGiven = NOT_GIVEN,
        reflectance: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        scenario: str | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        spectral_model: str | NotGiven = NOT_GIVEN,
        srch_inc: float | NotGiven = NOT_GIVEN,
        srch_pattern: str | NotGiven = NOT_GIVEN,
        state_vector: collect_request_create_params.StateVector | NotGiven = NOT_GIVEN,
        stop_alt: float | NotGiven = NOT_GIVEN,
        stop_lat: float | NotGiven = NOT_GIVEN,
        stop_lon: float | NotGiven = NOT_GIVEN,
        suffix: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        target_size: float | NotGiven = NOT_GIVEN,
        task_category: int | NotGiven = NOT_GIVEN,
        task_group: str | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        true_anomoly: float | NotGiven = NOT_GIVEN,
        uct_follow_up: bool | NotGiven = NOT_GIVEN,
        vis_mag: float | NotGiven = NOT_GIVEN,
        vis_mag_max: float | NotGiven = NOT_GIVEN,
        vis_mag_min: float | NotGiven = NOT_GIVEN,
        x_angle: float | NotGiven = NOT_GIVEN,
        y_angle: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single CollectRequest as a POST body and ingest into
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

          source: Source of the data.

          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format.

          type: The type of this collect or contact request (DIRECTED SEARCH, DWELL, OBJECT,
              POL, RATE TRACK, SEARCH, SOI, STARE, TTC, VOLUME SEARCH, etc.).

          id: Unique identifier of the record, auto-generated by the system.

          alt: Height above WGS-84 ellipsoid (HAE), in kilometers. If an accompanying stopAlt
              is provided, then alt value can be assumed to be the starting altitude of a
              volume definition.

          arg_of_perigee: The argument of perigee is the angle, in degrees, formed between the perigee and
              the ascending node.

          az: The expected or directed azimuth angle, in degrees, for search or target
              acquisition.

          customer: The customer for this request.

          dec: The expected or directed declination angle, in degrees, for search or target
              acquisition.

          duration: The duration of the collect request, in seconds. If both duration and endTime
              are provided, the endTime is assumed to take precedence.

          dwell_id: The dwell ID associated with this request. A dwell ID is dwell point specific
              and a DWELL request consist of many dwell point requests.

          eccentricity: The orbital eccentricity of an astronomical object is a parameter that
              determines the amount by which its orbit around another body deviates from a
              perfect circle.

          el: The expected or directed elevation angle, in degrees, for search or target
              acquisition.

          elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          end_time: The end time of the collect or contact request window, in ISO 8601 UTC format.
              If no endTime or duration is provided it is assumed the request is either
              ongoing or that the request is for a specified number of tracks (numTracks). If
              both duration and endTime are provided, the endTime is assumed to take
              precedence.

          epoch: Epoch time, in ISO 8601 UTC format, of the orbital elements.

          es_id: ID of the UDL Ephemeris Set of the object associated with this request.

          extent_az: The extent of the azimuth angle, in degrees, from center azimuth to define a
              spatial volume.

          extent_el: The extent of the elevation angle, in degrees, from center elevation to define a
              spatial volume.

          extent_range: The extent of the range, in km, from center range to define a spatial volume.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          frame_rate: For optical sensors, the frame rate of the camera, in Hz.

          freq: The estimated or expected emission frequency of the target, in MHz.

          freq_max: The maximum frequency of interest, in MHz.

          freq_min: The minimum frequency of interest, in MHz. If only minimum frequency is provided
              it is assumed to be minimum reportable frequency.

          id_elset: ID of the UDL Elset of the object associated with this request.

          id_manifold: ID of the UDL Manifold Elset of the object associated with this request. A
              Manifold Elset provides theoretical Keplerian orbital elements belonging to an
              object of interest's manifold describing a possible/theoretical orbit for an
              object of interest for tasking purposes.

          id_parent_req: The unique ID of the collect request record from which this request originated.
              This may be used for cases of sensor-to-sensor tasking, such as tip/cue
              operations.

          id_plan: Unique identifier of the parent plan or schedule associated with this request.
              If null, this request is assumed not associated with a plan or schedule.

          id_sensor: Unique identifier of the requested/scheduled/planned sensor associated with this
              request. If both idSensor and origSensorId are null then the request is assumed
              to be a general request for observations or contact on an object, if specified,
              or an area/volume. In this case, the requester may specify a desired obType.

          id_state_vector: ID of the UDL State Vector of the object or central vector associated with this
              request.

          inclination: The angle, in degrees, between the equator and the orbit plane when looking from
              the center of the Earth. Inclination ranges from 0-180 degrees, with 0-90
              representing posigrade orbits and 90-180 representing retrograde orbits.

          integration_time: For optical sensors, the integration time per camera frame, in milliseconds.

          iron: Inter-Range Operations Number. Four-digit identifier used to schedule and
              identify AFSCN contact support for booster, launch, and on-orbit operations.

          irradiance: The target object irradiance value.

          lat: WGS-84 latitude, in degrees. -90 to 90 degrees (negative values south of
              equator). If an accompanying stopLat is provided, then the lat value can be
              assumed to be the starting latitude of a volume definition.

          lon: WGS-84 longitude, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian). If an accompanying stopLon is provided, then lon value can be assumed
              to be the starting longitude of a volume definition.

          msg_create_date: The timestamp of the external message from which this request originated, if
              applicable, in ISO8601 UTC format with millisecond precision.

          msg_type: The type of external message from which this request originated.

          notes: Notes or comments associated with this request.

          num_frames: For optical sensors, the requested number of frames to capture at each sensor
              step.

          num_obs: The number of requested observations on the target.

          num_tracks: The number of requested tracks on the target. If numTracks is not provided it is
              assumed to indicate all possible observations every pass over the request
              duration or within the request start/end window.

          ob_type: Optional type of observation (EO, IR, RADAR, RF-ACTIVE, RF-PASSIVE, OTHER)
              requested. This field may correspond to a request of a specific sensor, or to a
              general non sensor specific request.

          orbit_regime: The orbit regime of the target (GEO, HEO, LAUNCH, LEO, MEO, OTHER).

          orient_angle: The magnitude of rotation, in degrees, between the xAngle direction and locally
              defined equinoctial plane. A positive value indicates clockwise rotation about
              the sensor boresight vector.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the data source to indicate the target object of
              this request. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          orig_sensor_id: Optional identifier provided by the source to indicate the sensor identifier
              requested/scheduled/planned for this request. This may be an internal identifier
              and not necessarily a valid sensor ID. If both idSensor and origSensorId are
              null then the request is assumed to be a general request for observations or
              contact on an object, if specified, or an area/volume. In this case, the
              requester may specify a desired obType.

          plan_index: Index number (integer) for records within a collection plan or schedule.

          polarization: The RF polarization (H, LHC, RHC, V).

          priority: The priority of the collect request (EMERGENCY, FLASH, IMMEDIATE, PRIORITY,
              ROUTINE).

          ra: The expected or directed right ascension angle, in degrees, for search or target
              acquisition.

          raan: Right ascension of the ascending node, or RAAN is the angle as measured in
              degrees eastwards (or, as seen from the north, counterclockwise) from the First
              Point of Aries to the ascending node.

          range: The expected acquisition range or defined center range, in km.

          rcs: The Radar Cross-Section of the target, in m^2.

          rcs_max: The maximum Radar Cross-Section of the target, in m^2.

          rcs_min: The minimum Radar Cross-Section of the target, in m^2. If only minimum RCS is
              provided it is assumed to be minimum reportable RCS.

          reflectance: The fraction of solar energy reflected from target.

          sat_no: Satellite/catalog number of the target on-orbit object for this request.

          scenario: Pre-coordinated code, direction, or configuration to be executed by the sensor
              or site for this collect or contact.

          semi_major_axis: The average of the periapsis and apoapsis distances, in kilometers. For circular
              orbits, the semimajor axis is the distance between the centers of the bodies.

          spectral_model: The spectral model used for the irradiance calculation.

          srch_inc: The maximum inclination, in degrees, to be used in search operations.

          srch_pattern: The search pattern to be executed for this request (e.g. PICKET-FENCE, SCAN,
              etc.).

          state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          stop_alt: The stopping HAE WGS-84 height above ellipsoid (HAE), of a volume definition, in
              kilometers. The stopAlt value is only meaningful if a (starting) alt value is
              provided.

          stop_lat: The stopping WGS-84 latitude of a volume definition, in degrees. -90 to 90
              degrees (negative values south of equator). The stopLat value is only meaningful
              if a (starting) lat value is provided.

          stop_lon: The stopping WGS-84 longitude of a volume definition, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian). The stopLon value is only
              meaningful if a (starting) lon value is provided.

          suffix: The (SSN) tasking suffix (A-Z) associated with this request. The suffix defines
              the amount of observational data and the frequency of collection. Note that
              suffix definitions are sensor type specific.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          target_size: The minimum object (diameter) size, in meters, to be reported.

          task_category: The (SSN) tasking category (1-5) associated with this request. The tasking
              category defines the priority of gathering and transmitting the requested
              observational data. Note that category definitions are sensor type specific.

          task_group: The tasking group to which the target object is assigned.

          task_id: Task ID associated with this request. A task ID may be associated with a single
              collect request or may be used to tie together the sub-requests of a full
              collect, for example a DWELL consisting of many dwell points.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          true_anomoly: The true anomaly defines the angular position, in degrees, of the object on it's
              orbital path as measured from the orbit focal point at epoch. The true anomaly
              is referenced from perigee.

          uct_follow_up: Boolean indicating that this collect request is UCT follow-up.

          vis_mag: The estimated or expected visual magnitude of the target, in Magnitudes (M).

          vis_mag_max: The maximum estimated or expected visual magnitude of the target, in Magnitudes
              (M).

          vis_mag_min: The minimum estimated or expected visual magnitude of the target, in Magnitudes
              (M). If only minimum vismag is provided it is assumed to be minimum reportable
              vismag.

          x_angle: The angular distance, in degrees, in the sensor-x direction from scan center
              defined by the central vector. The specification of xAngle and yAngle defines a
              rectangle of width 2*xAngle and height 2*yAngle centered about the central
              vector.

          y_angle: The angular distance, in degrees, in the sensor-y direction from scan center
              defined by the central vector. The specification of xAngle and yAngle defines a
              rectangle of width 2*xAngle and height 2*yAngle centered about the central
              vector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/collectrequest",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "alt": alt,
                    "arg_of_perigee": arg_of_perigee,
                    "az": az,
                    "customer": customer,
                    "dec": dec,
                    "duration": duration,
                    "dwell_id": dwell_id,
                    "eccentricity": eccentricity,
                    "el": el,
                    "elset": elset,
                    "end_time": end_time,
                    "epoch": epoch,
                    "es_id": es_id,
                    "extent_az": extent_az,
                    "extent_el": extent_el,
                    "extent_range": extent_range,
                    "external_id": external_id,
                    "frame_rate": frame_rate,
                    "freq": freq,
                    "freq_max": freq_max,
                    "freq_min": freq_min,
                    "id_elset": id_elset,
                    "id_manifold": id_manifold,
                    "id_parent_req": id_parent_req,
                    "id_plan": id_plan,
                    "id_sensor": id_sensor,
                    "id_state_vector": id_state_vector,
                    "inclination": inclination,
                    "integration_time": integration_time,
                    "iron": iron,
                    "irradiance": irradiance,
                    "lat": lat,
                    "lon": lon,
                    "msg_create_date": msg_create_date,
                    "msg_type": msg_type,
                    "notes": notes,
                    "num_frames": num_frames,
                    "num_obs": num_obs,
                    "num_tracks": num_tracks,
                    "ob_type": ob_type,
                    "orbit_regime": orbit_regime,
                    "orient_angle": orient_angle,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "plan_index": plan_index,
                    "polarization": polarization,
                    "priority": priority,
                    "ra": ra,
                    "raan": raan,
                    "range": range,
                    "rcs": rcs,
                    "rcs_max": rcs_max,
                    "rcs_min": rcs_min,
                    "reflectance": reflectance,
                    "sat_no": sat_no,
                    "scenario": scenario,
                    "semi_major_axis": semi_major_axis,
                    "spectral_model": spectral_model,
                    "srch_inc": srch_inc,
                    "srch_pattern": srch_pattern,
                    "state_vector": state_vector,
                    "stop_alt": stop_alt,
                    "stop_lat": stop_lat,
                    "stop_lon": stop_lon,
                    "suffix": suffix,
                    "tags": tags,
                    "target_size": target_size,
                    "task_category": task_category,
                    "task_group": task_group,
                    "task_id": task_id,
                    "transaction_id": transaction_id,
                    "true_anomoly": true_anomoly,
                    "uct_follow_up": uct_follow_up,
                    "vis_mag": vis_mag,
                    "vis_mag_max": vis_mag_max,
                    "vis_mag_min": vis_mag_min,
                    "x_angle": x_angle,
                    "y_angle": y_angle,
                },
                collect_request_create_params.CollectRequestCreateParams,
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
    ) -> CollectRequestFull:
        """
        Service operation to get a single CollectRequest by its unique ID passed as a
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
            f"/udl/collectrequest/{id}",
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
                    collect_request_retrieve_params.CollectRequestRetrieveParams,
                ),
            ),
            cast_to=CollectRequestFull,
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
    ) -> SyncOffsetPage[CollectRequestAbridged]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/collectrequest",
            page=SyncOffsetPage[CollectRequestAbridged],
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
                    collect_request_list_params.CollectRequestListParams,
                ),
            ),
            model=CollectRequestAbridged,
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
          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/collectrequest/count",
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
                    collect_request_count_params.CollectRequestCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[collect_request_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        CollectRequest as a POST body and ingest into the database. This operation is
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
            "/udl/collectrequest/createBulk",
            body=maybe_transform(body, Iterable[collect_request_create_bulk_params.Body]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/udl/collectrequest/queryhelp",
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
    ) -> CollectRequestTupleResponse:
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

          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/collectrequest/tuple",
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
                    collect_request_tuple_params.CollectRequestTupleParams,
                ),
            ),
            cast_to=CollectRequestTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[collect_request_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of CollectRequest as a POST body and ingest
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
            "/filedrop/udl-collectrequest",
            body=maybe_transform(body, Iterable[collect_request_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCollectRequestsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncCollectRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        source: str,
        start_time: Union[str, datetime],
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        alt: float | NotGiven = NOT_GIVEN,
        arg_of_perigee: float | NotGiven = NOT_GIVEN,
        az: float | NotGiven = NOT_GIVEN,
        customer: str | NotGiven = NOT_GIVEN,
        dec: float | NotGiven = NOT_GIVEN,
        duration: int | NotGiven = NOT_GIVEN,
        dwell_id: str | NotGiven = NOT_GIVEN,
        eccentricity: float | NotGiven = NOT_GIVEN,
        el: float | NotGiven = NOT_GIVEN,
        elset: collect_request_create_params.Elset | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        epoch: Union[str, datetime] | NotGiven = NOT_GIVEN,
        es_id: str | NotGiven = NOT_GIVEN,
        extent_az: float | NotGiven = NOT_GIVEN,
        extent_el: float | NotGiven = NOT_GIVEN,
        extent_range: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        frame_rate: float | NotGiven = NOT_GIVEN,
        freq: float | NotGiven = NOT_GIVEN,
        freq_max: float | NotGiven = NOT_GIVEN,
        freq_min: float | NotGiven = NOT_GIVEN,
        id_elset: str | NotGiven = NOT_GIVEN,
        id_manifold: str | NotGiven = NOT_GIVEN,
        id_parent_req: str | NotGiven = NOT_GIVEN,
        id_plan: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        id_state_vector: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        integration_time: float | NotGiven = NOT_GIVEN,
        iron: int | NotGiven = NOT_GIVEN,
        irradiance: float | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        msg_create_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        msg_type: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_frames: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        num_tracks: int | NotGiven = NOT_GIVEN,
        ob_type: str | NotGiven = NOT_GIVEN,
        orbit_regime: str | NotGiven = NOT_GIVEN,
        orient_angle: float | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        plan_index: int | NotGiven = NOT_GIVEN,
        polarization: str | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        ra: float | NotGiven = NOT_GIVEN,
        raan: float | NotGiven = NOT_GIVEN,
        range: float | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_max: float | NotGiven = NOT_GIVEN,
        rcs_min: float | NotGiven = NOT_GIVEN,
        reflectance: float | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        scenario: str | NotGiven = NOT_GIVEN,
        semi_major_axis: float | NotGiven = NOT_GIVEN,
        spectral_model: str | NotGiven = NOT_GIVEN,
        srch_inc: float | NotGiven = NOT_GIVEN,
        srch_pattern: str | NotGiven = NOT_GIVEN,
        state_vector: collect_request_create_params.StateVector | NotGiven = NOT_GIVEN,
        stop_alt: float | NotGiven = NOT_GIVEN,
        stop_lat: float | NotGiven = NOT_GIVEN,
        stop_lon: float | NotGiven = NOT_GIVEN,
        suffix: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        target_size: float | NotGiven = NOT_GIVEN,
        task_category: int | NotGiven = NOT_GIVEN,
        task_group: str | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        true_anomoly: float | NotGiven = NOT_GIVEN,
        uct_follow_up: bool | NotGiven = NOT_GIVEN,
        vis_mag: float | NotGiven = NOT_GIVEN,
        vis_mag_max: float | NotGiven = NOT_GIVEN,
        vis_mag_min: float | NotGiven = NOT_GIVEN,
        x_angle: float | NotGiven = NOT_GIVEN,
        y_angle: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single CollectRequest as a POST body and ingest into
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

          source: Source of the data.

          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format.

          type: The type of this collect or contact request (DIRECTED SEARCH, DWELL, OBJECT,
              POL, RATE TRACK, SEARCH, SOI, STARE, TTC, VOLUME SEARCH, etc.).

          id: Unique identifier of the record, auto-generated by the system.

          alt: Height above WGS-84 ellipsoid (HAE), in kilometers. If an accompanying stopAlt
              is provided, then alt value can be assumed to be the starting altitude of a
              volume definition.

          arg_of_perigee: The argument of perigee is the angle, in degrees, formed between the perigee and
              the ascending node.

          az: The expected or directed azimuth angle, in degrees, for search or target
              acquisition.

          customer: The customer for this request.

          dec: The expected or directed declination angle, in degrees, for search or target
              acquisition.

          duration: The duration of the collect request, in seconds. If both duration and endTime
              are provided, the endTime is assumed to take precedence.

          dwell_id: The dwell ID associated with this request. A dwell ID is dwell point specific
              and a DWELL request consist of many dwell point requests.

          eccentricity: The orbital eccentricity of an astronomical object is a parameter that
              determines the amount by which its orbit around another body deviates from a
              perfect circle.

          el: The expected or directed elevation angle, in degrees, for search or target
              acquisition.

          elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          end_time: The end time of the collect or contact request window, in ISO 8601 UTC format.
              If no endTime or duration is provided it is assumed the request is either
              ongoing or that the request is for a specified number of tracks (numTracks). If
              both duration and endTime are provided, the endTime is assumed to take
              precedence.

          epoch: Epoch time, in ISO 8601 UTC format, of the orbital elements.

          es_id: ID of the UDL Ephemeris Set of the object associated with this request.

          extent_az: The extent of the azimuth angle, in degrees, from center azimuth to define a
              spatial volume.

          extent_el: The extent of the elevation angle, in degrees, from center elevation to define a
              spatial volume.

          extent_range: The extent of the range, in km, from center range to define a spatial volume.

          external_id: Optional ID from external systems. This field has no meaning within UDL and is
              provided as a convenience for systems that require tracking of an internal
              system generated ID.

          frame_rate: For optical sensors, the frame rate of the camera, in Hz.

          freq: The estimated or expected emission frequency of the target, in MHz.

          freq_max: The maximum frequency of interest, in MHz.

          freq_min: The minimum frequency of interest, in MHz. If only minimum frequency is provided
              it is assumed to be minimum reportable frequency.

          id_elset: ID of the UDL Elset of the object associated with this request.

          id_manifold: ID of the UDL Manifold Elset of the object associated with this request. A
              Manifold Elset provides theoretical Keplerian orbital elements belonging to an
              object of interest's manifold describing a possible/theoretical orbit for an
              object of interest for tasking purposes.

          id_parent_req: The unique ID of the collect request record from which this request originated.
              This may be used for cases of sensor-to-sensor tasking, such as tip/cue
              operations.

          id_plan: Unique identifier of the parent plan or schedule associated with this request.
              If null, this request is assumed not associated with a plan or schedule.

          id_sensor: Unique identifier of the requested/scheduled/planned sensor associated with this
              request. If both idSensor and origSensorId are null then the request is assumed
              to be a general request for observations or contact on an object, if specified,
              or an area/volume. In this case, the requester may specify a desired obType.

          id_state_vector: ID of the UDL State Vector of the object or central vector associated with this
              request.

          inclination: The angle, in degrees, between the equator and the orbit plane when looking from
              the center of the Earth. Inclination ranges from 0-180 degrees, with 0-90
              representing posigrade orbits and 90-180 representing retrograde orbits.

          integration_time: For optical sensors, the integration time per camera frame, in milliseconds.

          iron: Inter-Range Operations Number. Four-digit identifier used to schedule and
              identify AFSCN contact support for booster, launch, and on-orbit operations.

          irradiance: The target object irradiance value.

          lat: WGS-84 latitude, in degrees. -90 to 90 degrees (negative values south of
              equator). If an accompanying stopLat is provided, then the lat value can be
              assumed to be the starting latitude of a volume definition.

          lon: WGS-84 longitude, in degrees. -180 to 180 degrees (negative values west of Prime
              Meridian). If an accompanying stopLon is provided, then lon value can be assumed
              to be the starting longitude of a volume definition.

          msg_create_date: The timestamp of the external message from which this request originated, if
              applicable, in ISO8601 UTC format with millisecond precision.

          msg_type: The type of external message from which this request originated.

          notes: Notes or comments associated with this request.

          num_frames: For optical sensors, the requested number of frames to capture at each sensor
              step.

          num_obs: The number of requested observations on the target.

          num_tracks: The number of requested tracks on the target. If numTracks is not provided it is
              assumed to indicate all possible observations every pass over the request
              duration or within the request start/end window.

          ob_type: Optional type of observation (EO, IR, RADAR, RF-ACTIVE, RF-PASSIVE, OTHER)
              requested. This field may correspond to a request of a specific sensor, or to a
              general non sensor specific request.

          orbit_regime: The orbit regime of the target (GEO, HEO, LAUNCH, LEO, MEO, OTHER).

          orient_angle: The magnitude of rotation, in degrees, between the xAngle direction and locally
              defined equinoctial plane. A positive value indicates clockwise rotation about
              the sensor boresight vector.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Optional identifier provided by the data source to indicate the target object of
              this request. This may be an internal identifier and not necessarily map to a
              valid satellite number.

          orig_sensor_id: Optional identifier provided by the source to indicate the sensor identifier
              requested/scheduled/planned for this request. This may be an internal identifier
              and not necessarily a valid sensor ID. If both idSensor and origSensorId are
              null then the request is assumed to be a general request for observations or
              contact on an object, if specified, or an area/volume. In this case, the
              requester may specify a desired obType.

          plan_index: Index number (integer) for records within a collection plan or schedule.

          polarization: The RF polarization (H, LHC, RHC, V).

          priority: The priority of the collect request (EMERGENCY, FLASH, IMMEDIATE, PRIORITY,
              ROUTINE).

          ra: The expected or directed right ascension angle, in degrees, for search or target
              acquisition.

          raan: Right ascension of the ascending node, or RAAN is the angle as measured in
              degrees eastwards (or, as seen from the north, counterclockwise) from the First
              Point of Aries to the ascending node.

          range: The expected acquisition range or defined center range, in km.

          rcs: The Radar Cross-Section of the target, in m^2.

          rcs_max: The maximum Radar Cross-Section of the target, in m^2.

          rcs_min: The minimum Radar Cross-Section of the target, in m^2. If only minimum RCS is
              provided it is assumed to be minimum reportable RCS.

          reflectance: The fraction of solar energy reflected from target.

          sat_no: Satellite/catalog number of the target on-orbit object for this request.

          scenario: Pre-coordinated code, direction, or configuration to be executed by the sensor
              or site for this collect or contact.

          semi_major_axis: The average of the periapsis and apoapsis distances, in kilometers. For circular
              orbits, the semimajor axis is the distance between the centers of the bodies.

          spectral_model: The spectral model used for the irradiance calculation.

          srch_inc: The maximum inclination, in degrees, to be used in search operations.

          srch_pattern: The search pattern to be executed for this request (e.g. PICKET-FENCE, SCAN,
              etc.).

          state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          stop_alt: The stopping HAE WGS-84 height above ellipsoid (HAE), of a volume definition, in
              kilometers. The stopAlt value is only meaningful if a (starting) alt value is
              provided.

          stop_lat: The stopping WGS-84 latitude of a volume definition, in degrees. -90 to 90
              degrees (negative values south of equator). The stopLat value is only meaningful
              if a (starting) lat value is provided.

          stop_lon: The stopping WGS-84 longitude of a volume definition, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian). The stopLon value is only
              meaningful if a (starting) lon value is provided.

          suffix: The (SSN) tasking suffix (A-Z) associated with this request. The suffix defines
              the amount of observational data and the frequency of collection. Note that
              suffix definitions are sensor type specific.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          target_size: The minimum object (diameter) size, in meters, to be reported.

          task_category: The (SSN) tasking category (1-5) associated with this request. The tasking
              category defines the priority of gathering and transmitting the requested
              observational data. Note that category definitions are sensor type specific.

          task_group: The tasking group to which the target object is assigned.

          task_id: Task ID associated with this request. A task ID may be associated with a single
              collect request or may be used to tie together the sub-requests of a full
              collect, for example a DWELL consisting of many dwell points.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          true_anomoly: The true anomaly defines the angular position, in degrees, of the object on it's
              orbital path as measured from the orbit focal point at epoch. The true anomaly
              is referenced from perigee.

          uct_follow_up: Boolean indicating that this collect request is UCT follow-up.

          vis_mag: The estimated or expected visual magnitude of the target, in Magnitudes (M).

          vis_mag_max: The maximum estimated or expected visual magnitude of the target, in Magnitudes
              (M).

          vis_mag_min: The minimum estimated or expected visual magnitude of the target, in Magnitudes
              (M). If only minimum vismag is provided it is assumed to be minimum reportable
              vismag.

          x_angle: The angular distance, in degrees, in the sensor-x direction from scan center
              defined by the central vector. The specification of xAngle and yAngle defines a
              rectangle of width 2*xAngle and height 2*yAngle centered about the central
              vector.

          y_angle: The angular distance, in degrees, in the sensor-y direction from scan center
              defined by the central vector. The specification of xAngle and yAngle defines a
              rectangle of width 2*xAngle and height 2*yAngle centered about the central
              vector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/collectrequest",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "source": source,
                    "start_time": start_time,
                    "type": type,
                    "id": id,
                    "alt": alt,
                    "arg_of_perigee": arg_of_perigee,
                    "az": az,
                    "customer": customer,
                    "dec": dec,
                    "duration": duration,
                    "dwell_id": dwell_id,
                    "eccentricity": eccentricity,
                    "el": el,
                    "elset": elset,
                    "end_time": end_time,
                    "epoch": epoch,
                    "es_id": es_id,
                    "extent_az": extent_az,
                    "extent_el": extent_el,
                    "extent_range": extent_range,
                    "external_id": external_id,
                    "frame_rate": frame_rate,
                    "freq": freq,
                    "freq_max": freq_max,
                    "freq_min": freq_min,
                    "id_elset": id_elset,
                    "id_manifold": id_manifold,
                    "id_parent_req": id_parent_req,
                    "id_plan": id_plan,
                    "id_sensor": id_sensor,
                    "id_state_vector": id_state_vector,
                    "inclination": inclination,
                    "integration_time": integration_time,
                    "iron": iron,
                    "irradiance": irradiance,
                    "lat": lat,
                    "lon": lon,
                    "msg_create_date": msg_create_date,
                    "msg_type": msg_type,
                    "notes": notes,
                    "num_frames": num_frames,
                    "num_obs": num_obs,
                    "num_tracks": num_tracks,
                    "ob_type": ob_type,
                    "orbit_regime": orbit_regime,
                    "orient_angle": orient_angle,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "plan_index": plan_index,
                    "polarization": polarization,
                    "priority": priority,
                    "ra": ra,
                    "raan": raan,
                    "range": range,
                    "rcs": rcs,
                    "rcs_max": rcs_max,
                    "rcs_min": rcs_min,
                    "reflectance": reflectance,
                    "sat_no": sat_no,
                    "scenario": scenario,
                    "semi_major_axis": semi_major_axis,
                    "spectral_model": spectral_model,
                    "srch_inc": srch_inc,
                    "srch_pattern": srch_pattern,
                    "state_vector": state_vector,
                    "stop_alt": stop_alt,
                    "stop_lat": stop_lat,
                    "stop_lon": stop_lon,
                    "suffix": suffix,
                    "tags": tags,
                    "target_size": target_size,
                    "task_category": task_category,
                    "task_group": task_group,
                    "task_id": task_id,
                    "transaction_id": transaction_id,
                    "true_anomoly": true_anomoly,
                    "uct_follow_up": uct_follow_up,
                    "vis_mag": vis_mag,
                    "vis_mag_max": vis_mag_max,
                    "vis_mag_min": vis_mag_min,
                    "x_angle": x_angle,
                    "y_angle": y_angle,
                },
                collect_request_create_params.CollectRequestCreateParams,
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
    ) -> CollectRequestFull:
        """
        Service operation to get a single CollectRequest by its unique ID passed as a
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
            f"/udl/collectrequest/{id}",
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
                    collect_request_retrieve_params.CollectRequestRetrieveParams,
                ),
            ),
            cast_to=CollectRequestFull,
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
    ) -> AsyncPaginator[CollectRequestAbridged, AsyncOffsetPage[CollectRequestAbridged]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/collectrequest",
            page=AsyncOffsetPage[CollectRequestAbridged],
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
                    collect_request_list_params.CollectRequestListParams,
                ),
            ),
            model=CollectRequestAbridged,
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
          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/collectrequest/count",
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
                    collect_request_count_params.CollectRequestCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[collect_request_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        CollectRequest as a POST body and ingest into the database. This operation is
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
            "/udl/collectrequest/createBulk",
            body=await async_maybe_transform(body, Iterable[collect_request_create_bulk_params.Body]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/udl/collectrequest/queryhelp",
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
    ) -> CollectRequestTupleResponse:
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

          start_time: The start time or earliest time of the collect or contact request window, in ISO
              8601 UTC format. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/collectrequest/tuple",
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
                    collect_request_tuple_params.CollectRequestTupleParams,
                ),
            ),
            cast_to=CollectRequestTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[collect_request_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a list of CollectRequest as a POST body and ingest
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
            "/filedrop/udl-collectrequest",
            body=await async_maybe_transform(body, Iterable[collect_request_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CollectRequestsResourceWithRawResponse:
    def __init__(self, collect_requests: CollectRequestsResource) -> None:
        self._collect_requests = collect_requests

        self.create = to_raw_response_wrapper(
            collect_requests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collect_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            collect_requests.list,
        )
        self.count = to_raw_response_wrapper(
            collect_requests.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            collect_requests.create_bulk,
        )
        self.query_help = to_raw_response_wrapper(
            collect_requests.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            collect_requests.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            collect_requests.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._collect_requests.history)


class AsyncCollectRequestsResourceWithRawResponse:
    def __init__(self, collect_requests: AsyncCollectRequestsResource) -> None:
        self._collect_requests = collect_requests

        self.create = async_to_raw_response_wrapper(
            collect_requests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collect_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            collect_requests.list,
        )
        self.count = async_to_raw_response_wrapper(
            collect_requests.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            collect_requests.create_bulk,
        )
        self.query_help = async_to_raw_response_wrapper(
            collect_requests.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            collect_requests.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            collect_requests.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._collect_requests.history)


class CollectRequestsResourceWithStreamingResponse:
    def __init__(self, collect_requests: CollectRequestsResource) -> None:
        self._collect_requests = collect_requests

        self.create = to_streamed_response_wrapper(
            collect_requests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collect_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            collect_requests.list,
        )
        self.count = to_streamed_response_wrapper(
            collect_requests.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            collect_requests.create_bulk,
        )
        self.query_help = to_streamed_response_wrapper(
            collect_requests.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            collect_requests.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            collect_requests.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._collect_requests.history)


class AsyncCollectRequestsResourceWithStreamingResponse:
    def __init__(self, collect_requests: AsyncCollectRequestsResource) -> None:
        self._collect_requests = collect_requests

        self.create = async_to_streamed_response_wrapper(
            collect_requests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collect_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            collect_requests.list,
        )
        self.count = async_to_streamed_response_wrapper(
            collect_requests.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            collect_requests.create_bulk,
        )
        self.query_help = async_to_streamed_response_wrapper(
            collect_requests.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            collect_requests.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            collect_requests.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._collect_requests.history)
