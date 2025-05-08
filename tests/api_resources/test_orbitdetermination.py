# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    OrbitdeterminationGetResponse,
    OrbitdeterminationListResponse,
    OrbitdeterminationTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrbitdetermination:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
        )
        assert orbitdetermination is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            accepted_ob_ids=["EOOBSERVATION-ID1", "RADAROBSERVATION-ID1"],
            accepted_ob_typs=["EO", "RADAR"],
            agom_est=False,
            agom_model="RandomWalk",
            apriori_elset={
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
            apriori_id_elset="80e544b7-6a17-4554-8abf-7301e98f8e5d",
            apriori_id_state_vector="6e291992-8ae3-4592-bb0f-055715bf4803",
            apriori_state_vector={
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
            ballistic_coeff_est=False,
            ballistic_coeff_model="GaussMarkov",
            best_pass_wrms=0.975,
            edr=1.23,
            effective_from=parse_datetime("2023-08-28T11:20:21.247192Z"),
            effective_until=parse_datetime("2023-08-30T08:15:00.123456Z"),
            error_growth_rate=1.23,
            first_pass_wrms=0.985,
            fit_span=0.6,
            last_ob_end=parse_datetime("2023-08-28T11:20:21.247192Z"),
            last_ob_start=parse_datetime("2023-08-28T11:20:21.247192Z"),
            method_source="ASW",
            num_iterations=8,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            previous_wrms=1.02,
            rejected_ob_ids=["DIFFOFARRIVAL-ID2", "RFOBSERVATION-ID2"],
            rejected_ob_typs=["DOA", "RF"],
            rms_convergence_criteria=0.001,
            sat_no=54741,
            sensor_ids=["SENSOR-ID1", "SENSOR-ID2"],
            time_span=3.5,
            wrms=0.991,
        )
        assert orbitdetermination is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert orbitdetermination is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.list()
        assert_matches_type(SyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.list(
            first_result=0,
            id_on_orbit="idOnOrbit",
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert_matches_type(SyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert_matches_type(SyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.count()
        assert_matches_type(str, orbitdetermination, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.count(
            first_result=0,
            id_on_orbit="idOnOrbit",
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, orbitdetermination, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert_matches_type(str, orbitdetermination, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert_matches_type(str, orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )
        assert orbitdetermination is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert orbitdetermination is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.get(
            id="id",
        )
        assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.orbitdetermination.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.queryhelp()
        assert orbitdetermination is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert orbitdetermination is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.tuple(
            columns="columns",
        )
        assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.tuple(
            columns="columns",
            first_result=0,
            id_on_orbit="idOnOrbit",
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        orbitdetermination = client.orbitdetermination.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )
        assert orbitdetermination is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.orbitdetermination.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = response.parse()
        assert orbitdetermination is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.orbitdetermination.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOrbitdetermination:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
        )
        assert orbitdetermination is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
            id="026dd511-8ba5-47d3-9909-836149f87686",
            accepted_ob_ids=["EOOBSERVATION-ID1", "RADAROBSERVATION-ID1"],
            accepted_ob_typs=["EO", "RADAR"],
            agom_est=False,
            agom_model="RandomWalk",
            apriori_elset={
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
            apriori_id_elset="80e544b7-6a17-4554-8abf-7301e98f8e5d",
            apriori_id_state_vector="6e291992-8ae3-4592-bb0f-055715bf4803",
            apriori_state_vector={
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
            ballistic_coeff_est=False,
            ballistic_coeff_model="GaussMarkov",
            best_pass_wrms=0.975,
            edr=1.23,
            effective_from=parse_datetime("2023-08-28T11:20:21.247192Z"),
            effective_until=parse_datetime("2023-08-30T08:15:00.123456Z"),
            error_growth_rate=1.23,
            first_pass_wrms=0.985,
            fit_span=0.6,
            last_ob_end=parse_datetime("2023-08-28T11:20:21.247192Z"),
            last_ob_start=parse_datetime("2023-08-28T11:20:21.247192Z"),
            method_source="ASW",
            num_iterations=8,
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            previous_wrms=1.02,
            rejected_ob_ids=["DIFFOFARRIVAL-ID2", "RFOBSERVATION-ID2"],
            rejected_ob_typs=["DOA", "RF"],
            rms_convergence_criteria=0.001,
            sat_no=54741,
            sensor_ids=["SENSOR-ID1", "SENSOR-ID2"],
            time_span=3.5,
            wrms=0.991,
        )
        assert orbitdetermination is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert orbitdetermination is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            end_time=parse_datetime("2023-08-28T15:20:21.247192Z"),
            initial_od=False,
            method="BLS",
            source="Bluestaq",
            start_time=parse_datetime("2023-08-28T11:20:21.247192Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.list()
        assert_matches_type(AsyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.list(
            first_result=0,
            id_on_orbit="idOnOrbit",
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert_matches_type(AsyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert_matches_type(AsyncOffsetPage[OrbitdeterminationListResponse], orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.count()
        assert_matches_type(str, orbitdetermination, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.count(
            first_result=0,
            id_on_orbit="idOnOrbit",
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, orbitdetermination, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert_matches_type(str, orbitdetermination, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert_matches_type(str, orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )
        assert orbitdetermination is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert orbitdetermination is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.get(
            id="id",
        )
        assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert_matches_type(OrbitdeterminationGetResponse, orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.orbitdetermination.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.queryhelp()
        assert orbitdetermination is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert orbitdetermination is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.tuple(
            columns="columns",
        )
        assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.tuple(
            columns="columns",
            first_result=0,
            id_on_orbit="idOnOrbit",
            max_results=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.tuple(
            columns="columns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.tuple(
            columns="columns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert_matches_type(OrbitdeterminationTupleResponse, orbitdetermination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        orbitdetermination = await async_client.orbitdetermination.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )
        assert orbitdetermination is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.orbitdetermination.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orbitdetermination = await response.parse()
        assert orbitdetermination is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.orbitdetermination.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "end_time": parse_datetime("2023-08-28T15:20:21.247192Z"),
                    "initial_od": False,
                    "method": "BLS",
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2023-08-28T11:20:21.247192Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orbitdetermination = await response.parse()
            assert orbitdetermination is None

        assert cast(Any, response.is_closed) is True
