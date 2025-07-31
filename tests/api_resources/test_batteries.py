# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    BatteryAbridged,
    BatteryTupleResponse,
    BatteryQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import BatteryFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatteries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )
        assert battery is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
            id="BATTERY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert battery is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert battery is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert battery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.retrieve(
            id="id",
        )
        assert_matches_type(BatteryFull, battery, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BatteryFull, battery, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert_matches_type(BatteryFull, battery, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert_matches_type(BatteryFull, battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.batteries.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )
        assert battery is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
            body_id="BATTERY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert battery is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert battery is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert battery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.batteries.with_raw_response.update(
                path_id="",
                data_mode="TEST",
                name="JAK-BATTERY-1479",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.list()
        assert_matches_type(SyncOffsetPage[BatteryAbridged], battery, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[BatteryAbridged], battery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert_matches_type(SyncOffsetPage[BatteryAbridged], battery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert_matches_type(SyncOffsetPage[BatteryAbridged], battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.delete(
            "id",
        )
        assert battery is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert battery is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert battery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.batteries.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.count()
        assert_matches_type(str, battery, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, battery, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert_matches_type(str, battery, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert_matches_type(str, battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.queryhelp()
        assert_matches_type(BatteryQueryhelpResponse, battery, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert_matches_type(BatteryQueryhelpResponse, battery, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert_matches_type(BatteryQueryhelpResponse, battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.tuple(
            columns="columns",
        )
        assert_matches_type(BatteryTupleResponse, battery, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        battery = client.batteries.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BatteryTupleResponse, battery, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.batteries.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = response.parse()
        assert_matches_type(BatteryTupleResponse, battery, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.batteries.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = response.parse()
            assert_matches_type(BatteryTupleResponse, battery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatteries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )
        assert battery is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
            id="BATTERY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert battery is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert battery is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.create(
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert battery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.retrieve(
            id="id",
        )
        assert_matches_type(BatteryFull, battery, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BatteryFull, battery, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert_matches_type(BatteryFull, battery, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert_matches_type(BatteryFull, battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.batteries.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )
        assert battery is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
            body_id="BATTERY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert battery is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert battery is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.update(
            path_id="id",
            data_mode="TEST",
            name="JAK-BATTERY-1479",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert battery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.batteries.with_raw_response.update(
                path_id="",
                data_mode="TEST",
                name="JAK-BATTERY-1479",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.list()
        assert_matches_type(AsyncOffsetPage[BatteryAbridged], battery, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[BatteryAbridged], battery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert_matches_type(AsyncOffsetPage[BatteryAbridged], battery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert_matches_type(AsyncOffsetPage[BatteryAbridged], battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.delete(
            "id",
        )
        assert battery is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert battery is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert battery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.batteries.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.count()
        assert_matches_type(str, battery, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, battery, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert_matches_type(str, battery, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert_matches_type(str, battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.queryhelp()
        assert_matches_type(BatteryQueryhelpResponse, battery, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert_matches_type(BatteryQueryhelpResponse, battery, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert_matches_type(BatteryQueryhelpResponse, battery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.tuple(
            columns="columns",
        )
        assert_matches_type(BatteryTupleResponse, battery, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        battery = await async_client.batteries.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(BatteryTupleResponse, battery, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.batteries.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        battery = await response.parse()
        assert_matches_type(BatteryTupleResponse, battery, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.batteries.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            battery = await response.parse()
            assert_matches_type(BatteryTupleResponse, battery, path=["response"])

        assert cast(Any, response.is_closed) is True
