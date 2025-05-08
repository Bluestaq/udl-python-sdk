# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    GnssObservationsetListResponse,
    GnssObservationsetTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGnssObservationset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_observationset.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = response.parse()
        assert_matches_type(SyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.gnss_observationset.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = response.parse()
            assert_matches_type(SyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnss_observationset, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, gnss_observationset, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_observationset.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = response.parse()
        assert_matches_type(str, gnss_observationset, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.gnss_observationset.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = response.parse()
            assert_matches_type(str, gnss_observationset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )
        assert gnss_observationset is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_observationset.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = response.parse()
        assert gnss_observationset is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.gnss_observationset.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = response.parse()
            assert gnss_observationset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.queryhelp()
        assert gnss_observationset is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_observationset.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = response.parse()
        assert gnss_observationset is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.gnss_observationset.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = response.parse()
            assert gnss_observationset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_observationset.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = response.parse()
        assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.gnss_observationset.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = response.parse()
            assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        gnss_observationset = client.gnss_observationset.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )
        assert gnss_observationset is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.gnss_observationset.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = response.parse()
        assert gnss_observationset is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.gnss_observationset.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = response.parse()
            assert gnss_observationset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGnssObservationset:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_observationset.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = await response.parse()
        assert_matches_type(AsyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_observationset.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = await response.parse()
            assert_matches_type(AsyncOffsetPage[GnssObservationsetListResponse], gnss_observationset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, gnss_observationset, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, gnss_observationset, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_observationset.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = await response.parse()
        assert_matches_type(str, gnss_observationset, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_observationset.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = await response.parse()
            assert_matches_type(str, gnss_observationset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )
        assert gnss_observationset is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_observationset.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = await response.parse()
        assert gnss_observationset is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_observationset.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = await response.parse()
            assert gnss_observationset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.queryhelp()
        assert gnss_observationset is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_observationset.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = await response.parse()
        assert gnss_observationset is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_observationset.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = await response.parse()
            assert gnss_observationset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_observationset.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = await response.parse()
        assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_observationset.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = await response.parse()
            assert_matches_type(GnssObservationsetTupleResponse, gnss_observationset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        gnss_observationset = await async_client.gnss_observationset.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )
        assert gnss_observationset is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.gnss_observationset.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gnss_observationset = await response.parse()
        assert gnss_observationset is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.gnss_observationset.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2022-01-01T00:00:00.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gnss_observationset = await response.parse()
            assert gnss_observationset is None

        assert cast(Any, response.is_closed) is True
