# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    RouteStatQueryResponse,
    RouteStatTupleResponse,
    RouteStatRetrieveResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRouteStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )
        assert route_stat is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            avg_duration=47.1,
            avg_speed=450.1,
            data_pts_used=6,
            distance=63.1,
            dist_unit="Nautical miles",
            first_pt=parse_datetime("2024-01-01T16:00:00.123Z"),
            ideal_desc="Block speed using great circle path",
            ideal_duration=45.1,
            id_site_end="77b5550c-c0f4-47bd-94ce-d71cdaa52f62",
            id_site_start="23370387-5e8e-4a74-89db-ad81145aa4df",
            last_pt=parse_datetime("2024-03-31T16:00:00.123Z"),
            location_type="ICAO",
            max_duration=52.1,
            max_speed=470.1,
            min_duration=42.1,
            min_speed=420.1,
            origin="THIRD_PARTY_DATASOURCE",
            partial_desc="Performance speed using great circle path",
            partial_duration=38.1,
            speed_unit="knots",
            time_period="Q1",
            vehicle_category="AIRCRAFT",
            vehicle_type="C-17",
        )
        assert route_stat is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert route_stat is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.retrieve(
            id="id",
        )
        assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.route_stats.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )
        assert route_stat is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            avg_duration=47.1,
            avg_speed=450.1,
            data_pts_used=6,
            distance=63.1,
            dist_unit="Nautical miles",
            first_pt=parse_datetime("2024-01-01T16:00:00.123Z"),
            ideal_desc="Block speed using great circle path",
            ideal_duration=45.1,
            id_site_end="77b5550c-c0f4-47bd-94ce-d71cdaa52f62",
            id_site_start="23370387-5e8e-4a74-89db-ad81145aa4df",
            last_pt=parse_datetime("2024-03-31T16:00:00.123Z"),
            location_type="ICAO",
            max_duration=52.1,
            max_speed=470.1,
            min_duration=42.1,
            min_speed=420.1,
            origin="THIRD_PARTY_DATASOURCE",
            partial_desc="Performance speed using great circle path",
            partial_duration=38.1,
            speed_unit="knots",
            time_period="Q1",
            vehicle_category="AIRCRAFT",
            vehicle_type="C-17",
        )
        assert route_stat is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert route_stat is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.route_stats.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                location_end="KCOS",
                location_start="KDEN",
                source="Bluestaq",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.delete(
            "id",
        )
        assert route_stat is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert route_stat is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.route_stats.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.count()
        assert_matches_type(str, route_stat, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, route_stat, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert_matches_type(str, route_stat, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert_matches_type(str, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )
        assert route_stat is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert route_stat is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.query()
        assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.query(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.query_help()
        assert route_stat is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert route_stat is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.tuple(
            columns="columns",
        )
        assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        route_stat = client.route_stats.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )
        assert route_stat is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.route_stats.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = response.parse()
        assert route_stat is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.route_stats.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRouteStats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )
        assert route_stat is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
            id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            avg_duration=47.1,
            avg_speed=450.1,
            data_pts_used=6,
            distance=63.1,
            dist_unit="Nautical miles",
            first_pt=parse_datetime("2024-01-01T16:00:00.123Z"),
            ideal_desc="Block speed using great circle path",
            ideal_duration=45.1,
            id_site_end="77b5550c-c0f4-47bd-94ce-d71cdaa52f62",
            id_site_start="23370387-5e8e-4a74-89db-ad81145aa4df",
            last_pt=parse_datetime("2024-03-31T16:00:00.123Z"),
            location_type="ICAO",
            max_duration=52.1,
            max_speed=470.1,
            min_duration=42.1,
            min_speed=420.1,
            origin="THIRD_PARTY_DATASOURCE",
            partial_desc="Performance speed using great circle path",
            partial_duration=38.1,
            speed_unit="knots",
            time_period="Q1",
            vehicle_category="AIRCRAFT",
            vehicle_type="C-17",
        )
        assert route_stat is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert route_stat is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.retrieve(
            id="id",
        )
        assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert_matches_type(RouteStatRetrieveResponse, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.route_stats.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )
        assert route_stat is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
            body_id="0167f577-e06c-358e-85aa-0a07a730bdd0",
            avg_duration=47.1,
            avg_speed=450.1,
            data_pts_used=6,
            distance=63.1,
            dist_unit="Nautical miles",
            first_pt=parse_datetime("2024-01-01T16:00:00.123Z"),
            ideal_desc="Block speed using great circle path",
            ideal_duration=45.1,
            id_site_end="77b5550c-c0f4-47bd-94ce-d71cdaa52f62",
            id_site_start="23370387-5e8e-4a74-89db-ad81145aa4df",
            last_pt=parse_datetime("2024-03-31T16:00:00.123Z"),
            location_type="ICAO",
            max_duration=52.1,
            max_speed=470.1,
            min_duration=42.1,
            min_speed=420.1,
            origin="THIRD_PARTY_DATASOURCE",
            partial_desc="Performance speed using great circle path",
            partial_duration=38.1,
            speed_unit="knots",
            time_period="Q1",
            vehicle_category="AIRCRAFT",
            vehicle_type="C-17",
        )
        assert route_stat is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert route_stat is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            location_end="KCOS",
            location_start="KDEN",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.route_stats.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                location_end="KCOS",
                location_start="KDEN",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.delete(
            "id",
        )
        assert route_stat is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert route_stat is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.route_stats.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.count()
        assert_matches_type(str, route_stat, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, route_stat, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert_matches_type(str, route_stat, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert_matches_type(str, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )
        assert route_stat is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert route_stat is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.query()
        assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.query(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert_matches_type(RouteStatQueryResponse, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.query_help()
        assert route_stat is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert route_stat is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.tuple(
            columns="columns",
        )
        assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert_matches_type(RouteStatTupleResponse, route_stat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        route_stat = await async_client.route_stats.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )
        assert route_stat is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.route_stats.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route_stat = await response.parse()
        assert route_stat is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.route_stats.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "location_end": "KCOS",
                    "location_start": "KDEN",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route_stat = await response.parse()
            assert route_stat is None

        assert cast(Any, response.is_closed) is True
