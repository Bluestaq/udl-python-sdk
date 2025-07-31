# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    onorbitdetail_get_params,
    onorbitdetail_list_params,
    onorbitdetail_create_params,
    onorbitdetail_update_params,
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
from ..types.onorbitdetail_list_response import OnorbitdetailListResponse
from ..types.shared.onorbit_details_full import OnorbitDetailsFull

__all__ = ["OnorbitdetailsResource", "AsyncOnorbitdetailsResource"]


class OnorbitdetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnorbitdetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OnorbitdetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnorbitdetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return OnorbitdetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_on_orbit: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        additional_mass: float | NotGiven = NOT_GIVEN,
        adept_radius: float | NotGiven = NOT_GIVEN,
        bol_delta_v: float | NotGiven = NOT_GIVEN,
        bol_fuel_mass: float | NotGiven = NOT_GIVEN,
        bus_cross_section: float | NotGiven = NOT_GIVEN,
        bus_type: str | NotGiven = NOT_GIVEN,
        cola_radius: float | NotGiven = NOT_GIVEN,
        cross_section: float | NotGiven = NOT_GIVEN,
        current_mass: float | NotGiven = NOT_GIVEN,
        delta_v_unc: float | NotGiven = NOT_GIVEN,
        dep_est_masses: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_mass_uncs: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_names: List[str] | NotGiven = NOT_GIVEN,
        drift_rate: float | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        est_delta_v_duration: float | NotGiven = NOT_GIVEN,
        fuel_remaining: float | NotGiven = NOT_GIVEN,
        geo_slot: float | NotGiven = NOT_GIVEN,
        last_ob_source: str | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_mass_max: float | NotGiven = NOT_GIVEN,
        launch_mass_min: float | NotGiven = NOT_GIVEN,
        maneuverable: bool | NotGiven = NOT_GIVEN,
        max_delta_v: float | NotGiven = NOT_GIVEN,
        max_radius: float | NotGiven = NOT_GIVEN,
        mission_types: List[str] | NotGiven = NOT_GIVEN,
        num_deployable: int | NotGiven = NOT_GIVEN,
        num_mission: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_max: float | NotGiven = NOT_GIVEN,
        rcs_mean: float | NotGiven = NOT_GIVEN,
        rcs_min: float | NotGiven = NOT_GIVEN,
        ref_source: str | NotGiven = NOT_GIVEN,
        solar_array_area: float | NotGiven = NOT_GIVEN,
        total_mass_unc: float | NotGiven = NOT_GIVEN,
        vismag: float | NotGiven = NOT_GIVEN,
        vismag_max: float | NotGiven = NOT_GIVEN,
        vismag_mean: float | NotGiven = NOT_GIVEN,
        vismag_min: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitDetails as a POST body and ingest into
        the database. An OnorbitDetails is a collection of additional characteristics on
        an on-orbit object. A specific role is required to perform this service
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

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          additional_mass: Mass of fuel and disposables at launch time in kilograms.

          adept_radius: The radius used for long-term debris environment projection analyses that is not
              as conservative as COLA Radius, in meters.

          bol_delta_v: The total beginning of life delta V of the spacecraft, in meters per second.

          bol_fuel_mass: Spacecraft beginning of life fuel mass, in orbit, in kilograms.

          bus_cross_section: Average cross sectional area of the bus in meters squared.

          bus_type: Type of the bus on the spacecraft.

          cola_radius: Maximum dimension of the box circumscribing the spacecraft (d = sqrt(a*a + b*b +
              c\\**c) where a is the tip-to-tip dimension, b and c are perpendicular to that.)
              in meters.

          cross_section: Average cross sectional area in meters squared.

          current_mass: The estimated total current mass of the spacecraft, in kilograms.

          delta_v_unc: The 1-sigma uncertainty of the total spacecraft delta V, in meters per second.

          dep_est_masses: Array of the estimated mass of each deployable object, in kilograms. Must
              contain the same number of elements as the value of numDeployable.

          dep_mass_uncs: Array of the 1-sigma uncertainty of the mass for each deployable object, in
              kilograms. Must contain the same number of elements as the value of
              numDeployable.

          dep_names: Array of satellite deployable objects. Must contain the same number of elements
              as the value of numDeployable.

          drift_rate: GEO drift rate, if applicable in degrees per day.

          dry_mass: Spacecraft dry mass (without fuel or disposables) in kilograms.

          est_delta_v_duration: Estimated maximum burn duration for the object, in seconds.

          fuel_remaining: Estimated remaining fuel for the object in kilograms.

          geo_slot: GEO slot if applicable, in degrees. -180 (West of Prime Meridian) to 180 degrees
              (East of Prime Meridian). Prime Meridian is 0.

          last_ob_source: The name of the source who last provided an observation for this idOnOrbit.

          last_ob_time: Time of last reported observation for this object in ISO 8601 UTC with
              microsecond precision.

          launch_mass: Nominal mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_max: Maximum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_min: Minimum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          maneuverable: Boolean indicating whether a spacecraft is maneuverable. Note that a spacecraft
              may have propulsion capability but may not be maneuverable due to lack of fuel,
              anomalous condition, or other operational constraints.

          max_delta_v: Maximum delta V available for this on-orbit spacecraft, in meters per second.

          max_radius: Maximum dimension across the spacecraft (e.g., tip-to-tip across the solar panel
              arrays) in meters.

          mission_types: Array of the type of missions the spacecraft performs. Must contain the same
              number of elements as the value of numMission.

          num_deployable: The number of sub-satellites or deployable objects on the spacecraft.

          num_mission: The number of distinct missions the spacecraft performs.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rcs: Current/latest radar cross section in meters squared.

          rcs_max: Maximum radar cross section in meters squared.

          rcs_mean: Mean radar cross section in meters squared.

          rcs_min: Minimum radar cross section in meters squared.

          ref_source: The reference source, sources, or URL from which the data in this record was
              obtained.

          solar_array_area: Spacecraft deployed area of solar array in meters squared.

          total_mass_unc: The 1-sigma uncertainty of the total spacecraft mass, in kilograms.

          vismag: Current/latest visual magnitude in M.

          vismag_max: Maximum visual magnitude in M.

          vismag_mean: Mean visual magnitude in M.

          vismag_min: Minimum visual magnitude in M.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/onorbitdetails",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "id": id,
                    "additional_mass": additional_mass,
                    "adept_radius": adept_radius,
                    "bol_delta_v": bol_delta_v,
                    "bol_fuel_mass": bol_fuel_mass,
                    "bus_cross_section": bus_cross_section,
                    "bus_type": bus_type,
                    "cola_radius": cola_radius,
                    "cross_section": cross_section,
                    "current_mass": current_mass,
                    "delta_v_unc": delta_v_unc,
                    "dep_est_masses": dep_est_masses,
                    "dep_mass_uncs": dep_mass_uncs,
                    "dep_names": dep_names,
                    "drift_rate": drift_rate,
                    "dry_mass": dry_mass,
                    "est_delta_v_duration": est_delta_v_duration,
                    "fuel_remaining": fuel_remaining,
                    "geo_slot": geo_slot,
                    "last_ob_source": last_ob_source,
                    "last_ob_time": last_ob_time,
                    "launch_mass": launch_mass,
                    "launch_mass_max": launch_mass_max,
                    "launch_mass_min": launch_mass_min,
                    "maneuverable": maneuverable,
                    "max_delta_v": max_delta_v,
                    "max_radius": max_radius,
                    "mission_types": mission_types,
                    "num_deployable": num_deployable,
                    "num_mission": num_mission,
                    "origin": origin,
                    "rcs": rcs,
                    "rcs_max": rcs_max,
                    "rcs_mean": rcs_mean,
                    "rcs_min": rcs_min,
                    "ref_source": ref_source,
                    "solar_array_area": solar_array_area,
                    "total_mass_unc": total_mass_unc,
                    "vismag": vismag,
                    "vismag_max": vismag_max,
                    "vismag_mean": vismag_mean,
                    "vismag_min": vismag_min,
                },
                onorbitdetail_create_params.OnorbitdetailCreateParams,
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
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        additional_mass: float | NotGiven = NOT_GIVEN,
        adept_radius: float | NotGiven = NOT_GIVEN,
        bol_delta_v: float | NotGiven = NOT_GIVEN,
        bol_fuel_mass: float | NotGiven = NOT_GIVEN,
        bus_cross_section: float | NotGiven = NOT_GIVEN,
        bus_type: str | NotGiven = NOT_GIVEN,
        cola_radius: float | NotGiven = NOT_GIVEN,
        cross_section: float | NotGiven = NOT_GIVEN,
        current_mass: float | NotGiven = NOT_GIVEN,
        delta_v_unc: float | NotGiven = NOT_GIVEN,
        dep_est_masses: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_mass_uncs: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_names: List[str] | NotGiven = NOT_GIVEN,
        drift_rate: float | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        est_delta_v_duration: float | NotGiven = NOT_GIVEN,
        fuel_remaining: float | NotGiven = NOT_GIVEN,
        geo_slot: float | NotGiven = NOT_GIVEN,
        last_ob_source: str | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_mass_max: float | NotGiven = NOT_GIVEN,
        launch_mass_min: float | NotGiven = NOT_GIVEN,
        maneuverable: bool | NotGiven = NOT_GIVEN,
        max_delta_v: float | NotGiven = NOT_GIVEN,
        max_radius: float | NotGiven = NOT_GIVEN,
        mission_types: List[str] | NotGiven = NOT_GIVEN,
        num_deployable: int | NotGiven = NOT_GIVEN,
        num_mission: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_max: float | NotGiven = NOT_GIVEN,
        rcs_mean: float | NotGiven = NOT_GIVEN,
        rcs_min: float | NotGiven = NOT_GIVEN,
        ref_source: str | NotGiven = NOT_GIVEN,
        solar_array_area: float | NotGiven = NOT_GIVEN,
        total_mass_unc: float | NotGiven = NOT_GIVEN,
        vismag: float | NotGiven = NOT_GIVEN,
        vismag_max: float | NotGiven = NOT_GIVEN,
        vismag_mean: float | NotGiven = NOT_GIVEN,
        vismag_min: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single OnorbitDetails.

        An OnorbitDetails is a
        collection of additional characteristics on an on-orbit object. A specific role
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

          id_on_orbit: UUID of the parent Onorbit record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          additional_mass: Mass of fuel and disposables at launch time in kilograms.

          adept_radius: The radius used for long-term debris environment projection analyses that is not
              as conservative as COLA Radius, in meters.

          bol_delta_v: The total beginning of life delta V of the spacecraft, in meters per second.

          bol_fuel_mass: Spacecraft beginning of life fuel mass, in orbit, in kilograms.

          bus_cross_section: Average cross sectional area of the bus in meters squared.

          bus_type: Type of the bus on the spacecraft.

          cola_radius: Maximum dimension of the box circumscribing the spacecraft (d = sqrt(a*a + b*b +
              c\\**c) where a is the tip-to-tip dimension, b and c are perpendicular to that.)
              in meters.

          cross_section: Average cross sectional area in meters squared.

          current_mass: The estimated total current mass of the spacecraft, in kilograms.

          delta_v_unc: The 1-sigma uncertainty of the total spacecraft delta V, in meters per second.

          dep_est_masses: Array of the estimated mass of each deployable object, in kilograms. Must
              contain the same number of elements as the value of numDeployable.

          dep_mass_uncs: Array of the 1-sigma uncertainty of the mass for each deployable object, in
              kilograms. Must contain the same number of elements as the value of
              numDeployable.

          dep_names: Array of satellite deployable objects. Must contain the same number of elements
              as the value of numDeployable.

          drift_rate: GEO drift rate, if applicable in degrees per day.

          dry_mass: Spacecraft dry mass (without fuel or disposables) in kilograms.

          est_delta_v_duration: Estimated maximum burn duration for the object, in seconds.

          fuel_remaining: Estimated remaining fuel for the object in kilograms.

          geo_slot: GEO slot if applicable, in degrees. -180 (West of Prime Meridian) to 180 degrees
              (East of Prime Meridian). Prime Meridian is 0.

          last_ob_source: The name of the source who last provided an observation for this idOnOrbit.

          last_ob_time: Time of last reported observation for this object in ISO 8601 UTC with
              microsecond precision.

          launch_mass: Nominal mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_max: Maximum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_min: Minimum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          maneuverable: Boolean indicating whether a spacecraft is maneuverable. Note that a spacecraft
              may have propulsion capability but may not be maneuverable due to lack of fuel,
              anomalous condition, or other operational constraints.

          max_delta_v: Maximum delta V available for this on-orbit spacecraft, in meters per second.

          max_radius: Maximum dimension across the spacecraft (e.g., tip-to-tip across the solar panel
              arrays) in meters.

          mission_types: Array of the type of missions the spacecraft performs. Must contain the same
              number of elements as the value of numMission.

          num_deployable: The number of sub-satellites or deployable objects on the spacecraft.

          num_mission: The number of distinct missions the spacecraft performs.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rcs: Current/latest radar cross section in meters squared.

          rcs_max: Maximum radar cross section in meters squared.

          rcs_mean: Mean radar cross section in meters squared.

          rcs_min: Minimum radar cross section in meters squared.

          ref_source: The reference source, sources, or URL from which the data in this record was
              obtained.

          solar_array_area: Spacecraft deployed area of solar array in meters squared.

          total_mass_unc: The 1-sigma uncertainty of the total spacecraft mass, in kilograms.

          vismag: Current/latest visual magnitude in M.

          vismag_max: Maximum visual magnitude in M.

          vismag_mean: Mean visual magnitude in M.

          vismag_min: Minimum visual magnitude in M.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/onorbitdetails/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "body_id": body_id,
                    "additional_mass": additional_mass,
                    "adept_radius": adept_radius,
                    "bol_delta_v": bol_delta_v,
                    "bol_fuel_mass": bol_fuel_mass,
                    "bus_cross_section": bus_cross_section,
                    "bus_type": bus_type,
                    "cola_radius": cola_radius,
                    "cross_section": cross_section,
                    "current_mass": current_mass,
                    "delta_v_unc": delta_v_unc,
                    "dep_est_masses": dep_est_masses,
                    "dep_mass_uncs": dep_mass_uncs,
                    "dep_names": dep_names,
                    "drift_rate": drift_rate,
                    "dry_mass": dry_mass,
                    "est_delta_v_duration": est_delta_v_duration,
                    "fuel_remaining": fuel_remaining,
                    "geo_slot": geo_slot,
                    "last_ob_source": last_ob_source,
                    "last_ob_time": last_ob_time,
                    "launch_mass": launch_mass,
                    "launch_mass_max": launch_mass_max,
                    "launch_mass_min": launch_mass_min,
                    "maneuverable": maneuverable,
                    "max_delta_v": max_delta_v,
                    "max_radius": max_radius,
                    "mission_types": mission_types,
                    "num_deployable": num_deployable,
                    "num_mission": num_mission,
                    "origin": origin,
                    "rcs": rcs,
                    "rcs_max": rcs_max,
                    "rcs_mean": rcs_mean,
                    "rcs_min": rcs_min,
                    "ref_source": ref_source,
                    "solar_array_area": solar_array_area,
                    "total_mass_unc": total_mass_unc,
                    "vismag": vismag,
                    "vismag_max": vismag_max,
                    "vismag_mean": vismag_mean,
                    "vismag_min": vismag_min,
                },
                onorbitdetail_update_params.OnorbitdetailUpdateParams,
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
    ) -> SyncOffsetPage[OnorbitdetailListResponse]:
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
            "/udl/onorbitdetails",
            page=SyncOffsetPage[OnorbitdetailListResponse],
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
                    onorbitdetail_list_params.OnorbitdetailListParams,
                ),
            ),
            model=OnorbitdetailListResponse,
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
        Service operation to delete a OnorbitDetails object specified by the passed ID
        path parameter. An OnorbitDetails is a collection of additional characteristics
        on an on-orbit object. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/onorbitdetails/{id}",
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
    ) -> OnorbitDetailsFull:
        """
        Service operation to get a single OnorbitDetails record by its unique ID passed
        as a path parameter. An OnorbitDetails is a collection of additional
        characteristics on an on-orbit object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/onorbitdetails/{id}",
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
                    onorbitdetail_get_params.OnorbitdetailGetParams,
                ),
            ),
            cast_to=OnorbitDetailsFull,
        )


class AsyncOnorbitdetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnorbitdetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOnorbitdetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnorbitdetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncOnorbitdetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_on_orbit: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        additional_mass: float | NotGiven = NOT_GIVEN,
        adept_radius: float | NotGiven = NOT_GIVEN,
        bol_delta_v: float | NotGiven = NOT_GIVEN,
        bol_fuel_mass: float | NotGiven = NOT_GIVEN,
        bus_cross_section: float | NotGiven = NOT_GIVEN,
        bus_type: str | NotGiven = NOT_GIVEN,
        cola_radius: float | NotGiven = NOT_GIVEN,
        cross_section: float | NotGiven = NOT_GIVEN,
        current_mass: float | NotGiven = NOT_GIVEN,
        delta_v_unc: float | NotGiven = NOT_GIVEN,
        dep_est_masses: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_mass_uncs: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_names: List[str] | NotGiven = NOT_GIVEN,
        drift_rate: float | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        est_delta_v_duration: float | NotGiven = NOT_GIVEN,
        fuel_remaining: float | NotGiven = NOT_GIVEN,
        geo_slot: float | NotGiven = NOT_GIVEN,
        last_ob_source: str | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_mass_max: float | NotGiven = NOT_GIVEN,
        launch_mass_min: float | NotGiven = NOT_GIVEN,
        maneuverable: bool | NotGiven = NOT_GIVEN,
        max_delta_v: float | NotGiven = NOT_GIVEN,
        max_radius: float | NotGiven = NOT_GIVEN,
        mission_types: List[str] | NotGiven = NOT_GIVEN,
        num_deployable: int | NotGiven = NOT_GIVEN,
        num_mission: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_max: float | NotGiven = NOT_GIVEN,
        rcs_mean: float | NotGiven = NOT_GIVEN,
        rcs_min: float | NotGiven = NOT_GIVEN,
        ref_source: str | NotGiven = NOT_GIVEN,
        solar_array_area: float | NotGiven = NOT_GIVEN,
        total_mass_unc: float | NotGiven = NOT_GIVEN,
        vismag: float | NotGiven = NOT_GIVEN,
        vismag_max: float | NotGiven = NOT_GIVEN,
        vismag_mean: float | NotGiven = NOT_GIVEN,
        vismag_min: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single OnorbitDetails as a POST body and ingest into
        the database. An OnorbitDetails is a collection of additional characteristics on
        an on-orbit object. A specific role is required to perform this service
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

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          additional_mass: Mass of fuel and disposables at launch time in kilograms.

          adept_radius: The radius used for long-term debris environment projection analyses that is not
              as conservative as COLA Radius, in meters.

          bol_delta_v: The total beginning of life delta V of the spacecraft, in meters per second.

          bol_fuel_mass: Spacecraft beginning of life fuel mass, in orbit, in kilograms.

          bus_cross_section: Average cross sectional area of the bus in meters squared.

          bus_type: Type of the bus on the spacecraft.

          cola_radius: Maximum dimension of the box circumscribing the spacecraft (d = sqrt(a*a + b*b +
              c\\**c) where a is the tip-to-tip dimension, b and c are perpendicular to that.)
              in meters.

          cross_section: Average cross sectional area in meters squared.

          current_mass: The estimated total current mass of the spacecraft, in kilograms.

          delta_v_unc: The 1-sigma uncertainty of the total spacecraft delta V, in meters per second.

          dep_est_masses: Array of the estimated mass of each deployable object, in kilograms. Must
              contain the same number of elements as the value of numDeployable.

          dep_mass_uncs: Array of the 1-sigma uncertainty of the mass for each deployable object, in
              kilograms. Must contain the same number of elements as the value of
              numDeployable.

          dep_names: Array of satellite deployable objects. Must contain the same number of elements
              as the value of numDeployable.

          drift_rate: GEO drift rate, if applicable in degrees per day.

          dry_mass: Spacecraft dry mass (without fuel or disposables) in kilograms.

          est_delta_v_duration: Estimated maximum burn duration for the object, in seconds.

          fuel_remaining: Estimated remaining fuel for the object in kilograms.

          geo_slot: GEO slot if applicable, in degrees. -180 (West of Prime Meridian) to 180 degrees
              (East of Prime Meridian). Prime Meridian is 0.

          last_ob_source: The name of the source who last provided an observation for this idOnOrbit.

          last_ob_time: Time of last reported observation for this object in ISO 8601 UTC with
              microsecond precision.

          launch_mass: Nominal mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_max: Maximum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_min: Minimum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          maneuverable: Boolean indicating whether a spacecraft is maneuverable. Note that a spacecraft
              may have propulsion capability but may not be maneuverable due to lack of fuel,
              anomalous condition, or other operational constraints.

          max_delta_v: Maximum delta V available for this on-orbit spacecraft, in meters per second.

          max_radius: Maximum dimension across the spacecraft (e.g., tip-to-tip across the solar panel
              arrays) in meters.

          mission_types: Array of the type of missions the spacecraft performs. Must contain the same
              number of elements as the value of numMission.

          num_deployable: The number of sub-satellites or deployable objects on the spacecraft.

          num_mission: The number of distinct missions the spacecraft performs.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rcs: Current/latest radar cross section in meters squared.

          rcs_max: Maximum radar cross section in meters squared.

          rcs_mean: Mean radar cross section in meters squared.

          rcs_min: Minimum radar cross section in meters squared.

          ref_source: The reference source, sources, or URL from which the data in this record was
              obtained.

          solar_array_area: Spacecraft deployed area of solar array in meters squared.

          total_mass_unc: The 1-sigma uncertainty of the total spacecraft mass, in kilograms.

          vismag: Current/latest visual magnitude in M.

          vismag_max: Maximum visual magnitude in M.

          vismag_mean: Mean visual magnitude in M.

          vismag_min: Minimum visual magnitude in M.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/onorbitdetails",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "id": id,
                    "additional_mass": additional_mass,
                    "adept_radius": adept_radius,
                    "bol_delta_v": bol_delta_v,
                    "bol_fuel_mass": bol_fuel_mass,
                    "bus_cross_section": bus_cross_section,
                    "bus_type": bus_type,
                    "cola_radius": cola_radius,
                    "cross_section": cross_section,
                    "current_mass": current_mass,
                    "delta_v_unc": delta_v_unc,
                    "dep_est_masses": dep_est_masses,
                    "dep_mass_uncs": dep_mass_uncs,
                    "dep_names": dep_names,
                    "drift_rate": drift_rate,
                    "dry_mass": dry_mass,
                    "est_delta_v_duration": est_delta_v_duration,
                    "fuel_remaining": fuel_remaining,
                    "geo_slot": geo_slot,
                    "last_ob_source": last_ob_source,
                    "last_ob_time": last_ob_time,
                    "launch_mass": launch_mass,
                    "launch_mass_max": launch_mass_max,
                    "launch_mass_min": launch_mass_min,
                    "maneuverable": maneuverable,
                    "max_delta_v": max_delta_v,
                    "max_radius": max_radius,
                    "mission_types": mission_types,
                    "num_deployable": num_deployable,
                    "num_mission": num_mission,
                    "origin": origin,
                    "rcs": rcs,
                    "rcs_max": rcs_max,
                    "rcs_mean": rcs_mean,
                    "rcs_min": rcs_min,
                    "ref_source": ref_source,
                    "solar_array_area": solar_array_area,
                    "total_mass_unc": total_mass_unc,
                    "vismag": vismag,
                    "vismag_max": vismag_max,
                    "vismag_mean": vismag_mean,
                    "vismag_min": vismag_min,
                },
                onorbitdetail_create_params.OnorbitdetailCreateParams,
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
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        additional_mass: float | NotGiven = NOT_GIVEN,
        adept_radius: float | NotGiven = NOT_GIVEN,
        bol_delta_v: float | NotGiven = NOT_GIVEN,
        bol_fuel_mass: float | NotGiven = NOT_GIVEN,
        bus_cross_section: float | NotGiven = NOT_GIVEN,
        bus_type: str | NotGiven = NOT_GIVEN,
        cola_radius: float | NotGiven = NOT_GIVEN,
        cross_section: float | NotGiven = NOT_GIVEN,
        current_mass: float | NotGiven = NOT_GIVEN,
        delta_v_unc: float | NotGiven = NOT_GIVEN,
        dep_est_masses: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_mass_uncs: Iterable[float] | NotGiven = NOT_GIVEN,
        dep_names: List[str] | NotGiven = NOT_GIVEN,
        drift_rate: float | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        est_delta_v_duration: float | NotGiven = NOT_GIVEN,
        fuel_remaining: float | NotGiven = NOT_GIVEN,
        geo_slot: float | NotGiven = NOT_GIVEN,
        last_ob_source: str | NotGiven = NOT_GIVEN,
        last_ob_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_mass_max: float | NotGiven = NOT_GIVEN,
        launch_mass_min: float | NotGiven = NOT_GIVEN,
        maneuverable: bool | NotGiven = NOT_GIVEN,
        max_delta_v: float | NotGiven = NOT_GIVEN,
        max_radius: float | NotGiven = NOT_GIVEN,
        mission_types: List[str] | NotGiven = NOT_GIVEN,
        num_deployable: int | NotGiven = NOT_GIVEN,
        num_mission: int | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        rcs: float | NotGiven = NOT_GIVEN,
        rcs_max: float | NotGiven = NOT_GIVEN,
        rcs_mean: float | NotGiven = NOT_GIVEN,
        rcs_min: float | NotGiven = NOT_GIVEN,
        ref_source: str | NotGiven = NOT_GIVEN,
        solar_array_area: float | NotGiven = NOT_GIVEN,
        total_mass_unc: float | NotGiven = NOT_GIVEN,
        vismag: float | NotGiven = NOT_GIVEN,
        vismag_max: float | NotGiven = NOT_GIVEN,
        vismag_mean: float | NotGiven = NOT_GIVEN,
        vismag_min: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single OnorbitDetails.

        An OnorbitDetails is a
        collection of additional characteristics on an on-orbit object. A specific role
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

          id_on_orbit: UUID of the parent Onorbit record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          additional_mass: Mass of fuel and disposables at launch time in kilograms.

          adept_radius: The radius used for long-term debris environment projection analyses that is not
              as conservative as COLA Radius, in meters.

          bol_delta_v: The total beginning of life delta V of the spacecraft, in meters per second.

          bol_fuel_mass: Spacecraft beginning of life fuel mass, in orbit, in kilograms.

          bus_cross_section: Average cross sectional area of the bus in meters squared.

          bus_type: Type of the bus on the spacecraft.

          cola_radius: Maximum dimension of the box circumscribing the spacecraft (d = sqrt(a*a + b*b +
              c\\**c) where a is the tip-to-tip dimension, b and c are perpendicular to that.)
              in meters.

          cross_section: Average cross sectional area in meters squared.

          current_mass: The estimated total current mass of the spacecraft, in kilograms.

          delta_v_unc: The 1-sigma uncertainty of the total spacecraft delta V, in meters per second.

          dep_est_masses: Array of the estimated mass of each deployable object, in kilograms. Must
              contain the same number of elements as the value of numDeployable.

          dep_mass_uncs: Array of the 1-sigma uncertainty of the mass for each deployable object, in
              kilograms. Must contain the same number of elements as the value of
              numDeployable.

          dep_names: Array of satellite deployable objects. Must contain the same number of elements
              as the value of numDeployable.

          drift_rate: GEO drift rate, if applicable in degrees per day.

          dry_mass: Spacecraft dry mass (without fuel or disposables) in kilograms.

          est_delta_v_duration: Estimated maximum burn duration for the object, in seconds.

          fuel_remaining: Estimated remaining fuel for the object in kilograms.

          geo_slot: GEO slot if applicable, in degrees. -180 (West of Prime Meridian) to 180 degrees
              (East of Prime Meridian). Prime Meridian is 0.

          last_ob_source: The name of the source who last provided an observation for this idOnOrbit.

          last_ob_time: Time of last reported observation for this object in ISO 8601 UTC with
              microsecond precision.

          launch_mass: Nominal mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_max: Maximum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          launch_mass_min: Minimum (estimated) mass of spacecraft and fuel at launch time, in kilograms.

          maneuverable: Boolean indicating whether a spacecraft is maneuverable. Note that a spacecraft
              may have propulsion capability but may not be maneuverable due to lack of fuel,
              anomalous condition, or other operational constraints.

          max_delta_v: Maximum delta V available for this on-orbit spacecraft, in meters per second.

          max_radius: Maximum dimension across the spacecraft (e.g., tip-to-tip across the solar panel
              arrays) in meters.

          mission_types: Array of the type of missions the spacecraft performs. Must contain the same
              number of elements as the value of numMission.

          num_deployable: The number of sub-satellites or deployable objects on the spacecraft.

          num_mission: The number of distinct missions the spacecraft performs.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          rcs: Current/latest radar cross section in meters squared.

          rcs_max: Maximum radar cross section in meters squared.

          rcs_mean: Mean radar cross section in meters squared.

          rcs_min: Minimum radar cross section in meters squared.

          ref_source: The reference source, sources, or URL from which the data in this record was
              obtained.

          solar_array_area: Spacecraft deployed area of solar array in meters squared.

          total_mass_unc: The 1-sigma uncertainty of the total spacecraft mass, in kilograms.

          vismag: Current/latest visual magnitude in M.

          vismag_max: Maximum visual magnitude in M.

          vismag_mean: Mean visual magnitude in M.

          vismag_min: Minimum visual magnitude in M.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/onorbitdetails/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_on_orbit": id_on_orbit,
                    "source": source,
                    "body_id": body_id,
                    "additional_mass": additional_mass,
                    "adept_radius": adept_radius,
                    "bol_delta_v": bol_delta_v,
                    "bol_fuel_mass": bol_fuel_mass,
                    "bus_cross_section": bus_cross_section,
                    "bus_type": bus_type,
                    "cola_radius": cola_radius,
                    "cross_section": cross_section,
                    "current_mass": current_mass,
                    "delta_v_unc": delta_v_unc,
                    "dep_est_masses": dep_est_masses,
                    "dep_mass_uncs": dep_mass_uncs,
                    "dep_names": dep_names,
                    "drift_rate": drift_rate,
                    "dry_mass": dry_mass,
                    "est_delta_v_duration": est_delta_v_duration,
                    "fuel_remaining": fuel_remaining,
                    "geo_slot": geo_slot,
                    "last_ob_source": last_ob_source,
                    "last_ob_time": last_ob_time,
                    "launch_mass": launch_mass,
                    "launch_mass_max": launch_mass_max,
                    "launch_mass_min": launch_mass_min,
                    "maneuverable": maneuverable,
                    "max_delta_v": max_delta_v,
                    "max_radius": max_radius,
                    "mission_types": mission_types,
                    "num_deployable": num_deployable,
                    "num_mission": num_mission,
                    "origin": origin,
                    "rcs": rcs,
                    "rcs_max": rcs_max,
                    "rcs_mean": rcs_mean,
                    "rcs_min": rcs_min,
                    "ref_source": ref_source,
                    "solar_array_area": solar_array_area,
                    "total_mass_unc": total_mass_unc,
                    "vismag": vismag,
                    "vismag_max": vismag_max,
                    "vismag_mean": vismag_mean,
                    "vismag_min": vismag_min,
                },
                onorbitdetail_update_params.OnorbitdetailUpdateParams,
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
    ) -> AsyncPaginator[OnorbitdetailListResponse, AsyncOffsetPage[OnorbitdetailListResponse]]:
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
            "/udl/onorbitdetails",
            page=AsyncOffsetPage[OnorbitdetailListResponse],
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
                    onorbitdetail_list_params.OnorbitdetailListParams,
                ),
            ),
            model=OnorbitdetailListResponse,
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
        Service operation to delete a OnorbitDetails object specified by the passed ID
        path parameter. An OnorbitDetails is a collection of additional characteristics
        on an on-orbit object. A specific role is required to perform this service
        operation. Please contact the UDL team for assistance.

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
            f"/udl/onorbitdetails/{id}",
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
    ) -> OnorbitDetailsFull:
        """
        Service operation to get a single OnorbitDetails record by its unique ID passed
        as a path parameter. An OnorbitDetails is a collection of additional
        characteristics on an on-orbit object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/onorbitdetails/{id}",
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
                    onorbitdetail_get_params.OnorbitdetailGetParams,
                ),
            ),
            cast_to=OnorbitDetailsFull,
        )


