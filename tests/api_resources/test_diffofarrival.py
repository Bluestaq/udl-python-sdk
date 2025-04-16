# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    DiffofarrivalTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.types.tdoa_fdoa import DiffofarrivalFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiffofarrival:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.diffofarrival.retrieve(
            "id",
        )
        assert_matches_type(DiffofarrivalFull, diffofarrival, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.diffofarrival.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert_matches_type(DiffofarrivalFull, diffofarrival, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.diffofarrival.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert_matches_type(DiffofarrivalFull, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.diffofarrival.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.diffofarrival.queryhelp()
        assert diffofarrival is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.diffofarrival.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert diffofarrival is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.diffofarrival.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.diffofarrival.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DiffofarrivalTupleResponse, diffofarrival, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.diffofarrival.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert_matches_type(DiffofarrivalTupleResponse, diffofarrival, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.diffofarrival.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert_matches_type(DiffofarrivalTupleResponse, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        diffofarrival = client.diffofarrival.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert diffofarrival is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.diffofarrival.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = response.parse()
        assert diffofarrival is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.diffofarrival.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDiffofarrival:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.diffofarrival.retrieve(
            "id",
        )
        assert_matches_type(DiffofarrivalFull, diffofarrival, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diffofarrival.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert_matches_type(DiffofarrivalFull, diffofarrival, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diffofarrival.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert_matches_type(DiffofarrivalFull, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.diffofarrival.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.diffofarrival.queryhelp()
        assert diffofarrival is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diffofarrival.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert diffofarrival is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diffofarrival.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.diffofarrival.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DiffofarrivalTupleResponse, diffofarrival, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diffofarrival.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert_matches_type(DiffofarrivalTupleResponse, diffofarrival, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diffofarrival.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert_matches_type(DiffofarrivalTupleResponse, diffofarrival, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        diffofarrival = await async_client.diffofarrival.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert diffofarrival is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.diffofarrival.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        diffofarrival = await response.parse()
        assert diffofarrival is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.diffofarrival.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            diffofarrival = await response.parse()
            assert diffofarrival is None

        assert cast(Any, response.is_closed) is True
