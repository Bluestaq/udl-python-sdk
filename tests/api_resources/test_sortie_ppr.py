# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SortiePprListResponse,
    SortiePprTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.sortie_ppr import SortiePprFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSortiePpr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortie_ppr is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
            id="SORTIEPPR-ID",
            end_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_id="aa714f4d52a37ab1a00b21af9566e379",
            grantor="SMITH",
            number="07-21-07W",
            origin="THIRD_PARTY_DATASOURCE",
            remarks="PPR remark",
            requestor="jsmith1",
            start_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            type="M",
        )
        assert sortie_ppr is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert sortie_ppr is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortie_ppr is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
            body_id="SORTIEPPR-ID",
            end_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_id="aa714f4d52a37ab1a00b21af9566e379",
            grantor="SMITH",
            number="07-21-07W",
            origin="THIRD_PARTY_DATASOURCE",
            remarks="PPR remark",
            requestor="jsmith1",
            start_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            type="M",
        )
        assert sortie_ppr is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert sortie_ppr is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sortie_ppr.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.list(
            id_sortie="idSortie",
        )
        assert_matches_type(SyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.list(
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.list(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert_matches_type(SyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.list(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert_matches_type(SyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.delete(
            "id",
        )
        assert sortie_ppr is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert sortie_ppr is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sortie_ppr.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.count(
            id_sortie="idSortie",
        )
        assert_matches_type(str, sortie_ppr, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.count(
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sortie_ppr, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.count(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert_matches_type(str, sortie_ppr, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.count(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert_matches_type(str, sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortie_ppr is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert sortie_ppr is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.get(
            id="id",
        )
        assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sortie_ppr.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.queryhelp()
        assert sortie_ppr is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert sortie_ppr is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.tuple(
            columns="columns",
            id_sortie="idSortie",
        )
        assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.tuple(
            columns="columns",
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        sortie_ppr = client.sortie_ppr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortie_ppr is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = response.parse()
        assert sortie_ppr is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSortiePpr:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortie_ppr is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
            id="SORTIEPPR-ID",
            end_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_id="aa714f4d52a37ab1a00b21af9566e379",
            grantor="SMITH",
            number="07-21-07W",
            origin="THIRD_PARTY_DATASOURCE",
            remarks="PPR remark",
            requestor="jsmith1",
            start_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            type="M",
        )
        assert sortie_ppr is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert sortie_ppr is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortie_ppr is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
            body_id="SORTIEPPR-ID",
            end_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            external_id="aa714f4d52a37ab1a00b21af9566e379",
            grantor="SMITH",
            number="07-21-07W",
            origin="THIRD_PARTY_DATASOURCE",
            remarks="PPR remark",
            requestor="jsmith1",
            start_time=parse_datetime("2024-01-01T01:01:01.123Z"),
            type="M",
        )
        assert sortie_ppr is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert sortie_ppr is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sortie_ppr.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.list(
            id_sortie="idSortie",
        )
        assert_matches_type(AsyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.list(
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.list(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert_matches_type(AsyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.list(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert_matches_type(AsyncOffsetPage[SortiePprListResponse], sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.delete(
            "id",
        )
        assert sortie_ppr is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert sortie_ppr is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sortie_ppr.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.count(
            id_sortie="idSortie",
        )
        assert_matches_type(str, sortie_ppr, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.count(
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, sortie_ppr, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.count(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert_matches_type(str, sortie_ppr, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.count(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert_matches_type(str, sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortie_ppr is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert sortie_ppr is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.get(
            id="id",
        )
        assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert_matches_type(SortiePprFull, sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sortie_ppr.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.queryhelp()
        assert sortie_ppr is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert sortie_ppr is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.tuple(
            columns="columns",
            id_sortie="idSortie",
        )
        assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.tuple(
            columns="columns",
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert_matches_type(SortiePprTupleResponse, sortie_ppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortie_ppr = await async_client.sortie_ppr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortie_ppr is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortie_ppr = await response.parse()
        assert sortie_ppr is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortie_ppr = await response.parse()
            assert sortie_ppr is None

        assert cast(Any, response.is_closed) is True
