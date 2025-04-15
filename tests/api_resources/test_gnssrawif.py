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
    GnssrawifListResponse,
    GnssrawifTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from unifieddatalibrary.types.udl.gnssrawif import GnssRawIfFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGnssrawif:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.gnssrawif.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssrawifListResponse, gnssrawif, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.gnssrawif.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert_matches_type(GnssrawifListResponse, gnssrawif, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.gnssrawif.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = response.parse()
            assert_matches_type(GnssrawifListResponse, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.gnssrawif.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnssrawif, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.gnssrawif.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert_matches_type(str, gnssrawif, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.gnssrawif.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = response.parse()
            assert_matches_type(str, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnssrawif = client.gnssrawif.file_get(
            "id",
        )
        assert gnssrawif.is_closed
        assert gnssrawif.json() == {"foo": "bar"}
        assert cast(Any, gnssrawif.is_closed) is True
        assert isinstance(gnssrawif, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        gnssrawif = client.gnssrawif.with_raw_response.file_get(
            "id",
        )

        assert gnssrawif.is_closed is True
        assert gnssrawif.http_request.headers.get("X-Stainless-Lang") == "python"
        assert gnssrawif.json() == {"foo": "bar"}
        assert isinstance(gnssrawif, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.gnssrawif.with_streaming_response.file_get(
            "id",
        ) as gnssrawif:
            assert not gnssrawif.is_closed
            assert gnssrawif.http_request.headers.get("X-Stainless-Lang") == "python"

            assert gnssrawif.json() == {"foo": "bar"}
            assert cast(Any, gnssrawif.is_closed) is True
            assert isinstance(gnssrawif, StreamedBinaryAPIResponse)

        assert cast(Any, gnssrawif.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_file_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gnssrawif.with_raw_response.file_get(
                "",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.gnssrawif.get(
            "id",
        )
        assert_matches_type(GnssRawIfFull, gnssrawif, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.gnssrawif.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert_matches_type(GnssRawIfFull, gnssrawif, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.gnssrawif.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = response.parse()
            assert_matches_type(GnssRawIfFull, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gnssrawif.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.gnssrawif.queryhelp()
        assert gnssrawif is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.gnssrawif.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert gnssrawif is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.gnssrawif.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = response.parse()
            assert gnssrawif is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.gnssrawif.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssrawifTupleResponse, gnssrawif, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.gnssrawif.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert_matches_type(GnssrawifTupleResponse, gnssrawif, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.gnssrawif.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = response.parse()
            assert_matches_type(GnssrawifTupleResponse, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_zip(self, client: Unifieddatalibrary) -> None:
        gnssrawif = client.gnssrawif.upload_zip(
            file=b"raw file contents",
        )
        assert gnssrawif is None

    @parametrize
    def test_raw_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        response = client.gnssrawif.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = response.parse()
        assert gnssrawif is None

    @parametrize
    def test_streaming_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        with client.gnssrawif.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = response.parse()
            assert gnssrawif is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGnssrawif:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.gnssrawif.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssrawifListResponse, gnssrawif, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnssrawif.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert_matches_type(GnssrawifListResponse, gnssrawif, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnssrawif.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert_matches_type(GnssrawifListResponse, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.gnssrawif.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnssrawif, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnssrawif.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert_matches_type(str, gnssrawif, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnssrawif.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert_matches_type(str, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        gnssrawif = await async_client.gnssrawif.file_get(
            "id",
        )
        assert gnssrawif.is_closed
        assert await gnssrawif.json() == {"foo": "bar"}
        assert cast(Any, gnssrawif.is_closed) is True
        assert isinstance(gnssrawif, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        gnssrawif = await async_client.gnssrawif.with_raw_response.file_get(
            "id",
        )

        assert gnssrawif.is_closed is True
        assert gnssrawif.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await gnssrawif.json() == {"foo": "bar"}
        assert isinstance(gnssrawif, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_file_get(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/gnssrawif/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.gnssrawif.with_streaming_response.file_get(
            "id",
        ) as gnssrawif:
            assert not gnssrawif.is_closed
            assert gnssrawif.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await gnssrawif.json() == {"foo": "bar"}
            assert cast(Any, gnssrawif.is_closed) is True
            assert isinstance(gnssrawif, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, gnssrawif.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_file_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gnssrawif.with_raw_response.file_get(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.gnssrawif.get(
            "id",
        )
        assert_matches_type(GnssRawIfFull, gnssrawif, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnssrawif.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert_matches_type(GnssRawIfFull, gnssrawif, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnssrawif.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert_matches_type(GnssRawIfFull, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gnssrawif.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.gnssrawif.queryhelp()
        assert gnssrawif is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnssrawif.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert gnssrawif is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnssrawif.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert gnssrawif is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.gnssrawif.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssrawifTupleResponse, gnssrawif, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnssrawif.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert_matches_type(GnssrawifTupleResponse, gnssrawif, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnssrawif.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert_matches_type(GnssrawifTupleResponse, gnssrawif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnssrawif = await async_client.gnssrawif.upload_zip(
            file=b"raw file contents",
        )
        assert gnssrawif is None

    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnssrawif.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnssrawif = await response.parse()
        assert gnssrawif is None

    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnssrawif.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnssrawif = await response.parse()
            assert gnssrawif is None

        assert cast(Any, response.is_closed) is True
