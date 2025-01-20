# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    AirloadplanFull,
    AirLoadPlanListResponse,
    AirLoadPlanTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirLoadPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        air_load_plan = client.air_load_plans.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert air_load_plan is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        air_load_plan = client.air_load_plans.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            acl_onboard=0,
            acl_released=0,
            aircraft_mds="aircraftMDS",
            air_load_plan_hazmat_actuals=[
                {
                    "ashc": "ashc",
                    "cgc": "cgc",
                    "class_div": "classDiv",
                    "haz_description": "hazDescription",
                    "hazmat_remarks": "hazmatRemarks",
                    "haz_num": "hazNum",
                    "haz_num_type": "hazNumType",
                    "haz_off_icao": "hazOffICAO",
                    "haz_off_itin": 0,
                    "haz_on_icao": "hazOnICAO",
                    "haz_on_itin": 0,
                    "haz_pieces": 0,
                    "haz_tcn": "hazTcn",
                    "haz_weight": 0,
                    "item_name": "itemName",
                    "lot_num": "lotNum",
                    "net_exp_wt": 0,
                }
            ],
            air_load_plan_hr=[
                {
                    "container": "container",
                    "escort": "escort",
                    "hr_est_arr_time": "2019-12-27T18:11:19.117Z",
                    "hr_off_icao": "hrOffICAO",
                    "hr_off_itin": 0,
                    "hr_on_icao": "hrOnICAO",
                    "hr_on_itin": 0,
                    "hr_remarks": "hrRemarks",
                    "name": "name",
                    "rank": "rank",
                    "rec_agency": "recAgency",
                    "service": "service",
                    "viewable": True,
                }
            ],
            air_load_plan_pallet_details=[
                {
                    "category": "category",
                    "pp": "pp",
                    "pp_description": "ppDescription",
                    "pp_off_icao": "ppOffICAO",
                    "pp_pieces": 0,
                    "pp_remarks": "ppRemarks",
                    "pp_tcn": "ppTcn",
                    "pp_weight": 0,
                    "special_interest": True,
                }
            ],
            air_load_plan_pax_cargo=[
                {
                    "amb_pax": 0,
                    "att_pax": 0,
                    "available_pax": 0,
                    "bag_weight": 0,
                    "civ_pax": 0,
                    "dv_pax": 0,
                    "fn_pax": 0,
                    "group_cargo_weight": 0,
                    "group_type": "groupType",
                    "lit_pax": 0,
                    "mail_weight": 0,
                    "num_pallet": 0,
                    "pallet_weight": 0,
                    "pax_weight": 0,
                    "required_pax": 0,
                }
            ],
            air_load_plan_uln_actuals=[
                {
                    "num_ambulatory": 0,
                    "num_attendant": 0,
                    "num_litter": 0,
                    "num_pax": 0,
                    "offload_id": 0,
                    "offload_lo_code": "offloadLOCode",
                    "onload_id": 0,
                    "onload_lo_code": "onloadLOCode",
                    "oplan": "oplan",
                    "proj_name": "projName",
                    "uln": "uln",
                    "uln_cargo_weight": 0,
                    "uln_remarks": "ulnRemarks",
                }
            ],
            arr_airfield="arrAirfield",
            arr_icao="arrICAO",
            available_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            basic_moment=0,
            basic_weight=0,
            brief_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            call_sign="callSign",
            cargo_bay_fs_max=0,
            cargo_bay_fs_min=0,
            cargo_bay_width=0,
            cargo_config="cargoConfig",
            cargo_moment=0,
            cargo_volume=0,
            cargo_weight=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            crew_size=0,
            dep_airfield="depAirfield",
            dep_icao="depICAO",
            equip_config="equipConfig",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_landing_fuel_moment=0,
            est_landing_fuel_weight=0,
            external_id="externalId",
            fuel_moment=0,
            fuel_weight=0,
            gross_cg=0,
            gross_moment=0,
            gross_weight=0,
            id_mission="idMission",
            id_sortie="idSortie",
            landing_cg=0,
            landing_moment=0,
            landing_weight=0,
            leg_num=0,
            loadmaster_name="loadmasterName",
            loadmaster_rank="loadmasterRank",
            load_remarks="loadRemarks",
            mission_number="missionNumber",
            operating_moment=0,
            operating_weight=0,
            origin="origin",
            orig_network="origNetwork",
            pp_onboard=0,
            pp_released=0,
            sched_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            seats_onboard=0,
            seats_released=0,
            source_dl="sourceDL",
            tail_number="tailNumber",
            tank_config="tankConfig",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
            util_code="utilCode",
            zero_fuel_cg=0,
            zero_fuel_moment=0,
            zero_fuel_weight=0,
        )
        assert air_load_plan is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.air_load_plans.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = response.parse()
        assert air_load_plan is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.air_load_plans.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = response.parse()
            assert air_load_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        air_load_plan = client.air_load_plans.retrieve(
            "id",
        )
        assert_matches_type(AirloadplanFull, air_load_plan, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.air_load_plans.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = response.parse()
        assert_matches_type(AirloadplanFull, air_load_plan, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.air_load_plans.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = response.parse()
            assert_matches_type(AirloadplanFull, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.air_load_plans.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        air_load_plan = client.air_load_plans.list(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AirLoadPlanListResponse, air_load_plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.air_load_plans.with_raw_response.list(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = response.parse()
        assert_matches_type(AirLoadPlanListResponse, air_load_plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.air_load_plans.with_streaming_response.list(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = response.parse()
            assert_matches_type(AirLoadPlanListResponse, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        air_load_plan = client.air_load_plans.count(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, air_load_plan, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.air_load_plans.with_raw_response.count(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = response.parse()
        assert_matches_type(str, air_load_plan, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.air_load_plans.with_streaming_response.count(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = response.parse()
            assert_matches_type(str, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        air_load_plan = client.air_load_plans.queryhelp()
        assert air_load_plan is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.air_load_plans.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = response.parse()
        assert air_load_plan is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.air_load_plans.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = response.parse()
            assert air_load_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        air_load_plan = client.air_load_plans.tuple(
            columns="columns",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AirLoadPlanTupleResponse, air_load_plan, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.air_load_plans.with_raw_response.tuple(
            columns="columns",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = response.parse()
        assert_matches_type(AirLoadPlanTupleResponse, air_load_plan, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.air_load_plans.with_streaming_response.tuple(
            columns="columns",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = response.parse()
            assert_matches_type(AirLoadPlanTupleResponse, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAirLoadPlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_load_plan = await async_client.air_load_plans.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert air_load_plan is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_load_plan = await async_client.air_load_plans.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            acl_onboard=0,
            acl_released=0,
            aircraft_mds="aircraftMDS",
            air_load_plan_hazmat_actuals=[
                {
                    "ashc": "ashc",
                    "cgc": "cgc",
                    "class_div": "classDiv",
                    "haz_description": "hazDescription",
                    "hazmat_remarks": "hazmatRemarks",
                    "haz_num": "hazNum",
                    "haz_num_type": "hazNumType",
                    "haz_off_icao": "hazOffICAO",
                    "haz_off_itin": 0,
                    "haz_on_icao": "hazOnICAO",
                    "haz_on_itin": 0,
                    "haz_pieces": 0,
                    "haz_tcn": "hazTcn",
                    "haz_weight": 0,
                    "item_name": "itemName",
                    "lot_num": "lotNum",
                    "net_exp_wt": 0,
                }
            ],
            air_load_plan_hr=[
                {
                    "container": "container",
                    "escort": "escort",
                    "hr_est_arr_time": "2019-12-27T18:11:19.117Z",
                    "hr_off_icao": "hrOffICAO",
                    "hr_off_itin": 0,
                    "hr_on_icao": "hrOnICAO",
                    "hr_on_itin": 0,
                    "hr_remarks": "hrRemarks",
                    "name": "name",
                    "rank": "rank",
                    "rec_agency": "recAgency",
                    "service": "service",
                    "viewable": True,
                }
            ],
            air_load_plan_pallet_details=[
                {
                    "category": "category",
                    "pp": "pp",
                    "pp_description": "ppDescription",
                    "pp_off_icao": "ppOffICAO",
                    "pp_pieces": 0,
                    "pp_remarks": "ppRemarks",
                    "pp_tcn": "ppTcn",
                    "pp_weight": 0,
                    "special_interest": True,
                }
            ],
            air_load_plan_pax_cargo=[
                {
                    "amb_pax": 0,
                    "att_pax": 0,
                    "available_pax": 0,
                    "bag_weight": 0,
                    "civ_pax": 0,
                    "dv_pax": 0,
                    "fn_pax": 0,
                    "group_cargo_weight": 0,
                    "group_type": "groupType",
                    "lit_pax": 0,
                    "mail_weight": 0,
                    "num_pallet": 0,
                    "pallet_weight": 0,
                    "pax_weight": 0,
                    "required_pax": 0,
                }
            ],
            air_load_plan_uln_actuals=[
                {
                    "num_ambulatory": 0,
                    "num_attendant": 0,
                    "num_litter": 0,
                    "num_pax": 0,
                    "offload_id": 0,
                    "offload_lo_code": "offloadLOCode",
                    "onload_id": 0,
                    "onload_lo_code": "onloadLOCode",
                    "oplan": "oplan",
                    "proj_name": "projName",
                    "uln": "uln",
                    "uln_cargo_weight": 0,
                    "uln_remarks": "ulnRemarks",
                }
            ],
            arr_airfield="arrAirfield",
            arr_icao="arrICAO",
            available_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            basic_moment=0,
            basic_weight=0,
            brief_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            call_sign="callSign",
            cargo_bay_fs_max=0,
            cargo_bay_fs_min=0,
            cargo_bay_width=0,
            cargo_config="cargoConfig",
            cargo_moment=0,
            cargo_volume=0,
            cargo_weight=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            crew_size=0,
            dep_airfield="depAirfield",
            dep_icao="depICAO",
            equip_config="equipConfig",
            est_arr_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            est_landing_fuel_moment=0,
            est_landing_fuel_weight=0,
            external_id="externalId",
            fuel_moment=0,
            fuel_weight=0,
            gross_cg=0,
            gross_moment=0,
            gross_weight=0,
            id_mission="idMission",
            id_sortie="idSortie",
            landing_cg=0,
            landing_moment=0,
            landing_weight=0,
            leg_num=0,
            loadmaster_name="loadmasterName",
            loadmaster_rank="loadmasterRank",
            load_remarks="loadRemarks",
            mission_number="missionNumber",
            operating_moment=0,
            operating_weight=0,
            origin="origin",
            orig_network="origNetwork",
            pp_onboard=0,
            pp_released=0,
            sched_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            seats_onboard=0,
            seats_released=0,
            source_dl="sourceDL",
            tail_number="tailNumber",
            tank_config="tankConfig",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by="updatedBy",
            util_code="utilCode",
            zero_fuel_cg=0,
            zero_fuel_moment=0,
            zero_fuel_weight=0,
        )
        assert air_load_plan is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_load_plans.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = await response.parse()
        assert air_load_plan is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_load_plans.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = await response.parse()
            assert air_load_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_load_plan = await async_client.air_load_plans.retrieve(
            "id",
        )
        assert_matches_type(AirloadplanFull, air_load_plan, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_load_plans.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = await response.parse()
        assert_matches_type(AirloadplanFull, air_load_plan, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_load_plans.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = await response.parse()
            assert_matches_type(AirloadplanFull, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.air_load_plans.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_load_plan = await async_client.air_load_plans.list(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AirLoadPlanListResponse, air_load_plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_load_plans.with_raw_response.list(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = await response.parse()
        assert_matches_type(AirLoadPlanListResponse, air_load_plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_load_plans.with_streaming_response.list(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = await response.parse()
            assert_matches_type(AirLoadPlanListResponse, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_load_plan = await async_client.air_load_plans.count(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, air_load_plan, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_load_plans.with_raw_response.count(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = await response.parse()
        assert_matches_type(str, air_load_plan, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_load_plans.with_streaming_response.count(
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = await response.parse()
            assert_matches_type(str, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_load_plan = await async_client.air_load_plans.queryhelp()
        assert air_load_plan is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_load_plans.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = await response.parse()
        assert air_load_plan is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_load_plans.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = await response.parse()
            assert air_load_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        air_load_plan = await async_client.air_load_plans.tuple(
            columns="columns",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AirLoadPlanTupleResponse, air_load_plan, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.air_load_plans.with_raw_response.tuple(
            columns="columns",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        air_load_plan = await response.parse()
        assert_matches_type(AirLoadPlanTupleResponse, air_load_plan, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.air_load_plans.with_streaming_response.tuple(
            columns="columns",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            air_load_plan = await response.parse()
            assert_matches_type(AirLoadPlanTupleResponse, air_load_plan, path=["response"])

        assert cast(Any, response.is_closed) is True
