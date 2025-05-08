# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EquipmentRemarkFull,
    EquipmentRemarkAbridged,
    EquipmentRemarkTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEquipmentRemarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
        )
        assert equipment_remark is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            alt_rmk_id="123456ABC",
            code="M",
            name="Remark name",
            origin="THIRD_PARTY_DATASOURCE",
            type="Restriction",
        )
        assert equipment_remark is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.equipment_remarks.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = response.parse()
        assert equipment_remark is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.equipment_remarks.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = response.parse()
            assert equipment_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.retrieve(
            id="id",
        )
        assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.equipment_remarks.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = response.parse()
        assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.equipment_remarks.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = response.parse()
            assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.equipment_remarks.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.list()
        assert_matches_type(SyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.equipment_remarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = response.parse()
        assert_matches_type(SyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.equipment_remarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = response.parse()
            assert_matches_type(SyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.count()
        assert_matches_type(str, equipment_remark, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, equipment_remark, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.equipment_remarks.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = response.parse()
        assert_matches_type(str, equipment_remark, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.equipment_remarks.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = response.parse()
            assert_matches_type(str, equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_equipment": "EQUIPMENT-ID",
                    "source": "Bluestaq",
                    "text": "This is a remark",
                }
            ],
        )
        assert equipment_remark is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.equipment_remarks.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_equipment": "EQUIPMENT-ID",
                    "source": "Bluestaq",
                    "text": "This is a remark",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = response.parse()
        assert equipment_remark is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.equipment_remarks.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_equipment": "EQUIPMENT-ID",
                    "source": "Bluestaq",
                    "text": "This is a remark",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = response.parse()
            assert equipment_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.query_help()
        assert equipment_remark is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.equipment_remarks.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = response.parse()
        assert equipment_remark is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.equipment_remarks.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = response.parse()
            assert equipment_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.tuple(
            columns="columns",
        )
        assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        equipment_remark = client.equipment_remarks.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.equipment_remarks.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = response.parse()
        assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.equipment_remarks.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = response.parse()
            assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEquipmentRemarks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
        )
        assert equipment_remark is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            alt_rmk_id="123456ABC",
            code="M",
            name="Remark name",
            origin="THIRD_PARTY_DATASOURCE",
            type="Restriction",
        )
        assert equipment_remark is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment_remarks.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = await response.parse()
        assert equipment_remark is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment_remarks.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_equipment="EQUIPMENT-ID",
            source="Bluestaq",
            text="This is a remark",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = await response.parse()
            assert equipment_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.retrieve(
            id="id",
        )
        assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment_remarks.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = await response.parse()
        assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment_remarks.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = await response.parse()
            assert_matches_type(EquipmentRemarkFull, equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.equipment_remarks.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.list()
        assert_matches_type(AsyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment_remarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = await response.parse()
        assert_matches_type(AsyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment_remarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = await response.parse()
            assert_matches_type(AsyncOffsetPage[EquipmentRemarkAbridged], equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.count()
        assert_matches_type(str, equipment_remark, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, equipment_remark, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment_remarks.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = await response.parse()
        assert_matches_type(str, equipment_remark, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment_remarks.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = await response.parse()
            assert_matches_type(str, equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_equipment": "EQUIPMENT-ID",
                    "source": "Bluestaq",
                    "text": "This is a remark",
                }
            ],
        )
        assert equipment_remark is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment_remarks.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_equipment": "EQUIPMENT-ID",
                    "source": "Bluestaq",
                    "text": "This is a remark",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = await response.parse()
        assert equipment_remark is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment_remarks.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "id_equipment": "EQUIPMENT-ID",
                    "source": "Bluestaq",
                    "text": "This is a remark",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = await response.parse()
            assert equipment_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.query_help()
        assert equipment_remark is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment_remarks.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = await response.parse()
        assert equipment_remark is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment_remarks.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = await response.parse()
            assert equipment_remark is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.tuple(
            columns="columns",
        )
        assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        equipment_remark = await async_client.equipment_remarks.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.equipment_remarks.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        equipment_remark = await response.parse()
        assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.equipment_remarks.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            equipment_remark = await response.parse()
            assert_matches_type(EquipmentRemarkTupleResponse, equipment_remark, path=["response"])

        assert cast(Any, response.is_closed) is True
