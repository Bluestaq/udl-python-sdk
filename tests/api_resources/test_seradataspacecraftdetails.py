# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SeradataspacecraftdetailGetResponse,
    SeradataspacecraftdetailListResponse,
    SeradataspacecraftdetailTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeradataspacecraftdetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
            id="SERADATASPACECRAFTDETAILS-ID",
            additional_missions_groups="additionalMissionsGroups",
            altitude=36036.6330576414,
            annual_insured_depreciation_factor=1.23,
            annual_insured_depreciation_factor_estimated=True,
            apogee=1.23,
            bus_id="BUS-ID",
            capability_lost=1.23,
            capacity_lost=1.23,
            catalog_number=1,
            collision_risk_cm=1.43,
            collision_risk_mm=1.33,
            combined_cost_estimated=True,
            combined_new_cost=1.23,
            commercial_launch=True,
            constellation="GPS",
            cost_estimated=True,
            cubesat_dispenser_type="cubesatDispenserType",
            current_age=5.898630136986301,
            date_of_observation=parse_datetime("2018-01-01T16:00:00.123Z"),
            description="description",
            design_life=231,
            dry_mass=1.23,
            expected_life=231,
            geo_position=-8.23,
            id_on_orbit="503",
            inclination=1.23,
            insurance_losses_total=0.393,
            insurance_notes="Sample Notes",
            insurance_premium_at_launch=1.23,
            insurance_premium_at_launch_estimated=True,
            insured_at_launch=True,
            insured_value_at_launch=1.23,
            insured_value_launch_estimated=True,
            intl_number="number",
            lat=1.23,
            launch_arranger="launchArranger",
            launch_arranger_country="USA",
            launch_characteristic="Expendable",
            launch_cost=1.23,
            launch_cost_estimated=True,
            launch_country="USA",
            launch_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            launch_date_remarks="launchDateRemarks",
            launch_id="11573",
            launch_mass=1.23,
            launch_notes="Sample Notes",
            launch_number="FN040",
            launch_provider="launchProvider",
            launch_provider_country="USA",
            launch_provider_flight_number="launchProviderFlightNumber",
            launch_site_id="28",
            launch_site_name="launchSiteName",
            launch_type="Future",
            launch_vehicle_id="123",
            leased=True,
            life_lost=1.23,
            lon=1.23,
            mass_category="2500 - 3500kg  - Large Satellite",
            name_at_launch="nameAtLaunch",
            new_cost=1.23,
            notes="Sample Notes",
            num_humans=1,
            operator="operator",
            operator_country="USA",
            orbit_category="GEO",
            orbit_sub_category="Geostationary",
            order_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="owner",
            owner_country="USA",
            perigee=1.23,
            period=1.23,
            primary_mission_group="primaryMissionGroup",
            prime_manufacturer_org_id="05c43360-382e-4aa2-b875-ed28945ff2e5",
            program_name="programName",
            quantity=1,
            reusable_flights="reusableFlights",
            reused_hull_name="reusedHullName",
            sector="Commercial",
            serial_number="serialNumber",
            stabilizer="3-Axis",
            status="Inactive - Retired",
            total_claims=1,
            total_fatalities=1,
            total_injuries=1,
            total_payload_power=1.23,
            youtube_launch_link="youtubeLaunchLink",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
            body_id="SERADATASPACECRAFTDETAILS-ID",
            additional_missions_groups="additionalMissionsGroups",
            altitude=36036.6330576414,
            annual_insured_depreciation_factor=1.23,
            annual_insured_depreciation_factor_estimated=True,
            apogee=1.23,
            bus_id="BUS-ID",
            capability_lost=1.23,
            capacity_lost=1.23,
            catalog_number=1,
            collision_risk_cm=1.43,
            collision_risk_mm=1.33,
            combined_cost_estimated=True,
            combined_new_cost=1.23,
            commercial_launch=True,
            constellation="GPS",
            cost_estimated=True,
            cubesat_dispenser_type="cubesatDispenserType",
            current_age=5.898630136986301,
            date_of_observation=parse_datetime("2018-01-01T16:00:00.123Z"),
            description="description",
            design_life=231,
            dry_mass=1.23,
            expected_life=231,
            geo_position=-8.23,
            id_on_orbit="503",
            inclination=1.23,
            insurance_losses_total=0.393,
            insurance_notes="Sample Notes",
            insurance_premium_at_launch=1.23,
            insurance_premium_at_launch_estimated=True,
            insured_at_launch=True,
            insured_value_at_launch=1.23,
            insured_value_launch_estimated=True,
            intl_number="number",
            lat=1.23,
            launch_arranger="launchArranger",
            launch_arranger_country="USA",
            launch_characteristic="Expendable",
            launch_cost=1.23,
            launch_cost_estimated=True,
            launch_country="USA",
            launch_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            launch_date_remarks="launchDateRemarks",
            launch_id="11573",
            launch_mass=1.23,
            launch_notes="Sample Notes",
            launch_number="FN040",
            launch_provider="launchProvider",
            launch_provider_country="USA",
            launch_provider_flight_number="launchProviderFlightNumber",
            launch_site_id="28",
            launch_site_name="launchSiteName",
            launch_type="Future",
            launch_vehicle_id="123",
            leased=True,
            life_lost=1.23,
            lon=1.23,
            mass_category="2500 - 3500kg  - Large Satellite",
            name_at_launch="nameAtLaunch",
            new_cost=1.23,
            notes="Sample Notes",
            num_humans=1,
            operator="operator",
            operator_country="USA",
            orbit_category="GEO",
            orbit_sub_category="Geostationary",
            order_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="owner",
            owner_country="USA",
            perigee=1.23,
            period=1.23,
            primary_mission_group="primaryMissionGroup",
            prime_manufacturer_org_id="05c43360-382e-4aa2-b875-ed28945ff2e5",
            program_name="programName",
            quantity=1,
            reusable_flights="reusableFlights",
            reused_hull_name="reusedHullName",
            sector="Commercial",
            serial_number="serialNumber",
            stabilizer="3-Axis",
            status="Inactive - Retired",
            total_claims=1,
            total_fatalities=1,
            total_injuries=1,
            total_payload_power=1.23,
            youtube_launch_link="youtubeLaunchLink",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.seradataspacecraftdetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="name",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.list()
        assert_matches_type(SeradataspacecraftdetailListResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert_matches_type(SeradataspacecraftdetailListResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert_matches_type(SeradataspacecraftdetailListResponse, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.delete(
            "id",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradataspacecraftdetails.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.count()
        assert_matches_type(str, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert_matches_type(str, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert_matches_type(str, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.get(
            "id",
        )
        assert_matches_type(SeradataspacecraftdetailGetResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert_matches_type(SeradataspacecraftdetailGetResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert_matches_type(SeradataspacecraftdetailGetResponse, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradataspacecraftdetails.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.queryhelp()
        assert seradataspacecraftdetail is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        seradataspacecraftdetail = client.seradataspacecraftdetails.tuple(
            columns="columns",
        )
        assert_matches_type(SeradataspacecraftdetailTupleResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.seradataspacecraftdetails.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = response.parse()
        assert_matches_type(SeradataspacecraftdetailTupleResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.seradataspacecraftdetails.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = response.parse()
            assert_matches_type(SeradataspacecraftdetailTupleResponse, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeradataspacecraftdetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
            id="SERADATASPACECRAFTDETAILS-ID",
            additional_missions_groups="additionalMissionsGroups",
            altitude=36036.6330576414,
            annual_insured_depreciation_factor=1.23,
            annual_insured_depreciation_factor_estimated=True,
            apogee=1.23,
            bus_id="BUS-ID",
            capability_lost=1.23,
            capacity_lost=1.23,
            catalog_number=1,
            collision_risk_cm=1.43,
            collision_risk_mm=1.33,
            combined_cost_estimated=True,
            combined_new_cost=1.23,
            commercial_launch=True,
            constellation="GPS",
            cost_estimated=True,
            cubesat_dispenser_type="cubesatDispenserType",
            current_age=5.898630136986301,
            date_of_observation=parse_datetime("2018-01-01T16:00:00.123Z"),
            description="description",
            design_life=231,
            dry_mass=1.23,
            expected_life=231,
            geo_position=-8.23,
            id_on_orbit="503",
            inclination=1.23,
            insurance_losses_total=0.393,
            insurance_notes="Sample Notes",
            insurance_premium_at_launch=1.23,
            insurance_premium_at_launch_estimated=True,
            insured_at_launch=True,
            insured_value_at_launch=1.23,
            insured_value_launch_estimated=True,
            intl_number="number",
            lat=1.23,
            launch_arranger="launchArranger",
            launch_arranger_country="USA",
            launch_characteristic="Expendable",
            launch_cost=1.23,
            launch_cost_estimated=True,
            launch_country="USA",
            launch_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            launch_date_remarks="launchDateRemarks",
            launch_id="11573",
            launch_mass=1.23,
            launch_notes="Sample Notes",
            launch_number="FN040",
            launch_provider="launchProvider",
            launch_provider_country="USA",
            launch_provider_flight_number="launchProviderFlightNumber",
            launch_site_id="28",
            launch_site_name="launchSiteName",
            launch_type="Future",
            launch_vehicle_id="123",
            leased=True,
            life_lost=1.23,
            lon=1.23,
            mass_category="2500 - 3500kg  - Large Satellite",
            name_at_launch="nameAtLaunch",
            new_cost=1.23,
            notes="Sample Notes",
            num_humans=1,
            operator="operator",
            operator_country="USA",
            orbit_category="GEO",
            orbit_sub_category="Geostationary",
            order_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="owner",
            owner_country="USA",
            perigee=1.23,
            period=1.23,
            primary_mission_group="primaryMissionGroup",
            prime_manufacturer_org_id="05c43360-382e-4aa2-b875-ed28945ff2e5",
            program_name="programName",
            quantity=1,
            reusable_flights="reusableFlights",
            reused_hull_name="reusedHullName",
            sector="Commercial",
            serial_number="serialNumber",
            stabilizer="3-Axis",
            status="Inactive - Retired",
            total_claims=1,
            total_fatalities=1,
            total_injuries=1,
            total_payload_power=1.23,
            youtube_launch_link="youtubeLaunchLink",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
            body_id="SERADATASPACECRAFTDETAILS-ID",
            additional_missions_groups="additionalMissionsGroups",
            altitude=36036.6330576414,
            annual_insured_depreciation_factor=1.23,
            annual_insured_depreciation_factor_estimated=True,
            apogee=1.23,
            bus_id="BUS-ID",
            capability_lost=1.23,
            capacity_lost=1.23,
            catalog_number=1,
            collision_risk_cm=1.43,
            collision_risk_mm=1.33,
            combined_cost_estimated=True,
            combined_new_cost=1.23,
            commercial_launch=True,
            constellation="GPS",
            cost_estimated=True,
            cubesat_dispenser_type="cubesatDispenserType",
            current_age=5.898630136986301,
            date_of_observation=parse_datetime("2018-01-01T16:00:00.123Z"),
            description="description",
            design_life=231,
            dry_mass=1.23,
            expected_life=231,
            geo_position=-8.23,
            id_on_orbit="503",
            inclination=1.23,
            insurance_losses_total=0.393,
            insurance_notes="Sample Notes",
            insurance_premium_at_launch=1.23,
            insurance_premium_at_launch_estimated=True,
            insured_at_launch=True,
            insured_value_at_launch=1.23,
            insured_value_launch_estimated=True,
            intl_number="number",
            lat=1.23,
            launch_arranger="launchArranger",
            launch_arranger_country="USA",
            launch_characteristic="Expendable",
            launch_cost=1.23,
            launch_cost_estimated=True,
            launch_country="USA",
            launch_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            launch_date_remarks="launchDateRemarks",
            launch_id="11573",
            launch_mass=1.23,
            launch_notes="Sample Notes",
            launch_number="FN040",
            launch_provider="launchProvider",
            launch_provider_country="USA",
            launch_provider_flight_number="launchProviderFlightNumber",
            launch_site_id="28",
            launch_site_name="launchSiteName",
            launch_type="Future",
            launch_vehicle_id="123",
            leased=True,
            life_lost=1.23,
            lon=1.23,
            mass_category="2500 - 3500kg  - Large Satellite",
            name_at_launch="nameAtLaunch",
            new_cost=1.23,
            notes="Sample Notes",
            num_humans=1,
            operator="operator",
            operator_country="USA",
            orbit_category="GEO",
            orbit_sub_category="Geostationary",
            order_date=parse_datetime("2018-01-01T16:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="owner",
            owner_country="USA",
            perigee=1.23,
            period=1.23,
            primary_mission_group="primaryMissionGroup",
            prime_manufacturer_org_id="05c43360-382e-4aa2-b875-ed28945ff2e5",
            program_name="programName",
            quantity=1,
            reusable_flights="reusableFlights",
            reused_hull_name="reusedHullName",
            sector="Commercial",
            serial_number="serialNumber",
            stabilizer="3-Axis",
            status="Inactive - Retired",
            total_claims=1,
            total_fatalities=1,
            total_injuries=1,
            total_payload_power=1.23,
            youtube_launch_link="youtubeLaunchLink",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.seradataspacecraftdetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="name",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.list()
        assert_matches_type(SeradataspacecraftdetailListResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert_matches_type(SeradataspacecraftdetailListResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert_matches_type(SeradataspacecraftdetailListResponse, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.delete(
            "id",
        )
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradataspacecraftdetails.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.count()
        assert_matches_type(str, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert_matches_type(str, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert_matches_type(str, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.get(
            "id",
        )
        assert_matches_type(SeradataspacecraftdetailGetResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert_matches_type(SeradataspacecraftdetailGetResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert_matches_type(SeradataspacecraftdetailGetResponse, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradataspacecraftdetails.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.queryhelp()
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert seradataspacecraftdetail is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert seradataspacecraftdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataspacecraftdetail = await async_client.seradataspacecraftdetails.tuple(
            columns="columns",
        )
        assert_matches_type(SeradataspacecraftdetailTupleResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataspacecraftdetails.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataspacecraftdetail = await response.parse()
        assert_matches_type(SeradataspacecraftdetailTupleResponse, seradataspacecraftdetail, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataspacecraftdetails.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataspacecraftdetail = await response.parse()
            assert_matches_type(SeradataspacecraftdetailTupleResponse, seradataspacecraftdetail, path=["response"])

        assert cast(Any, response.is_closed) is True
