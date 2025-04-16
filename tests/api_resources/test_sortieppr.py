# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SortiepprListResponse,
    SortiepprTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.sortieppr import SortiePprFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSortieppr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortieppr is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.create(
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
        assert sortieppr is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert sortieppr is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortieppr is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.update(
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
        assert sortieppr is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert sortieppr is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.sortieppr.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.list(
            id_sortie="idSortie",
        )
        assert_matches_type(SortiepprListResponse, sortieppr, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.list(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert_matches_type(SortiepprListResponse, sortieppr, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.list(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert_matches_type(SortiepprListResponse, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.delete(
            "id",
        )
        assert sortieppr is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert sortieppr is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sortieppr.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.count(
            id_sortie="idSortie",
        )
        assert_matches_type(str, sortieppr, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.count(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert_matches_type(str, sortieppr, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.count(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert_matches_type(str, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortieppr is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.create_bulk(
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
        sortieppr = response.parse()
        assert sortieppr is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.create_bulk(
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

            sortieppr = response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.get(
            "id",
        )
        assert_matches_type(SortiePprFull, sortieppr, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert_matches_type(SortiePprFull, sortieppr, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert_matches_type(SortiePprFull, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sortieppr.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.queryhelp()
        assert sortieppr is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert sortieppr is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.tuple(
            columns="columns",
            id_sortie="idSortie",
        )
        assert_matches_type(SortiepprTupleResponse, sortieppr, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = response.parse()
        assert_matches_type(SortiepprTupleResponse, sortieppr, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = response.parse()
            assert_matches_type(SortiepprTupleResponse, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        sortieppr = client.sortieppr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortieppr is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.sortieppr.with_raw_response.unvalidated_publish(
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
        sortieppr = response.parse()
        assert sortieppr is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.sortieppr.with_streaming_response.unvalidated_publish(
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

            sortieppr = response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSortieppr:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortieppr is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.create(
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
        assert sortieppr is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert sortieppr is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )
        assert sortieppr is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.update(
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
        assert sortieppr is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert sortieppr is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.sortieppr.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_sortie="4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.list(
            id_sortie="idSortie",
        )
        assert_matches_type(SortiepprListResponse, sortieppr, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.list(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert_matches_type(SortiepprListResponse, sortieppr, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.list(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert_matches_type(SortiepprListResponse, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.delete(
            "id",
        )
        assert sortieppr is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert sortieppr is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sortieppr.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.count(
            id_sortie="idSortie",
        )
        assert_matches_type(str, sortieppr, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.count(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert_matches_type(str, sortieppr, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.count(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert_matches_type(str, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortieppr is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.create_bulk(
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
        sortieppr = await response.parse()
        assert sortieppr is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.create_bulk(
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

            sortieppr = await response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.get(
            "id",
        )
        assert_matches_type(SortiePprFull, sortieppr, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert_matches_type(SortiePprFull, sortieppr, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert_matches_type(SortiePprFull, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sortieppr.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.queryhelp()
        assert sortieppr is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert sortieppr is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.tuple(
            columns="columns",
            id_sortie="idSortie",
        )
        assert_matches_type(SortiepprTupleResponse, sortieppr, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sortieppr = await response.parse()
        assert_matches_type(SortiepprTupleResponse, sortieppr, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.tuple(
            columns="columns",
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sortieppr = await response.parse()
            assert_matches_type(SortiepprTupleResponse, sortieppr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        sortieppr = await async_client.sortieppr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_sortie": "4ef3d1e8-ab08-ab70-498f-edc479734e5c",
                    "source": "Bluestaq",
                }
            ],
        )
        assert sortieppr is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortieppr.with_raw_response.unvalidated_publish(
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
        sortieppr = await response.parse()
        assert sortieppr is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortieppr.with_streaming_response.unvalidated_publish(
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

            sortieppr = await response.parse()
            assert sortieppr is None

        assert cast(Any, response.is_closed) is True
