# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    NotificationListResponse,
    NotificationTupleResponse,
)
from unifieddatalibrary._utils import parse_date
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.notification import NotificationFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
        )
        assert notification is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
            id="NOTIFICATION-ID",
            origin="THIRD_PARTY_DATASOURCE",
            tags=["TAG1", "TAG2"],
        )
        assert notification is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.notification.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert notification is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.notification.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.notification.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.notification.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(SyncOffsetPage[NotificationListResponse], notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, notification, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, notification, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.notification.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(str, notification, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.notification.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(str, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_raw(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
        )
        assert notification is None

    @parametrize
    def test_method_create_raw_with_all_params(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
            msg_id="msgId",
            tags=["string"],
        )
        assert notification is None

    @parametrize
    def test_raw_response_create_raw(self, client: Unifieddatalibrary) -> None:
        response = client.notification.with_raw_response.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert notification is None

    @parametrize
    def test_streaming_response_create_raw(self, client: Unifieddatalibrary) -> None:
        with client.notification.with_streaming_response.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.get(
            id="id",
        )
        assert_matches_type(NotificationFull, notification, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(NotificationFull, notification, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.notification.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationFull, notification, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.notification.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationFull, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notification.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.queryhelp()
        assert notification is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.notification.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert notification is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.notification.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(NotificationTupleResponse, notification, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        notification = client.notification.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(NotificationTupleResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.notification.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationTupleResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.notification.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationTupleResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotification:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
        )
        assert notification is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
            id="NOTIFICATION-ID",
            origin="THIRD_PARTY_DATASOURCE",
            tags=["TAG1", "TAG2"],
        )
        assert notification is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.notification.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert notification is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.notification.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_body="msgBody",
            msg_type="msgType",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.notification.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.notification.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(AsyncOffsetPage[NotificationListResponse], notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, notification, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, notification, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.notification.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(str, notification, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.notification.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(str, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_raw(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
        )
        assert notification is None

    @parametrize
    async def test_method_create_raw_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
            msg_id="msgId",
            tags=["string"],
        )
        assert notification is None

    @parametrize
    async def test_raw_response_create_raw(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.notification.with_raw_response.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert notification is None

    @parametrize
    async def test_streaming_response_create_raw(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.notification.with_streaming_response.create_raw(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            msg_type="msgType",
            origin="origin",
            source="source",
            body='{ "Alert": "Warning",  "Code": 12345 }',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.get(
            id="id",
        )
        assert_matches_type(NotificationFull, notification, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(NotificationFull, notification, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.notification.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationFull, notification, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.notification.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationFull, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notification.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.queryhelp()
        assert notification is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.notification.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert notification is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.notification.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(NotificationTupleResponse, notification, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        notification = await async_client.notification.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(NotificationTupleResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.notification.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationTupleResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.notification.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationTupleResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True
