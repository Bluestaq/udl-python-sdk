# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        cot = client.cots.create(
            lat=0,
            lon=0,
        )
        assert cot is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        cot = client.cots.create(
            lat=0,
            lon=0,
            alt=0,
            call_signs=["string"],
            ce=0,
            cot_chat_data={
                "chat_msg": "chatMsg",
                "chat_room": "chatRoom",
                "chat_sender_call_sign": "chatSenderCallSign",
            },
            cot_position_data={
                "call_sign": "callSign",
                "team": "team",
                "team_role": "teamRole",
            },
            groups=["string"],
            how="how",
            le=0,
            sender_uid="senderUid",
            stale=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            uids=["string"],
        )
        assert cot is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.cots.with_raw_response.create(
            lat=0,
            lon=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cot = response.parse()
        assert cot is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.cots.with_streaming_response.create(
            lat=0,
            lon=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cot = response.parse()
            assert cot is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        cot = await async_client.cots.create(
            lat=0,
            lon=0,
        )
        assert cot is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        cot = await async_client.cots.create(
            lat=0,
            lon=0,
            alt=0,
            call_signs=["string"],
            ce=0,
            cot_chat_data={
                "chat_msg": "chatMsg",
                "chat_room": "chatRoom",
                "chat_sender_call_sign": "chatSenderCallSign",
            },
            cot_position_data={
                "call_sign": "callSign",
                "team": "team",
                "team_role": "teamRole",
            },
            groups=["string"],
            how="how",
            le=0,
            sender_uid="senderUid",
            stale=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="type",
            uids=["string"],
        )
        assert cot is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.cots.with_raw_response.create(
            lat=0,
            lon=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cot = await response.parse()
        assert cot is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.cots.with_streaming_response.create(
            lat=0,
            lon=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cot = await response.parse()
            assert cot is None

        assert cast(Any, response.is_closed) is True
