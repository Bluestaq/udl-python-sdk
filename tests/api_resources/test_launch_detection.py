# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaunchDetectionGetResponse,
    LaunchDetectionListResponse,
    LaunchDetectionTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaunchDetection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )
        assert launch_detection is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
            id="LAUNCHDETECTION-ID",
            descriptor="Example descriptor",
            event_id="EVENT-ID",
            high_zenith_azimuth=False,
            inclination=1.23,
            launch_azimuth=1.23,
            launch_latitude=1.23,
            launch_longitude=1.23,
            launch_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            observation_altitude=1.23,
            origin="THIRD_PARTY_DATASOURCE",
            raan=1.23,
            stereo_flag=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert launch_detection is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert launch_detection is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )
        assert launch_detection is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
            body_id="LAUNCHDETECTION-ID",
            descriptor="Example descriptor",
            event_id="EVENT-ID",
            high_zenith_azimuth=False,
            inclination=1.23,
            launch_azimuth=1.23,
            launch_latitude=1.23,
            launch_longitude=1.23,
            launch_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            observation_altitude=1.23,
            origin="THIRD_PARTY_DATASOURCE",
            raan=1.23,
            stereo_flag=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert launch_detection is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert launch_detection is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.launch_detection.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                message_type="Example-Msg-Type",
                observation_latitude=45.23,
                observation_longitude=1.23,
                observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
                sequence_number=5,
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.list()
        assert_matches_type(SyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert_matches_type(SyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert_matches_type(SyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.delete(
            "id",
        )
        assert launch_detection is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert launch_detection is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_detection.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.count()
        assert_matches_type(str, launch_detection, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, launch_detection, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert_matches_type(str, launch_detection, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert_matches_type(str, launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.get(
            id="id",
        )
        assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_detection.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.queryhelp()
        assert launch_detection is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert launch_detection is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.tuple(
            columns="columns",
        )
        assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_detection = client.launch_detection.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.launch_detection.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = response.parse()
        assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.launch_detection.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = response.parse()
            assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLaunchDetection:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )
        assert launch_detection is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
            id="LAUNCHDETECTION-ID",
            descriptor="Example descriptor",
            event_id="EVENT-ID",
            high_zenith_azimuth=False,
            inclination=1.23,
            launch_azimuth=1.23,
            launch_latitude=1.23,
            launch_longitude=1.23,
            launch_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            observation_altitude=1.23,
            origin="THIRD_PARTY_DATASOURCE",
            raan=1.23,
            stereo_flag=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert launch_detection is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert launch_detection is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )
        assert launch_detection is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
            body_id="LAUNCHDETECTION-ID",
            descriptor="Example descriptor",
            event_id="EVENT-ID",
            high_zenith_azimuth=False,
            inclination=1.23,
            launch_azimuth=1.23,
            launch_latitude=1.23,
            launch_longitude=1.23,
            launch_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            observation_altitude=1.23,
            origin="THIRD_PARTY_DATASOURCE",
            raan=1.23,
            stereo_flag=False,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
        )
        assert launch_detection is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert launch_detection is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.launch_detection.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                message_type="Example-Msg-Type",
                observation_latitude=45.23,
                observation_longitude=1.23,
                observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
                sequence_number=5,
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.list()
        assert_matches_type(AsyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert_matches_type(AsyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert_matches_type(AsyncOffsetPage[LaunchDetectionListResponse], launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.delete(
            "id",
        )
        assert launch_detection is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert launch_detection is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_detection.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.count()
        assert_matches_type(str, launch_detection, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, launch_detection, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert_matches_type(str, launch_detection, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert_matches_type(str, launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.get(
            id="id",
        )
        assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert_matches_type(LaunchDetectionGetResponse, launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_detection.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.queryhelp()
        assert launch_detection is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert launch_detection is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert launch_detection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.tuple(
            columns="columns",
        )
        assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_detection = await async_client.launch_detection.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_detection.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_detection = await response.parse()
        assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_detection.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_detection = await response.parse()
            assert_matches_type(LaunchDetectionTupleResponse, launch_detection, path=["response"])

        assert cast(Any, response.is_closed) is True
