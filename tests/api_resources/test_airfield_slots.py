# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import AirfieldSlotListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirfieldSlots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        airfield_slot = client.airfield_slots.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )
        assert airfield_slot is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfield_slot = client.airfield_slots.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            ac_slot_cat="WIDE",
            alt_airfield_id="ALT-AIRFIELD-ID",
            capacity=5,
            end_time="2359Z",
            icao="KCOS",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            min_separation=7,
            notes="Notes for an airfield slot.",
            origin="THIRD_PARTY_DATASOURCE",
            start_time="0000Z",
            type="WORKING",
        )
        assert airfield_slot is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slots.with_raw_response.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot = response.parse()
        assert airfield_slot is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slots.with_streaming_response.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot = response.parse()
            assert airfield_slot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airfield_slot = client.airfield_slots.list()
        assert_matches_type(AirfieldSlotListResponse, airfield_slot, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airfield_slots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot = response.parse()
        assert_matches_type(AirfieldSlotListResponse, airfield_slot, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airfield_slots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot = response.parse()
            assert_matches_type(AirfieldSlotListResponse, airfield_slot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirfieldSlots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot = await async_client.airfield_slots.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )
        assert airfield_slot is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot = await async_client.airfield_slots.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
            id="be831d39-1822-da9f-7ace-6cc5643397dc",
            ac_slot_cat="WIDE",
            alt_airfield_id="ALT-AIRFIELD-ID",
            capacity=5,
            end_time="2359Z",
            icao="KCOS",
            id_airfield="3136498f-2969-3535-1432-e984b2e2e686",
            min_separation=7,
            notes="Notes for an airfield slot.",
            origin="THIRD_PARTY_DATASOURCE",
            start_time="0000Z",
            type="WORKING",
        )
        assert airfield_slot is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slots.with_raw_response.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot = await response.parse()
        assert airfield_slot is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slots.with_streaming_response.create(
            airfield_name="USAF Academy AFLD",
            classification_marking="U",
            data_mode="TEST",
            name="Apron 5",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot = await response.parse()
            assert airfield_slot is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfield_slot = await async_client.airfield_slots.list()
        assert_matches_type(AirfieldSlotListResponse, airfield_slot, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfield_slots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfield_slot = await response.parse()
        assert_matches_type(AirfieldSlotListResponse, airfield_slot, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfield_slots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airfield_slot = await response.parse()
            assert_matches_type(AirfieldSlotListResponse, airfield_slot, path=["response"])

        assert cast(Any, response.is_closed) is True
