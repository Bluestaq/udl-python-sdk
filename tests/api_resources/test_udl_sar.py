# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlSar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_sar = client.udl_sar.create(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": "2023-04-22T17:38:10.20177Z",
                    "collection_start": "2023-04-22T17:35:00.123456Z",
                    "data_mode": "REAL",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sar is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.udl_sar.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": "2023-04-22T17:38:10.20177Z",
                    "collection_start": "2023-04-22T17:35:00.123456Z",
                    "data_mode": "REAL",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sar = response.parse()
        assert udl_sar is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.udl_sar.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": "2023-04-22T17:38:10.20177Z",
                    "collection_start": "2023-04-22T17:35:00.123456Z",
                    "data_mode": "REAL",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sar = response.parse()
            assert udl_sar is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlSar:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_sar = await async_client.udl_sar.create(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": "2023-04-22T17:38:10.20177Z",
                    "collection_start": "2023-04-22T17:35:00.123456Z",
                    "data_mode": "REAL",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sar is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.udl_sar.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": "2023-04-22T17:38:10.20177Z",
                    "collection_start": "2023-04-22T17:35:00.123456Z",
                    "data_mode": "REAL",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sar = await response.parse()
        assert udl_sar is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.udl_sar.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "collection_end": "2023-04-22T17:38:10.20177Z",
                    "collection_start": "2023-04-22T17:35:00.123456Z",
                    "data_mode": "REAL",
                    "sar_mode": "SPOTLIGHT",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sar = await response.parse()
            assert udl_sar is None

        assert cast(Any, response.is_closed) is True
