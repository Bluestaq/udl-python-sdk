# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    PersonnelRecoveryFullL,
    PersonnelrecoveryListResponse,
    PersonnelrecoveryTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPersonnelrecovery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
        )
        assert personnelrecovery is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
            id="PERSONNEL_RECOVERY-ID",
            auth_method="PASSPORT",
            auth_status="NO STATEMENT",
            beacon_ind=False,
            call_sign="BADGER",
            comm_eq1="LL PHONE",
            comm_eq2="LL PHONE",
            comm_eq3="LL PHONE",
            execution_info={
                "egress": 66.53,
                "egress_point": [107.23, 30.455],
                "escort_vehicle": {
                    "call_sign": "FALCO",
                    "primary_freq": 34.55,
                    "strength": 5,
                    "type": "C17",
                },
                "ingress": 35.66,
                "initial_point": [103.23, 30.445],
                "obj_strategy": "Description of strategy plan.",
                "recovery_vehicle": {
                    "call_sign": "FALCO",
                    "primary_freq": 34.55,
                    "strength": 5,
                    "type": "C17",
                },
            },
            identity="NEUTRAL CIVILIAN",
            id_weather_report="WEATHER_REPORT-ID",
            mil_class="CIVILIAN",
            nat_alliance=1,
            nat_alliance1=0,
            num_ambulatory=1,
            num_ambulatory_injured=2,
            num_non_ambulatory=0,
            num_persons=1,
            objective_area_info={
                "enemy_data": [
                    {
                        "dir_to_enemy": "NORTHWEST",
                        "friendlies_remarks": "Comments from friendlies.",
                        "hlz_remarks": "Hot Landing Zone remarks.",
                        "hostile_fire_type": "SMALL ARMS",
                    }
                ],
                "osc_call_sign": "STARFOX",
                "osc_freq": 12.55,
                "pz_desc": "Near the lake.",
                "pz_location": [103.23, 30.445],
            },
            origin="THIRD_PARTY_DATASOURCE",
            pickup_alt=30.1234,
            recov_id="RECOV-ID",
            rx_freq=5.5,
            survivor_messages="UNINJURED CANT MOVE HOSTILES NEARBY",
            survivor_radio="NO STATEMENT",
            term_ind=True,
            text_msg="Additional message from survivor.",
            tx_freq=5.5,
        )
        assert personnelrecovery is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert personnelrecovery is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert_matches_type(SyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert_matches_type(SyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, personnelrecovery, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, personnelrecovery, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert_matches_type(str, personnelrecovery, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert_matches_type(str, personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )
        assert personnelrecovery is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert personnelrecovery is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_file_create(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )
        assert personnelrecovery is None

    @parametrize
    def test_raw_response_file_create(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert personnelrecovery is None

    @parametrize
    def test_streaming_response_file_create(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.get(
            id="id",
        )
        assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.personnelrecovery.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.queryhelp()
        assert personnelrecovery is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert personnelrecovery is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        personnelrecovery = client.personnelrecovery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.personnelrecovery.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = response.parse()
        assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.personnelrecovery.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = response.parse()
            assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPersonnelrecovery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
        )
        assert personnelrecovery is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
            id="PERSONNEL_RECOVERY-ID",
            auth_method="PASSPORT",
            auth_status="NO STATEMENT",
            beacon_ind=False,
            call_sign="BADGER",
            comm_eq1="LL PHONE",
            comm_eq2="LL PHONE",
            comm_eq3="LL PHONE",
            execution_info={
                "egress": 66.53,
                "egress_point": [107.23, 30.455],
                "escort_vehicle": {
                    "call_sign": "FALCO",
                    "primary_freq": 34.55,
                    "strength": 5,
                    "type": "C17",
                },
                "ingress": 35.66,
                "initial_point": [103.23, 30.445],
                "obj_strategy": "Description of strategy plan.",
                "recovery_vehicle": {
                    "call_sign": "FALCO",
                    "primary_freq": 34.55,
                    "strength": 5,
                    "type": "C17",
                },
            },
            identity="NEUTRAL CIVILIAN",
            id_weather_report="WEATHER_REPORT-ID",
            mil_class="CIVILIAN",
            nat_alliance=1,
            nat_alliance1=0,
            num_ambulatory=1,
            num_ambulatory_injured=2,
            num_non_ambulatory=0,
            num_persons=1,
            objective_area_info={
                "enemy_data": [
                    {
                        "dir_to_enemy": "NORTHWEST",
                        "friendlies_remarks": "Comments from friendlies.",
                        "hlz_remarks": "Hot Landing Zone remarks.",
                        "hostile_fire_type": "SMALL ARMS",
                    }
                ],
                "osc_call_sign": "STARFOX",
                "osc_freq": 12.55,
                "pz_desc": "Near the lake.",
                "pz_location": [103.23, 30.445],
            },
            origin="THIRD_PARTY_DATASOURCE",
            pickup_alt=30.1234,
            recov_id="RECOV-ID",
            rx_freq=5.5,
            survivor_messages="UNINJURED CANT MOVE HOSTILES NEARBY",
            survivor_radio="NO STATEMENT",
            term_ind=True,
            text_msg="Additional message from survivor.",
            tx_freq=5.5,
        )
        assert personnelrecovery is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert personnelrecovery is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            msg_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            source="Bluestaq",
            type="MEDICAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert_matches_type(AsyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.list(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert_matches_type(AsyncOffsetPage[PersonnelrecoveryListResponse], personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, personnelrecovery, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, personnelrecovery, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert_matches_type(str, personnelrecovery, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.count(
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert_matches_type(str, personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )
        assert personnelrecovery is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert personnelrecovery is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )
        assert personnelrecovery is None

    @parametrize
    async def test_raw_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert personnelrecovery is None

    @parametrize
    async def test_streaming_response_file_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.file_create(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "msg_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "source": "Bluestaq",
                    "type": "MEDICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.get(
            id="id",
        )
        assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert_matches_type(PersonnelRecoveryFullL, personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.personnelrecovery.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.queryhelp()
        assert personnelrecovery is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert personnelrecovery is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert personnelrecovery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        personnelrecovery = await async_client.personnelrecovery.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.personnelrecovery.with_raw_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnelrecovery = await response.parse()
        assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.personnelrecovery.with_streaming_response.tuple(
            columns="columns",
            msg_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnelrecovery = await response.parse()
            assert_matches_type(PersonnelrecoveryTupleResponse, personnelrecovery, path=["response"])

        assert cast(Any, response.is_closed) is True
