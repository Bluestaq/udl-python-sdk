# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    TrackdetailListResponse,
    TrackdetailTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrackdetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        trackdetail = client.trackdetails.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackdetailListResponse, trackdetail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.trackdetails.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = response.parse()
        assert_matches_type(TrackdetailListResponse, trackdetail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.trackdetails.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = response.parse()
            assert_matches_type(TrackdetailListResponse, trackdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        trackdetail = client.trackdetails.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, trackdetail, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.trackdetails.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = response.parse()
        assert_matches_type(str, trackdetail, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.trackdetails.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = response.parse()
            assert_matches_type(str, trackdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        trackdetail = client.trackdetails.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )
        assert trackdetail is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.trackdetails.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = response.parse()
        assert trackdetail is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.trackdetails.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = response.parse()
            assert trackdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        trackdetail = client.trackdetails.queryhelp()
        assert trackdetail is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.trackdetails.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = response.parse()
        assert trackdetail is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.trackdetails.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = response.parse()
            assert trackdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        trackdetail = client.trackdetails.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackdetailTupleResponse, trackdetail, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.trackdetails.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = response.parse()
        assert_matches_type(TrackdetailTupleResponse, trackdetail, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.trackdetails.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = response.parse()
            assert_matches_type(TrackdetailTupleResponse, trackdetail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrackdetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackdetail = await async_client.trackdetails.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackdetailListResponse, trackdetail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackdetails.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = await response.parse()
        assert_matches_type(TrackdetailListResponse, trackdetail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackdetails.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = await response.parse()
            assert_matches_type(TrackdetailListResponse, trackdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackdetail = await async_client.trackdetails.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, trackdetail, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackdetails.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = await response.parse()
        assert_matches_type(str, trackdetail, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackdetails.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = await response.parse()
            assert_matches_type(str, trackdetail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackdetail = await async_client.trackdetails.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )
        assert trackdetail is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackdetails.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = await response.parse()
        assert trackdetail is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackdetails.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "lat": 19.88550102,
                    "lon": 46.74596844,
                    "source": "Bluestaq",
                    "ts": parse_datetime("2021-02-25T12:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = await response.parse()
            assert trackdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackdetail = await async_client.trackdetails.queryhelp()
        assert trackdetail is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackdetails.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = await response.parse()
        assert trackdetail is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackdetails.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = await response.parse()
            assert trackdetail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        trackdetail = await async_client.trackdetails.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrackdetailTupleResponse, trackdetail, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.trackdetails.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trackdetail = await response.parse()
        assert_matches_type(TrackdetailTupleResponse, trackdetail, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.trackdetails.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trackdetail = await response.parse()
            assert_matches_type(TrackdetailTupleResponse, trackdetail, path=["response"])

        assert cast(Any, response.is_closed) is True
