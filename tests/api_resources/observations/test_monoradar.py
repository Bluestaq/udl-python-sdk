# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonoradar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert monoradar is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.observations.monoradar.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = response.parse()
        assert monoradar is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.observations.monoradar.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = response.parse()
            assert monoradar is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMonoradar:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert monoradar is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.monoradar.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = await response.parse()
        assert monoradar is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.monoradar.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = await response.parse()
            assert monoradar is None

        assert cast(Any, response.is_closed) is True
