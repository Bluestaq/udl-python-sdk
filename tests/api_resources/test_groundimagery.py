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
    GroundimageryListResponse,
    GroundimageryTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from unifieddatalibrary.types.udl.groundimagery import GroundImageryFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroundimagery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        groundimagery = client.groundimagery.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert groundimagery is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        groundimagery = client.groundimagery.create(
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
        assert groundimagery is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.groundimagery.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = response.parse()
        assert groundimagery is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.groundimagery.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = response.parse()
            assert groundimagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        groundimagery = client.groundimagery.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GroundimageryListResponse, groundimagery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.groundimagery.with_raw_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = response.parse()
        assert_matches_type(GroundimageryListResponse, groundimagery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.groundimagery.with_streaming_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = response.parse()
            assert_matches_type(GroundimageryListResponse, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        groundimagery = client.groundimagery.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, groundimagery, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.groundimagery.with_raw_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = response.parse()
        assert_matches_type(str, groundimagery, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.groundimagery.with_streaming_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = response.parse()
            assert_matches_type(str, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        groundimagery = client.groundimagery.get(
            "id",
        )
        assert_matches_type(GroundImageryFull, groundimagery, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.groundimagery.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = response.parse()
        assert_matches_type(GroundImageryFull, groundimagery, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.groundimagery.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = response.parse()
            assert_matches_type(GroundImageryFull, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.groundimagery.with_raw_response.get(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        groundimagery = client.groundimagery.get_file(
            "id",
        )
        assert groundimagery.is_closed
        assert groundimagery.json() == {"foo": "bar"}
        assert cast(Any, groundimagery.is_closed) is True
        assert isinstance(groundimagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        groundimagery = client.groundimagery.with_raw_response.get_file(
            "id",
        )

        assert groundimagery.is_closed is True
        assert groundimagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert groundimagery.json() == {"foo": "bar"}
        assert isinstance(groundimagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_file(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.groundimagery.with_streaming_response.get_file(
            "id",
        ) as groundimagery:
            assert not groundimagery.is_closed
            assert groundimagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert groundimagery.json() == {"foo": "bar"}
            assert cast(Any, groundimagery.is_closed) is True
            assert isinstance(groundimagery, StreamedBinaryAPIResponse)

        assert cast(Any, groundimagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_file(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.groundimagery.with_raw_response.get_file(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        groundimagery = client.groundimagery.queryhelp()
        assert groundimagery is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.groundimagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = response.parse()
        assert groundimagery is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.groundimagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = response.parse()
            assert groundimagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        groundimagery = client.groundimagery.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GroundimageryTupleResponse, groundimagery, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.groundimagery.with_raw_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = response.parse()
        assert_matches_type(GroundimageryTupleResponse, groundimagery, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.groundimagery.with_streaming_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = response.parse()
            assert_matches_type(GroundimageryTupleResponse, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroundimagery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        groundimagery = await async_client.groundimagery.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )
        assert groundimagery is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        groundimagery = await async_client.groundimagery.create(
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
        assert groundimagery is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.groundimagery.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = await response.parse()
        assert groundimagery is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.groundimagery.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            filename="Example file name",
            image_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = await response.parse()
            assert groundimagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        groundimagery = await async_client.groundimagery.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GroundimageryListResponse, groundimagery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.groundimagery.with_raw_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = await response.parse()
        assert_matches_type(GroundimageryListResponse, groundimagery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.groundimagery.with_streaming_response.list(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = await response.parse()
            assert_matches_type(GroundimageryListResponse, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        groundimagery = await async_client.groundimagery.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, groundimagery, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.groundimagery.with_raw_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = await response.parse()
        assert_matches_type(str, groundimagery, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.groundimagery.with_streaming_response.count(
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = await response.parse()
            assert_matches_type(str, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        groundimagery = await async_client.groundimagery.get(
            "id",
        )
        assert_matches_type(GroundImageryFull, groundimagery, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.groundimagery.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = await response.parse()
        assert_matches_type(GroundImageryFull, groundimagery, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.groundimagery.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = await response.parse()
            assert_matches_type(GroundImageryFull, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.groundimagery.with_raw_response.get(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_file(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        groundimagery = await async_client.groundimagery.get_file(
            "id",
        )
        assert groundimagery.is_closed
        assert await groundimagery.json() == {"foo": "bar"}
        assert cast(Any, groundimagery.is_closed) is True
        assert isinstance(groundimagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_file(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        groundimagery = await async_client.groundimagery.with_raw_response.get_file(
            "id",
        )

        assert groundimagery.is_closed is True
        assert groundimagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await groundimagery.json() == {"foo": "bar"}
        assert isinstance(groundimagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_file(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/groundimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.groundimagery.with_streaming_response.get_file(
            "id",
        ) as groundimagery:
            assert not groundimagery.is_closed
            assert groundimagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await groundimagery.json() == {"foo": "bar"}
            assert cast(Any, groundimagery.is_closed) is True
            assert isinstance(groundimagery, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, groundimagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_file(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.groundimagery.with_raw_response.get_file(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        groundimagery = await async_client.groundimagery.queryhelp()
        assert groundimagery is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.groundimagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = await response.parse()
        assert groundimagery is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.groundimagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = await response.parse()
            assert groundimagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        groundimagery = await async_client.groundimagery.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GroundimageryTupleResponse, groundimagery, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.groundimagery.with_raw_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        groundimagery = await response.parse()
        assert_matches_type(GroundimageryTupleResponse, groundimagery, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.groundimagery.with_streaming_response.tuple(
            columns="columns",
            image_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            groundimagery = await response.parse()
            assert_matches_type(GroundimageryTupleResponse, groundimagery, path=["response"])

        assert cast(Any, response.is_closed) is True
