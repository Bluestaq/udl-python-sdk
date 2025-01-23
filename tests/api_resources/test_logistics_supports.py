# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogisticsSupports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_supports.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "rpt_created_time": "2023-07-13T13:47:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert logistics_support is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_supports.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "rpt_created_time": "2023-07-13T13:47:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert logistics_support is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.logistics_supports.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "rpt_created_time": "2023-07-13T13:47:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLogisticsSupports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_supports.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "rpt_created_time": "2023-07-13T13:47:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert logistics_support is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_supports.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "rpt_created_time": "2023-07-13T13:47:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert logistics_support is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_supports.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "rpt_created_time": "2023-07-13T13:47:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True
