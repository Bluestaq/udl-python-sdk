# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSurfaceobstructions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        surfaceobstruction = client.filedrop.surfaceobstructions.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "id_surface": "be831d39-1822-da9f-7ace-6cc5643397dc",
                    "source": "Bluestaq",
                }
            ],
        )
        assert surfaceobstruction is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.surfaceobstructions.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "id_surface": "be831d39-1822-da9f-7ace-6cc5643397dc",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surfaceobstruction = response.parse()
        assert surfaceobstruction is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.surfaceobstructions.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "id_surface": "be831d39-1822-da9f-7ace-6cc5643397dc",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surfaceobstruction = response.parse()
            assert surfaceobstruction is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSurfaceobstructions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        surfaceobstruction = await async_client.filedrop.surfaceobstructions.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "id_surface": "be831d39-1822-da9f-7ace-6cc5643397dc",
                    "source": "Bluestaq",
                }
            ],
        )
        assert surfaceobstruction is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.surfaceobstructions.with_raw_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "id_surface": "be831d39-1822-da9f-7ace-6cc5643397dc",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        surfaceobstruction = await response.parse()
        assert surfaceobstruction is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.surfaceobstructions.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "id_surface": "be831d39-1822-da9f-7ace-6cc5643397dc",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            surfaceobstruction = await response.parse()
            assert surfaceobstruction is None

        assert cast(Any, response.is_closed) is True
