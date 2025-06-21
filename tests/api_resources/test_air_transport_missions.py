# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirTransportMissionAbridged,
    AirTransportMissionTupleResponse,
    AirTransportMissionQueryhelpResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import AirTransportMissionFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirTransportMissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert air_transport_mission is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="bdad6945-c9e4-b829-f7be-1ad075541921",
            abp="ZZ12",
            alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            allocated_unit="437 AEW",
            amc_mission_id="AJM7939B1123",
            apacs_id="1083034",
            ato_call_sign="CHARLIE",
            ato_mission_id="8900",
            call_sign="RCH123",
            cw=True,
            dip_worksheet_name="G2-182402-AB",
            first_pick_up="KFAY",
            gdss_mission_id="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            haz_mat=[
                {
                    "applicable_notes": "11,12",
                    "cgc": "A",
                    "cgn": "4,5,7,8",
                    "class_div": 1.1,
                    "ext_haz_mat_id": "cb6289e0f38534e01291ab6421d42724",
                    "item_name": "LITHIUM METAL BATTERIES",
                    "net_exp_wt": 12.1,
                    "off_icao": "MBPV",
                    "off_itin": 300,
                    "on_icao": "LIRQ",
                    "on_itin": 50,
                    "pieces": 29,
                    "planned": "P",
                    "un_num": "0181",
                    "weight": 22.1,
                }
            ],
            jcs_priority="1A3",
            last_drop_off="PGUA",
            load_category_type="MIXED",
            m1="11",
            m2="3214",
            m3a="6655",
            naf="18AF",
            next_amc_mission_id="AJM7939B1124",
            next_mission_id="186e5658-1079-45c0-bccc-02d2fa31b663",
            node="45TEST",
            objective="Deliver water to island X.",
            operation="Golden Eye",
            origin="THIRD_PARTY_DATASOURCE",
            orig_mission_id="614bebb6-a62e-053c-ca51-e79f8a402b28",
            prev_amc_mission_id="AJM7939B1122",
            prev_mission_id="a77055df-edc3-4047-a5fa-604f80b9fe3c",
            purpose="People at island X need water ASAP. Two previous attempts failed due to weather.",
            remarks=[
                {
                    "date": parse_datetime("2022-01-01T16:00:00.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "itinerary_num": 825,
                    "text": "Example mission remarks.",
                    "type": "MP",
                    "user": "John Doe",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 1.3,
                    "ead": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gdss_req_id": "23a1fb67-cc2d-5ebe-6b99-68130cb1aa6c",
                    "lad": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "num_ambulatory": 10,
                    "num_attendant": 10,
                    "num_litter": 10,
                    "num_pax": 44,
                    "offload_id": 300,
                    "offload_lo_code": "KHOP",
                    "onload_id": 200,
                    "onload_lo_code": "KCHS",
                    "oplan": "5027",
                    "outsize_weight": 1.3,
                    "oversize_weight": 1.3,
                    "proj_name": "CENTINTRA21",
                    "trans_req_num": "T01ME01",
                    "uln": "T01ME01",
                }
            ],
            source_sys_deviation=-90.12,
            state="EXECUTION",
            type="SAAM",
        )
        assert air_transport_mission is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert air_transport_mission is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.retrieve(
            id="id",
        )
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.air_transport_missions.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert air_transport_mission is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="bdad6945-c9e4-b829-f7be-1ad075541921",
            abp="ZZ12",
            alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            allocated_unit="437 AEW",
            amc_mission_id="AJM7939B1123",
            apacs_id="1083034",
            ato_call_sign="CHARLIE",
            ato_mission_id="8900",
            call_sign="RCH123",
            cw=True,
            dip_worksheet_name="G2-182402-AB",
            first_pick_up="KFAY",
            gdss_mission_id="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            haz_mat=[
                {
                    "applicable_notes": "11,12",
                    "cgc": "A",
                    "cgn": "4,5,7,8",
                    "class_div": 1.1,
                    "ext_haz_mat_id": "cb6289e0f38534e01291ab6421d42724",
                    "item_name": "LITHIUM METAL BATTERIES",
                    "net_exp_wt": 12.1,
                    "off_icao": "MBPV",
                    "off_itin": 300,
                    "on_icao": "LIRQ",
                    "on_itin": 50,
                    "pieces": 29,
                    "planned": "P",
                    "un_num": "0181",
                    "weight": 22.1,
                }
            ],
            jcs_priority="1A3",
            last_drop_off="PGUA",
            load_category_type="MIXED",
            m1="11",
            m2="3214",
            m3a="6655",
            naf="18AF",
            next_amc_mission_id="AJM7939B1124",
            next_mission_id="186e5658-1079-45c0-bccc-02d2fa31b663",
            node="45TEST",
            objective="Deliver water to island X.",
            operation="Golden Eye",
            origin="THIRD_PARTY_DATASOURCE",
            orig_mission_id="614bebb6-a62e-053c-ca51-e79f8a402b28",
            prev_amc_mission_id="AJM7939B1122",
            prev_mission_id="a77055df-edc3-4047-a5fa-604f80b9fe3c",
            purpose="People at island X need water ASAP. Two previous attempts failed due to weather.",
            remarks=[
                {
                    "date": parse_datetime("2022-01-01T16:00:00.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "itinerary_num": 825,
                    "text": "Example mission remarks.",
                    "type": "MP",
                    "user": "John Doe",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 1.3,
                    "ead": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gdss_req_id": "23a1fb67-cc2d-5ebe-6b99-68130cb1aa6c",
                    "lad": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "num_ambulatory": 10,
                    "num_attendant": 10,
                    "num_litter": 10,
                    "num_pax": 44,
                    "offload_id": 300,
                    "offload_lo_code": "KHOP",
                    "onload_id": 200,
                    "onload_lo_code": "KCHS",
                    "oplan": "5027",
                    "outsize_weight": 1.3,
                    "oversize_weight": 1.3,
                    "proj_name": "CENTINTRA21",
                    "trans_req_num": "T01ME01",
                    "uln": "T01ME01",
                }
            ],
            source_sys_deviation=-90.12,
            state="EXECUTION",
            type="SAAM",
        )
        assert air_transport_mission is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert air_transport_mission is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.air_transport_missions.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert_matches_type(SyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert_matches_type(SyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, air_transport_mission, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, air_transport_mission, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert_matches_type(str, air_transport_mission, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert_matches_type(str, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.queryhelp()
        assert_matches_type(AirTransportMissionQueryhelpResponse, air_transport_mission, path=["response"])

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert_matches_type(AirTransportMissionQueryhelpResponse, air_transport_mission, path=["response"])

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert_matches_type(AirTransportMissionQueryhelpResponse, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirTransportMissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            id="bdad6945-c9e4-b829-f7be-1ad075541921",
            abp="ZZ12",
            alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            allocated_unit="437 AEW",
            amc_mission_id="AJM7939B1123",
            apacs_id="1083034",
            ato_call_sign="CHARLIE",
            ato_mission_id="8900",
            call_sign="RCH123",
            cw=True,
            dip_worksheet_name="G2-182402-AB",
            first_pick_up="KFAY",
            gdss_mission_id="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            haz_mat=[
                {
                    "applicable_notes": "11,12",
                    "cgc": "A",
                    "cgn": "4,5,7,8",
                    "class_div": 1.1,
                    "ext_haz_mat_id": "cb6289e0f38534e01291ab6421d42724",
                    "item_name": "LITHIUM METAL BATTERIES",
                    "net_exp_wt": 12.1,
                    "off_icao": "MBPV",
                    "off_itin": 300,
                    "on_icao": "LIRQ",
                    "on_itin": 50,
                    "pieces": 29,
                    "planned": "P",
                    "un_num": "0181",
                    "weight": 22.1,
                }
            ],
            jcs_priority="1A3",
            last_drop_off="PGUA",
            load_category_type="MIXED",
            m1="11",
            m2="3214",
            m3a="6655",
            naf="18AF",
            next_amc_mission_id="AJM7939B1124",
            next_mission_id="186e5658-1079-45c0-bccc-02d2fa31b663",
            node="45TEST",
            objective="Deliver water to island X.",
            operation="Golden Eye",
            origin="THIRD_PARTY_DATASOURCE",
            orig_mission_id="614bebb6-a62e-053c-ca51-e79f8a402b28",
            prev_amc_mission_id="AJM7939B1122",
            prev_mission_id="a77055df-edc3-4047-a5fa-604f80b9fe3c",
            purpose="People at island X need water ASAP. Two previous attempts failed due to weather.",
            remarks=[
                {
                    "date": parse_datetime("2022-01-01T16:00:00.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "itinerary_num": 825,
                    "text": "Example mission remarks.",
                    "type": "MP",
                    "user": "John Doe",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 1.3,
                    "ead": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gdss_req_id": "23a1fb67-cc2d-5ebe-6b99-68130cb1aa6c",
                    "lad": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "num_ambulatory": 10,
                    "num_attendant": 10,
                    "num_litter": 10,
                    "num_pax": 44,
                    "offload_id": 300,
                    "offload_lo_code": "KHOP",
                    "onload_id": 200,
                    "onload_lo_code": "KCHS",
                    "oplan": "5027",
                    "outsize_weight": 1.3,
                    "oversize_weight": 1.3,
                    "proj_name": "CENTINTRA21",
                    "trans_req_num": "T01ME01",
                    "uln": "T01ME01",
                }
            ],
            source_sys_deviation=-90.12,
            state="EXECUTION",
            type="SAAM",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert air_transport_mission is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.retrieve(
            id="id",
        )
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.air_transport_missions.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            body_id="bdad6945-c9e4-b829-f7be-1ad075541921",
            abp="ZZ12",
            alias="PACIFIC DEPLOY / CHAP 3 MOVEMENT",
            allocated_unit="437 AEW",
            amc_mission_id="AJM7939B1123",
            apacs_id="1083034",
            ato_call_sign="CHARLIE",
            ato_mission_id="8900",
            call_sign="RCH123",
            cw=True,
            dip_worksheet_name="G2-182402-AB",
            first_pick_up="KFAY",
            gdss_mission_id="1e6edeec-72e9-aaec-d33c-51147cb5ffdd",
            haz_mat=[
                {
                    "applicable_notes": "11,12",
                    "cgc": "A",
                    "cgn": "4,5,7,8",
                    "class_div": 1.1,
                    "ext_haz_mat_id": "cb6289e0f38534e01291ab6421d42724",
                    "item_name": "LITHIUM METAL BATTERIES",
                    "net_exp_wt": 12.1,
                    "off_icao": "MBPV",
                    "off_itin": 300,
                    "on_icao": "LIRQ",
                    "on_itin": 50,
                    "pieces": 29,
                    "planned": "P",
                    "un_num": "0181",
                    "weight": 22.1,
                }
            ],
            jcs_priority="1A3",
            last_drop_off="PGUA",
            load_category_type="MIXED",
            m1="11",
            m2="3214",
            m3a="6655",
            naf="18AF",
            next_amc_mission_id="AJM7939B1124",
            next_mission_id="186e5658-1079-45c0-bccc-02d2fa31b663",
            node="45TEST",
            objective="Deliver water to island X.",
            operation="Golden Eye",
            origin="THIRD_PARTY_DATASOURCE",
            orig_mission_id="614bebb6-a62e-053c-ca51-e79f8a402b28",
            prev_amc_mission_id="AJM7939B1122",
            prev_mission_id="a77055df-edc3-4047-a5fa-604f80b9fe3c",
            purpose="People at island X need water ASAP. Two previous attempts failed due to weather.",
            remarks=[
                {
                    "date": parse_datetime("2022-01-01T16:00:00.123Z"),
                    "gdss_remark_id": "GDSSREMARK-ID",
                    "itinerary_num": 825,
                    "text": "Example mission remarks.",
                    "type": "MP",
                    "user": "John Doe",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 1.3,
                    "ead": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "gdss_req_id": "23a1fb67-cc2d-5ebe-6b99-68130cb1aa6c",
                    "lad": parse_datetime("2024-01-01T16:00:00.123Z"),
                    "num_ambulatory": 10,
                    "num_attendant": 10,
                    "num_litter": 10,
                    "num_pax": 44,
                    "offload_id": 300,
                    "offload_lo_code": "KHOP",
                    "onload_id": 200,
                    "onload_lo_code": "KCHS",
                    "oplan": "5027",
                    "outsize_weight": 1.3,
                    "oversize_weight": 1.3,
                    "proj_name": "CENTINTRA21",
                    "trans_req_num": "T01ME01",
                    "uln": "T01ME01",
                }
            ],
            source_sys_deviation=-90.12,
            state="EXECUTION",
            type="SAAM",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert air_transport_mission is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.air_transport_missions.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.list(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert_matches_type(AsyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert_matches_type(AsyncOffsetPage[AirTransportMissionAbridged], air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.count(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(str, air_transport_mission, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.count(
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, air_transport_mission, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.count(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert_matches_type(str, air_transport_mission, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.count(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert_matches_type(str, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.queryhelp()
        assert_matches_type(AirTransportMissionQueryhelpResponse, air_transport_mission, path=["response"])

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert_matches_type(AirTransportMissionQueryhelpResponse, air_transport_mission, path=["response"])

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert_matches_type(AirTransportMissionQueryhelpResponse, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert_matches_type(AirTransportMissionTupleResponse, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True
