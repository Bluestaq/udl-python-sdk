# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaunchVehicleDetailGetResponse,
    LaunchVehicleDetailListResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaunchVehicleDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert launch_vehicle_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            id="LAUNCHVEHICLEDETAILS-ID",
            attitude_accuracy=10.23,
            category="Example-category",
            deployment_rotation_rate=10.23,
            diameter=10.23,
            est_launch_price=10.23,
            est_launch_price_typical=10.23,
            fairing_external_diameter=10.23,
            fairing_internal_diameter=10.23,
            fairing_length=10.23,
            fairing_mass=10.23,
            fairing_material="Example-fairing-material",
            fairing_name="Example-fairing-name",
            fairing_notes="Example notes",
            family="Example-family",
            geo_payload_mass=10.23,
            gto_inj3_sig_accuracy_apogee_margin=10.23,
            gto_inj3_sig_accuracy_apogee_target=10.23,
            gto_inj3_sig_accuracy_inclination_margin=10.23,
            gto_inj3_sig_accuracy_inclination_target=10.23,
            gto_inj3_sig_accuracy_perigee_margin=10.23,
            gto_inj3_sig_accuracy_perigee_target=10.23,
            gto_payload_mass=10.23,
            launch_mass=10.23,
            launch_prefix="AX011",
            length=10.23,
            leo_payload_mass=10.23,
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_accel_load=10.23,
            max_acoustic_level=10.23,
            max_acoustic_level_range=10.23,
            max_fairing_pressure_change=10.23,
            max_flight_shock_force=10.23,
            max_flight_shock_freq=10.23,
            max_payload_freq_lat=10.23,
            max_payload_freq_lon=10.23,
            minor_variant="Example-minor-variant",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Bromine",
            payload_notes="Example notes",
            payload_separation_rate=10.23,
            propellant="Nitrogen",
            sound_pressure_level=10.23,
            source_url="Example URL",
            sso_payload_mass=10.23,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            variant="Example-variant",
        )
        assert launch_vehicle_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = response.parse()
        assert launch_vehicle_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = response.parse()
            assert launch_vehicle_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert launch_vehicle_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            body_id="LAUNCHVEHICLEDETAILS-ID",
            attitude_accuracy=10.23,
            category="Example-category",
            deployment_rotation_rate=10.23,
            diameter=10.23,
            est_launch_price=10.23,
            est_launch_price_typical=10.23,
            fairing_external_diameter=10.23,
            fairing_internal_diameter=10.23,
            fairing_length=10.23,
            fairing_mass=10.23,
            fairing_material="Example-fairing-material",
            fairing_name="Example-fairing-name",
            fairing_notes="Example notes",
            family="Example-family",
            geo_payload_mass=10.23,
            gto_inj3_sig_accuracy_apogee_margin=10.23,
            gto_inj3_sig_accuracy_apogee_target=10.23,
            gto_inj3_sig_accuracy_inclination_margin=10.23,
            gto_inj3_sig_accuracy_inclination_target=10.23,
            gto_inj3_sig_accuracy_perigee_margin=10.23,
            gto_inj3_sig_accuracy_perigee_target=10.23,
            gto_payload_mass=10.23,
            launch_mass=10.23,
            launch_prefix="AX011",
            length=10.23,
            leo_payload_mass=10.23,
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_accel_load=10.23,
            max_acoustic_level=10.23,
            max_acoustic_level_range=10.23,
            max_fairing_pressure_change=10.23,
            max_flight_shock_force=10.23,
            max_flight_shock_freq=10.23,
            max_payload_freq_lat=10.23,
            max_payload_freq_lon=10.23,
            minor_variant="Example-minor-variant",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Bromine",
            payload_notes="Example notes",
            payload_separation_rate=10.23,
            propellant="Nitrogen",
            sound_pressure_level=10.23,
            source_url="Example URL",
            sso_payload_mass=10.23,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            variant="Example-variant",
        )
        assert launch_vehicle_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = response.parse()
        assert launch_vehicle_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = response.parse()
            assert launch_vehicle_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.launch_vehicle_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_launch_vehicle="LAUNCHVEHICLE-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.list()
        assert_matches_type(SyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = response.parse()
        assert_matches_type(SyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = response.parse()
            assert_matches_type(
                SyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.delete(
            "id",
        )
        assert launch_vehicle_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = response.parse()
        assert launch_vehicle_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = response.parse()
            assert launch_vehicle_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_vehicle_details.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.get(
            id="id",
        )
        assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_vehicle_detail = client.launch_vehicle_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.launch_vehicle_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = response.parse()
        assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.launch_vehicle_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = response.parse()
            assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_vehicle_details.with_raw_response.get(
                id="",
            )


class TestAsyncLaunchVehicleDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert launch_vehicle_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            id="LAUNCHVEHICLEDETAILS-ID",
            attitude_accuracy=10.23,
            category="Example-category",
            deployment_rotation_rate=10.23,
            diameter=10.23,
            est_launch_price=10.23,
            est_launch_price_typical=10.23,
            fairing_external_diameter=10.23,
            fairing_internal_diameter=10.23,
            fairing_length=10.23,
            fairing_mass=10.23,
            fairing_material="Example-fairing-material",
            fairing_name="Example-fairing-name",
            fairing_notes="Example notes",
            family="Example-family",
            geo_payload_mass=10.23,
            gto_inj3_sig_accuracy_apogee_margin=10.23,
            gto_inj3_sig_accuracy_apogee_target=10.23,
            gto_inj3_sig_accuracy_inclination_margin=10.23,
            gto_inj3_sig_accuracy_inclination_target=10.23,
            gto_inj3_sig_accuracy_perigee_margin=10.23,
            gto_inj3_sig_accuracy_perigee_target=10.23,
            gto_payload_mass=10.23,
            launch_mass=10.23,
            launch_prefix="AX011",
            length=10.23,
            leo_payload_mass=10.23,
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_accel_load=10.23,
            max_acoustic_level=10.23,
            max_acoustic_level_range=10.23,
            max_fairing_pressure_change=10.23,
            max_flight_shock_force=10.23,
            max_flight_shock_freq=10.23,
            max_payload_freq_lat=10.23,
            max_payload_freq_lon=10.23,
            minor_variant="Example-minor-variant",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Bromine",
            payload_notes="Example notes",
            payload_separation_rate=10.23,
            propellant="Nitrogen",
            sound_pressure_level=10.23,
            source_url="Example URL",
            sso_payload_mass=10.23,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            variant="Example-variant",
        )
        assert launch_vehicle_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = await response.parse()
        assert launch_vehicle_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = await response.parse()
            assert launch_vehicle_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )
        assert launch_vehicle_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
            body_id="LAUNCHVEHICLEDETAILS-ID",
            attitude_accuracy=10.23,
            category="Example-category",
            deployment_rotation_rate=10.23,
            diameter=10.23,
            est_launch_price=10.23,
            est_launch_price_typical=10.23,
            fairing_external_diameter=10.23,
            fairing_internal_diameter=10.23,
            fairing_length=10.23,
            fairing_mass=10.23,
            fairing_material="Example-fairing-material",
            fairing_name="Example-fairing-name",
            fairing_notes="Example notes",
            family="Example-family",
            geo_payload_mass=10.23,
            gto_inj3_sig_accuracy_apogee_margin=10.23,
            gto_inj3_sig_accuracy_apogee_target=10.23,
            gto_inj3_sig_accuracy_inclination_margin=10.23,
            gto_inj3_sig_accuracy_inclination_target=10.23,
            gto_inj3_sig_accuracy_perigee_margin=10.23,
            gto_inj3_sig_accuracy_perigee_target=10.23,
            gto_payload_mass=10.23,
            launch_mass=10.23,
            launch_prefix="AX011",
            length=10.23,
            leo_payload_mass=10.23,
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_accel_load=10.23,
            max_acoustic_level=10.23,
            max_acoustic_level_range=10.23,
            max_fairing_pressure_change=10.23,
            max_flight_shock_force=10.23,
            max_flight_shock_freq=10.23,
            max_payload_freq_lat=10.23,
            max_payload_freq_lon=10.23,
            minor_variant="Example-minor-variant",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Bromine",
            payload_notes="Example notes",
            payload_separation_rate=10.23,
            propellant="Nitrogen",
            sound_pressure_level=10.23,
            source_url="Example URL",
            sso_payload_mass=10.23,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            variant="Example-variant",
        )
        assert launch_vehicle_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = await response.parse()
        assert launch_vehicle_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_launch_vehicle="LAUNCHVEHICLE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = await response.parse()
            assert launch_vehicle_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.launch_vehicle_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_launch_vehicle="LAUNCHVEHICLE-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.list()
        assert_matches_type(AsyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[LaunchVehicleDetailListResponse], launch_vehicle_detail, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.delete(
            "id",
        )
        assert launch_vehicle_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = await response.parse()
        assert launch_vehicle_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = await response.parse()
            assert launch_vehicle_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_vehicle_details.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.get(
            id="id",
        )
        assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_vehicle_detail = await async_client.launch_vehicle_details.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_vehicle_details.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_vehicle_detail = await response.parse()
        assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_vehicle_details.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_vehicle_detail = await response.parse()
            assert_matches_type(LaunchVehicleDetailGetResponse, launch_vehicle_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_vehicle_details.with_raw_response.get(
                id="",
            )
