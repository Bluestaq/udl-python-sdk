# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaunchdetectionGetResponse,
    LaunchdetectionListResponse,
    LaunchdetectionTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaunchdetection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )
        assert launchdetection is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.create(
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
        assert launchdetection is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.create(
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
        launchdetection = response.parse()
        assert launchdetection is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.create(
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

            launchdetection = response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.update(
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
        assert launchdetection is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.update(
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
        assert launchdetection is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.update(
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
        launchdetection = response.parse()
        assert launchdetection is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.update(
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

            launchdetection = response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.launchdetection.with_raw_response.update(
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
        launchdetection = client.launchdetection.list()
        assert_matches_type(LaunchdetectionListResponse, launchdetection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = response.parse()
        assert_matches_type(LaunchdetectionListResponse, launchdetection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = response.parse()
            assert_matches_type(LaunchdetectionListResponse, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.delete(
            "id",
        )
        assert launchdetection is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = response.parse()
        assert launchdetection is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launchdetection.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.count()
        assert_matches_type(str, launchdetection, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = response.parse()
        assert_matches_type(str, launchdetection, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = response.parse()
            assert_matches_type(str, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.get(
            "id",
        )
        assert_matches_type(LaunchdetectionGetResponse, launchdetection, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = response.parse()
        assert_matches_type(LaunchdetectionGetResponse, launchdetection, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = response.parse()
            assert_matches_type(LaunchdetectionGetResponse, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launchdetection.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.queryhelp()
        assert launchdetection is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = response.parse()
        assert launchdetection is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        launchdetection = client.launchdetection.tuple(
            columns="columns",
        )
        assert_matches_type(LaunchdetectionTupleResponse, launchdetection, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.launchdetection.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = response.parse()
        assert_matches_type(LaunchdetectionTupleResponse, launchdetection, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.launchdetection.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = response.parse()
            assert_matches_type(LaunchdetectionTupleResponse, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLaunchdetection:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.create(
            classification_marking="U",
            data_mode="TEST",
            message_type="Example-Msg-Type",
            observation_latitude=45.23,
            observation_longitude=1.23,
            observation_time=parse_datetime("2018-01-01T16:00:00.123Z"),
            sequence_number=5,
            source="Bluestaq",
        )
        assert launchdetection is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.create(
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
        assert launchdetection is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.create(
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
        launchdetection = await response.parse()
        assert launchdetection is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.create(
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

            launchdetection = await response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.update(
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
        assert launchdetection is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.update(
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
        assert launchdetection is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.update(
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
        launchdetection = await response.parse()
        assert launchdetection is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.update(
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

            launchdetection = await response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.launchdetection.with_raw_response.update(
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
        launchdetection = await async_client.launchdetection.list()
        assert_matches_type(LaunchdetectionListResponse, launchdetection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = await response.parse()
        assert_matches_type(LaunchdetectionListResponse, launchdetection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = await response.parse()
            assert_matches_type(LaunchdetectionListResponse, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.delete(
            "id",
        )
        assert launchdetection is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = await response.parse()
        assert launchdetection is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = await response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launchdetection.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.count()
        assert_matches_type(str, launchdetection, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = await response.parse()
        assert_matches_type(str, launchdetection, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = await response.parse()
            assert_matches_type(str, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.get(
            "id",
        )
        assert_matches_type(LaunchdetectionGetResponse, launchdetection, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = await response.parse()
        assert_matches_type(LaunchdetectionGetResponse, launchdetection, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = await response.parse()
            assert_matches_type(LaunchdetectionGetResponse, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launchdetection.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.queryhelp()
        assert launchdetection is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = await response.parse()
        assert launchdetection is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = await response.parse()
            assert launchdetection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        launchdetection = await async_client.launchdetection.tuple(
            columns="columns",
        )
        assert_matches_type(LaunchdetectionTupleResponse, launchdetection, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launchdetection.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launchdetection = await response.parse()
        assert_matches_type(LaunchdetectionTupleResponse, launchdetection, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launchdetection.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launchdetection = await response.parse()
            assert_matches_type(LaunchdetectionTupleResponse, launchdetection, path=["response"])

        assert cast(Any, response.is_closed) is True
