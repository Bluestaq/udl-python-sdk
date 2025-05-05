# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary._utils import parse_datetime
from unifieddatalibrary.pagination import SyncOffsetPage, AsyncOffsetPage
from unifieddatalibrary.types.observations import (
    EoObservationAbridged,
    EoObservationTupleResponse,
)
from unifieddatalibrary.types.observations.eo_observations import EoObservationFull

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEoObservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )
        assert eo_observation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            id="EOOBSERVATION-ID",
            azimuth=1.1,
            azimuth_bias=1.1,
            azimuth_measured=True,
            azimuth_rate=1.1,
            azimuth_unc=1.1,
            bg_intensity=1.1,
            collect_method="AUTOTRACK",
            corr_quality=1.1,
            declination=1.1,
            declination_bias=1.1,
            declination_measured=True,
            declination_rate=1.1,
            declination_unc=1.1,
            descriptor="PROVIDED_DATA1",
            elevation=1.1,
            elevation_bias=1.1,
            elevation_measured=True,
            elevation_rate=1.1,
            elevation_unc=1.1,
            eoobservation_details={
                "acal_cr_pix_x": 123.2,
                "acal_cr_pix_y": 123.2,
                "acal_cr_val_x": 123.2,
                "acal_cr_val_y": 123.2,
                "acal_num_stars": 123,
                "background_signal": 4134.1,
                "background_signal_unc": 123.2,
                "binning_horiz": 12,
                "binning_vert": 14,
                "ccd_obj_pos_x": 123.3,
                "ccd_obj_pos_y": 321.4,
                "ccd_obj_width": 133.2,
                "ccd_temp": 123.4,
                "centroid_column": 0.5,
                "centroid_row": 0.1,
                "classification_marking": "U",
                "color_coeffs": [1.1, 2.1, 3.1],
                "column_variance": 0.1,
                "current_neutral_density_filter_num": 3,
                "current_spectral_filter_num": 23,
                "data_mode": "TEST",
                "declination_cov": 123.2,
                "dist_from_streak_center": [-127.153, -126.153, -125.153],
                "does": 123.2,
                "extinction_coeffs": [1.1, 2.1, 3.1],
                "extinction_coeffs_unc": [1.1, 2.1, 3.1],
                "gain": 234.2,
                "id_eo_observation": "EOOBSERVATION-ID",
                "ifov": 0.2,
                "mag_instrumental": 123.3,
                "mag_instrumental_unc": 123.3,
                "neutral_density_filter_names": ["numNeutralDensityFilters1", "numNeutralDensityFilters2"],
                "neutral_density_filter_transmissions": [1.1, 2.1, 3.1],
                "neutral_density_filter_transmissions_unc": [1.1, 2.1, 3.1],
                "num_catalog_stars": 123,
                "num_correlated_stars": 123,
                "num_detected_stars": 123,
                "num_neutral_density_filters": 12,
                "num_spectral_filters": 10,
                "obj_sun_range": 123.2,
                "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "optical_cross_section": 123.3,
                "optical_cross_section_unc": 123.3,
                "pcal_num_stars": 23,
                "peak_aperture_count": 123.2,
                "peak_background_count": 321,
                "phase_ang_bisect": 123.2,
                "pixel_array_height": 23,
                "pixel_array_width": 12,
                "pixel_max": 256,
                "pixel_min": 12,
                "predicted_azimuth": 10.1,
                "predicted_declination": 10.1,
                "predicted_declination_unc": 123.2,
                "predicted_elevation": 10.1,
                "predicted_ra": 10.1,
                "predicted_ra_unc": 123.2,
                "ra_cov": 123.2,
                "ra_declination_cov": 123.2,
                "row_col_cov": 0.01,
                "row_variance": 0.1,
                "snr_est": 13.4,
                "solar_disk_frac": 123.2,
                "source": "Bluestaq",
                "spectral_filters": ["Keyword1", "Keyword2"],
                "spectral_filter_solar_mag": [1.1, 2.1, 3.1],
                "spectral_zmfl": [1.1, 2.1, 3.1],
                "sun_azimuth": 10.1,
                "sun_elevation": 10.1,
                "sun_state_pos_x": 123.3,
                "sun_state_pos_y": 123.3,
                "sun_state_pos_z": 123.3,
                "sun_state_vel_x": 123.3,
                "sun_state_vel_y": 123.3,
                "sun_state_vel_z": 123.3,
                "surf_brightness": [21.01, 21.382, 21.725],
                "surf_brightness_unc": [0.165, 0.165, 0.165],
                "times_unc": 13.1,
                "toes": 123.2,
                "zero_points": [1.1, 2.1, 3.1],
                "zero_points_unc": [1.1, 2.1, 3.1],
            },
            exp_duration=1.1,
            fov_count=1,
            fov_count_uct=2,
            geoalt=1.1,
            geolat=1.1,
            geolon=1.1,
            georange=1.1,
            id_sensor="SENSOR-ID",
            id_sky_imagery="SKYIMAGERY-ID",
            intensity=1.1,
            los_unc=1.1,
            losx=1.1,
            losxvel=1.1,
            losy=1.1,
            losyvel=1.1,
            losz=1.1,
            loszvel=1.1,
            mag=1.1,
            mag_norm_range=1.1,
            mag_unc=1.1,
            net_obj_sig=1.1,
            net_obj_sig_unc=1.1,
            ob_position="FIRST",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            penumbra=False,
            primary_extinction=1.1,
            primary_extinction_unc=1.1,
            ra=1.1,
            ra_bias=1.1,
            ra_measured=True,
            range=1.1,
            range_bias=1.1,
            range_measured=True,
            range_rate=1.1,
            range_rate_measured=True,
            range_rate_unc=1.1,
            range_unc=1.1,
            ra_rate=1.1,
            ra_unc=1.1,
            raw_file_uri="Example URI",
            reference_frame="J2000",
            sat_no=5,
            senalt=1.1,
            senlat=45.1,
            senlon=179.1,
            sen_quat=[0.4492, 0.02, 0.8765, 0.2213],
            sen_reference_frame="J2000",
            senvelx=1.1,
            senvely=1.1,
            senvelz=1.1,
            senx=1.1,
            seny=1.1,
            senz=1.1,
            shutter_delay=1.1,
            sky_bkgrnd=1.1,
            solar_dec_angle=1.1,
            solar_eq_phase_angle=1.1,
            solar_phase_angle=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
            timing_bias=1.1,
            track_id="TRACK-ID",
            transaction_id="TRANSACTION-ID",
            uct=False,
            umbra=False,
            zeroptd=1.1,
            zero_ptd_unc=1.1,
        )
        assert eo_observation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert eo_observation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.retrieve(
            id="id",
        )
        assert_matches_type(EoObservationFull, eo_observation, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EoObservationFull, eo_observation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert_matches_type(EoObservationFull, eo_observation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert_matches_type(EoObservationFull, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.observations.eo_observations.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(SyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert_matches_type(SyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert_matches_type(SyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    def test_method_count_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert_matches_type(str, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert eo_observation is None

    @parametrize
    def test_method_create_bulk_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "id": "EOOBSERVATION-ID",
                    "azimuth": 1.1,
                    "azimuth_bias": 1.1,
                    "azimuth_measured": True,
                    "azimuth_rate": 1.1,
                    "azimuth_unc": 1.1,
                    "bg_intensity": 1.1,
                    "collect_method": "AUTOTRACK",
                    "corr_quality": 1.1,
                    "declination": 1.1,
                    "declination_bias": 1.1,
                    "declination_measured": True,
                    "declination_rate": 1.1,
                    "declination_unc": 1.1,
                    "descriptor": "PROVIDED_DATA1",
                    "elevation": 1.1,
                    "elevation_bias": 1.1,
                    "elevation_measured": True,
                    "elevation_rate": 1.1,
                    "elevation_unc": 1.1,
                    "eoobservation_details": {
                        "acal_cr_pix_x": 123.2,
                        "acal_cr_pix_y": 123.2,
                        "acal_cr_val_x": 123.2,
                        "acal_cr_val_y": 123.2,
                        "acal_num_stars": 123,
                        "background_signal": 4134.1,
                        "background_signal_unc": 123.2,
                        "binning_horiz": 12,
                        "binning_vert": 14,
                        "ccd_obj_pos_x": 123.3,
                        "ccd_obj_pos_y": 321.4,
                        "ccd_obj_width": 133.2,
                        "ccd_temp": 123.4,
                        "centroid_column": 0.5,
                        "centroid_row": 0.1,
                        "classification_marking": "U",
                        "color_coeffs": [1.1, 2.1, 3.1],
                        "column_variance": 0.1,
                        "current_neutral_density_filter_num": 3,
                        "current_spectral_filter_num": 23,
                        "data_mode": "TEST",
                        "declination_cov": 123.2,
                        "dist_from_streak_center": [-127.153, -126.153, -125.153],
                        "does": 123.2,
                        "extinction_coeffs": [1.1, 2.1, 3.1],
                        "extinction_coeffs_unc": [1.1, 2.1, 3.1],
                        "gain": 234.2,
                        "id_eo_observation": "EOOBSERVATION-ID",
                        "ifov": 0.2,
                        "mag_instrumental": 123.3,
                        "mag_instrumental_unc": 123.3,
                        "neutral_density_filter_names": ["numNeutralDensityFilters1", "numNeutralDensityFilters2"],
                        "neutral_density_filter_transmissions": [1.1, 2.1, 3.1],
                        "neutral_density_filter_transmissions_unc": [1.1, 2.1, 3.1],
                        "num_catalog_stars": 123,
                        "num_correlated_stars": 123,
                        "num_detected_stars": 123,
                        "num_neutral_density_filters": 12,
                        "num_spectral_filters": 10,
                        "obj_sun_range": 123.2,
                        "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                        "optical_cross_section": 123.3,
                        "optical_cross_section_unc": 123.3,
                        "pcal_num_stars": 23,
                        "peak_aperture_count": 123.2,
                        "peak_background_count": 321,
                        "phase_ang_bisect": 123.2,
                        "pixel_array_height": 23,
                        "pixel_array_width": 12,
                        "pixel_max": 256,
                        "pixel_min": 12,
                        "predicted_azimuth": 10.1,
                        "predicted_declination": 10.1,
                        "predicted_declination_unc": 123.2,
                        "predicted_elevation": 10.1,
                        "predicted_ra": 10.1,
                        "predicted_ra_unc": 123.2,
                        "ra_cov": 123.2,
                        "ra_declination_cov": 123.2,
                        "row_col_cov": 0.01,
                        "row_variance": 0.1,
                        "snr_est": 13.4,
                        "solar_disk_frac": 123.2,
                        "source": "Bluestaq",
                        "spectral_filters": ["Keyword1", "Keyword2"],
                        "spectral_filter_solar_mag": [1.1, 2.1, 3.1],
                        "spectral_zmfl": [1.1, 2.1, 3.1],
                        "sun_azimuth": 10.1,
                        "sun_elevation": 10.1,
                        "sun_state_pos_x": 123.3,
                        "sun_state_pos_y": 123.3,
                        "sun_state_pos_z": 123.3,
                        "sun_state_vel_x": 123.3,
                        "sun_state_vel_y": 123.3,
                        "sun_state_vel_z": 123.3,
                        "surf_brightness": [21.01, 21.382, 21.725],
                        "surf_brightness_unc": [0.165, 0.165, 0.165],
                        "times_unc": 13.1,
                        "toes": 123.2,
                        "zero_points": [1.1, 2.1, 3.1],
                        "zero_points_unc": [1.1, 2.1, 3.1],
                    },
                    "exp_duration": 1.1,
                    "fov_count": 1,
                    "fov_count_uct": 2,
                    "geoalt": 1.1,
                    "geolat": 1.1,
                    "geolon": 1.1,
                    "georange": 1.1,
                    "id_sensor": "SENSOR-ID",
                    "id_sky_imagery": "SKYIMAGERY-ID",
                    "intensity": 1.1,
                    "los_unc": 1.1,
                    "losx": 1.1,
                    "losxvel": 1.1,
                    "losy": 1.1,
                    "losyvel": 1.1,
                    "losz": 1.1,
                    "loszvel": 1.1,
                    "mag": 1.1,
                    "mag_norm_range": 1.1,
                    "mag_unc": 1.1,
                    "net_obj_sig": 1.1,
                    "net_obj_sig_unc": 1.1,
                    "ob_position": "FIRST",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "orig_sensor_id": "ORIGSENSOR-ID",
                    "penumbra": False,
                    "primary_extinction": 1.1,
                    "primary_extinction_unc": 1.1,
                    "ra": 1.1,
                    "ra_bias": 1.1,
                    "ra_measured": True,
                    "range": 1.1,
                    "range_bias": 1.1,
                    "range_measured": True,
                    "range_rate": 1.1,
                    "range_rate_measured": True,
                    "range_rate_unc": 1.1,
                    "range_unc": 1.1,
                    "ra_rate": 1.1,
                    "ra_unc": 1.1,
                    "raw_file_uri": "Example URI",
                    "reference_frame": "J2000",
                    "sat_no": 5,
                    "senalt": 1.1,
                    "senlat": 45.1,
                    "senlon": 179.1,
                    "sen_quat": [0.4492, 0.02, 0.8765, 0.2213],
                    "sen_reference_frame": "J2000",
                    "senvelx": 1.1,
                    "senvely": 1.1,
                    "senvelz": 1.1,
                    "senx": 1.1,
                    "seny": 1.1,
                    "senz": 1.1,
                    "shutter_delay": 1.1,
                    "sky_bkgrnd": 1.1,
                    "solar_dec_angle": 1.1,
                    "solar_eq_phase_angle": 1.1,
                    "solar_phase_angle": 1.1,
                    "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                    "task_id": "TASK-ID",
                    "timing_bias": 1.1,
                    "track_id": "TRACK-ID",
                    "transaction_id": "TRANSACTION-ID",
                    "uct": False,
                    "umbra": False,
                    "zeroptd": 1.1,
                    "zero_ptd_unc": 1.1,
                }
            ],
            convert_to_j2_k=True,
        )
        assert eo_observation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert eo_observation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_queryhelp(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.queryhelp()
        assert eo_observation is None

    @parametrize
    def test_raw_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert eo_observation is None

    @parametrize
    def test_streaming_response_queryhelp(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tuple(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

    @parametrize
    def test_method_tuple_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

    @parametrize
    def test_raw_response_tuple(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

    @parametrize
    def test_streaming_response_tuple(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.observations.eo_observations.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert eo_observation is None

    @parametrize
    def test_raw_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        response = client.observations.eo_observations.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert eo_observation is None

    @parametrize
    def test_streaming_response_unvalidated_publish(self, client: Unifieddatalibrary) -> None:
        with client.observations.eo_observations.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEoObservations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )
        assert eo_observation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
            id="EOOBSERVATION-ID",
            azimuth=1.1,
            azimuth_bias=1.1,
            azimuth_measured=True,
            azimuth_rate=1.1,
            azimuth_unc=1.1,
            bg_intensity=1.1,
            collect_method="AUTOTRACK",
            corr_quality=1.1,
            declination=1.1,
            declination_bias=1.1,
            declination_measured=True,
            declination_rate=1.1,
            declination_unc=1.1,
            descriptor="PROVIDED_DATA1",
            elevation=1.1,
            elevation_bias=1.1,
            elevation_measured=True,
            elevation_rate=1.1,
            elevation_unc=1.1,
            eoobservation_details={
                "acal_cr_pix_x": 123.2,
                "acal_cr_pix_y": 123.2,
                "acal_cr_val_x": 123.2,
                "acal_cr_val_y": 123.2,
                "acal_num_stars": 123,
                "background_signal": 4134.1,
                "background_signal_unc": 123.2,
                "binning_horiz": 12,
                "binning_vert": 14,
                "ccd_obj_pos_x": 123.3,
                "ccd_obj_pos_y": 321.4,
                "ccd_obj_width": 133.2,
                "ccd_temp": 123.4,
                "centroid_column": 0.5,
                "centroid_row": 0.1,
                "classification_marking": "U",
                "color_coeffs": [1.1, 2.1, 3.1],
                "column_variance": 0.1,
                "current_neutral_density_filter_num": 3,
                "current_spectral_filter_num": 23,
                "data_mode": "TEST",
                "declination_cov": 123.2,
                "dist_from_streak_center": [-127.153, -126.153, -125.153],
                "does": 123.2,
                "extinction_coeffs": [1.1, 2.1, 3.1],
                "extinction_coeffs_unc": [1.1, 2.1, 3.1],
                "gain": 234.2,
                "id_eo_observation": "EOOBSERVATION-ID",
                "ifov": 0.2,
                "mag_instrumental": 123.3,
                "mag_instrumental_unc": 123.3,
                "neutral_density_filter_names": ["numNeutralDensityFilters1", "numNeutralDensityFilters2"],
                "neutral_density_filter_transmissions": [1.1, 2.1, 3.1],
                "neutral_density_filter_transmissions_unc": [1.1, 2.1, 3.1],
                "num_catalog_stars": 123,
                "num_correlated_stars": 123,
                "num_detected_stars": 123,
                "num_neutral_density_filters": 12,
                "num_spectral_filters": 10,
                "obj_sun_range": 123.2,
                "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                "optical_cross_section": 123.3,
                "optical_cross_section_unc": 123.3,
                "pcal_num_stars": 23,
                "peak_aperture_count": 123.2,
                "peak_background_count": 321,
                "phase_ang_bisect": 123.2,
                "pixel_array_height": 23,
                "pixel_array_width": 12,
                "pixel_max": 256,
                "pixel_min": 12,
                "predicted_azimuth": 10.1,
                "predicted_declination": 10.1,
                "predicted_declination_unc": 123.2,
                "predicted_elevation": 10.1,
                "predicted_ra": 10.1,
                "predicted_ra_unc": 123.2,
                "ra_cov": 123.2,
                "ra_declination_cov": 123.2,
                "row_col_cov": 0.01,
                "row_variance": 0.1,
                "snr_est": 13.4,
                "solar_disk_frac": 123.2,
                "source": "Bluestaq",
                "spectral_filters": ["Keyword1", "Keyword2"],
                "spectral_filter_solar_mag": [1.1, 2.1, 3.1],
                "spectral_zmfl": [1.1, 2.1, 3.1],
                "sun_azimuth": 10.1,
                "sun_elevation": 10.1,
                "sun_state_pos_x": 123.3,
                "sun_state_pos_y": 123.3,
                "sun_state_pos_z": 123.3,
                "sun_state_vel_x": 123.3,
                "sun_state_vel_y": 123.3,
                "sun_state_vel_z": 123.3,
                "surf_brightness": [21.01, 21.382, 21.725],
                "surf_brightness_unc": [0.165, 0.165, 0.165],
                "times_unc": 13.1,
                "toes": 123.2,
                "zero_points": [1.1, 2.1, 3.1],
                "zero_points_unc": [1.1, 2.1, 3.1],
            },
            exp_duration=1.1,
            fov_count=1,
            fov_count_uct=2,
            geoalt=1.1,
            geolat=1.1,
            geolon=1.1,
            georange=1.1,
            id_sensor="SENSOR-ID",
            id_sky_imagery="SKYIMAGERY-ID",
            intensity=1.1,
            los_unc=1.1,
            losx=1.1,
            losxvel=1.1,
            losy=1.1,
            losyvel=1.1,
            losz=1.1,
            loszvel=1.1,
            mag=1.1,
            mag_norm_range=1.1,
            mag_unc=1.1,
            net_obj_sig=1.1,
            net_obj_sig_unc=1.1,
            ob_position="FIRST",
            origin="THIRD_PARTY_DATASOURCE",
            orig_object_id="ORIGOBJECT-ID",
            orig_sensor_id="ORIGSENSOR-ID",
            penumbra=False,
            primary_extinction=1.1,
            primary_extinction_unc=1.1,
            ra=1.1,
            ra_bias=1.1,
            ra_measured=True,
            range=1.1,
            range_bias=1.1,
            range_measured=True,
            range_rate=1.1,
            range_rate_measured=True,
            range_rate_unc=1.1,
            range_unc=1.1,
            ra_rate=1.1,
            ra_unc=1.1,
            raw_file_uri="Example URI",
            reference_frame="J2000",
            sat_no=5,
            senalt=1.1,
            senlat=45.1,
            senlon=179.1,
            sen_quat=[0.4492, 0.02, 0.8765, 0.2213],
            sen_reference_frame="J2000",
            senvelx=1.1,
            senvely=1.1,
            senvelz=1.1,
            senx=1.1,
            seny=1.1,
            senz=1.1,
            shutter_delay=1.1,
            sky_bkgrnd=1.1,
            solar_dec_angle=1.1,
            solar_eq_phase_angle=1.1,
            solar_phase_angle=1.1,
            tags=["PROVIDER_TAG1", "PROVIDER_TAG2"],
            task_id="TASK-ID",
            timing_bias=1.1,
            track_id="TRACK-ID",
            transaction_id="TRANSACTION-ID",
            uct=False,
            umbra=False,
            zeroptd=1.1,
            zero_ptd_unc=1.1,
        )
        assert eo_observation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert eo_observation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.create(
            classification_marking="U",
            data_mode="TEST",
            ob_time=parse_datetime("2018-01-01T16:00:00.123456Z"),
            source="Bluestaq",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.retrieve(
            id="id",
        )
        assert_matches_type(EoObservationFull, eo_observation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.retrieve(
            id="id",
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EoObservationFull, eo_observation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert_matches_type(EoObservationFull, eo_observation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert_matches_type(EoObservationFull, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnifieddatalibrary) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.observations.eo_observations.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(AsyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert_matches_type(AsyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert_matches_type(AsyncOffsetPage[EoObservationAbridged], eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert_matches_type(str, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert eo_observation is None

    @parametrize
    async def test_method_create_bulk_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                    "id": "EOOBSERVATION-ID",
                    "azimuth": 1.1,
                    "azimuth_bias": 1.1,
                    "azimuth_measured": True,
                    "azimuth_rate": 1.1,
                    "azimuth_unc": 1.1,
                    "bg_intensity": 1.1,
                    "collect_method": "AUTOTRACK",
                    "corr_quality": 1.1,
                    "declination": 1.1,
                    "declination_bias": 1.1,
                    "declination_measured": True,
                    "declination_rate": 1.1,
                    "declination_unc": 1.1,
                    "descriptor": "PROVIDED_DATA1",
                    "elevation": 1.1,
                    "elevation_bias": 1.1,
                    "elevation_measured": True,
                    "elevation_rate": 1.1,
                    "elevation_unc": 1.1,
                    "eoobservation_details": {
                        "acal_cr_pix_x": 123.2,
                        "acal_cr_pix_y": 123.2,
                        "acal_cr_val_x": 123.2,
                        "acal_cr_val_y": 123.2,
                        "acal_num_stars": 123,
                        "background_signal": 4134.1,
                        "background_signal_unc": 123.2,
                        "binning_horiz": 12,
                        "binning_vert": 14,
                        "ccd_obj_pos_x": 123.3,
                        "ccd_obj_pos_y": 321.4,
                        "ccd_obj_width": 133.2,
                        "ccd_temp": 123.4,
                        "centroid_column": 0.5,
                        "centroid_row": 0.1,
                        "classification_marking": "U",
                        "color_coeffs": [1.1, 2.1, 3.1],
                        "column_variance": 0.1,
                        "current_neutral_density_filter_num": 3,
                        "current_spectral_filter_num": 23,
                        "data_mode": "TEST",
                        "declination_cov": 123.2,
                        "dist_from_streak_center": [-127.153, -126.153, -125.153],
                        "does": 123.2,
                        "extinction_coeffs": [1.1, 2.1, 3.1],
                        "extinction_coeffs_unc": [1.1, 2.1, 3.1],
                        "gain": 234.2,
                        "id_eo_observation": "EOOBSERVATION-ID",
                        "ifov": 0.2,
                        "mag_instrumental": 123.3,
                        "mag_instrumental_unc": 123.3,
                        "neutral_density_filter_names": ["numNeutralDensityFilters1", "numNeutralDensityFilters2"],
                        "neutral_density_filter_transmissions": [1.1, 2.1, 3.1],
                        "neutral_density_filter_transmissions_unc": [1.1, 2.1, 3.1],
                        "num_catalog_stars": 123,
                        "num_correlated_stars": 123,
                        "num_detected_stars": 123,
                        "num_neutral_density_filters": 12,
                        "num_spectral_filters": 10,
                        "obj_sun_range": 123.2,
                        "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                        "optical_cross_section": 123.3,
                        "optical_cross_section_unc": 123.3,
                        "pcal_num_stars": 23,
                        "peak_aperture_count": 123.2,
                        "peak_background_count": 321,
                        "phase_ang_bisect": 123.2,
                        "pixel_array_height": 23,
                        "pixel_array_width": 12,
                        "pixel_max": 256,
                        "pixel_min": 12,
                        "predicted_azimuth": 10.1,
                        "predicted_declination": 10.1,
                        "predicted_declination_unc": 123.2,
                        "predicted_elevation": 10.1,
                        "predicted_ra": 10.1,
                        "predicted_ra_unc": 123.2,
                        "ra_cov": 123.2,
                        "ra_declination_cov": 123.2,
                        "row_col_cov": 0.01,
                        "row_variance": 0.1,
                        "snr_est": 13.4,
                        "solar_disk_frac": 123.2,
                        "source": "Bluestaq",
                        "spectral_filters": ["Keyword1", "Keyword2"],
                        "spectral_filter_solar_mag": [1.1, 2.1, 3.1],
                        "spectral_zmfl": [1.1, 2.1, 3.1],
                        "sun_azimuth": 10.1,
                        "sun_elevation": 10.1,
                        "sun_state_pos_x": 123.3,
                        "sun_state_pos_y": 123.3,
                        "sun_state_pos_z": 123.3,
                        "sun_state_vel_x": 123.3,
                        "sun_state_vel_y": 123.3,
                        "sun_state_vel_z": 123.3,
                        "surf_brightness": [21.01, 21.382, 21.725],
                        "surf_brightness_unc": [0.165, 0.165, 0.165],
                        "times_unc": 13.1,
                        "toes": 123.2,
                        "zero_points": [1.1, 2.1, 3.1],
                        "zero_points_unc": [1.1, 2.1, 3.1],
                    },
                    "exp_duration": 1.1,
                    "fov_count": 1,
                    "fov_count_uct": 2,
                    "geoalt": 1.1,
                    "geolat": 1.1,
                    "geolon": 1.1,
                    "georange": 1.1,
                    "id_sensor": "SENSOR-ID",
                    "id_sky_imagery": "SKYIMAGERY-ID",
                    "intensity": 1.1,
                    "los_unc": 1.1,
                    "losx": 1.1,
                    "losxvel": 1.1,
                    "losy": 1.1,
                    "losyvel": 1.1,
                    "losz": 1.1,
                    "loszvel": 1.1,
                    "mag": 1.1,
                    "mag_norm_range": 1.1,
                    "mag_unc": 1.1,
                    "net_obj_sig": 1.1,
                    "net_obj_sig_unc": 1.1,
                    "ob_position": "FIRST",
                    "origin": "THIRD_PARTY_DATASOURCE",
                    "orig_object_id": "ORIGOBJECT-ID",
                    "orig_sensor_id": "ORIGSENSOR-ID",
                    "penumbra": False,
                    "primary_extinction": 1.1,
                    "primary_extinction_unc": 1.1,
                    "ra": 1.1,
                    "ra_bias": 1.1,
                    "ra_measured": True,
                    "range": 1.1,
                    "range_bias": 1.1,
                    "range_measured": True,
                    "range_rate": 1.1,
                    "range_rate_measured": True,
                    "range_rate_unc": 1.1,
                    "range_unc": 1.1,
                    "ra_rate": 1.1,
                    "ra_unc": 1.1,
                    "raw_file_uri": "Example URI",
                    "reference_frame": "J2000",
                    "sat_no": 5,
                    "senalt": 1.1,
                    "senlat": 45.1,
                    "senlon": 179.1,
                    "sen_quat": [0.4492, 0.02, 0.8765, 0.2213],
                    "sen_reference_frame": "J2000",
                    "senvelx": 1.1,
                    "senvely": 1.1,
                    "senvelz": 1.1,
                    "senx": 1.1,
                    "seny": 1.1,
                    "senz": 1.1,
                    "shutter_delay": 1.1,
                    "sky_bkgrnd": 1.1,
                    "solar_dec_angle": 1.1,
                    "solar_eq_phase_angle": 1.1,
                    "solar_phase_angle": 1.1,
                    "tags": ["PROVIDER_TAG1", "PROVIDER_TAG2"],
                    "task_id": "TASK-ID",
                    "timing_bias": 1.1,
                    "track_id": "TRACK-ID",
                    "transaction_id": "TRANSACTION-ID",
                    "uct": False,
                    "umbra": False,
                    "zeroptd": 1.1,
                    "zero_ptd_unc": 1.1,
                }
            ],
            convert_to_j2_k=True,
        )
        assert eo_observation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert eo_observation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.queryhelp()
        assert eo_observation is None

    @parametrize
    async def test_raw_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.queryhelp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert eo_observation is None

    @parametrize
    async def test_streaming_response_queryhelp(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.queryhelp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

    @parametrize
    async def test_method_tuple_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_result=0,
            max_results=0,
        )
        assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

    @parametrize
    async def test_raw_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

    @parametrize
    async def test_streaming_response_tuple(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.tuple(
            columns="columns",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert_matches_type(EoObservationTupleResponse, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.observations.eo_observations.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )
        assert eo_observation is None

    @parametrize
    async def test_raw_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.observations.eo_observations.with_raw_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert eo_observation is None

    @parametrize
    async def test_streaming_response_unvalidated_publish(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.observations.eo_observations.with_streaming_response.unvalidated_publish(
            body=[
                {
                    "classification_marking": "U",
                    "data_mode": "TEST",
                    "ob_time": parse_datetime("2018-01-01T16:00:00.123456Z"),
                    "source": "Bluestaq",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True
