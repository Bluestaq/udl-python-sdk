# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirEventGetResponse,
    AirEventListResponse,
    AirEventTupleResponse,
    AirEventQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )
        assert air_event is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            actual_arr_time=parse_datetime("2024-01-07T14:00:03.123Z"),
            actual_dep_time=parse_datetime("2024-01-07T14:17:03.123Z"),
            arct=parse_datetime("2024-01-07T15:11:27.123Z"),
            ar_event_type="V",
            arr_purpose="A",
            ar_track_id="CH61",
            ar_track_name="CH61 POST",
            base_alt=28000.1,
            cancelled=False,
            dep_purpose="Q",
            est_arr_time=parse_datetime("2024-01-07T13:59:48.123Z"),
            est_dep_time=parse_datetime("2024-01-07T14:19:48.123Z"),
            external_air_event_id="MB014313032022407540",
            external_ar_track_id="6418a4b68e5c3896bf024cc79aa4174c",
            id_mission="190dea6d-2a90-45a2-a276-be9047d9b96c",
            id_sortie="b9866c03-2397-4506-8153-852e72d9b54f",
            leg_num=825,
            location="901EW",
            num_tankers=1,
            origin="THIRD_PARTY_DATASOURCE",
            planned_arr_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            planned_dep_time=parse_datetime("2024-01-07T14:15:43.123Z"),
            priority="1A2",
            receivers=[
                {
                    "alt_receiver_mission_id": "1UN05201L121",
                    "amc_receiver_mission_id": "8PH000B1S052",
                    "external_receiver_id": "3fb8169f-adc1-4667-acab-8415a012d766",
                    "fuel_on": 15000000.1,
                    "id_receiver_airfield": "96c4c2ba-a031-4e58-9b8e-3c6fb90a7534",
                    "id_receiver_mission": "ce99757d-f733-461f-8939-3939d4f05946",
                    "id_receiver_sortie": "1d03e85a-1fb9-4f6e-86a0-593306b6e3f0",
                    "num_rec_aircraft": 3,
                    "package_id": "135",
                    "receiver_call_sign": "BAKER",
                    "receiver_cell_position": 2,
                    "receiver_coord": "TTC601",
                    "receiver_delivery_method": "DROGUE",
                    "receiver_deployed_icao": "KOFF",
                    "receiver_exercise": "NATO19",
                    "receiver_fuel_type": "JP8",
                    "receiver_leg_num": 825,
                    "receiver_mds": "KC135R",
                    "receiver_owner": "117ARW",
                    "receiver_poc": "JOHN SMITH (555)555-5555",
                    "rec_org": "AMC",
                    "sequence_num": "1018",
                }
            ],
            remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "external_remark_id": "23ea2877a6f74d7d8f309567a5896441",
                    "text": "Example air event remarks.",
                    "user": "John Doe",
                }
            ],
            rev_track=True,
            rzct=parse_datetime("2024-01-07T13:55:43.123Z"),
            rz_point="AN",
            rz_type="PP",
            short_track=True,
            status_code="R",
            tankers=[
                {
                    "alt_tanker_mission_id": "1UN05201L121",
                    "amc_tanker_mission_id": "8PH000B1S052",
                    "dual_role": True,
                    "external_tanker_id": "ca673c580fb949a5b733f0e0b67ffab2",
                    "fuel_off": 15000000.1,
                    "id_tanker_airfield": "b33955d2-67d3-42be-8316-263e284ce6cc",
                    "id_tanker_mission": "edef700c-9917-4dbf-a153-89ffd4446fe9",
                    "id_tanker_sortie": "d833a4bc-756b-41d5-8845-f146fe563387",
                    "tanker_call_sign": "BAKER",
                    "tanker_cell_position": 2,
                    "tanker_coord": "TTC601",
                    "tanker_delivery_method": "DROGUE",
                    "tanker_deployed_icao": "KOFF",
                    "tanker_fuel_type": "JP8",
                    "tanker_leg_num": 825,
                    "tanker_mds": "KC135R",
                    "tanker_owner": "117ARW",
                    "tanker_poc": "JOHN SMITH (555)555-5555",
                }
            ],
            track_time=1.5,
        )
        assert air_event is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert air_event is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )
        assert air_event is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            actual_arr_time=parse_datetime("2024-01-07T14:00:03.123Z"),
            actual_dep_time=parse_datetime("2024-01-07T14:17:03.123Z"),
            arct=parse_datetime("2024-01-07T15:11:27.123Z"),
            ar_event_type="V",
            arr_purpose="A",
            ar_track_id="CH61",
            ar_track_name="CH61 POST",
            base_alt=28000.1,
            cancelled=False,
            dep_purpose="Q",
            est_arr_time=parse_datetime("2024-01-07T13:59:48.123Z"),
            est_dep_time=parse_datetime("2024-01-07T14:19:48.123Z"),
            external_air_event_id="MB014313032022407540",
            external_ar_track_id="6418a4b68e5c3896bf024cc79aa4174c",
            id_mission="190dea6d-2a90-45a2-a276-be9047d9b96c",
            id_sortie="b9866c03-2397-4506-8153-852e72d9b54f",
            leg_num=825,
            location="901EW",
            num_tankers=1,
            origin="THIRD_PARTY_DATASOURCE",
            planned_arr_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            planned_dep_time=parse_datetime("2024-01-07T14:15:43.123Z"),
            priority="1A2",
            receivers=[
                {
                    "alt_receiver_mission_id": "1UN05201L121",
                    "amc_receiver_mission_id": "8PH000B1S052",
                    "external_receiver_id": "3fb8169f-adc1-4667-acab-8415a012d766",
                    "fuel_on": 15000000.1,
                    "id_receiver_airfield": "96c4c2ba-a031-4e58-9b8e-3c6fb90a7534",
                    "id_receiver_mission": "ce99757d-f733-461f-8939-3939d4f05946",
                    "id_receiver_sortie": "1d03e85a-1fb9-4f6e-86a0-593306b6e3f0",
                    "num_rec_aircraft": 3,
                    "package_id": "135",
                    "receiver_call_sign": "BAKER",
                    "receiver_cell_position": 2,
                    "receiver_coord": "TTC601",
                    "receiver_delivery_method": "DROGUE",
                    "receiver_deployed_icao": "KOFF",
                    "receiver_exercise": "NATO19",
                    "receiver_fuel_type": "JP8",
                    "receiver_leg_num": 825,
                    "receiver_mds": "KC135R",
                    "receiver_owner": "117ARW",
                    "receiver_poc": "JOHN SMITH (555)555-5555",
                    "rec_org": "AMC",
                    "sequence_num": "1018",
                }
            ],
            remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "external_remark_id": "23ea2877a6f74d7d8f309567a5896441",
                    "text": "Example air event remarks.",
                    "user": "John Doe",
                }
            ],
            rev_track=True,
            rzct=parse_datetime("2024-01-07T13:55:43.123Z"),
            rz_point="AN",
            rz_type="PP",
            short_track=True,
            status_code="R",
            tankers=[
                {
                    "alt_tanker_mission_id": "1UN05201L121",
                    "amc_tanker_mission_id": "8PH000B1S052",
                    "dual_role": True,
                    "external_tanker_id": "ca673c580fb949a5b733f0e0b67ffab2",
                    "fuel_off": 15000000.1,
                    "id_tanker_airfield": "b33955d2-67d3-42be-8316-263e284ce6cc",
                    "id_tanker_mission": "edef700c-9917-4dbf-a153-89ffd4446fe9",
                    "id_tanker_sortie": "d833a4bc-756b-41d5-8845-f146fe563387",
                    "tanker_call_sign": "BAKER",
                    "tanker_cell_position": 2,
                    "tanker_coord": "TTC601",
                    "tanker_delivery_method": "DROGUE",
                    "tanker_deployed_icao": "KOFF",
                    "tanker_fuel_type": "JP8",
                    "tanker_leg_num": 825,
                    "tanker_mds": "KC135R",
                    "tanker_owner": "117ARW",
                    "tanker_poc": "JOHN SMITH (555)555-5555",
                }
            ],
            track_time=1.5,
        )
        assert air_event is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert air_event is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.air_events.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                type="FUEL TRANSFER",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.list()
        assert_matches_type(SyncOffsetPage[AirEventListResponse], air_event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AirEventListResponse], air_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert_matches_type(SyncOffsetPage[AirEventListResponse], air_event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert_matches_type(SyncOffsetPage[AirEventListResponse], air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.delete(
            "id",
        )
        assert air_event is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert air_event is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.air_events.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.count()
        assert_matches_type(str, air_event, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, air_event, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert_matches_type(str, air_event, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert_matches_type(str, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )
        assert air_event is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert air_event is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.get(
            id="id",
        )
        assert_matches_type(AirEventGetResponse, air_event, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirEventGetResponse, air_event, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert_matches_type(AirEventGetResponse, air_event, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert_matches_type(AirEventGetResponse, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.air_events.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.queryhelp()
        assert_matches_type(AirEventQueryhelpResponse, air_event, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert_matches_type(AirEventQueryhelpResponse, air_event, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert_matches_type(AirEventQueryhelpResponse, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.tuple(
            columns="columns",
        )
        assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        air_event = client.air_events.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )
        assert air_event is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.air_events.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = response.parse()
        assert air_event is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.air_events.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAirEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )
        assert air_event is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            actual_arr_time=parse_datetime("2024-01-07T14:00:03.123Z"),
            actual_dep_time=parse_datetime("2024-01-07T14:17:03.123Z"),
            arct=parse_datetime("2024-01-07T15:11:27.123Z"),
            ar_event_type="V",
            arr_purpose="A",
            ar_track_id="CH61",
            ar_track_name="CH61 POST",
            base_alt=28000.1,
            cancelled=False,
            dep_purpose="Q",
            est_arr_time=parse_datetime("2024-01-07T13:59:48.123Z"),
            est_dep_time=parse_datetime("2024-01-07T14:19:48.123Z"),
            external_air_event_id="MB014313032022407540",
            external_ar_track_id="6418a4b68e5c3896bf024cc79aa4174c",
            id_mission="190dea6d-2a90-45a2-a276-be9047d9b96c",
            id_sortie="b9866c03-2397-4506-8153-852e72d9b54f",
            leg_num=825,
            location="901EW",
            num_tankers=1,
            origin="THIRD_PARTY_DATASOURCE",
            planned_arr_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            planned_dep_time=parse_datetime("2024-01-07T14:15:43.123Z"),
            priority="1A2",
            receivers=[
                {
                    "alt_receiver_mission_id": "1UN05201L121",
                    "amc_receiver_mission_id": "8PH000B1S052",
                    "external_receiver_id": "3fb8169f-adc1-4667-acab-8415a012d766",
                    "fuel_on": 15000000.1,
                    "id_receiver_airfield": "96c4c2ba-a031-4e58-9b8e-3c6fb90a7534",
                    "id_receiver_mission": "ce99757d-f733-461f-8939-3939d4f05946",
                    "id_receiver_sortie": "1d03e85a-1fb9-4f6e-86a0-593306b6e3f0",
                    "num_rec_aircraft": 3,
                    "package_id": "135",
                    "receiver_call_sign": "BAKER",
                    "receiver_cell_position": 2,
                    "receiver_coord": "TTC601",
                    "receiver_delivery_method": "DROGUE",
                    "receiver_deployed_icao": "KOFF",
                    "receiver_exercise": "NATO19",
                    "receiver_fuel_type": "JP8",
                    "receiver_leg_num": 825,
                    "receiver_mds": "KC135R",
                    "receiver_owner": "117ARW",
                    "receiver_poc": "JOHN SMITH (555)555-5555",
                    "rec_org": "AMC",
                    "sequence_num": "1018",
                }
            ],
            remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "external_remark_id": "23ea2877a6f74d7d8f309567a5896441",
                    "text": "Example air event remarks.",
                    "user": "John Doe",
                }
            ],
            rev_track=True,
            rzct=parse_datetime("2024-01-07T13:55:43.123Z"),
            rz_point="AN",
            rz_type="PP",
            short_track=True,
            status_code="R",
            tankers=[
                {
                    "alt_tanker_mission_id": "1UN05201L121",
                    "amc_tanker_mission_id": "8PH000B1S052",
                    "dual_role": True,
                    "external_tanker_id": "ca673c580fb949a5b733f0e0b67ffab2",
                    "fuel_off": 15000000.1,
                    "id_tanker_airfield": "b33955d2-67d3-42be-8316-263e284ce6cc",
                    "id_tanker_mission": "edef700c-9917-4dbf-a153-89ffd4446fe9",
                    "id_tanker_sortie": "d833a4bc-756b-41d5-8845-f146fe563387",
                    "tanker_call_sign": "BAKER",
                    "tanker_cell_position": 2,
                    "tanker_coord": "TTC601",
                    "tanker_delivery_method": "DROGUE",
                    "tanker_deployed_icao": "KOFF",
                    "tanker_fuel_type": "JP8",
                    "tanker_leg_num": 825,
                    "tanker_mds": "KC135R",
                    "tanker_owner": "117ARW",
                    "tanker_poc": "JOHN SMITH (555)555-5555",
                }
            ],
            track_time=1.5,
        )
        assert air_event is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert air_event is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )
        assert air_event is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
            body_id="026dd511-8ba5-47d3-9909-836149f87686",
            actual_arr_time=parse_datetime("2024-01-07T14:00:03.123Z"),
            actual_dep_time=parse_datetime("2024-01-07T14:17:03.123Z"),
            arct=parse_datetime("2024-01-07T15:11:27.123Z"),
            ar_event_type="V",
            arr_purpose="A",
            ar_track_id="CH61",
            ar_track_name="CH61 POST",
            base_alt=28000.1,
            cancelled=False,
            dep_purpose="Q",
            est_arr_time=parse_datetime("2024-01-07T13:59:48.123Z"),
            est_dep_time=parse_datetime("2024-01-07T14:19:48.123Z"),
            external_air_event_id="MB014313032022407540",
            external_ar_track_id="6418a4b68e5c3896bf024cc79aa4174c",
            id_mission="190dea6d-2a90-45a2-a276-be9047d9b96c",
            id_sortie="b9866c03-2397-4506-8153-852e72d9b54f",
            leg_num=825,
            location="901EW",
            num_tankers=1,
            origin="THIRD_PARTY_DATASOURCE",
            planned_arr_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            planned_dep_time=parse_datetime("2024-01-07T14:15:43.123Z"),
            priority="1A2",
            receivers=[
                {
                    "alt_receiver_mission_id": "1UN05201L121",
                    "amc_receiver_mission_id": "8PH000B1S052",
                    "external_receiver_id": "3fb8169f-adc1-4667-acab-8415a012d766",
                    "fuel_on": 15000000.1,
                    "id_receiver_airfield": "96c4c2ba-a031-4e58-9b8e-3c6fb90a7534",
                    "id_receiver_mission": "ce99757d-f733-461f-8939-3939d4f05946",
                    "id_receiver_sortie": "1d03e85a-1fb9-4f6e-86a0-593306b6e3f0",
                    "num_rec_aircraft": 3,
                    "package_id": "135",
                    "receiver_call_sign": "BAKER",
                    "receiver_cell_position": 2,
                    "receiver_coord": "TTC601",
                    "receiver_delivery_method": "DROGUE",
                    "receiver_deployed_icao": "KOFF",
                    "receiver_exercise": "NATO19",
                    "receiver_fuel_type": "JP8",
                    "receiver_leg_num": 825,
                    "receiver_mds": "KC135R",
                    "receiver_owner": "117ARW",
                    "receiver_poc": "JOHN SMITH (555)555-5555",
                    "rec_org": "AMC",
                    "sequence_num": "1018",
                }
            ],
            remarks=[
                {
                    "date": parse_datetime("2024-01-01T01:01:01.123Z"),
                    "external_remark_id": "23ea2877a6f74d7d8f309567a5896441",
                    "text": "Example air event remarks.",
                    "user": "John Doe",
                }
            ],
            rev_track=True,
            rzct=parse_datetime("2024-01-07T13:55:43.123Z"),
            rz_point="AN",
            rz_type="PP",
            short_track=True,
            status_code="R",
            tankers=[
                {
                    "alt_tanker_mission_id": "1UN05201L121",
                    "amc_tanker_mission_id": "8PH000B1S052",
                    "dual_role": True,
                    "external_tanker_id": "ca673c580fb949a5b733f0e0b67ffab2",
                    "fuel_off": 15000000.1,
                    "id_tanker_airfield": "b33955d2-67d3-42be-8316-263e284ce6cc",
                    "id_tanker_mission": "edef700c-9917-4dbf-a153-89ffd4446fe9",
                    "id_tanker_sortie": "d833a4bc-756b-41d5-8845-f146fe563387",
                    "tanker_call_sign": "BAKER",
                    "tanker_cell_position": 2,
                    "tanker_coord": "TTC601",
                    "tanker_delivery_method": "DROGUE",
                    "tanker_deployed_icao": "KOFF",
                    "tanker_fuel_type": "JP8",
                    "tanker_leg_num": 825,
                    "tanker_mds": "KC135R",
                    "tanker_owner": "117ARW",
                    "tanker_poc": "JOHN SMITH (555)555-5555",
                }
            ],
            track_time=1.5,
        )
        assert air_event is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert air_event is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            type="FUEL TRANSFER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.air_events.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
                type="FUEL TRANSFER",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.list()
        assert_matches_type(AsyncOffsetPage[AirEventListResponse], air_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AirEventListResponse], air_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert_matches_type(AsyncOffsetPage[AirEventListResponse], air_event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert_matches_type(AsyncOffsetPage[AirEventListResponse], air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.delete(
            "id",
        )
        assert air_event is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert air_event is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.air_events.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.count()
        assert_matches_type(str, air_event, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, air_event, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert_matches_type(str, air_event, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert_matches_type(str, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )
        assert air_event is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert air_event is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.get(
            id="id",
        )
        assert_matches_type(AirEventGetResponse, air_event, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirEventGetResponse, air_event, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert_matches_type(AirEventGetResponse, air_event, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert_matches_type(AirEventGetResponse, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.air_events.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.queryhelp()
        assert_matches_type(AirEventQueryhelpResponse, air_event, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert_matches_type(AirEventQueryhelpResponse, air_event, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert_matches_type(AirEventQueryhelpResponse, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.tuple(
            columns="columns",
        )
        assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert_matches_type(AirEventTupleResponse, air_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_event = await async_client.air_events.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )
        assert air_event is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_events.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_event = await response.parse()
        assert air_event is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_events.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "type": "FUEL TRANSFER",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_event = await response.parse()
            assert air_event is None

        assert cast(Any, response.is_closed) is True
