# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.supporting_data import DataTypeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        data_type = client.supporting_data.data_types.list()
        assert_matches_type(SyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        data_type = client.supporting_data.data_types.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.supporting_data.data_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_type = response.parse()
        assert_matches_type(SyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.supporting_data.data_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_type = response.parse()
            assert_matches_type(SyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        data_type = await async_client.supporting_data.data_types.list()
        assert_matches_type(AsyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        data_type = await async_client.supporting_data.data_types.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.supporting_data.data_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_type = await response.parse()
        assert_matches_type(AsyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.supporting_data.data_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_type = await response.parse()
            assert_matches_type(AsyncOffsetPage[DataTypeListResponse], data_type, path=["response"])

        assert cast(Any, response.is_closed) is True
