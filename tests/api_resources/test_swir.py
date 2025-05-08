# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SwirListResponse,
    SwirTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.swir import SwirFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSwir:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )
        assert swir is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id="SWIR-ID",
            abs_fluxes=[1.23, 4.56],
            bad_wave="Example Comments",
            flux_ratios=[1.23, 4.56],
            lat=70.55208,
            location_name="AeroTel",
            lon=81.18191,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="WildBlue-1",
            ratio_wavelengths=[1.23, 4.56],
            sat_no=25544,
            solar_phase_angle=1.23,
            wavelengths=[1.23, 4.56],
        )
        assert swir is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.swir.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = response.parse()
        assert swir is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.swir.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = response.parse()
            assert swir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[SwirListResponse], swir, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SwirListResponse], swir, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.swir.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = response.parse()
        assert_matches_type(SyncOffsetPage[SwirListResponse], swir, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.swir.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = response.parse()
            assert_matches_type(SyncOffsetPage[SwirListResponse], swir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, swir, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, swir, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.swir.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = response.parse()
        assert_matches_type(str, swir, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.swir.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = response.parse()
            assert_matches_type(str, swir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert swir is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.swir.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = response.parse()
        assert swir is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.swir.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = response.parse()
            assert swir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.get(
            id="id",
        )
        assert_matches_type(SwirFull, swir, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SwirFull, swir, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.swir.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = response.parse()
        assert_matches_type(SwirFull, swir, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.swir.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = response.parse()
            assert_matches_type(SwirFull, swir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.swir.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.queryhelp()
        assert swir is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.swir.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = response.parse()
        assert swir is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.swir.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = response.parse()
            assert swir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SwirTupleResponse, swir, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        swir = client.swir.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SwirTupleResponse, swir, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.swir.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = response.parse()
        assert_matches_type(SwirTupleResponse, swir, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.swir.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = response.parse()
            assert_matches_type(SwirTupleResponse, swir, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSwir:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )
        assert swir is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
            id="SWIR-ID",
            abs_fluxes=[1.23, 4.56],
            bad_wave="Example Comments",
            flux_ratios=[1.23, 4.56],
            lat=70.55208,
            location_name="AeroTel",
            lon=81.18191,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="WildBlue-1",
            ratio_wavelengths=[1.23, 4.56],
            sat_no=25544,
            solar_phase_angle=1.23,
            wavelengths=[1.23, 4.56],
        )
        assert swir is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.swir.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = await response.parse()
        assert swir is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.swir.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            ts=parse_datetime("2021-01-01T01:01:01.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = await response.parse()
            assert swir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[SwirListResponse], swir, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SwirListResponse], swir, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.swir.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = await response.parse()
        assert_matches_type(AsyncOffsetPage[SwirListResponse], swir, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.swir.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = await response.parse()
            assert_matches_type(AsyncOffsetPage[SwirListResponse], swir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, swir, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, swir, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.swir.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = await response.parse()
        assert_matches_type(str, swir, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.swir.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = await response.parse()
            assert_matches_type(str, swir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert swir is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.swir.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = await response.parse()
        assert swir is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.swir.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = await response.parse()
            assert swir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.get(
            id="id",
        )
        assert_matches_type(SwirFull, swir, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SwirFull, swir, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.swir.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = await response.parse()
        assert_matches_type(SwirFull, swir, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.swir.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = await response.parse()
            assert_matches_type(SwirFull, swir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.swir.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.queryhelp()
        assert swir is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.swir.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = await response.parse()
        assert swir is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.swir.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = await response.parse()
            assert swir is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SwirTupleResponse, swir, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        swir = await async_client.swir.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SwirTupleResponse, swir, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.swir.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swir = await response.parse()
        assert_matches_type(SwirTupleResponse, swir, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.swir.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swir = await response.parse()
            assert_matches_type(SwirTupleResponse, swir, path=["response"])

        assert cast(Any, response.is_closed) is True
