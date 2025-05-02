# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    StatusGetResponse,
    StatusListResponse,
    StatusTupleResponse,
    StatusGetByEntityIDResponse,
    StatusGetByEntityTypeResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        status = client.status.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )
        assert status is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
            id="STATUS-ID",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="U",
            derived_from="SOME_SOURCE",
            notes="Example Notes",
            ops_cap="FMC",
            origin="THIRD_PARTY_DATASOURCE",
            state="ACTIVE",
            sub_status_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "notes": "Sample Notes",
                    "source": "Bluestaq",
                    "status": "FMC",
                    "status_id": "REF-STATUS-ID",
                    "type": "mdCap",
                    "id": "SUBSTATUS-ID",
                    "origin": "THIRD_PARTY_DATASOURCE",
                }
            ],
            sys_cap="FMC",
        )
        assert status is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert status is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        status = client.status.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )
        assert status is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
            body_id="STATUS-ID",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="U",
            derived_from="SOME_SOURCE",
            notes="Example Notes",
            ops_cap="FMC",
            origin="THIRD_PARTY_DATASOURCE",
            state="ACTIVE",
            sub_status_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "notes": "Sample Notes",
                    "source": "Bluestaq",
                    "status": "FMC",
                    "status_id": "REF-STATUS-ID",
                    "type": "mdCap",
                    "id": "SUBSTATUS-ID",
                    "origin": "THIRD_PARTY_DATASOURCE",
                }
            ],
            sys_cap="FMC",
        )
        assert status is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert status is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.status.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_entity="ENTITY-ID",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        status = client.status.list()
        assert_matches_type(SyncOffsetPage[StatusListResponse], status, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[StatusListResponse], status, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(SyncOffsetPage[StatusListResponse], status, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(SyncOffsetPage[StatusListResponse], status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        status = client.status.delete(
            "id",
        )
        assert status is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert status is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.status.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        status = client.status.count()
        assert_matches_type(str, status, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, status, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(str, status, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(str, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        status = client.status.get(
            id="id",
        )
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusGetResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.status.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_get_by_entity_id(self, client: Unifieddatalibrary) -> None:
        status = client.status.get_by_entity_id(
            id_entity="idEntity",
        )
        assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

    @parametrize
    def test_method_get_by_entity_id_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.get_by_entity_id(
            id_entity="idEntity",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

    @parametrize
    def test_raw_response_get_by_entity_id(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.get_by_entity_id(
            id_entity="idEntity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_get_by_entity_id(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.get_by_entity_id(
            id_entity="idEntity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_entity_id(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_entity` but received ''"):
            client.status.with_raw_response.get_by_entity_id(
                id_entity="",
            )

    @parametrize
    def test_method_get_by_entity_type(self, client: Unifieddatalibrary) -> None:
        status = client.status.get_by_entity_type(
            entity_type="entityType",
        )
        assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

    @parametrize
    def test_method_get_by_entity_type_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.get_by_entity_type(
            entity_type="entityType",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

    @parametrize
    def test_raw_response_get_by_entity_type(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.get_by_entity_type(
            entity_type="entityType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_get_by_entity_type(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.get_by_entity_type(
            entity_type="entityType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_entity_type(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_type` but received ''"):
            client.status.with_raw_response.get_by_entity_type(
                entity_type="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        status = client.status.queryhelp()
        assert status is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert status is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        status = client.status.tuple(
            columns="columns",
        )
        assert_matches_type(StatusTupleResponse, status, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        status = client.status.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusTupleResponse, status, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.status.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusTupleResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.status.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusTupleResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )
        assert status is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
            id="STATUS-ID",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="U",
            derived_from="SOME_SOURCE",
            notes="Example Notes",
            ops_cap="FMC",
            origin="THIRD_PARTY_DATASOURCE",
            state="ACTIVE",
            sub_status_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "notes": "Sample Notes",
                    "source": "Bluestaq",
                    "status": "FMC",
                    "status_id": "REF-STATUS-ID",
                    "type": "mdCap",
                    "id": "SUBSTATUS-ID",
                    "origin": "THIRD_PARTY_DATASOURCE",
                }
            ],
            sys_cap="FMC",
        )
        assert status is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert status is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )
        assert status is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
            body_id="STATUS-ID",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="U",
            derived_from="SOME_SOURCE",
            notes="Example Notes",
            ops_cap="FMC",
            origin="THIRD_PARTY_DATASOURCE",
            state="ACTIVE",
            sub_status_collection=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "notes": "Sample Notes",
                    "source": "Bluestaq",
                    "status": "FMC",
                    "status_id": "REF-STATUS-ID",
                    "type": "mdCap",
                    "id": "SUBSTATUS-ID",
                    "origin": "THIRD_PARTY_DATASOURCE",
                }
            ],
            sys_cap="FMC",
        )
        assert status is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert status is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            id_entity="ENTITY-ID",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.status.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                id_entity="ENTITY-ID",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.list()
        assert_matches_type(AsyncOffsetPage[StatusListResponse], status, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[StatusListResponse], status, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(AsyncOffsetPage[StatusListResponse], status, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(AsyncOffsetPage[StatusListResponse], status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.delete(
            "id",
        )
        assert status is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert status is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.status.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.count()
        assert_matches_type(str, status, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, status, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(str, status, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(str, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.get(
            id="id",
        )
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusGetResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.status.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_get_by_entity_id(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.get_by_entity_id(
            id_entity="idEntity",
        )
        assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

    @parametrize
    async def test_method_get_by_entity_id_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.get_by_entity_id(
            id_entity="idEntity",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_get_by_entity_id(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.get_by_entity_id(
            id_entity="idEntity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_entity_id(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.get_by_entity_id(
            id_entity="idEntity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusGetByEntityIDResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_entity_id(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_entity` but received ''"):
            await async_client.status.with_raw_response.get_by_entity_id(
                id_entity="",
            )

    @parametrize
    async def test_method_get_by_entity_type(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.get_by_entity_type(
            entity_type="entityType",
        )
        assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

    @parametrize
    async def test_method_get_by_entity_type_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.get_by_entity_type(
            entity_type="entityType",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_get_by_entity_type(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.get_by_entity_type(
            entity_type="entityType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_entity_type(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.get_by_entity_type(
            entity_type="entityType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusGetByEntityTypeResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_entity_type(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_type` but received ''"):
            await async_client.status.with_raw_response.get_by_entity_type(
                entity_type="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.queryhelp()
        assert status is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert status is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.tuple(
            columns="columns",
        )
        assert_matches_type(StatusTupleResponse, status, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        status = await async_client.status.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(StatusTupleResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.status.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusTupleResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.status.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusTupleResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True
