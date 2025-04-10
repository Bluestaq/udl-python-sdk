# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    MtiListResponse,
    MtiTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMti:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        mti = client.mti.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(MtiListResponse, mti, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.mti.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = response.parse()
        assert_matches_type(MtiListResponse, mti, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.mti.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = response.parse()
            assert_matches_type(MtiListResponse, mti, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        mti = client.mti.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, mti, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.mti.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = response.parse()
        assert_matches_type(str, mti, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.mti.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = response.parse()
            assert_matches_type(str, mti, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        mti = client.mti.create_bulk()
        assert mti is None

    @parametrize
    def test_method_create_bulk_with_all_params(self, client: Unifieddatalibrary) -> None:
        mti = client.mti.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "MTI-ID",
                    "dwells": [
                        {
                            "d10": 1.2,
                            "d11": 1.2,
                            "d12": 12,
                            "d13": 12,
                            "d14": 12,
                            "d15": 1.2,
                            "d16": 12,
                            "d17": 2,
                            "d18": 2,
                            "d19": 12,
                            "d2": 12,
                            "d20": 12,
                            "d21": 1.2,
                            "d22": 12.23,
                            "d23": 12.23,
                            "d24": 12.23,
                            "d25": 12.23,
                            "d26": 12.23,
                            "d27": 12.23,
                            "d28": 12.23,
                            "d29": 12.23,
                            "d3": 12,
                            "d30": 12.23,
                            "d31": 1,
                            "d32": [
                                {
                                    "d32_1": 2,
                                    "d32_10": "vehicle",
                                    "d32_11": 90,
                                    "d32_12": 2,
                                    "d32_13": 2,
                                    "d32_14": 2,
                                    "d32_15": 2,
                                    "d32_16": 2,
                                    "d32_17": 1234567890,
                                    "d32_18": 98,
                                    "d32_2": 20.23,
                                    "d32_3": 20.23,
                                    "d32_4": 2,
                                    "d32_5": 2,
                                    "d32_6": 2,
                                    "d32_7": 2,
                                    "d32_8": 2,
                                    "d32_9": 17,
                                }
                            ],
                            "d4": False,
                            "d5": 12,
                            "d6": 1234567890,
                            "d7": 1.2,
                            "d8": 12,
                            "d9": 12,
                            "dwellts": parse_datetime("2018-01-01T16:00:00.123Z"),
                        }
                    ],
                    "free_texts": [
                        {
                            "f1": "ORIGINATOR",
                            "f2": "RECIPIENT",
                            "f3": "TEXT",
                        }
                    ],
                    "hrrs": [
                        {
                            "h10": 1,
                            "h11": 12.23,
                            "h12": 12.23,
                            "h13": 12.23,
                            "h14": 12.23,
                            "h15": 12.23,
                            "h16": "TABLE",
                            "h17": "TABLE",
                            "h18": "TABLE",
                            "h19": 12.23,
                            "h2": 12,
                            "h20": 117,
                            "h21": 1,
                            "h22": 1,
                            "h23": "FIELD",
                            "h24": "FLAG",
                            "h27": 1,
                            "h28": 1234567890,
                            "h29": 1,
                            "h3": 12,
                            "h30": 22,
                            "h31": 55,
                            "h32": [
                                {
                                    "h32_1": 1,
                                    "h32_2": 1,
                                    "h32_3": 1,
                                    "h32_4": 1,
                                }
                            ],
                            "h4": True,
                            "h5": 12,
                            "h6": 12,
                            "h7": 12,
                            "h8": 12,
                            "h9": 1,
                        }
                    ],
                    "job_defs": [
                        {
                            "j1": 1234567890,
                            "j10": 10.23,
                            "j11": 10.23,
                            "j12": 10.23,
                            "j13": 10.23,
                            "j14": "MODE",
                            "j15": 100,
                            "j16": 100,
                            "j17": 100,
                            "j18": 100,
                            "j19": 10,
                            "j2": "TYPE",
                            "j20": 10,
                            "j21": 10,
                            "j22": 10.23,
                            "j23": 10,
                            "j24": 10,
                            "j25": 10,
                            "j26": 10,
                            "j27": "MODEL",
                            "j28": "MODEL",
                            "j3": "J3-ID",
                            "j4": 3,
                            "j5": 1,
                            "j6": 10.23,
                            "j7": 10.23,
                            "j8": 10.23,
                            "j9": 10.23,
                        }
                    ],
                    "job_requests": [
                        {
                            "job_req_est": parse_datetime("2018-01-01T16:00:00.123456Z"),
                            "r1": "REQUESTER",
                            "r10": 10.23,
                            "r11": 10.23,
                            "r12": "MODE",
                            "r13": 10,
                            "r14": 100,
                            "r2": "IDENTIFIER",
                            "r21": 10,
                            "r22": 10,
                            "r23": 100,
                            "r24": "TYPE",
                            "r25": "VARIANT",
                            "r26": True,
                            "r3": 15,
                            "r4": 10.23,
                            "r5": 10.23,
                            "r6": 10.23,
                            "r7": 10.23,
                            "r8": 10.23,
                            "r9": 10.23,
                        }
                    ],
                    "missions": [
                        {
                            "m1": "M1-ID",
                            "m2": "M2-ID",
                            "m3": "PLATFORM",
                            "m4": "IDENT",
                            "msn_ref_ts": parse_date("2018-01-01"),
                        }
                    ],
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "p10": 45,
                    "p3": "NATIONALITY",
                    "p6": "MARKING",
                    "p7": "INDICATOR",
                    "p8": "P8-ID",
                    "p9": 45,
                    "platform_locs": [
                        {
                            "l1": 1234567890,
                            "l2": 45.23,
                            "l3": 45.23,
                            "l4": 45,
                            "l5": 45.23,
                            "l6": 50,
                            "l7": 82,
                            "platlocts": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    ],
                }
            ],
        )
        assert mti is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.mti.with_raw_response.create_bulk()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = response.parse()
        assert mti is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.mti.with_streaming_response.create_bulk() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = response.parse()
            assert mti is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk_v2(self, client: Unifieddatalibrary) -> None:
        mti = client.mti.create_bulk_v2(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert mti is None

    @parametrize
    def test_raw_response_create_bulk_v2(self, client: Unifieddatalibrary) -> None:
        response = client.mti.with_raw_response.create_bulk_v2(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = response.parse()
        assert mti is None

    @parametrize
    def test_streaming_response_create_bulk_v2(self, client: Unifieddatalibrary) -> None:
        with client.mti.with_streaming_response.create_bulk_v2(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = response.parse()
            assert mti is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        mti = client.mti.queryhelp()
        assert mti is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.mti.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = response.parse()
        assert mti is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.mti.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = response.parse()
            assert mti is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        mti = client.mti.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(MtiTupleResponse, mti, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.mti.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = response.parse()
        assert_matches_type(MtiTupleResponse, mti, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.mti.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = response.parse()
            assert_matches_type(MtiTupleResponse, mti, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMti:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        mti = await async_client.mti.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(MtiListResponse, mti, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mti.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = await response.parse()
        assert_matches_type(MtiListResponse, mti, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mti.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = await response.parse()
            assert_matches_type(MtiListResponse, mti, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        mti = await async_client.mti.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, mti, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mti.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = await response.parse()
        assert_matches_type(str, mti, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mti.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = await response.parse()
            assert_matches_type(str, mti, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        mti = await async_client.mti.create_bulk()
        assert mti is None

    @parametrize
    async def test_method_create_bulk_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        mti = await async_client.mti.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "id": "MTI-ID",
                    "dwells": [
                        {
                            "d10": 1.2,
                            "d11": 1.2,
                            "d12": 12,
                            "d13": 12,
                            "d14": 12,
                            "d15": 1.2,
                            "d16": 12,
                            "d17": 2,
                            "d18": 2,
                            "d19": 12,
                            "d2": 12,
                            "d20": 12,
                            "d21": 1.2,
                            "d22": 12.23,
                            "d23": 12.23,
                            "d24": 12.23,
                            "d25": 12.23,
                            "d26": 12.23,
                            "d27": 12.23,
                            "d28": 12.23,
                            "d29": 12.23,
                            "d3": 12,
                            "d30": 12.23,
                            "d31": 1,
                            "d32": [
                                {
                                    "d32_1": 2,
                                    "d32_10": "vehicle",
                                    "d32_11": 90,
                                    "d32_12": 2,
                                    "d32_13": 2,
                                    "d32_14": 2,
                                    "d32_15": 2,
                                    "d32_16": 2,
                                    "d32_17": 1234567890,
                                    "d32_18": 98,
                                    "d32_2": 20.23,
                                    "d32_3": 20.23,
                                    "d32_4": 2,
                                    "d32_5": 2,
                                    "d32_6": 2,
                                    "d32_7": 2,
                                    "d32_8": 2,
                                    "d32_9": 17,
                                }
                            ],
                            "d4": False,
                            "d5": 12,
                            "d6": 1234567890,
                            "d7": 1.2,
                            "d8": 12,
                            "d9": 12,
                            "dwellts": parse_datetime("2018-01-01T16:00:00.123Z"),
                        }
                    ],
                    "free_texts": [
                        {
                            "f1": "ORIGINATOR",
                            "f2": "RECIPIENT",
                            "f3": "TEXT",
                        }
                    ],
                    "hrrs": [
                        {
                            "h10": 1,
                            "h11": 12.23,
                            "h12": 12.23,
                            "h13": 12.23,
                            "h14": 12.23,
                            "h15": 12.23,
                            "h16": "TABLE",
                            "h17": "TABLE",
                            "h18": "TABLE",
                            "h19": 12.23,
                            "h2": 12,
                            "h20": 117,
                            "h21": 1,
                            "h22": 1,
                            "h23": "FIELD",
                            "h24": "FLAG",
                            "h27": 1,
                            "h28": 1234567890,
                            "h29": 1,
                            "h3": 12,
                            "h30": 22,
                            "h31": 55,
                            "h32": [
                                {
                                    "h32_1": 1,
                                    "h32_2": 1,
                                    "h32_3": 1,
                                    "h32_4": 1,
                                }
                            ],
                            "h4": True,
                            "h5": 12,
                            "h6": 12,
                            "h7": 12,
                            "h8": 12,
                            "h9": 1,
                        }
                    ],
                    "job_defs": [
                        {
                            "j1": 1234567890,
                            "j10": 10.23,
                            "j11": 10.23,
                            "j12": 10.23,
                            "j13": 10.23,
                            "j14": "MODE",
                            "j15": 100,
                            "j16": 100,
                            "j17": 100,
                            "j18": 100,
                            "j19": 10,
                            "j2": "TYPE",
                            "j20": 10,
                            "j21": 10,
                            "j22": 10.23,
                            "j23": 10,
                            "j24": 10,
                            "j25": 10,
                            "j26": 10,
                            "j27": "MODEL",
                            "j28": "MODEL",
                            "j3": "J3-ID",
                            "j4": 3,
                            "j5": 1,
                            "j6": 10.23,
                            "j7": 10.23,
                            "j8": 10.23,
                            "j9": 10.23,
                        }
                    ],
                    "job_requests": [
                        {
                            "job_req_est": parse_datetime("2018-01-01T16:00:00.123456Z"),
                            "r1": "REQUESTER",
                            "r10": 10.23,
                            "r11": 10.23,
                            "r12": "MODE",
                            "r13": 10,
                            "r14": 100,
                            "r2": "IDENTIFIER",
                            "r21": 10,
                            "r22": 10,
                            "r23": 100,
                            "r24": "TYPE",
                            "r25": "VARIANT",
                            "r26": True,
                            "r3": 15,
                            "r4": 10.23,
                            "r5": 10.23,
                            "r6": 10.23,
                            "r7": 10.23,
                            "r8": 10.23,
                            "r9": 10.23,
                        }
                    ],
                    "missions": [
                        {
                            "m1": "M1-ID",
                            "m2": "M2-ID",
                            "m3": "PLATFORM",
                            "m4": "IDENT",
                            "msn_ref_ts": parse_date("2018-01-01"),
                        }
                    ],
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "p10": 45,
                    "p3": "NATIONALITY",
                    "p6": "MARKING",
                    "p7": "INDICATOR",
                    "p8": "P8-ID",
                    "p9": 45,
                    "platform_locs": [
                        {
                            "l1": 1234567890,
                            "l2": 45.23,
                            "l3": 45.23,
                            "l4": 45,
                            "l5": 45.23,
                            "l6": 50,
                            "l7": 82,
                            "platlocts": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    ],
                }
            ],
        )
        assert mti is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mti.with_raw_response.create_bulk()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = await response.parse()
        assert mti is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mti.with_streaming_response.create_bulk() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = await response.parse()
            assert mti is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk_v2(self, async_client: AsyncUnifieddatalibrary) -> None:
        mti = await async_client.mti.create_bulk_v2(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )
        assert mti is None

    @parametrize
    async def test_raw_response_create_bulk_v2(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mti.with_raw_response.create_bulk_v2(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = await response.parse()
        assert mti is None

    @parametrize
    async def test_streaming_response_create_bulk_v2(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mti.with_streaming_response.create_bulk_v2(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = await response.parse()
            assert mti is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        mti = await async_client.mti.queryhelp()
        assert mti is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mti.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = await response.parse()
        assert mti is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mti.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = await response.parse()
            assert mti is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        mti = await async_client.mti.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(MtiTupleResponse, mti, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.mti.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mti = await response.parse()
        assert_matches_type(MtiTupleResponse, mti, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.mti.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mti = await response.parse()
            assert_matches_type(MtiTupleResponse, mti, path=["response"])

        assert cast(Any, response.is_closed) is True
