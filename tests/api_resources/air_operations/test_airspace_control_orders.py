# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirspaceControlOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.air_operations.airspace_control_orders.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )
        assert airspace_control_order is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.airspace_control_orders.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert airspace_control_order is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.airspace_control_orders.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAirspaceControlOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.air_operations.airspace_control_orders.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )
        assert airspace_control_order is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.airspace_control_orders.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert airspace_control_order is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.airspace_control_orders.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True
