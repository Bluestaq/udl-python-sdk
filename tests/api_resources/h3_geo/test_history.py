# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.h3_geo import (
    HistoryQueryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ador(self, client: Unifieddatalibrary) -> None:
        history = client.h3_geo.history.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert history is None

    @parametrize
    def test_method_ador_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.h3_geo.history.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert history is None

    @parametrize
    def test_raw_response_ador(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.history.with_raw_response.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert history is None

    @parametrize
    def test_streaming_response_ador(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.history.with_streaming_response.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        history = client.h3_geo.history.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.h3_geo.history.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.history.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.history.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(str, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        history = client.h3_geo.history.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.h3_geo.history.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.history.with_raw_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.history.with_streaming_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryQueryResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_ador(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.h3_geo.history.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert history is None

    @parametrize
    async def test_method_ador_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.h3_geo.history.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert history is None

    @parametrize
    async def test_raw_response_ador(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.history.with_raw_response.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert history is None

    @parametrize
    async def test_streaming_response_ador(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.history.with_streaming_response.ador(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.h3_geo.history.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.h3_geo.history.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.history.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.history.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(str, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.h3_geo.history.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.h3_geo.history.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.history.with_raw_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryQueryResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.history.with_streaming_response.query(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryQueryResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True
