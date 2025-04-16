# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiplomaticClearance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        diplomatic_clearance = client.air_operations.diplomatic_clearance.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )
        assert diplomatic_clearance is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.diplomatic_clearance.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = response.parse()
        assert diplomatic_clearance is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.diplomatic_clearance.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDiplomaticClearance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        diplomatic_clearance = await async_client.air_operations.diplomatic_clearance.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )
        assert diplomatic_clearance is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.diplomatic_clearance.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diplomatic_clearance = await response.parse()
        assert diplomatic_clearance is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.diplomatic_clearance.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "first_dep_date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "id_mission": "0dba1363-2d09-49fa-a784-4bb4cbb1674a",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diplomatic_clearance = await response.parse()
            assert diplomatic_clearance is None

        assert cast(Any, response.is_closed) is True
