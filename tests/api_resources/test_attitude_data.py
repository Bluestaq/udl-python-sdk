# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import AttitudeDataTupleResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttitudeData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        attitude_data = client.attitude_data.query_help()
        assert attitude_data is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_data.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = response.parse()
        assert attitude_data is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.attitude_data.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = response.parse()
            assert attitude_data is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        attitude_data = client.attitude_data.tuple(
            as_id="asId",
            columns="columns",
        )
        assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        attitude_data = client.attitude_data.tuple(
            as_id="asId",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.attitude_data.with_raw_response.tuple(
            as_id="asId",
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = response.parse()
        assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.attitude_data.with_streaming_response.tuple(
            as_id="asId",
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = response.parse()
            assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAttitudeData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_data = await async_client.attitude_data.query_help()
        assert attitude_data is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_data.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = await response.parse()
        assert attitude_data is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_data.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = await response.parse()
            assert attitude_data is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_data = await async_client.attitude_data.tuple(
            as_id="asId",
            columns="columns",
        )
        assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        attitude_data = await async_client.attitude_data.tuple(
            as_id="asId",
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.attitude_data.with_raw_response.tuple(
            as_id="asId",
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attitude_data = await response.parse()
        assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.attitude_data.with_streaming_response.tuple(
            as_id="asId",
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attitude_data = await response.parse()
            assert_matches_type(AttitudeDataTupleResponse, attitude_data, path=["response"])

        assert cast(Any, response.is_closed) is True
