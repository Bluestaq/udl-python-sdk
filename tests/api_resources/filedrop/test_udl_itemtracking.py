# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlItemtracking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_itemtracking = client.filedrop.udl_itemtracking.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )
        assert udl_itemtracking is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.udl_itemtracking.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_itemtracking = response.parse()
        assert udl_itemtracking is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.udl_itemtracking.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_itemtracking = response.parse()
            assert udl_itemtracking is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlItemtracking:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_itemtracking = await async_client.filedrop.udl_itemtracking.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )
        assert udl_itemtracking is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.udl_itemtracking.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_itemtracking = await response.parse()
        assert udl_itemtracking is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.udl_itemtracking.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_itemtracking = await response.parse()
            assert udl_itemtracking is None

        assert cast(Any, response.is_closed) is True
