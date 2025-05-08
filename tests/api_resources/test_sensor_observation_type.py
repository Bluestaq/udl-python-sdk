# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SensorObservationTypeGetResponse,
    SensorObservationTypeListResponse,
)
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSensorObservationType:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        sensor_observation_type = client.sensor_observation_type.list()
        assert_matches_type(
            SyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_observation_type = client.sensor_observation_type.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            SyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_observation_type.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_observation_type = response.parse()
        assert_matches_type(
            SyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.sensor_observation_type.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_observation_type = response.parse()
            assert_matches_type(
                SyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        sensor_observation_type = client.sensor_observation_type.get(
            id="id",
        )
        assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        sensor_observation_type = client.sensor_observation_type.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_observation_type.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_observation_type = response.parse()
        assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.sensor_observation_type.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_observation_type = response.parse()
            assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sensor_observation_type.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        sensor_observation_type = client.sensor_observation_type.queryhelp()
        assert sensor_observation_type is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.sensor_observation_type.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_observation_type = response.parse()
        assert sensor_observation_type is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.sensor_observation_type.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_observation_type = response.parse()
            assert sensor_observation_type is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSensorObservationType:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_observation_type = await async_client.sensor_observation_type.list()
        assert_matches_type(
            AsyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_observation_type = await async_client.sensor_observation_type.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(
            AsyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_observation_type.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_observation_type = await response.parse()
        assert_matches_type(
            AsyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_observation_type.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_observation_type = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[SensorObservationTypeListResponse], sensor_observation_type, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_observation_type = await async_client.sensor_observation_type.get(
            id="id",
        )
        assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_observation_type = await async_client.sensor_observation_type.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_observation_type.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_observation_type = await response.parse()
        assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_observation_type.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_observation_type = await response.parse()
            assert_matches_type(SensorObservationTypeGetResponse, sensor_observation_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sensor_observation_type.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        sensor_observation_type = await async_client.sensor_observation_type.queryhelp()
        assert sensor_observation_type is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.sensor_observation_type.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor_observation_type = await response.parse()
        assert sensor_observation_type is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.sensor_observation_type.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor_observation_type = await response.parse()
            assert sensor_observation_type is None

        assert cast(Any, response.is_closed) is True
