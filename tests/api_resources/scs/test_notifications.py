# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types.scs import NotificationListResponse
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        notification = client.scs.notifications.list(
            offset="offset",
        )
        assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        notification = client.scs.notifications.list(
            offset="offset",
            first_result=0,
            max_results=0,
            path="path",
        )
        assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.scs.notifications.with_raw_response.list(
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.scs.notifications.with_streaming_response.list(
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            client.scs.notifications.with_raw_response.list(
                offset="",
            )


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.scs.notifications.list(
            offset="offset",
        )
        assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.scs.notifications.list(
            offset="offset",
            first_result=0,
            max_results=0,
            path="path",
        )
        assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.scs.notifications.with_raw_response.list(
            offset="offset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.scs.notifications.with_streaming_response.list(
            offset="offset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset` but received ''"):
            await async_client.scs.notifications.with_raw_response.list(
                offset="",
            )
