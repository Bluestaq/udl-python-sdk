# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import UserAuthResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_auth(self, client: Unifieddatalibrary) -> None:
        user = client.user.auth()
        assert_matches_type(UserAuthResponse, user, path=["response"])

    @parametrize
    def test_raw_response_auth(self, client: Unifieddatalibrary) -> None:
        response = client.user.with_raw_response.auth()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserAuthResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_auth(self, client: Unifieddatalibrary) -> None:
        with client.user.with_streaming_response.auth() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserAuthResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_auth(self, async_client: AsyncUnifieddatalibrary) -> None:
        user = await async_client.user.auth()
        assert_matches_type(UserAuthResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_auth(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.user.with_raw_response.auth()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserAuthResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_auth(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.user.with_streaming_response.auth() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserAuthResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
