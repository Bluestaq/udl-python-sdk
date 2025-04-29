# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.supporting_data import (
    DataownerRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataowner:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        dataowner = client.supporting_data.dataowner.retrieve()
        assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        dataowner = client.supporting_data.dataowner.retrieve(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.supporting_data.dataowner.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataowner = response.parse()
        assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.supporting_data.dataowner.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataowner = response.parse()
            assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        dataowner = client.supporting_data.dataowner.count()
        assert_matches_type(str, dataowner, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        dataowner = client.supporting_data.dataowner.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, dataowner, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.supporting_data.dataowner.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataowner = response.parse()
        assert_matches_type(str, dataowner, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.supporting_data.dataowner.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataowner = response.parse()
            assert_matches_type(str, dataowner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataowner:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        dataowner = await async_client.supporting_data.dataowner.retrieve()
        assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dataowner = await async_client.supporting_data.dataowner.retrieve(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.supporting_data.dataowner.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataowner = await response.parse()
        assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.supporting_data.dataowner.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataowner = await response.parse()
            assert_matches_type(DataownerRetrieveResponse, dataowner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        dataowner = await async_client.supporting_data.dataowner.count()
        assert_matches_type(str, dataowner, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        dataowner = await async_client.supporting_data.dataowner.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, dataowner, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.supporting_data.dataowner.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataowner = await response.parse()
        assert_matches_type(str, dataowner, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.supporting_data.dataowner.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataowner = await response.parse()
            assert_matches_type(str, dataowner, path=["response"])

        assert cast(Any, response.is_closed) is True
