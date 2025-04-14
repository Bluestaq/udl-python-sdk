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
    def test_method_history_aodr(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ground_imagery is None

    @parametrize
    def test_method_history_aodr_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert ground_imagery is None

    @parametrize
    def test_raw_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert ground_imagery is None

    @parametrize
    def test_streaming_response_history_aodr(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_zip(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert ground_imagery is None

    @parametrize
    def test_method_upload_zip_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
            id="GROUNDIMAGERY-ID",
            checksum_value="120EA8A25E5D487BF68B5F7096440019",
            filesize=0,
            format="PNG",
            id_sensor="SENSOR-ID",
            keywords=["KEYWORD1", "KEYWORD2"],
            name="Example name",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            region="POLYGON((26.156175339112 67.3291113966927,26.0910220642717 67.2580009640721,26.6637992964562 67.1795862381682,26.730115808233 67.2501237475598,26.156175339112 67.3291113966927))",
            region_geo_json='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            region_n_dims=2,
            region_s_rid=4326,
            region_text="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            region_type="Polygon",
            subject_id="SUBJECT-ID",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="37bdef1f-5a4f-4776-bee4-7a1e0ec7d35a",
        )
        assert ground_imagery is None

    @parametrize
    def test_raw_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert ground_imagery is None

    @parametrize
    def test_streaming_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGroundImagery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ground_imagery is None

    @parametrize
    async def test_method_history_aodr_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            notification="notification",
            output_delimiter="outputDelimiter",
            output_format="outputFormat",
        )
        assert ground_imagery is None

    @parametrize
    async def test_raw_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert ground_imagery is None

    @parametrize
    async def test_streaming_response_history_aodr(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.history_aodr(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert ground_imagery is None

    @parametrize
    async def test_method_upload_zip_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
            id="GROUNDIMAGERY-ID",
            checksum_value="120EA8A25E5D487BF68B5F7096440019",
            filesize=0,
            format="PNG",
            id_sensor="SENSOR-ID",
            keywords=["KEYWORD1", "KEYWORD2"],
            name="Example name",
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            orig_sensor_id="ORIGSENSOR-ID",
            region="POLYGON((26.156175339112 67.3291113966927,26.0910220642717 67.2580009640721,26.6637992964562 67.1795862381682,26.730115808233 67.2501237475598,26.156175339112 67.3291113966927))",
            region_geo_json='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            region_n_dims=2,
            region_s_rid=4326,
            region_text="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            region_type="Polygon",
            subject_id="SUBJECT-ID",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            transaction_id="37bdef1f-5a4f-4776-bee4-7a1e0ec7d35a",
        )
        assert ground_imagery is None

    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert ground_imagery is None

    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.upload_zip(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True
