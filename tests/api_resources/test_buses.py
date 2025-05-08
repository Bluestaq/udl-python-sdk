# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    BusFull,
    BusAbridged,
    BusTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert bus is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            id="BUS-ID",
            aocs_notes="Example notes",
            avg_dry_mass=2879.1,
            avg_payload_mass=10.1,
            avg_payload_power=10.1,
            avg_spacecraft_power=10.1,
            avg_wet_mass=5246.1,
            body_dimension_x=10.1,
            body_dimension_y=10.1,
            body_dimension_z=10.1,
            bus_kit_designer_org_id="BUSKITDESIGNERORG-ID",
            country_code="US",
            description="Dedicated small spacecraft bus.",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            generic=False,
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            launch_envelope_dimension_x=10.1,
            launch_envelope_dimension_y=10.1,
            launch_envelope_dimension_z=10.1,
            main_computer_manufacturer_org_id="MAINCOMPUTERMANUFACTURERORG-ID",
            manufacturer_org_id="MANUFACTURERORG-ID",
            mass_category="Nanosatellite",
            max_bol_power_lower=10.1,
            max_bol_power_upper=10.1,
            max_bol_station_mass=10.1,
            max_dry_mass=2900.1,
            max_eol_power_lower=10.1,
            max_eol_power_upper=10.1,
            max_launch_mass_lower=10.1,
            max_launch_mass_upper=10.1,
            max_payload_mass=10.1,
            max_payload_power=10.1,
            max_spacecraft_power=10.1,
            max_wet_mass=5300,
            median_dry_mass=2950.1,
            median_wet_mass=5260.1,
            min_dry_mass=2858.1,
            min_wet_mass=5192.1,
            num_orbit_type=3,
            oap_payload_power=10.1,
            oap_spacecraft_power=10.1,
            orbit_types=["LEO", "HEO", "GEO"],
            origin="THIRD_PARTY_DATASOURCE",
            payload_dimension_x=1.1,
            payload_dimension_y=1.1,
            payload_dimension_z=1.1,
            payload_volume=1.1,
            power_category="low power",
            telemetry_tracking_manufacturer_org_id="TELEMETRYTRACKINGMANUFACTURERORG-ID",
            type="Example type",
        )
        assert bus is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.retrieve(
            id="id",
        )
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(BusFull, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.buses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert bus is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            body_id="BUS-ID",
            aocs_notes="Example notes",
            avg_dry_mass=2879.1,
            avg_payload_mass=10.1,
            avg_payload_power=10.1,
            avg_spacecraft_power=10.1,
            avg_wet_mass=5246.1,
            body_dimension_x=10.1,
            body_dimension_y=10.1,
            body_dimension_z=10.1,
            bus_kit_designer_org_id="BUSKITDESIGNERORG-ID",
            country_code="US",
            description="Dedicated small spacecraft bus.",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            generic=False,
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            launch_envelope_dimension_x=10.1,
            launch_envelope_dimension_y=10.1,
            launch_envelope_dimension_z=10.1,
            main_computer_manufacturer_org_id="MAINCOMPUTERMANUFACTURERORG-ID",
            manufacturer_org_id="MANUFACTURERORG-ID",
            mass_category="Nanosatellite",
            max_bol_power_lower=10.1,
            max_bol_power_upper=10.1,
            max_bol_station_mass=10.1,
            max_dry_mass=2900.1,
            max_eol_power_lower=10.1,
            max_eol_power_upper=10.1,
            max_launch_mass_lower=10.1,
            max_launch_mass_upper=10.1,
            max_payload_mass=10.1,
            max_payload_power=10.1,
            max_spacecraft_power=10.1,
            max_wet_mass=5300,
            median_dry_mass=2950.1,
            median_wet_mass=5260.1,
            min_dry_mass=2858.1,
            min_wet_mass=5192.1,
            num_orbit_type=3,
            oap_payload_power=10.1,
            oap_spacecraft_power=10.1,
            orbit_types=["LEO", "HEO", "GEO"],
            origin="THIRD_PARTY_DATASOURCE",
            payload_dimension_x=1.1,
            payload_dimension_y=1.1,
            payload_dimension_z=1.1,
            payload_volume=1.1,
            power_category="low power",
            telemetry_tracking_manufacturer_org_id="TELEMETRYTRACKINGMANUFACTURERORG-ID",
            type="Example type",
        )
        assert bus is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.buses.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example name",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.list()
        assert_matches_type(SyncOffsetPage[BusAbridged], bus, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[BusAbridged], bus, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(SyncOffsetPage[BusAbridged], bus, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(SyncOffsetPage[BusAbridged], bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.delete(
            "id",
        )
        assert bus is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.buses.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.count()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(str, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.query_help()
        assert bus is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert bus is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.tuple(
            columns="columns",
        )
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        bus = client.buses.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.buses.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = response.parse()
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.buses.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = response.parse()
            assert_matches_type(BusTupleResponse, bus, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBuses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert bus is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            id="BUS-ID",
            aocs_notes="Example notes",
            avg_dry_mass=2879.1,
            avg_payload_mass=10.1,
            avg_payload_power=10.1,
            avg_spacecraft_power=10.1,
            avg_wet_mass=5246.1,
            body_dimension_x=10.1,
            body_dimension_y=10.1,
            body_dimension_z=10.1,
            bus_kit_designer_org_id="BUSKITDESIGNERORG-ID",
            country_code="US",
            description="Dedicated small spacecraft bus.",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            generic=False,
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            launch_envelope_dimension_x=10.1,
            launch_envelope_dimension_y=10.1,
            launch_envelope_dimension_z=10.1,
            main_computer_manufacturer_org_id="MAINCOMPUTERMANUFACTURERORG-ID",
            manufacturer_org_id="MANUFACTURERORG-ID",
            mass_category="Nanosatellite",
            max_bol_power_lower=10.1,
            max_bol_power_upper=10.1,
            max_bol_station_mass=10.1,
            max_dry_mass=2900.1,
            max_eol_power_lower=10.1,
            max_eol_power_upper=10.1,
            max_launch_mass_lower=10.1,
            max_launch_mass_upper=10.1,
            max_payload_mass=10.1,
            max_payload_power=10.1,
            max_spacecraft_power=10.1,
            max_wet_mass=5300,
            median_dry_mass=2950.1,
            median_wet_mass=5260.1,
            min_dry_mass=2858.1,
            min_wet_mass=5192.1,
            num_orbit_type=3,
            oap_payload_power=10.1,
            oap_spacecraft_power=10.1,
            orbit_types=["LEO", "HEO", "GEO"],
            origin="THIRD_PARTY_DATASOURCE",
            payload_dimension_x=1.1,
            payload_dimension_y=1.1,
            payload_dimension_z=1.1,
            payload_volume=1.1,
            power_category="low power",
            telemetry_tracking_manufacturer_org_id="TELEMETRYTRACKINGMANUFACTURERORG-ID",
            type="Example type",
        )
        assert bus is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.retrieve(
            id="id",
        )
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(BusFull, bus, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(BusFull, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.buses.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )
        assert bus is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
            body_id="BUS-ID",
            aocs_notes="Example notes",
            avg_dry_mass=2879.1,
            avg_payload_mass=10.1,
            avg_payload_power=10.1,
            avg_spacecraft_power=10.1,
            avg_wet_mass=5246.1,
            body_dimension_x=10.1,
            body_dimension_y=10.1,
            body_dimension_z=10.1,
            bus_kit_designer_org_id="BUSKITDESIGNERORG-ID",
            country_code="US",
            description="Dedicated small spacecraft bus.",
            entity={
                "classification_marking": "U",
                "data_mode": "TEST",
                "name": "Example name",
                "source": "Bluestaq",
                "type": "ONORBIT",
                "country_code": "US",
                "id_entity": "ENTITY-ID",
                "id_location": "LOCATION-ID",
                "id_on_orbit": "ONORBIT-ID",
                "id_operating_unit": "OPERATINGUNIT-ID",
                "location": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "Example location",
                    "source": "Bluestaq",
                    "altitude": 10.23,
                    "country_code": "US",
                    "id_location": "LOCATION-ID",
                    "lat": 45.23,
                    "lon": 179.1,
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "on_orbit": {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "sat_no": 1,
                    "source": "Bluestaq",
                    "alt_name": "Alternate Name",
                    "category": "Lunar",
                    "common_name": "Example common name",
                    "constellation": "Big Dipper",
                    "country_code": "US",
                    "decay_date": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "id_on_orbit": "ONORBIT-ID",
                    "intl_des": "2021123ABC",
                    "launch_date": parse_date("2018-01-01"),
                    "launch_site_id": "LAUNCHSITE-ID",
                    "lifetime_years": 10,
                    "mission_number": "Expedition 1",
                    "object_type": "PAYLOAD",
                    "origin": "THIRD_PARTY_DATASOURCE",
                },
                "origin": "THIRD_PARTY_DATASOURCE",
                "owner_type": "Commercial",
                "taskable": False,
                "urls": ["URL1", "URL2"],
            },
            generic=False,
            id_entity="0167f577-e06c-358e-85aa-0a07a730bdd0",
            launch_envelope_dimension_x=10.1,
            launch_envelope_dimension_y=10.1,
            launch_envelope_dimension_z=10.1,
            main_computer_manufacturer_org_id="MAINCOMPUTERMANUFACTURERORG-ID",
            manufacturer_org_id="MANUFACTURERORG-ID",
            mass_category="Nanosatellite",
            max_bol_power_lower=10.1,
            max_bol_power_upper=10.1,
            max_bol_station_mass=10.1,
            max_dry_mass=2900.1,
            max_eol_power_lower=10.1,
            max_eol_power_upper=10.1,
            max_launch_mass_lower=10.1,
            max_launch_mass_upper=10.1,
            max_payload_mass=10.1,
            max_payload_power=10.1,
            max_spacecraft_power=10.1,
            max_wet_mass=5300,
            median_dry_mass=2950.1,
            median_wet_mass=5260.1,
            min_dry_mass=2858.1,
            min_wet_mass=5192.1,
            num_orbit_type=3,
            oap_payload_power=10.1,
            oap_spacecraft_power=10.1,
            orbit_types=["LEO", "HEO", "GEO"],
            origin="THIRD_PARTY_DATASOURCE",
            payload_dimension_x=1.1,
            payload_dimension_y=1.1,
            payload_dimension_z=1.1,
            payload_volume=1.1,
            power_category="low power",
            telemetry_tracking_manufacturer_org_id="TELEMETRYTRACKINGMANUFACTURERORG-ID",
            type="Example type",
        )
        assert bus is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="Example name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.buses.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="Example name",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.list()
        assert_matches_type(AsyncOffsetPage[BusAbridged], bus, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[BusAbridged], bus, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(AsyncOffsetPage[BusAbridged], bus, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(AsyncOffsetPage[BusAbridged], bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.delete(
            "id",
        )
        assert bus is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.buses.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.count()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(str, bus, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(str, bus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.query_help()
        assert bus is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert bus is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert bus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.tuple(
            columns="columns",
        )
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        bus = await async_client.buses.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.buses.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bus = await response.parse()
        assert_matches_type(BusTupleResponse, bus, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.buses.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bus = await response.parse()
            assert_matches_type(BusTupleResponse, bus, path=["response"])

        assert cast(Any, response.is_closed) is True
