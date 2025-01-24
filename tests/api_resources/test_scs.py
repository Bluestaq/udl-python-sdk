# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ScSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_move(self, client: Unifieddatalibrary) -> None:
        sc = client.scs.move(
            target_path="targetPath",
        )
        assert_matches_type(str, sc, path=["response"])

    @parametrize
    def test_raw_response_move(self, client: Unifieddatalibrary) -> None:
        response = client.scs.with_raw_response.move(
            target_path="targetPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = response.parse()
        assert_matches_type(str, sc, path=["response"])

    @parametrize
    def test_streaming_response_move(self, client: Unifieddatalibrary) -> None:
        with client.scs.with_streaming_response.move(
            target_path="targetPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = response.parse()
            assert_matches_type(str, sc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rename(self, client: Unifieddatalibrary) -> None:
        sc = client.scs.rename(
            new_name="newName",
        )
        assert sc is None

    @parametrize
    def test_raw_response_rename(self, client: Unifieddatalibrary) -> None:
        response = client.scs.with_raw_response.rename(
            new_name="newName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = response.parse()
        assert sc is None

    @parametrize
    def test_streaming_response_rename(self, client: Unifieddatalibrary) -> None:
        with client.scs.with_streaming_response.rename(
            new_name="newName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = response.parse()
            assert sc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Unifieddatalibrary) -> None:
        sc = client.scs.search(
            path="path",
        )
        assert_matches_type(ScSearchResponse, sc, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Unifieddatalibrary) -> None:
        sc = client.scs.search(
            path="path",
            count=0,
            offset=0,
            content_criteria="contentCriteria",
            meta_data_criteria={"CREATED_AT": ["< 2022-06-14T07:48:11.302Z"]},
            non_range_criteria={"foo": ["string"]},
            range_criteria={"foo": ["string"]},
            search_after="searchAfter",
        )
        assert_matches_type(ScSearchResponse, sc, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Unifieddatalibrary) -> None:
        response = client.scs.with_raw_response.search(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = response.parse()
        assert_matches_type(ScSearchResponse, sc, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Unifieddatalibrary) -> None:
        with client.scs.with_streaming_response.search(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = response.parse()
            assert_matches_type(ScSearchResponse, sc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_tags(self, client: Unifieddatalibrary) -> None:
        sc = client.scs.update_tags(
            folder="folder",
            tags="tags",
        )
        assert sc is None

    @parametrize
    def test_raw_response_update_tags(self, client: Unifieddatalibrary) -> None:
        response = client.scs.with_raw_response.update_tags(
            folder="folder",
            tags="tags",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = response.parse()
        assert sc is None

    @parametrize
    def test_streaming_response_update_tags(self, client: Unifieddatalibrary) -> None:
        with client.scs.with_streaming_response.update_tags(
            folder="folder",
            tags="tags",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = response.parse()
            assert sc is None

        assert cast(Any, response.is_closed) is True


class TestAsyncScs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_move(self, async_client: AsyncUnifieddatalibrary) -> None:
        sc = await async_client.scs.move(
            target_path="targetPath",
        )
        assert_matches_type(str, sc, path=["response"])

    @parametrize
    async def test_raw_response_move(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.with_raw_response.move(
            target_path="targetPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = await response.parse()
        assert_matches_type(str, sc, path=["response"])

    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.with_streaming_response.move(
            target_path="targetPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = await response.parse()
            assert_matches_type(str, sc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rename(self, async_client: AsyncUnifieddatalibrary) -> None:
        sc = await async_client.scs.rename(
            new_name="newName",
        )
        assert sc is None

    @parametrize
    async def test_raw_response_rename(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.with_raw_response.rename(
            new_name="newName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = await response.parse()
        assert sc is None

    @parametrize
    async def test_streaming_response_rename(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.with_streaming_response.rename(
            new_name="newName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = await response.parse()
            assert sc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncUnifieddatalibrary) -> None:
        sc = await async_client.scs.search(
            path="path",
        )
        assert_matches_type(ScSearchResponse, sc, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sc = await async_client.scs.search(
            path="path",
            count=0,
            offset=0,
            content_criteria="contentCriteria",
            meta_data_criteria={"CREATED_AT": ["< 2022-06-14T07:48:11.302Z"]},
            non_range_criteria={"foo": ["string"]},
            range_criteria={"foo": ["string"]},
            search_after="searchAfter",
        )
        assert_matches_type(ScSearchResponse, sc, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.with_raw_response.search(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = await response.parse()
        assert_matches_type(ScSearchResponse, sc, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.with_streaming_response.search(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = await response.parse()
            assert_matches_type(ScSearchResponse, sc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_tags(self, async_client: AsyncUnifieddatalibrary) -> None:
        sc = await async_client.scs.update_tags(
            folder="folder",
            tags="tags",
        )
        assert sc is None

    @parametrize
    async def test_raw_response_update_tags(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.with_raw_response.update_tags(
            folder="folder",
            tags="tags",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sc = await response.parse()
        assert sc is None

    @parametrize
    async def test_streaming_response_update_tags(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.with_streaming_response.update_tags(
            folder="folder",
            tags="tags",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sc = await response.parse()
            assert sc is None

        assert cast(Any, response.is_closed) is True
