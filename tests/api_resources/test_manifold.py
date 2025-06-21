# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ManifoldGetResponse,
    ManifoldListResponse,
    ManifoldTupleResponse,
    ManifoldQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManifold:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )
        assert manifold is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
            id="MANIFOLD-ID",
            delta_t=10.23,
            delta_v=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            status="PENDING",
            weight=0.3,
        )
        assert manifold is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert manifold is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )
        assert manifold is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
            body_id="MANIFOLD-ID",
            delta_t=10.23,
            delta_v=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            status="PENDING",
            weight=0.3,
        )
        assert manifold is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert manifold is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.manifold.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_object_of_interest="OBJECTOFINTEREST-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.list()
        assert_matches_type(SyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert_matches_type(SyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert_matches_type(SyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.delete(
            "id",
        )
        assert manifold is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert manifold is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.manifold.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.count()
        assert_matches_type(str, manifold, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, manifold, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert_matches_type(str, manifold, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert_matches_type(str, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_object_of_interest": "OBJECTOFINTEREST-ID",
                    "source": "Bluestaq",
                }
            ],
        )
        assert manifold is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_object_of_interest": "OBJECTOFINTEREST-ID",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert manifold is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_object_of_interest": "OBJECTOFINTEREST-ID",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.get(
            id="id",
        )
        assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.manifold.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.queryhelp()
        assert_matches_type(ManifoldQueryhelpResponse, manifold, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert_matches_type(ManifoldQueryhelpResponse, manifold, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert_matches_type(ManifoldQueryhelpResponse, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.tuple(
            columns="columns",
        )
        assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        manifold = client.manifold.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.manifold.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = response.parse()
        assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.manifold.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = response.parse()
            assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncManifold:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )
        assert manifold is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
            id="MANIFOLD-ID",
            delta_t=10.23,
            delta_v=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            status="PENDING",
            weight=0.3,
        )
        assert manifold is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert manifold is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )
        assert manifold is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
            body_id="MANIFOLD-ID",
            delta_t=10.23,
            delta_v=10.23,
            origin="THIRD_PARTY_DATASOURCE",
            status="PENDING",
            weight=0.3,
        )
        assert manifold is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert manifold is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_object_of_interest="OBJECTOFINTEREST-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.manifold.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_object_of_interest="OBJECTOFINTEREST-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.list()
        assert_matches_type(AsyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert_matches_type(AsyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert_matches_type(AsyncOffsetPage[ManifoldListResponse], manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.delete(
            "id",
        )
        assert manifold is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert manifold is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.manifold.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.count()
        assert_matches_type(str, manifold, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, manifold, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert_matches_type(str, manifold, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert_matches_type(str, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_object_of_interest": "OBJECTOFINTEREST-ID",
                    "source": "Bluestaq",
                }
            ],
        )
        assert manifold is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_object_of_interest": "OBJECTOFINTEREST-ID",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert manifold is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_object_of_interest": "OBJECTOFINTEREST-ID",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert manifold is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.get(
            id="id",
        )
        assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert_matches_type(ManifoldGetResponse, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.manifold.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.queryhelp()
        assert_matches_type(ManifoldQueryhelpResponse, manifold, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert_matches_type(ManifoldQueryhelpResponse, manifold, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert_matches_type(ManifoldQueryhelpResponse, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.tuple(
            columns="columns",
        )
        assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        manifold = await async_client.manifold.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.manifold.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manifold = await response.parse()
        assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.manifold.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manifold = await response.parse()
            assert_matches_type(ManifoldTupleResponse, manifold, path=["response"])

        assert cast(Any, response.is_closed) is True
