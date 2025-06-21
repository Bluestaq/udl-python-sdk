# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    DriftHistoryTupleResponse,
    DriftHistoryQueryhelpResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import DriftHistoryFull, DriftHistoryAbridged

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDriftHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.retrieve(
            id="id",
        )
        assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.drift_history.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = response.parse()
        assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.drift_history.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = response.parse()
            assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.drift_history.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.list()
        assert_matches_type(SyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.drift_history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = response.parse()
        assert_matches_type(SyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.drift_history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = response.parse()
            assert_matches_type(SyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.count()
        assert_matches_type(str, drift_history, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, drift_history, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.drift_history.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = response.parse()
        assert_matches_type(str, drift_history, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.drift_history.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = response.parse()
            assert_matches_type(str, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.queryhelp()
        assert_matches_type(DriftHistoryQueryhelpResponse, drift_history, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.drift_history.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = response.parse()
        assert_matches_type(DriftHistoryQueryhelpResponse, drift_history, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.drift_history.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = response.parse()
            assert_matches_type(DriftHistoryQueryhelpResponse, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.tuple(
            columns="columns",
        )
        assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        drift_history = client.drift_history.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.drift_history.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = response.parse()
        assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.drift_history.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = response.parse()
            assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDriftHistory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.retrieve(
            id="id",
        )
        assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.drift_history.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = await response.parse()
        assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.drift_history.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = await response.parse()
            assert_matches_type(DriftHistoryFull, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.drift_history.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.list()
        assert_matches_type(AsyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.drift_history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = await response.parse()
        assert_matches_type(AsyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.drift_history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = await response.parse()
            assert_matches_type(AsyncOffsetPage[DriftHistoryAbridged], drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.count()
        assert_matches_type(str, drift_history, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, drift_history, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.drift_history.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = await response.parse()
        assert_matches_type(str, drift_history, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.drift_history.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = await response.parse()
            assert_matches_type(str, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.queryhelp()
        assert_matches_type(DriftHistoryQueryhelpResponse, drift_history, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.drift_history.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = await response.parse()
        assert_matches_type(DriftHistoryQueryhelpResponse, drift_history, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.drift_history.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = await response.parse()
            assert_matches_type(DriftHistoryQueryhelpResponse, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.tuple(
            columns="columns",
        )
        assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        drift_history = await async_client.drift_history.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.drift_history.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drift_history = await response.parse()
        assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.drift_history.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drift_history = await response.parse()
            assert_matches_type(DriftHistoryTupleResponse, drift_history, path=["response"])

        assert cast(Any, response.is_closed) is True
