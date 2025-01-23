# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventevolutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        eventevolution = client.filedrop.eventevolutions.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": "2021-12-02T16:00:00.123Z",
                    "summary": "Example summary of the event.",
                }
            ],
        )
        assert eventevolution is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.eventevolutions.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": "2021-12-02T16:00:00.123Z",
                    "summary": "Example summary of the event.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eventevolution = response.parse()
        assert eventevolution is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.eventevolutions.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": "2021-12-02T16:00:00.123Z",
                    "summary": "Example summary of the event.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eventevolution = response.parse()
            assert eventevolution is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEventevolutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        eventevolution = await async_client.filedrop.eventevolutions.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": "2021-12-02T16:00:00.123Z",
                    "summary": "Example summary of the event.",
                }
            ],
        )
        assert eventevolution is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.eventevolutions.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": "2021-12-02T16:00:00.123Z",
                    "summary": "Example summary of the event.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eventevolution = await response.parse()
        assert eventevolution is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.eventevolutions.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": "2021-12-02T16:00:00.123Z",
                    "summary": "Example summary of the event.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eventevolution = await response.parse()
            assert eventevolution is None

        assert cast(Any, response.is_closed) is True
