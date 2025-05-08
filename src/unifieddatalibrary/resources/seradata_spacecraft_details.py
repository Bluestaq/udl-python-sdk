# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    seradata_spacecraft_detail_get_params,
    seradata_spacecraft_detail_list_params,
    seradata_spacecraft_detail_count_params,
    seradata_spacecraft_detail_tuple_params,
    seradata_spacecraft_detail_create_params,
    seradata_spacecraft_detail_update_params,
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
from ..types.seradata_spacecraft_detail_get_response import SeradataSpacecraftDetailGetResponse
from ..types.seradata_spacecraft_detail_list_response import SeradataSpacecraftDetailListResponse
from ..types.seradata_spacecraft_detail_tuple_response import SeradataSpacecraftDetailTupleResponse

__all__ = ["SeradataSpacecraftDetailsResource", "AsyncSeradataSpacecraftDetailsResource"]


class SeradataSpacecraftDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeradataSpacecraftDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SeradataSpacecraftDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeradataSpacecraftDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return SeradataSpacecraftDetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        additional_missions_groups: str | NotGiven = NOT_GIVEN,
        altitude: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor_estimated: bool | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        bus_id: str | NotGiven = NOT_GIVEN,
        capability_lost: float | NotGiven = NOT_GIVEN,
        capacity_lost: float | NotGiven = NOT_GIVEN,
        catalog_number: int | NotGiven = NOT_GIVEN,
        collision_risk_cm: float | NotGiven = NOT_GIVEN,
        collision_risk_mm: float | NotGiven = NOT_GIVEN,
        combined_cost_estimated: bool | NotGiven = NOT_GIVEN,
        combined_new_cost: float | NotGiven = NOT_GIVEN,
        commercial_launch: bool | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        cost_estimated: bool | NotGiven = NOT_GIVEN,
        cubesat_dispenser_type: str | NotGiven = NOT_GIVEN,
        current_age: float | NotGiven = NOT_GIVEN,
        date_of_observation: Union[str, datetime] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        design_life: int | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        expected_life: int | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        insurance_losses_total: float | NotGiven = NOT_GIVEN,
        insurance_notes: str | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch: float | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch_estimated: bool | NotGiven = NOT_GIVEN,
        insured_at_launch: bool | NotGiven = NOT_GIVEN,
        insured_value_at_launch: float | NotGiven = NOT_GIVEN,
        insured_value_launch_estimated: bool | NotGiven = NOT_GIVEN,
        intl_number: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        launch_arranger: str | NotGiven = NOT_GIVEN,
        launch_arranger_country: str | NotGiven = NOT_GIVEN,
        launch_characteristic: str | NotGiven = NOT_GIVEN,
        launch_cost: float | NotGiven = NOT_GIVEN,
        launch_cost_estimated: bool | NotGiven = NOT_GIVEN,
        launch_country: str | NotGiven = NOT_GIVEN,
        launch_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_date_remarks: str | NotGiven = NOT_GIVEN,
        launch_id: str | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_notes: str | NotGiven = NOT_GIVEN,
        launch_number: str | NotGiven = NOT_GIVEN,
        launch_provider: str | NotGiven = NOT_GIVEN,
        launch_provider_country: str | NotGiven = NOT_GIVEN,
        launch_provider_flight_number: str | NotGiven = NOT_GIVEN,
        launch_site_id: str | NotGiven = NOT_GIVEN,
        launch_site_name: str | NotGiven = NOT_GIVEN,
        launch_type: str | NotGiven = NOT_GIVEN,
        launch_vehicle_id: str | NotGiven = NOT_GIVEN,
        leased: bool | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        name_at_launch: str | NotGiven = NOT_GIVEN,
        new_cost: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_humans: int | NotGiven = NOT_GIVEN,
        operator: str | NotGiven = NOT_GIVEN,
        operator_country: str | NotGiven = NOT_GIVEN,
        orbit_category: str | NotGiven = NOT_GIVEN,
        orbit_sub_category: str | NotGiven = NOT_GIVEN,
        order_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        owner_country: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        primary_mission_group: str | NotGiven = NOT_GIVEN,
        prime_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        program_name: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        reusable_flights: str | NotGiven = NOT_GIVEN,
        reused_hull_name: str | NotGiven = NOT_GIVEN,
        sector: str | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        stabilizer: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        total_claims: int | NotGiven = NOT_GIVEN,
        total_fatalities: int | NotGiven = NOT_GIVEN,
        total_injuries: int | NotGiven = NOT_GIVEN,
        total_payload_power: float | NotGiven = NOT_GIVEN,
        youtube_launch_link: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SeradataSpacecraftDetails as a POST body and
        ingest into the database. A specific role is required to perform this service
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

          name: Spacecraft name.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          additional_missions_groups: Spacecraft additional missions and groups.

          altitude: Spacecraft latest altitude in km.

          annual_insured_depreciation_factor: Annual insured depreciaion factor as a percent fraction.

          annual_insured_depreciation_factor_estimated: Boolean indicating if the spacecraft annualInsuredDepreciationFactor is
              estimated.

          apogee: Apogee in km.

          bus_id: Spacecraft Bus ID.

          capability_lost: Total capability lost as a percent fraction.

          capacity_lost: Total capacity lost as a percent fraction.

          catalog_number: NORAD satellite number if available.

          collision_risk_cm: Spacecraft collision risk 1cm sqm latest.

          collision_risk_mm: Spacecraft collision risk 1mm sqm latest.

          combined_cost_estimated: Boolean indicating if the spacecraft combined new cost is estimated.

          combined_new_cost: Combined cost of spacecraft at new in M USD.

          commercial_launch: Boolean indicating if the launch was commercial.

          constellation: Spacecraft constellation.

          cost_estimated: Boolean indicating if the spacecraft cost is estimated.

          cubesat_dispenser_type: Cubesat dispenser type.

          current_age: Current age in years.

          date_of_observation: Spacecraft date of observation.

          description: Description associated with the spacecraft.

          design_life: Spacecraft design life in days.

          dry_mass: Mass dry in kg.

          expected_life: Spacecraft expected life in days.

          geo_position: WGS84 longitude of the spacecraft’s latest GEO position, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          id_on_orbit: UUID of the parent Onorbit record, if available.

          inclination: Seradata provided inclination in degrees.

          insurance_losses_total: Spacecraft total insurance losses as a fraction.

          insurance_notes: Insurance notes for the spacecraft.

          insurance_premium_at_launch: Insurance premium at launch in M USD.

          insurance_premium_at_launch_estimated: Boolean indicating if the spacecraft insurancePremiumAtLaunch is estimated.

          insured_at_launch: Boolean indicating if the spacecraft was insured at launch.

          insured_value_at_launch: Insured value of spacecraft at launch in M USD.

          insured_value_launch_estimated: Boolean indicating if the spacecraft insured value at launch is estimated.

          intl_number: Seradata international number.

          lat: Spacecraft latest latitude in degrees.

          launch_arranger: Spacecraft launch arranger.

          launch_arranger_country: Spacecraft launch arranger country.

          launch_characteristic: Seradata launch characteristic (e.g. Expendable, Reusable (New), etc).

          launch_cost: Cost of launch in M USD.

          launch_cost_estimated: Boolean indicating if the spacecraft launch cost is estimated.

          launch_country: Seradata launch country.

          launch_date: Launch date.

          launch_date_remarks: Seradata remarks on launch date.

          launch_id: Seradata launch ID.

          launch_mass: Mass at launch in kg.

          launch_notes: Insurance notes for the spacecraft.

          launch_number: Seradata launch number.

          launch_provider: Seradata launch provider.

          launch_provider_country: Seradata launch provider country.

          launch_provider_flight_number: Seradata launch vehicle family.

          launch_site_id: Seradata Launch Site ID.

          launch_site_name: Launch Site Name.

          launch_type: Seradata launch type (e.g. Launched, Future, etc).

          launch_vehicle_id: Seradata launch ID.

          leased: Boolean indicating if the spacecraft was leased.

          life_lost: Spacecraft life lost as a percent fraction.

          lon: Spacecraft latest longitude in degrees.

          mass_category: Mass category (e.g. 2500 - 3500kg - Large Satellite, 10 - 100 kg -
              Microsatellite, etc).

          name_at_launch: Spacecraft name at launch.

          new_cost: Cost of spacecraft at new in M USD.

          notes: Notes on the spacecraft.

          num_humans: Number of humans carried on spacecraft.

          operator: Spacecraft operator name.

          operator_country: Spacecraft operator country.

          orbit_category: Spacecraft orbit category (e.g GEO, LEO, etc).

          orbit_sub_category: Spacecraft sub orbit category (e.g LEO - Sun-synchronous, Geostationary, etc).

          order_date: Spacecraft order date.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: Spacecraft owner name.

          owner_country: Spacecraft owner country.

          perigee: Perigee in km.

          period: Spacecraft period in minutes.

          primary_mission_group: Spacecraft primary mission and group.

          prime_manufacturer_org_id: UUID of the prime manufacturer organization, if available.

          program_name: Spacecraft program name.

          quantity: Spacecraft quantity.

          reusable_flights: Spacecraft reusable flights.

          reused_hull_name: Spacecraft reused hull name.

          sector: Seradata sector (e.g. Commercial, Military, Civil/Other).

          serial_number: Spacecraft serial number.

          stabilizer: Spacecraft stabilizer (e.g. 3-Axis, Gravity Gradiant, etc).

          status: Spacecraft status (e.g. Inactive - Retired, Inactive - Re-entered, Active, etc).

          total_claims: Number of insurance claims for this spacecraft.

          total_fatalities: Number of fatalities related to this spacecraft.

          total_injuries: Number of injuries related to this spacecraft.

          total_payload_power: Mass dry in kg.

          youtube_launch_link: Youtube link of launch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/seradataspacecraftdetails",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "id": id,
                    "additional_missions_groups": additional_missions_groups,
                    "altitude": altitude,
                    "annual_insured_depreciation_factor": annual_insured_depreciation_factor,
                    "annual_insured_depreciation_factor_estimated": annual_insured_depreciation_factor_estimated,
                    "apogee": apogee,
                    "bus_id": bus_id,
                    "capability_lost": capability_lost,
                    "capacity_lost": capacity_lost,
                    "catalog_number": catalog_number,
                    "collision_risk_cm": collision_risk_cm,
                    "collision_risk_mm": collision_risk_mm,
                    "combined_cost_estimated": combined_cost_estimated,
                    "combined_new_cost": combined_new_cost,
                    "commercial_launch": commercial_launch,
                    "constellation": constellation,
                    "cost_estimated": cost_estimated,
                    "cubesat_dispenser_type": cubesat_dispenser_type,
                    "current_age": current_age,
                    "date_of_observation": date_of_observation,
                    "description": description,
                    "design_life": design_life,
                    "dry_mass": dry_mass,
                    "expected_life": expected_life,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclination": inclination,
                    "insurance_losses_total": insurance_losses_total,
                    "insurance_notes": insurance_notes,
                    "insurance_premium_at_launch": insurance_premium_at_launch,
                    "insurance_premium_at_launch_estimated": insurance_premium_at_launch_estimated,
                    "insured_at_launch": insured_at_launch,
                    "insured_value_at_launch": insured_value_at_launch,
                    "insured_value_launch_estimated": insured_value_launch_estimated,
                    "intl_number": intl_number,
                    "lat": lat,
                    "launch_arranger": launch_arranger,
                    "launch_arranger_country": launch_arranger_country,
                    "launch_characteristic": launch_characteristic,
                    "launch_cost": launch_cost,
                    "launch_cost_estimated": launch_cost_estimated,
                    "launch_country": launch_country,
                    "launch_date": launch_date,
                    "launch_date_remarks": launch_date_remarks,
                    "launch_id": launch_id,
                    "launch_mass": launch_mass,
                    "launch_notes": launch_notes,
                    "launch_number": launch_number,
                    "launch_provider": launch_provider,
                    "launch_provider_country": launch_provider_country,
                    "launch_provider_flight_number": launch_provider_flight_number,
                    "launch_site_id": launch_site_id,
                    "launch_site_name": launch_site_name,
                    "launch_type": launch_type,
                    "launch_vehicle_id": launch_vehicle_id,
                    "leased": leased,
                    "life_lost": life_lost,
                    "lon": lon,
                    "mass_category": mass_category,
                    "name_at_launch": name_at_launch,
                    "new_cost": new_cost,
                    "notes": notes,
                    "num_humans": num_humans,
                    "operator": operator,
                    "operator_country": operator_country,
                    "orbit_category": orbit_category,
                    "orbit_sub_category": orbit_sub_category,
                    "order_date": order_date,
                    "origin": origin,
                    "owner": owner,
                    "owner_country": owner_country,
                    "perigee": perigee,
                    "period": period,
                    "primary_mission_group": primary_mission_group,
                    "prime_manufacturer_org_id": prime_manufacturer_org_id,
                    "program_name": program_name,
                    "quantity": quantity,
                    "reusable_flights": reusable_flights,
                    "reused_hull_name": reused_hull_name,
                    "sector": sector,
                    "serial_number": serial_number,
                    "stabilizer": stabilizer,
                    "status": status,
                    "total_claims": total_claims,
                    "total_fatalities": total_fatalities,
                    "total_injuries": total_injuries,
                    "total_payload_power": total_payload_power,
                    "youtube_launch_link": youtube_launch_link,
                },
                seradata_spacecraft_detail_create_params.SeradataSpacecraftDetailCreateParams,
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
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        additional_missions_groups: str | NotGiven = NOT_GIVEN,
        altitude: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor_estimated: bool | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        bus_id: str | NotGiven = NOT_GIVEN,
        capability_lost: float | NotGiven = NOT_GIVEN,
        capacity_lost: float | NotGiven = NOT_GIVEN,
        catalog_number: int | NotGiven = NOT_GIVEN,
        collision_risk_cm: float | NotGiven = NOT_GIVEN,
        collision_risk_mm: float | NotGiven = NOT_GIVEN,
        combined_cost_estimated: bool | NotGiven = NOT_GIVEN,
        combined_new_cost: float | NotGiven = NOT_GIVEN,
        commercial_launch: bool | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        cost_estimated: bool | NotGiven = NOT_GIVEN,
        cubesat_dispenser_type: str | NotGiven = NOT_GIVEN,
        current_age: float | NotGiven = NOT_GIVEN,
        date_of_observation: Union[str, datetime] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        design_life: int | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        expected_life: int | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        insurance_losses_total: float | NotGiven = NOT_GIVEN,
        insurance_notes: str | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch: float | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch_estimated: bool | NotGiven = NOT_GIVEN,
        insured_at_launch: bool | NotGiven = NOT_GIVEN,
        insured_value_at_launch: float | NotGiven = NOT_GIVEN,
        insured_value_launch_estimated: bool | NotGiven = NOT_GIVEN,
        intl_number: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        launch_arranger: str | NotGiven = NOT_GIVEN,
        launch_arranger_country: str | NotGiven = NOT_GIVEN,
        launch_characteristic: str | NotGiven = NOT_GIVEN,
        launch_cost: float | NotGiven = NOT_GIVEN,
        launch_cost_estimated: bool | NotGiven = NOT_GIVEN,
        launch_country: str | NotGiven = NOT_GIVEN,
        launch_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_date_remarks: str | NotGiven = NOT_GIVEN,
        launch_id: str | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_notes: str | NotGiven = NOT_GIVEN,
        launch_number: str | NotGiven = NOT_GIVEN,
        launch_provider: str | NotGiven = NOT_GIVEN,
        launch_provider_country: str | NotGiven = NOT_GIVEN,
        launch_provider_flight_number: str | NotGiven = NOT_GIVEN,
        launch_site_id: str | NotGiven = NOT_GIVEN,
        launch_site_name: str | NotGiven = NOT_GIVEN,
        launch_type: str | NotGiven = NOT_GIVEN,
        launch_vehicle_id: str | NotGiven = NOT_GIVEN,
        leased: bool | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        name_at_launch: str | NotGiven = NOT_GIVEN,
        new_cost: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_humans: int | NotGiven = NOT_GIVEN,
        operator: str | NotGiven = NOT_GIVEN,
        operator_country: str | NotGiven = NOT_GIVEN,
        orbit_category: str | NotGiven = NOT_GIVEN,
        orbit_sub_category: str | NotGiven = NOT_GIVEN,
        order_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        owner_country: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        primary_mission_group: str | NotGiven = NOT_GIVEN,
        prime_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        program_name: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        reusable_flights: str | NotGiven = NOT_GIVEN,
        reused_hull_name: str | NotGiven = NOT_GIVEN,
        sector: str | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        stabilizer: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        total_claims: int | NotGiven = NOT_GIVEN,
        total_fatalities: int | NotGiven = NOT_GIVEN,
        total_injuries: int | NotGiven = NOT_GIVEN,
        total_payload_power: float | NotGiven = NOT_GIVEN,
        youtube_launch_link: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an SeradataSpacecraftDetails.

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

          name: Spacecraft name.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          additional_missions_groups: Spacecraft additional missions and groups.

          altitude: Spacecraft latest altitude in km.

          annual_insured_depreciation_factor: Annual insured depreciaion factor as a percent fraction.

          annual_insured_depreciation_factor_estimated: Boolean indicating if the spacecraft annualInsuredDepreciationFactor is
              estimated.

          apogee: Apogee in km.

          bus_id: Spacecraft Bus ID.

          capability_lost: Total capability lost as a percent fraction.

          capacity_lost: Total capacity lost as a percent fraction.

          catalog_number: NORAD satellite number if available.

          collision_risk_cm: Spacecraft collision risk 1cm sqm latest.

          collision_risk_mm: Spacecraft collision risk 1mm sqm latest.

          combined_cost_estimated: Boolean indicating if the spacecraft combined new cost is estimated.

          combined_new_cost: Combined cost of spacecraft at new in M USD.

          commercial_launch: Boolean indicating if the launch was commercial.

          constellation: Spacecraft constellation.

          cost_estimated: Boolean indicating if the spacecraft cost is estimated.

          cubesat_dispenser_type: Cubesat dispenser type.

          current_age: Current age in years.

          date_of_observation: Spacecraft date of observation.

          description: Description associated with the spacecraft.

          design_life: Spacecraft design life in days.

          dry_mass: Mass dry in kg.

          expected_life: Spacecraft expected life in days.

          geo_position: WGS84 longitude of the spacecraft’s latest GEO position, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          id_on_orbit: UUID of the parent Onorbit record, if available.

          inclination: Seradata provided inclination in degrees.

          insurance_losses_total: Spacecraft total insurance losses as a fraction.

          insurance_notes: Insurance notes for the spacecraft.

          insurance_premium_at_launch: Insurance premium at launch in M USD.

          insurance_premium_at_launch_estimated: Boolean indicating if the spacecraft insurancePremiumAtLaunch is estimated.

          insured_at_launch: Boolean indicating if the spacecraft was insured at launch.

          insured_value_at_launch: Insured value of spacecraft at launch in M USD.

          insured_value_launch_estimated: Boolean indicating if the spacecraft insured value at launch is estimated.

          intl_number: Seradata international number.

          lat: Spacecraft latest latitude in degrees.

          launch_arranger: Spacecraft launch arranger.

          launch_arranger_country: Spacecraft launch arranger country.

          launch_characteristic: Seradata launch characteristic (e.g. Expendable, Reusable (New), etc).

          launch_cost: Cost of launch in M USD.

          launch_cost_estimated: Boolean indicating if the spacecraft launch cost is estimated.

          launch_country: Seradata launch country.

          launch_date: Launch date.

          launch_date_remarks: Seradata remarks on launch date.

          launch_id: Seradata launch ID.

          launch_mass: Mass at launch in kg.

          launch_notes: Insurance notes for the spacecraft.

          launch_number: Seradata launch number.

          launch_provider: Seradata launch provider.

          launch_provider_country: Seradata launch provider country.

          launch_provider_flight_number: Seradata launch vehicle family.

          launch_site_id: Seradata Launch Site ID.

          launch_site_name: Launch Site Name.

          launch_type: Seradata launch type (e.g. Launched, Future, etc).

          launch_vehicle_id: Seradata launch ID.

          leased: Boolean indicating if the spacecraft was leased.

          life_lost: Spacecraft life lost as a percent fraction.

          lon: Spacecraft latest longitude in degrees.

          mass_category: Mass category (e.g. 2500 - 3500kg - Large Satellite, 10 - 100 kg -
              Microsatellite, etc).

          name_at_launch: Spacecraft name at launch.

          new_cost: Cost of spacecraft at new in M USD.

          notes: Notes on the spacecraft.

          num_humans: Number of humans carried on spacecraft.

          operator: Spacecraft operator name.

          operator_country: Spacecraft operator country.

          orbit_category: Spacecraft orbit category (e.g GEO, LEO, etc).

          orbit_sub_category: Spacecraft sub orbit category (e.g LEO - Sun-synchronous, Geostationary, etc).

          order_date: Spacecraft order date.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: Spacecraft owner name.

          owner_country: Spacecraft owner country.

          perigee: Perigee in km.

          period: Spacecraft period in minutes.

          primary_mission_group: Spacecraft primary mission and group.

          prime_manufacturer_org_id: UUID of the prime manufacturer organization, if available.

          program_name: Spacecraft program name.

          quantity: Spacecraft quantity.

          reusable_flights: Spacecraft reusable flights.

          reused_hull_name: Spacecraft reused hull name.

          sector: Seradata sector (e.g. Commercial, Military, Civil/Other).

          serial_number: Spacecraft serial number.

          stabilizer: Spacecraft stabilizer (e.g. 3-Axis, Gravity Gradiant, etc).

          status: Spacecraft status (e.g. Inactive - Retired, Inactive - Re-entered, Active, etc).

          total_claims: Number of insurance claims for this spacecraft.

          total_fatalities: Number of fatalities related to this spacecraft.

          total_injuries: Number of injuries related to this spacecraft.

          total_payload_power: Mass dry in kg.

          youtube_launch_link: Youtube link of launch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/seradataspacecraftdetails/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "additional_missions_groups": additional_missions_groups,
                    "altitude": altitude,
                    "annual_insured_depreciation_factor": annual_insured_depreciation_factor,
                    "annual_insured_depreciation_factor_estimated": annual_insured_depreciation_factor_estimated,
                    "apogee": apogee,
                    "bus_id": bus_id,
                    "capability_lost": capability_lost,
                    "capacity_lost": capacity_lost,
                    "catalog_number": catalog_number,
                    "collision_risk_cm": collision_risk_cm,
                    "collision_risk_mm": collision_risk_mm,
                    "combined_cost_estimated": combined_cost_estimated,
                    "combined_new_cost": combined_new_cost,
                    "commercial_launch": commercial_launch,
                    "constellation": constellation,
                    "cost_estimated": cost_estimated,
                    "cubesat_dispenser_type": cubesat_dispenser_type,
                    "current_age": current_age,
                    "date_of_observation": date_of_observation,
                    "description": description,
                    "design_life": design_life,
                    "dry_mass": dry_mass,
                    "expected_life": expected_life,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclination": inclination,
                    "insurance_losses_total": insurance_losses_total,
                    "insurance_notes": insurance_notes,
                    "insurance_premium_at_launch": insurance_premium_at_launch,
                    "insurance_premium_at_launch_estimated": insurance_premium_at_launch_estimated,
                    "insured_at_launch": insured_at_launch,
                    "insured_value_at_launch": insured_value_at_launch,
                    "insured_value_launch_estimated": insured_value_launch_estimated,
                    "intl_number": intl_number,
                    "lat": lat,
                    "launch_arranger": launch_arranger,
                    "launch_arranger_country": launch_arranger_country,
                    "launch_characteristic": launch_characteristic,
                    "launch_cost": launch_cost,
                    "launch_cost_estimated": launch_cost_estimated,
                    "launch_country": launch_country,
                    "launch_date": launch_date,
                    "launch_date_remarks": launch_date_remarks,
                    "launch_id": launch_id,
                    "launch_mass": launch_mass,
                    "launch_notes": launch_notes,
                    "launch_number": launch_number,
                    "launch_provider": launch_provider,
                    "launch_provider_country": launch_provider_country,
                    "launch_provider_flight_number": launch_provider_flight_number,
                    "launch_site_id": launch_site_id,
                    "launch_site_name": launch_site_name,
                    "launch_type": launch_type,
                    "launch_vehicle_id": launch_vehicle_id,
                    "leased": leased,
                    "life_lost": life_lost,
                    "lon": lon,
                    "mass_category": mass_category,
                    "name_at_launch": name_at_launch,
                    "new_cost": new_cost,
                    "notes": notes,
                    "num_humans": num_humans,
                    "operator": operator,
                    "operator_country": operator_country,
                    "orbit_category": orbit_category,
                    "orbit_sub_category": orbit_sub_category,
                    "order_date": order_date,
                    "origin": origin,
                    "owner": owner,
                    "owner_country": owner_country,
                    "perigee": perigee,
                    "period": period,
                    "primary_mission_group": primary_mission_group,
                    "prime_manufacturer_org_id": prime_manufacturer_org_id,
                    "program_name": program_name,
                    "quantity": quantity,
                    "reusable_flights": reusable_flights,
                    "reused_hull_name": reused_hull_name,
                    "sector": sector,
                    "serial_number": serial_number,
                    "stabilizer": stabilizer,
                    "status": status,
                    "total_claims": total_claims,
                    "total_fatalities": total_fatalities,
                    "total_injuries": total_injuries,
                    "total_payload_power": total_payload_power,
                    "youtube_launch_link": youtube_launch_link,
                },
                seradata_spacecraft_detail_update_params.SeradataSpacecraftDetailUpdateParams,
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
    ) -> SyncOffsetPage[SeradataSpacecraftDetailListResponse]:
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
            "/udl/seradataspacecraftdetails",
            page=SyncOffsetPage[SeradataSpacecraftDetailListResponse],
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
                    seradata_spacecraft_detail_list_params.SeradataSpacecraftDetailListParams,
                ),
            ),
            model=SeradataSpacecraftDetailListResponse,
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
        Service operation to delete an SeradataSpacecraftDetails specified by the passed
        ID path parameter. A specific role is required to perform this service
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
            f"/udl/seradataspacecraftdetails/{id}",
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
            "/udl/seradataspacecraftdetails/count",
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
                    seradata_spacecraft_detail_count_params.SeradataSpacecraftDetailCountParams,
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
    ) -> SeradataSpacecraftDetailGetResponse:
        """
        Service operation to get a single SeradataSpacecraftDetails by its unique ID
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
            f"/udl/seradataspacecraftdetails/{id}",
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
                    seradata_spacecraft_detail_get_params.SeradataSpacecraftDetailGetParams,
                ),
            ),
            cast_to=SeradataSpacecraftDetailGetResponse,
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
            "/udl/seradataspacecraftdetails/queryhelp",
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
    ) -> SeradataSpacecraftDetailTupleResponse:
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
            "/udl/seradataspacecraftdetails/tuple",
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
                    seradata_spacecraft_detail_tuple_params.SeradataSpacecraftDetailTupleParams,
                ),
            ),
            cast_to=SeradataSpacecraftDetailTupleResponse,
        )


class AsyncSeradataSpacecraftDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeradataSpacecraftDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSeradataSpacecraftDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        additional_missions_groups: str | NotGiven = NOT_GIVEN,
        altitude: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor_estimated: bool | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        bus_id: str | NotGiven = NOT_GIVEN,
        capability_lost: float | NotGiven = NOT_GIVEN,
        capacity_lost: float | NotGiven = NOT_GIVEN,
        catalog_number: int | NotGiven = NOT_GIVEN,
        collision_risk_cm: float | NotGiven = NOT_GIVEN,
        collision_risk_mm: float | NotGiven = NOT_GIVEN,
        combined_cost_estimated: bool | NotGiven = NOT_GIVEN,
        combined_new_cost: float | NotGiven = NOT_GIVEN,
        commercial_launch: bool | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        cost_estimated: bool | NotGiven = NOT_GIVEN,
        cubesat_dispenser_type: str | NotGiven = NOT_GIVEN,
        current_age: float | NotGiven = NOT_GIVEN,
        date_of_observation: Union[str, datetime] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        design_life: int | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        expected_life: int | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        insurance_losses_total: float | NotGiven = NOT_GIVEN,
        insurance_notes: str | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch: float | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch_estimated: bool | NotGiven = NOT_GIVEN,
        insured_at_launch: bool | NotGiven = NOT_GIVEN,
        insured_value_at_launch: float | NotGiven = NOT_GIVEN,
        insured_value_launch_estimated: bool | NotGiven = NOT_GIVEN,
        intl_number: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        launch_arranger: str | NotGiven = NOT_GIVEN,
        launch_arranger_country: str | NotGiven = NOT_GIVEN,
        launch_characteristic: str | NotGiven = NOT_GIVEN,
        launch_cost: float | NotGiven = NOT_GIVEN,
        launch_cost_estimated: bool | NotGiven = NOT_GIVEN,
        launch_country: str | NotGiven = NOT_GIVEN,
        launch_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_date_remarks: str | NotGiven = NOT_GIVEN,
        launch_id: str | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_notes: str | NotGiven = NOT_GIVEN,
        launch_number: str | NotGiven = NOT_GIVEN,
        launch_provider: str | NotGiven = NOT_GIVEN,
        launch_provider_country: str | NotGiven = NOT_GIVEN,
        launch_provider_flight_number: str | NotGiven = NOT_GIVEN,
        launch_site_id: str | NotGiven = NOT_GIVEN,
        launch_site_name: str | NotGiven = NOT_GIVEN,
        launch_type: str | NotGiven = NOT_GIVEN,
        launch_vehicle_id: str | NotGiven = NOT_GIVEN,
        leased: bool | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        name_at_launch: str | NotGiven = NOT_GIVEN,
        new_cost: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_humans: int | NotGiven = NOT_GIVEN,
        operator: str | NotGiven = NOT_GIVEN,
        operator_country: str | NotGiven = NOT_GIVEN,
        orbit_category: str | NotGiven = NOT_GIVEN,
        orbit_sub_category: str | NotGiven = NOT_GIVEN,
        order_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        owner_country: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        primary_mission_group: str | NotGiven = NOT_GIVEN,
        prime_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        program_name: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        reusable_flights: str | NotGiven = NOT_GIVEN,
        reused_hull_name: str | NotGiven = NOT_GIVEN,
        sector: str | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        stabilizer: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        total_claims: int | NotGiven = NOT_GIVEN,
        total_fatalities: int | NotGiven = NOT_GIVEN,
        total_injuries: int | NotGiven = NOT_GIVEN,
        total_payload_power: float | NotGiven = NOT_GIVEN,
        youtube_launch_link: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single SeradataSpacecraftDetails as a POST body and
        ingest into the database. A specific role is required to perform this service
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

          name: Spacecraft name.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          additional_missions_groups: Spacecraft additional missions and groups.

          altitude: Spacecraft latest altitude in km.

          annual_insured_depreciation_factor: Annual insured depreciaion factor as a percent fraction.

          annual_insured_depreciation_factor_estimated: Boolean indicating if the spacecraft annualInsuredDepreciationFactor is
              estimated.

          apogee: Apogee in km.

          bus_id: Spacecraft Bus ID.

          capability_lost: Total capability lost as a percent fraction.

          capacity_lost: Total capacity lost as a percent fraction.

          catalog_number: NORAD satellite number if available.

          collision_risk_cm: Spacecraft collision risk 1cm sqm latest.

          collision_risk_mm: Spacecraft collision risk 1mm sqm latest.

          combined_cost_estimated: Boolean indicating if the spacecraft combined new cost is estimated.

          combined_new_cost: Combined cost of spacecraft at new in M USD.

          commercial_launch: Boolean indicating if the launch was commercial.

          constellation: Spacecraft constellation.

          cost_estimated: Boolean indicating if the spacecraft cost is estimated.

          cubesat_dispenser_type: Cubesat dispenser type.

          current_age: Current age in years.

          date_of_observation: Spacecraft date of observation.

          description: Description associated with the spacecraft.

          design_life: Spacecraft design life in days.

          dry_mass: Mass dry in kg.

          expected_life: Spacecraft expected life in days.

          geo_position: WGS84 longitude of the spacecraft’s latest GEO position, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          id_on_orbit: UUID of the parent Onorbit record, if available.

          inclination: Seradata provided inclination in degrees.

          insurance_losses_total: Spacecraft total insurance losses as a fraction.

          insurance_notes: Insurance notes for the spacecraft.

          insurance_premium_at_launch: Insurance premium at launch in M USD.

          insurance_premium_at_launch_estimated: Boolean indicating if the spacecraft insurancePremiumAtLaunch is estimated.

          insured_at_launch: Boolean indicating if the spacecraft was insured at launch.

          insured_value_at_launch: Insured value of spacecraft at launch in M USD.

          insured_value_launch_estimated: Boolean indicating if the spacecraft insured value at launch is estimated.

          intl_number: Seradata international number.

          lat: Spacecraft latest latitude in degrees.

          launch_arranger: Spacecraft launch arranger.

          launch_arranger_country: Spacecraft launch arranger country.

          launch_characteristic: Seradata launch characteristic (e.g. Expendable, Reusable (New), etc).

          launch_cost: Cost of launch in M USD.

          launch_cost_estimated: Boolean indicating if the spacecraft launch cost is estimated.

          launch_country: Seradata launch country.

          launch_date: Launch date.

          launch_date_remarks: Seradata remarks on launch date.

          launch_id: Seradata launch ID.

          launch_mass: Mass at launch in kg.

          launch_notes: Insurance notes for the spacecraft.

          launch_number: Seradata launch number.

          launch_provider: Seradata launch provider.

          launch_provider_country: Seradata launch provider country.

          launch_provider_flight_number: Seradata launch vehicle family.

          launch_site_id: Seradata Launch Site ID.

          launch_site_name: Launch Site Name.

          launch_type: Seradata launch type (e.g. Launched, Future, etc).

          launch_vehicle_id: Seradata launch ID.

          leased: Boolean indicating if the spacecraft was leased.

          life_lost: Spacecraft life lost as a percent fraction.

          lon: Spacecraft latest longitude in degrees.

          mass_category: Mass category (e.g. 2500 - 3500kg - Large Satellite, 10 - 100 kg -
              Microsatellite, etc).

          name_at_launch: Spacecraft name at launch.

          new_cost: Cost of spacecraft at new in M USD.

          notes: Notes on the spacecraft.

          num_humans: Number of humans carried on spacecraft.

          operator: Spacecraft operator name.

          operator_country: Spacecraft operator country.

          orbit_category: Spacecraft orbit category (e.g GEO, LEO, etc).

          orbit_sub_category: Spacecraft sub orbit category (e.g LEO - Sun-synchronous, Geostationary, etc).

          order_date: Spacecraft order date.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: Spacecraft owner name.

          owner_country: Spacecraft owner country.

          perigee: Perigee in km.

          period: Spacecraft period in minutes.

          primary_mission_group: Spacecraft primary mission and group.

          prime_manufacturer_org_id: UUID of the prime manufacturer organization, if available.

          program_name: Spacecraft program name.

          quantity: Spacecraft quantity.

          reusable_flights: Spacecraft reusable flights.

          reused_hull_name: Spacecraft reused hull name.

          sector: Seradata sector (e.g. Commercial, Military, Civil/Other).

          serial_number: Spacecraft serial number.

          stabilizer: Spacecraft stabilizer (e.g. 3-Axis, Gravity Gradiant, etc).

          status: Spacecraft status (e.g. Inactive - Retired, Inactive - Re-entered, Active, etc).

          total_claims: Number of insurance claims for this spacecraft.

          total_fatalities: Number of fatalities related to this spacecraft.

          total_injuries: Number of injuries related to this spacecraft.

          total_payload_power: Mass dry in kg.

          youtube_launch_link: Youtube link of launch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/seradataspacecraftdetails",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "id": id,
                    "additional_missions_groups": additional_missions_groups,
                    "altitude": altitude,
                    "annual_insured_depreciation_factor": annual_insured_depreciation_factor,
                    "annual_insured_depreciation_factor_estimated": annual_insured_depreciation_factor_estimated,
                    "apogee": apogee,
                    "bus_id": bus_id,
                    "capability_lost": capability_lost,
                    "capacity_lost": capacity_lost,
                    "catalog_number": catalog_number,
                    "collision_risk_cm": collision_risk_cm,
                    "collision_risk_mm": collision_risk_mm,
                    "combined_cost_estimated": combined_cost_estimated,
                    "combined_new_cost": combined_new_cost,
                    "commercial_launch": commercial_launch,
                    "constellation": constellation,
                    "cost_estimated": cost_estimated,
                    "cubesat_dispenser_type": cubesat_dispenser_type,
                    "current_age": current_age,
                    "date_of_observation": date_of_observation,
                    "description": description,
                    "design_life": design_life,
                    "dry_mass": dry_mass,
                    "expected_life": expected_life,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclination": inclination,
                    "insurance_losses_total": insurance_losses_total,
                    "insurance_notes": insurance_notes,
                    "insurance_premium_at_launch": insurance_premium_at_launch,
                    "insurance_premium_at_launch_estimated": insurance_premium_at_launch_estimated,
                    "insured_at_launch": insured_at_launch,
                    "insured_value_at_launch": insured_value_at_launch,
                    "insured_value_launch_estimated": insured_value_launch_estimated,
                    "intl_number": intl_number,
                    "lat": lat,
                    "launch_arranger": launch_arranger,
                    "launch_arranger_country": launch_arranger_country,
                    "launch_characteristic": launch_characteristic,
                    "launch_cost": launch_cost,
                    "launch_cost_estimated": launch_cost_estimated,
                    "launch_country": launch_country,
                    "launch_date": launch_date,
                    "launch_date_remarks": launch_date_remarks,
                    "launch_id": launch_id,
                    "launch_mass": launch_mass,
                    "launch_notes": launch_notes,
                    "launch_number": launch_number,
                    "launch_provider": launch_provider,
                    "launch_provider_country": launch_provider_country,
                    "launch_provider_flight_number": launch_provider_flight_number,
                    "launch_site_id": launch_site_id,
                    "launch_site_name": launch_site_name,
                    "launch_type": launch_type,
                    "launch_vehicle_id": launch_vehicle_id,
                    "leased": leased,
                    "life_lost": life_lost,
                    "lon": lon,
                    "mass_category": mass_category,
                    "name_at_launch": name_at_launch,
                    "new_cost": new_cost,
                    "notes": notes,
                    "num_humans": num_humans,
                    "operator": operator,
                    "operator_country": operator_country,
                    "orbit_category": orbit_category,
                    "orbit_sub_category": orbit_sub_category,
                    "order_date": order_date,
                    "origin": origin,
                    "owner": owner,
                    "owner_country": owner_country,
                    "perigee": perigee,
                    "period": period,
                    "primary_mission_group": primary_mission_group,
                    "prime_manufacturer_org_id": prime_manufacturer_org_id,
                    "program_name": program_name,
                    "quantity": quantity,
                    "reusable_flights": reusable_flights,
                    "reused_hull_name": reused_hull_name,
                    "sector": sector,
                    "serial_number": serial_number,
                    "stabilizer": stabilizer,
                    "status": status,
                    "total_claims": total_claims,
                    "total_fatalities": total_fatalities,
                    "total_injuries": total_injuries,
                    "total_payload_power": total_payload_power,
                    "youtube_launch_link": youtube_launch_link,
                },
                seradata_spacecraft_detail_create_params.SeradataSpacecraftDetailCreateParams,
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
        name: str,
        source: str,
        body_id: str | NotGiven = NOT_GIVEN,
        additional_missions_groups: str | NotGiven = NOT_GIVEN,
        altitude: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor: float | NotGiven = NOT_GIVEN,
        annual_insured_depreciation_factor_estimated: bool | NotGiven = NOT_GIVEN,
        apogee: float | NotGiven = NOT_GIVEN,
        bus_id: str | NotGiven = NOT_GIVEN,
        capability_lost: float | NotGiven = NOT_GIVEN,
        capacity_lost: float | NotGiven = NOT_GIVEN,
        catalog_number: int | NotGiven = NOT_GIVEN,
        collision_risk_cm: float | NotGiven = NOT_GIVEN,
        collision_risk_mm: float | NotGiven = NOT_GIVEN,
        combined_cost_estimated: bool | NotGiven = NOT_GIVEN,
        combined_new_cost: float | NotGiven = NOT_GIVEN,
        commercial_launch: bool | NotGiven = NOT_GIVEN,
        constellation: str | NotGiven = NOT_GIVEN,
        cost_estimated: bool | NotGiven = NOT_GIVEN,
        cubesat_dispenser_type: str | NotGiven = NOT_GIVEN,
        current_age: float | NotGiven = NOT_GIVEN,
        date_of_observation: Union[str, datetime] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        design_life: int | NotGiven = NOT_GIVEN,
        dry_mass: float | NotGiven = NOT_GIVEN,
        expected_life: int | NotGiven = NOT_GIVEN,
        geo_position: float | NotGiven = NOT_GIVEN,
        id_on_orbit: str | NotGiven = NOT_GIVEN,
        inclination: float | NotGiven = NOT_GIVEN,
        insurance_losses_total: float | NotGiven = NOT_GIVEN,
        insurance_notes: str | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch: float | NotGiven = NOT_GIVEN,
        insurance_premium_at_launch_estimated: bool | NotGiven = NOT_GIVEN,
        insured_at_launch: bool | NotGiven = NOT_GIVEN,
        insured_value_at_launch: float | NotGiven = NOT_GIVEN,
        insured_value_launch_estimated: bool | NotGiven = NOT_GIVEN,
        intl_number: str | NotGiven = NOT_GIVEN,
        lat: float | NotGiven = NOT_GIVEN,
        launch_arranger: str | NotGiven = NOT_GIVEN,
        launch_arranger_country: str | NotGiven = NOT_GIVEN,
        launch_characteristic: str | NotGiven = NOT_GIVEN,
        launch_cost: float | NotGiven = NOT_GIVEN,
        launch_cost_estimated: bool | NotGiven = NOT_GIVEN,
        launch_country: str | NotGiven = NOT_GIVEN,
        launch_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        launch_date_remarks: str | NotGiven = NOT_GIVEN,
        launch_id: str | NotGiven = NOT_GIVEN,
        launch_mass: float | NotGiven = NOT_GIVEN,
        launch_notes: str | NotGiven = NOT_GIVEN,
        launch_number: str | NotGiven = NOT_GIVEN,
        launch_provider: str | NotGiven = NOT_GIVEN,
        launch_provider_country: str | NotGiven = NOT_GIVEN,
        launch_provider_flight_number: str | NotGiven = NOT_GIVEN,
        launch_site_id: str | NotGiven = NOT_GIVEN,
        launch_site_name: str | NotGiven = NOT_GIVEN,
        launch_type: str | NotGiven = NOT_GIVEN,
        launch_vehicle_id: str | NotGiven = NOT_GIVEN,
        leased: bool | NotGiven = NOT_GIVEN,
        life_lost: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        name_at_launch: str | NotGiven = NOT_GIVEN,
        new_cost: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        num_humans: int | NotGiven = NOT_GIVEN,
        operator: str | NotGiven = NOT_GIVEN,
        operator_country: str | NotGiven = NOT_GIVEN,
        orbit_category: str | NotGiven = NOT_GIVEN,
        orbit_sub_category: str | NotGiven = NOT_GIVEN,
        order_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        owner_country: str | NotGiven = NOT_GIVEN,
        perigee: float | NotGiven = NOT_GIVEN,
        period: float | NotGiven = NOT_GIVEN,
        primary_mission_group: str | NotGiven = NOT_GIVEN,
        prime_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        program_name: str | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        reusable_flights: str | NotGiven = NOT_GIVEN,
        reused_hull_name: str | NotGiven = NOT_GIVEN,
        sector: str | NotGiven = NOT_GIVEN,
        serial_number: str | NotGiven = NOT_GIVEN,
        stabilizer: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        total_claims: int | NotGiven = NOT_GIVEN,
        total_fatalities: int | NotGiven = NOT_GIVEN,
        total_injuries: int | NotGiven = NOT_GIVEN,
        total_payload_power: float | NotGiven = NOT_GIVEN,
        youtube_launch_link: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update an SeradataSpacecraftDetails.

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

          name: Spacecraft name.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          additional_missions_groups: Spacecraft additional missions and groups.

          altitude: Spacecraft latest altitude in km.

          annual_insured_depreciation_factor: Annual insured depreciaion factor as a percent fraction.

          annual_insured_depreciation_factor_estimated: Boolean indicating if the spacecraft annualInsuredDepreciationFactor is
              estimated.

          apogee: Apogee in km.

          bus_id: Spacecraft Bus ID.

          capability_lost: Total capability lost as a percent fraction.

          capacity_lost: Total capacity lost as a percent fraction.

          catalog_number: NORAD satellite number if available.

          collision_risk_cm: Spacecraft collision risk 1cm sqm latest.

          collision_risk_mm: Spacecraft collision risk 1mm sqm latest.

          combined_cost_estimated: Boolean indicating if the spacecraft combined new cost is estimated.

          combined_new_cost: Combined cost of spacecraft at new in M USD.

          commercial_launch: Boolean indicating if the launch was commercial.

          constellation: Spacecraft constellation.

          cost_estimated: Boolean indicating if the spacecraft cost is estimated.

          cubesat_dispenser_type: Cubesat dispenser type.

          current_age: Current age in years.

          date_of_observation: Spacecraft date of observation.

          description: Description associated with the spacecraft.

          design_life: Spacecraft design life in days.

          dry_mass: Mass dry in kg.

          expected_life: Spacecraft expected life in days.

          geo_position: WGS84 longitude of the spacecraft’s latest GEO position, in degrees. -180 to 180
              degrees (negative values west of Prime Meridian).

          id_on_orbit: UUID of the parent Onorbit record, if available.

          inclination: Seradata provided inclination in degrees.

          insurance_losses_total: Spacecraft total insurance losses as a fraction.

          insurance_notes: Insurance notes for the spacecraft.

          insurance_premium_at_launch: Insurance premium at launch in M USD.

          insurance_premium_at_launch_estimated: Boolean indicating if the spacecraft insurancePremiumAtLaunch is estimated.

          insured_at_launch: Boolean indicating if the spacecraft was insured at launch.

          insured_value_at_launch: Insured value of spacecraft at launch in M USD.

          insured_value_launch_estimated: Boolean indicating if the spacecraft insured value at launch is estimated.

          intl_number: Seradata international number.

          lat: Spacecraft latest latitude in degrees.

          launch_arranger: Spacecraft launch arranger.

          launch_arranger_country: Spacecraft launch arranger country.

          launch_characteristic: Seradata launch characteristic (e.g. Expendable, Reusable (New), etc).

          launch_cost: Cost of launch in M USD.

          launch_cost_estimated: Boolean indicating if the spacecraft launch cost is estimated.

          launch_country: Seradata launch country.

          launch_date: Launch date.

          launch_date_remarks: Seradata remarks on launch date.

          launch_id: Seradata launch ID.

          launch_mass: Mass at launch in kg.

          launch_notes: Insurance notes for the spacecraft.

          launch_number: Seradata launch number.

          launch_provider: Seradata launch provider.

          launch_provider_country: Seradata launch provider country.

          launch_provider_flight_number: Seradata launch vehicle family.

          launch_site_id: Seradata Launch Site ID.

          launch_site_name: Launch Site Name.

          launch_type: Seradata launch type (e.g. Launched, Future, etc).

          launch_vehicle_id: Seradata launch ID.

          leased: Boolean indicating if the spacecraft was leased.

          life_lost: Spacecraft life lost as a percent fraction.

          lon: Spacecraft latest longitude in degrees.

          mass_category: Mass category (e.g. 2500 - 3500kg - Large Satellite, 10 - 100 kg -
              Microsatellite, etc).

          name_at_launch: Spacecraft name at launch.

          new_cost: Cost of spacecraft at new in M USD.

          notes: Notes on the spacecraft.

          num_humans: Number of humans carried on spacecraft.

          operator: Spacecraft operator name.

          operator_country: Spacecraft operator country.

          orbit_category: Spacecraft orbit category (e.g GEO, LEO, etc).

          orbit_sub_category: Spacecraft sub orbit category (e.g LEO - Sun-synchronous, Geostationary, etc).

          order_date: Spacecraft order date.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          owner: Spacecraft owner name.

          owner_country: Spacecraft owner country.

          perigee: Perigee in km.

          period: Spacecraft period in minutes.

          primary_mission_group: Spacecraft primary mission and group.

          prime_manufacturer_org_id: UUID of the prime manufacturer organization, if available.

          program_name: Spacecraft program name.

          quantity: Spacecraft quantity.

          reusable_flights: Spacecraft reusable flights.

          reused_hull_name: Spacecraft reused hull name.

          sector: Seradata sector (e.g. Commercial, Military, Civil/Other).

          serial_number: Spacecraft serial number.

          stabilizer: Spacecraft stabilizer (e.g. 3-Axis, Gravity Gradiant, etc).

          status: Spacecraft status (e.g. Inactive - Retired, Inactive - Re-entered, Active, etc).

          total_claims: Number of insurance claims for this spacecraft.

          total_fatalities: Number of fatalities related to this spacecraft.

          total_injuries: Number of injuries related to this spacecraft.

          total_payload_power: Mass dry in kg.

          youtube_launch_link: Youtube link of launch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/seradataspacecraftdetails/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "additional_missions_groups": additional_missions_groups,
                    "altitude": altitude,
                    "annual_insured_depreciation_factor": annual_insured_depreciation_factor,
                    "annual_insured_depreciation_factor_estimated": annual_insured_depreciation_factor_estimated,
                    "apogee": apogee,
                    "bus_id": bus_id,
                    "capability_lost": capability_lost,
                    "capacity_lost": capacity_lost,
                    "catalog_number": catalog_number,
                    "collision_risk_cm": collision_risk_cm,
                    "collision_risk_mm": collision_risk_mm,
                    "combined_cost_estimated": combined_cost_estimated,
                    "combined_new_cost": combined_new_cost,
                    "commercial_launch": commercial_launch,
                    "constellation": constellation,
                    "cost_estimated": cost_estimated,
                    "cubesat_dispenser_type": cubesat_dispenser_type,
                    "current_age": current_age,
                    "date_of_observation": date_of_observation,
                    "description": description,
                    "design_life": design_life,
                    "dry_mass": dry_mass,
                    "expected_life": expected_life,
                    "geo_position": geo_position,
                    "id_on_orbit": id_on_orbit,
                    "inclination": inclination,
                    "insurance_losses_total": insurance_losses_total,
                    "insurance_notes": insurance_notes,
                    "insurance_premium_at_launch": insurance_premium_at_launch,
                    "insurance_premium_at_launch_estimated": insurance_premium_at_launch_estimated,
                    "insured_at_launch": insured_at_launch,
                    "insured_value_at_launch": insured_value_at_launch,
                    "insured_value_launch_estimated": insured_value_launch_estimated,
                    "intl_number": intl_number,
                    "lat": lat,
                    "launch_arranger": launch_arranger,
                    "launch_arranger_country": launch_arranger_country,
                    "launch_characteristic": launch_characteristic,
                    "launch_cost": launch_cost,
                    "launch_cost_estimated": launch_cost_estimated,
                    "launch_country": launch_country,
                    "launch_date": launch_date,
                    "launch_date_remarks": launch_date_remarks,
                    "launch_id": launch_id,
                    "launch_mass": launch_mass,
                    "launch_notes": launch_notes,
                    "launch_number": launch_number,
                    "launch_provider": launch_provider,
                    "launch_provider_country": launch_provider_country,
                    "launch_provider_flight_number": launch_provider_flight_number,
                    "launch_site_id": launch_site_id,
                    "launch_site_name": launch_site_name,
                    "launch_type": launch_type,
                    "launch_vehicle_id": launch_vehicle_id,
                    "leased": leased,
                    "life_lost": life_lost,
                    "lon": lon,
                    "mass_category": mass_category,
                    "name_at_launch": name_at_launch,
                    "new_cost": new_cost,
                    "notes": notes,
                    "num_humans": num_humans,
                    "operator": operator,
                    "operator_country": operator_country,
                    "orbit_category": orbit_category,
                    "orbit_sub_category": orbit_sub_category,
                    "order_date": order_date,
                    "origin": origin,
                    "owner": owner,
                    "owner_country": owner_country,
                    "perigee": perigee,
                    "period": period,
                    "primary_mission_group": primary_mission_group,
                    "prime_manufacturer_org_id": prime_manufacturer_org_id,
                    "program_name": program_name,
                    "quantity": quantity,
                    "reusable_flights": reusable_flights,
                    "reused_hull_name": reused_hull_name,
                    "sector": sector,
                    "serial_number": serial_number,
                    "stabilizer": stabilizer,
                    "status": status,
                    "total_claims": total_claims,
                    "total_fatalities": total_fatalities,
                    "total_injuries": total_injuries,
                    "total_payload_power": total_payload_power,
                    "youtube_launch_link": youtube_launch_link,
                },
                seradata_spacecraft_detail_update_params.SeradataSpacecraftDetailUpdateParams,
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
    ) -> AsyncPaginator[SeradataSpacecraftDetailListResponse, AsyncOffsetPage[SeradataSpacecraftDetailListResponse]]:
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
            "/udl/seradataspacecraftdetails",
            page=AsyncOffsetPage[SeradataSpacecraftDetailListResponse],
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
                    seradata_spacecraft_detail_list_params.SeradataSpacecraftDetailListParams,
                ),
            ),
            model=SeradataSpacecraftDetailListResponse,
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
        Service operation to delete an SeradataSpacecraftDetails specified by the passed
        ID path parameter. A specific role is required to perform this service
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
            f"/udl/seradataspacecraftdetails/{id}",
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
            "/udl/seradataspacecraftdetails/count",
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
                    seradata_spacecraft_detail_count_params.SeradataSpacecraftDetailCountParams,
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
    ) -> SeradataSpacecraftDetailGetResponse:
        """
        Service operation to get a single SeradataSpacecraftDetails by its unique ID
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
            f"/udl/seradataspacecraftdetails/{id}",
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
                    seradata_spacecraft_detail_get_params.SeradataSpacecraftDetailGetParams,
                ),
            ),
            cast_to=SeradataSpacecraftDetailGetResponse,
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
            "/udl/seradataspacecraftdetails/queryhelp",
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
    ) -> SeradataSpacecraftDetailTupleResponse:
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
            "/udl/seradataspacecraftdetails/tuple",
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
                    seradata_spacecraft_detail_tuple_params.SeradataSpacecraftDetailTupleParams,
                ),
            ),
            cast_to=SeradataSpacecraftDetailTupleResponse,
        )


