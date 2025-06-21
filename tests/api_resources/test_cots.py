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
            lat=45.23,
            lon=45.23,
        )
        assert cot is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        cot = client.cots.create(
            lat=45.23,
            lon=45.23,
            alt=5.23,
            call_signs=["string"],
            ce=10.23,
            cot_chat_data={
                "chat_msg": "Mission is go",
                "chat_room": "All Chat Rooms",
                "chat_sender_call_sign": "Pebble",
            },
            cot_position_data={
                "call_sign": "POI_NAME",
                "team": "Description of the object",
                "team_role": "Team Member",
            },
            groups=["string"],
            how="h-e",
            le=10.23,
            sender_uid="POI-ID",
            stale=parse_datetime("2020-01-01T16:00:00.123456Z"),
            start=parse_datetime("2020-01-01T16:00:00.123456Z"),
            type="a-h-G",
            uids=["string"],
        )
        assert cot is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.cots.with_raw_response.create(
            lat=45.23,
            lon=45.23,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cot = response.parse()
        assert cot is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.cots.with_streaming_response.create(
            lat=45.23,
            lon=45.23,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cot = response.parse()
            assert cot is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        cot = await async_client.cots.create(
            lat=45.23,
            lon=45.23,
        )
        assert cot is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        cot = await async_client.cots.create(
            lat=45.23,
            lon=45.23,
            alt=5.23,
            call_signs=["string"],
            ce=10.23,
            cot_chat_data={
                "chat_msg": "Mission is go",
                "chat_room": "All Chat Rooms",
                "chat_sender_call_sign": "Pebble",
            },
            cot_position_data={
                "call_sign": "POI_NAME",
                "team": "Description of the object",
                "team_role": "Team Member",
            },
            groups=["string"],
            how="h-e",
            le=10.23,
            sender_uid="POI-ID",
            stale=parse_datetime("2020-01-01T16:00:00.123456Z"),
            start=parse_datetime("2020-01-01T16:00:00.123456Z"),
            type="a-h-G",
            uids=["string"],
        )
        assert cot is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.cots.with_raw_response.create(
            lat=45.23,
            lon=45.23,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cot = await response.parse()
        assert cot is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.cots.with_streaming_response.create(
            lat=45.23,
            lon=45.23,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cot = await response.parse()
            assert cot is None

        assert cast(Any, response.is_closed) is True
