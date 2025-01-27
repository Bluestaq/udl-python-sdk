# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaunchEvent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_file_create(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "msg_create_date": "2020-01-01T00:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert launch_event is None

    @parametrize
    def test_raw_response_file_create(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "msg_create_date": "2020-01-01T00:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert launch_event is None

    @parametrize
    def test_streaming_response_file_create(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "msg_create_date": "2020-01-01T00:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLaunchEvent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "msg_create_date": "2020-01-01T00:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )
        assert launch_event is None

    @parametrize
    async def test_raw_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "msg_create_date": "2020-01-01T00:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert launch_event is None

    @parametrize
    async def test_streaming_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "msg_create_date": "2020-01-01T00:00:00.123Z",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True
