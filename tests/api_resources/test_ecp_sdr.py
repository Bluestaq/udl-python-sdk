# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEcpSdr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        ecp_sdr = client.ecp_sdr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )
        assert ecp_sdr is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.ecp_sdr.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecp_sdr = response.parse()
        assert ecp_sdr is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.ecp_sdr.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecp_sdr = response.parse()
            assert ecp_sdr is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEcpSdr:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecp_sdr = await async_client.ecp_sdr.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )
        assert ecp_sdr is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecp_sdr.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecp_sdr = await response.parse()
        assert ecp_sdr is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecp_sdr.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2018-01-01T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "STANDARD",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecp_sdr = await response.parse()
            assert ecp_sdr is None

        assert cast(Any, response.is_closed) is True
