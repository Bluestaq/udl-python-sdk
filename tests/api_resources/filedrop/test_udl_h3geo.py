# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUdlH3geo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        udl_h3geo = client.filedrop.udl_h3geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )
        assert udl_h3geo is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        udl_h3geo = client.filedrop.udl_h3geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "id": "443fg911-4ab6-3d74-1991-372149d87f89",
                    "alt_mean": 450.1,
                    "alt_sigma": 400.1,
                    "anom_score_interference": 0.125,
                    "anom_score_spoofing": 0.125,
                    "coverage": 8,
                    "created_at": "2018-01-01T16:00:00.123Z",
                    "created_by": "some.user",
                    "id_h3_geo": "026dd511-8ba5-47d3-9909-836149f87686",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_network": "OPS1",
                    "rpm_max": 50.1,
                    "rpm_mean": 47.953125,
                    "rpm_median": 48.375,
                    "rpm_min": 43.1,
                    "rpm_sigma": 1.23,
                    "source_dl": "AXE",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            center_freq=1575.42,
            end_time=parse_datetime("2024-07-03T00:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            resolution=3,
            tags=["TAG1", "TAG2"],
            type="Cell Towers",
        )
        assert udl_h3geo is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.filedrop.udl_h3geo.with_raw_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_h3geo = response.parse()
        assert udl_h3geo is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.filedrop.udl_h3geo.with_streaming_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_h3geo = response.parse()
            assert udl_h3geo is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUdlH3geo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_h3geo = await async_client.filedrop.udl_h3geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )
        assert udl_h3geo is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        udl_h3geo = await async_client.filedrop.udl_h3geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                    "id": "443fg911-4ab6-3d74-1991-372149d87f89",
                    "alt_mean": 450.1,
                    "alt_sigma": 400.1,
                    "anom_score_interference": 0.125,
                    "anom_score_spoofing": 0.125,
                    "coverage": 8,
                    "created_at": "2018-01-01T16:00:00.123Z",
                    "created_by": "some.user",
                    "id_h3_geo": "026dd511-8ba5-47d3-9909-836149f87686",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_network": "OPS1",
                    "rpm_max": 50.1,
                    "rpm_mean": 47.953125,
                    "rpm_median": 48.375,
                    "rpm_min": 43.1,
                    "rpm_sigma": 1.23,
                    "source_dl": "AXE",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            center_freq=1575.42,
            end_time=parse_datetime("2024-07-03T00:00:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            resolution=3,
            tags=["TAG1", "TAG2"],
            type="Cell Towers",
        )
        assert udl_h3geo is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.filedrop.udl_h3geo.with_raw_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        udl_h3geo = await response.parse()
        assert udl_h3geo is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.filedrop.udl_h3geo.with_streaming_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "REAL",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="REAL",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            udl_h3geo = await response.parse()
            assert udl_h3geo is None

        assert cast(Any, response.is_closed) is True
