# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGnssRawIf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_history_aodr(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert gnss_raw_if is None

    @parametrize
    def test_method_history_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert gnss_raw_if is None

    @parametrize
    def test_raw_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_raw_if.with_raw_response.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = response.parse()
        assert gnss_raw_if is None

    @parametrize
    def test_streaming_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        with client.gnss_raw_if.with_streaming_response.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = response.parse()
            assert gnss_raw_if is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGnssRawIf:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert gnss_raw_if is None

    @parametrize
    async def test_method_history_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert gnss_raw_if is None

    @parametrize
    async def test_raw_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_raw_if.with_raw_response.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = await response.parse()
        assert gnss_raw_if is None

    @parametrize
    async def test_streaming_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_raw_if.with_streaming_response.history_aodr(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = await response.parse()
            assert gnss_raw_if is None

        assert cast(Any, response.is_closed) is True
