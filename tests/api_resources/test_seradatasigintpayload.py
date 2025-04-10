# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SeradatasigintpayloadGetResponse,
    SeradatasigintpayloadListResponse,
    SeradatasigintpayloadTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeradatasigintpayload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatasigintpayload is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATASIGINTPAYLOAD-ID",
            frequency_coverage="1.1 to 3.3",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="0c5ec9c0-10cd-1d35-c46b-3764c4d76e13",
            intercept_parameters="interceptParameters",
            manufacturer_org_id="manufacturerOrgId",
            name="Sensor Name",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            positional_accuracy="positionalAccuracy",
            swath_width=1.23,
            type="Comint",
        )
        assert seradatasigintpayload is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert seradatasigintpayload is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatasigintpayload is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATASIGINTPAYLOAD-ID",
            frequency_coverage="1.1 to 3.3",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="0c5ec9c0-10cd-1d35-c46b-3764c4d76e13",
            intercept_parameters="interceptParameters",
            manufacturer_org_id="manufacturerOrgId",
            name="Sensor Name",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            positional_accuracy="positionalAccuracy",
            swath_width=1.23,
            type="Comint",
        )
        assert seradatasigintpayload is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert seradatasigintpayload is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.seradatasigintpayload.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.list()
        assert_matches_type(SeradatasigintpayloadListResponse, seradatasigintpayload, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert_matches_type(SeradatasigintpayloadListResponse, seradatasigintpayload, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert_matches_type(SeradatasigintpayloadListResponse, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.delete(
            "id",
        )
        assert seradatasigintpayload is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert seradatasigintpayload is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradatasigintpayload.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.count()
        assert_matches_type(str, seradatasigintpayload, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert_matches_type(str, seradatasigintpayload, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert_matches_type(str, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.get(
            "id",
        )
        assert_matches_type(SeradatasigintpayloadGetResponse, seradatasigintpayload, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert_matches_type(SeradatasigintpayloadGetResponse, seradatasigintpayload, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert_matches_type(SeradatasigintpayloadGetResponse, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.seradatasigintpayload.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.queryhelp()
        assert seradatasigintpayload is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert seradatasigintpayload is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        seradatasigintpayload = client.seradatasigintpayload.tuple(
            columns="columns",
        )
        assert_matches_type(SeradatasigintpayloadTupleResponse, seradatasigintpayload, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.seradatasigintpayload.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = response.parse()
        assert_matches_type(SeradatasigintpayloadTupleResponse, seradatasigintpayload, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.seradatasigintpayload.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = response.parse()
            assert_matches_type(SeradatasigintpayloadTupleResponse, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeradatasigintpayload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatasigintpayload is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            id="SERADATASIGINTPAYLOAD-ID",
            frequency_coverage="1.1 to 3.3",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="0c5ec9c0-10cd-1d35-c46b-3764c4d76e13",
            intercept_parameters="interceptParameters",
            manufacturer_org_id="manufacturerOrgId",
            name="Sensor Name",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            positional_accuracy="positionalAccuracy",
            swath_width=1.23,
            type="Comint",
        )
        assert seradatasigintpayload is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert seradatasigintpayload is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )
        assert seradatasigintpayload is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
            body_id="SERADATASIGINTPAYLOAD-ID",
            frequency_coverage="1.1 to 3.3",
            ground_station_locations="groundStationLocations",
            ground_stations="groundStations",
            hosted_for_company_org_id="hostedForCompanyOrgId",
            id_sensor="0c5ec9c0-10cd-1d35-c46b-3764c4d76e13",
            intercept_parameters="interceptParameters",
            manufacturer_org_id="manufacturerOrgId",
            name="Sensor Name",
            notes="Sample Notes",
            origin="THIRD_PARTY_DATASOURCE",
            positional_accuracy="positionalAccuracy",
            swath_width=1.23,
            type="Comint",
        )
        assert seradatasigintpayload is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert seradatasigintpayload is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            spacecraft_id="spacecraftId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.seradatasigintpayload.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                spacecraft_id="spacecraftId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.list()
        assert_matches_type(SeradatasigintpayloadListResponse, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert_matches_type(SeradatasigintpayloadListResponse, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert_matches_type(SeradatasigintpayloadListResponse, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.delete(
            "id",
        )
        assert seradatasigintpayload is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert seradatasigintpayload is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradatasigintpayload.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.count()
        assert_matches_type(str, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert_matches_type(str, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert_matches_type(str, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.get(
            "id",
        )
        assert_matches_type(SeradatasigintpayloadGetResponse, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert_matches_type(SeradatasigintpayloadGetResponse, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert_matches_type(SeradatasigintpayloadGetResponse, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.seradatasigintpayload.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.queryhelp()
        assert seradatasigintpayload is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert seradatasigintpayload is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert seradatasigintpayload is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        seradatasigintpayload = await async_client.seradatasigintpayload.tuple(
            columns="columns",
        )
        assert_matches_type(SeradatasigintpayloadTupleResponse, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.seradatasigintpayload.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seradatasigintpayload = await response.parse()
        assert_matches_type(SeradatasigintpayloadTupleResponse, seradatasigintpayload, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.seradatasigintpayload.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seradatasigintpayload = await response.parse()
            assert_matches_type(SeradatasigintpayloadTupleResponse, seradatasigintpayload, path=["response"])

        assert cast(Any, response.is_closed) is True
