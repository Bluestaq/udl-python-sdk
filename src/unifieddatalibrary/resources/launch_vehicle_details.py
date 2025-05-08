# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    launch_vehicle_detail_get_params,
    launch_vehicle_detail_list_params,
    launch_vehicle_detail_create_params,
    launch_vehicle_detail_update_params,
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
from ..types.launch_vehicle_detail_get_response import LaunchVehicleDetailGetResponse
from ..types.launch_vehicle_detail_list_response import LaunchVehicleDetailListResponse

__all__ = ["LaunchVehicleDetailsResource", "AsyncLaunchVehicleDetailsResource"]


class LaunchVehicleDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LaunchVehicleDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LaunchVehicleDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LaunchVehicleDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return LaunchVehicleDetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_launch_vehicle: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        attitude_accuracy: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        deployment_rotation_rate: float | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        est_launch_price: float | NotGiven = NOT_GIVEN,
        est_launch_price_typical: float | NotGiven = NOT_GIVEN,
        fairing_external_diameter: float | NotGiven = NOT_GIVEN,
        fairing_internal_diameter: float | NotGiven = NOT_GIVEN,
        fairing_length: float | NotGiven = NOT_GIVEN,
        fairing_mass: float | NotGiven = NOT_GIVEN,
        fairing_material: str | NotGiven = NOT_GIVEN,
        fairing_name: str | NotGiven = NOT_GIVEN,
        fairing_notes: str | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        geo_payload_mass: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_target: float | NotGiven = NOT_GIVEN,
        gto_payload_mass: float | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_prefix: str | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        leo_payload_mass: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        max_accel_load: float | NotGiven = NOT_GIVEN,
        max_acoustic_level: float | NotGiven = NOT_GIVEN,
        max_acoustic_level_range: float | NotGiven = NOT_GIVEN,
        max_fairing_pressure_change: float | NotGiven = NOT_GIVEN,
        max_flight_shock_force: float | NotGiven = NOT_GIVEN,
        max_flight_shock_freq: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lat: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lon: float | NotGiven = NOT_GIVEN,
        minor_variant: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        oxidizer: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        payload_separation_rate: float | NotGiven = NOT_GIVEN,
        propellant: str | NotGiven = NOT_GIVEN,
        sound_pressure_level: float | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        sso_payload_mass: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single LaunchVehicleDetails as a POST body and
        ingest into the database. LaunchVehicleDetails represents launch vehicle details
        and characteristics, compiled by a particular source. A vehicle may have
        multiple details records from various sources. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          id_launch_vehicle: Identifier of the parent launch vehicle record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          attitude_accuracy: Launch vehicle attitude accuracy (degrees).

          category: Vehicle category.

          deployment_rotation_rate: Launch vehicle deployment rotation rate in RPM.

          diameter: Vehicle diameter in meters.

          est_launch_price: Launch vehicle estimated launch price in US dollars.

          est_launch_price_typical: Launch vehicle typical estimated launch price in US dollars.

          fairing_external_diameter: Vehicle fairing maximum external diameter in meters.

          fairing_internal_diameter: Vehicle fairing maximum internal diameter in meters.

          fairing_length: Vehicle fairing length in meters.

          fairing_mass: Vehicle fairing mass in kg.

          fairing_material: Fairing material.

          fairing_name: Name of the fairing.

          fairing_notes: Notes/Description of the launch vehicle fairing.

          family: Vehicle family.

          geo_payload_mass: Maximum vehicle payload mass to GEO orbit in kg.

          gto_inj3_sig_accuracy_apogee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Margin (degrees).

          gto_inj3_sig_accuracy_apogee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Target (degrees).

          gto_inj3_sig_accuracy_inclination_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Margin (degrees).

          gto_inj3_sig_accuracy_inclination_target: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Target (degrees).

          gto_inj3_sig_accuracy_perigee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Margin (degrees).

          gto_inj3_sig_accuracy_perigee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Target (degrees).

          gto_payload_mass: Max vehicle payload mass to Geo-Transfer Orbit in kg.

          launch_mass: Vehicle total mass at launch time in kg (including all boosters).

          launch_prefix: Vehicle launch prefix.

          length: Vehicle length in meters.

          leo_payload_mass: Max vehicle payload mass to LEO orbit in kg.

          manufacturer_org_id: ID of the organization that manufactures the launch vehicle.

          max_accel_load: Vehicle maximum acceleration load in g.

          max_acoustic_level: Vehicle maximum acoustic level in dB.

          max_acoustic_level_range: Vehicle maximum acoustic level range in Hz.

          max_fairing_pressure_change: Vehicle fairing maximum pressure change in kPa/sec.

          max_flight_shock_force: Vehicle maximum flight shock force in g.

          max_flight_shock_freq: Vehicle maximum flight shock frequency in Hz.

          max_payload_freq_lat: Vehicle maximum payload lateral frequency in Hz.

          max_payload_freq_lon: Vehicle maximum payload longitudinal frequency in Hz.

          minor_variant: Vehicle minor variant.

          notes: Notes/Description of the launch vehicle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          oxidizer: Oxidizer type.

          payload_notes: Notes/Description of the launch vehicle payload.

          payload_separation_rate: Launch vehicle payload separation rate in m/s.

          propellant: Propellant type.

          sound_pressure_level: Vehicle overall sound pressure level in dB.

          source_url: Optional URL for additional information on the vehicle.

          sso_payload_mass: Max vehicle payload mass to Sun-Synchronous Orbit in kg.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          variant: Vehicle variant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/launchvehicledetails",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "id": id,
                    "attitude_accuracy": attitude_accuracy,
                    "category": category,
                    "deployment_rotation_rate": deployment_rotation_rate,
                    "diameter": diameter,
                    "est_launch_price": est_launch_price,
                    "est_launch_price_typical": est_launch_price_typical,
                    "fairing_external_diameter": fairing_external_diameter,
                    "fairing_internal_diameter": fairing_internal_diameter,
                    "fairing_length": fairing_length,
                    "fairing_mass": fairing_mass,
                    "fairing_material": fairing_material,
                    "fairing_name": fairing_name,
                    "fairing_notes": fairing_notes,
                    "family": family,
                    "geo_payload_mass": geo_payload_mass,
                    "gto_inj3_sig_accuracy_apogee_margin": gto_inj3_sig_accuracy_apogee_margin,
                    "gto_inj3_sig_accuracy_apogee_target": gto_inj3_sig_accuracy_apogee_target,
                    "gto_inj3_sig_accuracy_inclination_margin": gto_inj3_sig_accuracy_inclination_margin,
                    "gto_inj3_sig_accuracy_inclination_target": gto_inj3_sig_accuracy_inclination_target,
                    "gto_inj3_sig_accuracy_perigee_margin": gto_inj3_sig_accuracy_perigee_margin,
                    "gto_inj3_sig_accuracy_perigee_target": gto_inj3_sig_accuracy_perigee_target,
                    "gto_payload_mass": gto_payload_mass,
                    "launch_mass": launch_mass,
                    "launch_prefix": launch_prefix,
                    "length": length,
                    "leo_payload_mass": leo_payload_mass,
                    "manufacturer_org_id": manufacturer_org_id,
                    "max_accel_load": max_accel_load,
                    "max_acoustic_level": max_acoustic_level,
                    "max_acoustic_level_range": max_acoustic_level_range,
                    "max_fairing_pressure_change": max_fairing_pressure_change,
                    "max_flight_shock_force": max_flight_shock_force,
                    "max_flight_shock_freq": max_flight_shock_freq,
                    "max_payload_freq_lat": max_payload_freq_lat,
                    "max_payload_freq_lon": max_payload_freq_lon,
                    "minor_variant": minor_variant,
                    "notes": notes,
                    "origin": origin,
                    "oxidizer": oxidizer,
                    "payload_notes": payload_notes,
                    "payload_separation_rate": payload_separation_rate,
                    "propellant": propellant,
                    "sound_pressure_level": sound_pressure_level,
                    "source_url": source_url,
                    "sso_payload_mass": sso_payload_mass,
                    "tags": tags,
                    "variant": variant,
                },
                launch_vehicle_detail_create_params.LaunchVehicleDetailCreateParams,
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
        id_launch_vehicle: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        attitude_accuracy: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        deployment_rotation_rate: float | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        est_launch_price: float | NotGiven = NOT_GIVEN,
        est_launch_price_typical: float | NotGiven = NOT_GIVEN,
        fairing_external_diameter: float | NotGiven = NOT_GIVEN,
        fairing_internal_diameter: float | NotGiven = NOT_GIVEN,
        fairing_length: float | NotGiven = NOT_GIVEN,
        fairing_mass: float | NotGiven = NOT_GIVEN,
        fairing_material: str | NotGiven = NOT_GIVEN,
        fairing_name: str | NotGiven = NOT_GIVEN,
        fairing_notes: str | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        geo_payload_mass: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_target: float | NotGiven = NOT_GIVEN,
        gto_payload_mass: float | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_prefix: str | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        leo_payload_mass: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        max_accel_load: float | NotGiven = NOT_GIVEN,
        max_acoustic_level: float | NotGiven = NOT_GIVEN,
        max_acoustic_level_range: float | NotGiven = NOT_GIVEN,
        max_fairing_pressure_change: float | NotGiven = NOT_GIVEN,
        max_flight_shock_force: float | NotGiven = NOT_GIVEN,
        max_flight_shock_freq: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lat: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lon: float | NotGiven = NOT_GIVEN,
        minor_variant: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        oxidizer: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        payload_separation_rate: float | NotGiven = NOT_GIVEN,
        propellant: str | NotGiven = NOT_GIVEN,
        sound_pressure_level: float | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        sso_payload_mass: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single LaunchVehicleDetails.

        LaunchVehicleDetails
        represents launch vehicle details and characteristics, compiled by a particular
        source. A vehicle may have multiple details records from various sources. A
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

          id_launch_vehicle: Identifier of the parent launch vehicle record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          attitude_accuracy: Launch vehicle attitude accuracy (degrees).

          category: Vehicle category.

          deployment_rotation_rate: Launch vehicle deployment rotation rate in RPM.

          diameter: Vehicle diameter in meters.

          est_launch_price: Launch vehicle estimated launch price in US dollars.

          est_launch_price_typical: Launch vehicle typical estimated launch price in US dollars.

          fairing_external_diameter: Vehicle fairing maximum external diameter in meters.

          fairing_internal_diameter: Vehicle fairing maximum internal diameter in meters.

          fairing_length: Vehicle fairing length in meters.

          fairing_mass: Vehicle fairing mass in kg.

          fairing_material: Fairing material.

          fairing_name: Name of the fairing.

          fairing_notes: Notes/Description of the launch vehicle fairing.

          family: Vehicle family.

          geo_payload_mass: Maximum vehicle payload mass to GEO orbit in kg.

          gto_inj3_sig_accuracy_apogee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Margin (degrees).

          gto_inj3_sig_accuracy_apogee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Target (degrees).

          gto_inj3_sig_accuracy_inclination_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Margin (degrees).

          gto_inj3_sig_accuracy_inclination_target: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Target (degrees).

          gto_inj3_sig_accuracy_perigee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Margin (degrees).

          gto_inj3_sig_accuracy_perigee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Target (degrees).

          gto_payload_mass: Max vehicle payload mass to Geo-Transfer Orbit in kg.

          launch_mass: Vehicle total mass at launch time in kg (including all boosters).

          launch_prefix: Vehicle launch prefix.

          length: Vehicle length in meters.

          leo_payload_mass: Max vehicle payload mass to LEO orbit in kg.

          manufacturer_org_id: ID of the organization that manufactures the launch vehicle.

          max_accel_load: Vehicle maximum acceleration load in g.

          max_acoustic_level: Vehicle maximum acoustic level in dB.

          max_acoustic_level_range: Vehicle maximum acoustic level range in Hz.

          max_fairing_pressure_change: Vehicle fairing maximum pressure change in kPa/sec.

          max_flight_shock_force: Vehicle maximum flight shock force in g.

          max_flight_shock_freq: Vehicle maximum flight shock frequency in Hz.

          max_payload_freq_lat: Vehicle maximum payload lateral frequency in Hz.

          max_payload_freq_lon: Vehicle maximum payload longitudinal frequency in Hz.

          minor_variant: Vehicle minor variant.

          notes: Notes/Description of the launch vehicle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          oxidizer: Oxidizer type.

          payload_notes: Notes/Description of the launch vehicle payload.

          payload_separation_rate: Launch vehicle payload separation rate in m/s.

          propellant: Propellant type.

          sound_pressure_level: Vehicle overall sound pressure level in dB.

          source_url: Optional URL for additional information on the vehicle.

          sso_payload_mass: Max vehicle payload mass to Sun-Synchronous Orbit in kg.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          variant: Vehicle variant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/launchvehicledetails/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "body_id": body_id,
                    "attitude_accuracy": attitude_accuracy,
                    "category": category,
                    "deployment_rotation_rate": deployment_rotation_rate,
                    "diameter": diameter,
                    "est_launch_price": est_launch_price,
                    "est_launch_price_typical": est_launch_price_typical,
                    "fairing_external_diameter": fairing_external_diameter,
                    "fairing_internal_diameter": fairing_internal_diameter,
                    "fairing_length": fairing_length,
                    "fairing_mass": fairing_mass,
                    "fairing_material": fairing_material,
                    "fairing_name": fairing_name,
                    "fairing_notes": fairing_notes,
                    "family": family,
                    "geo_payload_mass": geo_payload_mass,
                    "gto_inj3_sig_accuracy_apogee_margin": gto_inj3_sig_accuracy_apogee_margin,
                    "gto_inj3_sig_accuracy_apogee_target": gto_inj3_sig_accuracy_apogee_target,
                    "gto_inj3_sig_accuracy_inclination_margin": gto_inj3_sig_accuracy_inclination_margin,
                    "gto_inj3_sig_accuracy_inclination_target": gto_inj3_sig_accuracy_inclination_target,
                    "gto_inj3_sig_accuracy_perigee_margin": gto_inj3_sig_accuracy_perigee_margin,
                    "gto_inj3_sig_accuracy_perigee_target": gto_inj3_sig_accuracy_perigee_target,
                    "gto_payload_mass": gto_payload_mass,
                    "launch_mass": launch_mass,
                    "launch_prefix": launch_prefix,
                    "length": length,
                    "leo_payload_mass": leo_payload_mass,
                    "manufacturer_org_id": manufacturer_org_id,
                    "max_accel_load": max_accel_load,
                    "max_acoustic_level": max_acoustic_level,
                    "max_acoustic_level_range": max_acoustic_level_range,
                    "max_fairing_pressure_change": max_fairing_pressure_change,
                    "max_flight_shock_force": max_flight_shock_force,
                    "max_flight_shock_freq": max_flight_shock_freq,
                    "max_payload_freq_lat": max_payload_freq_lat,
                    "max_payload_freq_lon": max_payload_freq_lon,
                    "minor_variant": minor_variant,
                    "notes": notes,
                    "origin": origin,
                    "oxidizer": oxidizer,
                    "payload_notes": payload_notes,
                    "payload_separation_rate": payload_separation_rate,
                    "propellant": propellant,
                    "sound_pressure_level": sound_pressure_level,
                    "source_url": source_url,
                    "sso_payload_mass": sso_payload_mass,
                    "tags": tags,
                    "variant": variant,
                },
                launch_vehicle_detail_update_params.LaunchVehicleDetailUpdateParams,
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
    ) -> SyncOffsetPage[LaunchVehicleDetailListResponse]:
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
            "/udl/launchvehicledetails",
            page=SyncOffsetPage[LaunchVehicleDetailListResponse],
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
                    launch_vehicle_detail_list_params.LaunchVehicleDetailListParams,
                ),
            ),
            model=LaunchVehicleDetailListResponse,
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
        Service operation to delete a LaunchVehicleDetails object specified by the
        passed ID path parameter. LaunchVehicleDetails represents launch vehicle details
        and characteristics, compiled by a particular source. A vehicle may have
        multiple details records from various sources. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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
            f"/udl/launchvehicledetails/{id}",
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
    ) -> LaunchVehicleDetailGetResponse:
        """
        Service operation to get a single LaunchVehicleDetails record by its unique ID
        passed as a path parameter. LaunchVehicleDetails represents launch vehicle
        details and characteristics, compiled by a particular source. A vehicle may have
        multiple details records from various sources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/udl/launchvehicledetails/{id}",
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
                    launch_vehicle_detail_get_params.LaunchVehicleDetailGetParams,
                ),
            ),
            cast_to=LaunchVehicleDetailGetResponse,
        )


class AsyncLaunchVehicleDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLaunchVehicleDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLaunchVehicleDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLaunchVehicleDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncLaunchVehicleDetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        id_launch_vehicle: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        attitude_accuracy: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        deployment_rotation_rate: float | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        est_launch_price: float | NotGiven = NOT_GIVEN,
        est_launch_price_typical: float | NotGiven = NOT_GIVEN,
        fairing_external_diameter: float | NotGiven = NOT_GIVEN,
        fairing_internal_diameter: float | NotGiven = NOT_GIVEN,
        fairing_length: float | NotGiven = NOT_GIVEN,
        fairing_mass: float | NotGiven = NOT_GIVEN,
        fairing_material: str | NotGiven = NOT_GIVEN,
        fairing_name: str | NotGiven = NOT_GIVEN,
        fairing_notes: str | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        geo_payload_mass: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_target: float | NotGiven = NOT_GIVEN,
        gto_payload_mass: float | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_prefix: str | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        leo_payload_mass: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        max_accel_load: float | NotGiven = NOT_GIVEN,
        max_acoustic_level: float | NotGiven = NOT_GIVEN,
        max_acoustic_level_range: float | NotGiven = NOT_GIVEN,
        max_fairing_pressure_change: float | NotGiven = NOT_GIVEN,
        max_flight_shock_force: float | NotGiven = NOT_GIVEN,
        max_flight_shock_freq: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lat: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lon: float | NotGiven = NOT_GIVEN,
        minor_variant: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        oxidizer: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        payload_separation_rate: float | NotGiven = NOT_GIVEN,
        propellant: str | NotGiven = NOT_GIVEN,
        sound_pressure_level: float | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        sso_payload_mass: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single LaunchVehicleDetails as a POST body and
        ingest into the database. LaunchVehicleDetails represents launch vehicle details
        and characteristics, compiled by a particular source. A vehicle may have
        multiple details records from various sources. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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

          id_launch_vehicle: Identifier of the parent launch vehicle record.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          attitude_accuracy: Launch vehicle attitude accuracy (degrees).

          category: Vehicle category.

          deployment_rotation_rate: Launch vehicle deployment rotation rate in RPM.

          diameter: Vehicle diameter in meters.

          est_launch_price: Launch vehicle estimated launch price in US dollars.

          est_launch_price_typical: Launch vehicle typical estimated launch price in US dollars.

          fairing_external_diameter: Vehicle fairing maximum external diameter in meters.

          fairing_internal_diameter: Vehicle fairing maximum internal diameter in meters.

          fairing_length: Vehicle fairing length in meters.

          fairing_mass: Vehicle fairing mass in kg.

          fairing_material: Fairing material.

          fairing_name: Name of the fairing.

          fairing_notes: Notes/Description of the launch vehicle fairing.

          family: Vehicle family.

          geo_payload_mass: Maximum vehicle payload mass to GEO orbit in kg.

          gto_inj3_sig_accuracy_apogee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Margin (degrees).

          gto_inj3_sig_accuracy_apogee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Target (degrees).

          gto_inj3_sig_accuracy_inclination_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Margin (degrees).

          gto_inj3_sig_accuracy_inclination_target: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Target (degrees).

          gto_inj3_sig_accuracy_perigee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Margin (degrees).

          gto_inj3_sig_accuracy_perigee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Target (degrees).

          gto_payload_mass: Max vehicle payload mass to Geo-Transfer Orbit in kg.

          launch_mass: Vehicle total mass at launch time in kg (including all boosters).

          launch_prefix: Vehicle launch prefix.

          length: Vehicle length in meters.

          leo_payload_mass: Max vehicle payload mass to LEO orbit in kg.

          manufacturer_org_id: ID of the organization that manufactures the launch vehicle.

          max_accel_load: Vehicle maximum acceleration load in g.

          max_acoustic_level: Vehicle maximum acoustic level in dB.

          max_acoustic_level_range: Vehicle maximum acoustic level range in Hz.

          max_fairing_pressure_change: Vehicle fairing maximum pressure change in kPa/sec.

          max_flight_shock_force: Vehicle maximum flight shock force in g.

          max_flight_shock_freq: Vehicle maximum flight shock frequency in Hz.

          max_payload_freq_lat: Vehicle maximum payload lateral frequency in Hz.

          max_payload_freq_lon: Vehicle maximum payload longitudinal frequency in Hz.

          minor_variant: Vehicle minor variant.

          notes: Notes/Description of the launch vehicle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          oxidizer: Oxidizer type.

          payload_notes: Notes/Description of the launch vehicle payload.

          payload_separation_rate: Launch vehicle payload separation rate in m/s.

          propellant: Propellant type.

          sound_pressure_level: Vehicle overall sound pressure level in dB.

          source_url: Optional URL for additional information on the vehicle.

          sso_payload_mass: Max vehicle payload mass to Sun-Synchronous Orbit in kg.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          variant: Vehicle variant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/launchvehicledetails",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "id": id,
                    "attitude_accuracy": attitude_accuracy,
                    "category": category,
                    "deployment_rotation_rate": deployment_rotation_rate,
                    "diameter": diameter,
                    "est_launch_price": est_launch_price,
                    "est_launch_price_typical": est_launch_price_typical,
                    "fairing_external_diameter": fairing_external_diameter,
                    "fairing_internal_diameter": fairing_internal_diameter,
                    "fairing_length": fairing_length,
                    "fairing_mass": fairing_mass,
                    "fairing_material": fairing_material,
                    "fairing_name": fairing_name,
                    "fairing_notes": fairing_notes,
                    "family": family,
                    "geo_payload_mass": geo_payload_mass,
                    "gto_inj3_sig_accuracy_apogee_margin": gto_inj3_sig_accuracy_apogee_margin,
                    "gto_inj3_sig_accuracy_apogee_target": gto_inj3_sig_accuracy_apogee_target,
                    "gto_inj3_sig_accuracy_inclination_margin": gto_inj3_sig_accuracy_inclination_margin,
                    "gto_inj3_sig_accuracy_inclination_target": gto_inj3_sig_accuracy_inclination_target,
                    "gto_inj3_sig_accuracy_perigee_margin": gto_inj3_sig_accuracy_perigee_margin,
                    "gto_inj3_sig_accuracy_perigee_target": gto_inj3_sig_accuracy_perigee_target,
                    "gto_payload_mass": gto_payload_mass,
                    "launch_mass": launch_mass,
                    "launch_prefix": launch_prefix,
                    "length": length,
                    "leo_payload_mass": leo_payload_mass,
                    "manufacturer_org_id": manufacturer_org_id,
                    "max_accel_load": max_accel_load,
                    "max_acoustic_level": max_acoustic_level,
                    "max_acoustic_level_range": max_acoustic_level_range,
                    "max_fairing_pressure_change": max_fairing_pressure_change,
                    "max_flight_shock_force": max_flight_shock_force,
                    "max_flight_shock_freq": max_flight_shock_freq,
                    "max_payload_freq_lat": max_payload_freq_lat,
                    "max_payload_freq_lon": max_payload_freq_lon,
                    "minor_variant": minor_variant,
                    "notes": notes,
                    "origin": origin,
                    "oxidizer": oxidizer,
                    "payload_notes": payload_notes,
                    "payload_separation_rate": payload_separation_rate,
                    "propellant": propellant,
                    "sound_pressure_level": sound_pressure_level,
                    "source_url": source_url,
                    "sso_payload_mass": sso_payload_mass,
                    "tags": tags,
                    "variant": variant,
                },
                launch_vehicle_detail_create_params.LaunchVehicleDetailCreateParams,
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
        id_launch_vehicle: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        attitude_accuracy: float | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        deployment_rotation_rate: float | NotGiven = NOT_GIVEN,
        diameter: float | NotGiven = NOT_GIVEN,
        est_launch_price: float | NotGiven = NOT_GIVEN,
        est_launch_price_typical: float | NotGiven = NOT_GIVEN,
        fairing_external_diameter: float | NotGiven = NOT_GIVEN,
        fairing_internal_diameter: float | NotGiven = NOT_GIVEN,
        fairing_length: float | NotGiven = NOT_GIVEN,
        fairing_mass: float | NotGiven = NOT_GIVEN,
        fairing_material: str | NotGiven = NOT_GIVEN,
        fairing_name: str | NotGiven = NOT_GIVEN,
        fairing_notes: str | NotGiven = NOT_GIVEN,
        family: str | NotGiven = NOT_GIVEN,
        geo_payload_mass: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_apogee_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_inclination_target: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_margin: float | NotGiven = NOT_GIVEN,
        gto_inj3_sig_accuracy_perigee_target: float | NotGiven = NOT_GIVEN,
        gto_payload_mass: float | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_prefix: str | NotGiven = NOT_GIVEN,
        length: float | NotGiven = NOT_GIVEN,
        leo_payload_mass: float | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        max_accel_load: float | NotGiven = NOT_GIVEN,
        max_acoustic_level: float | NotGiven = NOT_GIVEN,
        max_acoustic_level_range: float | NotGiven = NOT_GIVEN,
        max_fairing_pressure_change: float | NotGiven = NOT_GIVEN,
        max_flight_shock_force: float | NotGiven = NOT_GIVEN,
        max_flight_shock_freq: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lat: float | NotGiven = NOT_GIVEN,
        max_payload_freq_lon: float | NotGiven = NOT_GIVEN,
        minor_variant: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        oxidizer: str | NotGiven = NOT_GIVEN,
        payload_notes: str | NotGiven = NOT_GIVEN,
        payload_separation_rate: float | NotGiven = NOT_GIVEN,
        propellant: str | NotGiven = NOT_GIVEN,
        sound_pressure_level: float | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        sso_payload_mass: float | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single LaunchVehicleDetails.

        LaunchVehicleDetails
        represents launch vehicle details and characteristics, compiled by a particular
        source. A vehicle may have multiple details records from various sources. A
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

          id_launch_vehicle: Identifier of the parent launch vehicle record.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          attitude_accuracy: Launch vehicle attitude accuracy (degrees).

          category: Vehicle category.

          deployment_rotation_rate: Launch vehicle deployment rotation rate in RPM.

          diameter: Vehicle diameter in meters.

          est_launch_price: Launch vehicle estimated launch price in US dollars.

          est_launch_price_typical: Launch vehicle typical estimated launch price in US dollars.

          fairing_external_diameter: Vehicle fairing maximum external diameter in meters.

          fairing_internal_diameter: Vehicle fairing maximum internal diameter in meters.

          fairing_length: Vehicle fairing length in meters.

          fairing_mass: Vehicle fairing mass in kg.

          fairing_material: Fairing material.

          fairing_name: Name of the fairing.

          fairing_notes: Notes/Description of the launch vehicle fairing.

          family: Vehicle family.

          geo_payload_mass: Maximum vehicle payload mass to GEO orbit in kg.

          gto_inj3_sig_accuracy_apogee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Margin (degrees).

          gto_inj3_sig_accuracy_apogee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Apogee Target (degrees).

          gto_inj3_sig_accuracy_inclination_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Margin (degrees).

          gto_inj3_sig_accuracy_inclination_target: Launch vehicle GTO Injection 3 Sigma Accuracy Inclination Target (degrees).

          gto_inj3_sig_accuracy_perigee_margin: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Margin (degrees).

          gto_inj3_sig_accuracy_perigee_target: Launch vehicle GTO Injection 3 Sigma Accuracy Perigee Target (degrees).

          gto_payload_mass: Max vehicle payload mass to Geo-Transfer Orbit in kg.

          launch_mass: Vehicle total mass at launch time in kg (including all boosters).

          launch_prefix: Vehicle launch prefix.

          length: Vehicle length in meters.

          leo_payload_mass: Max vehicle payload mass to LEO orbit in kg.

          manufacturer_org_id: ID of the organization that manufactures the launch vehicle.

          max_accel_load: Vehicle maximum acceleration load in g.

          max_acoustic_level: Vehicle maximum acoustic level in dB.

          max_acoustic_level_range: Vehicle maximum acoustic level range in Hz.

          max_fairing_pressure_change: Vehicle fairing maximum pressure change in kPa/sec.

          max_flight_shock_force: Vehicle maximum flight shock force in g.

          max_flight_shock_freq: Vehicle maximum flight shock frequency in Hz.

          max_payload_freq_lat: Vehicle maximum payload lateral frequency in Hz.

          max_payload_freq_lon: Vehicle maximum payload longitudinal frequency in Hz.

          minor_variant: Vehicle minor variant.

          notes: Notes/Description of the launch vehicle.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          oxidizer: Oxidizer type.

          payload_notes: Notes/Description of the launch vehicle payload.

          payload_separation_rate: Launch vehicle payload separation rate in m/s.

          propellant: Propellant type.

          sound_pressure_level: Vehicle overall sound pressure level in dB.

          source_url: Optional URL for additional information on the vehicle.

          sso_payload_mass: Max vehicle payload mass to Sun-Synchronous Orbit in kg.

          tags: Optional array of provider/source specific tags for this data, where each
              element is no longer than 32 characters, used for implementing data owner
              conditional access controls to restrict access to the data. Should be left null
              by data providers unless conditional access controls are coordinated with the
              UDL team.

          variant: Vehicle variant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/launchvehicledetails/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "id_launch_vehicle": id_launch_vehicle,
                    "source": source,
                    "body_id": body_id,
                    "attitude_accuracy": attitude_accuracy,
                    "category": category,
                    "deployment_rotation_rate": deployment_rotation_rate,
                    "diameter": diameter,
                    "est_launch_price": est_launch_price,
                    "est_launch_price_typical": est_launch_price_typical,
                    "fairing_external_diameter": fairing_external_diameter,
                    "fairing_internal_diameter": fairing_internal_diameter,
                    "fairing_length": fairing_length,
                    "fairing_mass": fairing_mass,
                    "fairing_material": fairing_material,
                    "fairing_name": fairing_name,
                    "fairing_notes": fairing_notes,
                    "family": family,
                    "geo_payload_mass": geo_payload_mass,
                    "gto_inj3_sig_accuracy_apogee_margin": gto_inj3_sig_accuracy_apogee_margin,
                    "gto_inj3_sig_accuracy_apogee_target": gto_inj3_sig_accuracy_apogee_target,
                    "gto_inj3_sig_accuracy_inclination_margin": gto_inj3_sig_accuracy_inclination_margin,
                    "gto_inj3_sig_accuracy_inclination_target": gto_inj3_sig_accuracy_inclination_target,
                    "gto_inj3_sig_accuracy_perigee_margin": gto_inj3_sig_accuracy_perigee_margin,
                    "gto_inj3_sig_accuracy_perigee_target": gto_inj3_sig_accuracy_perigee_target,
                    "gto_payload_mass": gto_payload_mass,
                    "launch_mass": launch_mass,
                    "launch_prefix": launch_prefix,
                    "length": length,
                    "leo_payload_mass": leo_payload_mass,
                    "manufacturer_org_id": manufacturer_org_id,
                    "max_accel_load": max_accel_load,
                    "max_acoustic_level": max_acoustic_level,
                    "max_acoustic_level_range": max_acoustic_level_range,
                    "max_fairing_pressure_change": max_fairing_pressure_change,
                    "max_flight_shock_force": max_flight_shock_force,
                    "max_flight_shock_freq": max_flight_shock_freq,
                    "max_payload_freq_lat": max_payload_freq_lat,
                    "max_payload_freq_lon": max_payload_freq_lon,
                    "minor_variant": minor_variant,
                    "notes": notes,
                    "origin": origin,
                    "oxidizer": oxidizer,
                    "payload_notes": payload_notes,
                    "payload_separation_rate": payload_separation_rate,
                    "propellant": propellant,
                    "sound_pressure_level": sound_pressure_level,
                    "source_url": source_url,
                    "sso_payload_mass": sso_payload_mass,
                    "tags": tags,
                    "variant": variant,
                },
                launch_vehicle_detail_update_params.LaunchVehicleDetailUpdateParams,
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
    ) -> AsyncPaginator[LaunchVehicleDetailListResponse, AsyncOffsetPage[LaunchVehicleDetailListResponse]]:
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
            "/udl/launchvehicledetails",
            page=AsyncOffsetPage[LaunchVehicleDetailListResponse],
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
                    launch_vehicle_detail_list_params.LaunchVehicleDetailListParams,
                ),
            ),
            model=LaunchVehicleDetailListResponse,
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
        Service operation to delete a LaunchVehicleDetails object specified by the
        passed ID path parameter. LaunchVehicleDetails represents launch vehicle details
        and characteristics, compiled by a particular source. A vehicle may have
        multiple details records from various sources. A specific role is required to
        perform this service operation. Please contact the UDL team for assistance.

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
            f"/udl/launchvehicledetails/{id}",
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
    ) -> LaunchVehicleDetailGetResponse:
        """
        Service operation to get a single LaunchVehicleDetails record by its unique ID
        passed as a path parameter. LaunchVehicleDetails represents launch vehicle
        details and characteristics, compiled by a particular source. A vehicle may have
        multiple details records from various sources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/udl/launchvehicledetails/{id}",
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
                    launch_vehicle_detail_get_params.LaunchVehicleDetailGetParams,
                ),
            ),
            cast_to=LaunchVehicleDetailGetResponse,
        )


