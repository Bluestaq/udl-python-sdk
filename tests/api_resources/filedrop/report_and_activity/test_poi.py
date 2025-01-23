# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPoi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        poi = client.filedrop.report_and_activity.poi.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert poi is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.report_and_activity.poi.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert poi is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.report_and_activity.poi.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPoi:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.filedrop.report_and_activity.poi.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert poi is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.report_and_activity.poi.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert poi is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.report_and_activity.poi.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True
