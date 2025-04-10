# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    GeostatusListResponse,
    GeostatusTupleResponse,
)
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.types.udl.geostatus import GeoStatusFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGeostatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert geostatus is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.create(
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
        assert geostatus is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.geostatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = response.parse()
        assert geostatus is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.geostatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = response.parse()
            assert geostatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(GeostatusListResponse, geostatus, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.geostatus.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = response.parse()
        assert_matches_type(GeostatusListResponse, geostatus, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.geostatus.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = response.parse()
            assert_matches_type(GeostatusListResponse, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, geostatus, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.geostatus.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = response.parse()
        assert_matches_type(str, geostatus, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.geostatus.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = response.parse()
            assert_matches_type(str, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert geostatus is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.geostatus.with_raw_response.create_bulk(
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
        geostatus = response.parse()
        assert geostatus is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.geostatus.with_streaming_response.create_bulk(
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

            geostatus = response.parse()
            assert geostatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.get(
            "id",
        )
        assert_matches_type(GeoStatusFull, geostatus, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.geostatus.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = response.parse()
        assert_matches_type(GeoStatusFull, geostatus, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.geostatus.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = response.parse()
            assert_matches_type(GeoStatusFull, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.geostatus.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.queryhelp()
        assert geostatus is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.geostatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = response.parse()
        assert geostatus is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.geostatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = response.parse()
            assert geostatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        geostatus = client.geostatus.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(GeostatusTupleResponse, geostatus, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.geostatus.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = response.parse()
        assert_matches_type(GeostatusTupleResponse, geostatus, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.geostatus.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = response.parse()
            assert_matches_type(GeostatusTupleResponse, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGeostatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert geostatus is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.create(
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
        assert geostatus is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geostatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = await response.parse()
        assert geostatus is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geostatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = await response.parse()
            assert geostatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(GeostatusListResponse, geostatus, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geostatus.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = await response.parse()
        assert_matches_type(GeostatusListResponse, geostatus, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geostatus.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = await response.parse()
            assert_matches_type(GeostatusListResponse, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, geostatus, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geostatus.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = await response.parse()
        assert_matches_type(str, geostatus, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geostatus.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = await response.parse()
            assert_matches_type(str, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert geostatus is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geostatus.with_raw_response.create_bulk(
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
        geostatus = await response.parse()
        assert geostatus is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geostatus.with_streaming_response.create_bulk(
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

            geostatus = await response.parse()
            assert geostatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.get(
            "id",
        )
        assert_matches_type(GeoStatusFull, geostatus, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geostatus.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = await response.parse()
        assert_matches_type(GeoStatusFull, geostatus, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geostatus.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = await response.parse()
            assert_matches_type(GeoStatusFull, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.geostatus.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.queryhelp()
        assert geostatus is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geostatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = await response.parse()
        assert geostatus is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geostatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = await response.parse()
            assert geostatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        geostatus = await async_client.geostatus.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(GeostatusTupleResponse, geostatus, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.geostatus.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geostatus = await response.parse()
        assert_matches_type(GeostatusTupleResponse, geostatus, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.geostatus.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geostatus = await response.parse()
            assert_matches_type(GeostatusTupleResponse, geostatus, path=["response"])

        assert cast(Any, response.is_closed) is True
