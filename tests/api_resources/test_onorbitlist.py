# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OnorbitlistGetResponse,
    OnorbitlistListResponse,
    OnorbitlistTupleResponse,
    OnorbitlistQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnorbitlist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )
        assert onorbitlist is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[
                {
                    "clearing_box_cross_track": 1.25,
                    "clearing_box_in_track": 1.25,
                    "clearing_radius": 1.25,
                    "common_name": "VANGUARD 1",
                    "country_code": "USA",
                    "expired_on": parse_datetime("2024-07-12T00:00:00.000Z"),
                    "freq_mins": 300.25,
                    "monitoring_type": "REVISIT_RATE",
                    "object_id": "5",
                    "orbit_regime": "LEO",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "payload_priority": 2.5,
                    "rank": 3,
                    "urgency": 5.1,
                }
            ],
            source="Bluestaq",
            id="ONORBITLIST-ID",
            default_revisit_rate_mins=15.3,
            description="DESCRIPTION_OF_LIST",
            list_priority=1.1,
            namespace="18SDS",
            origin="THIRD_PARTY_DATASOURCE",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert onorbitlist is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert onorbitlist is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert onorbitlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )
        assert onorbitlist is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[
                {
                    "clearing_box_cross_track": 1.25,
                    "clearing_box_in_track": 1.25,
                    "clearing_radius": 1.25,
                    "common_name": "VANGUARD 1",
                    "country_code": "USA",
                    "expired_on": parse_datetime("2024-07-12T00:00:00.000Z"),
                    "freq_mins": 300.25,
                    "monitoring_type": "REVISIT_RATE",
                    "object_id": "5",
                    "orbit_regime": "LEO",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "payload_priority": 2.5,
                    "rank": 3,
                    "urgency": 5.1,
                }
            ],
            source="Bluestaq",
            body_id="ONORBITLIST-ID",
            default_revisit_rate_mins=15.3,
            description="DESCRIPTION_OF_LIST",
            list_priority=1.1,
            namespace="18SDS",
            origin="THIRD_PARTY_DATASOURCE",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert onorbitlist is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert onorbitlist is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert onorbitlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.onorbitlist.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="HRR-SATELLITES",
                on_orbit_list_items=[{}],
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.list()
        assert_matches_type(SyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert_matches_type(SyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert_matches_type(SyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.delete(
            "id",
        )
        assert onorbitlist is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert onorbitlist is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert onorbitlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitlist.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.count()
        assert_matches_type(str, onorbitlist, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbitlist, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert_matches_type(str, onorbitlist, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert_matches_type(str, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.get(
            id="id",
        )
        assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.onorbitlist.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.queryhelp()
        assert_matches_type(OnorbitlistQueryhelpResponse, onorbitlist, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert_matches_type(OnorbitlistQueryhelpResponse, onorbitlist, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert_matches_type(OnorbitlistQueryhelpResponse, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        onorbitlist = client.onorbitlist.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.onorbitlist.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = response.parse()
        assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.onorbitlist.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = response.parse()
            assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnorbitlist:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )
        assert onorbitlist is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[
                {
                    "clearing_box_cross_track": 1.25,
                    "clearing_box_in_track": 1.25,
                    "clearing_radius": 1.25,
                    "common_name": "VANGUARD 1",
                    "country_code": "USA",
                    "expired_on": parse_datetime("2024-07-12T00:00:00.000Z"),
                    "freq_mins": 300.25,
                    "monitoring_type": "REVISIT_RATE",
                    "object_id": "5",
                    "orbit_regime": "LEO",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "payload_priority": 2.5,
                    "rank": 3,
                    "urgency": 5.1,
                }
            ],
            source="Bluestaq",
            id="ONORBITLIST-ID",
            default_revisit_rate_mins=15.3,
            description="DESCRIPTION_OF_LIST",
            list_priority=1.1,
            namespace="18SDS",
            origin="THIRD_PARTY_DATASOURCE",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert onorbitlist is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert onorbitlist is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert onorbitlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )
        assert onorbitlist is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[
                {
                    "clearing_box_cross_track": 1.25,
                    "clearing_box_in_track": 1.25,
                    "clearing_radius": 1.25,
                    "common_name": "VANGUARD 1",
                    "country_code": "USA",
                    "expired_on": parse_datetime("2024-07-12T00:00:00.000Z"),
                    "freq_mins": 300.25,
                    "monitoring_type": "REVISIT_RATE",
                    "object_id": "5",
                    "orbit_regime": "LEO",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "payload_priority": 2.5,
                    "rank": 3,
                    "urgency": 5.1,
                }
            ],
            source="Bluestaq",
            body_id="ONORBITLIST-ID",
            default_revisit_rate_mins=15.3,
            description="DESCRIPTION_OF_LIST",
            list_priority=1.1,
            namespace="18SDS",
            origin="THIRD_PARTY_DATASOURCE",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
        )
        assert onorbitlist is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert onorbitlist is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            name="HRR-SATELLITES",
            on_orbit_list_items=[{}],
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert onorbitlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.onorbitlist.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                name="HRR-SATELLITES",
                on_orbit_list_items=[{}],
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.list()
        assert_matches_type(AsyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert_matches_type(AsyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert_matches_type(AsyncOffsetPage[OnorbitlistListResponse], onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.delete(
            "id",
        )
        assert onorbitlist is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert onorbitlist is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert onorbitlist is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitlist.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.count()
        assert_matches_type(str, onorbitlist, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, onorbitlist, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert_matches_type(str, onorbitlist, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert_matches_type(str, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.get(
            id="id",
        )
        assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert_matches_type(OnorbitlistGetResponse, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.onorbitlist.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.queryhelp()
        assert_matches_type(OnorbitlistQueryhelpResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert_matches_type(OnorbitlistQueryhelpResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert_matches_type(OnorbitlistQueryhelpResponse, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.tuple(
            columns="columns",
        )
        assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        onorbitlist = await async_client.onorbitlist.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.onorbitlist.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onorbitlist = await response.parse()
        assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.onorbitlist.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onorbitlist = await response.parse()
            assert_matches_type(OnorbitlistTupleResponse, onorbitlist, path=["response"])

        assert cast(Any, response.is_closed) is True
