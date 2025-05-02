# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EventEvolutionListResponse,
    EventEvolutionTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import EventEvolutionFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventEvolution:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
        )
        assert event_evolution is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
            id="EVENT_EVOL_ID",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            andims=2,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=4326,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="POLYGON",
            category="PROTEST",
            country_code="US",
            data_description="Description of relationship between srcTyps and srcIds",
            end_time=parse_datetime("2021-12-03T16:00:00.123Z"),
            geo_admin_level1="Colorado",
            geo_admin_level2="El Paso County",
            geo_admin_level3="Colorado Springs",
            origin="THIRD_PARTY_DATASOURCE",
            redact=False,
            src_ids=["SRC_ID_1", "SRC_ID_2"],
            src_typs=["AIS", "CONJUNCTION"],
            status="UNKNOWN",
            tags=["TAG1", "TAG2"],
            url=["URL1", "URL2"],
        )
        assert event_evolution is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert event_evolution is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.retrieve(
            id="id",
        )
        assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.event_evolution.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.list()
        assert_matches_type(SyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.list(
            event_id="eventId",
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert_matches_type(SyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert_matches_type(SyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.count()
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.count(
            event_id="eventId",
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert_matches_type(str, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )
        assert event_evolution is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert event_evolution is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.queryhelp()
        assert event_evolution is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert event_evolution is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.tuple(
            columns="columns",
        )
        assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.tuple(
            columns="columns",
            event_id="eventId",
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )
        assert event_evolution is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert event_evolution is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEventEvolution:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
        )
        assert event_evolution is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
            id="EVENT_EVOL_ID",
            agjson='{"type":"Polygon","coordinates":[ [ [ 67.3291113966927, 26.156175339112 ], [ 67.2580009640721, 26.091022064271 ], [ 67.1795862381682, 26.6637992964562 ], [ 67.2501237475598, 26.730115808233 ], [ 67.3291113966927, 26.156175339112 ] ] ] }',
            andims=2,
            area="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            asrid=4326,
            atext="POLYGON((67.3291113966927 26.156175339112,67.2580009640721 26.091022064271,67.1795862381682 26.6637992964562,67.2501237475598 26.730115808233,67.3291113966927 26.156175339112))",
            atype="POLYGON",
            category="PROTEST",
            country_code="US",
            data_description="Description of relationship between srcTyps and srcIds",
            end_time=parse_datetime("2021-12-03T16:00:00.123Z"),
            geo_admin_level1="Colorado",
            geo_admin_level2="El Paso County",
            geo_admin_level3="Colorado Springs",
            origin="THIRD_PARTY_DATASOURCE",
            redact=False,
            src_ids=["SRC_ID_1", "SRC_ID_2"],
            src_typs=["AIS", "CONJUNCTION"],
            status="UNKNOWN",
            tags=["TAG1", "TAG2"],
            url=["URL1", "URL2"],
        )
        assert event_evolution is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert event_evolution is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_id="EVENT_ID",
            source="Bluestaq",
            start_time=parse_datetime("2021-12-02T16:00:00.123Z"),
            summary="Example summary of the event.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.retrieve(
            id="id",
        )
        assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert_matches_type(EventEvolutionFull, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.event_evolution.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.list()
        assert_matches_type(AsyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.list(
            event_id="eventId",
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert_matches_type(AsyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert_matches_type(AsyncOffsetPage[EventEvolutionListResponse], event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.count()
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.count(
            event_id="eventId",
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert_matches_type(str, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )
        assert event_evolution is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert event_evolution is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.queryhelp()
        assert event_evolution is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert event_evolution is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.tuple(
            columns="columns",
        )
        assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.tuple(
            columns="columns",
            event_id="eventId",
            first_result=0,
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert_matches_type(EventEvolutionTupleResponse, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )
        assert event_evolution is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert event_evolution is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_id": "EVENT_ID",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2021-12-02T16:00:00.123Z"),
                    "summary": "Example summary of the event.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True
