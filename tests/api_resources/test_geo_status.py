# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    GeoStatusListResponse,
    GeoStatusTupleResponse,
)
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.geo_status import GeoStatusFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGeoStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert geo_status is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="GEOSTATUS-ID",
            confidence_level="Low",
            longitude_max=1.01,
            longitude_min=180.1,
            longitude_rate=1.1,
            lost_flag=False,
            object_status="Active",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            plane_change_status="Current",
            raw_file_uri="Example URI",
            relative_energy=1.1,
            sat_no=21,
            sc=1.1,
            semi_annual_corr_flag=False,
            ss=1.1,
            trough_type="West",
        )
        assert geo_status is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.geo_status.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = response.parse()
        assert geo_status is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.geo_status.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = response.parse()
            assert geo_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.geo_status.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = response.parse()
        assert_matches_type(SyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.geo_status.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = response.parse()
            assert_matches_type(SyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, geo_status, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, geo_status, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.geo_status.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = response.parse()
        assert_matches_type(str, geo_status, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.geo_status.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = response.parse()
            assert_matches_type(str, geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert geo_status is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.geo_status.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = response.parse()
        assert geo_status is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.geo_status.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = response.parse()
            assert geo_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.get(
            id="id",
        )
        assert_matches_type(GeoStatusFull, geo_status, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GeoStatusFull, geo_status, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.geo_status.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = response.parse()
        assert_matches_type(GeoStatusFull, geo_status, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.geo_status.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = response.parse()
            assert_matches_type(GeoStatusFull, geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.geo_status.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.queryhelp()
        assert geo_status is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.geo_status.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = response.parse()
        assert geo_status is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.geo_status.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = response.parse()
            assert geo_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        geo_status = client.geo_status.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.geo_status.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = response.parse()
        assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.geo_status.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = response.parse()
            assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGeoStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert geo_status is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="GEOSTATUS-ID",
            confidence_level="Low",
            longitude_max=1.01,
            longitude_min=180.1,
            longitude_rate=1.1,
            lost_flag=False,
            object_status="Active",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            plane_change_status="Current",
            raw_file_uri="Example URI",
            relative_energy=1.1,
            sat_no=21,
            sc=1.1,
            semi_annual_corr_flag=False,
            ss=1.1,
            trough_type="West",
        )
        assert geo_status is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geo_status.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = await response.parse()
        assert geo_status is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geo_status.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = await response.parse()
            assert geo_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geo_status.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = await response.parse()
        assert_matches_type(AsyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geo_status.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = await response.parse()
            assert_matches_type(AsyncOffsetPage[GeoStatusListResponse], geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, geo_status, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, geo_status, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geo_status.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = await response.parse()
        assert_matches_type(str, geo_status, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geo_status.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = await response.parse()
            assert_matches_type(str, geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert geo_status is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geo_status.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = await response.parse()
        assert geo_status is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geo_status.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = await response.parse()
            assert geo_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.get(
            id="id",
        )
        assert_matches_type(GeoStatusFull, geo_status, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GeoStatusFull, geo_status, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geo_status.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = await response.parse()
        assert_matches_type(GeoStatusFull, geo_status, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geo_status.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = await response.parse()
            assert_matches_type(GeoStatusFull, geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.geo_status.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.queryhelp()
        assert geo_status is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geo_status.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = await response.parse()
        assert geo_status is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geo_status.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = await response.parse()
            assert geo_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        geo_status = await async_client.geo_status.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geo_status.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geo_status = await response.parse()
        assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geo_status.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geo_status = await response.parse()
            assert_matches_type(GeoStatusTupleResponse, geo_status, path=["response"])

        assert cast(Any, response.is_closed) is True
