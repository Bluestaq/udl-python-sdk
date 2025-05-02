# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    ConjunctionFull,
    ConjunctionAbridged,
    ConjunctionTupleResponse,
    ConjunctionGetHistoryResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConjunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.retrieve(
            id="id",
        )
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(ConjunctionFull, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conjunctions.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(SyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(SyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(str, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_udl(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )
        assert conjunction is None

    @parametrize
    def test_method_create_udl_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
            convert_pos_vel=True,
            id="CONJUNCTION-ID",
            ccir="Example notes",
            cd_ao_m1=0.016386,
            cd_ao_m2=0.016386,
            collision_prob=0.5,
            collision_prob_method="FOSTER-1992",
            comments="Example notes",
            concern_notes="Example notes",
            cr_ao_m1=0.013814,
            cr_ao_m2=0.013814,
            descriptor="sample_descriptor here",
            ephem_name1="MEME_SPCFT_ABC_2180000_ops_nomnvr_unclassified.oem",
            ephem_name2="MEME_SPCFT_DEF_2170000_ops_nomnvr_unclassified.txt",
            es_id1="a2ae2356-6d83-4e4b-896d-ddd1958800fa",
            es_id2="6fa31433-8beb-4b9b-8bf9-326dbd041c3f",
            event_id="some.user",
            id_state_vector1="REF-STATEVECTOR1-ID",
            id_state_vector2="REF-STATEVECTOR2-ID",
            large_cov_warning=False,
            large_rel_pos_warning=False,
            last_ob_time1=parse_datetime("2021-01-01T01:01:01.123456Z"),
            last_ob_time2=parse_datetime("2021-01-01T01:01:01.123456Z"),
            message_for="Message for space craft A",
            message_id="MESSAGE-ID",
            miss_distance=1.1,
            orig_id_on_orbit1="ORIGONORBIT1-ID",
            orig_id_on_orbit2="ORIGONORBIT2-ID",
            origin="THIRD_PARTY_DATASOURCE",
            originator="some.user",
            owner_contacted=False,
            penetration_level_sigma=1.1,
            raw_file_uri="Example link",
            rel_pos_n=1.1,
            rel_pos_r=1.1,
            rel_pos_t=1.1,
            rel_vel_mag=1.1,
            rel_vel_n=1.1,
            rel_vel_r=1.1,
            rel_vel_t=1.1,
            sat_no1=1,
            sat_no2=2,
            screen_entry_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            screen_exit_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            screen_volume_x=1.1,
            screen_volume_y=1.1,
            screen_volume_z=1.1,
            small_cov_warning=False,
            small_rel_vel_warning=False,
            state_dept_notified=False,
            state_vector1={
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
            state_vector2={
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
            tags=["PROVIDER_TAG1", "PROVIDER_TAG1"],
            thrust_accel1=0.033814,
            thrust_accel2=0.033814,
            transaction_id="TRANSACTION-ID",
            type="CONJUNCTION",
            uvw_warn=False,
            vol_entry_time=parse_datetime("2021-01-01T01:02:01.123456Z"),
            vol_exit_time=parse_datetime("2021-01-01T01:02:28.123456Z"),
            vol_shape="ELLIPSOID",
        )
        assert conjunction is None

    @parametrize
    def test_raw_response_create_udl(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_create_udl(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_history(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    def test_method_get_history_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    def test_raw_response_get_history(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_get_history(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.queryhelp()
        assert conjunction is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_conjunction_data_message(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
        )
        assert conjunction is None

    @parametrize
    def test_method_upload_conjunction_data_message_with_all_params(self, client: Unifieddatalibrary) -> None:
        conjunction = client.conjunctions.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
            tags="tags",
        )
        assert conjunction is None

    @parametrize
    def test_raw_response_upload_conjunction_data_message(self, client: Unifieddatalibrary) -> None:
        response = client.conjunctions.with_raw_response.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = response.parse()
        assert conjunction is None

    @parametrize
    def test_streaming_response_upload_conjunction_data_message(self, client: Unifieddatalibrary) -> None:
        with client.conjunctions.with_streaming_response.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True


class TestAsyncConjunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.retrieve(
            id="id",
        )
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(ConjunctionFull, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(ConjunctionFull, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conjunctions.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(AsyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.list(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(AsyncOffsetPage[ConjunctionAbridged], conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(str, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.count(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(str, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_udl(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )
        assert conjunction is None

    @parametrize
    async def test_method_create_udl_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
            convert_pos_vel=True,
            id="CONJUNCTION-ID",
            ccir="Example notes",
            cd_ao_m1=0.016386,
            cd_ao_m2=0.016386,
            collision_prob=0.5,
            collision_prob_method="FOSTER-1992",
            comments="Example notes",
            concern_notes="Example notes",
            cr_ao_m1=0.013814,
            cr_ao_m2=0.013814,
            descriptor="sample_descriptor here",
            ephem_name1="MEME_SPCFT_ABC_2180000_ops_nomnvr_unclassified.oem",
            ephem_name2="MEME_SPCFT_DEF_2170000_ops_nomnvr_unclassified.txt",
            es_id1="a2ae2356-6d83-4e4b-896d-ddd1958800fa",
            es_id2="6fa31433-8beb-4b9b-8bf9-326dbd041c3f",
            event_id="some.user",
            id_state_vector1="REF-STATEVECTOR1-ID",
            id_state_vector2="REF-STATEVECTOR2-ID",
            large_cov_warning=False,
            large_rel_pos_warning=False,
            last_ob_time1=parse_datetime("2021-01-01T01:01:01.123456Z"),
            last_ob_time2=parse_datetime("2021-01-01T01:01:01.123456Z"),
            message_for="Message for space craft A",
            message_id="MESSAGE-ID",
            miss_distance=1.1,
            orig_id_on_orbit1="ORIGONORBIT1-ID",
            orig_id_on_orbit2="ORIGONORBIT2-ID",
            origin="THIRD_PARTY_DATASOURCE",
            originator="some.user",
            owner_contacted=False,
            penetration_level_sigma=1.1,
            raw_file_uri="Example link",
            rel_pos_n=1.1,
            rel_pos_r=1.1,
            rel_pos_t=1.1,
            rel_vel_mag=1.1,
            rel_vel_n=1.1,
            rel_vel_r=1.1,
            rel_vel_t=1.1,
            sat_no1=1,
            sat_no2=2,
            screen_entry_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            screen_exit_time=parse_datetime("2021-01-01T01:01:01.123456Z"),
            screen_volume_x=1.1,
            screen_volume_y=1.1,
            screen_volume_z=1.1,
            small_cov_warning=False,
            small_rel_vel_warning=False,
            state_dept_notified=False,
            state_vector1={
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
            state_vector2={
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
            tags=["PROVIDER_TAG1", "PROVIDER_TAG1"],
            thrust_accel1=0.033814,
            thrust_accel2=0.033814,
            transaction_id="TRANSACTION-ID",
            type="CONJUNCTION",
            uvw_warn=False,
            vol_entry_time=parse_datetime("2021-01-01T01:02:01.123456Z"),
            vol_exit_time=parse_datetime("2021-01-01T01:02:28.123456Z"),
            vol_shape="ELLIPSOID",
        )
        assert conjunction is None

    @parametrize
    async def test_raw_response_create_udl(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_create_udl(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.create_udl(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            tca=parse_datetime("2021-01-01T01:01:01.123456Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    async def test_method_get_history_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            columns="columns",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_get_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_get_history(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.get_history(
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(ConjunctionGetHistoryResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.queryhelp()
        assert conjunction is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.tuple(
            columns="columns",
            tca=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert_matches_type(ConjunctionTupleResponse, conjunction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )
        assert conjunction is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.conjunctions.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "tca": parse_datetime("2021-01-01T01:01:01.123456Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_conjunction_data_message(self, async_client: AsyncUnifieddatalibrary) -> None:
        conjunction = await async_client.conjunctions.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
        )
        assert conjunction is None

    @parametrize
    async def test_method_upload_conjunction_data_message_with_all_params(
        self, async_client: AsyncUnifieddatalibrary
    ) -> None:
        conjunction = await async_client.conjunctions.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
            tags="tags",
        )
        assert conjunction is None

    @parametrize
    async def test_raw_response_upload_conjunction_data_message(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.conjunctions.with_raw_response.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conjunction = await response.parse()
        assert conjunction is None

    @parametrize
    async def test_streaming_response_upload_conjunction_data_message(
        self, async_client: AsyncUnifieddatalibrary
    ) -> None:
        async with async_client.conjunctions.with_streaming_response.upload_conjunction_data_message(
            classification="classification",
            data_mode="REAL",
            filename="filename",
            source="source",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conjunction = await response.parse()
            assert conjunction is None

        assert cast(Any, response.is_closed) is True
