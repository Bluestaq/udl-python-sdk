# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEcpsdr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ecpsdr = client.ecpsdr.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "msg_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )
        assert ecpsdr is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.ecpsdr.with_raw_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "msg_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = response.parse()
        assert ecpsdr is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.ecpsdr.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "msg_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEcpsdr:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ecpsdr = await async_client.ecpsdr.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "msg_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )
        assert ecpsdr is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ecpsdr.with_raw_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "msg_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ecpsdr = await response.parse()
        assert ecpsdr is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ecpsdr.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "msg_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ecpsdr = await response.parse()
            assert ecpsdr is None

        assert cast(Any, response.is_closed) is True
