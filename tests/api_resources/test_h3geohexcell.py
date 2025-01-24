# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    H3geohexcellListResponse,
    H3geohexcellTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestH3geohexcell:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        h3geohexcell = client.h3geohexcell.list(
            id_h3_geo="idH3Geo",
        )
        assert_matches_type(H3geohexcellListResponse, h3geohexcell, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.h3geohexcell.with_raw_response.list(
            id_h3_geo="idH3Geo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = response.parse()
        assert_matches_type(H3geohexcellListResponse, h3geohexcell, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.h3geohexcell.with_streaming_response.list(
            id_h3_geo="idH3Geo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = response.parse()
            assert_matches_type(H3geohexcellListResponse, h3geohexcell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        h3geohexcell = client.h3geohexcell.count(
            id_h3_geo="idH3Geo",
        )
        assert_matches_type(str, h3geohexcell, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.h3geohexcell.with_raw_response.count(
            id_h3_geo="idH3Geo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = response.parse()
        assert_matches_type(str, h3geohexcell, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.h3geohexcell.with_streaming_response.count(
            id_h3_geo="idH3Geo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = response.parse()
            assert_matches_type(str, h3geohexcell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        h3geohexcell = client.h3geohexcell.queryhelp()
        assert h3geohexcell is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.h3geohexcell.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = response.parse()
        assert h3geohexcell is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.h3geohexcell.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = response.parse()
            assert h3geohexcell is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        h3geohexcell = client.h3geohexcell.tuple(
            columns="columns",
            id_h3_geo="idH3Geo",
        )
        assert_matches_type(H3geohexcellTupleResponse, h3geohexcell, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.h3geohexcell.with_raw_response.tuple(
            columns="columns",
            id_h3_geo="idH3Geo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = response.parse()
        assert_matches_type(H3geohexcellTupleResponse, h3geohexcell, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.h3geohexcell.with_streaming_response.tuple(
            columns="columns",
            id_h3_geo="idH3Geo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = response.parse()
            assert_matches_type(H3geohexcellTupleResponse, h3geohexcell, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncH3geohexcell:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3geohexcell = await async_client.h3geohexcell.list(
            id_h3_geo="idH3Geo",
        )
        assert_matches_type(H3geohexcellListResponse, h3geohexcell, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3geohexcell.with_raw_response.list(
            id_h3_geo="idH3Geo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = await response.parse()
        assert_matches_type(H3geohexcellListResponse, h3geohexcell, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3geohexcell.with_streaming_response.list(
            id_h3_geo="idH3Geo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = await response.parse()
            assert_matches_type(H3geohexcellListResponse, h3geohexcell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3geohexcell = await async_client.h3geohexcell.count(
            id_h3_geo="idH3Geo",
        )
        assert_matches_type(str, h3geohexcell, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3geohexcell.with_raw_response.count(
            id_h3_geo="idH3Geo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = await response.parse()
        assert_matches_type(str, h3geohexcell, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3geohexcell.with_streaming_response.count(
            id_h3_geo="idH3Geo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = await response.parse()
            assert_matches_type(str, h3geohexcell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3geohexcell = await async_client.h3geohexcell.queryhelp()
        assert h3geohexcell is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3geohexcell.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = await response.parse()
        assert h3geohexcell is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3geohexcell.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = await response.parse()
            assert h3geohexcell is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3geohexcell = await async_client.h3geohexcell.tuple(
            columns="columns",
            id_h3_geo="idH3Geo",
        )
        assert_matches_type(H3geohexcellTupleResponse, h3geohexcell, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3geohexcell.with_raw_response.tuple(
            columns="columns",
            id_h3_geo="idH3Geo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geohexcell = await response.parse()
        assert_matches_type(H3geohexcellTupleResponse, h3geohexcell, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3geohexcell.with_streaming_response.tuple(
            columns="columns",
            id_h3_geo="idH3Geo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geohexcell = await response.parse()
            assert_matches_type(H3geohexcellTupleResponse, h3geohexcell, path=["response"])

        assert cast(Any, response.is_closed) is True
