# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    PortGetResponse,
    PortListResponse,
    PortTupleResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPort:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        port = client.port.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert port is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        port = client.port.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            avg_duration=41.1,
            country_code="US",
            external_id="fe4ad5dc-0128-4ce8-b09c-0b404322025e",
            harbor_size=160.1,
            harbor_type="COASTAL NATURAL",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            lat=45.23,
            locode="CAVAN",
            lon=179.1,
            max_draught=18.1,
            origin="THIRD_PARTY_DATASOURCE",
            pilot_reqd=True,
            port_name="Vancouver",
            shelter="EXCELLENT",
            tide_range=4.1,
        )
        assert port is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert port is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        port = client.port.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert port is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        port = client.port.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            avg_duration=41.1,
            country_code="US",
            external_id="fe4ad5dc-0128-4ce8-b09c-0b404322025e",
            harbor_size=160.1,
            harbor_type="COASTAL NATURAL",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            lat=45.23,
            locode="CAVAN",
            lon=179.1,
            max_draught=18.1,
            origin="THIRD_PARTY_DATASOURCE",
            pilot_reqd=True,
            port_name="Vancouver",
            shelter="EXCELLENT",
            tide_range=4.1,
        )
        assert port is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert port is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.port.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        port = client.port.list()
        assert_matches_type(SyncOffsetPage[PortListResponse], port, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        port = client.port.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[PortListResponse], port, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(SyncOffsetPage[PortListResponse], port, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(SyncOffsetPage[PortListResponse], port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        port = client.port.count()
        assert_matches_type(str, port, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        port = client.port.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, port, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(str, port, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(str, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        port = client.port.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert port is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert port is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        port = client.port.get(
            id="id",
        )
        assert_matches_type(PortGetResponse, port, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        port = client.port.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PortGetResponse, port, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(PortGetResponse, port, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(PortGetResponse, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.port.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        port = client.port.queryhelp()
        assert port is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert port is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        port = client.port.tuple(
            columns="columns",
        )
        assert_matches_type(PortTupleResponse, port, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        port = client.port.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PortTupleResponse, port, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.port.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = response.parse()
        assert_matches_type(PortTupleResponse, port, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.port.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = response.parse()
            assert_matches_type(PortTupleResponse, port, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPort:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert port is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            avg_duration=41.1,
            country_code="US",
            external_id="fe4ad5dc-0128-4ce8-b09c-0b404322025e",
            harbor_size=160.1,
            harbor_type="COASTAL NATURAL",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            lat=45.23,
            locode="CAVAN",
            lon=179.1,
            max_draught=18.1,
            origin="THIRD_PARTY_DATASOURCE",
            pilot_reqd=True,
            port_name="Vancouver",
            shelter="EXCELLENT",
            tide_range=4.1,
        )
        assert port is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert port is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert port is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            avg_duration=41.1,
            country_code="US",
            external_id="fe4ad5dc-0128-4ce8-b09c-0b404322025e",
            harbor_size=160.1,
            harbor_type="COASTAL NATURAL",
            id_site="a150b3ee-884b-b9ac-60a0-6408b4b16088",
            lat=45.23,
            locode="CAVAN",
            lon=179.1,
            max_draught=18.1,
            origin="THIRD_PARTY_DATASOURCE",
            pilot_reqd=True,
            port_name="Vancouver",
            shelter="EXCELLENT",
            tide_range=4.1,
        )
        assert port is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert port is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.port.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.list()
        assert_matches_type(AsyncOffsetPage[PortListResponse], port, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[PortListResponse], port, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(AsyncOffsetPage[PortListResponse], port, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(AsyncOffsetPage[PortListResponse], port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.count()
        assert_matches_type(str, port, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, port, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(str, port, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(str, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert port is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert port is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.get(
            id="id",
        )
        assert_matches_type(PortGetResponse, port, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PortGetResponse, port, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(PortGetResponse, port, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(PortGetResponse, port, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.port.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.queryhelp()
        assert port is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert port is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert port is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.tuple(
            columns="columns",
        )
        assert_matches_type(PortTupleResponse, port, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        port = await async_client.port.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PortTupleResponse, port, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.port.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        port = await response.parse()
        assert_matches_type(PortTupleResponse, port, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.port.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            port = await response.parse()
            assert_matches_type(PortTupleResponse, port, path=["response"])

        assert cast(Any, response.is_closed) is True
