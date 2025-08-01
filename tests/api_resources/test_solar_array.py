# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SolarArrayListResponse,
    SolarArrayTupleResponse,
    SolarArrayQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import SolarArrayFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSolarArray:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )
        assert solar_array is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
            id="SOLARARRAY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert solar_array is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert solar_array is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert solar_array is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )
        assert solar_array is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
            body_id="SOLARARRAY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert solar_array is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert solar_array is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert solar_array is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.solar_array.with_raw_response.update(
                path_id="",
                data_mode="TEST",
                name="Solar1",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.list()
        assert_matches_type(SyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert_matches_type(SyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert_matches_type(SyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.delete(
            "id",
        )
        assert solar_array is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert solar_array is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert solar_array is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.solar_array.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.count()
        assert_matches_type(str, solar_array, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, solar_array, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert_matches_type(str, solar_array, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert_matches_type(str, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.get(
            id="id",
        )
        assert_matches_type(SolarArrayFull, solar_array, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SolarArrayFull, solar_array, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert_matches_type(SolarArrayFull, solar_array, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert_matches_type(SolarArrayFull, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.solar_array.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.queryhelp()
        assert_matches_type(SolarArrayQueryhelpResponse, solar_array, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert_matches_type(SolarArrayQueryhelpResponse, solar_array, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert_matches_type(SolarArrayQueryhelpResponse, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.tuple(
            columns="columns",
        )
        assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        solar_array = client.solar_array.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.solar_array.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = response.parse()
        assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.solar_array.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = response.parse()
            assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSolarArray:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )
        assert solar_array is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
            id="SOLARARRAY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert solar_array is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert solar_array is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.create(
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert solar_array is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )
        assert solar_array is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
            body_id="SOLARARRAY-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert solar_array is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert solar_array is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.update(
            path_id="id",
            data_mode="TEST",
            name="Solar1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert solar_array is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.solar_array.with_raw_response.update(
                path_id="",
                data_mode="TEST",
                name="Solar1",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.list()
        assert_matches_type(AsyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert_matches_type(AsyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert_matches_type(AsyncOffsetPage[SolarArrayListResponse], solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.delete(
            "id",
        )
        assert solar_array is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert solar_array is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert solar_array is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.solar_array.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.count()
        assert_matches_type(str, solar_array, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, solar_array, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert_matches_type(str, solar_array, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert_matches_type(str, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.get(
            id="id",
        )
        assert_matches_type(SolarArrayFull, solar_array, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SolarArrayFull, solar_array, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert_matches_type(SolarArrayFull, solar_array, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert_matches_type(SolarArrayFull, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.solar_array.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.queryhelp()
        assert_matches_type(SolarArrayQueryhelpResponse, solar_array, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert_matches_type(SolarArrayQueryhelpResponse, solar_array, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert_matches_type(SolarArrayQueryhelpResponse, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.tuple(
            columns="columns",
        )
        assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        solar_array = await async_client.solar_array.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.solar_array.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solar_array = await response.parse()
        assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.solar_array.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solar_array = await response.parse()
            assert_matches_type(SolarArrayTupleResponse, solar_array, path=["response"])

        assert cast(Any, response.is_closed) is True
