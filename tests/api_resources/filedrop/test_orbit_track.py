# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrbitTrack:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        orbit_track = client.filedrop.orbit_track.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )
        assert orbit_track is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.orbit_track.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbit_track = response.parse()
        assert orbit_track is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.orbit_track.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbit_track = response.parse()
            assert orbit_track is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOrbitTrack:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbit_track = await async_client.filedrop.orbit_track.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )
        assert orbit_track is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.orbit_track.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbit_track = await response.parse()
        assert orbit_track is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.orbit_track.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbit_track = await response.parse()
            assert orbit_track is None

        assert cast(Any, response.is_closed) is True
