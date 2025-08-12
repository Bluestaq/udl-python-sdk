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
    GnssRawIfGetResponse,
    GnssRawIfListResponse,
    GnssRawIfTupleResponse,
    GnssRawIfQueryhelpResponse,
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


class TestGnssRawIf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_raw_if.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = response.parse()
        assert_matches_type(SyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.gnss_raw_if.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = response.parse()
            assert_matches_type(SyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnss_raw_if, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, gnss_raw_if, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_raw_if.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = response.parse()
        assert_matches_type(str, gnss_raw_if, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.gnss_raw_if.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = response.parse()
            assert_matches_type(str, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_raw_if = client.gnss_raw_if.file_get(
            id="id",
        )
        assert gnss_raw_if.is_closed
        assert gnss_raw_if.json() == {"foo": "bar"}
        assert cast(Any, gnss_raw_if.is_closed) is True
        assert isinstance(gnss_raw_if, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_raw_if = client.gnss_raw_if.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert gnss_raw_if.is_closed
        assert gnss_raw_if.json() == {"foo": "bar"}
        assert cast(Any, gnss_raw_if.is_closed) is True
        assert isinstance(gnss_raw_if, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        gnss_raw_if = client.gnss_raw_if.with_raw_response.file_get(
            id="id",
        )

        assert gnss_raw_if.is_closed is True
        assert gnss_raw_if.http_request.headers.get("X-Stainless-Lang") == "python"
        assert gnss_raw_if.json() == {"foo": "bar"}
        assert isinstance(gnss_raw_if, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.gnss_raw_if.with_streaming_response.file_get(
            id="id",
        ) as gnss_raw_if:
            assert not gnss_raw_if.is_closed
            assert gnss_raw_if.http_request.headers.get("X-Stainless-Lang") == "python"

            assert gnss_raw_if.json() == {"foo": "bar"}
            assert cast(Any, gnss_raw_if.is_closed) is True
            assert isinstance(gnss_raw_if, StreamedBinaryAPIResponse)

        assert cast(Any, gnss_raw_if.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_file_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gnss_raw_if.with_raw_response.file_get(
                id="",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.get(
            id="id",
        )
        assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_raw_if.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = response.parse()
        assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.gnss_raw_if.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = response.parse()
            assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gnss_raw_if.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.queryhelp()
        assert_matches_type(GnssRawIfQueryhelpResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_raw_if.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = response.parse()
        assert_matches_type(GnssRawIfQueryhelpResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.gnss_raw_if.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = response.parse()
            assert_matches_type(GnssRawIfQueryhelpResponse, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_raw_if.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = response.parse()
        assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.gnss_raw_if.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = response.parse()
            assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_zip(self, client: Unifieddatalibrary) -> None:
        gnss_raw_if = client.gnss_raw_if.upload_zip(
            file=b"raw file contents",
        )
        assert gnss_raw_if is None

    @parametrize
    def test_raw_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_raw_if.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = response.parse()
        assert gnss_raw_if is None

    @parametrize
    def test_streaming_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        with client.gnss_raw_if.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = response.parse()
            assert gnss_raw_if is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGnssRawIf:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_raw_if.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = await response.parse()
        assert_matches_type(AsyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_raw_if.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = await response.parse()
            assert_matches_type(AsyncOffsetPage[GnssRawIfListResponse], gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnss_raw_if, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, gnss_raw_if, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_raw_if.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = await response.parse()
        assert_matches_type(str, gnss_raw_if, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_raw_if.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = await response.parse()
            assert_matches_type(str, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_raw_if = await async_client.gnss_raw_if.file_get(
            id="id",
        )
        assert gnss_raw_if.is_closed
        assert await gnss_raw_if.json() == {"foo": "bar"}
        assert cast(Any, gnss_raw_if.is_closed) is True
        assert isinstance(gnss_raw_if, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_raw_if = await async_client.gnss_raw_if.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert gnss_raw_if.is_closed
        assert await gnss_raw_if.json() == {"foo": "bar"}
        assert cast(Any, gnss_raw_if.is_closed) is True
        assert isinstance(gnss_raw_if, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        gnss_raw_if = await async_client.gnss_raw_if.with_raw_response.file_get(
            id="id",
        )

        assert gnss_raw_if.is_closed is True
        assert gnss_raw_if.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await gnss_raw_if.json() == {"foo": "bar"}
        assert isinstance(gnss_raw_if, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_file_get(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.gnss_raw_if.with_streaming_response.file_get(
            id="id",
        ) as gnss_raw_if:
            assert not gnss_raw_if.is_closed
            assert gnss_raw_if.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await gnss_raw_if.json() == {"foo": "bar"}
            assert cast(Any, gnss_raw_if.is_closed) is True
            assert isinstance(gnss_raw_if, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, gnss_raw_if.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_file_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gnss_raw_if.with_raw_response.file_get(
                id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.get(
            id="id",
        )
        assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_raw_if.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = await response.parse()
        assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_raw_if.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = await response.parse()
            assert_matches_type(GnssRawIfGetResponse, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gnss_raw_if.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.queryhelp()
        assert_matches_type(GnssRawIfQueryhelpResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_raw_if.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = await response.parse()
        assert_matches_type(GnssRawIfQueryhelpResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_raw_if.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = await response.parse()
            assert_matches_type(GnssRawIfQueryhelpResponse, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_raw_if.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = await response.parse()
        assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_raw_if.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = await response.parse()
            assert_matches_type(GnssRawIfTupleResponse, gnss_raw_if, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_raw_if = await async_client.gnss_raw_if.upload_zip(
            file=b"raw file contents",
        )
        assert gnss_raw_if is None

    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_raw_if.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_raw_if = await response.parse()
        assert gnss_raw_if is None

    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_raw_if.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_raw_if = await response.parse()
            assert gnss_raw_if is None

        assert cast(Any, response.is_closed) is True
