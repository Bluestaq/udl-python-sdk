# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SeradataradarpayloadGetResponse,
    SeradataradarpayloadListResponse,
    SeradataradarpayloadTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeradataradarpayload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )
        assert seradataradarpayload is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
            id="SERADATARADARPAYLOAD-ID",
            bandwidth=1.23,
            best_resolution=1.23,
            category="SAR",
            constellation_interferometric_capability="constellationInterferometricCapability",
            duty_cycle="dutyCycle",
            field_of_regard=1.23,
            field_of_view=1.23,
            frequency=1.23,
            frequency_band="X",
            ground_station_locations="51,42N-44,35E",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="3c1ee9a0-90ad-1d75-c47b-2414e0a77e53",
            manufacturer_org_id="manufacturerOrgId",
            name="ALT",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft="partnerSpacecraft",
            pointing_method="Spacecraft",
            receive_polarization="Lin Dual",
            recorder_size="256",
            swath_width=1.23,
            transmit_polarization="Lin Dual",
            wave_length=1.23,
        )
        assert seradataradarpayload is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert seradataradarpayload is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )
        assert seradataradarpayload is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
            body_id="SERADATARADARPAYLOAD-ID",
            bandwidth=1.23,
            best_resolution=1.23,
            category="SAR",
            constellation_interferometric_capability="constellationInterferometricCapability",
            duty_cycle="dutyCycle",
            field_of_regard=1.23,
            field_of_view=1.23,
            frequency=1.23,
            frequency_band="X",
            ground_station_locations="51,42N-44,35E",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="3c1ee9a0-90ad-1d75-c47b-2414e0a77e53",
            manufacturer_org_id="manufacturerOrgId",
            name="ALT",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft="partnerSpacecraft",
            pointing_method="Spacecraft",
            receive_polarization="Lin Dual",
            recorder_size="256",
            swath_width=1.23,
            transmit_polarization="Lin Dual",
            wave_length=1.23,
        )
        assert seradataradarpayload is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert seradataradarpayload is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.seradataradarpayload.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="12345",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.list()
        assert_matches_type(SeradataradarpayloadListResponse, seradataradarpayload, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert_matches_type(SeradataradarpayloadListResponse, seradataradarpayload, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert_matches_type(SeradataradarpayloadListResponse, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.delete(
            "id",
        )
        assert seradataradarpayload is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert seradataradarpayload is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradataradarpayload.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.count()
        assert_matches_type(str, seradataradarpayload, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert_matches_type(str, seradataradarpayload, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert_matches_type(str, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.get(
            "id",
        )
        assert_matches_type(SeradataradarpayloadGetResponse, seradataradarpayload, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert_matches_type(SeradataradarpayloadGetResponse, seradataradarpayload, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert_matches_type(SeradataradarpayloadGetResponse, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradataradarpayload.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.queryhelp()
        assert seradataradarpayload is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert seradataradarpayload is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        seradataradarpayload = client.seradataradarpayload.tuple(
            columns="columns",
        )
        assert_matches_type(SeradataradarpayloadTupleResponse, seradataradarpayload, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.seradataradarpayload.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = response.parse()
        assert_matches_type(SeradataradarpayloadTupleResponse, seradataradarpayload, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.seradataradarpayload.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = response.parse()
            assert_matches_type(SeradataradarpayloadTupleResponse, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeradataradarpayload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )
        assert seradataradarpayload is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
            id="SERADATARADARPAYLOAD-ID",
            bandwidth=1.23,
            best_resolution=1.23,
            category="SAR",
            constellation_interferometric_capability="constellationInterferometricCapability",
            duty_cycle="dutyCycle",
            field_of_regard=1.23,
            field_of_view=1.23,
            frequency=1.23,
            frequency_band="X",
            ground_station_locations="51,42N-44,35E",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="3c1ee9a0-90ad-1d75-c47b-2414e0a77e53",
            manufacturer_org_id="manufacturerOrgId",
            name="ALT",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft="partnerSpacecraft",
            pointing_method="Spacecraft",
            receive_polarization="Lin Dual",
            recorder_size="256",
            swath_width=1.23,
            transmit_polarization="Lin Dual",
            wave_length=1.23,
        )
        assert seradataradarpayload is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert seradataradarpayload is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )
        assert seradataradarpayload is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
            body_id="SERADATARADARPAYLOAD-ID",
            bandwidth=1.23,
            best_resolution=1.23,
            category="SAR",
            constellation_interferometric_capability="constellationInterferometricCapability",
            duty_cycle="dutyCycle",
            field_of_regard=1.23,
            field_of_view=1.23,
            frequency=1.23,
            frequency_band="X",
            ground_station_locations="51,42N-44,35E",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="3c1ee9a0-90ad-1d75-c47b-2414e0a77e53",
            manufacturer_org_id="manufacturerOrgId",
            name="ALT",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            partner_spacecraft="partnerSpacecraft",
            pointing_method="Spacecraft",
            receive_polarization="Lin Dual",
            recorder_size="256",
            swath_width=1.23,
            transmit_polarization="Lin Dual",
            wave_length=1.23,
        )
        assert seradataradarpayload is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert seradataradarpayload is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.seradataradarpayload.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="12345",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.list()
        assert_matches_type(SeradataradarpayloadListResponse, seradataradarpayload, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert_matches_type(SeradataradarpayloadListResponse, seradataradarpayload, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert_matches_type(SeradataradarpayloadListResponse, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.delete(
            "id",
        )
        assert seradataradarpayload is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert seradataradarpayload is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradataradarpayload.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.count()
        assert_matches_type(str, seradataradarpayload, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert_matches_type(str, seradataradarpayload, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert_matches_type(str, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.get(
            "id",
        )
        assert_matches_type(SeradataradarpayloadGetResponse, seradataradarpayload, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert_matches_type(SeradataradarpayloadGetResponse, seradataradarpayload, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert_matches_type(SeradataradarpayloadGetResponse, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradataradarpayload.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.queryhelp()
        assert seradataradarpayload is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert seradataradarpayload is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert seradataradarpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradataradarpayload = await async_client.seradataradarpayload.tuple(
            columns="columns",
        )
        assert_matches_type(SeradataradarpayloadTupleResponse, seradataradarpayload, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradataradarpayload.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradataradarpayload = await response.parse()
        assert_matches_type(SeradataradarpayloadTupleResponse, seradataradarpayload, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradataradarpayload.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradataradarpayload = await response.parse()
            assert_matches_type(SeradataradarpayloadTupleResponse, seradataradarpayload, path=["response"])

        assert cast(Any, response.is_closed) is True
