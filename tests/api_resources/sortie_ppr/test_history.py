# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.sortie_ppr import (
    SortiePprFull,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        history = client.sortie_ppr.history.list(
            id_sortie="idSortie",
        )
        assert_matches_type(SyncOffsetPage[SortiePprFull], history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.sortie_ppr.history.list(
            id_sortie="idSortie",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SortiePprFull], history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.history.with_raw_response.list(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(SyncOffsetPage[SortiePprFull], history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.history.with_streaming_response.list(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(SyncOffsetPage[SortiePprFull], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_aodr(self, client: Unifieddatalibrary) -> None:
        history = client.sortie_ppr.history.aodr(
            id_sortie="idSortie",
        )
        assert history is None

    @parametrize
    def test_method_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.sortie_ppr.history.aodr(
            id_sortie="idSortie",
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
        response = client.sortie_ppr.history.with_raw_response.aodr(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert history is None

    @parametrize
    def test_streaming_response_aodr(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.history.with_streaming_response.aodr(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        history = client.sortie_ppr.history.count(
            id_sortie="idSortie",
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.sortie_ppr.history.count(
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.sortie_ppr.history.with_raw_response.count(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.sortie_ppr.history.with_streaming_response.count(
            id_sortie="idSortie",
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
        history = await async_client.sortie_ppr.history.list(
            id_sortie="idSortie",
        )
        assert_matches_type(AsyncOffsetPage[SortiePprFull], history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.sortie_ppr.history.list(
            id_sortie="idSortie",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SortiePprFull], history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.history.with_raw_response.list(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(AsyncOffsetPage[SortiePprFull], history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.history.with_streaming_response.list(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(AsyncOffsetPage[SortiePprFull], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.sortie_ppr.history.aodr(
            id_sortie="idSortie",
        )
        assert history is None

    @parametrize
    async def test_method_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.sortie_ppr.history.aodr(
            id_sortie="idSortie",
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
        response = await async_client.sortie_ppr.history.with_raw_response.aodr(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert history is None

    @parametrize
    async def test_streaming_response_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.history.with_streaming_response.aodr(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.sortie_ppr.history.count(
            id_sortie="idSortie",
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.sortie_ppr.history.count(
            id_sortie="idSortie",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sortie_ppr.history.with_raw_response.count(
            id_sortie="idSortie",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(str, history, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sortie_ppr.history.with_streaming_response.count(
            id_sortie="idSortie",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(str, history, path=["response"])

        assert cast(Any, response.is_closed) is True
