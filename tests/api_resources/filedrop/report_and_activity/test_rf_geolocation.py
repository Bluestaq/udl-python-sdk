# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRfGeolocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        rf_geolocation = client.filedrop.report_and_activity.rf_geolocation.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )
        assert rf_geolocation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.report_and_activity.rf_geolocation.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_geolocation = response.parse()
        assert rf_geolocation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.report_and_activity.rf_geolocation.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_geolocation = response.parse()
            assert rf_geolocation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRfGeolocation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        rf_geolocation = await async_client.filedrop.report_and_activity.rf_geolocation.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )
        assert rf_geolocation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.report_and_activity.rf_geolocation.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rf_geolocation = await response.parse()
        assert rf_geolocation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.report_and_activity.rf_geolocation.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "order_id": "155240",
                    "received_ts": "2024-05-31T21:16:58.123456Z",
                    "source": "Bluestaq",
                    "start_time": "2024-05-31T21:12:12.123456Z",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rf_geolocation = await response.parse()
            assert rf_geolocation is None

        assert cast(Any, response.is_closed) is True
