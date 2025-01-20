# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unifieddatalibrary import Unifieddatalibrary, AsyncUnifieddatalibrary
from unifieddatalibrary.types import (
    EoObservationListResponse,
)
from unifieddatalibrary._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEoObservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.eo_observations.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert eo_observation is None

    @parametrize
    def test_method_create_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.eo_observations.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            azimuth=0,
            azimuth_bias=0,
            azimuth_rate=0,
            azimuth_unc=0,
            bg_intensity=0,
            collect_method="collectMethod",
            corr_quality=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            declination=0,
            declination_bias=0,
            declination_rate=0,
            declination_unc=0,
            descriptor="descriptor",
            elevation=0,
            elevation_bias=0,
            elevation_rate=0,
            elevation_unc=0,
            eoobservation_details={
                "acal_cr_pix_x": 0,
                "acal_cr_pix_y": 0,
                "acal_cr_val_x": 0,
                "acal_cr_val_y": 0,
                "acal_num_stars": 0,
                "background_signal": 0,
                "background_signal_unc": 0,
                "binning_horiz": 0,
                "binning_vert": 0,
                "ccd_obj_pos_x": 0,
                "ccd_obj_pos_y": 0,
                "ccd_obj_width": 0,
                "ccd_temp": 0,
                "centroid_column": 0,
                "centroid_row": 0,
                "classification_marking": "classificationMarking",
                "color_coeffs": [0],
                "column_variance": 0,
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "current_neutral_density_filter_num": 0,
                "current_spectral_filter_num": 0,
                "data_mode": "dataMode",
                "declination_cov": 0,
                "dist_from_streak_center": [0],
                "does": 0,
                "extinction_coeffs": [0],
                "extinction_coeffs_unc": [0],
                "gain": 0,
                "id_eo_observation": "idEOObservation",
                "ifov": 0,
                "mag_instrumental": 0,
                "mag_instrumental_unc": 0,
                "neutral_density_filter_names": ["string"],
                "neutral_density_filter_transmissions": [0],
                "neutral_density_filter_transmissions_unc": [0],
                "num_catalog_stars": 0,
                "num_correlated_stars": 0,
                "num_detected_stars": 0,
                "num_neutral_density_filters": 0,
                "num_spectral_filters": 0,
                "obj_sun_range": 0,
                "ob_time": "2019-12-27T18:11:19.117Z",
                "optical_cross_section": 0,
                "optical_cross_section_unc": 0,
                "pcal_num_stars": 0,
                "peak_aperture_count": 0,
                "peak_background_count": 0,
                "phase_ang_bisect": 0,
                "pixel_array_height": 0,
                "pixel_array_width": 0,
                "pixel_max": 0,
                "pixel_min": 0,
                "predicted_azimuth": 0,
                "predicted_declination": 0,
                "predicted_declination_unc": 0,
                "predicted_elevation": 0,
                "predicted_ra": 0,
                "predicted_ra_unc": 0,
                "ra_cov": 0,
                "ra_declination_cov": 0,
                "row_col_cov": 0,
                "row_variance": 0,
                "snr_est": 0,
                "solar_disk_frac": 0,
                "source": "source",
                "spectral_filters": ["string"],
                "spectral_filter_solar_mag": [0],
                "spectral_zmfl": [0],
                "sun_azimuth": 0,
                "sun_elevation": 0,
                "sun_state_pos_x": 0,
                "sun_state_pos_y": 0,
                "sun_state_pos_z": 0,
                "sun_state_vel_x": 0,
                "sun_state_vel_y": 0,
                "sun_state_vel_z": 0,
                "surf_brightness": [0],
                "surf_brightness_unc": [0],
                "times_unc": 0,
                "toes": 0,
                "zero_points": [0],
                "zero_points_unc": [0],
            },
            exp_duration=0,
            fov_count=0,
            geoalt=0,
            geolat=0,
            geolon=0,
            georange=0,
            id_on_orbit="idOnOrbit",
            id_sensor="idSensor",
            id_sky_imagery="idSkyImagery",
            intensity=0,
            los_unc=0,
            losx=0,
            losxvel=0,
            losy=0,
            losyvel=0,
            losz=0,
            loszvel=0,
            mag=0,
            mag_norm_range=0,
            mag_unc=0,
            net_obj_sig=0,
            net_obj_sig_unc=0,
            ob_position="obPosition",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            penumbra=True,
            primary_extinction=0,
            primary_extinction_unc=0,
            ra=0,
            ra_bias=0,
            range=0,
            range_bias=0,
            range_rate=0,
            range_rate_unc=0,
            range_unc=0,
            ra_rate=0,
            ra_unc=0,
            raw_file_uri="rawFileURI",
            reference_frame="referenceFrame",
            sat_no=0,
            senalt=0,
            senlat=0,
            senlon=0,
            sen_quat=[0],
            sen_reference_frame="senReferenceFrame",
            senvelx=0,
            senvely=0,
            senvelz=0,
            senx=0,
            seny=0,
            senz=0,
            shutter_delay=0,
            sky_bkgrnd=0,
            solar_dec_angle=0,
            solar_eq_phase_angle=0,
            solar_phase_angle=0,
            source_dl="sourceDL",
            tags=["string"],
            task_id="taskId",
            timing_bias=0,
            track_id="trackId",
            transaction_id="transactionId",
            type="type",
            uct=True,
            umbra=True,
            zeroptd=0,
            zero_ptd_unc=0,
        )
        assert eo_observation is None

    @parametrize
    def test_raw_response_create(self, client: Unifieddatalibrary) -> None:
        response = client.eo_observations.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert eo_observation is None

    @parametrize
    def test_streaming_response_create(self, client: Unifieddatalibrary) -> None:
        with client.eo_observations.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.eo_observations.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EoObservationListResponse, eo_observation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unifieddatalibrary) -> None:
        response = client.eo_observations.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert_matches_type(EoObservationListResponse, eo_observation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unifieddatalibrary) -> None:
        with client.eo_observations.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert_matches_type(EoObservationListResponse, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.eo_observations.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    def test_raw_response_count(self, client: Unifieddatalibrary) -> None:
        response = client.eo_observations.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    def test_streaming_response_count(self, client: Unifieddatalibrary) -> None:
        with client.eo_observations.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = response.parse()
            assert_matches_type(str, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_bulk(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )
        assert eo_observation is None

    @parametrize
    def test_method_create_bulk_with_all_params(self, client: Unifieddatalibrary) -> None:
        eo_observation = client.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "id": "id",
                    "azimuth": 0,
                    "azimuth_bias": 0,
                    "azimuth_rate": 0,
                    "azimuth_unc": 0,
                    "bg_intensity": 0,
                    "collect_method": "collectMethod",
                    "corr_quality": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "declination": 0,
                    "declination_bias": 0,
                    "declination_rate": 0,
                    "declination_unc": 0,
                    "descriptor": "descriptor",
                    "elevation": 0,
                    "elevation_bias": 0,
                    "elevation_rate": 0,
                    "elevation_unc": 0,
                    "eoobservation_details": {
                        "acal_cr_pix_x": 0,
                        "acal_cr_pix_y": 0,
                        "acal_cr_val_x": 0,
                        "acal_cr_val_y": 0,
                        "acal_num_stars": 0,
                        "background_signal": 0,
                        "background_signal_unc": 0,
                        "binning_horiz": 0,
                        "binning_vert": 0,
                        "ccd_obj_pos_x": 0,
                        "ccd_obj_pos_y": 0,
                        "ccd_obj_width": 0,
                        "ccd_temp": 0,
                        "centroid_column": 0,
                        "centroid_row": 0,
                        "classification_marking": "classificationMarking",
                        "color_coeffs": [0],
                        "column_variance": 0,
                        "created_at": "2019-12-27T18:11:19.117Z",
                        "created_by": "createdBy",
                        "current_neutral_density_filter_num": 0,
                        "current_spectral_filter_num": 0,
                        "data_mode": "dataMode",
                        "declination_cov": 0,
                        "dist_from_streak_center": [0],
                        "does": 0,
                        "extinction_coeffs": [0],
                        "extinction_coeffs_unc": [0],
                        "gain": 0,
                        "id_eo_observation": "idEOObservation",
                        "ifov": 0,
                        "mag_instrumental": 0,
                        "mag_instrumental_unc": 0,
                        "neutral_density_filter_names": ["string"],
                        "neutral_density_filter_transmissions": [0],
                        "neutral_density_filter_transmissions_unc": [0],
                        "num_catalog_stars": 0,
                        "num_correlated_stars": 0,
                        "num_detected_stars": 0,
                        "num_neutral_density_filters": 0,
                        "num_spectral_filters": 0,
                        "obj_sun_range": 0,
                        "ob_time": "2019-12-27T18:11:19.117Z",
                        "optical_cross_section": 0,
                        "optical_cross_section_unc": 0,
                        "pcal_num_stars": 0,
                        "peak_aperture_count": 0,
                        "peak_background_count": 0,
                        "phase_ang_bisect": 0,
                        "pixel_array_height": 0,
                        "pixel_array_width": 0,
                        "pixel_max": 0,
                        "pixel_min": 0,
                        "predicted_azimuth": 0,
                        "predicted_declination": 0,
                        "predicted_declination_unc": 0,
                        "predicted_elevation": 0,
                        "predicted_ra": 0,
                        "predicted_ra_unc": 0,
                        "ra_cov": 0,
                        "ra_declination_cov": 0,
                        "row_col_cov": 0,
                        "row_variance": 0,
                        "snr_est": 0,
                        "solar_disk_frac": 0,
                        "source": "source",
                        "spectral_filters": ["string"],
                        "spectral_filter_solar_mag": [0],
                        "spectral_zmfl": [0],
                        "sun_azimuth": 0,
                        "sun_elevation": 0,
                        "sun_state_pos_x": 0,
                        "sun_state_pos_y": 0,
                        "sun_state_pos_z": 0,
                        "sun_state_vel_x": 0,
                        "sun_state_vel_y": 0,
                        "sun_state_vel_z": 0,
                        "surf_brightness": [0],
                        "surf_brightness_unc": [0],
                        "times_unc": 0,
                        "toes": 0,
                        "zero_points": [0],
                        "zero_points_unc": [0],
                    },
                    "exp_duration": 0,
                    "fov_count": 0,
                    "geoalt": 0,
                    "geolat": 0,
                    "geolon": 0,
                    "georange": 0,
                    "id_on_orbit": "idOnOrbit",
                    "id_sensor": "idSensor",
                    "id_sky_imagery": "idSkyImagery",
                    "intensity": 0,
                    "los_unc": 0,
                    "losx": 0,
                    "losxvel": 0,
                    "losy": 0,
                    "losyvel": 0,
                    "losz": 0,
                    "loszvel": 0,
                    "mag": 0,
                    "mag_norm_range": 0,
                    "mag_unc": 0,
                    "net_obj_sig": 0,
                    "net_obj_sig_unc": 0,
                    "ob_position": "obPosition",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "orig_object_id": "origObjectId",
                    "orig_sensor_id": "origSensorId",
                    "penumbra": True,
                    "primary_extinction": 0,
                    "primary_extinction_unc": 0,
                    "ra": 0,
                    "ra_bias": 0,
                    "range": 0,
                    "range_bias": 0,
                    "range_rate": 0,
                    "range_rate_unc": 0,
                    "range_unc": 0,
                    "ra_rate": 0,
                    "ra_unc": 0,
                    "raw_file_uri": "rawFileURI",
                    "reference_frame": "referenceFrame",
                    "sat_no": 0,
                    "senalt": 0,
                    "senlat": 0,
                    "senlon": 0,
                    "sen_quat": [0],
                    "sen_reference_frame": "senReferenceFrame",
                    "senvelx": 0,
                    "senvely": 0,
                    "senvelz": 0,
                    "senx": 0,
                    "seny": 0,
                    "senz": 0,
                    "shutter_delay": 0,
                    "sky_bkgrnd": 0,
                    "solar_dec_angle": 0,
                    "solar_eq_phase_angle": 0,
                    "solar_phase_angle": 0,
                    "source_dl": "sourceDL",
                    "tags": ["string"],
                    "task_id": "taskId",
                    "timing_bias": 0,
                    "track_id": "trackId",
                    "transaction_id": "transactionId",
                    "type": "type",
                    "uct": True,
                    "umbra": True,
                    "zeroptd": 0,
                    "zero_ptd_unc": 0,
                }
            ],
            convert_to_j2_k=True,
        )
        assert eo_observation is None

    @parametrize
    def test_raw_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        response = client.eo_observations.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = response.parse()
        assert eo_observation is None

    @parametrize
    def test_streaming_response_create_bulk(self, client: Unifieddatalibrary) -> None:
        with client.eo_observations.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
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
        eo_observation = await async_client.eo_observations.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )
        assert eo_observation is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.eo_observations.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
            id="id",
            azimuth=0,
            azimuth_bias=0,
            azimuth_rate=0,
            azimuth_unc=0,
            bg_intensity=0,
            collect_method="collectMethod",
            corr_quality=0,
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="createdBy",
            declination=0,
            declination_bias=0,
            declination_rate=0,
            declination_unc=0,
            descriptor="descriptor",
            elevation=0,
            elevation_bias=0,
            elevation_rate=0,
            elevation_unc=0,
            eoobservation_details={
                "acal_cr_pix_x": 0,
                "acal_cr_pix_y": 0,
                "acal_cr_val_x": 0,
                "acal_cr_val_y": 0,
                "acal_num_stars": 0,
                "background_signal": 0,
                "background_signal_unc": 0,
                "binning_horiz": 0,
                "binning_vert": 0,
                "ccd_obj_pos_x": 0,
                "ccd_obj_pos_y": 0,
                "ccd_obj_width": 0,
                "ccd_temp": 0,
                "centroid_column": 0,
                "centroid_row": 0,
                "classification_marking": "classificationMarking",
                "color_coeffs": [0],
                "column_variance": 0,
                "created_at": "2019-12-27T18:11:19.117Z",
                "created_by": "createdBy",
                "current_neutral_density_filter_num": 0,
                "current_spectral_filter_num": 0,
                "data_mode": "dataMode",
                "declination_cov": 0,
                "dist_from_streak_center": [0],
                "does": 0,
                "extinction_coeffs": [0],
                "extinction_coeffs_unc": [0],
                "gain": 0,
                "id_eo_observation": "idEOObservation",
                "ifov": 0,
                "mag_instrumental": 0,
                "mag_instrumental_unc": 0,
                "neutral_density_filter_names": ["string"],
                "neutral_density_filter_transmissions": [0],
                "neutral_density_filter_transmissions_unc": [0],
                "num_catalog_stars": 0,
                "num_correlated_stars": 0,
                "num_detected_stars": 0,
                "num_neutral_density_filters": 0,
                "num_spectral_filters": 0,
                "obj_sun_range": 0,
                "ob_time": "2019-12-27T18:11:19.117Z",
                "optical_cross_section": 0,
                "optical_cross_section_unc": 0,
                "pcal_num_stars": 0,
                "peak_aperture_count": 0,
                "peak_background_count": 0,
                "phase_ang_bisect": 0,
                "pixel_array_height": 0,
                "pixel_array_width": 0,
                "pixel_max": 0,
                "pixel_min": 0,
                "predicted_azimuth": 0,
                "predicted_declination": 0,
                "predicted_declination_unc": 0,
                "predicted_elevation": 0,
                "predicted_ra": 0,
                "predicted_ra_unc": 0,
                "ra_cov": 0,
                "ra_declination_cov": 0,
                "row_col_cov": 0,
                "row_variance": 0,
                "snr_est": 0,
                "solar_disk_frac": 0,
                "source": "source",
                "spectral_filters": ["string"],
                "spectral_filter_solar_mag": [0],
                "spectral_zmfl": [0],
                "sun_azimuth": 0,
                "sun_elevation": 0,
                "sun_state_pos_x": 0,
                "sun_state_pos_y": 0,
                "sun_state_pos_z": 0,
                "sun_state_vel_x": 0,
                "sun_state_vel_y": 0,
                "sun_state_vel_z": 0,
                "surf_brightness": [0],
                "surf_brightness_unc": [0],
                "times_unc": 0,
                "toes": 0,
                "zero_points": [0],
                "zero_points_unc": [0],
            },
            exp_duration=0,
            fov_count=0,
            geoalt=0,
            geolat=0,
            geolon=0,
            georange=0,
            id_on_orbit="idOnOrbit",
            id_sensor="idSensor",
            id_sky_imagery="idSkyImagery",
            intensity=0,
            los_unc=0,
            losx=0,
            losxvel=0,
            losy=0,
            losyvel=0,
            losz=0,
            loszvel=0,
            mag=0,
            mag_norm_range=0,
            mag_unc=0,
            net_obj_sig=0,
            net_obj_sig_unc=0,
            ob_position="obPosition",
            origin="origin",
            orig_network="origNetwork",
            orig_object_id="origObjectId",
            orig_sensor_id="origSensorId",
            penumbra=True,
            primary_extinction=0,
            primary_extinction_unc=0,
            ra=0,
            ra_bias=0,
            range=0,
            range_bias=0,
            range_rate=0,
            range_rate_unc=0,
            range_unc=0,
            ra_rate=0,
            ra_unc=0,
            raw_file_uri="rawFileURI",
            reference_frame="referenceFrame",
            sat_no=0,
            senalt=0,
            senlat=0,
            senlon=0,
            sen_quat=[0],
            sen_reference_frame="senReferenceFrame",
            senvelx=0,
            senvely=0,
            senvelz=0,
            senx=0,
            seny=0,
            senz=0,
            shutter_delay=0,
            sky_bkgrnd=0,
            solar_dec_angle=0,
            solar_eq_phase_angle=0,
            solar_phase_angle=0,
            source_dl="sourceDL",
            tags=["string"],
            task_id="taskId",
            timing_bias=0,
            track_id="trackId",
            transaction_id="transactionId",
            type="type",
            uct=True,
            umbra=True,
            zeroptd=0,
            zero_ptd_unc=0,
        )
        assert eo_observation is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eo_observations.with_raw_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert eo_observation is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eo_observations.with_streaming_response.create(
            classification_marking="classificationMarking",
            data_mode="dataMode",
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.eo_observations.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EoObservationListResponse, eo_observation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eo_observations.with_raw_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert_matches_type(EoObservationListResponse, eo_observation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eo_observations.with_streaming_response.list(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert_matches_type(EoObservationListResponse, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.eo_observations.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eo_observations.with_raw_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert_matches_type(str, eo_observation, path=["response"])

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eo_observations.with_streaming_response.count(
            ob_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert_matches_type(str, eo_observation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )
        assert eo_observation is None

    @parametrize
    async def test_method_create_bulk_with_all_params(self, async_client: AsyncUnifieddatalibrary) -> None:
        eo_observation = await async_client.eo_observations.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                    "id": "id",
                    "azimuth": 0,
                    "azimuth_bias": 0,
                    "azimuth_rate": 0,
                    "azimuth_unc": 0,
                    "bg_intensity": 0,
                    "collect_method": "collectMethod",
                    "corr_quality": 0,
                    "created_at": "2019-12-27T18:11:19.117Z",
                    "created_by": "createdBy",
                    "declination": 0,
                    "declination_bias": 0,
                    "declination_rate": 0,
                    "declination_unc": 0,
                    "descriptor": "descriptor",
                    "elevation": 0,
                    "elevation_bias": 0,
                    "elevation_rate": 0,
                    "elevation_unc": 0,
                    "eoobservation_details": {
                        "acal_cr_pix_x": 0,
                        "acal_cr_pix_y": 0,
                        "acal_cr_val_x": 0,
                        "acal_cr_val_y": 0,
                        "acal_num_stars": 0,
                        "background_signal": 0,
                        "background_signal_unc": 0,
                        "binning_horiz": 0,
                        "binning_vert": 0,
                        "ccd_obj_pos_x": 0,
                        "ccd_obj_pos_y": 0,
                        "ccd_obj_width": 0,
                        "ccd_temp": 0,
                        "centroid_column": 0,
                        "centroid_row": 0,
                        "classification_marking": "classificationMarking",
                        "color_coeffs": [0],
                        "column_variance": 0,
                        "created_at": "2019-12-27T18:11:19.117Z",
                        "created_by": "createdBy",
                        "current_neutral_density_filter_num": 0,
                        "current_spectral_filter_num": 0,
                        "data_mode": "dataMode",
                        "declination_cov": 0,
                        "dist_from_streak_center": [0],
                        "does": 0,
                        "extinction_coeffs": [0],
                        "extinction_coeffs_unc": [0],
                        "gain": 0,
                        "id_eo_observation": "idEOObservation",
                        "ifov": 0,
                        "mag_instrumental": 0,
                        "mag_instrumental_unc": 0,
                        "neutral_density_filter_names": ["string"],
                        "neutral_density_filter_transmissions": [0],
                        "neutral_density_filter_transmissions_unc": [0],
                        "num_catalog_stars": 0,
                        "num_correlated_stars": 0,
                        "num_detected_stars": 0,
                        "num_neutral_density_filters": 0,
                        "num_spectral_filters": 0,
                        "obj_sun_range": 0,
                        "ob_time": "2019-12-27T18:11:19.117Z",
                        "optical_cross_section": 0,
                        "optical_cross_section_unc": 0,
                        "pcal_num_stars": 0,
                        "peak_aperture_count": 0,
                        "peak_background_count": 0,
                        "phase_ang_bisect": 0,
                        "pixel_array_height": 0,
                        "pixel_array_width": 0,
                        "pixel_max": 0,
                        "pixel_min": 0,
                        "predicted_azimuth": 0,
                        "predicted_declination": 0,
                        "predicted_declination_unc": 0,
                        "predicted_elevation": 0,
                        "predicted_ra": 0,
                        "predicted_ra_unc": 0,
                        "ra_cov": 0,
                        "ra_declination_cov": 0,
                        "row_col_cov": 0,
                        "row_variance": 0,
                        "snr_est": 0,
                        "solar_disk_frac": 0,
                        "source": "source",
                        "spectral_filters": ["string"],
                        "spectral_filter_solar_mag": [0],
                        "spectral_zmfl": [0],
                        "sun_azimuth": 0,
                        "sun_elevation": 0,
                        "sun_state_pos_x": 0,
                        "sun_state_pos_y": 0,
                        "sun_state_pos_z": 0,
                        "sun_state_vel_x": 0,
                        "sun_state_vel_y": 0,
                        "sun_state_vel_z": 0,
                        "surf_brightness": [0],
                        "surf_brightness_unc": [0],
                        "times_unc": 0,
                        "toes": 0,
                        "zero_points": [0],
                        "zero_points_unc": [0],
                    },
                    "exp_duration": 0,
                    "fov_count": 0,
                    "geoalt": 0,
                    "geolat": 0,
                    "geolon": 0,
                    "georange": 0,
                    "id_on_orbit": "idOnOrbit",
                    "id_sensor": "idSensor",
                    "id_sky_imagery": "idSkyImagery",
                    "intensity": 0,
                    "los_unc": 0,
                    "losx": 0,
                    "losxvel": 0,
                    "losy": 0,
                    "losyvel": 0,
                    "losz": 0,
                    "loszvel": 0,
                    "mag": 0,
                    "mag_norm_range": 0,
                    "mag_unc": 0,
                    "net_obj_sig": 0,
                    "net_obj_sig_unc": 0,
                    "ob_position": "obPosition",
                    "origin": "origin",
                    "orig_network": "origNetwork",
                    "orig_object_id": "origObjectId",
                    "orig_sensor_id": "origSensorId",
                    "penumbra": True,
                    "primary_extinction": 0,
                    "primary_extinction_unc": 0,
                    "ra": 0,
                    "ra_bias": 0,
                    "range": 0,
                    "range_bias": 0,
                    "range_rate": 0,
                    "range_rate_unc": 0,
                    "range_unc": 0,
                    "ra_rate": 0,
                    "ra_unc": 0,
                    "raw_file_uri": "rawFileURI",
                    "reference_frame": "referenceFrame",
                    "sat_no": 0,
                    "senalt": 0,
                    "senlat": 0,
                    "senlon": 0,
                    "sen_quat": [0],
                    "sen_reference_frame": "senReferenceFrame",
                    "senvelx": 0,
                    "senvely": 0,
                    "senvelz": 0,
                    "senx": 0,
                    "seny": 0,
                    "senz": 0,
                    "shutter_delay": 0,
                    "sky_bkgrnd": 0,
                    "solar_dec_angle": 0,
                    "solar_eq_phase_angle": 0,
                    "solar_phase_angle": 0,
                    "source_dl": "sourceDL",
                    "tags": ["string"],
                    "task_id": "taskId",
                    "timing_bias": 0,
                    "track_id": "trackId",
                    "transaction_id": "transactionId",
                    "type": "type",
                    "uct": True,
                    "umbra": True,
                    "zeroptd": 0,
                    "zero_ptd_unc": 0,
                }
            ],
            convert_to_j2_k=True,
        )
        assert eo_observation is None

    @parametrize
    async def test_raw_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        response = await async_client.eo_observations.with_raw_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eo_observation = await response.parse()
        assert eo_observation is None

    @parametrize
    async def test_streaming_response_create_bulk(self, async_client: AsyncUnifieddatalibrary) -> None:
        async with async_client.eo_observations.with_streaming_response.create_bulk(
            body=[
                {
                    "classification_marking": "classificationMarking",
                    "data_mode": "dataMode",
                    "ob_time": "2019-12-27T18:11:19.117Z",
                    "source": "source",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eo_observation = await response.parse()
            assert eo_observation is None

        assert cast(Any, response.is_closed) is True
