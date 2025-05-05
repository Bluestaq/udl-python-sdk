# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SeraDataEarlyWarningGetResponse,
    SeraDataEarlyWarningListResponse,
    SeraDataEarlyWarningTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeraDataEarlyWarning:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert sera_data_early_warning is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATAEARLYWARNING-ID",
            best_resolution=1.23,
            earth_pointing=True,
            frequency_limits="frequencyLimits",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_ir="idIR",
            manufacturer_org_id="manufacturerOrgId",
            missile_launch_phase_detection_ability="missileLaunchPhaseDetectionAbility",
            name="Infra red telescope",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_notes="Sample Notes",
            spectral_bands="Infra-Red",
        )
        assert sera_data_early_warning is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert sera_data_early_warning is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert sera_data_early_warning is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATAEARLYWARNING-ID",
            best_resolution=1.23,
            earth_pointing=True,
            frequency_limits="frequencyLimits",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_ir="idIR",
            manufacturer_org_id="manufacturerOrgId",
            missile_launch_phase_detection_ability="missileLaunchPhaseDetectionAbility",
            name="Infra red telescope",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_notes="Sample Notes",
            spectral_bands="Infra-Red",
        )
        assert sera_data_early_warning is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert sera_data_early_warning is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sera_data_early_warning.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.list()
        assert_matches_type(
            SyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            SyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert_matches_type(
            SyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert_matches_type(
                SyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.delete(
            "id",
        )
        assert sera_data_early_warning is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert sera_data_early_warning is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sera_data_early_warning.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.count()
        assert_matches_type(str, sera_data_early_warning, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sera_data_early_warning, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert_matches_type(str, sera_data_early_warning, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert_matches_type(str, sera_data_early_warning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.get(
            id="id",
        )
        assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sera_data_early_warning.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.queryhelp()
        assert sera_data_early_warning is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert sera_data_early_warning is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.tuple(
            columns="columns",
        )
        assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sera_data_early_warning = client.sera_data_early_warning.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sera_data_early_warning.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = response.parse()
        assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sera_data_early_warning.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = response.parse()
            assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeraDataEarlyWarning:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert sera_data_early_warning is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATAEARLYWARNING-ID",
            best_resolution=1.23,
            earth_pointing=True,
            frequency_limits="frequencyLimits",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_ir="idIR",
            manufacturer_org_id="manufacturerOrgId",
            missile_launch_phase_detection_ability="missileLaunchPhaseDetectionAbility",
            name="Infra red telescope",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_notes="Sample Notes",
            spectral_bands="Infra-Red",
        )
        assert sera_data_early_warning is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert sera_data_early_warning is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert sera_data_early_warning is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATAEARLYWARNING-ID",
            best_resolution=1.23,
            earth_pointing=True,
            frequency_limits="frequencyLimits",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_ir="idIR",
            manufacturer_org_id="manufacturerOrgId",
            missile_launch_phase_detection_ability="missileLaunchPhaseDetectionAbility",
            name="Infra red telescope",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft_id="partnerSpacecraftId",
            payload_notes="Sample Notes",
            spectral_bands="Infra-Red",
        )
        assert sera_data_early_warning is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert sera_data_early_warning is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sera_data_early_warning.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.list()
        assert_matches_type(
            AsyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            AsyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[SeraDataEarlyWarningListResponse], sera_data_early_warning, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.delete(
            "id",
        )
        assert sera_data_early_warning is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert sera_data_early_warning is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sera_data_early_warning.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.count()
        assert_matches_type(str, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert_matches_type(str, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert_matches_type(str, sera_data_early_warning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.get(
            id="id",
        )
        assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert_matches_type(SeraDataEarlyWarningGetResponse, sera_data_early_warning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sera_data_early_warning.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.queryhelp()
        assert sera_data_early_warning is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert sera_data_early_warning is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert sera_data_early_warning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.tuple(
            columns="columns",
        )
        assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sera_data_early_warning = await async_client.sera_data_early_warning.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sera_data_early_warning.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sera_data_early_warning = await response.parse()
        assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sera_data_early_warning.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sera_data_early_warning = await response.parse()
            assert_matches_type(SeraDataEarlyWarningTupleResponse, sera_data_early_warning, path=["response"])

        assert cast(Any, response.is_closed) is True
