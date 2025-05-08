# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ManeuverGetResponse,
    ManeuverListResponse,
    ManeuverTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManeuvers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
        )
        assert maneuver is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
            id="MANEUVER-ID",
            algorithm="Example algorithm",
            characterization="North-South Station Keeping",
            characterization_unc=0.15,
            cov=[1.1, 2.4, 3.4, 4.1, 5.6, 6.2, 7.9, 8, 9.2, 10.1],
            delta_mass=0.15,
            delta_pos=0.715998327,
            delta_pos_u=-0.022172844,
            delta_pos_v=-0.033700154,
            delta_pos_w=-0.714861014,
            delta_vel=0.000631505,
            delta_vel_u=0.0000350165629389647,
            delta_vel_v=0.000544413,
            delta_vel_w=-0.000318099,
            description="Example notes",
            descriptor="Example descriptor",
            event_end_time=parse_datetime("2023-11-16T01:09:01.350012Z"),
            event_id="EVENT-ID",
            id_sensor="SENSOR-ID",
            maneuver_unc=0.5,
            mnvr_accels=[0.05, 0.1, 0.05],
            mnvr_accel_times=[10.25, 50.56, 150.78],
            mnvr_accel_uncs=[0.0005, 0.001, 0.0005],
            num_accel_points=3,
            num_obs=10,
            od_fit_end_time=parse_datetime("2023-11-16T03:55:51.000000Z"),
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            post_apogee=35800.1,
            post_area=35.77,
            post_ballistic_coeff=0.000433209,
            post_drift_rate=-0.0125,
            post_eccentricity=0.000164,
            post_event_elset={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "agom": 0.0126,
                "algorithm": "Example algorithm",
                "apogee": 1.1,
                "arg_of_perigee": 1.1,
                "ballistic_coeff": 0.00815,
                "b_star": 1.1,
                "descriptor": "Example description",
                "eccentricity": 0.333,
                "ephem_type": 1,
                "id_elset": "ELSET-ID",
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "inclination": 45.1,
                "mean_anomaly": 179.1,
                "mean_motion": 1.1,
                "mean_motion_d_dot": 1.1,
                "mean_motion_dot": 1.1,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "perigee": 1.1,
                "period": 1.1,
                "raan": 1.1,
                "raw_file_uri": "Example URI",
                "rev_no": 111,
                "sat_no": 12,
                "semi_major_axis": 1.1,
                "sourced_data": ["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
                "sourced_data_types": ["RADAR", "RF"],
                "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                "transaction_id": "TRANSACTION-ID",
                "uct": False,
            },
            post_event_id_elset="225adf4c-8606-40a8-929e-63e22cffe220",
            post_event_id_state_vector="d83a23f8-1496-485a-bd88-ec5808c73299",
            post_event_state_vector={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "actual_od_span": 3.5,
                "algorithm": "SAMPLE_ALGORITHM",
                "alt1_reference_frame": "TEME",
                "alt2_reference_frame": "EFG/TDR",
                "area": 5.065,
                "b_dot": 1.23,
                "cm_offset": 1.23,
                "cov": [1.1, 2.4, 3.8, 4.2, 5.5, 6],
                "cov_method": "CALCULATED",
                "cov_reference_frame": "J2000",
                "descriptor": "descriptor",
                "drag_area": 4.739,
                "drag_coeff": 0.0224391269775,
                "drag_model": "JAC70",
                "edr": 1.23,
                "eq_cov": [1.1, 2.2],
                "error_control": 1.23,
                "fixed_step": True,
                "geopotential_model": "EGM-96",
                "iau1980_terms": 4,
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "id_state_vector": "STATEVECTOR-ID",
                "integrator_mode": "integratorMode",
                "in_track_thrust": True,
                "last_ob_end": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "last_ob_start": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "leap_second_time": parse_datetime("2021-01-01T01:01:01.123Z"),
                "lunar_solar": True,
                "mass": 164.5,
                "obs_available": 376,
                "obs_used": 374,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "partials": "ANALYTIC",
                "pedigree": "CONJUNCTION",
                "polar_motion_x": 1.23,
                "polar_motion_y": 1.23,
                "pos_unc": 0.333399744452,
                "raw_file_uri": "rawFileURI",
                "rec_od_span": 3.5,
                "reference_frame": "J2000",
                "residuals_acc": 99.5,
                "rev_no": 7205,
                "rms": 0.991,
                "sat_no": 12,
                "sigma_pos_uvw": [1.23, 4.56],
                "sigma_vel_uvw": [1.23, 4.56],
                "solar_flux_ap_avg": 1.23,
                "solar_flux_f10": 1.23,
                "solar_flux_f10_avg": 1.23,
                "solar_rad_press": True,
                "solar_rad_press_coeff": 0.0244394,
                "solid_earth_tides": True,
                "sourced_data": ["DATA1", "DATA2"],
                "sourced_data_types": ["RADAR"],
                "srp_area": 4.311,
                "step_mode": "AUTO",
                "step_size": 1.23,
                "step_size_selection": "AUTO",
                "tags": ["TAG1", "TAG2"],
                "tai_utc": 1.23,
                "thrust_accel": 1.23,
                "tracks_avail": 163,
                "tracks_used": 163,
                "transaction_id": "transactionId",
                "uct": True,
                "ut1_rate": 1.23,
                "ut1_utc": 1.23,
                "vel_unc": 0.000004,
                "xaccel": -2.12621392,
                "xpos": -1118.577381,
                "xpos_alt1": -1145.688502,
                "xpos_alt2": -1456.915926,
                "xvel": -4.25242784,
                "xvel_alt1": -4.270832252,
                "xvel_alt2": -1.219814294,
                "yaccel": 2.645553717,
                "ypos": 3026.231084,
                "ypos_alt1": 3020.729572,
                "ypos_alt2": -2883.540406,
                "yvel": 5.291107434,
                "yvel_alt1": 5.27074276,
                "yvel_alt2": -6.602080212,
                "zaccel": -1.06310696,
                "zpos": 6167.831808,
                "zpos_alt1": 6165.55187,
                "zpos_alt2": 6165.55187,
                "zvel": -3.356493869,
                "zvel_alt1": -3.365155181,
                "zvel_alt2": -3.365155181,
            },
            post_geo_longitude=-93.15,
            post_inclination=0.0327,
            post_mass=1844.5,
            post_perigee=35787.9,
            post_period=1436.01,
            post_pos_x=3589.351957,
            post_pos_y=42017.26823,
            post_pos_z=-1.27161796,
            post_raan=98.3335,
            post_radiation_press_coeff=4.51e-7,
            post_sigma_u=12.285,
            post_sigma_v=71.339,
            post_sigma_w=12.77,
            post_sma=42164.87,
            post_vel_x=-3.063152826,
            post_vel_y=0.261586769,
            post_vel_z=0.006842148,
            pre_apogee=35802,
            pre_ballistic_coeff=0.000437116,
            pre_drift_rate=-0.0125,
            pre_eccentricity=0.00017,
            pre_event_elset={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "agom": 0.0126,
                "algorithm": "Example algorithm",
                "apogee": 1.1,
                "arg_of_perigee": 1.1,
                "ballistic_coeff": 0.00815,
                "b_star": 1.1,
                "descriptor": "Example description",
                "eccentricity": 0.333,
                "ephem_type": 1,
                "id_elset": "ELSET-ID",
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "inclination": 45.1,
                "mean_anomaly": 179.1,
                "mean_motion": 1.1,
                "mean_motion_d_dot": 1.1,
                "mean_motion_dot": 1.1,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "perigee": 1.1,
                "period": 1.1,
                "raan": 1.1,
                "raw_file_uri": "Example URI",
                "rev_no": 111,
                "sat_no": 12,
                "semi_major_axis": 1.1,
                "sourced_data": ["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
                "sourced_data_types": ["RADAR", "RF"],
                "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                "transaction_id": "TRANSACTION-ID",
                "uct": False,
            },
            pre_event_id_elset="80e544b7-6a17-4554-8abf-7301e98f8e5d",
            pre_event_id_state_vector="6e291992-8ae3-4592-bb0f-055715bf4803",
            pre_event_state_vector={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "actual_od_span": 3.5,
                "algorithm": "SAMPLE_ALGORITHM",
                "alt1_reference_frame": "TEME",
                "alt2_reference_frame": "EFG/TDR",
                "area": 5.065,
                "b_dot": 1.23,
                "cm_offset": 1.23,
                "cov": [1.1, 2.4, 3.8, 4.2, 5.5, 6],
                "cov_method": "CALCULATED",
                "cov_reference_frame": "J2000",
                "descriptor": "descriptor",
                "drag_area": 4.739,
                "drag_coeff": 0.0224391269775,
                "drag_model": "JAC70",
                "edr": 1.23,
                "eq_cov": [1.1, 2.2],
                "error_control": 1.23,
                "fixed_step": True,
                "geopotential_model": "EGM-96",
                "iau1980_terms": 4,
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "id_state_vector": "STATEVECTOR-ID",
                "integrator_mode": "integratorMode",
                "in_track_thrust": True,
                "last_ob_end": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "last_ob_start": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "leap_second_time": parse_datetime("2021-01-01T01:01:01.123Z"),
                "lunar_solar": True,
                "mass": 164.5,
                "obs_available": 376,
                "obs_used": 374,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "partials": "ANALYTIC",
                "pedigree": "CONJUNCTION",
                "polar_motion_x": 1.23,
                "polar_motion_y": 1.23,
                "pos_unc": 0.333399744452,
                "raw_file_uri": "rawFileURI",
                "rec_od_span": 3.5,
                "reference_frame": "J2000",
                "residuals_acc": 99.5,
                "rev_no": 7205,
                "rms": 0.991,
                "sat_no": 12,
                "sigma_pos_uvw": [1.23, 4.56],
                "sigma_vel_uvw": [1.23, 4.56],
                "solar_flux_ap_avg": 1.23,
                "solar_flux_f10": 1.23,
                "solar_flux_f10_avg": 1.23,
                "solar_rad_press": True,
                "solar_rad_press_coeff": 0.0244394,
                "solid_earth_tides": True,
                "sourced_data": ["DATA1", "DATA2"],
                "sourced_data_types": ["RADAR"],
                "srp_area": 4.311,
                "step_mode": "AUTO",
                "step_size": 1.23,
                "step_size_selection": "AUTO",
                "tags": ["TAG1", "TAG2"],
                "tai_utc": 1.23,
                "thrust_accel": 1.23,
                "tracks_avail": 163,
                "tracks_used": 163,
                "transaction_id": "transactionId",
                "uct": True,
                "ut1_rate": 1.23,
                "ut1_utc": 1.23,
                "vel_unc": 0.000004,
                "xaccel": -2.12621392,
                "xpos": -1118.577381,
                "xpos_alt1": -1145.688502,
                "xpos_alt2": -1456.915926,
                "xvel": -4.25242784,
                "xvel_alt1": -4.270832252,
                "xvel_alt2": -1.219814294,
                "yaccel": 2.645553717,
                "ypos": 3026.231084,
                "ypos_alt1": 3020.729572,
                "ypos_alt2": -2883.540406,
                "yvel": 5.291107434,
                "yvel_alt1": 5.27074276,
                "yvel_alt2": -6.602080212,
                "zaccel": -1.06310696,
                "zpos": 6167.831808,
                "zpos_alt1": 6165.55187,
                "zpos_alt2": 6165.55187,
                "zvel": -3.356493869,
                "zvel_alt1": -3.365155181,
                "zvel_alt2": -3.365155181,
            },
            pre_geo_longitude=-93.12,
            pre_inclination=0.0336,
            pre_perigee=35786.5,
            pre_period=1436.12,
            pre_pos_x=3584.432545,
            pre_pos_y=42028.43245,
            pre_pos_z=-1.97765,
            pre_raan=98.3336,
            pre_radiation_press_coeff=4.51e-7,
            pre_sigma_u=0.215,
            pre_sigma_v=1.97,
            pre_sigma_w=0.208,
            pre_sma=42165.1,
            pre_vel_x=-2.543266,
            pre_vel_y=0.24876,
            pre_vel_z=0.0067352,
            report_time=parse_datetime("2023-11-16T04:15:00.000100Z"),
            sat_no=12,
            sourced_data=["SOURCEDDATA-ID", "SOURCEDDATA-ID"],
            sourced_data_types=["EO", "RADAR"],
            state_model="Example name",
            state_model_version=3,
            status="POSSIBLE",
            tags=["PROVIDER_TAG1", "PROVIDERTAG2"],
            total_burn_time=600.72,
            transaction_id="TRANSACTION-ID",
            uct=False,
        )
        assert maneuver is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert maneuver is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert_matches_type(SyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert_matches_type(SyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, maneuver, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, maneuver, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert_matches_type(str, maneuver, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert_matches_type(str, maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert maneuver is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert maneuver is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.get(
            id="id",
        )
        assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.maneuvers.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.queryhelp()
        assert maneuver is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert maneuver is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        maneuver = client.maneuvers.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert maneuver is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.maneuvers.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = response.parse()
        assert maneuver is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.maneuvers.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True


class TestAsyncManeuvers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
        )
        assert maneuver is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
            id="MANEUVER-ID",
            algorithm="Example algorithm",
            characterization="North-South Station Keeping",
            characterization_unc=0.15,
            cov=[1.1, 2.4, 3.4, 4.1, 5.6, 6.2, 7.9, 8, 9.2, 10.1],
            delta_mass=0.15,
            delta_pos=0.715998327,
            delta_pos_u=-0.022172844,
            delta_pos_v=-0.033700154,
            delta_pos_w=-0.714861014,
            delta_vel=0.000631505,
            delta_vel_u=0.0000350165629389647,
            delta_vel_v=0.000544413,
            delta_vel_w=-0.000318099,
            description="Example notes",
            descriptor="Example descriptor",
            event_end_time=parse_datetime("2023-11-16T01:09:01.350012Z"),
            event_id="EVENT-ID",
            id_sensor="SENSOR-ID",
            maneuver_unc=0.5,
            mnvr_accels=[0.05, 0.1, 0.05],
            mnvr_accel_times=[10.25, 50.56, 150.78],
            mnvr_accel_uncs=[0.0005, 0.001, 0.0005],
            num_accel_points=3,
            num_obs=10,
            od_fit_end_time=parse_datetime("2023-11-16T03:55:51.000000Z"),
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            post_apogee=35800.1,
            post_area=35.77,
            post_ballistic_coeff=0.000433209,
            post_drift_rate=-0.0125,
            post_eccentricity=0.000164,
            post_event_elset={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "agom": 0.0126,
                "algorithm": "Example algorithm",
                "apogee": 1.1,
                "arg_of_perigee": 1.1,
                "ballistic_coeff": 0.00815,
                "b_star": 1.1,
                "descriptor": "Example description",
                "eccentricity": 0.333,
                "ephem_type": 1,
                "id_elset": "ELSET-ID",
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "inclination": 45.1,
                "mean_anomaly": 179.1,
                "mean_motion": 1.1,
                "mean_motion_d_dot": 1.1,
                "mean_motion_dot": 1.1,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "perigee": 1.1,
                "period": 1.1,
                "raan": 1.1,
                "raw_file_uri": "Example URI",
                "rev_no": 111,
                "sat_no": 12,
                "semi_major_axis": 1.1,
                "sourced_data": ["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
                "sourced_data_types": ["RADAR", "RF"],
                "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                "transaction_id": "TRANSACTION-ID",
                "uct": False,
            },
            post_event_id_elset="225adf4c-8606-40a8-929e-63e22cffe220",
            post_event_id_state_vector="d83a23f8-1496-485a-bd88-ec5808c73299",
            post_event_state_vector={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "actual_od_span": 3.5,
                "algorithm": "SAMPLE_ALGORITHM",
                "alt1_reference_frame": "TEME",
                "alt2_reference_frame": "EFG/TDR",
                "area": 5.065,
                "b_dot": 1.23,
                "cm_offset": 1.23,
                "cov": [1.1, 2.4, 3.8, 4.2, 5.5, 6],
                "cov_method": "CALCULATED",
                "cov_reference_frame": "J2000",
                "descriptor": "descriptor",
                "drag_area": 4.739,
                "drag_coeff": 0.0224391269775,
                "drag_model": "JAC70",
                "edr": 1.23,
                "eq_cov": [1.1, 2.2],
                "error_control": 1.23,
                "fixed_step": True,
                "geopotential_model": "EGM-96",
                "iau1980_terms": 4,
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "id_state_vector": "STATEVECTOR-ID",
                "integrator_mode": "integratorMode",
                "in_track_thrust": True,
                "last_ob_end": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "last_ob_start": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "leap_second_time": parse_datetime("2021-01-01T01:01:01.123Z"),
                "lunar_solar": True,
                "mass": 164.5,
                "obs_available": 376,
                "obs_used": 374,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "partials": "ANALYTIC",
                "pedigree": "CONJUNCTION",
                "polar_motion_x": 1.23,
                "polar_motion_y": 1.23,
                "pos_unc": 0.333399744452,
                "raw_file_uri": "rawFileURI",
                "rec_od_span": 3.5,
                "reference_frame": "J2000",
                "residuals_acc": 99.5,
                "rev_no": 7205,
                "rms": 0.991,
                "sat_no": 12,
                "sigma_pos_uvw": [1.23, 4.56],
                "sigma_vel_uvw": [1.23, 4.56],
                "solar_flux_ap_avg": 1.23,
                "solar_flux_f10": 1.23,
                "solar_flux_f10_avg": 1.23,
                "solar_rad_press": True,
                "solar_rad_press_coeff": 0.0244394,
                "solid_earth_tides": True,
                "sourced_data": ["DATA1", "DATA2"],
                "sourced_data_types": ["RADAR"],
                "srp_area": 4.311,
                "step_mode": "AUTO",
                "step_size": 1.23,
                "step_size_selection": "AUTO",
                "tags": ["TAG1", "TAG2"],
                "tai_utc": 1.23,
                "thrust_accel": 1.23,
                "tracks_avail": 163,
                "tracks_used": 163,
                "transaction_id": "transactionId",
                "uct": True,
                "ut1_rate": 1.23,
                "ut1_utc": 1.23,
                "vel_unc": 0.000004,
                "xaccel": -2.12621392,
                "xpos": -1118.577381,
                "xpos_alt1": -1145.688502,
                "xpos_alt2": -1456.915926,
                "xvel": -4.25242784,
                "xvel_alt1": -4.270832252,
                "xvel_alt2": -1.219814294,
                "yaccel": 2.645553717,
                "ypos": 3026.231084,
                "ypos_alt1": 3020.729572,
                "ypos_alt2": -2883.540406,
                "yvel": 5.291107434,
                "yvel_alt1": 5.27074276,
                "yvel_alt2": -6.602080212,
                "zaccel": -1.06310696,
                "zpos": 6167.831808,
                "zpos_alt1": 6165.55187,
                "zpos_alt2": 6165.55187,
                "zvel": -3.356493869,
                "zvel_alt1": -3.365155181,
                "zvel_alt2": -3.365155181,
            },
            post_geo_longitude=-93.15,
            post_inclination=0.0327,
            post_mass=1844.5,
            post_perigee=35787.9,
            post_period=1436.01,
            post_pos_x=3589.351957,
            post_pos_y=42017.26823,
            post_pos_z=-1.27161796,
            post_raan=98.3335,
            post_radiation_press_coeff=4.51e-7,
            post_sigma_u=12.285,
            post_sigma_v=71.339,
            post_sigma_w=12.77,
            post_sma=42164.87,
            post_vel_x=-3.063152826,
            post_vel_y=0.261586769,
            post_vel_z=0.006842148,
            pre_apogee=35802,
            pre_ballistic_coeff=0.000437116,
            pre_drift_rate=-0.0125,
            pre_eccentricity=0.00017,
            pre_event_elset={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "agom": 0.0126,
                "algorithm": "Example algorithm",
                "apogee": 1.1,
                "arg_of_perigee": 1.1,
                "ballistic_coeff": 0.00815,
                "b_star": 1.1,
                "descriptor": "Example description",
                "eccentricity": 0.333,
                "ephem_type": 1,
                "id_elset": "ELSET-ID",
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "inclination": 45.1,
                "mean_anomaly": 179.1,
                "mean_motion": 1.1,
                "mean_motion_d_dot": 1.1,
                "mean_motion_dot": 1.1,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "perigee": 1.1,
                "period": 1.1,
                "raan": 1.1,
                "raw_file_uri": "Example URI",
                "rev_no": 111,
                "sat_no": 12,
                "semi_major_axis": 1.1,
                "sourced_data": ["OBSERVATION_UUID1", "OBSERVATION_UUID2"],
                "sourced_data_types": ["RADAR", "RF"],
                "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                "transaction_id": "TRANSACTION-ID",
                "uct": False,
            },
            pre_event_id_elset="80e544b7-6a17-4554-8abf-7301e98f8e5d",
            pre_event_id_state_vector="6e291992-8ae3-4592-bb0f-055715bf4803",
            pre_event_state_vector={
                "classification_marking": "U",
                "data_mode": "TEST",
                "epoch": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "source": "Bluestaq",
                "actual_od_span": 3.5,
                "algorithm": "SAMPLE_ALGORITHM",
                "alt1_reference_frame": "TEME",
                "alt2_reference_frame": "EFG/TDR",
                "area": 5.065,
                "b_dot": 1.23,
                "cm_offset": 1.23,
                "cov": [1.1, 2.4, 3.8, 4.2, 5.5, 6],
                "cov_method": "CALCULATED",
                "cov_reference_frame": "J2000",
                "descriptor": "descriptor",
                "drag_area": 4.739,
                "drag_coeff": 0.0224391269775,
                "drag_model": "JAC70",
                "edr": 1.23,
                "eq_cov": [1.1, 2.2],
                "error_control": 1.23,
                "fixed_step": True,
                "geopotential_model": "EGM-96",
                "iau1980_terms": 4,
                "id_orbit_determination": "026dd511-8ba5-47d3-9909-836149f87686",
                "id_state_vector": "STATEVECTOR-ID",
                "integrator_mode": "integratorMode",
                "in_track_thrust": True,
                "last_ob_end": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "last_ob_start": parse_datetime("2022-11-09T11:20:21.247192Z"),
                "leap_second_time": parse_datetime("2021-01-01T01:01:01.123Z"),
                "lunar_solar": True,
                "mass": 164.5,
                "obs_available": 376,
                "obs_used": 374,
                "origin": "THIRD_PARTY_DATASOURCE",
                "orig_object_id": "ORIGOBJECT-ID",
                "partials": "ANALYTIC",
                "pedigree": "CONJUNCTION",
                "polar_motion_x": 1.23,
                "polar_motion_y": 1.23,
                "pos_unc": 0.333399744452,
                "raw_file_uri": "rawFileURI",
                "rec_od_span": 3.5,
                "reference_frame": "J2000",
                "residuals_acc": 99.5,
                "rev_no": 7205,
                "rms": 0.991,
                "sat_no": 12,
                "sigma_pos_uvw": [1.23, 4.56],
                "sigma_vel_uvw": [1.23, 4.56],
                "solar_flux_ap_avg": 1.23,
                "solar_flux_f10": 1.23,
                "solar_flux_f10_avg": 1.23,
                "solar_rad_press": True,
                "solar_rad_press_coeff": 0.0244394,
                "solid_earth_tides": True,
                "sourced_data": ["DATA1", "DATA2"],
                "sourced_data_types": ["RADAR"],
                "srp_area": 4.311,
                "step_mode": "AUTO",
                "step_size": 1.23,
                "step_size_selection": "AUTO",
                "tags": ["TAG1", "TAG2"],
                "tai_utc": 1.23,
                "thrust_accel": 1.23,
                "tracks_avail": 163,
                "tracks_used": 163,
                "transaction_id": "transactionId",
                "uct": True,
                "ut1_rate": 1.23,
                "ut1_utc": 1.23,
                "vel_unc": 0.000004,
                "xaccel": -2.12621392,
                "xpos": -1118.577381,
                "xpos_alt1": -1145.688502,
                "xpos_alt2": -1456.915926,
                "xvel": -4.25242784,
                "xvel_alt1": -4.270832252,
                "xvel_alt2": -1.219814294,
                "yaccel": 2.645553717,
                "ypos": 3026.231084,
                "ypos_alt1": 3020.729572,
                "ypos_alt2": -2883.540406,
                "yvel": 5.291107434,
                "yvel_alt1": 5.27074276,
                "yvel_alt2": -6.602080212,
                "zaccel": -1.06310696,
                "zpos": 6167.831808,
                "zpos_alt1": 6165.55187,
                "zpos_alt2": 6165.55187,
                "zvel": -3.356493869,
                "zvel_alt1": -3.365155181,
                "zvel_alt2": -3.365155181,
            },
            pre_geo_longitude=-93.12,
            pre_inclination=0.0336,
            pre_perigee=35786.5,
            pre_period=1436.12,
            pre_pos_x=3584.432545,
            pre_pos_y=42028.43245,
            pre_pos_z=-1.97765,
            pre_raan=98.3336,
            pre_radiation_press_coeff=4.51e-7,
            pre_sigma_u=0.215,
            pre_sigma_v=1.97,
            pre_sigma_w=0.208,
            pre_sma=42165.1,
            pre_vel_x=-2.543266,
            pre_vel_y=0.24876,
            pre_vel_z=0.0067352,
            report_time=parse_datetime("2023-11-16T04:15:00.000100Z"),
            sat_no=12,
            sourced_data=["SOURCEDDATA-ID", "SOURCEDDATA-ID"],
            sourced_data_types=["EO", "RADAR"],
            state_model="Example name",
            state_model_version=3,
            status="POSSIBLE",
            tags=["PROVIDER_TAG1", "PROVIDERTAG2"],
            total_burn_time=600.72,
            transaction_id="TRANSACTION-ID",
            uct=False,
        )
        assert maneuver is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert maneuver is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            event_start_time=parse_datetime("2023-11-16T01:05:16.835689Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert_matches_type(AsyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.list(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert_matches_type(AsyncOffsetPage[ManeuverListResponse], maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, maneuver, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, maneuver, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert_matches_type(str, maneuver, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.count(
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert_matches_type(str, maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert maneuver is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert maneuver is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.get(
            id="id",
        )
        assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert_matches_type(ManeuverGetResponse, maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.maneuvers.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.queryhelp()
        assert maneuver is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert maneuver is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.tuple(
            columns="columns",
            event_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert_matches_type(ManeuverTupleResponse, maneuver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        maneuver = await async_client.maneuvers.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert maneuver is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.maneuvers.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maneuver = await response.parse()
        assert maneuver is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.maneuvers.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "event_start_time": parse_datetime("2023-11-16T01:05:16.835689Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maneuver = await response.parse()
            assert maneuver is None

        assert cast(Any, response.is_closed) is True
