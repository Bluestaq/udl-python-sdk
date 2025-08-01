# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    bus_list_params,
    bus_count_params,
    bus_tuple_params,
    bus_create_params,
    bus_update_params,
    bus_retrieve_params,
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
from ..types.bus_abridged import BusAbridged
from ..types.shared.bus_full import BusFull
from ..types.bus_tuple_response import BusTupleResponse
from ..types.entity_ingest_param import EntityIngestParam
from ..types.bus_query_help_response import BusQueryHelpResponse

__all__ = ["BusesResource", "AsyncBusesResource"]


class BusesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return BusesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        aocs_notes: str | NotGiven = NOT_GIVEN,
        avg_dry_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_power: float | NotGiven = NOT_GIVEN,
        avg_spacecraft_power: float | NotGiven = NOT_GIVEN,
        avg_wet_mass: float | NotGiven = NOT_GIVEN,
        body_dimension_x: float | NotGiven = NOT_GIVEN,
        body_dimension_y: float | NotGiven = NOT_GIVEN,
        body_dimension_z: float | NotGiven = NOT_GIVEN,
        bus_kit_designer_org_id: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        generic: bool | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_x: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_y: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_z: float | NotGiven = NOT_GIVEN,
        main_computer_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        max_bol_power_lower: float | NotGiven = NOT_GIVEN,
        max_bol_power_upper: float | NotGiven = NOT_GIVEN,
        max_bol_station_mass: float | NotGiven = NOT_GIVEN,
        max_dry_mass: float | NotGiven = NOT_GIVEN,
        max_eol_power_lower: float | NotGiven = NOT_GIVEN,
        max_eol_power_upper: float | NotGiven = NOT_GIVEN,
        max_launch_mass_lower: float | NotGiven = NOT_GIVEN,
        max_launch_mass_upper: float | NotGiven = NOT_GIVEN,
        max_payload_mass: float | NotGiven = NOT_GIVEN,
        max_payload_power: float | NotGiven = NOT_GIVEN,
        max_spacecraft_power: float | NotGiven = NOT_GIVEN,
        max_wet_mass: float | NotGiven = NOT_GIVEN,
        median_dry_mass: float | NotGiven = NOT_GIVEN,
        median_wet_mass: float | NotGiven = NOT_GIVEN,
        min_dry_mass: float | NotGiven = NOT_GIVEN,
        min_wet_mass: float | NotGiven = NOT_GIVEN,
        num_orbit_type: int | NotGiven = NOT_GIVEN,
        oap_payload_power: float | NotGiven = NOT_GIVEN,
        oap_spacecraft_power: float | NotGiven = NOT_GIVEN,
        orbit_types: List[str] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_dimension_x: float | NotGiven = NOT_GIVEN,
        payload_dimension_y: float | NotGiven = NOT_GIVEN,
        payload_dimension_z: float | NotGiven = NOT_GIVEN,
        payload_volume: float | NotGiven = NOT_GIVEN,
        power_category: str | NotGiven = NOT_GIVEN,
        telemetry_tracking_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Bus as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
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

          name: Name of this bus.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          aocs_notes: Attitude and Orbital Control Notes/description for the bus.

          avg_dry_mass: Average mass of this bus without payloads or fuel, in kilograms.

          avg_payload_mass: Average mass available on this bus for payloads, in kilograms.

          avg_payload_power: Average power available on this bus for payloads, in kilowatts.

          avg_spacecraft_power: Average power available on this bus, in kilowatts.

          avg_wet_mass: Average mass of this bus with fuel, but without payloads, in kilograms.

          body_dimension_x: Body dimension in X direction pertaining to length, in meters.

          body_dimension_y: Body dimension in Y direction pertaining to height, in meters.

          body_dimension_z: Body dimension in Z direction pertaining to width, in meters.

          bus_kit_designer_org_id: Unique identifier of the organization which designs the bus kit.

          country_code: Country where this bus was manufactured. This value is typically the ISO 3166
              Alpha-2 two-character country code, however it can also represent various
              consortiums that do not appear in the ISO document. The code must correspond to
              an existing country in the UDL’s country API. Call udl/country/{code} to get any
              associated FIPS code, ISO Alpha-3 code, or alternate code values that exist for
              the specified country code.

          description: Notes/description of the bus.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          generic: Boolean indicating if this bus is generic.

          id_entity: ID of the parent entity for this bus.

          launch_envelope_dimension_x: Launch envelope dimension in X direction, in meters.

          launch_envelope_dimension_y: Launch envelope dimension in Y direction, in meters.

          launch_envelope_dimension_z: Launch envelope dimension in Z direction, in meters.

          main_computer_manufacturer_org_id: Unique identifier of the organization which manufactures the main onboard
              computer for this bus.

          manufacturer_org_id: Unique identifier of the organization which manufactures this bus.

          mass_category:
              Mass category of this bus (e.g. 1 - 10 kg: Nanosatellite, 10 - 100 kg:
              Microsatellite, 100 - 500 kg: Minisatellite, 1000 - 2500kg: Medium satellite,
              etc.).

          max_bol_power_lower: Maximum power at beginning of life, lower bounds, in kilowatts.

          max_bol_power_upper: Maximum power at beginning of life, upper bounds, in kilowatts.

          max_bol_station_mass: Maximum mass on station at beginning of life, in kilograms.

          max_dry_mass: Maximum mass of this bus without payloads or fuel, in kilograms.

          max_eol_power_lower: Maximum power at end of life, lower bounds, in kilowatts.

          max_eol_power_upper: Maximum power at end of life, upper bounds, in kilowatts.

          max_launch_mass_lower: Maximum mass at launch, lower bounds, in kilograms.

          max_launch_mass_upper: Maximum mass at launch, upper bounds, in kilograms.

          max_payload_mass: Maximum payload mass available, in kilograms.

          max_payload_power: Maximum payload power available, in kilowatts.

          max_spacecraft_power: Maximum power available on this bus, in kilowatts.

          max_wet_mass: Maximum mass of this bus with fuel, but without payloads, in kilograms.

          median_dry_mass: Median mass of this bus without payloads or fuel, in kilograms.

          median_wet_mass: Median mass of this bus with fuel, but without payloads, in kilograms.

          min_dry_mass: Minimum mass of this bus without payloads or fuel, in kilograms.

          min_wet_mass: Minimum mass of this bus with fuel, but without payloads, in kilograms.

          num_orbit_type: The number of orbit types this bus can support.

          oap_payload_power: Orbit averaged power (the power averaged over one orbit) available on this bus
              for payloads, in kilowatts.

          oap_spacecraft_power: Orbit averaged power (the power averaged over one orbit) available on this bus,
              in kilowatts.

          orbit_types: Array of orbit types this bus can support (e.g. GEO, LEO, etc.). Must contain
              the same number of elements as the value of numOrbitType.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_dimension_x: The radial dimension available on this bus for payloads, in meters.

          payload_dimension_y: The in-track dimension available on this bus for payloads, in meters.

          payload_dimension_z: The cross-track dimension available on this bus for payloads, in meters.

          payload_volume: The volume available on this bus for payloads, in cubic meters.

          power_category: Power category of this bus (e.g. 0-1kW low power, etc).

          telemetry_tracking_manufacturer_org_id: Unique identifier of the organization which manufactures the telemetry tracking
              and command subsystem for this bus.

          type: Type of this bus.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/udl/bus",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "id": id,
                    "aocs_notes": aocs_notes,
                    "avg_dry_mass": avg_dry_mass,
                    "avg_payload_mass": avg_payload_mass,
                    "avg_payload_power": avg_payload_power,
                    "avg_spacecraft_power": avg_spacecraft_power,
                    "avg_wet_mass": avg_wet_mass,
                    "body_dimension_x": body_dimension_x,
                    "body_dimension_y": body_dimension_y,
                    "body_dimension_z": body_dimension_z,
                    "bus_kit_designer_org_id": bus_kit_designer_org_id,
                    "country_code": country_code,
                    "description": description,
                    "entity": entity,
                    "generic": generic,
                    "id_entity": id_entity,
                    "launch_envelope_dimension_x": launch_envelope_dimension_x,
                    "launch_envelope_dimension_y": launch_envelope_dimension_y,
                    "launch_envelope_dimension_z": launch_envelope_dimension_z,
                    "main_computer_manufacturer_org_id": main_computer_manufacturer_org_id,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass_category": mass_category,
                    "max_bol_power_lower": max_bol_power_lower,
                    "max_bol_power_upper": max_bol_power_upper,
                    "max_bol_station_mass": max_bol_station_mass,
                    "max_dry_mass": max_dry_mass,
                    "max_eol_power_lower": max_eol_power_lower,
                    "max_eol_power_upper": max_eol_power_upper,
                    "max_launch_mass_lower": max_launch_mass_lower,
                    "max_launch_mass_upper": max_launch_mass_upper,
                    "max_payload_mass": max_payload_mass,
                    "max_payload_power": max_payload_power,
                    "max_spacecraft_power": max_spacecraft_power,
                    "max_wet_mass": max_wet_mass,
                    "median_dry_mass": median_dry_mass,
                    "median_wet_mass": median_wet_mass,
                    "min_dry_mass": min_dry_mass,
                    "min_wet_mass": min_wet_mass,
                    "num_orbit_type": num_orbit_type,
                    "oap_payload_power": oap_payload_power,
                    "oap_spacecraft_power": oap_spacecraft_power,
                    "orbit_types": orbit_types,
                    "origin": origin,
                    "payload_dimension_x": payload_dimension_x,
                    "payload_dimension_y": payload_dimension_y,
                    "payload_dimension_z": payload_dimension_z,
                    "payload_volume": payload_volume,
                    "power_category": power_category,
                    "telemetry_tracking_manufacturer_org_id": telemetry_tracking_manufacturer_org_id,
                    "type": type,
                },
                bus_create_params.BusCreateParams,
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
    ) -> BusFull:
        """
        Service operation to get a single Bus record by its unique ID passed as a path
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
            f"/udl/bus/{id}",
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
                    bus_retrieve_params.BusRetrieveParams,
                ),
            ),
            cast_to=BusFull,
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
        aocs_notes: str | NotGiven = NOT_GIVEN,
        avg_dry_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_power: float | NotGiven = NOT_GIVEN,
        avg_spacecraft_power: float | NotGiven = NOT_GIVEN,
        avg_wet_mass: float | NotGiven = NOT_GIVEN,
        body_dimension_x: float | NotGiven = NOT_GIVEN,
        body_dimension_y: float | NotGiven = NOT_GIVEN,
        body_dimension_z: float | NotGiven = NOT_GIVEN,
        bus_kit_designer_org_id: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        generic: bool | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_x: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_y: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_z: float | NotGiven = NOT_GIVEN,
        main_computer_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        max_bol_power_lower: float | NotGiven = NOT_GIVEN,
        max_bol_power_upper: float | NotGiven = NOT_GIVEN,
        max_bol_station_mass: float | NotGiven = NOT_GIVEN,
        max_dry_mass: float | NotGiven = NOT_GIVEN,
        max_eol_power_lower: float | NotGiven = NOT_GIVEN,
        max_eol_power_upper: float | NotGiven = NOT_GIVEN,
        max_launch_mass_lower: float | NotGiven = NOT_GIVEN,
        max_launch_mass_upper: float | NotGiven = NOT_GIVEN,
        max_payload_mass: float | NotGiven = NOT_GIVEN,
        max_payload_power: float | NotGiven = NOT_GIVEN,
        max_spacecraft_power: float | NotGiven = NOT_GIVEN,
        max_wet_mass: float | NotGiven = NOT_GIVEN,
        median_dry_mass: float | NotGiven = NOT_GIVEN,
        median_wet_mass: float | NotGiven = NOT_GIVEN,
        min_dry_mass: float | NotGiven = NOT_GIVEN,
        min_wet_mass: float | NotGiven = NOT_GIVEN,
        num_orbit_type: int | NotGiven = NOT_GIVEN,
        oap_payload_power: float | NotGiven = NOT_GIVEN,
        oap_spacecraft_power: float | NotGiven = NOT_GIVEN,
        orbit_types: List[str] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_dimension_x: float | NotGiven = NOT_GIVEN,
        payload_dimension_y: float | NotGiven = NOT_GIVEN,
        payload_dimension_z: float | NotGiven = NOT_GIVEN,
        payload_volume: float | NotGiven = NOT_GIVEN,
        power_category: str | NotGiven = NOT_GIVEN,
        telemetry_tracking_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Bus.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

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

          name: Name of this bus.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          aocs_notes: Attitude and Orbital Control Notes/description for the bus.

          avg_dry_mass: Average mass of this bus without payloads or fuel, in kilograms.

          avg_payload_mass: Average mass available on this bus for payloads, in kilograms.

          avg_payload_power: Average power available on this bus for payloads, in kilowatts.

          avg_spacecraft_power: Average power available on this bus, in kilowatts.

          avg_wet_mass: Average mass of this bus with fuel, but without payloads, in kilograms.

          body_dimension_x: Body dimension in X direction pertaining to length, in meters.

          body_dimension_y: Body dimension in Y direction pertaining to height, in meters.

          body_dimension_z: Body dimension in Z direction pertaining to width, in meters.

          bus_kit_designer_org_id: Unique identifier of the organization which designs the bus kit.

          country_code: Country where this bus was manufactured. This value is typically the ISO 3166
              Alpha-2 two-character country code, however it can also represent various
              consortiums that do not appear in the ISO document. The code must correspond to
              an existing country in the UDL’s country API. Call udl/country/{code} to get any
              associated FIPS code, ISO Alpha-3 code, or alternate code values that exist for
              the specified country code.

          description: Notes/description of the bus.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          generic: Boolean indicating if this bus is generic.

          id_entity: ID of the parent entity for this bus.

          launch_envelope_dimension_x: Launch envelope dimension in X direction, in meters.

          launch_envelope_dimension_y: Launch envelope dimension in Y direction, in meters.

          launch_envelope_dimension_z: Launch envelope dimension in Z direction, in meters.

          main_computer_manufacturer_org_id: Unique identifier of the organization which manufactures the main onboard
              computer for this bus.

          manufacturer_org_id: Unique identifier of the organization which manufactures this bus.

          mass_category:
              Mass category of this bus (e.g. 1 - 10 kg: Nanosatellite, 10 - 100 kg:
              Microsatellite, 100 - 500 kg: Minisatellite, 1000 - 2500kg: Medium satellite,
              etc.).

          max_bol_power_lower: Maximum power at beginning of life, lower bounds, in kilowatts.

          max_bol_power_upper: Maximum power at beginning of life, upper bounds, in kilowatts.

          max_bol_station_mass: Maximum mass on station at beginning of life, in kilograms.

          max_dry_mass: Maximum mass of this bus without payloads or fuel, in kilograms.

          max_eol_power_lower: Maximum power at end of life, lower bounds, in kilowatts.

          max_eol_power_upper: Maximum power at end of life, upper bounds, in kilowatts.

          max_launch_mass_lower: Maximum mass at launch, lower bounds, in kilograms.

          max_launch_mass_upper: Maximum mass at launch, upper bounds, in kilograms.

          max_payload_mass: Maximum payload mass available, in kilograms.

          max_payload_power: Maximum payload power available, in kilowatts.

          max_spacecraft_power: Maximum power available on this bus, in kilowatts.

          max_wet_mass: Maximum mass of this bus with fuel, but without payloads, in kilograms.

          median_dry_mass: Median mass of this bus without payloads or fuel, in kilograms.

          median_wet_mass: Median mass of this bus with fuel, but without payloads, in kilograms.

          min_dry_mass: Minimum mass of this bus without payloads or fuel, in kilograms.

          min_wet_mass: Minimum mass of this bus with fuel, but without payloads, in kilograms.

          num_orbit_type: The number of orbit types this bus can support.

          oap_payload_power: Orbit averaged power (the power averaged over one orbit) available on this bus
              for payloads, in kilowatts.

          oap_spacecraft_power: Orbit averaged power (the power averaged over one orbit) available on this bus,
              in kilowatts.

          orbit_types: Array of orbit types this bus can support (e.g. GEO, LEO, etc.). Must contain
              the same number of elements as the value of numOrbitType.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_dimension_x: The radial dimension available on this bus for payloads, in meters.

          payload_dimension_y: The in-track dimension available on this bus for payloads, in meters.

          payload_dimension_z: The cross-track dimension available on this bus for payloads, in meters.

          payload_volume: The volume available on this bus for payloads, in cubic meters.

          power_category: Power category of this bus (e.g. 0-1kW low power, etc).

          telemetry_tracking_manufacturer_org_id: Unique identifier of the organization which manufactures the telemetry tracking
              and command subsystem for this bus.

          type: Type of this bus.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/udl/bus/{path_id}",
            body=maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "aocs_notes": aocs_notes,
                    "avg_dry_mass": avg_dry_mass,
                    "avg_payload_mass": avg_payload_mass,
                    "avg_payload_power": avg_payload_power,
                    "avg_spacecraft_power": avg_spacecraft_power,
                    "avg_wet_mass": avg_wet_mass,
                    "body_dimension_x": body_dimension_x,
                    "body_dimension_y": body_dimension_y,
                    "body_dimension_z": body_dimension_z,
                    "bus_kit_designer_org_id": bus_kit_designer_org_id,
                    "country_code": country_code,
                    "description": description,
                    "entity": entity,
                    "generic": generic,
                    "id_entity": id_entity,
                    "launch_envelope_dimension_x": launch_envelope_dimension_x,
                    "launch_envelope_dimension_y": launch_envelope_dimension_y,
                    "launch_envelope_dimension_z": launch_envelope_dimension_z,
                    "main_computer_manufacturer_org_id": main_computer_manufacturer_org_id,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass_category": mass_category,
                    "max_bol_power_lower": max_bol_power_lower,
                    "max_bol_power_upper": max_bol_power_upper,
                    "max_bol_station_mass": max_bol_station_mass,
                    "max_dry_mass": max_dry_mass,
                    "max_eol_power_lower": max_eol_power_lower,
                    "max_eol_power_upper": max_eol_power_upper,
                    "max_launch_mass_lower": max_launch_mass_lower,
                    "max_launch_mass_upper": max_launch_mass_upper,
                    "max_payload_mass": max_payload_mass,
                    "max_payload_power": max_payload_power,
                    "max_spacecraft_power": max_spacecraft_power,
                    "max_wet_mass": max_wet_mass,
                    "median_dry_mass": median_dry_mass,
                    "median_wet_mass": median_wet_mass,
                    "min_dry_mass": min_dry_mass,
                    "min_wet_mass": min_wet_mass,
                    "num_orbit_type": num_orbit_type,
                    "oap_payload_power": oap_payload_power,
                    "oap_spacecraft_power": oap_spacecraft_power,
                    "orbit_types": orbit_types,
                    "origin": origin,
                    "payload_dimension_x": payload_dimension_x,
                    "payload_dimension_y": payload_dimension_y,
                    "payload_dimension_z": payload_dimension_z,
                    "payload_volume": payload_volume,
                    "power_category": power_category,
                    "telemetry_tracking_manufacturer_org_id": telemetry_tracking_manufacturer_org_id,
                    "type": type,
                },
                bus_update_params.BusUpdateParams,
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
    ) -> SyncOffsetPage[BusAbridged]:
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
            "/udl/bus",
            page=SyncOffsetPage[BusAbridged],
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
                    bus_list_params.BusListParams,
                ),
            ),
            model=BusAbridged,
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
        Service operation to delete a Bus object specified by the passed ID path
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
            f"/udl/bus/{id}",
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
            "/udl/bus/count",
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
                    bus_count_params.BusCountParams,
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
    ) -> BusQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return self._get(
            "/udl/bus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusQueryHelpResponse,
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
    ) -> BusTupleResponse:
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
            "/udl/bus/tuple",
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
                    bus_tuple_params.BusTupleParams,
                ),
            ),
            cast_to=BusTupleResponse,
        )


class AsyncBusesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Bluestaq/udl-python-sdk#with_streaming_response
        """
        return AsyncBusesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        classification_marking: str,
        data_mode: Literal["REAL", "TEST", "SIMULATED", "EXERCISE"],
        name: str,
        source: str,
        id: str | NotGiven = NOT_GIVEN,
        aocs_notes: str | NotGiven = NOT_GIVEN,
        avg_dry_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_power: float | NotGiven = NOT_GIVEN,
        avg_spacecraft_power: float | NotGiven = NOT_GIVEN,
        avg_wet_mass: float | NotGiven = NOT_GIVEN,
        body_dimension_x: float | NotGiven = NOT_GIVEN,
        body_dimension_y: float | NotGiven = NOT_GIVEN,
        body_dimension_z: float | NotGiven = NOT_GIVEN,
        bus_kit_designer_org_id: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        generic: bool | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_x: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_y: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_z: float | NotGiven = NOT_GIVEN,
        main_computer_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        max_bol_power_lower: float | NotGiven = NOT_GIVEN,
        max_bol_power_upper: float | NotGiven = NOT_GIVEN,
        max_bol_station_mass: float | NotGiven = NOT_GIVEN,
        max_dry_mass: float | NotGiven = NOT_GIVEN,
        max_eol_power_lower: float | NotGiven = NOT_GIVEN,
        max_eol_power_upper: float | NotGiven = NOT_GIVEN,
        max_launch_mass_lower: float | NotGiven = NOT_GIVEN,
        max_launch_mass_upper: float | NotGiven = NOT_GIVEN,
        max_payload_mass: float | NotGiven = NOT_GIVEN,
        max_payload_power: float | NotGiven = NOT_GIVEN,
        max_spacecraft_power: float | NotGiven = NOT_GIVEN,
        max_wet_mass: float | NotGiven = NOT_GIVEN,
        median_dry_mass: float | NotGiven = NOT_GIVEN,
        median_wet_mass: float | NotGiven = NOT_GIVEN,
        min_dry_mass: float | NotGiven = NOT_GIVEN,
        min_wet_mass: float | NotGiven = NOT_GIVEN,
        num_orbit_type: int | NotGiven = NOT_GIVEN,
        oap_payload_power: float | NotGiven = NOT_GIVEN,
        oap_spacecraft_power: float | NotGiven = NOT_GIVEN,
        orbit_types: List[str] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_dimension_x: float | NotGiven = NOT_GIVEN,
        payload_dimension_y: float | NotGiven = NOT_GIVEN,
        payload_dimension_z: float | NotGiven = NOT_GIVEN,
        payload_volume: float | NotGiven = NOT_GIVEN,
        power_category: str | NotGiven = NOT_GIVEN,
        telemetry_tracking_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Service operation to take a single Bus as a POST body and ingest into the
        database. A specific role is required to perform this service operation. Please
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

          name: Name of this bus.

          source: Source of the data.

          id: Unique identifier of the record, auto-generated by the system.

          aocs_notes: Attitude and Orbital Control Notes/description for the bus.

          avg_dry_mass: Average mass of this bus without payloads or fuel, in kilograms.

          avg_payload_mass: Average mass available on this bus for payloads, in kilograms.

          avg_payload_power: Average power available on this bus for payloads, in kilowatts.

          avg_spacecraft_power: Average power available on this bus, in kilowatts.

          avg_wet_mass: Average mass of this bus with fuel, but without payloads, in kilograms.

          body_dimension_x: Body dimension in X direction pertaining to length, in meters.

          body_dimension_y: Body dimension in Y direction pertaining to height, in meters.

          body_dimension_z: Body dimension in Z direction pertaining to width, in meters.

          bus_kit_designer_org_id: Unique identifier of the organization which designs the bus kit.

          country_code: Country where this bus was manufactured. This value is typically the ISO 3166
              Alpha-2 two-character country code, however it can also represent various
              consortiums that do not appear in the ISO document. The code must correspond to
              an existing country in the UDL’s country API. Call udl/country/{code} to get any
              associated FIPS code, ISO Alpha-3 code, or alternate code values that exist for
              the specified country code.

          description: Notes/description of the bus.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          generic: Boolean indicating if this bus is generic.

          id_entity: ID of the parent entity for this bus.

          launch_envelope_dimension_x: Launch envelope dimension in X direction, in meters.

          launch_envelope_dimension_y: Launch envelope dimension in Y direction, in meters.

          launch_envelope_dimension_z: Launch envelope dimension in Z direction, in meters.

          main_computer_manufacturer_org_id: Unique identifier of the organization which manufactures the main onboard
              computer for this bus.

          manufacturer_org_id: Unique identifier of the organization which manufactures this bus.

          mass_category:
              Mass category of this bus (e.g. 1 - 10 kg: Nanosatellite, 10 - 100 kg:
              Microsatellite, 100 - 500 kg: Minisatellite, 1000 - 2500kg: Medium satellite,
              etc.).

          max_bol_power_lower: Maximum power at beginning of life, lower bounds, in kilowatts.

          max_bol_power_upper: Maximum power at beginning of life, upper bounds, in kilowatts.

          max_bol_station_mass: Maximum mass on station at beginning of life, in kilograms.

          max_dry_mass: Maximum mass of this bus without payloads or fuel, in kilograms.

          max_eol_power_lower: Maximum power at end of life, lower bounds, in kilowatts.

          max_eol_power_upper: Maximum power at end of life, upper bounds, in kilowatts.

          max_launch_mass_lower: Maximum mass at launch, lower bounds, in kilograms.

          max_launch_mass_upper: Maximum mass at launch, upper bounds, in kilograms.

          max_payload_mass: Maximum payload mass available, in kilograms.

          max_payload_power: Maximum payload power available, in kilowatts.

          max_spacecraft_power: Maximum power available on this bus, in kilowatts.

          max_wet_mass: Maximum mass of this bus with fuel, but without payloads, in kilograms.

          median_dry_mass: Median mass of this bus without payloads or fuel, in kilograms.

          median_wet_mass: Median mass of this bus with fuel, but without payloads, in kilograms.

          min_dry_mass: Minimum mass of this bus without payloads or fuel, in kilograms.

          min_wet_mass: Minimum mass of this bus with fuel, but without payloads, in kilograms.

          num_orbit_type: The number of orbit types this bus can support.

          oap_payload_power: Orbit averaged power (the power averaged over one orbit) available on this bus
              for payloads, in kilowatts.

          oap_spacecraft_power: Orbit averaged power (the power averaged over one orbit) available on this bus,
              in kilowatts.

          orbit_types: Array of orbit types this bus can support (e.g. GEO, LEO, etc.). Must contain
              the same number of elements as the value of numOrbitType.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_dimension_x: The radial dimension available on this bus for payloads, in meters.

          payload_dimension_y: The in-track dimension available on this bus for payloads, in meters.

          payload_dimension_z: The cross-track dimension available on this bus for payloads, in meters.

          payload_volume: The volume available on this bus for payloads, in cubic meters.

          power_category: Power category of this bus (e.g. 0-1kW low power, etc).

          telemetry_tracking_manufacturer_org_id: Unique identifier of the organization which manufactures the telemetry tracking
              and command subsystem for this bus.

          type: Type of this bus.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/udl/bus",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "id": id,
                    "aocs_notes": aocs_notes,
                    "avg_dry_mass": avg_dry_mass,
                    "avg_payload_mass": avg_payload_mass,
                    "avg_payload_power": avg_payload_power,
                    "avg_spacecraft_power": avg_spacecraft_power,
                    "avg_wet_mass": avg_wet_mass,
                    "body_dimension_x": body_dimension_x,
                    "body_dimension_y": body_dimension_y,
                    "body_dimension_z": body_dimension_z,
                    "bus_kit_designer_org_id": bus_kit_designer_org_id,
                    "country_code": country_code,
                    "description": description,
                    "entity": entity,
                    "generic": generic,
                    "id_entity": id_entity,
                    "launch_envelope_dimension_x": launch_envelope_dimension_x,
                    "launch_envelope_dimension_y": launch_envelope_dimension_y,
                    "launch_envelope_dimension_z": launch_envelope_dimension_z,
                    "main_computer_manufacturer_org_id": main_computer_manufacturer_org_id,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass_category": mass_category,
                    "max_bol_power_lower": max_bol_power_lower,
                    "max_bol_power_upper": max_bol_power_upper,
                    "max_bol_station_mass": max_bol_station_mass,
                    "max_dry_mass": max_dry_mass,
                    "max_eol_power_lower": max_eol_power_lower,
                    "max_eol_power_upper": max_eol_power_upper,
                    "max_launch_mass_lower": max_launch_mass_lower,
                    "max_launch_mass_upper": max_launch_mass_upper,
                    "max_payload_mass": max_payload_mass,
                    "max_payload_power": max_payload_power,
                    "max_spacecraft_power": max_spacecraft_power,
                    "max_wet_mass": max_wet_mass,
                    "median_dry_mass": median_dry_mass,
                    "median_wet_mass": median_wet_mass,
                    "min_dry_mass": min_dry_mass,
                    "min_wet_mass": min_wet_mass,
                    "num_orbit_type": num_orbit_type,
                    "oap_payload_power": oap_payload_power,
                    "oap_spacecraft_power": oap_spacecraft_power,
                    "orbit_types": orbit_types,
                    "origin": origin,
                    "payload_dimension_x": payload_dimension_x,
                    "payload_dimension_y": payload_dimension_y,
                    "payload_dimension_z": payload_dimension_z,
                    "payload_volume": payload_volume,
                    "power_category": power_category,
                    "telemetry_tracking_manufacturer_org_id": telemetry_tracking_manufacturer_org_id,
                    "type": type,
                },
                bus_create_params.BusCreateParams,
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
    ) -> BusFull:
        """
        Service operation to get a single Bus record by its unique ID passed as a path
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
            f"/udl/bus/{id}",
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
                    bus_retrieve_params.BusRetrieveParams,
                ),
            ),
            cast_to=BusFull,
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
        aocs_notes: str | NotGiven = NOT_GIVEN,
        avg_dry_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_mass: float | NotGiven = NOT_GIVEN,
        avg_payload_power: float | NotGiven = NOT_GIVEN,
        avg_spacecraft_power: float | NotGiven = NOT_GIVEN,
        avg_wet_mass: float | NotGiven = NOT_GIVEN,
        body_dimension_x: float | NotGiven = NOT_GIVEN,
        body_dimension_y: float | NotGiven = NOT_GIVEN,
        body_dimension_z: float | NotGiven = NOT_GIVEN,
        bus_kit_designer_org_id: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        entity: EntityIngestParam | NotGiven = NOT_GIVEN,
        generic: bool | NotGiven = NOT_GIVEN,
        id_entity: str | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_x: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_y: float | NotGiven = NOT_GIVEN,
        launch_envelope_dimension_z: float | NotGiven = NOT_GIVEN,
        main_computer_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        mass_category: str | NotGiven = NOT_GIVEN,
        max_bol_power_lower: float | NotGiven = NOT_GIVEN,
        max_bol_power_upper: float | NotGiven = NOT_GIVEN,
        max_bol_station_mass: float | NotGiven = NOT_GIVEN,
        max_dry_mass: float | NotGiven = NOT_GIVEN,
        max_eol_power_lower: float | NotGiven = NOT_GIVEN,
        max_eol_power_upper: float | NotGiven = NOT_GIVEN,
        max_launch_mass_lower: float | NotGiven = NOT_GIVEN,
        max_launch_mass_upper: float | NotGiven = NOT_GIVEN,
        max_payload_mass: float | NotGiven = NOT_GIVEN,
        max_payload_power: float | NotGiven = NOT_GIVEN,
        max_spacecraft_power: float | NotGiven = NOT_GIVEN,
        max_wet_mass: float | NotGiven = NOT_GIVEN,
        median_dry_mass: float | NotGiven = NOT_GIVEN,
        median_wet_mass: float | NotGiven = NOT_GIVEN,
        min_dry_mass: float | NotGiven = NOT_GIVEN,
        min_wet_mass: float | NotGiven = NOT_GIVEN,
        num_orbit_type: int | NotGiven = NOT_GIVEN,
        oap_payload_power: float | NotGiven = NOT_GIVEN,
        oap_spacecraft_power: float | NotGiven = NOT_GIVEN,
        orbit_types: List[str] | NotGiven = NOT_GIVEN,
        origin: str | NotGiven = NOT_GIVEN,
        payload_dimension_x: float | NotGiven = NOT_GIVEN,
        payload_dimension_y: float | NotGiven = NOT_GIVEN,
        payload_dimension_z: float | NotGiven = NOT_GIVEN,
        payload_volume: float | NotGiven = NOT_GIVEN,
        power_category: str | NotGiven = NOT_GIVEN,
        telemetry_tracking_manufacturer_org_id: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Service operation to update a single Bus.

        A specific role is required to perform
        this service operation. Please contact the UDL team for assistance.

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

          name: Name of this bus.

          source: Source of the data.

          body_id: Unique identifier of the record, auto-generated by the system.

          aocs_notes: Attitude and Orbital Control Notes/description for the bus.

          avg_dry_mass: Average mass of this bus without payloads or fuel, in kilograms.

          avg_payload_mass: Average mass available on this bus for payloads, in kilograms.

          avg_payload_power: Average power available on this bus for payloads, in kilowatts.

          avg_spacecraft_power: Average power available on this bus, in kilowatts.

          avg_wet_mass: Average mass of this bus with fuel, but without payloads, in kilograms.

          body_dimension_x: Body dimension in X direction pertaining to length, in meters.

          body_dimension_y: Body dimension in Y direction pertaining to height, in meters.

          body_dimension_z: Body dimension in Z direction pertaining to width, in meters.

          bus_kit_designer_org_id: Unique identifier of the organization which designs the bus kit.

          country_code: Country where this bus was manufactured. This value is typically the ISO 3166
              Alpha-2 two-character country code, however it can also represent various
              consortiums that do not appear in the ISO document. The code must correspond to
              an existing country in the UDL’s country API. Call udl/country/{code} to get any
              associated FIPS code, ISO Alpha-3 code, or alternate code values that exist for
              the specified country code.

          description: Notes/description of the bus.

          entity: An entity is a generic representation of any object within a space/SSA system
              such as sensors, on-orbit objects, RF Emitters, space craft buses, etc. An
              entity can have an operating unit, a location (if terrestrial), and statuses.

          generic: Boolean indicating if this bus is generic.

          id_entity: ID of the parent entity for this bus.

          launch_envelope_dimension_x: Launch envelope dimension in X direction, in meters.

          launch_envelope_dimension_y: Launch envelope dimension in Y direction, in meters.

          launch_envelope_dimension_z: Launch envelope dimension in Z direction, in meters.

          main_computer_manufacturer_org_id: Unique identifier of the organization which manufactures the main onboard
              computer for this bus.

          manufacturer_org_id: Unique identifier of the organization which manufactures this bus.

          mass_category:
              Mass category of this bus (e.g. 1 - 10 kg: Nanosatellite, 10 - 100 kg:
              Microsatellite, 100 - 500 kg: Minisatellite, 1000 - 2500kg: Medium satellite,
              etc.).

          max_bol_power_lower: Maximum power at beginning of life, lower bounds, in kilowatts.

          max_bol_power_upper: Maximum power at beginning of life, upper bounds, in kilowatts.

          max_bol_station_mass: Maximum mass on station at beginning of life, in kilograms.

          max_dry_mass: Maximum mass of this bus without payloads or fuel, in kilograms.

          max_eol_power_lower: Maximum power at end of life, lower bounds, in kilowatts.

          max_eol_power_upper: Maximum power at end of life, upper bounds, in kilowatts.

          max_launch_mass_lower: Maximum mass at launch, lower bounds, in kilograms.

          max_launch_mass_upper: Maximum mass at launch, upper bounds, in kilograms.

          max_payload_mass: Maximum payload mass available, in kilograms.

          max_payload_power: Maximum payload power available, in kilowatts.

          max_spacecraft_power: Maximum power available on this bus, in kilowatts.

          max_wet_mass: Maximum mass of this bus with fuel, but without payloads, in kilograms.

          median_dry_mass: Median mass of this bus without payloads or fuel, in kilograms.

          median_wet_mass: Median mass of this bus with fuel, but without payloads, in kilograms.

          min_dry_mass: Minimum mass of this bus without payloads or fuel, in kilograms.

          min_wet_mass: Minimum mass of this bus with fuel, but without payloads, in kilograms.

          num_orbit_type: The number of orbit types this bus can support.

          oap_payload_power: Orbit averaged power (the power averaged over one orbit) available on this bus
              for payloads, in kilowatts.

          oap_spacecraft_power: Orbit averaged power (the power averaged over one orbit) available on this bus,
              in kilowatts.

          orbit_types: Array of orbit types this bus can support (e.g. GEO, LEO, etc.). Must contain
              the same number of elements as the value of numOrbitType.

          origin: Originating system or organization which produced the data, if different from
              the source. The origin may be different than the source if the source was a
              mediating system which forwarded the data on behalf of the origin system. If
              null, the source may be assumed to be the origin.

          payload_dimension_x: The radial dimension available on this bus for payloads, in meters.

          payload_dimension_y: The in-track dimension available on this bus for payloads, in meters.

          payload_dimension_z: The cross-track dimension available on this bus for payloads, in meters.

          payload_volume: The volume available on this bus for payloads, in cubic meters.

          power_category: Power category of this bus (e.g. 0-1kW low power, etc).

          telemetry_tracking_manufacturer_org_id: Unique identifier of the organization which manufactures the telemetry tracking
              and command subsystem for this bus.

          type: Type of this bus.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/udl/bus/{path_id}",
            body=await async_maybe_transform(
                {
                    "classification_marking": classification_marking,
                    "data_mode": data_mode,
                    "name": name,
                    "source": source,
                    "body_id": body_id,
                    "aocs_notes": aocs_notes,
                    "avg_dry_mass": avg_dry_mass,
                    "avg_payload_mass": avg_payload_mass,
                    "avg_payload_power": avg_payload_power,
                    "avg_spacecraft_power": avg_spacecraft_power,
                    "avg_wet_mass": avg_wet_mass,
                    "body_dimension_x": body_dimension_x,
                    "body_dimension_y": body_dimension_y,
                    "body_dimension_z": body_dimension_z,
                    "bus_kit_designer_org_id": bus_kit_designer_org_id,
                    "country_code": country_code,
                    "description": description,
                    "entity": entity,
                    "generic": generic,
                    "id_entity": id_entity,
                    "launch_envelope_dimension_x": launch_envelope_dimension_x,
                    "launch_envelope_dimension_y": launch_envelope_dimension_y,
                    "launch_envelope_dimension_z": launch_envelope_dimension_z,
                    "main_computer_manufacturer_org_id": main_computer_manufacturer_org_id,
                    "manufacturer_org_id": manufacturer_org_id,
                    "mass_category": mass_category,
                    "max_bol_power_lower": max_bol_power_lower,
                    "max_bol_power_upper": max_bol_power_upper,
                    "max_bol_station_mass": max_bol_station_mass,
                    "max_dry_mass": max_dry_mass,
                    "max_eol_power_lower": max_eol_power_lower,
                    "max_eol_power_upper": max_eol_power_upper,
                    "max_launch_mass_lower": max_launch_mass_lower,
                    "max_launch_mass_upper": max_launch_mass_upper,
                    "max_payload_mass": max_payload_mass,
                    "max_payload_power": max_payload_power,
                    "max_spacecraft_power": max_spacecraft_power,
                    "max_wet_mass": max_wet_mass,
                    "median_dry_mass": median_dry_mass,
                    "median_wet_mass": median_wet_mass,
                    "min_dry_mass": min_dry_mass,
                    "min_wet_mass": min_wet_mass,
                    "num_orbit_type": num_orbit_type,
                    "oap_payload_power": oap_payload_power,
                    "oap_spacecraft_power": oap_spacecraft_power,
                    "orbit_types": orbit_types,
                    "origin": origin,
                    "payload_dimension_x": payload_dimension_x,
                    "payload_dimension_y": payload_dimension_y,
                    "payload_dimension_z": payload_dimension_z,
                    "payload_volume": payload_volume,
                    "power_category": power_category,
                    "telemetry_tracking_manufacturer_org_id": telemetry_tracking_manufacturer_org_id,
                    "type": type,
                },
                bus_update_params.BusUpdateParams,
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
    ) -> AsyncPaginator[BusAbridged, AsyncOffsetPage[BusAbridged]]:
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
            "/udl/bus",
            page=AsyncOffsetPage[BusAbridged],
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
                    bus_list_params.BusListParams,
                ),
            ),
            model=BusAbridged,
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
        Service operation to delete a Bus object specified by the passed ID path
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
            f"/udl/bus/{id}",
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
            "/udl/bus/count",
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
                    bus_count_params.BusCountParams,
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
    ) -> BusQueryHelpResponse:
        """
        Service operation to provide detailed information on available dynamic query
        parameters for a particular data type.
        """
        return await self._get(
            "/udl/bus/queryhelp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusQueryHelpResponse,
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
    ) -> BusTupleResponse:
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
            "/udl/bus/tuple",
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
                    bus_tuple_params.BusTupleParams,
                ),
            ),
            cast_to=BusTupleResponse,
        )


class BusesResourceWithRawResponse:
    def __init__(self, buses: BusesResource) -> None:
        self._buses = buses

        self.create = to_raw_response_wrapper(
            buses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            buses.retrieve,
        )
        self.update = to_raw_response_wrapper(
            buses.update,
        )
        self.list = to_raw_response_wrapper(
            buses.list,
        )
        self.delete = to_raw_response_wrapper(
            buses.delete,
        )
        self.count = to_raw_response_wrapper(
            buses.count,
        )
        self.query_help = to_raw_response_wrapper(
            buses.query_help,
        )
        self.tuple = to_raw_response_wrapper(
            buses.tuple,
        )


class AsyncBusesResourceWithRawResponse:
    def __init__(self, buses: AsyncBusesResource) -> None:
        self._buses = buses

        self.create = async_to_raw_response_wrapper(
            buses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            buses.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            buses.update,
        )
        self.list = async_to_raw_response_wrapper(
            buses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            buses.delete,
        )
        self.count = async_to_raw_response_wrapper(
            buses.count,
        )
        self.query_help = async_to_raw_response_wrapper(
            buses.query_help,
        )
        self.tuple = async_to_raw_response_wrapper(
            buses.tuple,
        )


class BusesResourceWithStreamingResponse:
    def __init__(self, buses: BusesResource) -> None:
        self._buses = buses

        self.create = to_streamed_response_wrapper(
            buses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            buses.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            buses.update,
        )
        self.list = to_streamed_response_wrapper(
            buses.list,
        )
        self.delete = to_streamed_response_wrapper(
            buses.delete,
        )
        self.count = to_streamed_response_wrapper(
            buses.count,
        )
        self.query_help = to_streamed_response_wrapper(
            buses.query_help,
        )
        self.tuple = to_streamed_response_wrapper(
            buses.tuple,
        )


class AsyncBusesResourceWithStreamingResponse:
    def __init__(self, buses: AsyncBusesResource) -> None:
        self._buses = buses

        self.create = async_to_streamed_response_wrapper(
            buses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            buses.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            buses.update,
        )
        self.list = async_to_streamed_response_wrapper(
            buses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            buses.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            buses.count,
        )
        self.query_help = async_to_streamed_response_wrapper(
            buses.query_help,
        )
        self.tuple = async_to_streamed_response_wrapper(
            buses.tuple,
        )
