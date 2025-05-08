# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OnorbitdetailGetResponse,
    OnorbitdetailListResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnorbitdetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitdetail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
            id="ONORBITDETAILS-ID",
            additional_mass=10.23,
            adept_radius=10.23,
            bol_delta_v=1000.1,
            bol_fuel_mass=10.23,
            bus_cross_section=10.23,
            bus_type="A2100",
            cola_radius=10.23,
            cross_section=10.23,
            current_mass=500,
            delta_v_unc=50.1,
            dep_est_masses=[20, 21],
            dep_mass_uncs=[10, 5],
            dep_names=["GOES-18A", "GOES-18B"],
            drift_rate=1.23,
            dry_mass=10.23,
            est_delta_v_duration=10.23,
            fuel_remaining=10.23,
            geo_slot=90.23,
            last_ob_source="THIRD_PARTY_DATASOURCE",
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            launch_mass=10.23,
            launch_mass_max=15.23,
            launch_mass_min=5.23,
            maneuverable=False,
            max_delta_v=10.23,
            max_radius=10.23,
            mission_types=["Weather", "Space Weather"],
            num_deployable=2,
            num_mission=2,
            origin="THIRD_PARTY_DATASOURCE",
            rcs=10.23,
            rcs_max=15.23,
            rcs_mean=10.23,
            rcs_min=5.23,
            ref_source="Wikipedia",
            solar_array_area=10.23,
            total_mass_unc=50.1,
            vismag=10.23,
            vismag_max=15.23,
            vismag_mean=10.23,
            vismag_min=5.23,
        )
        assert onorbitdetail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitdetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = response.parse()
        assert onorbitdetail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbitdetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = response.parse()
            assert onorbitdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitdetail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
            body_id="ONORBITDETAILS-ID",
            additional_mass=10.23,
            adept_radius=10.23,
            bol_delta_v=1000.1,
            bol_fuel_mass=10.23,
            bus_cross_section=10.23,
            bus_type="A2100",
            cola_radius=10.23,
            cross_section=10.23,
            current_mass=500,
            delta_v_unc=50.1,
            dep_est_masses=[20, 21],
            dep_mass_uncs=[10, 5],
            dep_names=["GOES-18A", "GOES-18B"],
            drift_rate=1.23,
            dry_mass=10.23,
            est_delta_v_duration=10.23,
            fuel_remaining=10.23,
            geo_slot=90.23,
            last_ob_source="THIRD_PARTY_DATASOURCE",
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            launch_mass=10.23,
            launch_mass_max=15.23,
            launch_mass_min=5.23,
            maneuverable=False,
            max_delta_v=10.23,
            max_radius=10.23,
            mission_types=["Weather", "Space Weather"],
            num_deployable=2,
            num_mission=2,
            origin="THIRD_PARTY_DATASOURCE",
            rcs=10.23,
            rcs_max=15.23,
            rcs_mean=10.23,
            rcs_min=5.23,
            ref_source="Wikipedia",
            solar_array_area=10.23,
            total_mass_unc=50.1,
            vismag=10.23,
            vismag_max=15.23,
            vismag_mean=10.23,
            vismag_min=5.23,
        )
        assert onorbitdetail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitdetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = response.parse()
        assert onorbitdetail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.onorbitdetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = response.parse()
            assert onorbitdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.onorbitdetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_on_orbit="REF-ONORBIT-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.list()
        assert_matches_type(SyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitdetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = response.parse()
        assert_matches_type(SyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbitdetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = response.parse()
            assert_matches_type(SyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.delete(
            "id",
        )
        assert onorbitdetail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitdetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = response.parse()
        assert onorbitdetail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbitdetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = response.parse()
            assert onorbitdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitdetails.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.get(
            id="id",
        )
        assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitdetail = client.onorbitdetails.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitdetails.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = response.parse()
        assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.onorbitdetails.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = response.parse()
            assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitdetails.with_raw_response.get(
                id="",
            )


class TestAsyncOnorbitdetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitdetail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
            id="ONORBITDETAILS-ID",
            additional_mass=10.23,
            adept_radius=10.23,
            bol_delta_v=1000.1,
            bol_fuel_mass=10.23,
            bus_cross_section=10.23,
            bus_type="A2100",
            cola_radius=10.23,
            cross_section=10.23,
            current_mass=500,
            delta_v_unc=50.1,
            dep_est_masses=[20, 21],
            dep_mass_uncs=[10, 5],
            dep_names=["GOES-18A", "GOES-18B"],
            drift_rate=1.23,
            dry_mass=10.23,
            est_delta_v_duration=10.23,
            fuel_remaining=10.23,
            geo_slot=90.23,
            last_ob_source="THIRD_PARTY_DATASOURCE",
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            launch_mass=10.23,
            launch_mass_max=15.23,
            launch_mass_min=5.23,
            maneuverable=False,
            max_delta_v=10.23,
            max_radius=10.23,
            mission_types=["Weather", "Space Weather"],
            num_deployable=2,
            num_mission=2,
            origin="THIRD_PARTY_DATASOURCE",
            rcs=10.23,
            rcs_max=15.23,
            rcs_mean=10.23,
            rcs_min=5.23,
            ref_source="Wikipedia",
            solar_array_area=10.23,
            total_mass_unc=50.1,
            vismag=10.23,
            vismag_max=15.23,
            vismag_mean=10.23,
            vismag_min=5.23,
        )
        assert onorbitdetail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitdetails.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = await response.parse()
        assert onorbitdetail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitdetails.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = await response.parse()
            assert onorbitdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitdetail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
            body_id="ONORBITDETAILS-ID",
            additional_mass=10.23,
            adept_radius=10.23,
            bol_delta_v=1000.1,
            bol_fuel_mass=10.23,
            bus_cross_section=10.23,
            bus_type="A2100",
            cola_radius=10.23,
            cross_section=10.23,
            current_mass=500,
            delta_v_unc=50.1,
            dep_est_masses=[20, 21],
            dep_mass_uncs=[10, 5],
            dep_names=["GOES-18A", "GOES-18B"],
            drift_rate=1.23,
            dry_mass=10.23,
            est_delta_v_duration=10.23,
            fuel_remaining=10.23,
            geo_slot=90.23,
            last_ob_source="THIRD_PARTY_DATASOURCE",
            last_ob_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            launch_mass=10.23,
            launch_mass_max=15.23,
            launch_mass_min=5.23,
            maneuverable=False,
            max_delta_v=10.23,
            max_radius=10.23,
            mission_types=["Weather", "Space Weather"],
            num_deployable=2,
            num_mission=2,
            origin="THIRD_PARTY_DATASOURCE",
            rcs=10.23,
            rcs_max=15.23,
            rcs_mean=10.23,
            rcs_min=5.23,
            ref_source="Wikipedia",
            solar_array_area=10.23,
            total_mass_unc=50.1,
            vismag=10.23,
            vismag_max=15.23,
            vismag_mean=10.23,
            vismag_min=5.23,
        )
        assert onorbitdetail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitdetails.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = await response.parse()
        assert onorbitdetail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitdetails.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_on_orbit="REF-ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = await response.parse()
            assert onorbitdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.onorbitdetails.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_on_orbit="REF-ONORBIT-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.list()
        assert_matches_type(AsyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitdetails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = await response.parse()
        assert_matches_type(AsyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitdetails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = await response.parse()
            assert_matches_type(AsyncOffsetPage[OnorbitdetailListResponse], onorbitdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.delete(
            "id",
        )
        assert onorbitdetail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitdetails.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = await response.parse()
        assert onorbitdetail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitdetails.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = await response.parse()
            assert onorbitdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitdetails.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.get(
            id="id",
        )
        assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitdetail = await async_client.onorbitdetails.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitdetails.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitdetail = await response.parse()
        assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitdetails.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitdetail = await response.parse()
            assert_matches_type(OnorbitdetailGetResponse, onorbitdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitdetails.with_raw_response.get(
                id="",
            )