class LaunchVehicleDetailsResourceWithRawResponse:
    def __init__(self, launch_vehicle_details: LaunchVehicleDetailsResource) -> None:
        self._launch_vehicle_details = launch_vehicle_details

        self.create = to_raw_response_wrapper(
            launch_vehicle_details.create,
        )
        self.update = to_raw_response_wrapper(
            launch_vehicle_details.update,
        )
        self.list = to_raw_response_wrapper(
            launch_vehicle_details.list,
        )
        self.delete = to_raw_response_wrapper(
            launch_vehicle_details.delete,
        )
        self.get = to_raw_response_wrapper(
            launch_vehicle_details.get,
        )


class AsyncLaunchVehicleDetailsResourceWithRawResponse:
    def __init__(self, launch_vehicle_details: AsyncLaunchVehicleDetailsResource) -> None:
        self._launch_vehicle_details = launch_vehicle_details

        self.create = async_to_raw_response_wrapper(
            launch_vehicle_details.create,
        )
        self.update = async_to_raw_response_wrapper(
            launch_vehicle_details.update,
        )
        self.list = async_to_raw_response_wrapper(
            launch_vehicle_details.list,
        )
        self.delete = async_to_raw_response_wrapper(
            launch_vehicle_details.delete,
        )
        self.get = async_to_raw_response_wrapper(
            launch_vehicle_details.get,
        )


class LaunchVehicleDetailsResourceWithStreamingResponse:
    def __init__(self, launch_vehicle_details: LaunchVehicleDetailsResource) -> None:
        self._launch_vehicle_details = launch_vehicle_details

        self.create = to_streamed_response_wrapper(
            launch_vehicle_details.create,
        )
        self.update = to_streamed_response_wrapper(
            launch_vehicle_details.update,
        )
        self.list = to_streamed_response_wrapper(
            launch_vehicle_details.list,
        )
        self.delete = to_streamed_response_wrapper(
            launch_vehicle_details.delete,
        )
        self.get = to_streamed_response_wrapper(
            launch_vehicle_details.get,
        )


class AsyncLaunchVehicleDetailsResourceWithStreamingResponse:
    def __init__(self, launch_vehicle_details: AsyncLaunchVehicleDetailsResource) -> None:
        self._launch_vehicle_details = launch_vehicle_details

        self.create = async_to_streamed_response_wrapper(
            launch_vehicle_details.create,
        )
        self.update = async_to_streamed_response_wrapper(
            launch_vehicle_details.update,
        )
        self.list = async_to_streamed_response_wrapper(
            launch_vehicle_details.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            launch_vehicle_details.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            launch_vehicle_details.get,
        )
