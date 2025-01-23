# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeatherData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        weather_data = client.filedrop.weather_data.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "ob_time": "2018-01-01T16:00:00.123456Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert weather_data is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.weather_data.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "ob_time": "2018-01-01T16:00:00.123456Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weather_data = response.parse()
        assert weather_data is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.weather_data.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "ob_time": "2018-01-01T16:00:00.123456Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weather_data = response.parse()
            assert weather_data is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWeatherData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        weather_data = await async_client.filedrop.weather_data.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "ob_time": "2018-01-01T16:00:00.123456Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert weather_data is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.weather_data.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "ob_time": "2018-01-01T16:00:00.123456Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        weather_data = await response.parse()
        assert weather_data is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.weather_data.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "ob_time": "2018-01-01T16:00:00.123456Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            weather_data = await response.parse()
            assert weather_data is None

        assert cast(Any, response.is_closed) is True