class SeradataSpacecraftDetailsResourceWithRawResponse:
    def __init__(self, seradata_spacecraft_details: SeradataSpacecraftDetailsResource) -> None:
        self._seradata_spacecraft_details = seradata_spacecraft_details

        self.create = to_raw_response_wrapper(
            seradata_spacecraft_details.create,
        )
        self.update = to_raw_response_wrapper(
            seradata_spacecraft_details.update,
        )
        self.list = to_raw_response_wrapper(
            seradata_spacecraft_details.list,
        )
        self.delete = to_raw_response_wrapper(
            seradata_spacecraft_details.delete,
        )
        self.count = to_raw_response_wrapper(
            seradata_spacecraft_details.count,
        )
        self.get = to_raw_response_wrapper(
            seradata_spacecraft_details.get,
        )
        self.queryhelp = to_raw_response_wrapper(
            seradata_spacecraft_details.queryhelp,
        )
        self.tuple = to_raw_response_wrapper(
            seradata_spacecraft_details.tuple,
        )


class AsyncSeradataSpacecraftDetailsResourceWithRawResponse:
    def __init__(self, seradata_spacecraft_details: AsyncSeradataSpacecraftDetailsResource) -> None:
        self._seradata_spacecraft_details = seradata_spacecraft_details

        self.create = async_to_raw_response_wrapper(
            seradata_spacecraft_details.create,
        )
        self.update = async_to_raw_response_wrapper(
            seradata_spacecraft_details.update,
        )
        self.list = async_to_raw_response_wrapper(
            seradata_spacecraft_details.list,
        )
        self.delete = async_to_raw_response_wrapper(
            seradata_spacecraft_details.delete,
        )
        self.count = async_to_raw_response_wrapper(
            seradata_spacecraft_details.count,
        )
        self.get = async_to_raw_response_wrapper(
            seradata_spacecraft_details.get,
        )
        self.queryhelp = async_to_raw_response_wrapper(
            seradata_spacecraft_details.queryhelp,
        )
        self.tuple = async_to_raw_response_wrapper(
            seradata_spacecraft_details.tuple,
        )


