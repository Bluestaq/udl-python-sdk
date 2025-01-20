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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )
        assert airfieldstatus is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airfieldstatus = client.airfieldstatus.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
            id="id",
            alt_airfield_id="altAirfieldId",
            arff_cat="arffCat",
            cargo_mog=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            fleet_service_mog=0,
            fuel_mog=0,
            fuel_qtys=[0],
            fuel_types=["string"],
            gse_time=0,
            med_cap="medCap",
            message="message",
            mhe_qtys=[0],
            mhe_types=["string"],
            mx_mog=0,
            narrow_parking_mog=0,
            narrow_working_mog=0,
            num_cog=0,
            operating_mog=0,
            origin="origin",
            orig_network="origNetwork",
            passenger_service_mog=0,
            pri_freq=0,
            pri_rwy_num="priRwyNum",
            rwy_cond_reading=0,
            rwy_friction_factor=0,
            rwy_markings=["string"],
            slot_types_req=["string"],
            source_dl="sourceDL",
            wide_parking_mog=0,
            wide_working_mog=0,
        )
        assert airfieldstatus is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airfieldstatus.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = response.parse()
        assert airfieldstatus is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airfieldstatus.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
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
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )
        assert airfieldstatus is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airfieldstatus = await async_client.airfieldstatus.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
            id="id",
            alt_airfield_id="altAirfieldId",
            arff_cat="arffCat",
            cargo_mog=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            fleet_service_mog=0,
            fuel_mog=0,
            fuel_qtys=[0],
            fuel_types=["string"],
            gse_time=0,
            med_cap="medCap",
            message="message",
            mhe_qtys=[0],
            mhe_types=["string"],
            mx_mog=0,
            narrow_parking_mog=0,
            narrow_working_mog=0,
            num_cog=0,
            operating_mog=0,
            origin="origin",
            orig_network="origNetwork",
            passenger_service_mog=0,
            pri_freq=0,
            pri_rwy_num="priRwyNum",
            rwy_cond_reading=0,
            rwy_friction_factor=0,
            rwy_markings=["string"],
            slot_types_req=["string"],
            source_dl="sourceDL",
            wide_parking_mog=0,
            wide_working_mog=0,
        )
        assert airfieldstatus is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airfieldstatus.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airfieldstatus = await response.parse()
        assert airfieldstatus is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airfieldstatus.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            id_airfield="idAirfield",
            source="source",
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
