# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import EphemerisFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        history = client.ephemeris.history.list(
            es_id="esId",
        )
        assert_matches_type(SyncOffsetPage[EphemerisFull], history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.ephemeris.history.list(
            es_id="esId",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EphemerisFull], history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris.history.with_raw_response.list(
            es_id="esId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(SyncOffsetPage[EphemerisFull], history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris.history.with_streaming_response.list(
            es_id="esId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(SyncOffsetPage[EphemerisFull], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_aodr(self, client: Unifieddatalibrary) -> None:
        history = client.ephemeris.history.aodr(
            es_id="esId",
        )
        assert history is None

    @parametrize
    def test_method_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.ephemeris.history.aodr(
            es_id="esId",
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert history is None

    @parametrize
    def test_raw_response_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris.history.with_raw_response.aodr(
            es_id="esId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert history is None

    @parametrize
    def test_streaming_response_aodr(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris.history.with_streaming_response.aodr(
            es_id="esId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        history = client.ephemeris.history.count(
            es_id="esId",
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.ephemeris.history.count(
            es_id="esId",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris.history.with_raw_response.count(
            es_id="esId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris.history.with_streaming_response.count(
            es_id="esId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(str, history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.ephemeris.history.list(
            es_id="esId",
        )
        assert_matches_type(AsyncOffsetPage[EphemerisFull], history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.ephemeris.history.list(
            es_id="esId",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EphemerisFull], history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris.history.with_raw_response.list(
            es_id="esId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(AsyncOffsetPage[EphemerisFull], history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris.history.with_streaming_response.list(
            es_id="esId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(AsyncOffsetPage[EphemerisFull], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.ephemeris.history.aodr(
            es_id="esId",
        )
        assert history is None

    @parametrize
    async def test_method_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.ephemeris.history.aodr(
            es_id="esId",
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert history is None

    @parametrize
    async def test_raw_response_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris.history.with_raw_response.aodr(
            es_id="esId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert history is None

    @parametrize
    async def test_streaming_response_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris.history.with_streaming_response.aodr(
            es_id="esId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.ephemeris.history.count(
            es_id="esId",
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.ephemeris.history.count(
            es_id="esId",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris.history.with_raw_response.count(
            es_id="esId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris.history.with_streaming_response.count(
            es_id="esId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(str, history, path=["response"])

        assert cast(Any, response.is_closed) is True
