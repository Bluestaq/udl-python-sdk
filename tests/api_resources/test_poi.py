# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    PoiGetResponse,
    PoiListResponse,
    PoiTupleResponse,
    PoiQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPoi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
        )
        assert poi is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
            id="POI-ID",
            activity="TRAINING",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            alt=5.23,
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            asset="PLATFORM_NAME",
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="Type1",
            az=45.23,
            be_number="0427RT1030",
            ce=10.23,
            cntct="Contact Info",
            conf=0.5,
            desc="Description of the object",
            el=45.23,
            elle=[125.5, 85.1, 125.75],
            env="SURFACE",
            groups=["GROUP1", "GROUP2"],
            how="h-g-i-g-o",
            ident="FRIEND",
            id_weather_report=["WEATHER-EVENT-ID1", "WEATHER-EVENT-ID2"],
            lat=45.23,
            le=10.23,
            lon=45.23,
            msnid="MSN-ID",
            orientation=45.23,
            origin="THIRD_PARTY_DATASOURCE",
            plat="COMBAT_VEHICLE",
            pps="BDA",
            pri=2,
            spec="LIGHT_TANK",
            src_ids=["ID1", "ID2"],
            src_typs=["TYPE1", "TYPE2"],
            stale=parse_datetime("2020-01-01T16:00:00.123456Z"),
            start=parse_datetime("2020-01-01T16:00:00.123456Z"),
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            trkid="TRK-ID",
            type="a-h-G",
            urls=["URL1", "URL2"],
        )
        assert poi is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert poi is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[PoiListResponse], poi, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[PoiListResponse], poi, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert_matches_type(SyncOffsetPage[PoiListResponse], poi, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert_matches_type(SyncOffsetPage[PoiListResponse], poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, poi, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, poi, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert_matches_type(str, poi, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert_matches_type(str, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert poi is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert poi is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.get(
            id="id",
        )
        assert_matches_type(PoiGetResponse, poi, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PoiGetResponse, poi, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert_matches_type(PoiGetResponse, poi, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert_matches_type(PoiGetResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.poi.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.queryhelp()
        assert_matches_type(PoiQueryhelpResponse, poi, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert_matches_type(PoiQueryhelpResponse, poi, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert_matches_type(PoiQueryhelpResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PoiTupleResponse, poi, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PoiTupleResponse, poi, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert_matches_type(PoiTupleResponse, poi, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert_matches_type(PoiTupleResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        poi = client.poi.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert poi is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.poi.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = response.parse()
        assert poi is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.poi.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPoi:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
        )
        assert poi is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
            id="POI-ID",
            activity="TRAINING",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            alt=5.23,
            andims=3,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=3,
            asset="PLATFORM_NAME",
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="Type1",
            az=45.23,
            be_number="0427RT1030",
            ce=10.23,
            cntct="Contact Info",
            conf=0.5,
            desc="Description of the object",
            el=45.23,
            elle=[125.5, 85.1, 125.75],
            env="SURFACE",
            groups=["GROUP1", "GROUP2"],
            how="h-g-i-g-o",
            ident="FRIEND",
            id_weather_report=["WEATHER-EVENT-ID1", "WEATHER-EVENT-ID2"],
            lat=45.23,
            le=10.23,
            lon=45.23,
            msnid="MSN-ID",
            orientation=45.23,
            origin="THIRD_PARTY_DATASOURCE",
            plat="COMBAT_VEHICLE",
            pps="BDA",
            pri=2,
            spec="LIGHT_TANK",
            src_ids=["ID1", "ID2"],
            src_typs=["TYPE1", "TYPE2"],
            stale=parse_datetime("2020-01-01T16:00:00.123456Z"),
            start=parse_datetime("2020-01-01T16:00:00.123456Z"),
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            trkid="TRK-ID",
            type="a-h-G",
            urls=["URL1", "URL2"],
        )
        assert poi is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert poi is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="POI_NAME",
            poiid="POI-ID",
            source="Bluestaq",
            ts=parse_datetime("2020-01-01T16:00:00.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[PoiListResponse], poi, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[PoiListResponse], poi, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert_matches_type(AsyncOffsetPage[PoiListResponse], poi, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert_matches_type(AsyncOffsetPage[PoiListResponse], poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, poi, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, poi, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert_matches_type(str, poi, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert_matches_type(str, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert poi is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert poi is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.get(
            id="id",
        )
        assert_matches_type(PoiGetResponse, poi, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PoiGetResponse, poi, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert_matches_type(PoiGetResponse, poi, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert_matches_type(PoiGetResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.poi.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.queryhelp()
        assert_matches_type(PoiQueryhelpResponse, poi, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert_matches_type(PoiQueryhelpResponse, poi, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert_matches_type(PoiQueryhelpResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PoiTupleResponse, poi, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PoiTupleResponse, poi, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert_matches_type(PoiTupleResponse, poi, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert_matches_type(PoiTupleResponse, poi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        poi = await async_client.poi.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )
        assert poi is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.poi.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poi = await response.parse()
        assert poi is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.poi.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "name": "POI_NAME",
                    "poiid": "POI-ID",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2020-01-01T16:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poi = await response.parse()
            assert poi is None

        assert cast(Any, response.is_closed) is True
