# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    SoiObservationSetListResponse,
    SoiObservationSetTupleResponse,
)
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.soi_observation_set import SoiObservationSetFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSoiObservationSet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
        )
        assert soi_observation_set is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            binning_horiz=2,
            binning_vert=2,
            brightness_variance_change_detected=True,
            calibrations=[
                {
                    "cal_bg_intensity": 1.1,
                    "cal_extinction_coeff": 0.2,
                    "cal_extinction_coeff_max_unc": 0.19708838,
                    "cal_extinction_coeff_unc": 0.06474939,
                    "cal_num_correlated_stars": 1,
                    "cal_num_detected_stars": 1,
                    "cal_sky_bg": 30086.25,
                    "cal_spectral_filter_solar_mag": 19.23664587,
                    "cal_time": parse_datetime("2023-01-02T16:00:00.123Z"),
                    "cal_type": "PRE",
                    "cal_zero_point": 25.15682157,
                }
            ],
            calibration_type="ALL SKY",
            change_conf="MEDIUM",
            change_detected=True,
            collection_density_conf="MEDIUM",
            collection_id="b5133288-ab63-4b15-81f6-c7eec0cdb0c0",
            collection_mode="RATE TRACK",
            corr_quality=0.327,
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            gain=234.2,
            id_elset="REF-ELSET-ID",
            id_sensor="SENSOR-ID",
            los_declination_end=1.1,
            los_declination_start=1.1,
            msg_create_date=parse_datetime("2022-07-07T16:00:00.123Z"),
            num_spectral_filters=10,
            optical_soi_observation_list=[
                {
                    "ob_start_time": parse_datetime("2018-01-01T16:00:00.888456Z"),
                    "current_spectral_filter_num": 0,
                    "declinations": [-0.45, -0.45, -0.45],
                    "exp_duration": 0.455,
                    "extinction_coeffs": [0.32, 0.32, 0.32],
                    "extinction_coeffs_unc": [0.06, 0.06, 0.06],
                    "intensities": [1.1, 1.1, 1.1],
                    "intensity_times": [
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                        parse_datetime("2018-01-01T16:00:00.898456Z"),
                        parse_datetime("2018-01-01T16:00:00.998456Z"),
                    ],
                    "local_sky_bgs": [100625.375, 100625.375, 100625.375],
                    "local_sky_bgs_unc": [0.065, 0.065, 0.065],
                    "num_correlated_stars": [3, 3, 3],
                    "num_detected_stars": [6, 6, 6],
                    "percent_sats": [0.1, 0.2, 1],
                    "ra_rates": [0, 0, 0],
                    "ras": [107.4, 107.4, 107.4],
                    "sky_bgs": [100625.375, 100625.375, 100625.375],
                    "zero_points": [24.711, 24.711, 24.711],
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            percent_sat_threshold=0.1,
            periodicity_change_detected=True,
            periodicity_detection_conf="MEDIUM",
            periodicity_sampling_conf="MEDIUM",
            pixel_array_height=32,
            pixel_array_width=32,
            pixel_max=16383,
            pixel_min=0,
            pointing_angle_az_end=1.1,
            pointing_angle_az_start=1.1,
            pointing_angle_el_end=1.1,
            pointing_angle_el_start=1.1,
            polar_angle_end=1.1,
            polar_angle_start=1.1,
            radar_soi_observation_list=[
                {
                    "ob_start_time": parse_datetime("2018-01-01T16:00:00.888456Z"),
                    "aspect_angles": [4.278, 4.278, 4.278],
                    "azimuth_biases": [45.23, 45.23, 45.23],
                    "azimuth_rates": [-1.481, -1.481, -1.481],
                    "azimuths": [278.27, 278.27, 278.27],
                    "beta": -89.97,
                    "center_frequency": 160047.0625,
                    "cross_range_res": [11.301, 11.301, 11.301],
                    "delta_times": [0.005, 0.005, 0.005],
                    "doppler2_x_rs": [5644.27, 5644.27, 5644.27],
                    "elevation_biases": [1.23, 1.23, 1.23],
                    "elevation_rates": [-0.074, -0.074, -0.074],
                    "elevations": [70.85, 70.85, 70.85],
                    "id_attitude_set": "99a0de63-b38f-4d81-b057",
                    "id_state_vector": "99a0de63-b38f-4d81-b057",
                    "integration_angles": [8.594, 8.594, 8.594],
                    "kappa": 103.04,
                    "peak_amplitudes": [33.1, 33.1, 33.1],
                    "polarizations": ["H", "L", "V"],
                    "proj_ang_vels": [0.166, 0.166, 0.166],
                    "pulse_bandwidth": 24094.12,
                    "range_accels": [0.12, 0.01, 0.2],
                    "range_biases": [1.23, 1.23, 1.23],
                    "range_rates": [0.317, 0.317, 0.317],
                    "ranges": [877.938, 877.938, 877.938],
                    "rcs_error_ests": [0.01, 0.003, 0.001],
                    "rcs_values": [12.34, 26.11, 43.21],
                    "rspaces": [0.006, 0.006, 0.006],
                    "spectral_widths": [23.45, 20.57, 12.21],
                    "tovs": [
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                    ],
                    "xaccel": [-0.075, -0.74, -0.4],
                    "xpos": [-1118.577381, -1118.577381, -1118.577381],
                    "xspaces": [0.006, 0.006, 0.006],
                    "xvel": [-4.25242784, -4.25242784, -4.25242784],
                    "yaccel": [-0.007, 0.003, 0.1],
                    "ypos": [3026.231084, 3026.231084, 3026.231084],
                    "yvel": [5.291107434, 5.291107434, 5.291107434],
                    "zaccel": [0.1, 0.2, 0.3],
                    "zpos": [6167.831808, 6167.831808, 6167.831808],
                    "zvel": [-3.356493869, -3.356493869, -3.356493869],
                }
            ],
            reference_frame="J2000",
            satellite_name="TITAN 3C TRANSTAGE R/B",
            sat_no=101,
            senalt=1.1,
            senlat=45.1,
            senlon=179.1,
            sen_reference_frame="J2000",
            sensor_as_id="026dd511-8ba5-47d3-9909-836149f87686",
            senvelx=1.1,
            senvely=1.1,
            senvelz=1.1,
            senx=1.1,
            seny=1.1,
            senz=1.1,
            software_version="GSV99/17-1",
            solar_mag=-26.91,
            solar_phase_angle_brightness_change_detected=True,
            spectral_filters=["Keyword1", "Keyword2"],
            star_cat_name="SSTRC5",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            uct=True,
            valid_calibrations="BOTH",
        )
        assert soi_observation_set is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert soi_observation_set is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert_matches_type(SyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert_matches_type(SyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, soi_observation_set, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, soi_observation_set, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert_matches_type(str, soi_observation_set, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert_matches_type(str, soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )
        assert soi_observation_set is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert soi_observation_set is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.get(
            id="id",
        )
        assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.soi_observation_set.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.queryhelp()
        assert soi_observation_set is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert soi_observation_set is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        soi_observation_set = client.soi_observation_set.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )
        assert soi_observation_set is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.soi_observation_set.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = response.parse()
        assert soi_observation_set is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.soi_observation_set.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSoiObservationSet:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
        )
        assert soi_observation_set is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
            id="026dd511-8ba5-47d3-9909-836149f87686",
            binning_horiz=2,
            binning_vert=2,
            brightness_variance_change_detected=True,
            calibrations=[
                {
                    "cal_bg_intensity": 1.1,
                    "cal_extinction_coeff": 0.2,
                    "cal_extinction_coeff_max_unc": 0.19708838,
                    "cal_extinction_coeff_unc": 0.06474939,
                    "cal_num_correlated_stars": 1,
                    "cal_num_detected_stars": 1,
                    "cal_sky_bg": 30086.25,
                    "cal_spectral_filter_solar_mag": 19.23664587,
                    "cal_time": parse_datetime("2023-01-02T16:00:00.123Z"),
                    "cal_type": "PRE",
                    "cal_zero_point": 25.15682157,
                }
            ],
            calibration_type="ALL SKY",
            change_conf="MEDIUM",
            change_detected=True,
            collection_density_conf="MEDIUM",
            collection_id="b5133288-ab63-4b15-81f6-c7eec0cdb0c0",
            collection_mode="RATE TRACK",
            corr_quality=0.327,
            end_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            gain=234.2,
            id_elset="REF-ELSET-ID",
            id_sensor="SENSOR-ID",
            los_declination_end=1.1,
            los_declination_start=1.1,
            msg_create_date=parse_datetime("2022-07-07T16:00:00.123Z"),
            num_spectral_filters=10,
            optical_soi_observation_list=[
                {
                    "ob_start_time": parse_datetime("2018-01-01T16:00:00.888456Z"),
                    "current_spectral_filter_num": 0,
                    "declinations": [-0.45, -0.45, -0.45],
                    "exp_duration": 0.455,
                    "extinction_coeffs": [0.32, 0.32, 0.32],
                    "extinction_coeffs_unc": [0.06, 0.06, 0.06],
                    "intensities": [1.1, 1.1, 1.1],
                    "intensity_times": [
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                        parse_datetime("2018-01-01T16:00:00.898456Z"),
                        parse_datetime("2018-01-01T16:00:00.998456Z"),
                    ],
                    "local_sky_bgs": [100625.375, 100625.375, 100625.375],
                    "local_sky_bgs_unc": [0.065, 0.065, 0.065],
                    "num_correlated_stars": [3, 3, 3],
                    "num_detected_stars": [6, 6, 6],
                    "percent_sats": [0.1, 0.2, 1],
                    "ra_rates": [0, 0, 0],
                    "ras": [107.4, 107.4, 107.4],
                    "sky_bgs": [100625.375, 100625.375, 100625.375],
                    "zero_points": [24.711, 24.711, 24.711],
                }
            ],
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            percent_sat_threshold=0.1,
            periodicity_change_detected=True,
            periodicity_detection_conf="MEDIUM",
            periodicity_sampling_conf="MEDIUM",
            pixel_array_height=32,
            pixel_array_width=32,
            pixel_max=16383,
            pixel_min=0,
            pointing_angle_az_end=1.1,
            pointing_angle_az_start=1.1,
            pointing_angle_el_end=1.1,
            pointing_angle_el_start=1.1,
            polar_angle_end=1.1,
            polar_angle_start=1.1,
            radar_soi_observation_list=[
                {
                    "ob_start_time": parse_datetime("2018-01-01T16:00:00.888456Z"),
                    "aspect_angles": [4.278, 4.278, 4.278],
                    "azimuth_biases": [45.23, 45.23, 45.23],
                    "azimuth_rates": [-1.481, -1.481, -1.481],
                    "azimuths": [278.27, 278.27, 278.27],
                    "beta": -89.97,
                    "center_frequency": 160047.0625,
                    "cross_range_res": [11.301, 11.301, 11.301],
                    "delta_times": [0.005, 0.005, 0.005],
                    "doppler2_x_rs": [5644.27, 5644.27, 5644.27],
                    "elevation_biases": [1.23, 1.23, 1.23],
                    "elevation_rates": [-0.074, -0.074, -0.074],
                    "elevations": [70.85, 70.85, 70.85],
                    "id_attitude_set": "99a0de63-b38f-4d81-b057",
                    "id_state_vector": "99a0de63-b38f-4d81-b057",
                    "integration_angles": [8.594, 8.594, 8.594],
                    "kappa": 103.04,
                    "peak_amplitudes": [33.1, 33.1, 33.1],
                    "polarizations": ["H", "L", "V"],
                    "proj_ang_vels": [0.166, 0.166, 0.166],
                    "pulse_bandwidth": 24094.12,
                    "range_accels": [0.12, 0.01, 0.2],
                    "range_biases": [1.23, 1.23, 1.23],
                    "range_rates": [0.317, 0.317, 0.317],
                    "ranges": [877.938, 877.938, 877.938],
                    "rcs_error_ests": [0.01, 0.003, 0.001],
                    "rcs_values": [12.34, 26.11, 43.21],
                    "rspaces": [0.006, 0.006, 0.006],
                    "spectral_widths": [23.45, 20.57, 12.21],
                    "tovs": [
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                        parse_datetime("2018-01-01T16:00:00.888456Z"),
                    ],
                    "xaccel": [-0.075, -0.74, -0.4],
                    "xpos": [-1118.577381, -1118.577381, -1118.577381],
                    "xspaces": [0.006, 0.006, 0.006],
                    "xvel": [-4.25242784, -4.25242784, -4.25242784],
                    "yaccel": [-0.007, 0.003, 0.1],
                    "ypos": [3026.231084, 3026.231084, 3026.231084],
                    "yvel": [5.291107434, 5.291107434, 5.291107434],
                    "zaccel": [0.1, 0.2, 0.3],
                    "zpos": [6167.831808, 6167.831808, 6167.831808],
                    "zvel": [-3.356493869, -3.356493869, -3.356493869],
                }
            ],
            reference_frame="J2000",
            satellite_name="TITAN 3C TRANSTAGE R/B",
            sat_no=101,
            senalt=1.1,
            senlat=45.1,
            senlon=179.1,
            sen_reference_frame="J2000",
            sensor_as_id="026dd511-8ba5-47d3-9909-836149f87686",
            senvelx=1.1,
            senvely=1.1,
            senvelz=1.1,
            senx=1.1,
            seny=1.1,
            senz=1.1,
            software_version="GSV99/17-1",
            solar_mag=-26.91,
            solar_phase_angle_brightness_change_detected=True,
            spectral_filters=["Keyword1", "Keyword2"],
            star_cat_name="SSTRC5",
            tags=["TAG1", "TAG2"],
            transaction_id="TRANSACTION-ID",
            uct=True,
            valid_calibrations="BOTH",
        )
        assert soi_observation_set is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert soi_observation_set is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            num_obs=1,
            source="Bluestaq",
            start_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            type="OPTICAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert_matches_type(AsyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.list(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert_matches_type(AsyncOffsetPage[SoiObservationSetListResponse], soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, soi_observation_set, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, soi_observation_set, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert_matches_type(str, soi_observation_set, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.count(
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert_matches_type(str, soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )
        assert soi_observation_set is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert soi_observation_set is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.get(
            id="id",
        )
        assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.get(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert_matches_type(SoiObservationSetFull, soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.soi_observation_set.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.queryhelp()
        assert soi_observation_set is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert soi_observation_set is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.tuple(
            columns="columns",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert_matches_type(SoiObservationSetTupleResponse, soi_observation_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        soi_observation_set = await async_client.soi_observation_set.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )
        assert soi_observation_set is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.soi_observation_set.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        soi_observation_set = await response.parse()
        assert soi_observation_set is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.soi_observation_set.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "num_obs": 1,
                    "source": "Bluestaq",
                    "start_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "type": "OPTICAL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            soi_observation_set = await response.parse()
            assert soi_observation_set is None

        assert cast(Any, response.is_closed) is True
