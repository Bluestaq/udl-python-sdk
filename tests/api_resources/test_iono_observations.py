# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIonoObservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        iono_observation = client.iono_observations.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "start_time_utc": "2021-01-01T01:01:01.123456Z",
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )
        assert iono_observation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.iono_observations.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "start_time_utc": "2021-01-01T01:01:01.123456Z",
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iono_observation = response.parse()
        assert iono_observation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.iono_observations.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "start_time_utc": "2021-01-01T01:01:01.123456Z",
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iono_observation = response.parse()
            assert iono_observation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncIonoObservations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        iono_observation = await async_client.iono_observations.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "start_time_utc": "2021-01-01T01:01:01.123456Z",
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )
        assert iono_observation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.iono_observations.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "start_time_utc": "2021-01-01T01:01:01.123456Z",
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iono_observation = await response.parse()
        assert iono_observation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.iono_observations.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "start_time_utc": "2021-01-01T01:01:01.123456Z",
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iono_observation = await response.parse()
            assert iono_observation is None

        assert cast(Any, response.is_closed) is True