class OnorbitdetailsResourceWithRawResponse:
    def __init__(self, onorbitdetails: OnorbitdetailsResource) -> None:
        self._onorbitdetails = onorbitdetails

        self.create = to_raw_response_wrapper(
            onorbitdetails.create,
        )
        self.update = to_raw_response_wrapper(
            onorbitdetails.update,
        )
        self.list = to_raw_response_wrapper(
            onorbitdetails.list,
        )
        self.delete = to_raw_response_wrapper(
            onorbitdetails.delete,
        )
        self.get = to_raw_response_wrapper(
            onorbitdetails.get,
        )


class AsyncOnorbitdetailsResourceWithRawResponse:
    def __init__(self, onorbitdetails: AsyncOnorbitdetailsResource) -> None:
        self._onorbitdetails = onorbitdetails

        self.create = async_to_raw_response_wrapper(
            onorbitdetails.create,
        )
        self.update = async_to_raw_response_wrapper(
            onorbitdetails.update,
        )
        self.list = async_to_raw_response_wrapper(
            onorbitdetails.list,
        )
        self.delete = async_to_raw_response_wrapper(
            onorbitdetails.delete,
        )
        self.get = async_to_raw_response_wrapper(
            onorbitdetails.get,
        )


class OnorbitdetailsResourceWithStreamingResponse:
    def __init__(self, onorbitdetails: OnorbitdetailsResource) -> None:
        self._onorbitdetails = onorbitdetails

        self.create = to_streamed_response_wrapper(
            onorbitdetails.create,
        )
        self.update = to_streamed_response_wrapper(
            onorbitdetails.update,
        )
        self.list = to_streamed_response_wrapper(
            onorbitdetails.list,
        )
        self.delete = to_streamed_response_wrapper(
            onorbitdetails.delete,
        )
        self.get = to_streamed_response_wrapper(
            onorbitdetails.get,
        )


class AsyncOnorbitdetailsResourceWithStreamingResponse:
    def __init__(self, onorbitdetails: AsyncOnorbitdetailsResource) -> None:
        self._onorbitdetails = onorbitdetails

        self.create = async_to_streamed_response_wrapper(
            onorbitdetails.create,
        )
        self.update = async_to_streamed_response_wrapper(
            onorbitdetails.update,
        )
        self.list = async_to_streamed_response_wrapper(
            onorbitdetails.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            onorbitdetails.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            onorbitdetails.get,
        )
