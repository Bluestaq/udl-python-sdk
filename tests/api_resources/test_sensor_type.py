# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SensorTypeGetResponse,
    SensorTypeListResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSensorType:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sensor_type = client.sensor_type.list()
        assert_matches_type(SyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_type = client.sensor_type.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_type.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_type = response.parse()
        assert_matches_type(SyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sensor_type.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_type = response.parse()
            assert_matches_type(SyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sensor_type = client.sensor_type.get(
            id=0,
        )
        assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_type = client.sensor_type.get(
            id=0,
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_type.with_raw_response.get(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_type = response.parse()
        assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sensor_type.with_streaming_response.get(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_type = response.parse()
            assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sensor_type = client.sensor_type.queryhelp()
        assert sensor_type is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_type.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_type = response.parse()
        assert sensor_type is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sensor_type.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_type = response.parse()
            assert sensor_type is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSensorType:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_type = await async_client.sensor_type.list()
        assert_matches_type(AsyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_type = await async_client.sensor_type.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_type.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_type = await response.parse()
        assert_matches_type(AsyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_type.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_type = await response.parse()
            assert_matches_type(AsyncOffsetPage[SensorTypeListResponse], sensor_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_type = await async_client.sensor_type.get(
            id=0,
        )
        assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_type = await async_client.sensor_type.get(
            id=0,
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_type.with_raw_response.get(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_type = await response.parse()
        assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_type.with_streaming_response.get(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_type = await response.parse()
            assert_matches_type(SensorTypeGetResponse, sensor_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_type = await async_client.sensor_type.queryhelp()
        assert sensor_type is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_type.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_type = await response.parse()
        assert sensor_type is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_type.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_type = await response.parse()
            assert sensor_type is None

        assert cast(Any, response.is_closed) is True
