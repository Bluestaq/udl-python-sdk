# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirspacecontrolorderAbridged,
    AirspaceControlOrderTupleResponse,
    AirspaceControlOrderQueryHelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import AirspacecontrolorderFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirspaceControlOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )
        assert airspace_control_order is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            id="c44b0a80-9fef-63d9-6267-79037fb93e4c",
            aco_comments="CHOKE POINTS",
            aco_serial_num="27B",
            airspace_control_means_status=[
                {
                    "airspace_control_means": [
                        {
                            "airspace_control_point": [
                                {
                                    "ctrl_pt_altitude": "BRFL:MSL-FL230",
                                    "ctrl_pt_location": "203632N0594256E",
                                    "ctrl_pt_name": "APPLE",
                                    "ctrl_pt_type": "CP",
                                }
                            ],
                            "airspace_time_period": [
                                {
                                    "int_dur": ["65WK"],
                                    "int_freq": ["WEEKLY"],
                                    "time_end": "141325ZFEB2002",
                                    "time_mode": "DISCRETE",
                                    "time_start": "141325ZFEB2002",
                                }
                            ],
                            "bearing0": 330,
                            "bearing1": 160,
                            "cm_id": "DESIG:C34",
                            "cm_shape": "POLYARC",
                            "cm_type": "cmType",
                            "cntrl_auth": "RHEIN MAIN CP",
                            "cntrl_auth_freqs": ["125.25MHZ"],
                            "coord0": "152345N0505657E",
                            "coord1": "1523N05057E",
                            "corr_way_points": ["POB", "RDU", "IAD"],
                            "eff_v_dim": "BRRA:GL-100AGL",
                            "free_text": "1. CAPACITY: MDM TK, 50 VEHICLE CONVOY. 2. CHOKE POINTS: EXIT 5",
                            "gen_text_ind": "SITUATION",
                            "geo_datum_alt": "NAR",
                            "link16_id": "F3356",
                            "orbit_alignment": "C",
                            "poly_coord": ["203632N0594256E", "155000N0594815E", "155000N0591343E"],
                            "rad_mag0": 30.04,
                            "rad_mag1": 50.12,
                            "rad_mag_unit": "NM",
                            "track_leg": 99,
                            "trans_altitude": "18000FT",
                            "usage": "usage",
                            "width": 15.6,
                            "width_left": 5.2,
                            "width_right": 10.4,
                            "width_unit": "KM",
                        }
                    ],
                    "cm_stat": "ADD",
                    "cm_stat_id": ["DESIGN:B35", "NAME:ERMA", "RANG:C21-C25"],
                }
            ],
            airspace_control_order_references=[
                {
                    "ref_originator": "SHAPE",
                    "ref_serial_num": "100",
                    "ref_si_cs": ["RCA", "FN:4503B"],
                    "ref_s_id": "A",
                    "ref_special_notation": "NOTAL",
                    "ref_ts": parse_datetime("2024-01-07T13:55:43.123Z"),
                    "ref_type": "NBC1",
                }
            ],
            area_of_validity="FORT BRAGG",
            class_reasons=["15C", "10C"],
            class_source="ORIG:USJFCOM",
            declass_exemption_codes=["X1", "X2"],
            downgrade_ins_dates=["NST:AT EXERCISE ENDEX", "DATE:25NOV1997"],
            geo_datum="EUR-T",
            month="OCT",
            op_ex_info="CONTROL",
            op_ex_info_alt="ORANGE",
            origin="THIRD_PARTY_DATASOURCE",
            plan_orig_num="SACEUR 106",
            qualifier="CHG",
            qual_sn=1,
            serial_num="1201003",
            stop_qualifier="AFTER",
            stop_time=parse_datetime("2024-01-08T13:55:43.123Z"),
            und_lnk_trks=["A2467", "A3466", "AA232"],
        )
        assert airspace_control_order is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert airspace_control_order is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.retrieve(
            id="id",
        )
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airspace_control_orders.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.list()
        assert_matches_type(SyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(SyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(SyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.count()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(str, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )
        assert airspace_control_order is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert airspace_control_order is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.query_help()
        assert_matches_type(AirspaceControlOrderQueryHelpResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(AirspaceControlOrderQueryHelpResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(AirspaceControlOrderQueryHelpResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        airspace_control_order = client.airspace_control_orders.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.airspace_control_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = response.parse()
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.airspace_control_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = response.parse()
            assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirspaceControlOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )
        assert airspace_control_order is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
            id="c44b0a80-9fef-63d9-6267-79037fb93e4c",
            aco_comments="CHOKE POINTS",
            aco_serial_num="27B",
            airspace_control_means_status=[
                {
                    "airspace_control_means": [
                        {
                            "airspace_control_point": [
                                {
                                    "ctrl_pt_altitude": "BRFL:MSL-FL230",
                                    "ctrl_pt_location": "203632N0594256E",
                                    "ctrl_pt_name": "APPLE",
                                    "ctrl_pt_type": "CP",
                                }
                            ],
                            "airspace_time_period": [
                                {
                                    "int_dur": ["65WK"],
                                    "int_freq": ["WEEKLY"],
                                    "time_end": "141325ZFEB2002",
                                    "time_mode": "DISCRETE",
                                    "time_start": "141325ZFEB2002",
                                }
                            ],
                            "bearing0": 330,
                            "bearing1": 160,
                            "cm_id": "DESIG:C34",
                            "cm_shape": "POLYARC",
                            "cm_type": "cmType",
                            "cntrl_auth": "RHEIN MAIN CP",
                            "cntrl_auth_freqs": ["125.25MHZ"],
                            "coord0": "152345N0505657E",
                            "coord1": "1523N05057E",
                            "corr_way_points": ["POB", "RDU", "IAD"],
                            "eff_v_dim": "BRRA:GL-100AGL",
                            "free_text": "1. CAPACITY: MDM TK, 50 VEHICLE CONVOY. 2. CHOKE POINTS: EXIT 5",
                            "gen_text_ind": "SITUATION",
                            "geo_datum_alt": "NAR",
                            "link16_id": "F3356",
                            "orbit_alignment": "C",
                            "poly_coord": ["203632N0594256E", "155000N0594815E", "155000N0591343E"],
                            "rad_mag0": 30.04,
                            "rad_mag1": 50.12,
                            "rad_mag_unit": "NM",
                            "track_leg": 99,
                            "trans_altitude": "18000FT",
                            "usage": "usage",
                            "width": 15.6,
                            "width_left": 5.2,
                            "width_right": 10.4,
                            "width_unit": "KM",
                        }
                    ],
                    "cm_stat": "ADD",
                    "cm_stat_id": ["DESIGN:B35", "NAME:ERMA", "RANG:C21-C25"],
                }
            ],
            airspace_control_order_references=[
                {
                    "ref_originator": "SHAPE",
                    "ref_serial_num": "100",
                    "ref_si_cs": ["RCA", "FN:4503B"],
                    "ref_s_id": "A",
                    "ref_special_notation": "NOTAL",
                    "ref_ts": parse_datetime("2024-01-07T13:55:43.123Z"),
                    "ref_type": "NBC1",
                }
            ],
            area_of_validity="FORT BRAGG",
            class_reasons=["15C", "10C"],
            class_source="ORIG:USJFCOM",
            declass_exemption_codes=["X1", "X2"],
            downgrade_ins_dates=["NST:AT EXERCISE ENDEX", "DATE:25NOV1997"],
            geo_datum="EUR-T",
            month="OCT",
            op_ex_info="CONTROL",
            op_ex_info_alt="ORANGE",
            origin="THIRD_PARTY_DATASOURCE",
            plan_orig_num="SACEUR 106",
            qualifier="CHG",
            qual_sn=1,
            serial_num="1201003",
            stop_qualifier="AFTER",
            stop_time=parse_datetime("2024-01-08T13:55:43.123Z"),
            und_lnk_trks=["A2467", "A3466", "AA232"],
        )
        assert airspace_control_order is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert airspace_control_order is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            op_ex_name="DESERT WIND",
            originator="USCENTCOM",
            source="Bluestaq",
            start_time=parse_datetime("2024-01-07T13:55:43.123Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.retrieve(
            id="id",
        )
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(AirspacecontrolorderFull, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airspace_control_orders.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.list()
        assert_matches_type(AsyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(AsyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(
                AsyncOffsetPage[AirspacecontrolorderAbridged], airspace_control_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.count()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(str, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(str, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )
        assert airspace_control_order is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert airspace_control_order is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "op_ex_name": "DESERT WIND",
                    "originator": "USCENTCOM",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2024-01-07T13:55:43.123Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert airspace_control_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.query_help()
        assert_matches_type(AirspaceControlOrderQueryHelpResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(AirspaceControlOrderQueryHelpResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(AirspaceControlOrderQueryHelpResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.tuple(
            columns="columns",
        )
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airspace_control_order = await async_client.airspace_control_orders.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airspace_control_orders.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airspace_control_order = await response.parse()
        assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airspace_control_orders.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airspace_control_order = await response.parse()
            assert_matches_type(AirspaceControlOrderTupleResponse, airspace_control_order, path=["response"])

        assert cast(Any, response.is_closed) is True
