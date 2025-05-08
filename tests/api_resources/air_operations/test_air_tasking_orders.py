# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.air_operations import (
    AirTaskingOrderFull,
    AirtaskingorderAbridged,
    AirTaskingOrderTupleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirTaskingOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
        )
        assert air_tasking_order is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
            id="POI-ID",
            ack_req_ind="YES",
            ack_unit_instructions="INST:45TS",
            ac_msn_tasking=[
                {
                    "country_code": "US",
                    "tasked_service": "A",
                    "unit_designator": "AMPHIB5DIV",
                    "ac_msn_loc_seg": [
                        {
                            "start_time": parse_datetime("2021-10-25T12:00:00.123Z"),
                            "air_msn_pri": "1A",
                            "alt": 210,
                            "area_geo_rad": 1000,
                            "end_time": parse_datetime("2021-10-25T12:00:00.123Z"),
                            "msn_loc_name": "KLSV",
                            "msn_loc_pt_bar_t": "330T-PT ALFA-50NM",
                            "msn_loc_pt_lat": 35.123,
                            "msn_loc_pt_lon": 79.01,
                            "msn_loc_pt_name": "PT ALFA",
                        }
                    ],
                    "alert_status": 30,
                    "amc_msn_num": "AMC:JJXD123HA045",
                    "dep_loc_lat": 35.123,
                    "dep_loc_lon": 79.2354,
                    "dep_loc_name": "ICAO:KBIF",
                    "dep_loc_utm": "32WDL123123",
                    "dep_time": parse_datetime("2021-10-25T12:00:00.123Z"),
                    "ind_ac_tasking": [
                        {
                            "acft_type": "F35A",
                            "call_sign": "EAGLE47",
                            "iff_sif_mode1_code": "111",
                            "iff_sif_mode2_code": "20147",
                            "iff_sif_mode3_code": "30147",
                            "ju_address": [12345, 65432],
                            "link16_call_sign": "EE47",
                            "num_acft": 2,
                            "pri_config_code": "6A2W3",
                            "sec_config_code": "2S2WG",
                            "tacan_chan": 123,
                        }
                    ],
                    "msn_commander": "MC",
                    "msn_num": "D123HA",
                    "pkg_id": "ZZ",
                    "pri_msn_type": "CAS",
                    "rcvy_loc_lat": [48.8584, 40.7554],
                    "rcvy_loc_lon": [2.2945, -73.9866],
                    "rcvy_loc_name": ["ARRLOC:KBIF", "ARRLOC:KDZ7"],
                    "rcvy_loc_utm": ["ARRUTMO:32WDL123123", "ARRUTMO:32WDL321321"],
                    "rcvy_time": [
                        parse_datetime("2021-10-25T16:00:00.234Z"),
                        parse_datetime("2021-10-26T16:00:00.234Z"),
                    ],
                    "res_msn_ind": "N",
                    "sec_msn_type": "SEAD",
                    "unit_loc_name": "ICAO:KXXQ",
                }
            ],
            end_ts=parse_datetime("2023-10-27T12:00:00.123Z"),
            gen_text=[
                {
                    "text": "FREE-TEXT",
                    "text_ind": "OPENING REMARKS",
                }
            ],
            msg_month="OCT",
            msg_originator="USCENTCOM",
            msg_qualifier="CHG",
            msg_sn="ATO A",
            naval_flt_ops=[
                {
                    "ship_name": "USS WASP",
                    "flt_op_start": parse_datetime("2021-02-25T12:00:00.123Z"),
                    "flt_op_stop": parse_datetime("2021-02-25T12:00:00.123Z"),
                    "schd_launch_rcvy_time": [parse_datetime("2021-02-25T12:00:00.123Z")],
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert air_tasking_order is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert air_tasking_order is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.retrieve(
            id="id",
        )
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.air_operations.air_tasking_orders.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.list()
        assert_matches_type(SyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert_matches_type(SyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert_matches_type(SyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.count()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert_matches_type(str, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.query_help()
        assert air_tasking_order is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert air_tasking_order is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        air_tasking_order = client.air_operations.air_tasking_orders.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )
        assert air_tasking_order is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.air_operations.air_tasking_orders.with_raw_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = response.parse()
        assert air_tasking_order is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.air_operations.air_tasking_orders.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAirTaskingOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
        )
        assert air_tasking_order is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
            id="POI-ID",
            ack_req_ind="YES",
            ack_unit_instructions="INST:45TS",
            ac_msn_tasking=[
                {
                    "country_code": "US",
                    "tasked_service": "A",
                    "unit_designator": "AMPHIB5DIV",
                    "ac_msn_loc_seg": [
                        {
                            "start_time": parse_datetime("2021-10-25T12:00:00.123Z"),
                            "air_msn_pri": "1A",
                            "alt": 210,
                            "area_geo_rad": 1000,
                            "end_time": parse_datetime("2021-10-25T12:00:00.123Z"),
                            "msn_loc_name": "KLSV",
                            "msn_loc_pt_bar_t": "330T-PT ALFA-50NM",
                            "msn_loc_pt_lat": 35.123,
                            "msn_loc_pt_lon": 79.01,
                            "msn_loc_pt_name": "PT ALFA",
                        }
                    ],
                    "alert_status": 30,
                    "amc_msn_num": "AMC:JJXD123HA045",
                    "dep_loc_lat": 35.123,
                    "dep_loc_lon": 79.2354,
                    "dep_loc_name": "ICAO:KBIF",
                    "dep_loc_utm": "32WDL123123",
                    "dep_time": parse_datetime("2021-10-25T12:00:00.123Z"),
                    "ind_ac_tasking": [
                        {
                            "acft_type": "F35A",
                            "call_sign": "EAGLE47",
                            "iff_sif_mode1_code": "111",
                            "iff_sif_mode2_code": "20147",
                            "iff_sif_mode3_code": "30147",
                            "ju_address": [12345, 65432],
                            "link16_call_sign": "EE47",
                            "num_acft": 2,
                            "pri_config_code": "6A2W3",
                            "sec_config_code": "2S2WG",
                            "tacan_chan": 123,
                        }
                    ],
                    "msn_commander": "MC",
                    "msn_num": "D123HA",
                    "pkg_id": "ZZ",
                    "pri_msn_type": "CAS",
                    "rcvy_loc_lat": [48.8584, 40.7554],
                    "rcvy_loc_lon": [2.2945, -73.9866],
                    "rcvy_loc_name": ["ARRLOC:KBIF", "ARRLOC:KDZ7"],
                    "rcvy_loc_utm": ["ARRUTMO:32WDL123123", "ARRUTMO:32WDL321321"],
                    "rcvy_time": [
                        parse_datetime("2021-10-25T16:00:00.234Z"),
                        parse_datetime("2021-10-26T16:00:00.234Z"),
                    ],
                    "res_msn_ind": "N",
                    "sec_msn_type": "SEAD",
                    "unit_loc_name": "ICAO:KXXQ",
                }
            ],
            end_ts=parse_datetime("2023-10-27T12:00:00.123Z"),
            gen_text=[
                {
                    "text": "FREE-TEXT",
                    "text_ind": "OPENING REMARKS",
                }
            ],
            msg_month="OCT",
            msg_originator="USCENTCOM",
            msg_qualifier="CHG",
            msg_sn="ATO A",
            naval_flt_ops=[
                {
                    "ship_name": "USS WASP",
                    "flt_op_start": parse_datetime("2021-02-25T12:00:00.123Z"),
                    "flt_op_stop": parse_datetime("2021-02-25T12:00:00.123Z"),
                    "schd_launch_rcvy_time": [parse_datetime("2021-02-25T12:00:00.123Z")],
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
        )
        assert air_tasking_order is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert air_tasking_order is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.create(
            begin_ts=parse_datetime("2023-10-25T12:00:00.123Z"),
            classification_marking="U",
            data_mode="TEST",
            op_exer_name="DESERT WIND",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.retrieve(
            id="id",
        )
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert_matches_type(AirTaskingOrderFull, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.air_operations.air_tasking_orders.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.list()
        assert_matches_type(AsyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert_matches_type(AsyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert_matches_type(AsyncOffsetPage[AirtaskingorderAbridged], air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.count()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert_matches_type(str, air_tasking_order, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert_matches_type(str, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.query_help()
        assert air_tasking_order is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert air_tasking_order is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert_matches_type(AirTaskingOrderTupleResponse, air_tasking_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_tasking_order = await async_client.air_operations.air_tasking_orders.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )
        assert air_tasking_order is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_operations.air_tasking_orders.with_raw_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_tasking_order = await response.parse()
        assert air_tasking_order is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_operations.air_tasking_orders.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "begin_ts": parse_datetime("2023-10-25T12:00:00.123Z"),
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_exer_name": "DESERT WIND",
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_tasking_order = await response.parse()
            assert air_tasking_order is None

        assert cast(Any, response.is_closed) is True
