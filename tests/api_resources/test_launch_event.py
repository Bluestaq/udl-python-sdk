# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LaunchEventGetResponse,
    LaunchEventListResponse,
    LaunchEventTupleResponse,
    LaunchEventQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLaunchEvent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
        )
        assert launch_event is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
            id="LAUNCHEVENT-ID",
            be_number="ENC-123",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="Example Declassification",
            derived_from="Example source",
            launch_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            launch_facility_name="Example launch facility name",
            launch_failure_code="Example failure code",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            o_suffix="oSuffix",
            sat_no=12,
        )
        assert launch_event is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert launch_event is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert_matches_type(SyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert_matches_type(SyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, launch_event, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, launch_event, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert_matches_type(str, launch_event, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert_matches_type(str, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert launch_event is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert launch_event is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.get(
            id="id",
        )
        assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.launch_event.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.queryhelp()
        assert_matches_type(LaunchEventQueryhelpResponse, launch_event, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert_matches_type(LaunchEventQueryhelpResponse, launch_event, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert_matches_type(LaunchEventQueryhelpResponse, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        launch_event = client.launch_event.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert launch_event is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.launch_event.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = response.parse()
        assert launch_event is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.launch_event.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLaunchEvent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
        )
        assert launch_event is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
            id="LAUNCHEVENT-ID",
            be_number="ENC-123",
            declassification_date=parse_datetime("2021-01-01T01:02:02.123Z"),
            declassification_string="Example Declassification",
            derived_from="Example source",
            launch_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            launch_facility_name="Example launch facility name",
            launch_failure_code="Example failure code",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            o_suffix="oSuffix",
            sat_no=12,
        )
        assert launch_event is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert launch_event is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_create_date=parse_datetime("2020-01-01T00:00:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert_matches_type(AsyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.list(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert_matches_type(AsyncOffsetPage[LaunchEventListResponse], launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, launch_event, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, launch_event, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert_matches_type(str, launch_event, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.count(
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert_matches_type(str, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert launch_event is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert launch_event is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.get(
            id="id",
        )
        assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert_matches_type(LaunchEventGetResponse, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.launch_event.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.queryhelp()
        assert_matches_type(LaunchEventQueryhelpResponse, launch_event, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert_matches_type(LaunchEventQueryhelpResponse, launch_event, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert_matches_type(LaunchEventQueryhelpResponse, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.tuple(
            columns="columns",
            msg_create_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert_matches_type(LaunchEventTupleResponse, launch_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        launch_event = await async_client.launch_event.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert launch_event is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.launch_event.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        launch_event = await response.parse()
        assert launch_event is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.launch_event.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_create_date": parse_datetime("2020-01-01T00:00:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            launch_event = await response.parse()
            assert launch_event is None

        assert cast(Any, response.is_closed) is True
