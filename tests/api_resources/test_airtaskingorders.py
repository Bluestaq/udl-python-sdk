# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import AirtaskingorderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirtaskingorders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airtaskingorder = client.airtaskingorders.list()
        assert_matches_type(AirtaskingorderListResponse, airtaskingorder, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airtaskingorders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airtaskingorder = response.parse()
        assert_matches_type(AirtaskingorderListResponse, airtaskingorder, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airtaskingorders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airtaskingorder = response.parse()
            assert_matches_type(AirtaskingorderListResponse, airtaskingorder, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirtaskingorders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airtaskingorder = await async_client.airtaskingorders.list()
        assert_matches_type(AirtaskingorderListResponse, airtaskingorder, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airtaskingorders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airtaskingorder = await response.parse()
        assert_matches_type(AirtaskingorderListResponse, airtaskingorder, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airtaskingorders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airtaskingorder = await response.parse()
            assert_matches_type(AirtaskingorderListResponse, airtaskingorder, path=["response"])

        assert cast(Any, response.is_closed) is True
