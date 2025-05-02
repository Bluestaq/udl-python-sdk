# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.tdoa_fdoa import (
    DiffofarrivalAbridged,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiffofarrival:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )
        assert diffofarrival is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            id="DIFFOFARRIVAL-ID",
            bandwidth=1.1,
            collection_mode="SURVEY",
            delta_range=1.1,
            delta_range_rate=1.1,
            delta_range_rate_unc=1.1,
            delta_range_unc=1.1,
            descriptor="Example descriptor",
            fdoa=1.1,
            fdoa_unc=1.1,
            frequency=1.1,
            id_sensor1="SENSOR1-ID",
            id_sensor2="SENSOR2-ID",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id1="ORIGSENSOR1-ID",
            orig_sensor_id2="ORIGSENSOR2-ID",
            raw_file_uri="rawFileURI",
            sat_no=25544,
            sen2alt=1.1,
            sen2lat=1.1,
            sen2lon=1.1,
            senalt=1.1,
            senlat=45.1,
            senlon=120.1,
            sensor1_delay=1.1,
            sensor2_delay=1.1,
            snr=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
            tdoa=1.1,
            tdoa_unc=1.1,
            transaction_id="TRANSACTION-ID",
            uct=False,
        )
        assert diffofarrival is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.tdoa_fdoa.diffofarrival.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert diffofarrival is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.tdoa_fdoa.diffofarrival.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.tdoa_fdoa.diffofarrival.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert_matches_type(SyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.tdoa_fdoa.diffofarrival.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert_matches_type(SyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, diffofarrival, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, diffofarrival, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.tdoa_fdoa.diffofarrival.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert_matches_type(str, diffofarrival, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.tdoa_fdoa.diffofarrival.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert_matches_type(str, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert diffofarrival is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.tdoa_fdoa.diffofarrival.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert diffofarrival is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.tdoa_fdoa.diffofarrival.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDiffofarrival:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )
        assert diffofarrival is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            id="DIFFOFARRIVAL-ID",
            bandwidth=1.1,
            collection_mode="SURVEY",
            delta_range=1.1,
            delta_range_rate=1.1,
            delta_range_rate_unc=1.1,
            delta_range_unc=1.1,
            descriptor="Example descriptor",
            fdoa=1.1,
            fdoa_unc=1.1,
            frequency=1.1,
            id_sensor1="SENSOR1-ID",
            id_sensor2="SENSOR2-ID",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id1="ORIGSENSOR1-ID",
            orig_sensor_id2="ORIGSENSOR2-ID",
            raw_file_uri="rawFileURI",
            sat_no=25544,
            sen2alt=1.1,
            sen2lat=1.1,
            sen2lon=1.1,
            senalt=1.1,
            senlat=45.1,
            senlon=120.1,
            sensor1_delay=1.1,
            sensor2_delay=1.1,
            snr=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
            tdoa=1.1,
            tdoa_unc=1.1,
            transaction_id="TRANSACTION-ID",
            uct=False,
        )
        assert diffofarrival is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.tdoa_fdoa.diffofarrival.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert diffofarrival is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.tdoa_fdoa.diffofarrival.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.tdoa_fdoa.diffofarrival.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert_matches_type(AsyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.tdoa_fdoa.diffofarrival.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert_matches_type(AsyncOffsetPage[DiffofarrivalAbridged], diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, diffofarrival, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, diffofarrival, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.tdoa_fdoa.diffofarrival.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert_matches_type(str, diffofarrival, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.tdoa_fdoa.diffofarrival.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert_matches_type(str, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert diffofarrival is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.tdoa_fdoa.diffofarrival.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert diffofarrival is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.tdoa_fdoa.diffofarrival.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True
