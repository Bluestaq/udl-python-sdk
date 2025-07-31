# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EngineDetailsAbridged,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import EngineDetailsFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEngineDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )
        assert engine_detail is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
            id="ENGINEDETAILS-ID",
            burn_time=1.1,
            chamber_pressure=1.1,
            characteristic_type="Electric",
            cycle_type="Pressure Fed",
            family="ENGINE_TYPE1",
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_firings=5,
            notes="Example notes",
            nozzle_expansion_ratio=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Liquid Oxygen",
            propellant="Liquid",
            sea_level_thrust=1.1,
            specific_impulse=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            vacuum_thrust=1.1,
        )
        assert engine_detail is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert engine_detail is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.retrieve(
            id="id",
        )
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.engine_details.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )
        assert engine_detail is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
            body_id="ENGINEDETAILS-ID",
            burn_time=1.1,
            chamber_pressure=1.1,
            characteristic_type="Electric",
            cycle_type="Pressure Fed",
            family="ENGINE_TYPE1",
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_firings=5,
            notes="Example notes",
            nozzle_expansion_ratio=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Liquid Oxygen",
            propellant="Liquid",
            sea_level_thrust=1.1,
            specific_impulse=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            vacuum_thrust=1.1,
        )
        assert engine_detail is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert engine_detail is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.engine_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_engine="ENGINE-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.list()
        assert_matches_type(SyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert_matches_type(SyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert_matches_type(SyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        engine_detail = client.engine_details.delete(
            "id",
        )
        assert engine_detail is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.engine_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = response.parse()
        assert engine_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.engine_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.engine_details.with_raw_response.delete(
                "",
            )


class TestAsyncEngineDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )
        assert engine_detail is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
            id="ENGINEDETAILS-ID",
            burn_time=1.1,
            chamber_pressure=1.1,
            characteristic_type="Electric",
            cycle_type="Pressure Fed",
            family="ENGINE_TYPE1",
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_firings=5,
            notes="Example notes",
            nozzle_expansion_ratio=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Liquid Oxygen",
            propellant="Liquid",
            sea_level_thrust=1.1,
            specific_impulse=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            vacuum_thrust=1.1,
        )
        assert engine_detail is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert engine_detail is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.retrieve(
            id="id",
        )
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert_matches_type(EngineDetailsFull, engine_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.engine_details.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )
        assert engine_detail is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
            body_id="ENGINEDETAILS-ID",
            burn_time=1.1,
            chamber_pressure=1.1,
            characteristic_type="Electric",
            cycle_type="Pressure Fed",
            family="ENGINE_TYPE1",
            manufacturer_org_id="MANUFACTURERORG-ID",
            max_firings=5,
            notes="Example notes",
            nozzle_expansion_ratio=1.1,
            origin="THIRD_PARTY_DATASOURCE",
            oxidizer="Liquid Oxygen",
            propellant="Liquid",
            sea_level_thrust=1.1,
            specific_impulse=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            vacuum_thrust=1.1,
        )
        assert engine_detail is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert engine_detail is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_engine="ENGINE-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.engine_details.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_engine="ENGINE-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.list()
        assert_matches_type(AsyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert_matches_type(AsyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert_matches_type(AsyncOffsetPage[EngineDetailsAbridged], engine_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine_detail = await async_client.engine_details.delete(
            "id",
        )
        assert engine_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engine_details.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine_detail = await response.parse()
        assert engine_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engine_details.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine_detail = await response.parse()
            assert engine_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.engine_details.with_raw_response.delete(
                "",
            )
