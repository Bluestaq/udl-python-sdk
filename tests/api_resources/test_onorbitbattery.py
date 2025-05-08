# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OnorbitbatteryGetResponse,
    OnorbitbatteryListResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnorbitbattery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitbattery is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
            id="ONORBITBATTERY-ID",
            battery={
                "data_mode": "TEST",
                "name": "JAK-BATTERY-1479",
                "source": "Bluestaq",
                "id": "BATTERY-ID",
                "origin": "THIRD_PARTY_DATASOURCE",
            },
            origin="THIRD_PARTY_DATASOURCE",
            quantity=5,
        )
        assert onorbitbattery is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitbattery.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = response.parse()
        assert onorbitbattery is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbitbattery.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = response.parse()
            assert onorbitbattery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitbattery is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
            body_id="ONORBITBATTERY-ID",
            battery={
                "data_mode": "TEST",
                "name": "JAK-BATTERY-1479",
                "source": "Bluestaq",
                "id": "BATTERY-ID",
                "origin": "THIRD_PARTY_DATASOURCE",
            },
            origin="THIRD_PARTY_DATASOURCE",
            quantity=5,
        )
        assert onorbitbattery is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitbattery.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = response.parse()
        assert onorbitbattery is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.onorbitbattery.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = response.parse()
            assert onorbitbattery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.onorbitbattery.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_battery="BATTERY-ID",
                id_on_orbit="ONORBIT-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.list()
        assert_matches_type(SyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitbattery.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = response.parse()
        assert_matches_type(SyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbitbattery.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = response.parse()
            assert_matches_type(SyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.delete(
            "id",
        )
        assert onorbitbattery is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitbattery.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = response.parse()
        assert onorbitbattery is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbitbattery.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = response.parse()
            assert onorbitbattery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitbattery.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.get(
            id="id",
        )
        assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitbattery = client.onorbitbattery.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitbattery.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = response.parse()
        assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.onorbitbattery.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = response.parse()
            assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitbattery.with_raw_response.get(
                id="",
            )


class TestAsyncOnorbitbattery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitbattery is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
            id="ONORBITBATTERY-ID",
            battery={
                "data_mode": "TEST",
                "name": "JAK-BATTERY-1479",
                "source": "Bluestaq",
                "id": "BATTERY-ID",
                "origin": "THIRD_PARTY_DATASOURCE",
            },
            origin="THIRD_PARTY_DATASOURCE",
            quantity=5,
        )
        assert onorbitbattery is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitbattery.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = await response.parse()
        assert onorbitbattery is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitbattery.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = await response.parse()
            assert onorbitbattery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )
        assert onorbitbattery is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
            body_id="ONORBITBATTERY-ID",
            battery={
                "data_mode": "TEST",
                "name": "JAK-BATTERY-1479",
                "source": "Bluestaq",
                "id": "BATTERY-ID",
                "origin": "THIRD_PARTY_DATASOURCE",
            },
            origin="THIRD_PARTY_DATASOURCE",
            quantity=5,
        )
        assert onorbitbattery is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitbattery.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = await response.parse()
        assert onorbitbattery is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitbattery.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_battery="BATTERY-ID",
            id_on_orbit="ONORBIT-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = await response.parse()
            assert onorbitbattery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.onorbitbattery.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_battery="BATTERY-ID",
                id_on_orbit="ONORBIT-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.list()
        assert_matches_type(AsyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitbattery.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = await response.parse()
        assert_matches_type(AsyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitbattery.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = await response.parse()
            assert_matches_type(AsyncOffsetPage[OnorbitbatteryListResponse], onorbitbattery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.delete(
            "id",
        )
        assert onorbitbattery is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitbattery.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = await response.parse()
        assert onorbitbattery is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitbattery.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = await response.parse()
            assert onorbitbattery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitbattery.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.get(
            id="id",
        )
        assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitbattery = await async_client.onorbitbattery.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitbattery.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitbattery = await response.parse()
        assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitbattery.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitbattery = await response.parse()
            assert_matches_type(OnorbitbatteryGetResponse, onorbitbattery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitbattery.with_raw_response.get(
                id="",
            )
