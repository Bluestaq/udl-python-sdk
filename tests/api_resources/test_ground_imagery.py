# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroundImagery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert ground_imagery is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            checksum_value="checksumValue",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            filesize=0,
            format="format",
            id_sensor="idSensor",
            keywords=["string"],
            name="name",
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            orig_sensor_id="origSensorId",
            region="region",
            region_geo_json="regionGeoJSON",
            region_n_dims=0,
            region_s_rid=0,
            region_text="regionText",
            region_type="regionType",
            source_dl="sourceDL",
            subject_id="subjectId",
            tags=["string"],
            transaction_id="transactionId",
        )
        assert ground_imagery is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert ground_imagery is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGroundImagery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert ground_imagery is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            checksum_value="checksumValue",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            filesize=0,
            format="format",
            id_sensor="idSensor",
            keywords=["string"],
            name="name",
            notes="notes",
            origin="origin",
            orig_network="origNetwork",
            orig_sensor_id="origSensorId",
            region="region",
            region_geo_json="regionGeoJSON",
            region_n_dims=0,
            region_s_rid=0,
            region_text="regionText",
            region_type="regionType",
            source_dl="sourceDL",
            subject_id="subjectId",
            tags=["string"],
            transaction_id="transactionId",
        )
        assert ground_imagery is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert ground_imagery is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            filename="filename",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True
