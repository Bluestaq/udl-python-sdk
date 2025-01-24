# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.scs import FileListNonrecursiveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_nonrecursive(self, client: Unifieddatalibrary) -> None:
        file = client.scs.files.list_nonrecursive(
            path="path",
        )
        assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

    @parametrize
    def test_method_list_nonrecursive_with_all_params(self, client: Unifieddatalibrary) -> None:
        file = client.scs.files.list_nonrecursive(
            path="path",
            count=0,
            offset=0,
        )
        assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list_nonrecursive(self, client: Unifieddatalibrary) -> None:
        response = client.scs.files.with_raw_response.list_nonrecursive(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list_nonrecursive(self, client: Unifieddatalibrary) -> None:
        with client.scs.files.with_streaming_response.list_nonrecursive(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_nonrecursive(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.files.list_nonrecursive(
            path="path",
        )
        assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

    @parametrize
    async def test_method_list_nonrecursive_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        file = await async_client.scs.files.list_nonrecursive(
            path="path",
            count=0,
            offset=0,
        )
        assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list_nonrecursive(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.files.with_raw_response.list_nonrecursive(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list_nonrecursive(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.files.with_streaming_response.list_nonrecursive(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListNonrecursiveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
