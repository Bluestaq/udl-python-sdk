# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    H3GeoGetResponse,
    H3GeoListResponse,
    H3GeoTupleResponse,
    H3GeoQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestH3Geo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="TEST",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )
        assert h3_geo is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "443fg911-4ab6-3d74-1991-372149d87f89",
                    "alt_mean": 450.1,
                    "alt_sigma": 400.1,
                    "anom_score_interference": 0.125,
                    "anom_score_spoofing": 0.125,
                    "change_score": 12.34,
                    "coverage": 8,
                    "id_h3_geo": "026dd511-8ba5-47d3-9909-836149f87686",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "rpm_max": 50.1,
                    "rpm_mean": 47.953125,
                    "rpm_median": 48.375,
                    "rpm_min": 43.1,
                    "rpm_sigma": 1.23,
                }
            ],
            classification_marking="U",
            data_mode="TEST",
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
        assert h3_geo is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.with_raw_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="TEST",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = response.parse()
        assert h3_geo is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.with_streaming_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="TEST",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = response.parse()
            assert h3_geo is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = response.parse()
        assert_matches_type(SyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = response.parse()
            assert_matches_type(SyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, h3_geo, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, h3_geo, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = response.parse()
        assert_matches_type(str, h3_geo, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = response.parse()
            assert_matches_type(str, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.get(
            id="id",
        )
        assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = response.parse()
        assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = response.parse()
            assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.h3_geo.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.queryhelp()
        assert_matches_type(H3GeoQueryhelpResponse, h3_geo, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = response.parse()
        assert_matches_type(H3GeoQueryhelpResponse, h3_geo, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = response.parse()
            assert_matches_type(H3GeoQueryhelpResponse, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        h3_geo = client.h3_geo.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.h3_geo.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = response.parse()
        assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.h3_geo.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = response.parse()
            assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncH3Geo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="TEST",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )
        assert h3_geo is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "443fg911-4ab6-3d74-1991-372149d87f89",
                    "alt_mean": 450.1,
                    "alt_sigma": 400.1,
                    "anom_score_interference": 0.125,
                    "anom_score_spoofing": 0.125,
                    "change_score": 12.34,
                    "coverage": 8,
                    "id_h3_geo": "026dd511-8ba5-47d3-9909-836149f87686",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "rpm_max": 50.1,
                    "rpm_mean": 47.953125,
                    "rpm_median": 48.375,
                    "rpm_min": 43.1,
                    "rpm_sigma": 1.23,
                }
            ],
            classification_marking="U",
            data_mode="TEST",
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
        assert h3_geo is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.with_raw_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="TEST",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = await response.parse()
        assert h3_geo is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.with_streaming_response.create(
            cells=[
                {
                    "cell_id": "830b90fffffffff",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
            classification_marking="U",
            data_mode="TEST",
            num_cells=1,
            source="Bluestaq",
            start_time=parse_datetime("2024-07-02T00:00:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = await response.parse()
            assert h3_geo is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = await response.parse()
        assert_matches_type(AsyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = await response.parse()
            assert_matches_type(AsyncOffsetPage[H3GeoListResponse], h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, h3_geo, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, h3_geo, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = await response.parse()
        assert_matches_type(str, h3_geo, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = await response.parse()
            assert_matches_type(str, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.get(
            id="id",
        )
        assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = await response.parse()
        assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = await response.parse()
            assert_matches_type(H3GeoGetResponse, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.h3_geo.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.queryhelp()
        assert_matches_type(H3GeoQueryhelpResponse, h3_geo, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = await response.parse()
        assert_matches_type(H3GeoQueryhelpResponse, h3_geo, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = await response.parse()
            assert_matches_type(H3GeoQueryhelpResponse, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        h3_geo = await async_client.h3_geo.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.h3_geo.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h3_geo = await response.parse()
        assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.h3_geo.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h3_geo = await response.parse()
            assert_matches_type(H3GeoTupleResponse, h3_geo, path=["response"])

        assert cast(Any, response.is_closed) is True
