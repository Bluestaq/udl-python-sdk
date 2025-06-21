# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    GroundImageryGetResponse,
    GroundImageryListResponse,
    GroundImageryTupleResponse,
    GroundImageryQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroundImagery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert ground_imagery is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.create(
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
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.create(
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
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.create(
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

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert_matches_type(SyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert_matches_type(SyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ground_imagery, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ground_imagery, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert_matches_type(str, ground_imagery, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert_matches_type(str, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.get(
            id="id",
        )
        assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ground_imagery.with_raw_response.get(
                id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ground_imagery = client.ground_imagery.get_file(
            id="id",
        )
        assert ground_imagery.is_closed
        assert ground_imagery.json() == {"foo": "bar"}
        assert cast(Any, ground_imagery.is_closed) is True
        assert isinstance(ground_imagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_file_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ground_imagery = client.ground_imagery.get_file(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert ground_imagery.is_closed
        assert ground_imagery.json() == {"foo": "bar"}
        assert cast(Any, ground_imagery.is_closed) is True
        assert isinstance(ground_imagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        ground_imagery = client.ground_imagery.with_raw_response.get_file(
            id="id",
        )

        assert ground_imagery.is_closed is True
        assert ground_imagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert ground_imagery.json() == {"foo": "bar"}
        assert isinstance(ground_imagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.ground_imagery.with_streaming_response.get_file(
            id="id",
        ) as ground_imagery:
            assert not ground_imagery.is_closed
            assert ground_imagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert ground_imagery.json() == {"foo": "bar"}
            assert cast(Any, ground_imagery.is_closed) is True
            assert isinstance(ground_imagery, StreamedBinaryAPIResponse)

        assert cast(Any, ground_imagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_file(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ground_imagery.with_raw_response.get_file(
                id="",
            )

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
            first_result=0,
            max_results=0,
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
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.queryhelp()
        assert_matches_type(GroundImageryQueryhelpResponse, ground_imagery, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert_matches_type(GroundImageryQueryhelpResponse, ground_imagery, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert_matches_type(GroundImageryQueryhelpResponse, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_zip(self, client: Unifieddatalibrary) -> None:
        ground_imagery = client.ground_imagery.upload_zip(
            file=b"raw file contents",
        )
        assert ground_imagery is None

    @parametrize
    def test_raw_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        response = client.ground_imagery.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = response.parse()
        assert ground_imagery is None

    @parametrize
    def test_streaming_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        with client.ground_imagery.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGroundImagery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert ground_imagery is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.create(
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
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.create(
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
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.create(
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

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert_matches_type(AsyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert_matches_type(AsyncOffsetPage[GroundImageryListResponse], ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ground_imagery, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, ground_imagery, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert_matches_type(str, ground_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert_matches_type(str, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.get(
            id="id",
        )
        assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert_matches_type(GroundImageryGetResponse, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ground_imagery.with_raw_response.get(
                id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_file(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ground_imagery = await async_client.ground_imagery.get_file(
            id="id",
        )
        assert ground_imagery.is_closed
        assert await ground_imagery.json() == {"foo": "bar"}
        assert cast(Any, ground_imagery.is_closed) is True
        assert isinstance(ground_imagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_file_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        ground_imagery = await async_client.ground_imagery.get_file(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert ground_imagery.is_closed
        assert await ground_imagery.json() == {"foo": "bar"}
        assert cast(Any, ground_imagery.is_closed) is True
        assert isinstance(ground_imagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_file(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        ground_imagery = await async_client.ground_imagery.with_raw_response.get_file(
            id="id",
        )

        assert ground_imagery.is_closed is True
        assert ground_imagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await ground_imagery.json() == {"foo": "bar"}
        assert isinstance(ground_imagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_file(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.ground_imagery.with_streaming_response.get_file(
            id="id",
        ) as ground_imagery:
            assert not ground_imagery.is_closed
            assert ground_imagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await ground_imagery.json() == {"foo": "bar"}
            assert cast(Any, ground_imagery.is_closed) is True
            assert isinstance(ground_imagery, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, ground_imagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_file(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ground_imagery.with_raw_response.get_file(
                id="",
            )

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
            first_result=0,
            max_results=0,
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
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.queryhelp()
        assert_matches_type(GroundImageryQueryhelpResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert_matches_type(GroundImageryQueryhelpResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert_matches_type(GroundImageryQueryhelpResponse, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert_matches_type(GroundImageryTupleResponse, ground_imagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        ground_imagery = await async_client.ground_imagery.upload_zip(
            file=b"raw file contents",
        )
        assert ground_imagery is None

    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ground_imagery.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ground_imagery = await response.parse()
        assert ground_imagery is None

    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ground_imagery.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ground_imagery = await response.parse()
            assert ground_imagery is None

        assert cast(Any, response.is_closed) is True
