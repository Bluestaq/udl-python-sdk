# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    CollectRequestAbridged,
    CollectRequestTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.shared import CollectRequestFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollectRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
        )
        assert collect_request is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
            id="COLLECTREQUEST-ID",
            alt=1.1,
            arg_of_perigee=1.1,
            az=1.1,
            customer="Bluestaq",
            dec=1.1,
            duration=11,
            dwell_id="DWELL-ID",
            eccentricity=1.1,
            el=1.1,
            elset={
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
            end_time=parse_datetime("2018-01-01T18:00:00.123456Z"),
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            es_id="ES-ID",
            extent_az=1.1,
            extent_el=1.1,
            extent_range=1.1,
            external_id="EXTERNAL-ID",
            frame_rate=1.1,
            freq=1.1,
            freq_max=1.1,
            freq_min=1.1,
            id_elset="REF-ELSET-ID",
            id_manifold="REF-MANIFOLD-ID",
            id_parent_req="da98671b-34db-47bf-8c8d-7c668b92c800",
            id_plan="REF-PLAN-ID",
            id_sensor="REF-SENSOR-ID",
            id_state_vector="STATEVECTOR-ID",
            inclination=1.1,
            integration_time=1.1,
            iron=3,
            irradiance=1.1,
            lat=1.1,
            lon=1.1,
            msg_create_date=parse_datetime("2024-04-25T08:17:01.346Z"),
            msg_type="SU67",
            notes="Example notes",
            num_frames=6,
            num_obs=9,
            num_tracks=3,
            ob_type="RADAR",
            orbit_regime="GEO",
            orient_angle=1.1,
            origin="Example source",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            plan_index=8,
            polarization="H",
            priority="EMERGENCY",
            ra=1.1,
            raan=1.1,
            range=1.1,
            rcs=1.1,
            rcs_max=1.1,
            rcs_min=1.1,
            reflectance=1.1,
            sat_no=101,
            scenario="Example direction",
            semi_major_axis=1.1,
            spectral_model="Example Model",
            srch_inc=1.1,
            srch_pattern="SCAN",
            state_vector={
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
            stop_alt=1.1,
            stop_lat=1.1,
            stop_lon=1.1,
            suffix="T",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            target_size=1.1,
            task_category=4,
            task_group="729",
            task_id="TASK-ID",
            transaction_id="TRANSACTION-ID",
            true_anomoly=1.1,
            uct_follow_up=False,
            vis_mag=1.1,
            vis_mag_max=1.1,
            vis_mag_min=1.1,
            x_angle=1.1,
            y_angle=1.1,
        )
        assert collect_request is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert collect_request is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.retrieve(
            id="id",
        )
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(CollectRequestFull, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collect_requests.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(SyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(SyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(str, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )
        assert collect_request is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert collect_request is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_help(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.query_help()
        assert collect_request is None

    @parametrize
    def test_raw_response_query_help(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert collect_request is None

    @parametrize
    def test_streaming_response_query_help(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        collect_request = client.collect_requests.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )
        assert collect_request is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.collect_requests.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = response.parse()
        assert collect_request is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.collect_requests.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCollectRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
        )
        assert collect_request is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
            id="COLLECTREQUEST-ID",
            alt=1.1,
            arg_of_perigee=1.1,
            az=1.1,
            customer="Bluestaq",
            dec=1.1,
            duration=11,
            dwell_id="DWELL-ID",
            eccentricity=1.1,
            el=1.1,
            elset={
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
            end_time=parse_datetime("2018-01-01T18:00:00.123456Z"),
            epoch=parse_datetime("2018-01-01T16:00:00.123456Z"),
            es_id="ES-ID",
            extent_az=1.1,
            extent_el=1.1,
            extent_range=1.1,
            external_id="EXTERNAL-ID",
            frame_rate=1.1,
            freq=1.1,
            freq_max=1.1,
            freq_min=1.1,
            id_elset="REF-ELSET-ID",
            id_manifold="REF-MANIFOLD-ID",
            id_parent_req="da98671b-34db-47bf-8c8d-7c668b92c800",
            id_plan="REF-PLAN-ID",
            id_sensor="REF-SENSOR-ID",
            id_state_vector="STATEVECTOR-ID",
            inclination=1.1,
            integration_time=1.1,
            iron=3,
            irradiance=1.1,
            lat=1.1,
            lon=1.1,
            msg_create_date=parse_datetime("2024-04-25T08:17:01.346Z"),
            msg_type="SU67",
            notes="Example notes",
            num_frames=6,
            num_obs=9,
            num_tracks=3,
            ob_type="RADAR",
            orbit_regime="GEO",
            orient_angle=1.1,
            origin="Example source",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            plan_index=8,
            polarization="H",
            priority="EMERGENCY",
            ra=1.1,
            raan=1.1,
            range=1.1,
            rcs=1.1,
            rcs_max=1.1,
            rcs_min=1.1,
            reflectance=1.1,
            sat_no=101,
            scenario="Example direction",
            semi_major_axis=1.1,
            spectral_model="Example Model",
            srch_inc=1.1,
            srch_pattern="SCAN",
            state_vector={
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
            stop_alt=1.1,
            stop_lat=1.1,
            stop_lon=1.1,
            suffix="T",
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            target_size=1.1,
            task_category=4,
            task_group="729",
            task_id="TASK-ID",
            transaction_id="TRANSACTION-ID",
            true_anomoly=1.1,
            uct_follow_up=False,
            vis_mag=1.1,
            vis_mag_max=1.1,
            vis_mag_min=1.1,
            x_angle=1.1,
            y_angle=1.1,
        )
        assert collect_request is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert collect_request is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="DWELL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.retrieve(
            id="id",
        )
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(CollectRequestFull, collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(CollectRequestFull, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collect_requests.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(AsyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(AsyncOffsetPage[CollectRequestAbridged], collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(str, collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(str, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )
        assert collect_request is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert collect_request is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.query_help()
        assert collect_request is None

    @parametrize
    async def test_raw_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.query_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert collect_request is None

    @parametrize
    async def test_streaming_response_query_help(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.query_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert_matches_type(CollectRequestTupleResponse, collect_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        collect_request = await async_client.collect_requests.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )
        assert collect_request is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.collect_requests.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collect_request = await response.parse()
        assert collect_request is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.collect_requests.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "DWELL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collect_request = await response.parse()
            assert collect_request is None

        assert cast(Any, response.is_closed) is True
