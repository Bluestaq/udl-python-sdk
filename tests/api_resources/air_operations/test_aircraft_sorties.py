# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAircraftSorties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        aircraft_sorty = client.air_operations.aircraft_sorties.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "planned_dep_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )
        assert aircraft_sorty is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.aircraft_sorties.with_raw_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "planned_dep_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = response.parse()
        assert aircraft_sorty is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.aircraft_sorties.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "planned_dep_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAircraftSorties:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        aircraft_sorty = await async_client.air_operations.aircraft_sorties.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "planned_dep_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )
        assert aircraft_sorty is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.aircraft_sorties.with_raw_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "planned_dep_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aircraft_sorty = await response.parse()
        assert aircraft_sorty is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.aircraft_sorties.with_streaming_response.create(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "planned_dep_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aircraft_sorty = await response.parse()
            assert aircraft_sorty is None

        assert cast(Any, response.is_closed) is True
