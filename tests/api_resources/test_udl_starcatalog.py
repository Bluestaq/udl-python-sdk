# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlStarcatalog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_starcatalog = client.udl_starcatalog.create(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "REAL",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )
        assert udl_starcatalog is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.udl_starcatalog.with_raw_response.create(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "REAL",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_starcatalog = response.parse()
        assert udl_starcatalog is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.udl_starcatalog.with_streaming_response.create(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "REAL",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_starcatalog = response.parse()
            assert udl_starcatalog is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlStarcatalog:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_starcatalog = await async_client.udl_starcatalog.create(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "REAL",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )
        assert udl_starcatalog is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.udl_starcatalog.with_raw_response.create(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "REAL",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_starcatalog = await response.parse()
        assert udl_starcatalog is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.udl_starcatalog.with_streaming_response.create(
            body=[
                {
                    "astrometry_origin": "GAIADR3",
                    "classification_marking": "U",
                    "cs_id": 12345,
                    "data_mode": "REAL",
                    "dec": 21.8,
                    "ra": 14.43,
                    "source": "Bluestaq",
                    "star_epoch": 2016,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_starcatalog = await response.parse()
            assert udl_starcatalog is None

        assert cast(Any, response.is_closed) is True
