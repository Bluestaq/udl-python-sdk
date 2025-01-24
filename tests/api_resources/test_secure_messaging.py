# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    TopicDetails,
    SecureMessagingListTopicsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecureMessaging:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_describe_topic(self, client: Unifieddatalibrary) -> None:
        secure_messaging = client.secure_messaging.describe_topic(
            topic_1="topic",
            topic_2="topic",
        )
        assert_matches_type(TopicDetails, secure_messaging, path=["response"])

    @parametrize
    def test_raw_response_describe_topic(self, client: Unifieddatalibrary) -> None:
        response = client.secure_messaging.with_raw_response.describe_topic(
            topic_1="topic",
            topic_2="topic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = response.parse()
        assert_matches_type(TopicDetails, secure_messaging, path=["response"])

    @parametrize
    def test_streaming_response_describe_topic(self, client: Unifieddatalibrary) -> None:
        with client.secure_messaging.with_streaming_response.describe_topic(
            topic_1="topic",
            topic_2="topic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = response.parse()
            assert_matches_type(TopicDetails, secure_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_describe_topic(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_1` but received ''"):
            client.secure_messaging.with_raw_response.describe_topic(
                topic_1="",
                topic_2="",
            )

    @parametrize
    def test_method_get_latest_offset(self, client: Unifieddatalibrary) -> None:
        secure_messaging = client.secure_messaging.get_latest_offset(
            topic_1="topic",
            topic_2="topic",
        )
        assert secure_messaging is None

    @parametrize
    def test_raw_response_get_latest_offset(self, client: Unifieddatalibrary) -> None:
        response = client.secure_messaging.with_raw_response.get_latest_offset(
            topic_1="topic",
            topic_2="topic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = response.parse()
        assert secure_messaging is None

    @parametrize
    def test_streaming_response_get_latest_offset(self, client: Unifieddatalibrary) -> None:
        with client.secure_messaging.with_streaming_response.get_latest_offset(
            topic_1="topic",
            topic_2="topic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = response.parse()
            assert secure_messaging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_latest_offset(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_1` but received ''"):
            client.secure_messaging.with_raw_response.get_latest_offset(
                topic_1="",
                topic_2="",
            )

    @parametrize
    def test_method_get_messages(self, client: Unifieddatalibrary) -> None:
        secure_messaging = client.secure_messaging.get_messages(
            offset_1="offset",
            topic_1="topic",
            offset_2=0,
            topic_2="topic",
        )
        assert secure_messaging is None

    @parametrize
    def test_raw_response_get_messages(self, client: Unifieddatalibrary) -> None:
        response = client.secure_messaging.with_raw_response.get_messages(
            offset_1="offset",
            topic_1="topic",
            offset_2=0,
            topic_2="topic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = response.parse()
        assert secure_messaging is None

    @parametrize
    def test_streaming_response_get_messages(self, client: Unifieddatalibrary) -> None:
        with client.secure_messaging.with_streaming_response.get_messages(
            offset_1="offset",
            topic_1="topic",
            offset_2=0,
            topic_2="topic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = response.parse()
            assert secure_messaging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_messages(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_1` but received ''"):
            client.secure_messaging.with_raw_response.get_messages(
                offset_1="offset",
                topic_1="",
                offset_2=0,
                topic_2="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset_1` but received ''"):
            client.secure_messaging.with_raw_response.get_messages(
                offset_1="",
                topic_1="topic",
                offset_2="",
                topic_2="topic",
            )

    @parametrize
    def test_method_list_topics(self, client: Unifieddatalibrary) -> None:
        secure_messaging = client.secure_messaging.list_topics()
        assert_matches_type(SecureMessagingListTopicsResponse, secure_messaging, path=["response"])

    @parametrize
    def test_raw_response_list_topics(self, client: Unifieddatalibrary) -> None:
        response = client.secure_messaging.with_raw_response.list_topics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = response.parse()
        assert_matches_type(SecureMessagingListTopicsResponse, secure_messaging, path=["response"])

    @parametrize
    def test_streaming_response_list_topics(self, client: Unifieddatalibrary) -> None:
        with client.secure_messaging.with_streaming_response.list_topics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = response.parse()
            assert_matches_type(SecureMessagingListTopicsResponse, secure_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecureMessaging:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_describe_topic(self, async_client: AsyncUnifieddatalibrary) -> None:
        secure_messaging = await async_client.secure_messaging.describe_topic(
            topic_1="topic",
            topic_2="topic",
        )
        assert_matches_type(TopicDetails, secure_messaging, path=["response"])

    @parametrize
    async def test_raw_response_describe_topic(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.secure_messaging.with_raw_response.describe_topic(
            topic_1="topic",
            topic_2="topic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = await response.parse()
        assert_matches_type(TopicDetails, secure_messaging, path=["response"])

    @parametrize
    async def test_streaming_response_describe_topic(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.secure_messaging.with_streaming_response.describe_topic(
            topic_1="topic",
            topic_2="topic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = await response.parse()
            assert_matches_type(TopicDetails, secure_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_describe_topic(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_1` but received ''"):
            await async_client.secure_messaging.with_raw_response.describe_topic(
                topic_1="",
                topic_2="",
            )

    @parametrize
    async def test_method_get_latest_offset(self, async_client: AsyncUnifieddatalibrary) -> None:
        secure_messaging = await async_client.secure_messaging.get_latest_offset(
            topic_1="topic",
            topic_2="topic",
        )
        assert secure_messaging is None

    @parametrize
    async def test_raw_response_get_latest_offset(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.secure_messaging.with_raw_response.get_latest_offset(
            topic_1="topic",
            topic_2="topic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = await response.parse()
        assert secure_messaging is None

    @parametrize
    async def test_streaming_response_get_latest_offset(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.secure_messaging.with_streaming_response.get_latest_offset(
            topic_1="topic",
            topic_2="topic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = await response.parse()
            assert secure_messaging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_latest_offset(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_1` but received ''"):
            await async_client.secure_messaging.with_raw_response.get_latest_offset(
                topic_1="",
                topic_2="",
            )

    @parametrize
    async def test_method_get_messages(self, async_client: AsyncUnifieddatalibrary) -> None:
        secure_messaging = await async_client.secure_messaging.get_messages(
            offset_1="offset",
            topic_1="topic",
            offset_2=0,
            topic_2="topic",
        )
        assert secure_messaging is None

    @parametrize
    async def test_raw_response_get_messages(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.secure_messaging.with_raw_response.get_messages(
            offset_1="offset",
            topic_1="topic",
            offset_2=0,
            topic_2="topic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = await response.parse()
        assert secure_messaging is None

    @parametrize
    async def test_streaming_response_get_messages(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.secure_messaging.with_streaming_response.get_messages(
            offset_1="offset",
            topic_1="topic",
            offset_2=0,
            topic_2="topic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = await response.parse()
            assert secure_messaging is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_messages(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_1` but received ''"):
            await async_client.secure_messaging.with_raw_response.get_messages(
                offset_1="offset",
                topic_1="",
                offset_2=0,
                topic_2="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `offset_1` but received ''"):
            await async_client.secure_messaging.with_raw_response.get_messages(
                offset_1="",
                topic_1="topic",
                offset_2="",
                topic_2="topic",
            )

    @parametrize
    async def test_method_list_topics(self, async_client: AsyncUnifieddatalibrary) -> None:
        secure_messaging = await async_client.secure_messaging.list_topics()
        assert_matches_type(SecureMessagingListTopicsResponse, secure_messaging, path=["response"])

    @parametrize
    async def test_raw_response_list_topics(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.secure_messaging.with_raw_response.list_topics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secure_messaging = await response.parse()
        assert_matches_type(SecureMessagingListTopicsResponse, secure_messaging, path=["response"])

    @parametrize
    async def test_streaming_response_list_topics(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.secure_messaging.with_streaming_response.list_topics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secure_messaging = await response.parse()
            assert_matches_type(SecureMessagingListTopicsResponse, secure_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True
