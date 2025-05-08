# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.ephemeris import (
    AttitudeDataAbridged,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttitudeData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        attitude_data = client.ephemeris.attitude_data.list(
            as_id="asId",
        )
        assert_matches_type(SyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_data = client.ephemeris.attitude_data.list(
            as_id="asId",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris.attitude_data.with_raw_response.list(
            as_id="asId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = response.parse()
        assert_matches_type(SyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris.attitude_data.with_streaming_response.list(
            as_id="asId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = response.parse()
            assert_matches_type(SyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        attitude_data = client.ephemeris.attitude_data.count(
            as_id="asId",
        )
        assert_matches_type(str, attitude_data, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_data = client.ephemeris.attitude_data.count(
            as_id="asId",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, attitude_data, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.ephemeris.attitude_data.with_raw_response.count(
            as_id="asId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = response.parse()
        assert_matches_type(str, attitude_data, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.ephemeris.attitude_data.with_streaming_response.count(
            as_id="asId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = response.parse()
            assert_matches_type(str, attitude_data, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAttitudeData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_data = await async_client.ephemeris.attitude_data.list(
            as_id="asId",
        )
        assert_matches_type(AsyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_data = await async_client.ephemeris.attitude_data.list(
            as_id="asId",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris.attitude_data.with_raw_response.list(
            as_id="asId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = await response.parse()
        assert_matches_type(AsyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris.attitude_data.with_streaming_response.list(
            as_id="asId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = await response.parse()
            assert_matches_type(AsyncOffsetPage[AttitudeDataAbridged], attitude_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_data = await async_client.ephemeris.attitude_data.count(
            as_id="asId",
        )
        assert_matches_type(str, attitude_data, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_data = await async_client.ephemeris.attitude_data.count(
            as_id="asId",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, attitude_data, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.ephemeris.attitude_data.with_raw_response.count(
            as_id="asId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = await response.parse()
        assert_matches_type(str, attitude_data, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.ephemeris.attitude_data.with_streaming_response.count(
            as_id="asId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = await response.parse()
            assert_matches_type(str, attitude_data, path=["response"])

        assert cast(Any, response.is_closed) is True
