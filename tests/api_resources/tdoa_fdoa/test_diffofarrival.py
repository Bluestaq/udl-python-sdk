# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.tdoa_fdoa import (
    DiffofarrivalListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiffofarrival:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert diffofarrival is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            bandwidth=0,
            collection_mode="collectionMode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            delta_range=0,
            delta_range_rate=0,
            delta_range_rate_unc=0,
            delta_range_unc=0,
            descriptor="descriptor",
            fdoa=0,
            fdoa_unc=0,
            frequency=0,
            id_on_orbit="idOnOrbit",
            id_sensor1="idSensor1",
            id_sensor2="idSensor2",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id1="origSensorId1",
            orig_sensor_id2="origSensorId2",
            raw_file_uri="rawFileURI",
            sat_no=0,
            sen2alt=0,
            sen2lat=0,
            sen2lon=0,
            senalt=0,
            senlat=0,
            senlon=0,
            sensor1_delay=0,
            sensor2_delay=0,
            snr=0,
            source_dl="sourceDL",
            tags=["string"],
            task_id="taskId",
            tdoa=0,
            tdoa_unc=0,
            transaction_id="transactionId",
            uct=True,
        )
        assert diffofarrival is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.tdoa_fdoa.diffofarrival.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert diffofarrival is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.tdoa_fdoa.diffofarrival.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
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
        assert_matches_type(DiffofarrivalListResponse, diffofarrival, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.tdoa_fdoa.diffofarrival.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert_matches_type(DiffofarrivalListResponse, diffofarrival, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.tdoa_fdoa.diffofarrival.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert_matches_type(DiffofarrivalListResponse, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.tdoa_fdoa.diffofarrival.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )
        assert diffofarrival is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.tdoa_fdoa.diffofarrival.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert diffofarrival is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            bandwidth=0,
            collection_mode="collectionMode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            delta_range=0,
            delta_range_rate=0,
            delta_range_rate_unc=0,
            delta_range_unc=0,
            descriptor="descriptor",
            fdoa=0,
            fdoa_unc=0,
            frequency=0,
            id_on_orbit="idOnOrbit",
            id_sensor1="idSensor1",
            id_sensor2="idSensor2",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id1="origSensorId1",
            orig_sensor_id2="origSensorId2",
            raw_file_uri="rawFileURI",
            sat_no=0,
            sen2alt=0,
            sen2lat=0,
            sen2lon=0,
            senalt=0,
            senlat=0,
            senlon=0,
            sensor1_delay=0,
            sensor2_delay=0,
            snr=0,
            source_dl="sourceDL",
            tags=["string"],
            task_id="taskId",
            tdoa=0,
            tdoa_unc=0,
            transaction_id="transactionId",
            uct=True,
        )
        assert diffofarrival is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.tdoa_fdoa.diffofarrival.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert diffofarrival is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.tdoa_fdoa.diffofarrival.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
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
        assert_matches_type(DiffofarrivalListResponse, diffofarrival, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.tdoa_fdoa.diffofarrival.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert_matches_type(DiffofarrivalListResponse, diffofarrival, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.tdoa_fdoa.diffofarrival.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert_matches_type(DiffofarrivalListResponse, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.tdoa_fdoa.diffofarrival.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )
        assert diffofarrival is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.tdoa_fdoa.diffofarrival.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True
