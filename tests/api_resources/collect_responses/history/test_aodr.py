# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAodr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        aodr = client.collect_responses.history.aodr.list(
            created_at=parse_date("2019-12-27"),
        )
        assert aodr is None

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        aodr = client.collect_responses.history.aodr.list(
            created_at=parse_date("2019-12-27"),
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert aodr is None

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.collect_responses.history.aodr.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aodr = response.parse()
        assert aodr is None

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.collect_responses.history.aodr.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aodr = response.parse()
            assert aodr is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAodr:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        aodr = await async_client.collect_responses.history.aodr.list(
            created_at=parse_date("2019-12-27"),
        )
        assert aodr is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        aodr = await async_client.collect_responses.history.aodr.list(
            created_at=parse_date("2019-12-27"),
            columns="columns",
            first_result=0,
            max_results=0,
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert aodr is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_responses.history.aodr.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aodr = await response.parse()
        assert aodr is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_responses.history.aodr.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aodr = await response.parse()
            assert aodr is None

        assert cast(Any, response.is_closed) is True
