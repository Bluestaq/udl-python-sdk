# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.observations import (
    MonoradarListResponse,
    MonoradarTupleResponse,
    MonoradarQueryhelpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonoradar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.observations.monoradar.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = response.parse()
        assert_matches_type(SyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.observations.monoradar.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = response.parse()
            assert_matches_type(SyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, monoradar, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, monoradar, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.observations.monoradar.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = response.parse()
        assert_matches_type(str, monoradar, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.observations.monoradar.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = response.parse()
            assert_matches_type(str, monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert monoradar is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.observations.monoradar.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = response.parse()
        assert monoradar is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.observations.monoradar.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = response.parse()
            assert monoradar is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.queryhelp()
        assert_matches_type(MonoradarQueryhelpResponse, monoradar, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.observations.monoradar.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = response.parse()
        assert_matches_type(MonoradarQueryhelpResponse, monoradar, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.observations.monoradar.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = response.parse()
            assert_matches_type(MonoradarQueryhelpResponse, monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.observations.monoradar.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = response.parse()
        assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.observations.monoradar.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = response.parse()
            assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        monoradar = client.observations.monoradar.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert monoradar is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.observations.monoradar.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = response.parse()
        assert monoradar is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.observations.monoradar.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = response.parse()
            assert monoradar is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMonoradar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.monoradar.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = await response.parse()
        assert_matches_type(AsyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.monoradar.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = await response.parse()
            assert_matches_type(AsyncOffsetPage[MonoradarListResponse], monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, monoradar, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, monoradar, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.monoradar.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = await response.parse()
        assert_matches_type(str, monoradar, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.monoradar.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = await response.parse()
            assert_matches_type(str, monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert monoradar is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.monoradar.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = await response.parse()
        assert monoradar is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.monoradar.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = await response.parse()
            assert monoradar is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.queryhelp()
        assert_matches_type(MonoradarQueryhelpResponse, monoradar, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.monoradar.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = await response.parse()
        assert_matches_type(MonoradarQueryhelpResponse, monoradar, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.monoradar.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = await response.parse()
            assert_matches_type(MonoradarQueryhelpResponse, monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.monoradar.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = await response.parse()
        assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.monoradar.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = await response.parse()
            assert_matches_type(MonoradarTupleResponse, monoradar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        monoradar = await async_client.observations.monoradar.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert monoradar is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.monoradar.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monoradar = await response.parse()
        assert monoradar is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.monoradar.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msgfmt": "CAT48",
                    "msgts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "msgtyp": "BCN",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monoradar = await response.parse()
            assert monoradar is None

        assert cast(Any, response.is_closed) is True
