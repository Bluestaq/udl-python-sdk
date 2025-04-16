# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    IonoobservationListResponse,
    IonoobservationTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIonoobservation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        ionoobservation = client.ionoobservation.list(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(IonoobservationListResponse, ionoobservation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ionoobservation.with_raw_response.list(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = response.parse()
        assert_matches_type(IonoobservationListResponse, ionoobservation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ionoobservation.with_streaming_response.list(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = response.parse()
            assert_matches_type(IonoobservationListResponse, ionoobservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        ionoobservation = client.ionoobservation.count(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ionoobservation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.ionoobservation.with_raw_response.count(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = response.parse()
        assert_matches_type(str, ionoobservation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.ionoobservation.with_streaming_response.count(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = response.parse()
            assert_matches_type(str, ionoobservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        ionoobservation = client.ionoobservation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )
        assert ionoobservation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.ionoobservation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = response.parse()
        assert ionoobservation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.ionoobservation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = response.parse()
            assert ionoobservation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        ionoobservation = client.ionoobservation.queryhelp()
        assert ionoobservation is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.ionoobservation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = response.parse()
        assert ionoobservation is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.ionoobservation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = response.parse()
            assert ionoobservation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        ionoobservation = client.ionoobservation.tuple(
            columns="columns",
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(IonoobservationTupleResponse, ionoobservation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.ionoobservation.with_raw_response.tuple(
            columns="columns",
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = response.parse()
        assert_matches_type(IonoobservationTupleResponse, ionoobservation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.ionoobservation.with_streaming_response.tuple(
            columns="columns",
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = response.parse()
            assert_matches_type(IonoobservationTupleResponse, ionoobservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        ionoobservation = client.ionoobservation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )
        assert ionoobservation is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.ionoobservation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = response.parse()
        assert ionoobservation is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.ionoobservation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = response.parse()
            assert ionoobservation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncIonoobservation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        ionoobservation = await async_client.ionoobservation.list(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(IonoobservationListResponse, ionoobservation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ionoobservation.with_raw_response.list(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = await response.parse()
        assert_matches_type(IonoobservationListResponse, ionoobservation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ionoobservation.with_streaming_response.list(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = await response.parse()
            assert_matches_type(IonoobservationListResponse, ionoobservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        ionoobservation = await async_client.ionoobservation.count(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, ionoobservation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ionoobservation.with_raw_response.count(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = await response.parse()
        assert_matches_type(str, ionoobservation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ionoobservation.with_streaming_response.count(
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = await response.parse()
            assert_matches_type(str, ionoobservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        ionoobservation = await async_client.ionoobservation.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )
        assert ionoobservation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ionoobservation.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = await response.parse()
        assert ionoobservation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ionoobservation.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = await response.parse()
            assert ionoobservation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        ionoobservation = await async_client.ionoobservation.queryhelp()
        assert ionoobservation is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ionoobservation.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = await response.parse()
        assert ionoobservation is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ionoobservation.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = await response.parse()
            assert ionoobservation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        ionoobservation = await async_client.ionoobservation.tuple(
            columns="columns",
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(IonoobservationTupleResponse, ionoobservation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ionoobservation.with_raw_response.tuple(
            columns="columns",
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = await response.parse()
        assert_matches_type(IonoobservationTupleResponse, ionoobservation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ionoobservation.with_streaming_response.tuple(
            columns="columns",
            start_time_utc=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = await response.parse()
            assert_matches_type(IonoobservationTupleResponse, ionoobservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        ionoobservation = await async_client.ionoobservation.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )
        assert ionoobservation is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ionoobservation.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ionoobservation = await response.parse()
        assert ionoobservation is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ionoobservation.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time_utc": parse_datetime("2021-01-01T01:01:01.123456Z"),
                    "station_id": "STATION-ID",
                    "system": "Example hardware type",
                    "system_info": "Example settings",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ionoobservation = await response.parse()
            assert ionoobservation is None

        assert cast(Any, response.is_closed) is True
