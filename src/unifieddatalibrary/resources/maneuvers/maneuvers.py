# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    maneuver_get_params,
    maneuver_list_params,
    maneuver_count_params,
    maneuver_tuple_params,
    maneuver_create_params,
    maneuver_create_bulk_params,
    maneuver_unvalidated_publish_params,
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
from ...types.maneuver_get_response import ManeuverGetResponse
from ...types.maneuver_list_response import ManeuverListResponse
from ...types.maneuver_tuple_response import ManeuverTupleResponse
from ...types.maneuver_queryhelp_response import ManeuverQueryhelpResponse

__all__ = ["ManeuversResource", "AsyncManeuversResource"]


class ManeuversResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ManeuversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ManeuversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManeuversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return ManeuversResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        algorithm: str | NotGiven = NOT_GIVEN,
        characterization: str | NotGiven = NOT_GIVEN,
        characterization_unc: float | NotGiven = NOT_GIVEN,
        cov: Iterable[float] | NotGiven = NOT_GIVEN,
        delta_mass: float | NotGiven = NOT_GIVEN,
        delta_pos: float | NotGiven = NOT_GIVEN,
        delta_pos_u: float | NotGiven = NOT_GIVEN,
        delta_pos_v: float | NotGiven = NOT_GIVEN,
        delta_pos_w: float | NotGiven = NOT_GIVEN,
        delta_vel: float | NotGiven = NOT_GIVEN,
        delta_vel_u: float | NotGiven = NOT_GIVEN,
        delta_vel_v: float | NotGiven = NOT_GIVEN,
        delta_vel_w: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        event_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_id: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        maneuver_unc: float | NotGiven = NOT_GIVEN,
        mnvr_accels: Iterable[float] | NotGiven = NOT_GIVEN,
        mnvr_accel_times: Iterable[float] | NotGiven = NOT_GIVEN,
        mnvr_accel_uncs: Iterable[float] | NotGiven = NOT_GIVEN,
        num_accel_points: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        od_fit_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        post_apogee: float | NotGiven = NOT_GIVEN,
        post_area: float | NotGiven = NOT_GIVEN,
        post_ballistic_coeff: float | NotGiven = NOT_GIVEN,
        post_drift_rate: float | NotGiven = NOT_GIVEN,
        post_eccentricity: float | NotGiven = NOT_GIVEN,
        post_event_elset: maneuver_create_params.PostEventElset | NotGiven = NOT_GIVEN,
        post_event_id_elset: str | NotGiven = NOT_GIVEN,
        post_event_id_state_vector: str | NotGiven = NOT_GIVEN,
        post_event_state_vector: maneuver_create_params.PostEventStateVector | NotGiven = NOT_GIVEN,
        post_geo_longitude: float | NotGiven = NOT_GIVEN,
        post_inclination: float | NotGiven = NOT_GIVEN,
        post_mass: float | NotGiven = NOT_GIVEN,
        post_perigee: float | NotGiven = NOT_GIVEN,
        post_period: float | NotGiven = NOT_GIVEN,
        post_pos_x: float | NotGiven = NOT_GIVEN,
        post_pos_y: float | NotGiven = NOT_GIVEN,
        post_pos_z: float | NotGiven = NOT_GIVEN,
        post_raan: float | NotGiven = NOT_GIVEN,
        post_radiation_press_coeff: float | NotGiven = NOT_GIVEN,
        post_sigma_u: float | NotGiven = NOT_GIVEN,
        post_sigma_v: float | NotGiven = NOT_GIVEN,
        post_sigma_w: float | NotGiven = NOT_GIVEN,
        post_sma: float | NotGiven = NOT_GIVEN,
        post_vel_x: float | NotGiven = NOT_GIVEN,
        post_vel_y: float | NotGiven = NOT_GIVEN,
        post_vel_z: float | NotGiven = NOT_GIVEN,
        pre_apogee: float | NotGiven = NOT_GIVEN,
        pre_ballistic_coeff: float | NotGiven = NOT_GIVEN,
        pre_drift_rate: float | NotGiven = NOT_GIVEN,
        pre_eccentricity: float | NotGiven = NOT_GIVEN,
        pre_event_elset: maneuver_create_params.PreEventElset | NotGiven = NOT_GIVEN,
        pre_event_id_elset: str | NotGiven = NOT_GIVEN,
        pre_event_id_state_vector: str | NotGiven = NOT_GIVEN,
        pre_event_state_vector: maneuver_create_params.PreEventStateVector | NotGiven = NOT_GIVEN,
        pre_geo_longitude: float | NotGiven = NOT_GIVEN,
        pre_inclination: float | NotGiven = NOT_GIVEN,
        pre_perigee: float | NotGiven = NOT_GIVEN,
        pre_period: float | NotGiven = NOT_GIVEN,
        pre_pos_x: float | NotGiven = NOT_GIVEN,
        pre_pos_y: float | NotGiven = NOT_GIVEN,
        pre_pos_z: float | NotGiven = NOT_GIVEN,
        pre_raan: float | NotGiven = NOT_GIVEN,
        pre_radiation_press_coeff: float | NotGiven = NOT_GIVEN,
        pre_sigma_u: float | NotGiven = NOT_GIVEN,
        pre_sigma_v: float | NotGiven = NOT_GIVEN,
        pre_sigma_w: float | NotGiven = NOT_GIVEN,
        pre_sma: float | NotGiven = NOT_GIVEN,
        pre_vel_x: float | NotGiven = NOT_GIVEN,
        pre_vel_y: float | NotGiven = NOT_GIVEN,
        pre_vel_z: float | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sourced_data: List[str] | NotGiven = NOT_GIVEN,
        sourced_data_types: List[Literal["EO", "RADAR", "RF", "DOA", "ELSET", "SV"]] | NotGiven = NOT_GIVEN,
        state_model: str | NotGiven = NOT_GIVEN,
        state_model_version: float | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        total_burn_time: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single maneuver as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          algorithm: Optional algorithm used to produce this record.

          characterization: Optional purpose of the maneuver if known (e.g. North-South Station Keeping,
              East-West Station Keeping, Longitude Shift, Unknown).

          characterization_unc: Uncertainty in the characterization or purpose assessment of this maneuver (0 -
              1).

          cov: Optional maneuver cross-track/radial/in-track covariance array, in meter and
              second based units, in the following order: CR_R, CI_R, CI_I, CC_R, CC_I, CC_C,
              CT_R, CT_I, CT_C, CT_T.

          delta_mass: Difference in mass before and after the maneuver, in kg.

          delta_pos: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors at the maneuver event time.

          delta_pos_u: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors in the direction of the pre-maneuver 'U' unit vector at the maneuver
              event time.

          delta_pos_v: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors in the direction of the pre-maneuver 'V' unit vector at the maneuver
              event time.

          delta_pos_w: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors in the direction of the pre-maneuver 'W' unit vector at the maneuver
              event time.

          delta_vel: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors at the maneuver event time.

          delta_vel_u: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors in the direction of the pre-maneuver 'U' unit vector at the maneuver
              event time.

          delta_vel_v: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors in the direction of the pre-maneuver 'V' unit vector at the maneuver
              event time.

          delta_vel_w: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors in the direction of the pre-maneuver 'W' unit vector at the maneuver
              event time.

          description: Description and notes of the maneuver.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          event_end_time: Maneuver event end time in ISO 8601 UTC with microsecond precision.

          event_id: Optional source-provided identifier for this maneuver event. In the case where
              multiple maneuver records are submitted for the same event, this field can be
              used to tie them together to the same event.

          id_sensor: Optional ID of the sensor that detected this maneuver (for example, if detected
              by passive RF anomalies).

          maneuver_unc: Uncertainty in the occurrence of this maneuver (0 - 1).

          mnvr_accels: Array of estimated acceleration values, in meters per second squared. Number of
              elements must match the numAccelPoints.

          mnvr_accel_times: Array of elapsed times, in seconds from maneuver start time, at which each
              acceleration point is estimated. Number of elements must match the
              numAccelPoints.

          mnvr_accel_uncs: Array of the 1-sigma uncertainties in estimated accelerations, in meters per
              second squared. Number of elements must match the numAccelPoints.

          num_accel_points: The total number of estimated acceleration points during the maneuver.

          num_obs: Number of observations used to generate the maneuver data.

          od_fit_end_time: Maneuver orbit determination fit data end time in ISO 8601 UTC with microsecond
              precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Identifier provided by source to indicate the target on-orbit object performing
              this maneuver. This may be an internal identifier and not necessarily a valid
              satellite number/ID.

          orig_sensor_id: Optional identifier provided by source to indicate the sensor identifier used to
              detect this event. This may be an internal identifier and not necessarily a
              valid sensor ID.

          post_apogee: Post-event spacecraft apogee (measured from Earth center), in kilometers.

          post_area: Estimated area of the object following the maneuver, in meters squared.

          post_ballistic_coeff: Post-event ballistic coefficient. The units of the ballistic coefficient vary
              depending on provider. Users should consult the data provider to verify the
              units of the ballistic coefficient.

          post_drift_rate: Post-event GEO drift rate of the spacecraft, in degrees per day. Negative values
              indicate westward drift.

          post_eccentricity: Post-event spacecraft eccentricity.

          post_event_elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          post_event_id_elset: Optional identifier of the element set for the post-maneuver orbit.

          post_event_id_state_vector: Optional identifier of the state vector for the post-maneuver trajectory of the
              spacecraft.

          post_event_state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          post_geo_longitude: Post-event spacecraft WGS-84 GEO belt longitude, represented as -180 to 180
              degrees (negative values west of Prime Meridian).

          post_inclination: Post-event spacecraft orbital inclination, in degrees. 0-180.

          post_mass: Estimated mass of the object following the maneuver, in kg.

          post_perigee: Post-event spacecraft perigee (measured from Earth center), in kilometers.

          post_period: Post-event spacecraft orbital period, in minutes.

          post_pos_x: Post-event X component of position in ECI space, in km.

          post_pos_y: Post-event Y component of position in ECI space, in km.

          post_pos_z: Post-event Z component of position in ECI space, in km.

          post_raan: Post-event spacecraft Right Ascension of the Ascending Node (RAAN), in degrees.

          post_radiation_press_coeff: Post-event radiation pressure coefficient. The units of the radiation pressure
              coefficient vary depending on provider. Users should consult the data provider
              to verify the units of the radiation pressure coefficient.

          post_sigma_u: Post-event standard deviation, in kilometers, of spacecraft position in the 'U'
              unit vector direction.

          post_sigma_v: Post-event standard deviation, in kilometers, of spacecraft position in the 'V'
              unit vector direction.

          post_sigma_w: Post-event standard deviation, in kilometers, of spacecraft position in the 'W'
              unit vector direction.

          post_sma: Post-event spacecraft Semi-Major Axis (SMA), in kilometers.

          post_vel_x: Post-event X component of velocity in ECI space, in km/sec.

          post_vel_y: Post-event Y component of velocity in ECI space, in km/sec.

          post_vel_z: Post-event Z component of velocity in ECI space, in km/sec.

          pre_apogee: Pre-event spacecraft apogee (measured from Earth center), in kilometers.

          pre_ballistic_coeff: Pre-event ballistic coefficient. The units of the ballistic coefficient vary
              depending on provider. Users should consult the data provider to verify the
              units of the ballistic coefficient.

          pre_drift_rate: Pre-event GEO drift rate of the spacecraft, in degrees per day. Negative values
              indicate westward drift.

          pre_eccentricity: Pre-event spacecraft eccentricity.

          pre_event_elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          pre_event_id_elset: Optional identifier of the element set for the pre-maneuver orbit.

          pre_event_id_state_vector: Optional identifier of the state vector for the pre-maneuver trajectory of the
              spacecraft.

          pre_event_state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          pre_geo_longitude: Pre-event spacecraft WGS-84 GEO belt longitude, represented as -180 to 180
              degrees (negative values west of Prime Meridian).

          pre_inclination: Pre-event spacecraft orbital inclination, in degrees. 0-180.

          pre_perigee: Pre-event spacecraft perigee (measured from Earth center), in kilometers.

          pre_period: Pre-event spacecraft orbital period, in minutes.

          pre_pos_x: Pre-event X component of position in ECI space, in km.

          pre_pos_y: Pre-event Y component of position in ECI space, in km.

          pre_pos_z: Pre-event Z component of position in ECI space, in km.

          pre_raan: Pre-event spacecraft Right Ascension of the Ascending Node (RAAN), in degrees.

          pre_radiation_press_coeff: Pre-event radiation pressure coefficient. The units of the radiation pressure
              coefficient vary depending on provider. Users should consult the data provider
              to verify the units of the radiation pressure coefficient.

          pre_sigma_u: Pre-event standard deviation, in kilometers, of spacecraft position in the 'U'
              unit vector direction.

          pre_sigma_v: Pre-event standard deviation, in kilometers, of spacecraft position in the 'V'
              unit vector direction.

          pre_sigma_w: Pre-event standard deviation, in kilometers, of spacecraft position in the 'W'
              unit vector direction.

          pre_sma: Pre-event spacecraft orbital Semi-Major Axis (SMA), in kilometers.

          pre_vel_x: Pre-event X component of velocity in ECI space, in km/sec.

          pre_vel_y: Pre-event Y component of velocity in ECI space, in km/sec.

          pre_vel_z: Pre-event Z component of velocity in ECI space, in km/sec.

          report_time: The time that the report or alert of this maneuver was generated, in ISO 8601
              UTC format.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          sourced_data: Optional array of UDL data (elsets, state vectors, etc) UUIDs used to build this
              maneuver. See the associated sourcedDataTypes array for the specific types of
              data for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          sourced_data_types: Optional array of UDL data types used to build this maneuver (e.g. EO, RADAR,
              RF, DOA, ELSET, SV). See the associated sourcedData array for the specific UUIDs
              of data for the positionally corresponding data types in this array (the two
              arrays must match in size).

          state_model: Name of the state model used to generate the maneuver data.

          state_model_version: Version of the state model used to generate the maneuver data.

          status: Status of this maneuver (CANCELLED, PLANNED, POSSIBLE, REDACTED, VERIFIED).

              CANCELLED: A previously planned maneuver whose execution was cancelled.

              PLANNED: A maneuver planned to take place at the eventStartTime.

              POSSIBLE: A possible maneuver detected by observation of the spacecraft or by
              evaluation of the spacecraft orbit.

              REDACTED: A redaction of a reported possible maneuver that has been determined
              to have not taken place after further observation/evaluation.

              VERIFIED: A maneuver whose execution has been verified, either by the
              owner/operator or observation/evaluation.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          total_burn_time: The estimated total active burn time of a maneuver, in seconds. This includes
              the sum of all burns in numAccelPoints. Not to be confused with the total
              duration of the maneuver.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this maneuver was unable to be correlated to a known object.
              This flag should only be set to true by data providers after an attempt to
              correlate to an on-orbit object was made and failed. If unable to correlate, the
              'origObjectId' field may be populated with an internal data provider specific
              identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/maneuver",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "source": source,
                    "id": id,
                    "algorithm": algorithm,
                    "characterization": characterization,
                    "characterization_unc": characterization_unc,
                    "cov": cov,
                    "delta_mass": delta_mass,
                    "delta_pos": delta_pos,
                    "delta_pos_u": delta_pos_u,
                    "delta_pos_v": delta_pos_v,
                    "delta_pos_w": delta_pos_w,
                    "delta_vel": delta_vel,
                    "delta_vel_u": delta_vel_u,
                    "delta_vel_v": delta_vel_v,
                    "delta_vel_w": delta_vel_w,
                    "description": description,
                    "descriptor": descriptor,
                    "event_end_time": event_end_time,
                    "event_id": event_id,
                    "id_sensor": id_sensor,
                    "maneuver_unc": maneuver_unc,
                    "mnvr_accels": mnvr_accels,
                    "mnvr_accel_times": mnvr_accel_times,
                    "mnvr_accel_uncs": mnvr_accel_uncs,
                    "num_accel_points": num_accel_points,
                    "num_obs": num_obs,
                    "od_fit_end_time": od_fit_end_time,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "post_apogee": post_apogee,
                    "post_area": post_area,
                    "post_ballistic_coeff": post_ballistic_coeff,
                    "post_drift_rate": post_drift_rate,
                    "post_eccentricity": post_eccentricity,
                    "post_event_elset": post_event_elset,
                    "post_event_id_elset": post_event_id_elset,
                    "post_event_id_state_vector": post_event_id_state_vector,
                    "post_event_state_vector": post_event_state_vector,
                    "post_geo_longitude": post_geo_longitude,
                    "post_inclination": post_inclination,
                    "post_mass": post_mass,
                    "post_perigee": post_perigee,
                    "post_period": post_period,
                    "post_pos_x": post_pos_x,
                    "post_pos_y": post_pos_y,
                    "post_pos_z": post_pos_z,
                    "post_raan": post_raan,
                    "post_radiation_press_coeff": post_radiation_press_coeff,
                    "post_sigma_u": post_sigma_u,
                    "post_sigma_v": post_sigma_v,
                    "post_sigma_w": post_sigma_w,
                    "post_sma": post_sma,
                    "post_vel_x": post_vel_x,
                    "post_vel_y": post_vel_y,
                    "post_vel_z": post_vel_z,
                    "pre_apogee": pre_apogee,
                    "pre_ballistic_coeff": pre_ballistic_coeff,
                    "pre_drift_rate": pre_drift_rate,
                    "pre_eccentricity": pre_eccentricity,
                    "pre_event_elset": pre_event_elset,
                    "pre_event_id_elset": pre_event_id_elset,
                    "pre_event_id_state_vector": pre_event_id_state_vector,
                    "pre_event_state_vector": pre_event_state_vector,
                    "pre_geo_longitude": pre_geo_longitude,
                    "pre_inclination": pre_inclination,
                    "pre_perigee": pre_perigee,
                    "pre_period": pre_period,
                    "pre_pos_x": pre_pos_x,
                    "pre_pos_y": pre_pos_y,
                    "pre_pos_z": pre_pos_z,
                    "pre_raan": pre_raan,
                    "pre_radiation_press_coeff": pre_radiation_press_coeff,
                    "pre_sigma_u": pre_sigma_u,
                    "pre_sigma_v": pre_sigma_v,
                    "pre_sigma_w": pre_sigma_w,
                    "pre_sma": pre_sma,
                    "pre_vel_x": pre_vel_x,
                    "pre_vel_y": pre_vel_y,
                    "pre_vel_z": pre_vel_z,
                    "report_time": report_time,
                    "sat_no": sat_no,
                    "sourced_data": sourced_data,
                    "sourced_data_types": sourced_data_types,
                    "state_model": state_model,
                    "state_model_version": state_model_version,
                    "status": status,
                    "tags": tags,
                    "total_burn_time": total_burn_time,
                    "transaction_id": transaction_id,
                    "uct": uct,
                },
                maneuver_create_params.ManeuverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[ManeuverListResponse]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/maneuver",
            page=SyncOffsetPage[ManeuverListResponse],
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
                    maneuver_list_params.ManeuverListParams,
                ),
            ),
            model=ManeuverListResponse,
        )

    def count(
        self,
        *,
        event_start_time: Union[str, datetime],
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
          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/udl/maneuver/count",
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
                    maneuver_count_params.ManeuverCountParams,
                ),
            ),
            cast_to=str,
        )

    def create_bulk(
        self,
        *,
        body: Iterable[maneuver_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        maneuvers as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/maneuver/createBulk",
            body=maybe_transform(body, Iterable[maneuver_create_bulk_params.Body]),
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
    ) -> ManeuverGetResponse:
        """
        Service operation to get a single maneuver by its unique ID passed as a path
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
            f"/udl/maneuver/{id}",
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
                    maneuver_get_params.ManeuverGetParams,
                ),
            ),
            cast_to=ManeuverGetResponse,
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
    ) -> ManeuverQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/maneuver/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManeuverQueryhelpResponse,
        )

    def tuple(
        self,
        *,
        columns: str,
        event_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManeuverTupleResponse:
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

          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/udl/maneuver/tuple",
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
                    maneuver_tuple_params.ManeuverTupleParams,
                ),
            ),
            cast_to=ManeuverTupleResponse,
        )

    def unvalidated_publish(
        self,
        *,
        body: Iterable[maneuver_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple maneuvers as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/filedrop/udl-maneuver",
            body=maybe_transform(body, Iterable[maneuver_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncManeuversResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncManeuversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncManeuversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManeuversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncManeuversResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        event_start_time: Union[str, datetime],
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        algorithm: str | NotGiven = NOT_GIVEN,
        characterization: str | NotGiven = NOT_GIVEN,
        characterization_unc: float | NotGiven = NOT_GIVEN,
        cov: Iterable[float] | NotGiven = NOT_GIVEN,
        delta_mass: float | NotGiven = NOT_GIVEN,
        delta_pos: float | NotGiven = NOT_GIVEN,
        delta_pos_u: float | NotGiven = NOT_GIVEN,
        delta_pos_v: float | NotGiven = NOT_GIVEN,
        delta_pos_w: float | NotGiven = NOT_GIVEN,
        delta_vel: float | NotGiven = NOT_GIVEN,
        delta_vel_u: float | NotGiven = NOT_GIVEN,
        delta_vel_v: float | NotGiven = NOT_GIVEN,
        delta_vel_w: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        event_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event_id: str | NotGiven = NOT_GIVEN,
        id_sensor: str | NotGiven = NOT_GIVEN,
        maneuver_unc: float | NotGiven = NOT_GIVEN,
        mnvr_accels: Iterable[float] | NotGiven = NOT_GIVEN,
        mnvr_accel_times: Iterable[float] | NotGiven = NOT_GIVEN,
        mnvr_accel_uncs: Iterable[float] | NotGiven = NOT_GIVEN,
        num_accel_points: int | NotGiven = NOT_GIVEN,
        num_obs: int | NotGiven = NOT_GIVEN,
        od_fit_end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        orig_object_id: str | NotGiven = NOT_GIVEN,
        orig_sensor_id: str | NotGiven = NOT_GIVEN,
        post_apogee: float | NotGiven = NOT_GIVEN,
        post_area: float | NotGiven = NOT_GIVEN,
        post_ballistic_coeff: float | NotGiven = NOT_GIVEN,
        post_drift_rate: float | NotGiven = NOT_GIVEN,
        post_eccentricity: float | NotGiven = NOT_GIVEN,
        post_event_elset: maneuver_create_params.PostEventElset | NotGiven = NOT_GIVEN,
        post_event_id_elset: str | NotGiven = NOT_GIVEN,
        post_event_id_state_vector: str | NotGiven = NOT_GIVEN,
        post_event_state_vector: maneuver_create_params.PostEventStateVector | NotGiven = NOT_GIVEN,
        post_geo_longitude: float | NotGiven = NOT_GIVEN,
        post_inclination: float | NotGiven = NOT_GIVEN,
        post_mass: float | NotGiven = NOT_GIVEN,
        post_perigee: float | NotGiven = NOT_GIVEN,
        post_period: float | NotGiven = NOT_GIVEN,
        post_pos_x: float | NotGiven = NOT_GIVEN,
        post_pos_y: float | NotGiven = NOT_GIVEN,
        post_pos_z: float | NotGiven = NOT_GIVEN,
        post_raan: float | NotGiven = NOT_GIVEN,
        post_radiation_press_coeff: float | NotGiven = NOT_GIVEN,
        post_sigma_u: float | NotGiven = NOT_GIVEN,
        post_sigma_v: float | NotGiven = NOT_GIVEN,
        post_sigma_w: float | NotGiven = NOT_GIVEN,
        post_sma: float | NotGiven = NOT_GIVEN,
        post_vel_x: float | NotGiven = NOT_GIVEN,
        post_vel_y: float | NotGiven = NOT_GIVEN,
        post_vel_z: float | NotGiven = NOT_GIVEN,
        pre_apogee: float | NotGiven = NOT_GIVEN,
        pre_ballistic_coeff: float | NotGiven = NOT_GIVEN,
        pre_drift_rate: float | NotGiven = NOT_GIVEN,
        pre_eccentricity: float | NotGiven = NOT_GIVEN,
        pre_event_elset: maneuver_create_params.PreEventElset | NotGiven = NOT_GIVEN,
        pre_event_id_elset: str | NotGiven = NOT_GIVEN,
        pre_event_id_state_vector: str | NotGiven = NOT_GIVEN,
        pre_event_state_vector: maneuver_create_params.PreEventStateVector | NotGiven = NOT_GIVEN,
        pre_geo_longitude: float | NotGiven = NOT_GIVEN,
        pre_inclination: float | NotGiven = NOT_GIVEN,
        pre_perigee: float | NotGiven = NOT_GIVEN,
        pre_period: float | NotGiven = NOT_GIVEN,
        pre_pos_x: float | NotGiven = NOT_GIVEN,
        pre_pos_y: float | NotGiven = NOT_GIVEN,
        pre_pos_z: float | NotGiven = NOT_GIVEN,
        pre_raan: float | NotGiven = NOT_GIVEN,
        pre_radiation_press_coeff: float | NotGiven = NOT_GIVEN,
        pre_sigma_u: float | NotGiven = NOT_GIVEN,
        pre_sigma_v: float | NotGiven = NOT_GIVEN,
        pre_sigma_w: float | NotGiven = NOT_GIVEN,
        pre_sma: float | NotGiven = NOT_GIVEN,
        pre_vel_x: float | NotGiven = NOT_GIVEN,
        pre_vel_y: float | NotGiven = NOT_GIVEN,
        pre_vel_z: float | NotGiven = NOT_GIVEN,
        report_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sat_no: int | NotGiven = NOT_GIVEN,
        sourced_data: List[str] | NotGiven = NOT_GIVEN,
        sourced_data_types: List[Literal["EO", "RADAR", "RF", "DOA", "ELSET", "SV"]] | NotGiven = NOT_GIVEN,
        state_model: str | NotGiven = NOT_GIVEN,
        state_model_version: float | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        total_burn_time: float | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        uct: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single maneuver as a POST body and ingest into the
        database. This operation is not intended to be used for automated feeds into
        UDL. Data providers should contact the UDL team for specific role assignments
        and for instructions on setting up a permanent feed through an alternate
        mechanism.

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

          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          algorithm: Optional algorithm used to produce this record.

          characterization: Optional purpose of the maneuver if known (e.g. North-South Station Keeping,
              East-West Station Keeping, Longitude Shift, Unknown).

          characterization_unc: Uncertainty in the characterization or purpose assessment of this maneuver (0 -
              1).

          cov: Optional maneuver cross-track/radial/in-track covariance array, in meter and
              second based units, in the following order: CR_R, CI_R, CI_I, CC_R, CC_I, CC_C,
              CT_R, CT_I, CT_C, CT_T.

          delta_mass: Difference in mass before and after the maneuver, in kg.

          delta_pos: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors at the maneuver event time.

          delta_pos_u: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors in the direction of the pre-maneuver 'U' unit vector at the maneuver
              event time.

          delta_pos_v: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors in the direction of the pre-maneuver 'V' unit vector at the maneuver
              event time.

          delta_pos_w: Magnitude, in km, of the difference in the pre- and post-maneuver position
              vectors in the direction of the pre-maneuver 'W' unit vector at the maneuver
              event time.

          delta_vel: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors at the maneuver event time.

          delta_vel_u: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors in the direction of the pre-maneuver 'U' unit vector at the maneuver
              event time.

          delta_vel_v: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors in the direction of the pre-maneuver 'V' unit vector at the maneuver
              event time.

          delta_vel_w: Magnitude, in km/sec, of the difference in the pre- and post-maneuver velocity
              vectors in the direction of the pre-maneuver 'W' unit vector at the maneuver
              event time.

          description: Description and notes of the maneuver.

          descriptor: Optional source-provided and searchable metadata or descriptor of the data.

          event_end_time: Maneuver event end time in ISO 8601 UTC with microsecond precision.

          event_id: Optional source-provided identifier for this maneuver event. In the case where
              multiple maneuver records are submitted for the same event, this field can be
              used to tie them together to the same event.

          id_sensor: Optional ID of the sensor that detected this maneuver (for example, if detected
              by passive RF anomalies).

          maneuver_unc: Uncertainty in the occurrence of this maneuver (0 - 1).

          mnvr_accels: Array of estimated acceleration values, in meters per second squared. Number of
              elements must match the numAccelPoints.

          mnvr_accel_times: Array of elapsed times, in seconds from maneuver start time, at which each
              acceleration point is estimated. Number of elements must match the
              numAccelPoints.

          mnvr_accel_uncs: Array of the 1-sigma uncertainties in estimated accelerations, in meters per
              second squared. Number of elements must match the numAccelPoints.

          num_accel_points: The total number of estimated acceleration points during the maneuver.

          num_obs: Number of observations used to generate the maneuver data.

          od_fit_end_time: Maneuver orbit determination fit data end time in ISO 8601 UTC with microsecond
              precision.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          orig_object_id: Identifier provided by source to indicate the target on-orbit object performing
              this maneuver. This may be an internal identifier and not necessarily a valid
              satellite number/ID.

          orig_sensor_id: Optional identifier provided by source to indicate the sensor identifier used to
              detect this event. This may be an internal identifier and not necessarily a
              valid sensor ID.

          post_apogee: Post-event spacecraft apogee (measured from Earth center), in kilometers.

          post_area: Estimated area of the object following the maneuver, in meters squared.

          post_ballistic_coeff: Post-event ballistic coefficient. The units of the ballistic coefficient vary
              depending on provider. Users should consult the data provider to verify the
              units of the ballistic coefficient.

          post_drift_rate: Post-event GEO drift rate of the spacecraft, in degrees per day. Negative values
              indicate westward drift.

          post_eccentricity: Post-event spacecraft eccentricity.

          post_event_elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          post_event_id_elset: Optional identifier of the element set for the post-maneuver orbit.

          post_event_id_state_vector: Optional identifier of the state vector for the post-maneuver trajectory of the
              spacecraft.

          post_event_state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          post_geo_longitude: Post-event spacecraft WGS-84 GEO belt longitude, represented as -180 to 180
              degrees (negative values west of Prime Meridian).

          post_inclination: Post-event spacecraft orbital inclination, in degrees. 0-180.

          post_mass: Estimated mass of the object following the maneuver, in kg.

          post_perigee: Post-event spacecraft perigee (measured from Earth center), in kilometers.

          post_period: Post-event spacecraft orbital period, in minutes.

          post_pos_x: Post-event X component of position in ECI space, in km.

          post_pos_y: Post-event Y component of position in ECI space, in km.

          post_pos_z: Post-event Z component of position in ECI space, in km.

          post_raan: Post-event spacecraft Right Ascension of the Ascending Node (RAAN), in degrees.

          post_radiation_press_coeff: Post-event radiation pressure coefficient. The units of the radiation pressure
              coefficient vary depending on provider. Users should consult the data provider
              to verify the units of the radiation pressure coefficient.

          post_sigma_u: Post-event standard deviation, in kilometers, of spacecraft position in the 'U'
              unit vector direction.

          post_sigma_v: Post-event standard deviation, in kilometers, of spacecraft position in the 'V'
              unit vector direction.

          post_sigma_w: Post-event standard deviation, in kilometers, of spacecraft position in the 'W'
              unit vector direction.

          post_sma: Post-event spacecraft Semi-Major Axis (SMA), in kilometers.

          post_vel_x: Post-event X component of velocity in ECI space, in km/sec.

          post_vel_y: Post-event Y component of velocity in ECI space, in km/sec.

          post_vel_z: Post-event Z component of velocity in ECI space, in km/sec.

          pre_apogee: Pre-event spacecraft apogee (measured from Earth center), in kilometers.

          pre_ballistic_coeff: Pre-event ballistic coefficient. The units of the ballistic coefficient vary
              depending on provider. Users should consult the data provider to verify the
              units of the ballistic coefficient.

          pre_drift_rate: Pre-event GEO drift rate of the spacecraft, in degrees per day. Negative values
              indicate westward drift.

          pre_eccentricity: Pre-event spacecraft eccentricity.

          pre_event_elset: An element set is a collection of Keplerian orbital elements describing an orbit
              of a particular satellite. The data is used along with an orbit propagator in
              order to predict the motion of a satellite. The element set, or elset for short,
              consists of identification data, the classical elements and drag parameters.

          pre_event_id_elset: Optional identifier of the element set for the pre-maneuver orbit.

          pre_event_id_state_vector: Optional identifier of the state vector for the pre-maneuver trajectory of the
              spacecraft.

          pre_event_state_vector: This service provides operations for querying and manipulation of state vectors
              for OnOrbit objects. State vectors are cartesian vectors of position (r) and
              velocity (v) that, together with their time (epoch) (t), uniquely determine the
              trajectory of the orbiting body in space. J2000 is the preferred coordinate
              frame for all state vector positions/velocities in UDL, but in some cases data
              may be in another frame depending on the provider and/or datatype. Please see
              the 'Discover' tab in the storefront to confirm coordinate frames by data
              provider.

          pre_geo_longitude: Pre-event spacecraft WGS-84 GEO belt longitude, represented as -180 to 180
              degrees (negative values west of Prime Meridian).

          pre_inclination: Pre-event spacecraft orbital inclination, in degrees. 0-180.

          pre_perigee: Pre-event spacecraft perigee (measured from Earth center), in kilometers.

          pre_period: Pre-event spacecraft orbital period, in minutes.

          pre_pos_x: Pre-event X component of position in ECI space, in km.

          pre_pos_y: Pre-event Y component of position in ECI space, in km.

          pre_pos_z: Pre-event Z component of position in ECI space, in km.

          pre_raan: Pre-event spacecraft Right Ascension of the Ascending Node (RAAN), in degrees.

          pre_radiation_press_coeff: Pre-event radiation pressure coefficient. The units of the radiation pressure
              coefficient vary depending on provider. Users should consult the data provider
              to verify the units of the radiation pressure coefficient.

          pre_sigma_u: Pre-event standard deviation, in kilometers, of spacecraft position in the 'U'
              unit vector direction.

          pre_sigma_v: Pre-event standard deviation, in kilometers, of spacecraft position in the 'V'
              unit vector direction.

          pre_sigma_w: Pre-event standard deviation, in kilometers, of spacecraft position in the 'W'
              unit vector direction.

          pre_sma: Pre-event spacecraft orbital Semi-Major Axis (SMA), in kilometers.

          pre_vel_x: Pre-event X component of velocity in ECI space, in km/sec.

          pre_vel_y: Pre-event Y component of velocity in ECI space, in km/sec.

          pre_vel_z: Pre-event Z component of velocity in ECI space, in km/sec.

          report_time: The time that the report or alert of this maneuver was generated, in ISO 8601
              UTC format.

          sat_no: Satellite/Catalog number of the target on-orbit object.

          sourced_data: Optional array of UDL data (elsets, state vectors, etc) UUIDs used to build this
              maneuver. See the associated sourcedDataTypes array for the specific types of
              data for the positionally corresponding UUIDs in this array (the two arrays must
              match in size).

          sourced_data_types: Optional array of UDL data types used to build this maneuver (e.g. EO, RADAR,
              RF, DOA, ELSET, SV). See the associated sourcedData array for the specific UUIDs
              of data for the positionally corresponding data types in this array (the two
              arrays must match in size).

          state_model: Name of the state model used to generate the maneuver data.

          state_model_version: Version of the state model used to generate the maneuver data.

          status: Status of this maneuver (CANCELLED, PLANNED, POSSIBLE, REDACTED, VERIFIED).

              CANCELLED: A previously planned maneuver whose execution was cancelled.

              PLANNED: A maneuver planned to take place at the eventStartTime.

              POSSIBLE: A possible maneuver detected by observation of the spacecraft or by
              evaluation of the spacecraft orbit.

              REDACTED: A redaction of a reported possible maneuver that has been determined
              to have not taken place after further observation/evaluation.

              VERIFIED: A maneuver whose execution has been verified, either by the
              owner/operator or observation/evaluation.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          total_burn_time: The estimated total active burn time of a maneuver, in seconds. This includes
              the sum of all burns in numAccelPoints. Not to be confused with the total
              duration of the maneuver.

          transaction_id: Optional identifier to track a commercial or marketplace transaction executed to
              produce this data.

          uct: Boolean indicating this maneuver was unable to be correlated to a known object.
              This flag should only be set to true by data providers after an attempt to
              correlate to an on-orbit object was made and failed. If unable to correlate, the
              'origObjectId' field may be populated with an internal data provider specific
              identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/maneuver",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "event_start_time": event_start_time,
                    "source": source,
                    "id": id,
                    "algorithm": algorithm,
                    "characterization": characterization,
                    "characterization_unc": characterization_unc,
                    "cov": cov,
                    "delta_mass": delta_mass,
                    "delta_pos": delta_pos,
                    "delta_pos_u": delta_pos_u,
                    "delta_pos_v": delta_pos_v,
                    "delta_pos_w": delta_pos_w,
                    "delta_vel": delta_vel,
                    "delta_vel_u": delta_vel_u,
                    "delta_vel_v": delta_vel_v,
                    "delta_vel_w": delta_vel_w,
                    "description": description,
                    "descriptor": descriptor,
                    "event_end_time": event_end_time,
                    "event_id": event_id,
                    "id_sensor": id_sensor,
                    "maneuver_unc": maneuver_unc,
                    "mnvr_accels": mnvr_accels,
                    "mnvr_accel_times": mnvr_accel_times,
                    "mnvr_accel_uncs": mnvr_accel_uncs,
                    "num_accel_points": num_accel_points,
                    "num_obs": num_obs,
                    "od_fit_end_time": od_fit_end_time,
                    "origin": origin,
                    "orig_object_id": orig_object_id,
                    "orig_sensor_id": orig_sensor_id,
                    "post_apogee": post_apogee,
                    "post_area": post_area,
                    "post_ballistic_coeff": post_ballistic_coeff,
                    "post_drift_rate": post_drift_rate,
                    "post_eccentricity": post_eccentricity,
                    "post_event_elset": post_event_elset,
                    "post_event_id_elset": post_event_id_elset,
                    "post_event_id_state_vector": post_event_id_state_vector,
                    "post_event_state_vector": post_event_state_vector,
                    "post_geo_longitude": post_geo_longitude,
                    "post_inclination": post_inclination,
                    "post_mass": post_mass,
                    "post_perigee": post_perigee,
                    "post_period": post_period,
                    "post_pos_x": post_pos_x,
                    "post_pos_y": post_pos_y,
                    "post_pos_z": post_pos_z,
                    "post_raan": post_raan,
                    "post_radiation_press_coeff": post_radiation_press_coeff,
                    "post_sigma_u": post_sigma_u,
                    "post_sigma_v": post_sigma_v,
                    "post_sigma_w": post_sigma_w,
                    "post_sma": post_sma,
                    "post_vel_x": post_vel_x,
                    "post_vel_y": post_vel_y,
                    "post_vel_z": post_vel_z,
                    "pre_apogee": pre_apogee,
                    "pre_ballistic_coeff": pre_ballistic_coeff,
                    "pre_drift_rate": pre_drift_rate,
                    "pre_eccentricity": pre_eccentricity,
                    "pre_event_elset": pre_event_elset,
                    "pre_event_id_elset": pre_event_id_elset,
                    "pre_event_id_state_vector": pre_event_id_state_vector,
                    "pre_event_state_vector": pre_event_state_vector,
                    "pre_geo_longitude": pre_geo_longitude,
                    "pre_inclination": pre_inclination,
                    "pre_perigee": pre_perigee,
                    "pre_period": pre_period,
                    "pre_pos_x": pre_pos_x,
                    "pre_pos_y": pre_pos_y,
                    "pre_pos_z": pre_pos_z,
                    "pre_raan": pre_raan,
                    "pre_radiation_press_coeff": pre_radiation_press_coeff,
                    "pre_sigma_u": pre_sigma_u,
                    "pre_sigma_v": pre_sigma_v,
                    "pre_sigma_w": pre_sigma_w,
                    "pre_sma": pre_sma,
                    "pre_vel_x": pre_vel_x,
                    "pre_vel_y": pre_vel_y,
                    "pre_vel_z": pre_vel_z,
                    "report_time": report_time,
                    "sat_no": sat_no,
                    "sourced_data": sourced_data,
                    "sourced_data_types": sourced_data_types,
                    "state_model": state_model,
                    "state_model_version": state_model_version,
                    "status": status,
                    "tags": tags,
                    "total_burn_time": total_burn_time,
                    "transaction_id": transaction_id,
                    "uct": uct,
                },
                maneuver_create_params.ManeuverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        event_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ManeuverListResponse, AsyncOffsetPage[ManeuverListResponse]]:
        """
        Service operation to dynamically query data by a variety of query parameters not
        specified in this API documentation. See the queryhelp operation
        (/udl/&lt;datatype&gt;/queryhelp) for more details on valid/required query
        parameter information.

        Args:
          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/udl/maneuver",
            page=AsyncOffsetPage[ManeuverListResponse],
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
                    maneuver_list_params.ManeuverListParams,
                ),
            ),
            model=ManeuverListResponse,
        )

    async def count(
        self,
        *,
        event_start_time: Union[str, datetime],
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
          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/udl/maneuver/count",
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
                    maneuver_count_params.ManeuverCountParams,
                ),
            ),
            cast_to=str,
        )

    async def create_bulk(
        self,
        *,
        body: Iterable[maneuver_create_bulk_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation intended for initial integration only, to take a list of
        maneuvers as a POST body and ingest into the database. This operation is not
        intended to be used for automated feeds into UDL. Data providers should contact
        the UDL team for specific role assignments and for instructions on setting up a
        permanent feed through an alternate mechanism.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/maneuver/createBulk",
            body=await async_maybe_transform(body, Iterable[maneuver_create_bulk_params.Body]),
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
    ) -> ManeuverGetResponse:
        """
        Service operation to get a single maneuver by its unique ID passed as a path
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
            f"/udl/maneuver/{id}",
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
                    maneuver_get_params.ManeuverGetParams,
                ),
            ),
            cast_to=ManeuverGetResponse,
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
    ) -> ManeuverQueryhelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/maneuver/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManeuverQueryhelpResponse,
        )

    async def tuple(
        self,
        *,
        columns: str,
        event_start_time: Union[str, datetime],
        first_result: int | NotGiven = NOT_GIVEN,
        max_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManeuverTupleResponse:
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

          event_start_time: Maneuver event start time in ISO 8601 UTC with microsecond precision. For
              maneuvers without start and end times, the start time is considered to be the
              maneuver event time. (YYYY-MM-DDTHH:MM:SS.ssssssZ)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/udl/maneuver/tuple",
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
                    maneuver_tuple_params.ManeuverTupleParams,
                ),
            ),
            cast_to=ManeuverTupleResponse,
        )

    async def unvalidated_publish(
        self,
        *,
        body: Iterable[maneuver_unvalidated_publish_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take multiple maneuvers as a POST body and ingest into the
        database. This operation is intended to be used for automated feeds into UDL. A
        specific role is required to perform this service operation. Please contact the
        UDL team for assistance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/filedrop/udl-maneuver",
            body=await async_maybe_transform(body, Iterable[maneuver_unvalidated_publish_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ManeuversResourceWithRawResponse:
    def __init__(self, maneuvers: ManeuversResource) -> None:
        self._maneuvers = maneuvers

        self.create = to_raw_response_wrapper(
            maneuvers.create,
        )
        self.list = to_raw_response_wrapper(
            maneuvers.list,
        )
        self.count = to_raw_response_wrapper(
            maneuvers.count,
        )
        self.create_bulk = to_raw_response_wrapper(
            maneuvers.create_bulk,
        )
        self.get = to_raw_response_wrapper(
            maneuvers.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            maneuvers.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            maneuvers.tuple,
        )
        self.unvalidated_publish = to_raw_response_wrapper(
            maneuvers.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._maneuvers.history)


class AsyncManeuversResourceWithRawResponse:
    def __init__(self, maneuvers: AsyncManeuversResource) -> None:
        self._maneuvers = maneuvers

        self.create = async_to_raw_response_wrapper(
            maneuvers.create,
        )
        self.list = async_to_raw_response_wrapper(
            maneuvers.list,
        )
        self.count = async_to_raw_response_wrapper(
            maneuvers.count,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            maneuvers.create_bulk,
        )
        self.get = async_to_raw_response_wrapper(
            maneuvers.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            maneuvers.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            maneuvers.tuple,
        )
        self.unvalidated_publish = async_to_raw_response_wrapper(
            maneuvers.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._maneuvers.history)


class ManeuversResourceWithStreamingResponse:
    def __init__(self, maneuvers: ManeuversResource) -> None:
        self._maneuvers = maneuvers

        self.create = to_streamed_response_wrapper(
            maneuvers.create,
        )
        self.list = to_streamed_response_wrapper(
            maneuvers.list,
        )
        self.count = to_streamed_response_wrapper(
            maneuvers.count,
        )
        self.create_bulk = to_streamed_response_wrapper(
            maneuvers.create_bulk,
        )
        self.get = to_streamed_response_wrapper(
            maneuvers.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            maneuvers.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            maneuvers.tuple,
        )
        self.unvalidated_publish = to_streamed_response_wrapper(
            maneuvers.unvalidated_publish,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._maneuvers.history)


class AsyncManeuversResourceWithStreamingResponse:
    def __init__(self, maneuvers: AsyncManeuversResource) -> None:
        self._maneuvers = maneuvers

        self.create = async_to_streamed_response_wrapper(
            maneuvers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            maneuvers.list,
        )
        self.count = async_to_streamed_response_wrapper(
            maneuvers.count,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            maneuvers.create_bulk,
        )
        self.get = async_to_streamed_response_wrapper(
            maneuvers.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            maneuvers.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            maneuvers.tuple,
        )
        self.unvalidated_publish = async_to_streamed_response_wrapper(
            maneuvers.unvalidated_publish,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._maneuvers.history)
