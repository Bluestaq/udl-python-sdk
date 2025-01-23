# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlSgi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_sgi = client.udl_sgi.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "effective_date": "2018-01-01T16:00:00.123Z",
                    "sgi_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sgi is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.udl_sgi.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "effective_date": "2018-01-01T16:00:00.123Z",
                    "sgi_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sgi = response.parse()
        assert udl_sgi is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.udl_sgi.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "effective_date": "2018-01-01T16:00:00.123Z",
                    "sgi_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sgi = response.parse()
            assert udl_sgi is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlSgi:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_sgi = await async_client.udl_sgi.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "effective_date": "2018-01-01T16:00:00.123Z",
                    "sgi_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sgi is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.udl_sgi.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "effective_date": "2018-01-01T16:00:00.123Z",
                    "sgi_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sgi = await response.parse()
        assert udl_sgi is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.udl_sgi.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "effective_date": "2018-01-01T16:00:00.123Z",
                    "sgi_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sgi = await response.parse()
            assert udl_sgi is None

        assert cast(Any, response.is_closed) is True
