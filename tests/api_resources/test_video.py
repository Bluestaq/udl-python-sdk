# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    VideoListResponse,
    VideoTupleResponse,
    VideoQueryhelpResponse,
    VideoGetStreamFileResponse,
    VideoGetPlayerStreamingInfoResponse,
    VideoGetPublisherStreamingInfoResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.video import VideoStreamsFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        video = client.video.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
        )
        assert video is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
            id="VIDEOSTREAMS-ID",
            origin="origin",
            start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )
        assert video is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert video is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        video = client.video.list()
        assert_matches_type(SyncOffsetPage[VideoListResponse], video, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[VideoListResponse], video, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(SyncOffsetPage[VideoListResponse], video, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(SyncOffsetPage[VideoListResponse], video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        video = client.video.count()
        assert_matches_type(str, video, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, video, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(str, video, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(str, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        video = client.video.get(
            id="id",
        )
        assert_matches_type(VideoStreamsFull, video, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoStreamsFull, video, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoStreamsFull, video, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoStreamsFull, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.video.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_get_player_streaming_info(self, client: Unifieddatalibrary) -> None:
        video = client.video.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )
        assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

    @parametrize
    def test_method_get_player_streaming_info_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

    @parametrize
    def test_raw_response_get_player_streaming_info(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_get_player_streaming_info(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_publisher_streaming_info(self, client: Unifieddatalibrary) -> None:
        video = client.video.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )
        assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

    @parametrize
    def test_method_get_publisher_streaming_info_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

    @parametrize
    def test_raw_response_get_publisher_streaming_info(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_get_publisher_streaming_info(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_stream_file(self, client: Unifieddatalibrary) -> None:
        video = client.video.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
        )
        assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

    @parametrize
    def test_method_get_stream_file_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

    @parametrize
    def test_raw_response_get_stream_file(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_get_stream_file(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        video = client.video.queryhelp()
        assert_matches_type(VideoQueryhelpResponse, video, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoQueryhelpResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoQueryhelpResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        video = client.video.tuple(
            columns="columns",
        )
        assert_matches_type(VideoTupleResponse, video, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        video = client.video.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoTupleResponse, video, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.video.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoTupleResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.video.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoTupleResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
        )
        assert video is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
            id="VIDEOSTREAMS-ID",
            origin="origin",
            start_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            stop_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )
        assert video is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert video is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            description="description",
            name="name",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert video is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.list()
        assert_matches_type(AsyncOffsetPage[VideoListResponse], video, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[VideoListResponse], video, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(AsyncOffsetPage[VideoListResponse], video, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(AsyncOffsetPage[VideoListResponse], video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.count()
        assert_matches_type(str, video, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, video, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(str, video, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(str, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.get(
            id="id",
        )
        assert_matches_type(VideoStreamsFull, video, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoStreamsFull, video, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoStreamsFull, video, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoStreamsFull, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.video.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_get_player_streaming_info(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )
        assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

    @parametrize
    async def test_method_get_player_streaming_info_with_all_params(
        self, async_client: AsyncUnifieddatalibrary
    ) -> None:
        video = await async_client.video.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_get_player_streaming_info(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_get_player_streaming_info(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.get_player_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoGetPlayerStreamingInfoResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_publisher_streaming_info(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )
        assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

    @parametrize
    async def test_method_get_publisher_streaming_info_with_all_params(
        self, async_client: AsyncUnifieddatalibrary
    ) -> None:
        video = await async_client.video.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_get_publisher_streaming_info(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_get_publisher_streaming_info(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.get_publisher_streaming_info(
            source_name="sourceName",
            stream_name="streamName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoGetPublisherStreamingInfoResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_stream_file(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
        )
        assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

    @parametrize
    async def test_method_get_stream_file_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_get_stream_file(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_get_stream_file(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.get_stream_file(
            source_name="sourceName",
            stream_name="streamName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoGetStreamFileResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.queryhelp()
        assert_matches_type(VideoQueryhelpResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoQueryhelpResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoQueryhelpResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.tuple(
            columns="columns",
        )
        assert_matches_type(VideoTupleResponse, video, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        video = await async_client.video.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(VideoTupleResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.video.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoTupleResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.video.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoTupleResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True
