# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    LogisticsSupportGetResponse,
    LogisticsSupportListResponse,
    LogisticsSupportTupleResponse,
    LogisticsSupportQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogisticsSupport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )
        assert logistics_support is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
            id="LOGISTICS-SUPPORT-DETAILS UUID",
            aircraft_mds="CO17A",
            curr_icao="KCOS",
            etic=parse_datetime("2023-07-13T13:47:00.123Z"),
            etmc=parse_datetime("2023-07-13T13:47:00.123Z"),
            ext_system_id="GDSSBL012307131347070165",
            logistic_action="WA",
            logistics_discrepancy_infos=[
                {
                    "closure_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "discrepancy_info": "PILOT WINDSHIELD PANEL ASSY CRACKED, AND ARCING REQ R2 IAW 56.11.10",
                    "jcn": "231942400",
                    "job_st_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                }
            ],
            logistics_record_id="L62017",
            logistics_remarks=[
                {
                    "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "remark": "EXAMPLE REMARK",
                    "username": "JSMITH",
                }
            ],
            logistics_support_items=[
                {
                    "cannibalized": True,
                    "deploy_plan_number": "T89003",
                    "description": "HOIST ADAPTER KIT",
                    "item_last_changed_date": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "job_control_number": "231942400",
                    "logistics_parts": [
                        {
                            "figure_number": "3",
                            "index_number": "4",
                            "location_verifier": "JANE DOE",
                            "logistics_stocks": [
                                {
                                    "quantity": 4,
                                    "source_icao": "PHIK",
                                    "stock_check_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                                    "stock_poc": "SMITH, JOHN J",
                                }
                            ],
                            "measurement_unit_code": "EA",
                            "national_stock_number": "5310-00-045-3299",
                            "part_number": "MS35338-42",
                            "request_verifier": "JOHN SMITH",
                            "supply_document_number": "J223FU31908300",
                            "technical_order_text": "1C-17A-4",
                            "work_unit_code": "5611UU001",
                        }
                    ],
                    "logistics_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "logistics_specialties": [
                        {
                            "first_name": "JOHN",
                            "last4_ssn": "9999",
                            "last_name": "SMITH",
                            "rank_code": "MAJ",
                            "role_type_code": "TC",
                            "skill_level": 3,
                            "specialty": "ELEN",
                        }
                    ],
                    "quantity": 1,
                    "ready_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "received_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "recovery_request_type_code": "E",
                    "redeploy_plan_number": "T89003",
                    "redeploy_shipment_unit_id": "X400LA31949108",
                    "request_number": "89208",
                    "resupport_flag": True,
                    "shipment_unit_id": "FB44273196X501XXX",
                    "si_poc": "SMITH, JOHN J",
                    "source_icao": "PHIK",
                }
            ],
            logistics_transportation_plans=[
                {
                    "act_dep_time": parse_datetime("2023-07-14T19:37:00.123Z"),
                    "aircraft_status": "NMCMU",
                    "approx_arr_time": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "cancelled_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "closed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "coordinator": "SMITH, JOHN",
                    "coordinator_unit": "TACC",
                    "destination_icao": "YBCS",
                    "duration": "086:20",
                    "est_arr_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "est_dep_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "last_changed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "logistic_master_record_id": "L62126",
                    "logistics_segments": [
                        {
                            "arrival_icao": "YBCS",
                            "departure_icao": "PHIK",
                            "ext_mission_id": "2001101RF01202307062205",
                            "id_mission": "EXAMPLE-UUID",
                            "itin": 200,
                            "mission_number": "TAM308901196",
                            "mission_type": "SAAM",
                            "mode_code": "A",
                            "seg_act_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_act_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_aircraft_mds": "B7772E",
                            "seg_est_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_est_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "segment_number": 3,
                            "seg_tail_number": "N819AX",
                        }
                    ],
                    "logistics_transportation_plans_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "majcom": "HQAMC",
                    "mission_change": False,
                    "num_enroute_stops": 4,
                    "num_trans_loads": 3,
                    "origin_icao": "KATL",
                    "plan_definition": "DEPLOY",
                    "plans_number": "T89002",
                    "serial_number": "9009209",
                    "status_code": "N",
                    "tp_aircraft_mds": "C17A",
                    "tp_tail_number": "99209",
                }
            ],
            maint_status_code="NMCMU",
            mc_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            me_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="EXAMPLE_OWNER",
            reopen_flag=True,
            rpt_closed_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            supp_icao="KCOS",
            tail_number="99290",
        )
        assert logistics_support is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert logistics_support is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )
        assert logistics_support is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
            body_id="LOGISTICS-SUPPORT-DETAILS UUID",
            aircraft_mds="CO17A",
            curr_icao="KCOS",
            etic=parse_datetime("2023-07-13T13:47:00.123Z"),
            etmc=parse_datetime("2023-07-13T13:47:00.123Z"),
            ext_system_id="GDSSBL012307131347070165",
            logistic_action="WA",
            logistics_discrepancy_infos=[
                {
                    "closure_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "discrepancy_info": "PILOT WINDSHIELD PANEL ASSY CRACKED, AND ARCING REQ R2 IAW 56.11.10",
                    "jcn": "231942400",
                    "job_st_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                }
            ],
            logistics_record_id="L62017",
            logistics_remarks=[
                {
                    "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "remark": "EXAMPLE REMARK",
                    "username": "JSMITH",
                }
            ],
            logistics_support_items=[
                {
                    "cannibalized": True,
                    "deploy_plan_number": "T89003",
                    "description": "HOIST ADAPTER KIT",
                    "item_last_changed_date": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "job_control_number": "231942400",
                    "logistics_parts": [
                        {
                            "figure_number": "3",
                            "index_number": "4",
                            "location_verifier": "JANE DOE",
                            "logistics_stocks": [
                                {
                                    "quantity": 4,
                                    "source_icao": "PHIK",
                                    "stock_check_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                                    "stock_poc": "SMITH, JOHN J",
                                }
                            ],
                            "measurement_unit_code": "EA",
                            "national_stock_number": "5310-00-045-3299",
                            "part_number": "MS35338-42",
                            "request_verifier": "JOHN SMITH",
                            "supply_document_number": "J223FU31908300",
                            "technical_order_text": "1C-17A-4",
                            "work_unit_code": "5611UU001",
                        }
                    ],
                    "logistics_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "logistics_specialties": [
                        {
                            "first_name": "JOHN",
                            "last4_ssn": "9999",
                            "last_name": "SMITH",
                            "rank_code": "MAJ",
                            "role_type_code": "TC",
                            "skill_level": 3,
                            "specialty": "ELEN",
                        }
                    ],
                    "quantity": 1,
                    "ready_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "received_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "recovery_request_type_code": "E",
                    "redeploy_plan_number": "T89003",
                    "redeploy_shipment_unit_id": "X400LA31949108",
                    "request_number": "89208",
                    "resupport_flag": True,
                    "shipment_unit_id": "FB44273196X501XXX",
                    "si_poc": "SMITH, JOHN J",
                    "source_icao": "PHIK",
                }
            ],
            logistics_transportation_plans=[
                {
                    "act_dep_time": parse_datetime("2023-07-14T19:37:00.123Z"),
                    "aircraft_status": "NMCMU",
                    "approx_arr_time": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "cancelled_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "closed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "coordinator": "SMITH, JOHN",
                    "coordinator_unit": "TACC",
                    "destination_icao": "YBCS",
                    "duration": "086:20",
                    "est_arr_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "est_dep_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "last_changed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "logistic_master_record_id": "L62126",
                    "logistics_segments": [
                        {
                            "arrival_icao": "YBCS",
                            "departure_icao": "PHIK",
                            "ext_mission_id": "2001101RF01202307062205",
                            "id_mission": "EXAMPLE-UUID",
                            "itin": 200,
                            "mission_number": "TAM308901196",
                            "mission_type": "SAAM",
                            "mode_code": "A",
                            "seg_act_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_act_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_aircraft_mds": "B7772E",
                            "seg_est_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_est_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "segment_number": 3,
                            "seg_tail_number": "N819AX",
                        }
                    ],
                    "logistics_transportation_plans_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "majcom": "HQAMC",
                    "mission_change": False,
                    "num_enroute_stops": 4,
                    "num_trans_loads": 3,
                    "origin_icao": "KATL",
                    "plan_definition": "DEPLOY",
                    "plans_number": "T89002",
                    "serial_number": "9009209",
                    "status_code": "N",
                    "tp_aircraft_mds": "C17A",
                    "tp_tail_number": "99209",
                }
            ],
            maint_status_code="NMCMU",
            mc_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            me_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="EXAMPLE_OWNER",
            reopen_flag=True,
            rpt_closed_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            supp_icao="KCOS",
            tail_number="99290",
        )
        assert logistics_support is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert logistics_support is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.logistics_support.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.list()
        assert_matches_type(SyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert_matches_type(SyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert_matches_type(SyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.count()
        assert_matches_type(str, logistics_support, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, logistics_support, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert_matches_type(str, logistics_support, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert_matches_type(str, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert logistics_support is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert logistics_support is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.get(
            id="id",
        )
        assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.logistics_support.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.queryhelp()
        assert_matches_type(LogisticsSupportQueryhelpResponse, logistics_support, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert_matches_type(LogisticsSupportQueryhelpResponse, logistics_support, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert_matches_type(LogisticsSupportQueryhelpResponse, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.tuple(
            columns="columns",
        )
        assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        logistics_support = client.logistics_support.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert logistics_support is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.logistics_support.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = response.parse()
        assert logistics_support is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.logistics_support.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLogisticsSupport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )
        assert logistics_support is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
            id="LOGISTICS-SUPPORT-DETAILS UUID",
            aircraft_mds="CO17A",
            curr_icao="KCOS",
            etic=parse_datetime("2023-07-13T13:47:00.123Z"),
            etmc=parse_datetime("2023-07-13T13:47:00.123Z"),
            ext_system_id="GDSSBL012307131347070165",
            logistic_action="WA",
            logistics_discrepancy_infos=[
                {
                    "closure_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "discrepancy_info": "PILOT WINDSHIELD PANEL ASSY CRACKED, AND ARCING REQ R2 IAW 56.11.10",
                    "jcn": "231942400",
                    "job_st_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                }
            ],
            logistics_record_id="L62017",
            logistics_remarks=[
                {
                    "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "remark": "EXAMPLE REMARK",
                    "username": "JSMITH",
                }
            ],
            logistics_support_items=[
                {
                    "cannibalized": True,
                    "deploy_plan_number": "T89003",
                    "description": "HOIST ADAPTER KIT",
                    "item_last_changed_date": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "job_control_number": "231942400",
                    "logistics_parts": [
                        {
                            "figure_number": "3",
                            "index_number": "4",
                            "location_verifier": "JANE DOE",
                            "logistics_stocks": [
                                {
                                    "quantity": 4,
                                    "source_icao": "PHIK",
                                    "stock_check_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                                    "stock_poc": "SMITH, JOHN J",
                                }
                            ],
                            "measurement_unit_code": "EA",
                            "national_stock_number": "5310-00-045-3299",
                            "part_number": "MS35338-42",
                            "request_verifier": "JOHN SMITH",
                            "supply_document_number": "J223FU31908300",
                            "technical_order_text": "1C-17A-4",
                            "work_unit_code": "5611UU001",
                        }
                    ],
                    "logistics_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "logistics_specialties": [
                        {
                            "first_name": "JOHN",
                            "last4_ssn": "9999",
                            "last_name": "SMITH",
                            "rank_code": "MAJ",
                            "role_type_code": "TC",
                            "skill_level": 3,
                            "specialty": "ELEN",
                        }
                    ],
                    "quantity": 1,
                    "ready_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "received_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "recovery_request_type_code": "E",
                    "redeploy_plan_number": "T89003",
                    "redeploy_shipment_unit_id": "X400LA31949108",
                    "request_number": "89208",
                    "resupport_flag": True,
                    "shipment_unit_id": "FB44273196X501XXX",
                    "si_poc": "SMITH, JOHN J",
                    "source_icao": "PHIK",
                }
            ],
            logistics_transportation_plans=[
                {
                    "act_dep_time": parse_datetime("2023-07-14T19:37:00.123Z"),
                    "aircraft_status": "NMCMU",
                    "approx_arr_time": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "cancelled_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "closed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "coordinator": "SMITH, JOHN",
                    "coordinator_unit": "TACC",
                    "destination_icao": "YBCS",
                    "duration": "086:20",
                    "est_arr_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "est_dep_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "last_changed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "logistic_master_record_id": "L62126",
                    "logistics_segments": [
                        {
                            "arrival_icao": "YBCS",
                            "departure_icao": "PHIK",
                            "ext_mission_id": "2001101RF01202307062205",
                            "id_mission": "EXAMPLE-UUID",
                            "itin": 200,
                            "mission_number": "TAM308901196",
                            "mission_type": "SAAM",
                            "mode_code": "A",
                            "seg_act_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_act_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_aircraft_mds": "B7772E",
                            "seg_est_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_est_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "segment_number": 3,
                            "seg_tail_number": "N819AX",
                        }
                    ],
                    "logistics_transportation_plans_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "majcom": "HQAMC",
                    "mission_change": False,
                    "num_enroute_stops": 4,
                    "num_trans_loads": 3,
                    "origin_icao": "KATL",
                    "plan_definition": "DEPLOY",
                    "plans_number": "T89002",
                    "serial_number": "9009209",
                    "status_code": "N",
                    "tp_aircraft_mds": "C17A",
                    "tp_tail_number": "99209",
                }
            ],
            maint_status_code="NMCMU",
            mc_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            me_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="EXAMPLE_OWNER",
            reopen_flag=True,
            rpt_closed_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            supp_icao="KCOS",
            tail_number="99290",
        )
        assert logistics_support is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert logistics_support is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )
        assert logistics_support is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
            body_id="LOGISTICS-SUPPORT-DETAILS UUID",
            aircraft_mds="CO17A",
            curr_icao="KCOS",
            etic=parse_datetime("2023-07-13T13:47:00.123Z"),
            etmc=parse_datetime("2023-07-13T13:47:00.123Z"),
            ext_system_id="GDSSBL012307131347070165",
            logistic_action="WA",
            logistics_discrepancy_infos=[
                {
                    "closure_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "discrepancy_info": "PILOT WINDSHIELD PANEL ASSY CRACKED, AND ARCING REQ R2 IAW 56.11.10",
                    "jcn": "231942400",
                    "job_st_time": parse_datetime("2023-07-17T10:30:00.123Z"),
                }
            ],
            logistics_record_id="L62017",
            logistics_remarks=[
                {
                    "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                    "remark": "EXAMPLE REMARK",
                    "username": "JSMITH",
                }
            ],
            logistics_support_items=[
                {
                    "cannibalized": True,
                    "deploy_plan_number": "T89003",
                    "description": "HOIST ADAPTER KIT",
                    "item_last_changed_date": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "job_control_number": "231942400",
                    "logistics_parts": [
                        {
                            "figure_number": "3",
                            "index_number": "4",
                            "location_verifier": "JANE DOE",
                            "logistics_stocks": [
                                {
                                    "quantity": 4,
                                    "source_icao": "PHIK",
                                    "stock_check_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                                    "stock_poc": "SMITH, JOHN J",
                                }
                            ],
                            "measurement_unit_code": "EA",
                            "national_stock_number": "5310-00-045-3299",
                            "part_number": "MS35338-42",
                            "request_verifier": "JOHN SMITH",
                            "supply_document_number": "J223FU31908300",
                            "technical_order_text": "1C-17A-4",
                            "work_unit_code": "5611UU001",
                        }
                    ],
                    "logistics_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "logistics_specialties": [
                        {
                            "first_name": "JOHN",
                            "last4_ssn": "9999",
                            "last_name": "SMITH",
                            "rank_code": "MAJ",
                            "role_type_code": "TC",
                            "skill_level": 3,
                            "specialty": "ELEN",
                        }
                    ],
                    "quantity": 1,
                    "ready_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "received_time": parse_datetime("2023-07-17T19:04:00.123Z"),
                    "recovery_request_type_code": "E",
                    "redeploy_plan_number": "T89003",
                    "redeploy_shipment_unit_id": "X400LA31949108",
                    "request_number": "89208",
                    "resupport_flag": True,
                    "shipment_unit_id": "FB44273196X501XXX",
                    "si_poc": "SMITH, JOHN J",
                    "source_icao": "PHIK",
                }
            ],
            logistics_transportation_plans=[
                {
                    "act_dep_time": parse_datetime("2023-07-14T19:37:00.123Z"),
                    "aircraft_status": "NMCMU",
                    "approx_arr_time": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "cancelled_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "closed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "coordinator": "SMITH, JOHN",
                    "coordinator_unit": "TACC",
                    "destination_icao": "YBCS",
                    "duration": "086:20",
                    "est_arr_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "est_dep_time": parse_datetime("2023-07-15T14:25:00.123Z"),
                    "last_changed_date": parse_datetime("2023-07-14T20:37:00.123Z"),
                    "logistic_master_record_id": "L62126",
                    "logistics_segments": [
                        {
                            "arrival_icao": "YBCS",
                            "departure_icao": "PHIK",
                            "ext_mission_id": "2001101RF01202307062205",
                            "id_mission": "EXAMPLE-UUID",
                            "itin": 200,
                            "mission_number": "TAM308901196",
                            "mission_type": "SAAM",
                            "mode_code": "A",
                            "seg_act_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_act_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_aircraft_mds": "B7772E",
                            "seg_est_arr_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "seg_est_dep_time": parse_datetime("2023-07-17T19:20:00.123Z"),
                            "segment_number": 3,
                            "seg_tail_number": "N819AX",
                        }
                    ],
                    "logistics_transportation_plans_remarks": [
                        {
                            "last_changed": parse_datetime("2023-07-17T10:30:00.123Z"),
                            "remark": "EXAMPLE REMARK",
                            "username": "JSMITH",
                        }
                    ],
                    "majcom": "HQAMC",
                    "mission_change": False,
                    "num_enroute_stops": 4,
                    "num_trans_loads": 3,
                    "origin_icao": "KATL",
                    "plan_definition": "DEPLOY",
                    "plans_number": "T89002",
                    "serial_number": "9009209",
                    "status_code": "N",
                    "tp_aircraft_mds": "C17A",
                    "tp_tail_number": "99209",
                }
            ],
            maint_status_code="NMCMU",
            mc_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            me_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            origin="THIRD_PARTY_DATASOURCE",
            owner="EXAMPLE_OWNER",
            reopen_flag=True,
            rpt_closed_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            supp_icao="KCOS",
            tail_number="99290",
        )
        assert logistics_support is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert logistics_support is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.logistics_support.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                rpt_created_time=parse_datetime("2023-07-13T13:47:00.123Z"),
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.list()
        assert_matches_type(AsyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert_matches_type(AsyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert_matches_type(AsyncOffsetPage[LogisticsSupportListResponse], logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.count()
        assert_matches_type(str, logistics_support, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, logistics_support, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert_matches_type(str, logistics_support, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert_matches_type(str, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert logistics_support is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert logistics_support is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.get(
            id="id",
        )
        assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert_matches_type(LogisticsSupportGetResponse, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.logistics_support.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.queryhelp()
        assert_matches_type(LogisticsSupportQueryhelpResponse, logistics_support, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert_matches_type(LogisticsSupportQueryhelpResponse, logistics_support, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert_matches_type(LogisticsSupportQueryhelpResponse, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.tuple(
            columns="columns",
        )
        assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert_matches_type(LogisticsSupportTupleResponse, logistics_support, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        logistics_support = await async_client.logistics_support.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert logistics_support is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.logistics_support.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logistics_support = await response.parse()
        assert logistics_support is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.logistics_support.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "rpt_created_time": parse_datetime("2023-07-13T13:47:00.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logistics_support = await response.parse()
            assert logistics_support is None

        assert cast(Any, response.is_closed) is True
