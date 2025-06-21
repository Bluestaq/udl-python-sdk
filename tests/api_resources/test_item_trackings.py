# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ItemTrackingGetResponse,
    ItemTrackingListResponse,
    ItemTrackingTupleResponse,
    ItemTrackingQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItemTrackings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
        )
        assert item_tracking is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            dv_code="DV-4",
            id_item="36054487-bcba-6e2d-4f3b-9f25738b2639",
            keys=["tapeColor", "hazmat"],
            lat=45.23,
            lon=179.1,
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            scan_type="TRANSIT",
            sc_gen_tool="bID",
            type="CARGO",
            values=["yellow", "false"],
        )
        assert item_tracking is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert item_tracking is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert item_tracking is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert_matches_type(SyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert_matches_type(SyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.delete(
            "id",
        )
        assert item_tracking is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert item_tracking is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert item_tracking is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.item_trackings.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, item_tracking, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, item_tracking, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert_matches_type(str, item_tracking, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert_matches_type(str, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.get(
            id="id",
        )
        assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.item_trackings.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.queryhelp()
        assert_matches_type(ItemTrackingQueryhelpResponse, item_tracking, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert_matches_type(ItemTrackingQueryhelpResponse, item_tracking, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert_matches_type(ItemTrackingQueryhelpResponse, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        item_tracking = client.item_trackings.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )
        assert item_tracking is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.item_trackings.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = response.parse()
        assert item_tracking is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.item_trackings.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = response.parse()
            assert item_tracking is None

        assert cast(Any, response.is_closed) is True


class TestAsyncItemTrackings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
        )
        assert item_tracking is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            dv_code="DV-4",
            id_item="36054487-bcba-6e2d-4f3b-9f25738b2639",
            keys=["tapeColor", "hazmat"],
            lat=45.23,
            lon=179.1,
            notes="Example notes",
            origin="THIRD_PARTY_DATASOURCE",
            scan_type="TRANSIT",
            sc_gen_tool="bID",
            type="CARGO",
            values=["yellow", "false"],
        )
        assert item_tracking is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert item_tracking is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            scan_code="ABC1234",
            scanner_id="2051M",
            source="Bluestaq",
            ts=parse_datetime("2023-03-21T14:22:00.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert item_tracking is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert_matches_type(AsyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.list(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert_matches_type(AsyncOffsetPage[ItemTrackingListResponse], item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.delete(
            "id",
        )
        assert item_tracking is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert item_tracking is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert item_tracking is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.item_trackings.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, item_tracking, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, item_tracking, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert_matches_type(str, item_tracking, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.count(
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert_matches_type(str, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.get(
            id="id",
        )
        assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert_matches_type(ItemTrackingGetResponse, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.item_trackings.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.queryhelp()
        assert_matches_type(ItemTrackingQueryhelpResponse, item_tracking, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert_matches_type(ItemTrackingQueryhelpResponse, item_tracking, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert_matches_type(ItemTrackingQueryhelpResponse, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.tuple(
            columns="columns",
            ts=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert_matches_type(ItemTrackingTupleResponse, item_tracking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        item_tracking = await async_client.item_trackings.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )
        assert item_tracking is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.item_trackings.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item_tracking = await response.parse()
        assert item_tracking is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.item_trackings.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "scan_code": "ABC1234",
                    "scanner_id": "2051M",
                    "source": "Bluestaq",
                    "ts": parse_datetime("2023-03-21T14:22:00.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item_tracking = await response.parse()
            assert item_tracking is None

        assert cast(Any, response.is_closed) is True
