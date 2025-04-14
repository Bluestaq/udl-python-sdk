# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirfieldstatusListResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirfieldstatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        airfieldstatus = client.airfieldstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
        )
        assert airfieldstatus is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfieldstatus = client.airfieldstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_airfield_id="AIRFIELD-ID",
            approved_by="John Smith",
            approved_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            arff_cat="FAA-A",
            cargo_mog=8,
            fleet_service_mog=4,
            fuel_mog=9,
            fuel_qtys=[263083.6, 286674.9, 18143.69],
            fuel_types=["JP-8", "Jet A", "AVGAS"],
            gse_time=10,
            med_cap="Large Field Hospital",
            message="Status message about the airfield.",
            mhe_qtys=[1, 3, 1],
            mhe_types=["30k", "AT", "60k"],
            mx_mog=3,
            narrow_parking_mog=5,
            narrow_working_mog=4,
            num_cog=2,
            operating_mog=4,
            origin="THIRD_PARTY_DATASOURCE",
            passenger_service_mog=5,
            pri_freq=123.45,
            pri_rwy_num="35R",
            reviewed_by="Jane Doe",
            reviewed_date=parse_datetime("2024-01-01T00:00:00.123Z"),
            rwy_cond_reading=23,
            rwy_friction_factor=10,
            rwy_markings=["Aiming Point", "Threshold"],
            slot_types_req=["PARKING", "WORKING", "LANDING"],
            survey_date=parse_datetime("2023-01-01T12:00:00.123Z"),
            wide_parking_mog=7,
            wide_working_mog=3,
        )
        assert airfieldstatus is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldstatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = response.parse()
        assert airfieldstatus is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airfieldstatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = response.parse()
            assert airfieldstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airfieldstatus = client.airfieldstatus.list()
        assert_matches_type(AirfieldstatusListResponse, airfieldstatus, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldstatus.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = response.parse()
        assert_matches_type(AirfieldstatusListResponse, airfieldstatus, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airfieldstatus.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = response.parse()
            assert_matches_type(AirfieldstatusListResponse, airfieldstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        airfieldstatus = client.airfieldstatus.count()
        assert_matches_type(str, airfieldstatus, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldstatus.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = response.parse()
        assert_matches_type(str, airfieldstatus, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.airfieldstatus.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = response.parse()
            assert_matches_type(str, airfieldstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        airfieldstatus = client.airfieldstatus.queryhelp()
        assert airfieldstatus is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldstatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = response.parse()
        assert airfieldstatus is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.airfieldstatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = response.parse()
            assert airfieldstatus is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAirfieldstatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldstatus = await async_client.airfieldstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
        )
        assert airfieldstatus is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldstatus = await async_client.airfieldstatus.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            alt_airfield_id="AIRFIELD-ID",
            approved_by="John Smith",
            approved_date=parse_datetime("2024-01-01T16:00:00.123Z"),
            arff_cat="FAA-A",
            cargo_mog=8,
            fleet_service_mog=4,
            fuel_mog=9,
            fuel_qtys=[263083.6, 286674.9, 18143.69],
            fuel_types=["JP-8", "Jet A", "AVGAS"],
            gse_time=10,
            med_cap="Large Field Hospital",
            message="Status message about the airfield.",
            mhe_qtys=[1, 3, 1],
            mhe_types=["30k", "AT", "60k"],
            mx_mog=3,
            narrow_parking_mog=5,
            narrow_working_mog=4,
            num_cog=2,
            operating_mog=4,
            origin="THIRD_PARTY_DATASOURCE",
            passenger_service_mog=5,
            pri_freq=123.45,
            pri_rwy_num="35R",
            reviewed_by="Jane Doe",
            reviewed_date=parse_datetime("2024-01-01T00:00:00.123Z"),
            rwy_cond_reading=23,
            rwy_friction_factor=10,
            rwy_markings=["Aiming Point", "Threshold"],
            slot_types_req=["PARKING", "WORKING", "LANDING"],
            survey_date=parse_datetime("2023-01-01T12:00:00.123Z"),
            wide_parking_mog=7,
            wide_working_mog=3,
        )
        assert airfieldstatus is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldstatus.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = await response.parse()
        assert airfieldstatus is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldstatus.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = await response.parse()
            assert airfieldstatus is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldstatus = await async_client.airfieldstatus.list()
        assert_matches_type(AirfieldstatusListResponse, airfieldstatus, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldstatus.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = await response.parse()
        assert_matches_type(AirfieldstatusListResponse, airfieldstatus, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldstatus.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = await response.parse()
            assert_matches_type(AirfieldstatusListResponse, airfieldstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldstatus = await async_client.airfieldstatus.count()
        assert_matches_type(str, airfieldstatus, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldstatus.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = await response.parse()
        assert_matches_type(str, airfieldstatus, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldstatus.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = await response.parse()
            assert_matches_type(str, airfieldstatus, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldstatus = await async_client.airfieldstatus.queryhelp()
        assert airfieldstatus is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldstatus.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = await response.parse()
        assert airfieldstatus is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldstatus.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfieldstatus = await response.parse()
            assert airfieldstatus is None

        assert cast(Any, response.is_closed) is True
