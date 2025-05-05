# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAirloadPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        airload_plan = client.airload_plans.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
        )
        assert airload_plan is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        airload_plan = client.airload_plans.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
            body_id="0457f578-e29c-312e-85aa-0a04a430bdd0",
            acl_onboard=500.1,
            acl_released=200.1,
            aircraft_mds="C17A",
            air_load_plan_hazmat_actuals=[
                {
                    "ashc": "RFL",
                    "cgc": "A",
                    "class_div": "1.1",
                    "haz_description": "CORROSIVE OXIDIZER",
                    "hazmat_remarks": "Hazmat remarks",
                    "haz_num": "2031",
                    "haz_num_type": "UN",
                    "haz_off_icao": "MBPV",
                    "haz_off_itin": 300,
                    "haz_on_icao": "LIRQ",
                    "haz_on_itin": 50,
                    "haz_pieces": 29,
                    "haz_tcn": "M1358232245912XXX",
                    "haz_weight": 22.1,
                    "item_name": "NITRIC ACID",
                    "lot_num": "1234A",
                    "net_exp_wt": 12.1,
                }
            ],
            air_load_plan_hr=[
                {
                    "container": "Metal",
                    "escort": "Jane Doe",
                    "hr_est_arr_time": parse_datetime("2024-01-01T01:00:00.123Z"),
                    "hr_off_icao": "KDEN",
                    "hr_off_itin": 200,
                    "hr_on_icao": "KCOS",
                    "hr_on_itin": 100,
                    "hr_remarks": "HR remarks",
                    "name": "John Doe",
                    "rank": "Captain",
                    "rec_agency": "Agency name",
                    "service": "Air Force",
                    "viewable": True,
                }
            ],
            air_load_plan_pallet_details=[
                {
                    "category": "AMCMICAP",
                    "pp": "2",
                    "pp_description": "Ammunition",
                    "pp_off_icao": "MBPV",
                    "pp_pieces": 3,
                    "pp_remarks": "Pallet remarks",
                    "pp_tcn": "M1358232245912XXX",
                    "pp_weight": 100.1,
                    "special_interest": True,
                }
            ],
            air_load_plan_pax_cargo=[
                {
                    "amb_pax": 5,
                    "att_pax": 6,
                    "available_pax": 20,
                    "bag_weight": 2000.1,
                    "civ_pax": 3,
                    "dv_pax": 2,
                    "fn_pax": 1,
                    "group_cargo_weight": 5000.1,
                    "group_type": "OFFTHIS",
                    "lit_pax": 4,
                    "mail_weight": 200.1,
                    "num_pallet": 20,
                    "pallet_weight": 400.1,
                    "pax_weight": 8000.1,
                    "required_pax": 20,
                }
            ],
            air_load_plan_uln_actuals=[
                {
                    "num_ambulatory": 10,
                    "num_attendant": 10,
                    "num_litter": 10,
                    "num_pax": 44,
                    "offload_id": 300,
                    "offload_lo_code": "KHOP",
                    "onload_id": 200,
                    "onload_lo_code": "KCHS",
                    "oplan": "5027A",
                    "proj_name": "CENTINTRA21",
                    "uln": "T01ME01",
                    "uln_cargo_weight": 1000.1,
                    "uln_remarks": "ULN actuals remark",
                }
            ],
            arr_airfield="W99",
            arr_icao="ETAR",
            available_time=parse_datetime("2024-01-01T02:00:00.123Z"),
            basic_moment=2500.1,
            basic_weight=100.1,
            brief_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            call_sign="RCH1234",
            cargo_bay_fs_max=20.1,
            cargo_bay_fs_min=10.1,
            cargo_bay_width=3.1,
            cargo_config="C-1",
            cargo_moment=2500.1,
            cargo_volume=50.1,
            cargo_weight=100.1,
            crew_size=5,
            dep_airfield="W99",
            dep_icao="KCHS",
            equip_config="Standard",
            est_arr_time=parse_datetime("2024-01-01T02:00:00.123Z"),
            est_landing_fuel_moment=2500.1,
            est_landing_fuel_weight=100.1,
            external_id="dec7a61a-cd97-4af0-b7bc-f4c3bb33341b",
            fuel_moment=2500.1,
            fuel_weight=100.1,
            gross_cg=38.8,
            gross_moment=2500.1,
            gross_weight=100.1,
            id_mission="412bebb6-a45e-029c-ca51-e29f8a442b12",
            id_sortie="823acfbe6-f36a-157b-ef32-b47c9b589c4",
            landing_cg=38.2,
            landing_moment=2500.1,
            landing_weight=100.1,
            leg_num=200,
            loadmaster_name="John Smith",
            loadmaster_rank="Staff Sergeant",
            load_remarks="Load remarks",
            mission_number="AJM123456123",
            operating_moment=2500.1,
            operating_weight=100.1,
            origin="THIRD_PARTY_DATASOURCE",
            pp_onboard=18,
            pp_released=5,
            sched_time=parse_datetime("2024-01-01T02:30:00.123Z"),
            seats_onboard=20,
            seats_released=15,
            tail_number="77187",
            tank_config="ER",
            util_code="AD",
            zero_fuel_cg=39.5,
            zero_fuel_moment=2500.1,
            zero_fuel_weight=100.1,
        )
        assert airload_plan is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.airload_plans.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airload_plan = response.parse()
        assert airload_plan is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.airload_plans.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airload_plan = response.parse()
            assert airload_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.airload_plans.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
                source="source",
            )

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        airload_plan = client.airload_plans.delete(
            "id",
        )
        assert airload_plan is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.airload_plans.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airload_plan = response.parse()
        assert airload_plan is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.airload_plans.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airload_plan = response.parse()
            assert airload_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.airload_plans.with_raw_response.delete(
                "",
            )


class TestAsyncAirloadPlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        airload_plan = await async_client.airload_plans.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
        )
        assert airload_plan is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        airload_plan = await async_client.airload_plans.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
            body_id="0457f578-e29c-312e-85aa-0a04a430bdd0",
            acl_onboard=500.1,
            acl_released=200.1,
            aircraft_mds="C17A",
            air_load_plan_hazmat_actuals=[
                {
                    "ashc": "RFL",
                    "cgc": "A",
                    "class_div": "1.1",
                    "haz_description": "CORROSIVE OXIDIZER",
                    "hazmat_remarks": "Hazmat remarks",
                    "haz_num": "2031",
                    "haz_num_type": "UN",
                    "haz_off_icao": "MBPV",
                    "haz_off_itin": 300,
                    "haz_on_icao": "LIRQ",
                    "haz_on_itin": 50,
                    "haz_pieces": 29,
                    "haz_tcn": "M1358232245912XXX",
                    "haz_weight": 22.1,
                    "item_name": "NITRIC ACID",
                    "lot_num": "1234A",
                    "net_exp_wt": 12.1,
                }
            ],
            air_load_plan_hr=[
                {
                    "container": "Metal",
                    "escort": "Jane Doe",
                    "hr_est_arr_time": parse_datetime("2024-01-01T01:00:00.123Z"),
                    "hr_off_icao": "KDEN",
                    "hr_off_itin": 200,
                    "hr_on_icao": "KCOS",
                    "hr_on_itin": 100,
                    "hr_remarks": "HR remarks",
                    "name": "John Doe",
                    "rank": "Captain",
                    "rec_agency": "Agency name",
                    "service": "Air Force",
                    "viewable": True,
                }
            ],
            air_load_plan_pallet_details=[
                {
                    "category": "AMCMICAP",
                    "pp": "2",
                    "pp_description": "Ammunition",
                    "pp_off_icao": "MBPV",
                    "pp_pieces": 3,
                    "pp_remarks": "Pallet remarks",
                    "pp_tcn": "M1358232245912XXX",
                    "pp_weight": 100.1,
                    "special_interest": True,
                }
            ],
            air_load_plan_pax_cargo=[
                {
                    "amb_pax": 5,
                    "att_pax": 6,
                    "available_pax": 20,
                    "bag_weight": 2000.1,
                    "civ_pax": 3,
                    "dv_pax": 2,
                    "fn_pax": 1,
                    "group_cargo_weight": 5000.1,
                    "group_type": "OFFTHIS",
                    "lit_pax": 4,
                    "mail_weight": 200.1,
                    "num_pallet": 20,
                    "pallet_weight": 400.1,
                    "pax_weight": 8000.1,
                    "required_pax": 20,
                }
            ],
            air_load_plan_uln_actuals=[
                {
                    "num_ambulatory": 10,
                    "num_attendant": 10,
                    "num_litter": 10,
                    "num_pax": 44,
                    "offload_id": 300,
                    "offload_lo_code": "KHOP",
                    "onload_id": 200,
                    "onload_lo_code": "KCHS",
                    "oplan": "5027A",
                    "proj_name": "CENTINTRA21",
                    "uln": "T01ME01",
                    "uln_cargo_weight": 1000.1,
                    "uln_remarks": "ULN actuals remark",
                }
            ],
            arr_airfield="W99",
            arr_icao="ETAR",
            available_time=parse_datetime("2024-01-01T02:00:00.123Z"),
            basic_moment=2500.1,
            basic_weight=100.1,
            brief_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            call_sign="RCH1234",
            cargo_bay_fs_max=20.1,
            cargo_bay_fs_min=10.1,
            cargo_bay_width=3.1,
            cargo_config="C-1",
            cargo_moment=2500.1,
            cargo_volume=50.1,
            cargo_weight=100.1,
            crew_size=5,
            dep_airfield="W99",
            dep_icao="KCHS",
            equip_config="Standard",
            est_arr_time=parse_datetime("2024-01-01T02:00:00.123Z"),
            est_landing_fuel_moment=2500.1,
            est_landing_fuel_weight=100.1,
            external_id="dec7a61a-cd97-4af0-b7bc-f4c3bb33341b",
            fuel_moment=2500.1,
            fuel_weight=100.1,
            gross_cg=38.8,
            gross_moment=2500.1,
            gross_weight=100.1,
            id_mission="412bebb6-a45e-029c-ca51-e29f8a442b12",
            id_sortie="823acfbe6-f36a-157b-ef32-b47c9b589c4",
            landing_cg=38.2,
            landing_moment=2500.1,
            landing_weight=100.1,
            leg_num=200,
            loadmaster_name="John Smith",
            loadmaster_rank="Staff Sergeant",
            load_remarks="Load remarks",
            mission_number="AJM123456123",
            operating_moment=2500.1,
            operating_weight=100.1,
            origin="THIRD_PARTY_DATASOURCE",
            pp_onboard=18,
            pp_released=5,
            sched_time=parse_datetime("2024-01-01T02:30:00.123Z"),
            seats_onboard=20,
            seats_released=15,
            tail_number="77187",
            tank_config="ER",
            util_code="AD",
            zero_fuel_cg=39.5,
            zero_fuel_moment=2500.1,
            zero_fuel_weight=100.1,
        )
        assert airload_plan is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airload_plans.with_raw_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airload_plan = await response.parse()
        assert airload_plan is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airload_plans.with_streaming_response.update(
            path_id="id",
            classification_marking="U",
            data_mode="TEST",
            est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airload_plan = await response.parse()
            assert airload_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.airload_plans.with_raw_response.update(
                path_id="",
                classification_marking="U",
                data_mode="TEST",
                est_dep_time=parse_datetime("2024-01-01T01:00:00.123Z"),
                source="source",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        airload_plan = await async_client.airload_plans.delete(
            "id",
        )
        assert airload_plan is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.airload_plans.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airload_plan = await response.parse()
        assert airload_plan is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.airload_plans.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airload_plan = await response.parse()
            assert airload_plan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.airload_plans.with_raw_response.delete(
                "",
            )
