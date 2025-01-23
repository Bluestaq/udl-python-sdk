# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManeuvers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_start_time": "2023-11-16T01:05:16.835689Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert maneuver is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_start_time": "2023-11-16T01:05:16.835689Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert maneuver is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_start_time": "2023-11-16T01:05:16.835689Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True


class TestAsyncManeuvers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_start_time": "2023-11-16T01:05:16.835689Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert maneuver is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_start_time": "2023-11-16T01:05:16.835689Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert maneuver is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_start_time": "2023-11-16T01:05:16.835689Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True