class SeradataSpacecraftDetailsResourceWithStreamingResponse:
    def __init__(self, seradata_spacecraft_details: SeradataSpacecraftDetailsResource) -> None:
        self._seradata_spacecraft_details = seradata_spacecraft_details

        self.create = to_streamed_response_wrapper(
            seradata_spacecraft_details.create,
        )
        self.update = to_streamed_response_wrapper(
            seradata_spacecraft_details.update,
        )
        self.list = to_streamed_response_wrapper(
            seradata_spacecraft_details.list,
        )
        self.delete = to_streamed_response_wrapper(
            seradata_spacecraft_details.delete,
        )
        self.count = to_streamed_response_wrapper(
            seradata_spacecraft_details.count,
        )
        self.get = to_streamed_response_wrapper(
            seradata_spacecraft_details.get,
        )
        self.queryhelp = to_streamed_response_wrapper(
            seradata_spacecraft_details.queryhelp,
        )
        self.tuple = to_streamed_response_wrapper(
            seradata_spacecraft_details.tuple,
        )


class AsyncSeradataSpacecraftDetailsResourceWithStreamingResponse:
    def __init__(self, seradata_spacecraft_details: AsyncSeradataSpacecraftDetailsResource) -> None:
        self._seradata_spacecraft_details = seradata_spacecraft_details

        self.create = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.create,
        )
        self.update = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.update,
        )
        self.list = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.count,
        )
        self.get = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.get,
        )
        self.queryhelp = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.queryhelp,
        )
        self.tuple = async_to_streamed_response_wrapper(
            seradata_spacecraft_details.tuple,
        )
