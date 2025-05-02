# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    FlightPlanAbridged,
    FlightplanTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import FlightPlanFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlightplan:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )
        assert flightplan is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
            id="c44b0a80-9fef-63d9-6267-79037fb93e4c",
            aircraft_mds="KC-130 HERCULES",
            air_refuel_events=[
                {
                    "ar_degrade": 3.1,
                    "ar_exchanged_fuel": 1500.1,
                    "ar_num": 2,
                    "divert_fuel": 143000.1,
                    "exit_fuel": 160000.1,
                }
            ],
            amc_mission_id="AJM7939B1123",
            app_landing_fuel=3000.1,
            arr_alternate1="EDDS",
            arr_alternate1_fuel=6000.1,
            arr_alternate2="EDDM",
            arr_alternate2_fuel=6000.1,
            arr_ice_fuel=1000.1,
            arr_runway="05L",
            atc_addresses=["EYCBZMFO", "EUCHZMFP", "ETARYXYX", "EDUUZVZI"],
            avg_temp_dev=16.1,
            burned_fuel=145000.1,
            call_sign="HKY629",
            cargo_remark="Expecting 55,000 lbs. If different, call us.",
            climb_fuel=7000.1,
            climb_time="00:13",
            contingency_fuel=3000.1,
            country_codes=["US", "CA", "UK"],
            dep_alternate="LFPO",
            depress_fuel=20000.1,
            dep_runway="05L",
            drag_index=16.9,
            early_descent_fuel=500.1,
            endurance_time="08:45",
            enroute_fuel=155000.1,
            enroute_time="06:30",
            equipment="SDFGHIRTUWXYZ/H",
            est_dep_time=parse_datetime("2023-05-01T01:01:01.123Z"),
            etops_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_alt_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_rating="85 MINUTES",
            etops_val_window="LPLA: 0317Z-0722Z",
            external_id="AFMAPP20322347140001",
            flight_plan_messages=[
                {
                    "msg_text": "Message text",
                    "route_path": "PRIMARY",
                    "severity": "SEVERE",
                    "wp_num": "20",
                }
            ],
            flight_plan_point_groups=[
                {
                    "avg_fuel_flow": 19693.1,
                    "etops_avg_wind_factor": 10.1,
                    "etops_distance": 684.1,
                    "etops_req_fuel": 4412.1,
                    "etops_temp_dev": 9.1,
                    "etops_time": "01:23",
                    "flight_plan_points": [
                        {
                            "fpp_eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                            "fpp_lat": 45.23,
                            "fpp_lon": 179.1,
                            "fpp_req_fuel": 4250.1,
                            "point_name": "CRUISE ALTITUDE ETP",
                        }
                    ],
                    "from_takeoff_time": "07:29",
                    "fsaf_avg_wind_factor": 10.1,
                    "fsaf_distance": 684.1,
                    "fsaf_req_fuel": 50380.1,
                    "fsaf_temp_dev": 9.1,
                    "fsaf_time": "01:23",
                    "fuel_calc_alt": 100.1,
                    "fuel_calc_spd": 365.1,
                    "lsaf_avg_wind_factor": 13.1,
                    "lsaf_distance": 684.1,
                    "lsaf_name": "LPPD",
                    "lsaf_req_fuel": 50787.1,
                    "lsaf_temp_dev": 9.1,
                    "lsaf_time": "01:23",
                    "planned_fuel": 190319.1,
                    "point_group_name": "ETOPS_CF_POINT_1",
                    "worst_fuel_case": "DEPRESSURIZED ENGINE OUT ETP",
                }
            ],
            flight_plan_waypoints=[
                {
                    "type": "COMMENT",
                    "waypoint_name": "KCHS",
                    "aa_tacan_channel": "31/94",
                    "air_distance": 321.1,
                    "airway": "W15",
                    "alt": 27000.1,
                    "ar_id": "AR202",
                    "arpt": "ARIP",
                    "ata": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "avg_cal_airspeed": 200.1,
                    "avg_drift_ang": -3.2,
                    "avg_ground_speed": 300.1,
                    "avg_true_airspeed": 210.1,
                    "avg_wind_dir": 165.5,
                    "avg_wind_speed": 14.4,
                    "day_low_alt": 1500.1,
                    "eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "exchanged_fuel": -30400.1,
                    "fuel_flow": 17654.1,
                    "ice_cat": "MODERATE",
                    "lat": 45.23,
                    "leg_alternate": "KCHS",
                    "leg_drag_index": 1.2,
                    "leg_fuel_degrade": 10.1,
                    "leg_mach": 0.74,
                    "leg_msn_index": 65,
                    "leg_wind_fac": -32.1,
                    "lon": 179.1,
                    "mag_course": 338.1,
                    "mag_heading": 212.1,
                    "mag_var": -13.2,
                    "navaid": "HTO",
                    "night_low_alt": 2300.1,
                    "nvg_low_alt": 2450.1,
                    "point_wind_dir": 165.5,
                    "point_wind_speed": 14.4,
                    "pri_freq": 357.5,
                    "sec_freq": 357.5,
                    "tacan_channel": "83X",
                    "temp_dev": 12.1,
                    "thunder_cat": "MODERATE",
                    "total_air_distance": 3251.1,
                    "total_flown_distance": 688.1,
                    "total_rem_distance": 1288.1,
                    "total_rem_fuel": 30453.1,
                    "total_time": "08:45",
                    "total_time_rem": "01:43",
                    "total_used_fuel": 70431.1,
                    "total_weight": 207123.1,
                    "true_course": 328.1,
                    "turb_cat": "EXTREME",
                    "vor_freq": 113.6,
                    "waypoint_num": 20,
                    "zone_distance": 212.1,
                    "zone_fuel": 1120.1,
                    "zone_time": 36.1,
                }
            ],
            flight_rules="l",
            flight_type="MILITARY",
            fuel_degrade=10.3,
            gps_raim="Failed by FAA SAPT 184022AUG2022",
            hold_down_fuel=500.1,
            hold_fuel=6000.1,
            hold_time="01:00",
            id_aircraft="4f4a67c6-40fd-11ee-be56-0242ac120002",
            id_arr_airfield="363080c2-40fd-11ee-be56-0242ac120002",
            id_dep_airfield="2a9020f6-40fd-11ee-be56-0242ac120002",
            ident_extra_fuel=5000.1,
            id_sortie="9d60c1b1-10b1-b2a7-e403-84c5d7eeb170",
            initial_cruise_speed="N0305",
            initial_flight_level="F270",
            landing_fuel=19000.1,
            leg_num=100,
            min_divert_fuel=25000.1,
            msn_index=44.1,
            notes="STS/STATE PBN/A1B2B5C2C4D2D4 EUR/PROTECTED",
            num_aircraft=1,
            op_condition_fuel=5000.1,
            op_weight=251830.5,
            origin="THIRD_PARTY_DATASOURCE",
            originator="ETARYXYX",
            planner_remark="Flight plan is good for 2 days before airspace closes over the UK.",
            ramp_fuel=180000.1,
            rem_alternate1_fuel=18000.1,
            rem_alternate2_fuel=18000.1,
            reserve_fuel=10000.1,
            route_string="RENV3B RENVI Y86 GOSVA/N0317F260 DCT EVLIT DCT UMUGI DCT NISIX DCT GIGOD DCT DIPEB DCT\nGORPI Z80 TILAV L87 RAKIT Z717 PODUS Z130 MAG/N0298F220 Z20 KENIG/N0319F220 Z20 ORTAG T177\nESEGU Z20 BEBLA DCT MASEK/N0300F200 DCT GISEM/N0319F200 DCT BOMBI/N0276F060 DCT RIDSU DCT",
            sid="RENV3B",
            star="ADANA",
            status="APPROVED",
            tail_number="77187",
            takeoff_fuel=178500.1,
            taxi_fuel=1500.1,
            thunder_avoid_fuel=1000.1,
            toc_fuel=160000.1,
            toc_ice_fuel=1000.1,
            tod_fuel=32000.1,
            tod_ice_fuel=2000.1,
            unident_extra_fuel=5000.1,
            unusable_fuel=2300.1,
            wake_turb_cat="MEDIUM",
            wind_fac1=-1.1,
            wind_fac2=10.1,
            wind_fac_avg=5.1,
            wx_valid_end=parse_datetime("2023-05-01T01:01:01.123Z"),
            wx_valid_start=parse_datetime("2023-05-01T01:01:01.123Z"),
        )
        assert flightplan is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert flightplan is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.retrieve(
            id="id",
        )
        assert_matches_type(FlightPlanFull, flightplan, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FlightPlanFull, flightplan, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert_matches_type(FlightPlanFull, flightplan, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert_matches_type(FlightPlanFull, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.flightplan.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )
        assert flightplan is None

    @parametrize
    def test_method_update_with_all_params(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
            body_id="c44b0a80-9fef-63d9-6267-79037fb93e4c",
            aircraft_mds="KC-130 HERCULES",
            air_refuel_events=[
                {
                    "ar_degrade": 3.1,
                    "ar_exchanged_fuel": 1500.1,
                    "ar_num": 2,
                    "divert_fuel": 143000.1,
                    "exit_fuel": 160000.1,
                }
            ],
            amc_mission_id="AJM7939B1123",
            app_landing_fuel=3000.1,
            arr_alternate1="EDDS",
            arr_alternate1_fuel=6000.1,
            arr_alternate2="EDDM",
            arr_alternate2_fuel=6000.1,
            arr_ice_fuel=1000.1,
            arr_runway="05L",
            atc_addresses=["EYCBZMFO", "EUCHZMFP", "ETARYXYX", "EDUUZVZI"],
            avg_temp_dev=16.1,
            burned_fuel=145000.1,
            call_sign="HKY629",
            cargo_remark="Expecting 55,000 lbs. If different, call us.",
            climb_fuel=7000.1,
            climb_time="00:13",
            contingency_fuel=3000.1,
            country_codes=["US", "CA", "UK"],
            dep_alternate="LFPO",
            depress_fuel=20000.1,
            dep_runway="05L",
            drag_index=16.9,
            early_descent_fuel=500.1,
            endurance_time="08:45",
            enroute_fuel=155000.1,
            enroute_time="06:30",
            equipment="SDFGHIRTUWXYZ/H",
            est_dep_time=parse_datetime("2023-05-01T01:01:01.123Z"),
            etops_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_alt_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_rating="85 MINUTES",
            etops_val_window="LPLA: 0317Z-0722Z",
            external_id="AFMAPP20322347140001",
            flight_plan_messages=[
                {
                    "msg_text": "Message text",
                    "route_path": "PRIMARY",
                    "severity": "SEVERE",
                    "wp_num": "20",
                }
            ],
            flight_plan_point_groups=[
                {
                    "avg_fuel_flow": 19693.1,
                    "etops_avg_wind_factor": 10.1,
                    "etops_distance": 684.1,
                    "etops_req_fuel": 4412.1,
                    "etops_temp_dev": 9.1,
                    "etops_time": "01:23",
                    "flight_plan_points": [
                        {
                            "fpp_eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                            "fpp_lat": 45.23,
                            "fpp_lon": 179.1,
                            "fpp_req_fuel": 4250.1,
                            "point_name": "CRUISE ALTITUDE ETP",
                        }
                    ],
                    "from_takeoff_time": "07:29",
                    "fsaf_avg_wind_factor": 10.1,
                    "fsaf_distance": 684.1,
                    "fsaf_req_fuel": 50380.1,
                    "fsaf_temp_dev": 9.1,
                    "fsaf_time": "01:23",
                    "fuel_calc_alt": 100.1,
                    "fuel_calc_spd": 365.1,
                    "lsaf_avg_wind_factor": 13.1,
                    "lsaf_distance": 684.1,
                    "lsaf_name": "LPPD",
                    "lsaf_req_fuel": 50787.1,
                    "lsaf_temp_dev": 9.1,
                    "lsaf_time": "01:23",
                    "planned_fuel": 190319.1,
                    "point_group_name": "ETOPS_CF_POINT_1",
                    "worst_fuel_case": "DEPRESSURIZED ENGINE OUT ETP",
                }
            ],
            flight_plan_waypoints=[
                {
                    "type": "COMMENT",
                    "waypoint_name": "KCHS",
                    "aa_tacan_channel": "31/94",
                    "air_distance": 321.1,
                    "airway": "W15",
                    "alt": 27000.1,
                    "ar_id": "AR202",
                    "arpt": "ARIP",
                    "ata": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "avg_cal_airspeed": 200.1,
                    "avg_drift_ang": -3.2,
                    "avg_ground_speed": 300.1,
                    "avg_true_airspeed": 210.1,
                    "avg_wind_dir": 165.5,
                    "avg_wind_speed": 14.4,
                    "day_low_alt": 1500.1,
                    "eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "exchanged_fuel": -30400.1,
                    "fuel_flow": 17654.1,
                    "ice_cat": "MODERATE",
                    "lat": 45.23,
                    "leg_alternate": "KCHS",
                    "leg_drag_index": 1.2,
                    "leg_fuel_degrade": 10.1,
                    "leg_mach": 0.74,
                    "leg_msn_index": 65,
                    "leg_wind_fac": -32.1,
                    "lon": 179.1,
                    "mag_course": 338.1,
                    "mag_heading": 212.1,
                    "mag_var": -13.2,
                    "navaid": "HTO",
                    "night_low_alt": 2300.1,
                    "nvg_low_alt": 2450.1,
                    "point_wind_dir": 165.5,
                    "point_wind_speed": 14.4,
                    "pri_freq": 357.5,
                    "sec_freq": 357.5,
                    "tacan_channel": "83X",
                    "temp_dev": 12.1,
                    "thunder_cat": "MODERATE",
                    "total_air_distance": 3251.1,
                    "total_flown_distance": 688.1,
                    "total_rem_distance": 1288.1,
                    "total_rem_fuel": 30453.1,
                    "total_time": "08:45",
                    "total_time_rem": "01:43",
                    "total_used_fuel": 70431.1,
                    "total_weight": 207123.1,
                    "true_course": 328.1,
                    "turb_cat": "EXTREME",
                    "vor_freq": 113.6,
                    "waypoint_num": 20,
                    "zone_distance": 212.1,
                    "zone_fuel": 1120.1,
                    "zone_time": 36.1,
                }
            ],
            flight_rules="l",
            flight_type="MILITARY",
            fuel_degrade=10.3,
            gps_raim="Failed by FAA SAPT 184022AUG2022",
            hold_down_fuel=500.1,
            hold_fuel=6000.1,
            hold_time="01:00",
            id_aircraft="4f4a67c6-40fd-11ee-be56-0242ac120002",
            id_arr_airfield="363080c2-40fd-11ee-be56-0242ac120002",
            id_dep_airfield="2a9020f6-40fd-11ee-be56-0242ac120002",
            ident_extra_fuel=5000.1,
            id_sortie="9d60c1b1-10b1-b2a7-e403-84c5d7eeb170",
            initial_cruise_speed="N0305",
            initial_flight_level="F270",
            landing_fuel=19000.1,
            leg_num=100,
            min_divert_fuel=25000.1,
            msn_index=44.1,
            notes="STS/STATE PBN/A1B2B5C2C4D2D4 EUR/PROTECTED",
            num_aircraft=1,
            op_condition_fuel=5000.1,
            op_weight=251830.5,
            origin="THIRD_PARTY_DATASOURCE",
            originator="ETARYXYX",
            planner_remark="Flight plan is good for 2 days before airspace closes over the UK.",
            ramp_fuel=180000.1,
            rem_alternate1_fuel=18000.1,
            rem_alternate2_fuel=18000.1,
            reserve_fuel=10000.1,
            route_string="RENV3B RENVI Y86 GOSVA/N0317F260 DCT EVLIT DCT UMUGI DCT NISIX DCT GIGOD DCT DIPEB DCT\nGORPI Z80 TILAV L87 RAKIT Z717 PODUS Z130 MAG/N0298F220 Z20 KENIG/N0319F220 Z20 ORTAG T177\nESEGU Z20 BEBLA DCT MASEK/N0300F200 DCT GISEM/N0319F200 DCT BOMBI/N0276F060 DCT RIDSU DCT",
            sid="RENV3B",
            star="ADANA",
            status="APPROVED",
            tail_number="77187",
            takeoff_fuel=178500.1,
            taxi_fuel=1500.1,
            thunder_avoid_fuel=1000.1,
            toc_fuel=160000.1,
            toc_ice_fuel=1000.1,
            tod_fuel=32000.1,
            tod_ice_fuel=2000.1,
            unident_extra_fuel=5000.1,
            unusable_fuel=2300.1,
            wake_turb_cat="MEDIUM",
            wind_fac1=-1.1,
            wind_fac2=10.1,
            wind_fac_avg=5.1,
            wx_valid_end=parse_datetime("2023-05-01T01:01:01.123Z"),
            wx_valid_start=parse_datetime("2023-05-01T01:01:01.123Z"),
        )
        assert flightplan is None

    @parametrize
    def test_raw_response_update(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert flightplan is None

    @parametrize
    def test_streaming_response_update(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.flightplan.with_raw_response.update(
                path_id="",
                arr_airfield="KCHS",
                classification_marking="U",
                data_mode="TEST",
                dep_airfield="KSLV",
                gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
                source="Bluestaq",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.list()
        assert_matches_type(SyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert_matches_type(SyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert_matches_type(SyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.delete(
            "id",
        )
        assert flightplan is None

    @parametrize
    def test_raw_response_delete(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert flightplan is None

    @parametrize
    def test_streaming_response_delete(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.flightplan.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.count()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert_matches_type(str, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.queryhelp()
        assert flightplan is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert flightplan is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.tuple(
            columns="columns",
        )
        assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplan.unvalidated_publish(
            body=[
                {
                    "arr_airfield": "KCHS",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "dep_airfield": "KSLV",
                    "gen_ts": parse_datetime("2023-05-01T01:01:01.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert flightplan is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.flightplan.with_raw_response.unvalidated_publish(
            body=[
                {
                    "arr_airfield": "KCHS",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "dep_airfield": "KSLV",
                    "gen_ts": parse_datetime("2023-05-01T01:01:01.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert flightplan is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.flightplan.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "arr_airfield": "KCHS",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "dep_airfield": "KSLV",
                    "gen_ts": parse_datetime("2023-05-01T01:01:01.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFlightplan:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )
        assert flightplan is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
            id="c44b0a80-9fef-63d9-6267-79037fb93e4c",
            aircraft_mds="KC-130 HERCULES",
            air_refuel_events=[
                {
                    "ar_degrade": 3.1,
                    "ar_exchanged_fuel": 1500.1,
                    "ar_num": 2,
                    "divert_fuel": 143000.1,
                    "exit_fuel": 160000.1,
                }
            ],
            amc_mission_id="AJM7939B1123",
            app_landing_fuel=3000.1,
            arr_alternate1="EDDS",
            arr_alternate1_fuel=6000.1,
            arr_alternate2="EDDM",
            arr_alternate2_fuel=6000.1,
            arr_ice_fuel=1000.1,
            arr_runway="05L",
            atc_addresses=["EYCBZMFO", "EUCHZMFP", "ETARYXYX", "EDUUZVZI"],
            avg_temp_dev=16.1,
            burned_fuel=145000.1,
            call_sign="HKY629",
            cargo_remark="Expecting 55,000 lbs. If different, call us.",
            climb_fuel=7000.1,
            climb_time="00:13",
            contingency_fuel=3000.1,
            country_codes=["US", "CA", "UK"],
            dep_alternate="LFPO",
            depress_fuel=20000.1,
            dep_runway="05L",
            drag_index=16.9,
            early_descent_fuel=500.1,
            endurance_time="08:45",
            enroute_fuel=155000.1,
            enroute_time="06:30",
            equipment="SDFGHIRTUWXYZ/H",
            est_dep_time=parse_datetime("2023-05-01T01:01:01.123Z"),
            etops_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_alt_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_rating="85 MINUTES",
            etops_val_window="LPLA: 0317Z-0722Z",
            external_id="AFMAPP20322347140001",
            flight_plan_messages=[
                {
                    "msg_text": "Message text",
                    "route_path": "PRIMARY",
                    "severity": "SEVERE",
                    "wp_num": "20",
                }
            ],
            flight_plan_point_groups=[
                {
                    "avg_fuel_flow": 19693.1,
                    "etops_avg_wind_factor": 10.1,
                    "etops_distance": 684.1,
                    "etops_req_fuel": 4412.1,
                    "etops_temp_dev": 9.1,
                    "etops_time": "01:23",
                    "flight_plan_points": [
                        {
                            "fpp_eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                            "fpp_lat": 45.23,
                            "fpp_lon": 179.1,
                            "fpp_req_fuel": 4250.1,
                            "point_name": "CRUISE ALTITUDE ETP",
                        }
                    ],
                    "from_takeoff_time": "07:29",
                    "fsaf_avg_wind_factor": 10.1,
                    "fsaf_distance": 684.1,
                    "fsaf_req_fuel": 50380.1,
                    "fsaf_temp_dev": 9.1,
                    "fsaf_time": "01:23",
                    "fuel_calc_alt": 100.1,
                    "fuel_calc_spd": 365.1,
                    "lsaf_avg_wind_factor": 13.1,
                    "lsaf_distance": 684.1,
                    "lsaf_name": "LPPD",
                    "lsaf_req_fuel": 50787.1,
                    "lsaf_temp_dev": 9.1,
                    "lsaf_time": "01:23",
                    "planned_fuel": 190319.1,
                    "point_group_name": "ETOPS_CF_POINT_1",
                    "worst_fuel_case": "DEPRESSURIZED ENGINE OUT ETP",
                }
            ],
            flight_plan_waypoints=[
                {
                    "type": "COMMENT",
                    "waypoint_name": "KCHS",
                    "aa_tacan_channel": "31/94",
                    "air_distance": 321.1,
                    "airway": "W15",
                    "alt": 27000.1,
                    "ar_id": "AR202",
                    "arpt": "ARIP",
                    "ata": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "avg_cal_airspeed": 200.1,
                    "avg_drift_ang": -3.2,
                    "avg_ground_speed": 300.1,
                    "avg_true_airspeed": 210.1,
                    "avg_wind_dir": 165.5,
                    "avg_wind_speed": 14.4,
                    "day_low_alt": 1500.1,
                    "eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "exchanged_fuel": -30400.1,
                    "fuel_flow": 17654.1,
                    "ice_cat": "MODERATE",
                    "lat": 45.23,
                    "leg_alternate": "KCHS",
                    "leg_drag_index": 1.2,
                    "leg_fuel_degrade": 10.1,
                    "leg_mach": 0.74,
                    "leg_msn_index": 65,
                    "leg_wind_fac": -32.1,
                    "lon": 179.1,
                    "mag_course": 338.1,
                    "mag_heading": 212.1,
                    "mag_var": -13.2,
                    "navaid": "HTO",
                    "night_low_alt": 2300.1,
                    "nvg_low_alt": 2450.1,
                    "point_wind_dir": 165.5,
                    "point_wind_speed": 14.4,
                    "pri_freq": 357.5,
                    "sec_freq": 357.5,
                    "tacan_channel": "83X",
                    "temp_dev": 12.1,
                    "thunder_cat": "MODERATE",
                    "total_air_distance": 3251.1,
                    "total_flown_distance": 688.1,
                    "total_rem_distance": 1288.1,
                    "total_rem_fuel": 30453.1,
                    "total_time": "08:45",
                    "total_time_rem": "01:43",
                    "total_used_fuel": 70431.1,
                    "total_weight": 207123.1,
                    "true_course": 328.1,
                    "turb_cat": "EXTREME",
                    "vor_freq": 113.6,
                    "waypoint_num": 20,
                    "zone_distance": 212.1,
                    "zone_fuel": 1120.1,
                    "zone_time": 36.1,
                }
            ],
            flight_rules="l",
            flight_type="MILITARY",
            fuel_degrade=10.3,
            gps_raim="Failed by FAA SAPT 184022AUG2022",
            hold_down_fuel=500.1,
            hold_fuel=6000.1,
            hold_time="01:00",
            id_aircraft="4f4a67c6-40fd-11ee-be56-0242ac120002",
            id_arr_airfield="363080c2-40fd-11ee-be56-0242ac120002",
            id_dep_airfield="2a9020f6-40fd-11ee-be56-0242ac120002",
            ident_extra_fuel=5000.1,
            id_sortie="9d60c1b1-10b1-b2a7-e403-84c5d7eeb170",
            initial_cruise_speed="N0305",
            initial_flight_level="F270",
            landing_fuel=19000.1,
            leg_num=100,
            min_divert_fuel=25000.1,
            msn_index=44.1,
            notes="STS/STATE PBN/A1B2B5C2C4D2D4 EUR/PROTECTED",
            num_aircraft=1,
            op_condition_fuel=5000.1,
            op_weight=251830.5,
            origin="THIRD_PARTY_DATASOURCE",
            originator="ETARYXYX",
            planner_remark="Flight plan is good for 2 days before airspace closes over the UK.",
            ramp_fuel=180000.1,
            rem_alternate1_fuel=18000.1,
            rem_alternate2_fuel=18000.1,
            reserve_fuel=10000.1,
            route_string="RENV3B RENVI Y86 GOSVA/N0317F260 DCT EVLIT DCT UMUGI DCT NISIX DCT GIGOD DCT DIPEB DCT\nGORPI Z80 TILAV L87 RAKIT Z717 PODUS Z130 MAG/N0298F220 Z20 KENIG/N0319F220 Z20 ORTAG T177\nESEGU Z20 BEBLA DCT MASEK/N0300F200 DCT GISEM/N0319F200 DCT BOMBI/N0276F060 DCT RIDSU DCT",
            sid="RENV3B",
            star="ADANA",
            status="APPROVED",
            tail_number="77187",
            takeoff_fuel=178500.1,
            taxi_fuel=1500.1,
            thunder_avoid_fuel=1000.1,
            toc_fuel=160000.1,
            toc_ice_fuel=1000.1,
            tod_fuel=32000.1,
            tod_ice_fuel=2000.1,
            unident_extra_fuel=5000.1,
            unusable_fuel=2300.1,
            wake_turb_cat="MEDIUM",
            wind_fac1=-1.1,
            wind_fac2=10.1,
            wind_fac_avg=5.1,
            wx_valid_end=parse_datetime("2023-05-01T01:01:01.123Z"),
            wx_valid_start=parse_datetime("2023-05-01T01:01:01.123Z"),
        )
        assert flightplan is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert flightplan is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.create(
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.retrieve(
            id="id",
        )
        assert_matches_type(FlightPlanFull, flightplan, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FlightPlanFull, flightplan, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert_matches_type(FlightPlanFull, flightplan, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert_matches_type(FlightPlanFull, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.flightplan.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )
        assert flightplan is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
            body_id="c44b0a80-9fef-63d9-6267-79037fb93e4c",
            aircraft_mds="KC-130 HERCULES",
            air_refuel_events=[
                {
                    "ar_degrade": 3.1,
                    "ar_exchanged_fuel": 1500.1,
                    "ar_num": 2,
                    "divert_fuel": 143000.1,
                    "exit_fuel": 160000.1,
                }
            ],
            amc_mission_id="AJM7939B1123",
            app_landing_fuel=3000.1,
            arr_alternate1="EDDS",
            arr_alternate1_fuel=6000.1,
            arr_alternate2="EDDM",
            arr_alternate2_fuel=6000.1,
            arr_ice_fuel=1000.1,
            arr_runway="05L",
            atc_addresses=["EYCBZMFO", "EUCHZMFP", "ETARYXYX", "EDUUZVZI"],
            avg_temp_dev=16.1,
            burned_fuel=145000.1,
            call_sign="HKY629",
            cargo_remark="Expecting 55,000 lbs. If different, call us.",
            climb_fuel=7000.1,
            climb_time="00:13",
            contingency_fuel=3000.1,
            country_codes=["US", "CA", "UK"],
            dep_alternate="LFPO",
            depress_fuel=20000.1,
            dep_runway="05L",
            drag_index=16.9,
            early_descent_fuel=500.1,
            endurance_time="08:45",
            enroute_fuel=155000.1,
            enroute_time="06:30",
            equipment="SDFGHIRTUWXYZ/H",
            est_dep_time=parse_datetime("2023-05-01T01:01:01.123Z"),
            etops_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_alt_airfields=["KHSV", "KISP", "KBG", "LTBS"],
            etops_rating="85 MINUTES",
            etops_val_window="LPLA: 0317Z-0722Z",
            external_id="AFMAPP20322347140001",
            flight_plan_messages=[
                {
                    "msg_text": "Message text",
                    "route_path": "PRIMARY",
                    "severity": "SEVERE",
                    "wp_num": "20",
                }
            ],
            flight_plan_point_groups=[
                {
                    "avg_fuel_flow": 19693.1,
                    "etops_avg_wind_factor": 10.1,
                    "etops_distance": 684.1,
                    "etops_req_fuel": 4412.1,
                    "etops_temp_dev": 9.1,
                    "etops_time": "01:23",
                    "flight_plan_points": [
                        {
                            "fpp_eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                            "fpp_lat": 45.23,
                            "fpp_lon": 179.1,
                            "fpp_req_fuel": 4250.1,
                            "point_name": "CRUISE ALTITUDE ETP",
                        }
                    ],
                    "from_takeoff_time": "07:29",
                    "fsaf_avg_wind_factor": 10.1,
                    "fsaf_distance": 684.1,
                    "fsaf_req_fuel": 50380.1,
                    "fsaf_temp_dev": 9.1,
                    "fsaf_time": "01:23",
                    "fuel_calc_alt": 100.1,
                    "fuel_calc_spd": 365.1,
                    "lsaf_avg_wind_factor": 13.1,
                    "lsaf_distance": 684.1,
                    "lsaf_name": "LPPD",
                    "lsaf_req_fuel": 50787.1,
                    "lsaf_temp_dev": 9.1,
                    "lsaf_time": "01:23",
                    "planned_fuel": 190319.1,
                    "point_group_name": "ETOPS_CF_POINT_1",
                    "worst_fuel_case": "DEPRESSURIZED ENGINE OUT ETP",
                }
            ],
            flight_plan_waypoints=[
                {
                    "type": "COMMENT",
                    "waypoint_name": "KCHS",
                    "aa_tacan_channel": "31/94",
                    "air_distance": 321.1,
                    "airway": "W15",
                    "alt": 27000.1,
                    "ar_id": "AR202",
                    "arpt": "ARIP",
                    "ata": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "avg_cal_airspeed": 200.1,
                    "avg_drift_ang": -3.2,
                    "avg_ground_speed": 300.1,
                    "avg_true_airspeed": 210.1,
                    "avg_wind_dir": 165.5,
                    "avg_wind_speed": 14.4,
                    "day_low_alt": 1500.1,
                    "eta": parse_datetime("2023-09-09T01:00:00.123Z"),
                    "exchanged_fuel": -30400.1,
                    "fuel_flow": 17654.1,
                    "ice_cat": "MODERATE",
                    "lat": 45.23,
                    "leg_alternate": "KCHS",
                    "leg_drag_index": 1.2,
                    "leg_fuel_degrade": 10.1,
                    "leg_mach": 0.74,
                    "leg_msn_index": 65,
                    "leg_wind_fac": -32.1,
                    "lon": 179.1,
                    "mag_course": 338.1,
                    "mag_heading": 212.1,
                    "mag_var": -13.2,
                    "navaid": "HTO",
                    "night_low_alt": 2300.1,
                    "nvg_low_alt": 2450.1,
                    "point_wind_dir": 165.5,
                    "point_wind_speed": 14.4,
                    "pri_freq": 357.5,
                    "sec_freq": 357.5,
                    "tacan_channel": "83X",
                    "temp_dev": 12.1,
                    "thunder_cat": "MODERATE",
                    "total_air_distance": 3251.1,
                    "total_flown_distance": 688.1,
                    "total_rem_distance": 1288.1,
                    "total_rem_fuel": 30453.1,
                    "total_time": "08:45",
                    "total_time_rem": "01:43",
                    "total_used_fuel": 70431.1,
                    "total_weight": 207123.1,
                    "true_course": 328.1,
                    "turb_cat": "EXTREME",
                    "vor_freq": 113.6,
                    "waypoint_num": 20,
                    "zone_distance": 212.1,
                    "zone_fuel": 1120.1,
                    "zone_time": 36.1,
                }
            ],
            flight_rules="l",
            flight_type="MILITARY",
            fuel_degrade=10.3,
            gps_raim="Failed by FAA SAPT 184022AUG2022",
            hold_down_fuel=500.1,
            hold_fuel=6000.1,
            hold_time="01:00",
            id_aircraft="4f4a67c6-40fd-11ee-be56-0242ac120002",
            id_arr_airfield="363080c2-40fd-11ee-be56-0242ac120002",
            id_dep_airfield="2a9020f6-40fd-11ee-be56-0242ac120002",
            ident_extra_fuel=5000.1,
            id_sortie="9d60c1b1-10b1-b2a7-e403-84c5d7eeb170",
            initial_cruise_speed="N0305",
            initial_flight_level="F270",
            landing_fuel=19000.1,
            leg_num=100,
            min_divert_fuel=25000.1,
            msn_index=44.1,
            notes="STS/STATE PBN/A1B2B5C2C4D2D4 EUR/PROTECTED",
            num_aircraft=1,
            op_condition_fuel=5000.1,
            op_weight=251830.5,
            origin="THIRD_PARTY_DATASOURCE",
            originator="ETARYXYX",
            planner_remark="Flight plan is good for 2 days before airspace closes over the UK.",
            ramp_fuel=180000.1,
            rem_alternate1_fuel=18000.1,
            rem_alternate2_fuel=18000.1,
            reserve_fuel=10000.1,
            route_string="RENV3B RENVI Y86 GOSVA/N0317F260 DCT EVLIT DCT UMUGI DCT NISIX DCT GIGOD DCT DIPEB DCT\nGORPI Z80 TILAV L87 RAKIT Z717 PODUS Z130 MAG/N0298F220 Z20 KENIG/N0319F220 Z20 ORTAG T177\nESEGU Z20 BEBLA DCT MASEK/N0300F200 DCT GISEM/N0319F200 DCT BOMBI/N0276F060 DCT RIDSU DCT",
            sid="RENV3B",
            star="ADANA",
            status="APPROVED",
            tail_number="77187",
            takeoff_fuel=178500.1,
            taxi_fuel=1500.1,
            thunder_avoid_fuel=1000.1,
            toc_fuel=160000.1,
            toc_ice_fuel=1000.1,
            tod_fuel=32000.1,
            tod_ice_fuel=2000.1,
            unident_extra_fuel=5000.1,
            unusable_fuel=2300.1,
            wake_turb_cat="MEDIUM",
            wind_fac1=-1.1,
            wind_fac2=10.1,
            wind_fac_avg=5.1,
            wx_valid_end=parse_datetime("2023-05-01T01:01:01.123Z"),
            wx_valid_start=parse_datetime("2023-05-01T01:01:01.123Z"),
        )
        assert flightplan is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert flightplan is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.update(
            path_id="id",
            arr_airfield="KCHS",
            classification_marking="U",
            data_mode="TEST",
            dep_airfield="KSLV",
            gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.flightplan.with_raw_response.update(
                path_id="",
                arr_airfield="KCHS",
                classification_marking="U",
                data_mode="TEST",
                dep_airfield="KSLV",
                gen_ts=parse_datetime("2023-05-01T01:01:01.123Z"),
                source="Bluestaq",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.list()
        assert_matches_type(AsyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.list(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert_matches_type(AsyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert_matches_type(AsyncOffsetPage[FlightPlanAbridged], flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.delete(
            "id",
        )
        assert flightplan is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert flightplan is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.flightplan.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.count()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.count(
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert_matches_type(str, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.queryhelp()
        assert flightplan is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert flightplan is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.tuple(
            columns="columns",
        )
        assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.tuple(
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert_matches_type(FlightplanTupleResponse, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplan.unvalidated_publish(
            body=[
                {
                    "arr_airfield": "KCHS",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "dep_airfield": "KSLV",
                    "gen_ts": parse_datetime("2023-05-01T01:01:01.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert flightplan is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplan.with_raw_response.unvalidated_publish(
            body=[
                {
                    "arr_airfield": "KCHS",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "dep_airfield": "KSLV",
                    "gen_ts": parse_datetime("2023-05-01T01:01:01.123Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert flightplan is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplan.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "arr_airfield": "KCHS",
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "dep_airfield": "KSLV",
                    "gen_ts": parse_datetime("2023-05-01T01:01:01.123Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True
