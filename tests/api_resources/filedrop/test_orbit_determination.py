# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrbitDetermination:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        orbit_determination = client.filedrop.orbit_determination.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "end_time": "2023-08-28T15:20:21.247192Z",
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": "2023-08-28T11:20:21.247192Z",
                }
            ],
        )
        assert orbit_determination is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.orbit_determination.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "end_time": "2023-08-28T15:20:21.247192Z",
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": "2023-08-28T11:20:21.247192Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbit_determination = response.parse()
        assert orbit_determination is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.orbit_determination.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "end_time": "2023-08-28T15:20:21.247192Z",
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": "2023-08-28T11:20:21.247192Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbit_determination = response.parse()
            assert orbit_determination is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOrbitDetermination:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbit_determination = await async_client.filedrop.orbit_determination.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "end_time": "2023-08-28T15:20:21.247192Z",
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": "2023-08-28T11:20:21.247192Z",
                }
            ],
        )
        assert orbit_determination is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.orbit_determination.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "end_time": "2023-08-28T15:20:21.247192Z",
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": "2023-08-28T11:20:21.247192Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbit_determination = await response.parse()
        assert orbit_determination is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.orbit_determination.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "end_time": "2023-08-28T15:20:21.247192Z",
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": "2023-08-28T11:20:21.247192Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbit_determination = await response.parse()
            assert orbit_determination is None

        assert cast(Any, response.is_closed) is True
