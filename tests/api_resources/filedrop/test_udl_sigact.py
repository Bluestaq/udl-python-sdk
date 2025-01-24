# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlSigact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_sigact = client.filedrop.udl_sigact.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sigact is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.udl_sigact.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sigact = response.parse()
        assert udl_sigact is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.udl_sigact.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sigact = response.parse()
            assert udl_sigact is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlSigact:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_sigact = await async_client.filedrop.udl_sigact.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert udl_sigact is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.udl_sigact.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sigact = await response.parse()
        assert udl_sigact is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.udl_sigact.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "report_date": "2018-01-01T16:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sigact = await response.parse()
            assert udl_sigact is None

        assert cast(Any, response.is_closed) is True
