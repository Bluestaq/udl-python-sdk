# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import FlightplanListResponse
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlightplans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplans.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert flightplan is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplans.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            aircraft_mds="aircraftMDS",
            air_refuel_events=[
                {
                    "ar_degrade": 0,
                    "ar_exchanged_fuel": 0,
                    "ar_num": 0,
                    "divert_fuel": 0,
                    "exit_fuel": 0,
                }
            ],
            amc_mission_id="amcMissionId",
            app_landing_fuel=0,
            arr_alternate1="arrAlternate1",
            arr_alternate1_fuel=0,
            arr_alternate2="arrAlternate2",
            arr_alternate2_fuel=0,
            arr_ice_fuel=0,
            arr_runway="arrRunway",
            atc_addresses=["string"],
            avg_temp_dev=0,
            burned_fuel=0,
            call_sign="callSign",
            cargo_remark="cargoRemark",
            climb_fuel=0,
            climb_time="climbTime",
            contingency_fuel=0,
            country_codes=["string"],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            dep_alternate="depAlternate",
            depress_fuel=0,
            dep_runway="depRunway",
            drag_index=0,
            early_descent_fuel=0,
            endurance_time="enduranceTime",
            enroute_fuel=0,
            enroute_time="enrouteTime",
            equipment="equipment",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            etops_airfields=["string"],
            etops_alt_airfields=["string"],
            etops_rating="etopsRating",
            etops_val_window="etopsValWindow",
            external_id="externalId",
            flight_plan_messages=[
                {
                    "msg_text": "msgText",
                    "route_path": "routePath",
                    "severity": "severity",
                    "wp_num": "wpNum",
                }
            ],
            flight_plan_point_groups=[
                {
                    "avg_fuel_flow": 0,
                    "etops_avg_wind_factor": 0,
                    "etops_distance": 0,
                    "etops_req_fuel": 0,
                    "etops_temp_dev": 0,
                    "etops_time": "etopsTime",
                    "flight_plan_points": [
                        {
                            "fpp_eta": "2019-12-27T18:11:19.117Z",
                            "fpp_lat": 0,
                            "fpp_lon": 0,
                            "fpp_req_fuel": 0,
                            "point_name": "pointName",
                        }
                    ],
                    "from_takeoff_time": "fromTakeoffTime",
                    "fsaf_avg_wind_factor": 0,
                    "fsaf_distance": 0,
                    "fsaf_req_fuel": 0,
                    "fsaf_temp_dev": 0,
                    "fsaf_time": "fsafTime",
                    "fuel_calc_alt": 0,
                    "fuel_calc_spd": 0,
                    "lsaf_avg_wind_factor": 0,
                    "lsaf_distance": 0,
                    "lsaf_name": "lsafName",
                    "lsaf_req_fuel": 0,
                    "lsaf_temp_dev": 0,
                    "lsaf_time": "lsafTime",
                    "planned_fuel": 0,
                    "point_group_name": "pointGroupName",
                    "worst_fuel_case": "worstFuelCase",
                }
            ],
            flight_plan_waypoints=[
                {
                    "type": "type",
                    "waypoint_name": "waypointName",
                    "aa_tacan_channel": "aaTacanChannel",
                    "air_distance": 0,
                    "airway": "airway",
                    "alt": 0,
                    "ar_id": "arId",
                    "arpt": "arpt",
                    "ata": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "avg_cal_airspeed": 0,
                    "avg_drift_ang": 0,
                    "avg_ground_speed": 0,
                    "avg_true_airspeed": 0,
                    "avg_wind_dir": 0,
                    "avg_wind_speed": 0,
                    "day_low_alt": 0,
                    "eta": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "exchanged_fuel": 0,
                    "fuel_flow": 0,
                    "ice_cat": "iceCat",
                    "lat": 0,
                    "leg_alternate": "legAlternate",
                    "leg_drag_index": 0,
                    "leg_fuel_degrade": 0,
                    "leg_mach": 0,
                    "leg_msn_index": 0,
                    "leg_wind_fac": 0,
                    "lon": 0,
                    "mag_course": 0,
                    "mag_heading": 0,
                    "mag_var": 0,
                    "navaid": "navaid",
                    "night_low_alt": 0,
                    "nvg_low_alt": 0,
                    "point_wind_dir": 0,
                    "point_wind_speed": 0,
                    "pri_freq": 0,
                    "sec_freq": 0,
                    "tacan_channel": "tacanChannel",
                    "temp_dev": 0,
                    "thunder_cat": "thunderCat",
                    "total_air_distance": 0,
                    "total_flown_distance": 0,
                    "total_rem_distance": 0,
                    "total_rem_fuel": 0,
                    "total_time": "totalTime",
                    "total_time_rem": "totalTimeRem",
                    "total_used_fuel": 0,
                    "total_weight": 0,
                    "true_course": 0,
                    "turb_cat": "turbCat",
                    "vor_freq": 0,
                    "waypoint_num": 0,
                    "zone_distance": 0,
                    "zone_fuel": 0,
                    "zone_time": 0,
                }
            ],
            flight_rules="flightRules",
            flight_type="flightType",
            fuel_degrade=0,
            gps_raim="gpsRAIM",
            hold_down_fuel=0,
            hold_fuel=0,
            hold_time="holdTime",
            id_aircraft="idAircraft",
            id_arr_airfield="idArrAirfield",
            id_dep_airfield="idDepAirfield",
            ident_extra_fuel=0,
            id_sortie="idSortie",
            initial_cruise_speed="initialCruiseSpeed",
            initial_flight_level="initialFlightLevel",
            landing_fuel=0,
            leg_num=0,
            min_divert_fuel=0,
            msn_index=0,
            notes="notes",
            num_aircraft=0,
            op_condition_fuel=0,
            op_weight=0,
            origin="origin",
            originator="originator",
            orig_network="origNetwork",
            planner_remark="plannerRemark",
            ramp_fuel=0,
            rem_alternate1_fuel=0,
            rem_alternate2_fuel=0,
            reserve_fuel=0,
            route_string="routeString",
            sid="sid",
            source_dl="sourceDL",
            star="star",
            tail_number="tailNumber",
            takeoff_fuel=0,
            taxi_fuel=0,
            thunder_avoid_fuel=0,
            toc_fuel=0,
            toc_ice_fuel=0,
            tod_fuel=0,
            tod_ice_fuel=0,
            unident_extra_fuel=0,
            unusable_fuel=0,
            wake_turb_cat="wakeTurbCat",
            wind_fac1=0,
            wind_fac2=0,
            wind_fac_avg=0,
            wx_valid_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            wx_valid_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert flightplan is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.flightplans.with_raw_response.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert flightplan is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.flightplans.with_streaming_response.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplans.list()
        assert_matches_type(FlightplanListResponse, flightplan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.flightplans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert_matches_type(FlightplanListResponse, flightplan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.flightplans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert_matches_type(FlightplanListResponse, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        flightplan = client.flightplans.count()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.flightplans.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = response.parse()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.flightplans.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = response.parse()
            assert_matches_type(str, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFlightplans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplans.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert flightplan is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplans.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            aircraft_mds="aircraftMDS",
            air_refuel_events=[
                {
                    "ar_degrade": 0,
                    "ar_exchanged_fuel": 0,
                    "ar_num": 0,
                    "divert_fuel": 0,
                    "exit_fuel": 0,
                }
            ],
            amc_mission_id="amcMissionId",
            app_landing_fuel=0,
            arr_alternate1="arrAlternate1",
            arr_alternate1_fuel=0,
            arr_alternate2="arrAlternate2",
            arr_alternate2_fuel=0,
            arr_ice_fuel=0,
            arr_runway="arrRunway",
            atc_addresses=["string"],
            avg_temp_dev=0,
            burned_fuel=0,
            call_sign="callSign",
            cargo_remark="cargoRemark",
            climb_fuel=0,
            climb_time="climbTime",
            contingency_fuel=0,
            country_codes=["string"],
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            dep_alternate="depAlternate",
            depress_fuel=0,
            dep_runway="depRunway",
            drag_index=0,
            early_descent_fuel=0,
            endurance_time="enduranceTime",
            enroute_fuel=0,
            enroute_time="enrouteTime",
            equipment="equipment",
            est_dep_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            etops_airfields=["string"],
            etops_alt_airfields=["string"],
            etops_rating="etopsRating",
            etops_val_window="etopsValWindow",
            external_id="externalId",
            flight_plan_messages=[
                {
                    "msg_text": "msgText",
                    "route_path": "routePath",
                    "severity": "severity",
                    "wp_num": "wpNum",
                }
            ],
            flight_plan_point_groups=[
                {
                    "avg_fuel_flow": 0,
                    "etops_avg_wind_factor": 0,
                    "etops_distance": 0,
                    "etops_req_fuel": 0,
                    "etops_temp_dev": 0,
                    "etops_time": "etopsTime",
                    "flight_plan_points": [
                        {
                            "fpp_eta": "2019-12-27T18:11:19.117Z",
                            "fpp_lat": 0,
                            "fpp_lon": 0,
                            "fpp_req_fuel": 0,
                            "point_name": "pointName",
                        }
                    ],
                    "from_takeoff_time": "fromTakeoffTime",
                    "fsaf_avg_wind_factor": 0,
                    "fsaf_distance": 0,
                    "fsaf_req_fuel": 0,
                    "fsaf_temp_dev": 0,
                    "fsaf_time": "fsafTime",
                    "fuel_calc_alt": 0,
                    "fuel_calc_spd": 0,
                    "lsaf_avg_wind_factor": 0,
                    "lsaf_distance": 0,
                    "lsaf_name": "lsafName",
                    "lsaf_req_fuel": 0,
                    "lsaf_temp_dev": 0,
                    "lsaf_time": "lsafTime",
                    "planned_fuel": 0,
                    "point_group_name": "pointGroupName",
                    "worst_fuel_case": "worstFuelCase",
                }
            ],
            flight_plan_waypoints=[
                {
                    "type": "type",
                    "waypoint_name": "waypointName",
                    "aa_tacan_channel": "aaTacanChannel",
                    "air_distance": 0,
                    "airway": "airway",
                    "alt": 0,
                    "ar_id": "arId",
                    "arpt": "arpt",
                    "ata": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "avg_cal_airspeed": 0,
                    "avg_drift_ang": 0,
                    "avg_ground_speed": 0,
                    "avg_true_airspeed": 0,
                    "avg_wind_dir": 0,
                    "avg_wind_speed": 0,
                    "day_low_alt": 0,
                    "eta": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "exchanged_fuel": 0,
                    "fuel_flow": 0,
                    "ice_cat": "iceCat",
                    "lat": 0,
                    "leg_alternate": "legAlternate",
                    "leg_drag_index": 0,
                    "leg_fuel_degrade": 0,
                    "leg_mach": 0,
                    "leg_msn_index": 0,
                    "leg_wind_fac": 0,
                    "lon": 0,
                    "mag_course": 0,
                    "mag_heading": 0,
                    "mag_var": 0,
                    "navaid": "navaid",
                    "night_low_alt": 0,
                    "nvg_low_alt": 0,
                    "point_wind_dir": 0,
                    "point_wind_speed": 0,
                    "pri_freq": 0,
                    "sec_freq": 0,
                    "tacan_channel": "tacanChannel",
                    "temp_dev": 0,
                    "thunder_cat": "thunderCat",
                    "total_air_distance": 0,
                    "total_flown_distance": 0,
                    "total_rem_distance": 0,
                    "total_rem_fuel": 0,
                    "total_time": "totalTime",
                    "total_time_rem": "totalTimeRem",
                    "total_used_fuel": 0,
                    "total_weight": 0,
                    "true_course": 0,
                    "turb_cat": "turbCat",
                    "vor_freq": 0,
                    "waypoint_num": 0,
                    "zone_distance": 0,
                    "zone_fuel": 0,
                    "zone_time": 0,
                }
            ],
            flight_rules="flightRules",
            flight_type="flightType",
            fuel_degrade=0,
            gps_raim="gpsRAIM",
            hold_down_fuel=0,
            hold_fuel=0,
            hold_time="holdTime",
            id_aircraft="idAircraft",
            id_arr_airfield="idArrAirfield",
            id_dep_airfield="idDepAirfield",
            ident_extra_fuel=0,
            id_sortie="idSortie",
            initial_cruise_speed="initialCruiseSpeed",
            initial_flight_level="initialFlightLevel",
            landing_fuel=0,
            leg_num=0,
            min_divert_fuel=0,
            msn_index=0,
            notes="notes",
            num_aircraft=0,
            op_condition_fuel=0,
            op_weight=0,
            origin="origin",
            originator="originator",
            orig_network="origNetwork",
            planner_remark="plannerRemark",
            ramp_fuel=0,
            rem_alternate1_fuel=0,
            rem_alternate2_fuel=0,
            reserve_fuel=0,
            route_string="routeString",
            sid="sid",
            source_dl="sourceDL",
            star="star",
            tail_number="tailNumber",
            takeoff_fuel=0,
            taxi_fuel=0,
            thunder_avoid_fuel=0,
            toc_fuel=0,
            toc_ice_fuel=0,
            tod_fuel=0,
            tod_ice_fuel=0,
            unident_extra_fuel=0,
            unusable_fuel=0,
            wake_turb_cat="wakeTurbCat",
            wind_fac1=0,
            wind_fac2=0,
            wind_fac_avg=0,
            wx_valid_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            wx_valid_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert flightplan is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplans.with_raw_response.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert flightplan is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplans.with_streaming_response.create(
            arr_airfield="arrAirfield",
            classification_marking="classificationMarking",
            data_mode="dataMode",
            dep_airfield="depAirfield",
            gen_ts=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert flightplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplans.list()
        assert_matches_type(FlightplanListResponse, flightplan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert_matches_type(FlightplanListResponse, flightplan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert_matches_type(FlightplanListResponse, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        flightplan = await async_client.flightplans.count()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.flightplans.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flightplan = await response.parse()
        assert_matches_type(str, flightplan, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.flightplans.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flightplan = await response.parse()
            assert_matches_type(str, flightplan, path=["response"])

        assert cast(Any, response.is_closed) is True
