# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlSar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_sar = client.udl_sar.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "collection_end": "2019-12-27T18:11:19.117Z",
                    "collection_start": "2019-12-27T18:11:19.117Z",
                    "data_mode": "dataMode",
                    "sar_mode": "sarMode",
                    "source": "source",
                }
            ],
        )
        assert udl_sar is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.udl_sar.with_raw_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "collection_end": "2019-12-27T18:11:19.117Z",
                    "collection_start": "2019-12-27T18:11:19.117Z",
                    "data_mode": "dataMode",
                    "sar_mode": "sarMode",
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sar = response.parse()
        assert udl_sar is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.udl_sar.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "collection_end": "2019-12-27T18:11:19.117Z",
                    "collection_start": "2019-12-27T18:11:19.117Z",
                    "data_mode": "dataMode",
                    "sar_mode": "sarMode",
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sar = response.parse()
            assert udl_sar is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlSar:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_sar = await async_client.udl_sar.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "collection_end": "2019-12-27T18:11:19.117Z",
                    "collection_start": "2019-12-27T18:11:19.117Z",
                    "data_mode": "dataMode",
                    "sar_mode": "sarMode",
                    "source": "source",
                }
            ],
        )
        assert udl_sar is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.udl_sar.with_raw_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "collection_end": "2019-12-27T18:11:19.117Z",
                    "collection_start": "2019-12-27T18:11:19.117Z",
                    "data_mode": "dataMode",
                    "sar_mode": "sarMode",
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_sar = await response.parse()
        assert udl_sar is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.udl_sar.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "collection_end": "2019-12-27T18:11:19.117Z",
                    "collection_start": "2019-12-27T18:11:19.117Z",
                    "data_mode": "dataMode",
                    "sar_mode": "sarMode",
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_sar = await response.parse()
            assert udl_sar is None

        assert cast(Any, response.is_closed) is True
