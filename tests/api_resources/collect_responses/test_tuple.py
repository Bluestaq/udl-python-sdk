# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import CollectResponseFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTuple:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        tuple_ = client.collect_responses.tuple.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        tuple_ = client.collect_responses.tuple.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.tuple.with_raw_response.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tuple_ = response.parse()
        assert_matches_type(SyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.tuple.with_streaming_response.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tuple_ = response.parse()
            assert_matches_type(SyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTuple:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        tuple_ = await async_client.collect_responses.tuple.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        tuple_ = await async_client.collect_responses.tuple.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.tuple.with_raw_response.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tuple_ = await response.parse()
        assert_matches_type(AsyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.tuple.with_streaming_response.list(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tuple_ = await response.parse()
            assert_matches_type(AsyncOffsetPage[CollectResponseFull], tuple_, path=["response"])

        assert cast(Any, response.is_closed) is True
