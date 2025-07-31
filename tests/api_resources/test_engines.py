# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EngineAbridged,
    EngineTupleResponse,
    EngineQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import Engine

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEngines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )
        assert engine is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
            id="ENGINE-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert engine is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert engine is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert engine is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.retrieve(
            id="id",
        )
        assert_matches_type(Engine, engine, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(Engine, engine, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(Engine, engine, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(Engine, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.engines.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )
        assert engine is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
            body_id="ENGINE-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert engine is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert engine is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert engine is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.engines.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="ENGINE_VARIANT1",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.list()
        assert_matches_type(SyncOffsetPage[EngineAbridged], engine, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EngineAbridged], engine, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(SyncOffsetPage[EngineAbridged], engine, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(SyncOffsetPage[EngineAbridged], engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.delete(
            "id",
        )
        assert engine is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert engine is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert engine is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.engines.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.count()
        assert_matches_type(str, engine, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, engine, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(str, engine, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(str, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.queryhelp()
        assert_matches_type(EngineQueryhelpResponse, engine, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(EngineQueryhelpResponse, engine, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(EngineQueryhelpResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.tuple(
            columns="columns",
        )
        assert_matches_type(EngineTupleResponse, engine, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        engine = client.engines.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EngineTupleResponse, engine, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.engines.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(EngineTupleResponse, engine, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.engines.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(EngineTupleResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEngines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )
        assert engine is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
            id="ENGINE-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert engine is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert engine is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert engine is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.retrieve(
            id="id",
        )
        assert_matches_type(Engine, engine, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(Engine, engine, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(Engine, engine, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(Engine, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.engines.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )
        assert engine is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
            body_id="ENGINE-ID",
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert engine is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert engine is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="ENGINE_VARIANT1",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert engine is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.engines.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="ENGINE_VARIANT1",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.list()
        assert_matches_type(AsyncOffsetPage[EngineAbridged], engine, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EngineAbridged], engine, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(AsyncOffsetPage[EngineAbridged], engine, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(AsyncOffsetPage[EngineAbridged], engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.delete(
            "id",
        )
        assert engine is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert engine is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert engine is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.engines.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.count()
        assert_matches_type(str, engine, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, engine, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(str, engine, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(str, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.queryhelp()
        assert_matches_type(EngineQueryhelpResponse, engine, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(EngineQueryhelpResponse, engine, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(EngineQueryhelpResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.tuple(
            columns="columns",
        )
        assert_matches_type(EngineTupleResponse, engine, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        engine = await async_client.engines.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EngineTupleResponse, engine, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.engines.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(EngineTupleResponse, engine, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.engines.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(EngineTupleResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True
