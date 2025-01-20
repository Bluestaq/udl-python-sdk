# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EventEvolutionListResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventEvolution:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
        )
        assert event_evolution is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
            id="id",
            agjson="agjson",
            andims=0,
            area="area",
            asrid=0,
            atext="atext",
            atype="atype",
            category="category",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            data_description="dataDescription",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            geo_admin_level1="geoAdminLevel1",
            geo_admin_level2="geoAdminLevel2",
            geo_admin_level3="geoAdminLevel3",
            origin="origin",
            orig_network="origNetwork",
            redact=True,
            src_ids=["string"],
            src_typs=["string"],
            status="status",
            tags=["string"],
            url=["string"],
        )
        assert event_evolution is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert event_evolution is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.list()
        assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.list(
            event_id="eventId",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = response.parse()
        assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.event_evolution.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = response.parse()
            assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.count()
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        event_evolution = client.event_evolution.count(
            event_id="eventId",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "event_id": "eventId",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "summary": "summary",
                }
            ],
        )
        assert event_evolution is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.event_evolution.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "event_id": "eventId",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "summary": "summary",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "event_id": "eventId",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "summary": "summary",
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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
        )
        assert event_evolution is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
            id="id",
            agjson="agjson",
            andims=0,
            area="area",
            asrid=0,
            atext="atext",
            atype="atype",
            category="category",
            country_code="countryCode",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            data_description="dataDescription",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            geo_admin_level1="geoAdminLevel1",
            geo_admin_level2="geoAdminLevel2",
            geo_admin_level3="geoAdminLevel3",
            origin="origin",
            orig_network="origNetwork",
            redact=True,
            src_ids=["string"],
            src_typs=["string"],
            status="status",
            tags=["string"],
            url=["string"],
        )
        assert event_evolution is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert event_evolution is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            event_id="eventId",
            source="source",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.list()
        assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.list(
            event_id="eventId",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_evolution = await response.parse()
        assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.event_evolution.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert_matches_type(EventEvolutionListResponse, event_evolution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.count()
        assert_matches_type(str, event_evolution, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        event_evolution = await async_client.event_evolution.count(
            event_id="eventId",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "event_id": "eventId",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "summary": "summary",
                }
            ],
        )
        assert event_evolution is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.event_evolution.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "event_id": "eventId",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "summary": "summary",
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
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "event_id": "eventId",
                    "source": "source",
                    "start_time": "2019-12-27T18:11:19.117Z",
                    "summary": "summary",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_evolution = await response.parse()
            assert event_evolution is None

        assert cast(Any, response.is_closed) is True
