# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    DeconflictsetGetResponse,
    DeconflictsetListResponse,
    DeconflictsetTupleResponse,
    DeconflictsetQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeconflictset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )
        assert deconflictset is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
            id="123dd511-8ba5-47d3-9909-836149f87434",
            calculation_end_time=parse_datetime("2023-09-25T20:00:00.123Z"),
            calculation_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            calculation_start_time=parse_datetime("2023-09-25T18:00:00.123Z"),
            deconflict_windows=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-09-27T20:49:37.812Z"),
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-07-19T00:00:00.001Z"),
                    "stop_time": parse_datetime("2023-07-19T04:20:34.257Z"),
                    "id": "123dd511-8ba5-47d3-9909-836149f87434",
                    "angle_of_entry": 0.65,
                    "angle_of_exit": 0.65,
                    "entry_coords": [-191500.74728263554, -987729.0529358581, 6735105.853234725],
                    "event_type": "LASER",
                    "exit_coords": [-361767.9896431379, -854021.6371921108, 6746208.020741149],
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "target": "41715",
                    "target_type": "VICTIM",
                    "victim": "55914",
                    "window_type": "CLOSED",
                }
            ],
            errors=["ERROR1", "ERROR2"],
            event_end_time=parse_datetime("2023-09-28T20:49:37.812Z"),
            event_type="LASER",
            id_laser_deconflict_request="026dd511-8ba5-47d3-9909-836149f87686",
            origin="THIRD_PARTY_DATASOURCE",
            reference_frame="J2000",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            warnings=["WARNING1", "WARNING2"],
        )
        assert deconflictset is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.deconflictset.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = response.parse()
        assert deconflictset is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.deconflictset.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = response.parse()
            assert deconflictset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.deconflictset.with_raw_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = response.parse()
        assert_matches_type(SyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.deconflictset.with_streaming_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = response.parse()
            assert_matches_type(SyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, deconflictset, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, deconflictset, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.deconflictset.with_raw_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = response.parse()
        assert_matches_type(str, deconflictset, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.deconflictset.with_streaming_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = response.parse()
            assert_matches_type(str, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.get(
            id="id",
        )
        assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.deconflictset.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = response.parse()
        assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.deconflictset.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = response.parse()
            assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.deconflictset.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.queryhelp()
        assert_matches_type(DeconflictsetQueryhelpResponse, deconflictset, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.deconflictset.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = response.parse()
        assert_matches_type(DeconflictsetQueryhelpResponse, deconflictset, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.deconflictset.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = response.parse()
            assert_matches_type(DeconflictsetQueryhelpResponse, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.deconflictset.with_raw_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = response.parse()
        assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.deconflictset.with_streaming_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = response.parse()
            assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )
        assert deconflictset is None

    @parametrize
    def test_method_unvalidated_publish_with_all_params(self, client: Unifieddatalibrary) -> None:
        deconflictset = client.deconflictset.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
            id="123dd511-8ba5-47d3-9909-836149f87434",
            calculation_end_time=parse_datetime("2023-09-25T20:00:00.123Z"),
            calculation_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            calculation_start_time=parse_datetime("2023-09-25T18:00:00.123Z"),
            deconflict_windows=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-09-27T20:49:37.812Z"),
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-07-19T00:00:00.001Z"),
                    "stop_time": parse_datetime("2023-07-19T04:20:34.257Z"),
                    "id": "123dd511-8ba5-47d3-9909-836149f87434",
                    "angle_of_entry": 0.65,
                    "angle_of_exit": 0.65,
                    "entry_coords": [-191500.74728263554, -987729.0529358581, 6735105.853234725],
                    "event_type": "LASER",
                    "exit_coords": [-361767.9896431379, -854021.6371921108, 6746208.020741149],
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "target": "41715",
                    "target_type": "VICTIM",
                    "victim": "55914",
                    "window_type": "CLOSED",
                }
            ],
            errors=["ERROR1", "ERROR2"],
            event_end_time=parse_datetime("2023-09-28T20:49:37.812Z"),
            event_type="LASER",
            id_laser_deconflict_request="026dd511-8ba5-47d3-9909-836149f87686",
            origin="THIRD_PARTY_DATASOURCE",
            reference_frame="J2000",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            warnings=["WARNING1", "WARNING2"],
        )
        assert deconflictset is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.deconflictset.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = response.parse()
        assert deconflictset is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.deconflictset.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = response.parse()
            assert deconflictset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDeconflictset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )
        assert deconflictset is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
            id="123dd511-8ba5-47d3-9909-836149f87434",
            calculation_end_time=parse_datetime("2023-09-25T20:00:00.123Z"),
            calculation_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            calculation_start_time=parse_datetime("2023-09-25T18:00:00.123Z"),
            deconflict_windows=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-09-27T20:49:37.812Z"),
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-07-19T00:00:00.001Z"),
                    "stop_time": parse_datetime("2023-07-19T04:20:34.257Z"),
                    "id": "123dd511-8ba5-47d3-9909-836149f87434",
                    "angle_of_entry": 0.65,
                    "angle_of_exit": 0.65,
                    "entry_coords": [-191500.74728263554, -987729.0529358581, 6735105.853234725],
                    "event_type": "LASER",
                    "exit_coords": [-361767.9896431379, -854021.6371921108, 6746208.020741149],
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "target": "41715",
                    "target_type": "VICTIM",
                    "victim": "55914",
                    "window_type": "CLOSED",
                }
            ],
            errors=["ERROR1", "ERROR2"],
            event_end_time=parse_datetime("2023-09-28T20:49:37.812Z"),
            event_type="LASER",
            id_laser_deconflict_request="026dd511-8ba5-47d3-9909-836149f87686",
            origin="THIRD_PARTY_DATASOURCE",
            reference_frame="J2000",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            warnings=["WARNING1", "WARNING2"],
        )
        assert deconflictset is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.deconflictset.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = await response.parse()
        assert deconflictset is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.deconflictset.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = await response.parse()
            assert deconflictset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.deconflictset.with_raw_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = await response.parse()
        assert_matches_type(AsyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.deconflictset.with_streaming_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = await response.parse()
            assert_matches_type(AsyncOffsetPage[DeconflictsetListResponse], deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, deconflictset, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, deconflictset, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.deconflictset.with_raw_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = await response.parse()
        assert_matches_type(str, deconflictset, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.deconflictset.with_streaming_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = await response.parse()
            assert_matches_type(str, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.get(
            id="id",
        )
        assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.deconflictset.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = await response.parse()
        assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.deconflictset.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = await response.parse()
            assert_matches_type(DeconflictsetGetResponse, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.deconflictset.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.queryhelp()
        assert_matches_type(DeconflictsetQueryhelpResponse, deconflictset, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.deconflictset.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = await response.parse()
        assert_matches_type(DeconflictsetQueryhelpResponse, deconflictset, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.deconflictset.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = await response.parse()
            assert_matches_type(DeconflictsetQueryhelpResponse, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.deconflictset.with_raw_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = await response.parse()
        assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.deconflictset.with_streaming_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = await response.parse()
            assert_matches_type(DeconflictsetTupleResponse, deconflictset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )
        assert deconflictset is None

    @parametrize
    async def test_method_unvalidated_publish_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        deconflictset = await async_client.deconflictset.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
            id="123dd511-8ba5-47d3-9909-836149f87434",
            calculation_end_time=parse_datetime("2023-09-25T20:00:00.123Z"),
            calculation_id="3856c0a0-585f-4232-af5d-93bad320fac6",
            calculation_start_time=parse_datetime("2023-09-25T18:00:00.123Z"),
            deconflict_windows=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-09-27T20:49:37.812Z"),
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-07-19T00:00:00.001Z"),
                    "stop_time": parse_datetime("2023-07-19T04:20:34.257Z"),
                    "id": "123dd511-8ba5-47d3-9909-836149f87434",
                    "angle_of_entry": 0.65,
                    "angle_of_exit": 0.65,
                    "entry_coords": [-191500.74728263554, -987729.0529358581, 6735105.853234725],
                    "event_type": "LASER",
                    "exit_coords": [-361767.9896431379, -854021.6371921108, 6746208.020741149],
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "target": "41715",
                    "target_type": "VICTIM",
                    "victim": "55914",
                    "window_type": "CLOSED",
                }
            ],
            errors=["ERROR1", "ERROR2"],
            event_end_time=parse_datetime("2023-09-28T20:49:37.812Z"),
            event_type="LASER",
            id_laser_deconflict_request="026dd511-8ba5-47d3-9909-836149f87686",
            origin="THIRD_PARTY_DATASOURCE",
            reference_frame="J2000",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            warnings=["WARNING1", "WARNING2"],
        )
        assert deconflictset is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.deconflictset.with_raw_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deconflictset = await response.parse()
        assert deconflictset is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.deconflictset.with_streaming_response.unvalidated_publish(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-09-27T20:49:37.812Z"),
            num_windows=250001,
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deconflictset = await response.parse()
            assert deconflictset is None

        assert cast(Any, response.is_closed) is True
