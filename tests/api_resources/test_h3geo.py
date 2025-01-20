# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestH3geo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        h3geo = client.h3geo.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert h3geo is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        h3geo = client.h3geo.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "id": "id",
                    "alt_mean": 0,
                    "alt_sigma": 0,
                    "anom_score_interference": 0,
                    "anom_score_spoofing": 0,
                    "coverage": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "id_h3_geo": "idH3Geo",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "rpm_max": 0,
                    "rpm_mean": 0,
                    "rpm_median": 0,
                    "rpm_min": 0,
                    "rpm_sigma": 0,
                    "source_dl": "sourceDL",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            center_freq=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            origin="origin",
            orig_network="origNetwork",
            resolution=0,
            source_dl="sourceDL",
            tags=["string"],
            type="type",
        )
        assert h3geo is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.h3geo.with_raw_response.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geo = response.parse()
        assert h3geo is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.h3geo.with_streaming_response.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geo = response.parse()
            assert h3geo is None

        assert cast(Any, response.is_closed) is True


class TestAsyncH3geo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3geo = await async_client.h3geo.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert h3geo is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3geo = await async_client.h3geo.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                    "id": "id",
                    "alt_mean": 0,
                    "alt_sigma": 0,
                    "anom_score_interference": 0,
                    "anom_score_spoofing": 0,
                    "coverage": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "id_h3_geo": "idH3Geo",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "rpm_max": 0,
                    "rpm_mean": 0,
                    "rpm_median": 0,
                    "rpm_min": 0,
                    "rpm_sigma": 0,
                    "source_dl": "sourceDL",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            id="id",
            center_freq=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            origin="origin",
            orig_network="origNetwork",
            resolution=0,
            source_dl="sourceDL",
            tags=["string"],
            type="type",
        )
        assert h3geo is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3geo.with_raw_response.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3geo = await response.parse()
        assert h3geo is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3geo.with_streaming_response.create(
            cells=[
                {
                    "cell_id": "cellId",
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "source": "source",
                }
            ],
            classification_marking="classificationMarking",
            data_mode="dataMode",
            num_cells=0,
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3geo = await response.parse()
            assert h3geo is None

        assert cast(Any, response.is_closed) is True
