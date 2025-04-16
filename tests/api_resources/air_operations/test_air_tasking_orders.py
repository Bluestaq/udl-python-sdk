# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirTaskingOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )
        assert air_tasking_order is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert air_tasking_order is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAirTaskingOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )
        assert air_tasking_order is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert air_tasking_order is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True
