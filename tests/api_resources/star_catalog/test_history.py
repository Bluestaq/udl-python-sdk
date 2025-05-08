# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_aodr(self, client: Unifieddatalibrary) -> None:
        history = client.star_catalog.history.aodr()
        assert history is None

    @parametrize
    def test_method_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        history = client.star_catalog.history.aodr(
            columns="columns",
            dec=0,
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
            ra=0,
        )
        assert history is None

    @parametrize
    def test_raw_response_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.star_catalog.history.with_raw_response.aodr()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert history is None

    @parametrize
    def test_streaming_response_aodr(self, client: Unifieddatalibrary) -> None:
        with client.star_catalog.history.with_streaming_response.aodr() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.star_catalog.history.aodr()
        assert history is None

    @parametrize
    async def test_method_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        history = await async_client.star_catalog.history.aodr(
            columns="columns",
            dec=0,
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
            ra=0,
        )
        assert history is None

    @parametrize
    async def test_raw_response_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.star_catalog.history.with_raw_response.aodr()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert history is None

    @parametrize
    async def test_streaming_response_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.star_catalog.history.with_streaming_response.aodr() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert history is None

        assert cast(Any, response.is_closed) is True
