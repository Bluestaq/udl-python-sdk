# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirTransportMissionListResponse,
    AirTransportMissionTupleResponse,
)
from unifieddatalibrary._utils import parse_date, parse_datetime
from unifieddatalibrary.types.shared import AirTransportMissionFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirTransportMissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert air_transport_mission is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id="id",
            alias="alias",
            allocated_unit="allocatedUnit",
            amc_mission_id="amcMissionId",
            apacs_id="apacsId",
            call_sign="callSign",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cw=True,
            dip_worksheet_name="dipWorksheetName",
            first_pick_up="firstPickUp",
            gdss_mission_id="gdssMissionId",
            haz_mat=[
                {
                    "applicable_notes": "applicableNotes",
                    "cgc": "cgc",
                    "cgn": "cgn",
                    "class_div": 0,
                    "ext_haz_mat_id": "extHazMatId",
                    "item_name": "itemName",
                    "net_exp_wt": 0,
                    "off_icao": "offICAO",
                    "off_itin": 0,
                    "on_icao": "onICAO",
                    "on_itin": 0,
                    "pieces": 0,
                    "planned": "planned",
                    "un_num": "unNum",
                    "weight": 0,
                }
            ],
            jcs_priority="jcsPriority",
            last_drop_off="lastDropOff",
            load_category_type="loadCategoryType",
            naf="naf",
            next_amc_mission_id="nextAMCMissionId",
            next_mission_id="nextMissionId",
            objective="objective",
            operation="operation",
            origin="origin",
            orig_mission_id="origMissionId",
            orig_network="origNetwork",
            prev_amc_mission_id="prevAMCMissionId",
            prev_mission_id="prevMissionId",
            purpose="purpose",
            remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "itinerary_num": 0,
                    "text": "text",
                    "type": "type",
                    "user": "user",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 0,
                    "ead": "ead",
                    "gdss_req_id": "gdssReqId",
                    "lad": "lad",
                    "num_ambulatory": 0,
                    "num_attendant": 0,
                    "num_litter": 0,
                    "num_pax": 0,
                    "offload_id": 0,
                    "offload_lo_code": "offloadLOCode",
                    "onload_id": 0,
                    "onload_lo_code": "onloadLOCode",
                    "oplan": "oplan",
                    "outsize_weight": 0,
                    "oversize_weight": 0,
                    "proj_name": "projName",
                    "trans_req_num": "transReqNum",
                    "uln": "uln",
                }
            ],
            source_dl="sourceDL",
            source_sys_deviation=0,
            state="state",
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert air_transport_mission is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert air_transport_mission is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.retrieve(
            "id",
        )
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert air_transport_mission is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id_2="id",
            alias="alias",
            allocated_unit="allocatedUnit",
            amc_mission_id="amcMissionId",
            apacs_id="apacsId",
            call_sign="callSign",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cw=True,
            dip_worksheet_name="dipWorksheetName",
            first_pick_up="firstPickUp",
            gdss_mission_id="gdssMissionId",
            haz_mat=[
                {
                    "applicable_notes": "applicableNotes",
                    "cgc": "cgc",
                    "cgn": "cgn",
                    "class_div": 0,
                    "ext_haz_mat_id": "extHazMatId",
                    "item_name": "itemName",
                    "net_exp_wt": 0,
                    "off_icao": "offICAO",
                    "off_itin": 0,
                    "on_icao": "onICAO",
                    "on_itin": 0,
                    "pieces": 0,
                    "planned": "planned",
                    "un_num": "unNum",
                    "weight": 0,
                }
            ],
            jcs_priority="jcsPriority",
            last_drop_off="lastDropOff",
            load_category_type="loadCategoryType",
            naf="naf",
            next_amc_mission_id="nextAMCMissionId",
            next_mission_id="nextMissionId",
            objective="objective",
            operation="operation",
            origin="origin",
            orig_mission_id="origMissionId",
            orig_network="origNetwork",
            prev_amc_mission_id="prevAMCMissionId",
            prev_mission_id="prevMissionId",
            purpose="purpose",
            remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "itinerary_num": 0,
                    "text": "text",
                    "type": "type",
                    "user": "user",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 0,
                    "ead": "ead",
                    "gdss_req_id": "gdssReqId",
                    "lad": "lad",
                    "num_ambulatory": 0,
                    "num_attendant": 0,
                    "num_litter": 0,
                    "num_pax": 0,
                    "offload_id": 0,
                    "offload_lo_code": "offloadLOCode",
                    "onload_id": 0,
                    "onload_lo_code": "onloadLOCode",
                    "oplan": "oplan",
                    "outsize_weight": 0,
                    "oversize_weight": 0,
                    "proj_name": "projName",
                    "trans_req_num": "transReqNum",
                    "uln": "uln",
                }
            ],
            source_dl="sourceDL",
            source_sys_deviation=0,
            state="state",
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert air_transport_mission is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert air_transport_mission is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.air_transport_missions.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                source="source",
                id_2="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AirTransportMissionListResponse, air_transport_mission, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert_matches_type(AirTransportMissionListResponse, air_transport_mission, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert_matches_type(AirTransportMissionListResponse, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.count(
            created_at=parse_date("2019-12-27"),
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
        assert air_transport_mission is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.air_transport_missions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = response.parse()
        assert air_transport_mission is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.air_transport_missions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        air_transport_mission = client.air_transport_missions.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id="id",
            alias="alias",
            allocated_unit="allocatedUnit",
            amc_mission_id="amcMissionId",
            apacs_id="apacsId",
            call_sign="callSign",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cw=True,
            dip_worksheet_name="dipWorksheetName",
            first_pick_up="firstPickUp",
            gdss_mission_id="gdssMissionId",
            haz_mat=[
                {
                    "applicable_notes": "applicableNotes",
                    "cgc": "cgc",
                    "cgn": "cgn",
                    "class_div": 0,
                    "ext_haz_mat_id": "extHazMatId",
                    "item_name": "itemName",
                    "net_exp_wt": 0,
                    "off_icao": "offICAO",
                    "off_itin": 0,
                    "on_icao": "onICAO",
                    "on_itin": 0,
                    "pieces": 0,
                    "planned": "planned",
                    "un_num": "unNum",
                    "weight": 0,
                }
            ],
            jcs_priority="jcsPriority",
            last_drop_off="lastDropOff",
            load_category_type="loadCategoryType",
            naf="naf",
            next_amc_mission_id="nextAMCMissionId",
            next_mission_id="nextMissionId",
            objective="objective",
            operation="operation",
            origin="origin",
            orig_mission_id="origMissionId",
            orig_network="origNetwork",
            prev_amc_mission_id="prevAMCMissionId",
            prev_mission_id="prevMissionId",
            purpose="purpose",
            remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "itinerary_num": 0,
                    "text": "text",
                    "type": "type",
                    "user": "user",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 0,
                    "ead": "ead",
                    "gdss_req_id": "gdssReqId",
                    "lad": "lad",
                    "num_ambulatory": 0,
                    "num_attendant": 0,
                    "num_litter": 0,
                    "num_pax": 0,
                    "offload_id": 0,
                    "offload_lo_code": "offloadLOCode",
                    "onload_id": 0,
                    "onload_lo_code": "onloadLOCode",
                    "oplan": "oplan",
                    "outsize_weight": 0,
                    "oversize_weight": 0,
                    "proj_name": "projName",
                    "trans_req_num": "transReqNum",
                    "uln": "uln",
                }
            ],
            source_dl="sourceDL",
            source_sys_deviation=0,
            state="state",
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert air_transport_mission is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.retrieve(
            "id",
        )
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert_matches_type(AirTransportMissionFull, air_transport_mission, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.retrieve(
            "id",
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
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
            id_2="id",
            alias="alias",
            allocated_unit="allocatedUnit",
            amc_mission_id="amcMissionId",
            apacs_id="apacsId",
            call_sign="callSign",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            cw=True,
            dip_worksheet_name="dipWorksheetName",
            first_pick_up="firstPickUp",
            gdss_mission_id="gdssMissionId",
            haz_mat=[
                {
                    "applicable_notes": "applicableNotes",
                    "cgc": "cgc",
                    "cgn": "cgn",
                    "class_div": 0,
                    "ext_haz_mat_id": "extHazMatId",
                    "item_name": "itemName",
                    "net_exp_wt": 0,
                    "off_icao": "offICAO",
                    "off_itin": 0,
                    "on_icao": "onICAO",
                    "on_itin": 0,
                    "pieces": 0,
                    "planned": "planned",
                    "un_num": "unNum",
                    "weight": 0,
                }
            ],
            jcs_priority="jcsPriority",
            last_drop_off="lastDropOff",
            load_category_type="loadCategoryType",
            naf="naf",
            next_amc_mission_id="nextAMCMissionId",
            next_mission_id="nextMissionId",
            objective="objective",
            operation="operation",
            origin="origin",
            orig_mission_id="origMissionId",
            orig_network="origNetwork",
            prev_amc_mission_id="prevAMCMissionId",
            prev_mission_id="prevMissionId",
            purpose="purpose",
            remarks=[
                {
                    "date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gdss_remark_id": "gdssRemarkId",
                    "itinerary_num": 0,
                    "text": "text",
                    "type": "type",
                    "user": "user",
                }
            ],
            requirements=[
                {
                    "bulk_weight": 0,
                    "ead": "ead",
                    "gdss_req_id": "gdssReqId",
                    "lad": "lad",
                    "num_ambulatory": 0,
                    "num_attendant": 0,
                    "num_litter": 0,
                    "num_pax": 0,
                    "offload_id": 0,
                    "offload_lo_code": "offloadLOCode",
                    "onload_id": 0,
                    "onload_lo_code": "onloadLOCode",
                    "oplan": "oplan",
                    "outsize_weight": 0,
                    "oversize_weight": 0,
                    "proj_name": "projName",
                    "trans_req_num": "transReqNum",
                    "uln": "uln",
                }
            ],
            source_dl="sourceDL",
            source_sys_deviation=0,
            state="state",
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
        )
        assert air_transport_mission is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert air_transport_mission is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.update(
            id_1="id",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.air_transport_missions.with_raw_response.update(
                id_1="",
                classification_marking="classificationMarking",
                data_mode="dataMode",
                source="source",
                id_2="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.list(
            created_at=parse_date("2019-12-27"),
        )
        assert_matches_type(AirTransportMissionListResponse, air_transport_mission, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.list(
            created_at=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert_matches_type(AirTransportMissionListResponse, air_transport_mission, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.list(
            created_at=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert_matches_type(AirTransportMissionListResponse, air_transport_mission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.count(
            created_at=parse_date("2019-12-27"),
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
        assert air_transport_mission is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_transport_missions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_transport_mission = await response.parse()
        assert air_transport_mission is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_transport_missions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_transport_mission = await response.parse()
            assert air_transport_mission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_transport_mission = await async_client.air_transport_missions.tuple(
            columns="columns",
            created_at=parse_date("2019-12-27"),
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
