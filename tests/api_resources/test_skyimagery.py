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
    SkyimageryListResponse,
    SkyimageryTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from unifieddatalibrary.types.udl.skyimagery import SkyimageryFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkyimagery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        skyimagery = client.skyimagery.list(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SkyimageryListResponse, skyimagery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.skyimagery.with_raw_response.list(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = response.parse()
        assert_matches_type(SkyimageryListResponse, skyimagery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.skyimagery.with_streaming_response.list(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = response.parse()
            assert_matches_type(SkyimageryListResponse, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        skyimagery = client.skyimagery.count(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, skyimagery, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.skyimagery.with_raw_response.count(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = response.parse()
        assert_matches_type(str, skyimagery, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.skyimagery.with_streaming_response.count(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = response.parse()
            assert_matches_type(str, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/skyimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        skyimagery = client.skyimagery.file_get(
            "id",
        )
        assert skyimagery.is_closed
        assert skyimagery.json() == {"foo": "bar"}
        assert cast(Any, skyimagery.is_closed) is True
        assert isinstance(skyimagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/skyimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        skyimagery = client.skyimagery.with_raw_response.file_get(
            "id",
        )

        assert skyimagery.is_closed is True
        assert skyimagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert skyimagery.json() == {"foo": "bar"}
        assert isinstance(skyimagery, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_file_get(self, client: Unifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/skyimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.skyimagery.with_streaming_response.file_get(
            "id",
        ) as skyimagery:
            assert not skyimagery.is_closed
            assert skyimagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert skyimagery.json() == {"foo": "bar"}
            assert cast(Any, skyimagery.is_closed) is True
            assert isinstance(skyimagery, StreamedBinaryAPIResponse)

        assert cast(Any, skyimagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_file_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.skyimagery.with_raw_response.file_get(
                "",
            )

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        skyimagery = client.skyimagery.get(
            "id",
        )
        assert_matches_type(SkyimageryFull, skyimagery, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.skyimagery.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = response.parse()
        assert_matches_type(SkyimageryFull, skyimagery, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.skyimagery.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = response.parse()
            assert_matches_type(SkyimageryFull, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.skyimagery.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        skyimagery = client.skyimagery.queryhelp()
        assert skyimagery is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.skyimagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = response.parse()
        assert skyimagery is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.skyimagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = response.parse()
            assert skyimagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        skyimagery = client.skyimagery.tuple(
            columns="columns",
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SkyimageryTupleResponse, skyimagery, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.skyimagery.with_raw_response.tuple(
            columns="columns",
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = response.parse()
        assert_matches_type(SkyimageryTupleResponse, skyimagery, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.skyimagery.with_streaming_response.tuple(
            columns="columns",
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = response.parse()
            assert_matches_type(SkyimageryTupleResponse, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_zip(self, client: Unifieddatalibrary) -> None:
        skyimagery = client.skyimagery.upload_zip(
            file=b"raw file contents",
        )
        assert skyimagery is None

    @parametrize
    def test_raw_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        response = client.skyimagery.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = response.parse()
        assert skyimagery is None

    @parametrize
    def test_streaming_response_upload_zip(self, client: Unifieddatalibrary) -> None:
        with client.skyimagery.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = response.parse()
            assert skyimagery is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSkyimagery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        skyimagery = await async_client.skyimagery.list(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SkyimageryListResponse, skyimagery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.skyimagery.with_raw_response.list(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = await response.parse()
        assert_matches_type(SkyimageryListResponse, skyimagery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.skyimagery.with_streaming_response.list(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = await response.parse()
            assert_matches_type(SkyimageryListResponse, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        skyimagery = await async_client.skyimagery.count(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, skyimagery, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.skyimagery.with_raw_response.count(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = await response.parse()
        assert_matches_type(str, skyimagery, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.skyimagery.with_streaming_response.count(
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = await response.parse()
            assert_matches_type(str, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/skyimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        skyimagery = await async_client.skyimagery.file_get(
            "id",
        )
        assert skyimagery.is_closed
        assert await skyimagery.json() == {"foo": "bar"}
        assert cast(Any, skyimagery.is_closed) is True
        assert isinstance(skyimagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_file_get(self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter) -> None:
        respx_mock.get("/udl/skyimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        skyimagery = await async_client.skyimagery.with_raw_response.file_get(
            "id",
        )

        assert skyimagery.is_closed is True
        assert skyimagery.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await skyimagery.json() == {"foo": "bar"}
        assert isinstance(skyimagery, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_file_get(
        self, async_client: AsyncUnifieddatalibrary, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/udl/skyimagery/getFile/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.skyimagery.with_streaming_response.file_get(
            "id",
        ) as skyimagery:
            assert not skyimagery.is_closed
            assert skyimagery.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await skyimagery.json() == {"foo": "bar"}
            assert cast(Any, skyimagery.is_closed) is True
            assert isinstance(skyimagery, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, skyimagery.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_file_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.skyimagery.with_raw_response.file_get(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        skyimagery = await async_client.skyimagery.get(
            "id",
        )
        assert_matches_type(SkyimageryFull, skyimagery, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.skyimagery.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = await response.parse()
        assert_matches_type(SkyimageryFull, skyimagery, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.skyimagery.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = await response.parse()
            assert_matches_type(SkyimageryFull, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.skyimagery.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        skyimagery = await async_client.skyimagery.queryhelp()
        assert skyimagery is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.skyimagery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = await response.parse()
        assert skyimagery is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.skyimagery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = await response.parse()
            assert skyimagery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        skyimagery = await async_client.skyimagery.tuple(
            columns="columns",
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SkyimageryTupleResponse, skyimagery, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.skyimagery.with_raw_response.tuple(
            columns="columns",
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = await response.parse()
        assert_matches_type(SkyimageryTupleResponse, skyimagery, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.skyimagery.with_streaming_response.tuple(
            columns="columns",
            exp_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = await response.parse()
            assert_matches_type(SkyimageryTupleResponse, skyimagery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        skyimagery = await async_client.skyimagery.upload_zip(
            file=b"raw file contents",
        )
        assert skyimagery is None

    @parametrize
    async def test_raw_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.skyimagery.with_raw_response.upload_zip(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skyimagery = await response.parse()
        assert skyimagery is None

    @parametrize
    async def test_streaming_response_upload_zip(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.skyimagery.with_streaming_response.upload_zip(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skyimagery = await response.parse()
            assert skyimagery is None

        assert cast(Any, response.is_closed) is True
