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
    GnssRawifGetResponse,
    GnssRawifListResponse,
    GnssRawifTupleResponse,
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


class TestGnssRawif:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_rawif.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = response.parse()
        assert_matches_type(SyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.gnss_rawif.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = response.parse()
            assert_matches_type(SyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnss_rawif, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, gnss_rawif, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_rawif.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = response.parse()
        assert_matches_type(str, gnss_rawif, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.gnss_rawif.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = response.parse()
            assert_matches_type(str, gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_rawif = client.gnss_rawif.file_get(
            id="id",
        )
        assert gnss_rawif.is_closed
        assert gnss_rawif.json() == {"foo": "bar"}
        assert cast(Any, gnss_rawif.is_closed) is True
        assert isinstance(gnss_rawif, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get_with_all_params(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_rawif = client.gnss_rawif.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert gnss_rawif.is_closed
        assert gnss_rawif.json() == {"foo": "bar"}
        assert cast(Any, gnss_rawif.is_closed) is True
        assert isinstance(gnss_rawif, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        gnss_rawif = client.gnss_rawif.with_raw_response.file_get(
            id="id",
        )

        assert gnss_rawif.is_closed is True
        assert gnss_rawif.http_request.headers.get("X-Stainless-Lang") == "python"
        assert gnss_rawif.json() == {"foo": "bar"}
        assert isinstance(gnss_rawif, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.gnss_rawif.with_streaming_response.file_get(
            id="id",
        ) as gnss_rawif:
            assert not gnss_rawif.is_closed
            assert gnss_rawif.http_request.headers.get("X-Stainless-Lang") == "python"

            assert gnss_rawif.json() == {"foo": "bar"}
            assert cast(Any, gnss_rawif.is_closed) is True
            assert isinstance(gnss_rawif, StreamedBinaryAPIResponse)

        assert cast(Any, gnss_rawif.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_file_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gnss_rawif.with_raw_response.file_get(
                id="",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.get(
            id="id",
        )
        assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_rawif.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = response.parse()
        assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.gnss_rawif.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = response.parse()
            assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gnss_rawif.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.queryhelp()
        assert gnss_rawif is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_rawif.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = response.parse()
        assert gnss_rawif is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.gnss_rawif.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = response.parse()
            assert gnss_rawif is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_rawif.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = response.parse()
        assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.gnss_rawif.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = response.parse()
            assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_zip(self, client: Unifieddatalibrary) -> None:
        gnss_rawif = client.gnss_rawif.upload_zip(
            file=b"raw file contents",
        )
        assert gnss_rawif is None

    @parametrize
    def test_raw_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_rawif.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = response.parse()
        assert gnss_rawif is None

    @parametrize
    def test_streaming_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        with client.gnss_rawif.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = response.parse()
            assert gnss_rawif is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGnssRawif:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_rawif.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = await response.parse()
        assert_matches_type(AsyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_rawif.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = await response.parse()
            assert_matches_type(AsyncOffsetPage[GnssRawifListResponse], gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnss_rawif, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, gnss_rawif, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_rawif.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = await response.parse()
        assert_matches_type(str, gnss_rawif, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_rawif.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = await response.parse()
            assert_matches_type(str, gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_rawif = await async_client.gnss_rawif.file_get(
            id="id",
        )
        assert gnss_rawif.is_closed
        assert await gnss_rawif.json() == {"foo": "bar"}
        assert cast(Any, gnss_rawif.is_closed) is True
        assert isinstance(gnss_rawif, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get_with_all_params(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnss_rawif = await async_client.gnss_rawif.file_get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert gnss_rawif.is_closed
        assert await gnss_rawif.json() == {"foo": "bar"}
        assert cast(Any, gnss_rawif.is_closed) is True
        assert isinstance(gnss_rawif, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        gnss_rawif = await async_client.gnss_rawif.with_raw_response.file_get(
            id="id",
        )

        assert gnss_rawif.is_closed is True
        assert gnss_rawif.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await gnss_rawif.json() == {"foo": "bar"}
        assert isinstance(gnss_rawif, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_file_get(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.gnss_rawif.with_streaming_response.file_get(
            id="id",
        ) as gnss_rawif:
            assert not gnss_rawif.is_closed
            assert gnss_rawif.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await gnss_rawif.json() == {"foo": "bar"}
            assert cast(Any, gnss_rawif.is_closed) is True
            assert isinstance(gnss_rawif, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, gnss_rawif.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_file_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gnss_rawif.with_raw_response.file_get(
                id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.get(
            id="id",
        )
        assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_rawif.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = await response.parse()
        assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_rawif.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = await response.parse()
            assert_matches_type(GnssRawifGetResponse, gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gnss_rawif.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.queryhelp()
        assert gnss_rawif is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_rawif.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = await response.parse()
        assert gnss_rawif is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_rawif.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = await response.parse()
            assert gnss_rawif is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_rawif.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = await response.parse()
        assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_rawif.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = await response.parse()
            assert_matches_type(GnssRawifTupleResponse, gnss_rawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_rawif = await async_client.gnss_rawif.upload_zip(
            file=b"raw file contents",
        )
        assert gnss_rawif is None

    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_rawif.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_rawif = await response.parse()
        assert gnss_rawif is None

    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_rawif.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_rawif = await response.parse()
            assert gnss_rawif is None

        assert cast(Any, response.is_closed) is True
