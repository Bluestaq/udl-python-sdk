# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EvacAbridged,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import EvacFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvac:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
        )
        assert evac is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
            id="MEDEVACEVENT-ID",
            casualty_info=[
                {
                    "age": 35,
                    "allergy": [
                        {
                            "comments": "Comments on the patient's allergies.",
                            "type": "PENICILLIN",
                        }
                    ],
                    "blood_type": "O NEG",
                    "body_part": "FACE",
                    "burial_location": [-33.123, 150.33, 0.24],
                    "call_sign": "SHARK",
                    "care_provider_urn": "CARE_PROVIDER-1",
                    "casualty_key": "casualty-007",
                    "casualty_type": "DENTAL",
                    "collection_point": [12.44, 122.55, 0.98],
                    "comments": "Comments relating to this casualty info.",
                    "condition": [
                        {
                            "body_part": "ANKLE LEFT FRONT",
                            "comments": "Comments on the patient's condition.",
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "ACTIVITY LOW",
                        }
                    ],
                    "contam_type": "NONE",
                    "disposition": "EVACUATE WOUNDED",
                    "disposition_type": "EVACUATE",
                    "etiology": [
                        {
                            "body_part": "ARM LEFT FRONT",
                            "comments": "Comments on the etiology info.",
                            "time": parse_datetime("2021-10-16T16:00:00.123Z"),
                            "type": "BURN",
                        }
                    ],
                    "evac_type": "GROUND",
                    "gender": "MALE",
                    "health_state": [
                        {
                            "health_state_code": "BLUE",
                            "med_conf_factor": 1,
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "COGNITIVE",
                        }
                    ],
                    "injury": [
                        {
                            "body_part": "ARM LEFT FRONT",
                            "comments": "Comments on the patient's injury.",
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "ABRASION",
                        }
                    ],
                    "last4_ssn": "1234",
                    "medication": [
                        {
                            "admin_route": "ORAL",
                            "body_part": "ARM LEFT BACK",
                            "comments": "Comments on the patient's medication information.",
                            "dose": "800mg",
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "TYLENOL",
                        }
                    ],
                    "name": "John Smith",
                    "nationality": "US",
                    "occ_speciality": "Healthcare",
                    "patient_identity": "FRIEND CIVILIAN",
                    "patient_status": "US CIVILIAN",
                    "pay_grade": "CIVILIAN",
                    "priority": "ROUTINE",
                    "report_gen": "DEVICE",
                    "report_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "service": "CIV",
                    "spec_med_equip": ["OXYGEN", "HOIST"],
                    "treatment": [
                        {
                            "body_part": "CHEST",
                            "comments": "Comments on the treatment info.",
                            "time": parse_datetime("2018-01-01T16:00:00.123Z"),
                            "type": "BREATHING CHEST TUBE",
                        }
                    ],
                    "vital_sign_data": [
                        {
                            "med_conf_factor": 1,
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "vital_sign": "HEART RATE",
                            "vital_sign1": 120,
                            "vital_sign2": 80,
                        }
                    ],
                }
            ],
            ce=10.1234,
            cntct_freq=3.11,
            comments="Comments concerning mission",
            enemy_data=[
                {
                    "dir_to_enemy": "NORTH",
                    "friendlies_remarks": "Comments from friendlies.",
                    "hlz_remarks": "Remarks about hot landing zone.",
                    "hostile_fire_type": "SMALL ARMS",
                }
            ],
            id_weather_report="WeatherReport-ID",
            le=5.1234,
            medevac_id="MedEvac-ID",
            medic_req=True,
            mission_type="GROUND",
            num_ambulatory=5,
            num_casualties=5,
            num_kia=0,
            num_litter=0,
            num_wia=3,
            obstacles_remarks="N/A",
            origin="THIRD_PARTY_DATASOURCE",
            pickup_alt=30.1234,
            pickup_time=parse_datetime("2021-10-20T16:00:00.123Z"),
            req_call_sign="Bravo",
            req_num="MED.1.223908",
            terrain="ROCKY",
            terrain_remarks="N/A",
            zone_contr_call_sign="Tango",
            zone_hot=False,
            zone_marking="ILLUMINATION",
            zone_marking_color="RED",
            zone_name="example-zone",
            zone_security="NO ENEMY",
        )
        assert evac is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert evac is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.retrieve(
            id="id",
        )
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert_matches_type(EvacFull, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evac.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EvacAbridged], evac, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EvacAbridged], evac, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert_matches_type(SyncOffsetPage[EvacAbridged], evac, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert_matches_type(SyncOffsetPage[EvacAbridged], evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert_matches_type(str, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )
        assert evac is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert evac is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.query_help()
        assert evac is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert evac is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        evac = client.evac.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )
        assert evac is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.evac.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = response.parse()
        assert evac is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.evac.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEvac:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
        )
        assert evac is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
            id="MEDEVACEVENT-ID",
            casualty_info=[
                {
                    "age": 35,
                    "allergy": [
                        {
                            "comments": "Comments on the patient's allergies.",
                            "type": "PENICILLIN",
                        }
                    ],
                    "blood_type": "O NEG",
                    "body_part": "FACE",
                    "burial_location": [-33.123, 150.33, 0.24],
                    "call_sign": "SHARK",
                    "care_provider_urn": "CARE_PROVIDER-1",
                    "casualty_key": "casualty-007",
                    "casualty_type": "DENTAL",
                    "collection_point": [12.44, 122.55, 0.98],
                    "comments": "Comments relating to this casualty info.",
                    "condition": [
                        {
                            "body_part": "ANKLE LEFT FRONT",
                            "comments": "Comments on the patient's condition.",
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "ACTIVITY LOW",
                        }
                    ],
                    "contam_type": "NONE",
                    "disposition": "EVACUATE WOUNDED",
                    "disposition_type": "EVACUATE",
                    "etiology": [
                        {
                            "body_part": "ARM LEFT FRONT",
                            "comments": "Comments on the etiology info.",
                            "time": parse_datetime("2021-10-16T16:00:00.123Z"),
                            "type": "BURN",
                        }
                    ],
                    "evac_type": "GROUND",
                    "gender": "MALE",
                    "health_state": [
                        {
                            "health_state_code": "BLUE",
                            "med_conf_factor": 1,
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "COGNITIVE",
                        }
                    ],
                    "injury": [
                        {
                            "body_part": "ARM LEFT FRONT",
                            "comments": "Comments on the patient's injury.",
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "ABRASION",
                        }
                    ],
                    "last4_ssn": "1234",
                    "medication": [
                        {
                            "admin_route": "ORAL",
                            "body_part": "ARM LEFT BACK",
                            "comments": "Comments on the patient's medication information.",
                            "dose": "800mg",
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "type": "TYLENOL",
                        }
                    ],
                    "name": "John Smith",
                    "nationality": "US",
                    "occ_speciality": "Healthcare",
                    "patient_identity": "FRIEND CIVILIAN",
                    "patient_status": "US CIVILIAN",
                    "pay_grade": "CIVILIAN",
                    "priority": "ROUTINE",
                    "report_gen": "DEVICE",
                    "report_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "service": "CIV",
                    "spec_med_equip": ["OXYGEN", "HOIST"],
                    "treatment": [
                        {
                            "body_part": "CHEST",
                            "comments": "Comments on the treatment info.",
                            "time": parse_datetime("2018-01-01T16:00:00.123Z"),
                            "type": "BREATHING CHEST TUBE",
                        }
                    ],
                    "vital_sign_data": [
                        {
                            "med_conf_factor": 1,
                            "time": parse_datetime("2021-10-15T16:00:00.123Z"),
                            "vital_sign": "HEART RATE",
                            "vital_sign1": 120,
                            "vital_sign2": 80,
                        }
                    ],
                }
            ],
            ce=10.1234,
            cntct_freq=3.11,
            comments="Comments concerning mission",
            enemy_data=[
                {
                    "dir_to_enemy": "NORTH",
                    "friendlies_remarks": "Comments from friendlies.",
                    "hlz_remarks": "Remarks about hot landing zone.",
                    "hostile_fire_type": "SMALL ARMS",
                }
            ],
            id_weather_report="WeatherReport-ID",
            le=5.1234,
            medevac_id="MedEvac-ID",
            medic_req=True,
            mission_type="GROUND",
            num_ambulatory=5,
            num_casualties=5,
            num_kia=0,
            num_litter=0,
            num_wia=3,
            obstacles_remarks="N/A",
            origin="THIRD_PARTY_DATASOURCE",
            pickup_alt=30.1234,
            pickup_time=parse_datetime("2021-10-20T16:00:00.123Z"),
            req_call_sign="Bravo",
            req_num="MED.1.223908",
            terrain="ROCKY",
            terrain_remarks="N/A",
            zone_contr_call_sign="Tango",
            zone_hot=False,
            zone_marking="ILLUMINATION",
            zone_marking_color="RED",
            zone_name="example-zone",
            zone_security="NO ENEMY",
        )
        assert evac is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert evac is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            pickup_lat=75.1234,
            pickup_lon=175.1234,
            req_time=parse_datetime("2021-10-15T16:00:00.123Z"),
            source="Bluestaq",
            type="REQUEST",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.retrieve(
            id="id",
        )
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert_matches_type(EvacFull, evac, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert_matches_type(EvacFull, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evac.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EvacAbridged], evac, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EvacAbridged], evac, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert_matches_type(AsyncOffsetPage[EvacAbridged], evac, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.list(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert_matches_type(AsyncOffsetPage[EvacAbridged], evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert_matches_type(str, evac, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.count(
            req_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert_matches_type(str, evac, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )
        assert evac is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert evac is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.query_help()
        assert evac is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert evac is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        evac = await async_client.evac.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )
        assert evac is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.evac.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evac = await response.parse()
        assert evac is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.evac.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "pickup_lat": 75.1234,
                    "pickup_lon": 175.1234,
                    "req_time": parse_datetime("2021-10-15T16:00:00.123Z"),
                    "source": "Bluestaq",
                    "type": "REQUEST",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evac = await response.parse()
            assert evac is None

        assert cast(Any, response.is_closed) is True
